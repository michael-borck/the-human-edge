#!/usr/bin/env python3
"""Load-test and analysis-test a local model server before offering it to a class.

Talks straight to the model server (Ollama's native API, or any OpenAI-compatible
endpoint), not to LibreChat, so the numbers are the model's, not the web app's.
Standard library only.

LOAD TEST: N simulated participants press Enter at the same moment.

    python3 loadtest.py --model gemma4:12b --users 25
    python3 loadtest.py --model gemma4:12b --users 25 --prompt csv      # the Exercise 5 paste
    python3 loadtest.py --model gemma4:12b --users 25 --stagger 20      # arrivals spread over 20 s
    python3 loadtest.py --base-url http://myserver:11434 --model qwen3.5:4b --users 25

ANALYSIS TEST: can it answer the RetailFlow questions from the pasted CSV?
Every answer is compared with the true figure, computed from the CSV here.

    python3 loadtest.py --model gemma4:12b --analysis

Thinking is sent as off (think: false), to match a class setup with thinking
turned off. Use --think on to compare, or --think omit for models without it.
For an OpenAI-compatible server use --api openai (and --api-key if it needs one).
"""
import argparse
import csv
import json
import pathlib
import random
import re
import statistics
import string
import threading
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_CSV = HERE.parent.parent / "data" / "retailflow-customer-service-data.csv"

SHORT = "In three sentences, what should a new team leader do in their first week?"
BRIEF = (
    "ROLE: Senior project manager. Plain-spoken and warm.\n"
    "TASK: Write to the client about a two-week delivery delay.\n"
    "CONTEXT: A vendor's API integration ran late. The client values transparency and the "
    "relationship is good. New date: 15 March.\n"
    "FORMAT: Under 200 words. Acknowledge, explain, new date, recommit."
)
CSV_ASK = "Describe this dataset: number of rows, columns, date range, and anything that looks incomplete. Don't analyse it yet."


def nonce():
    """A random first line, so the server can't reuse a cached prompt between users."""
    return "Request " + "".join(random.choices(string.ascii_lowercase, k=8)) + ".\n"


def build_prompt(kind, csv_text, rows):
    if kind == "short":
        return SHORT
    if kind == "brief":
        return BRIEF
    if kind == "csv":
        lines = csv_text.splitlines()
        part = "\n".join(lines[: rows + 1])
        return f"{CSV_ASK}\n\n{part}"
    raise ValueError(kind)


def stream_request(args, prompt, think, max_tokens):
    """Send one streamed chat request. Returns a dict of timings and counts."""
    t0 = time.perf_counter()
    out = {"ok": False, "ttft": None, "total": None, "out_tokens": 0, "prompt_tokens": None,
           "text": "", "error": None}
    if args.api == "ollama":
        url = args.base_url.rstrip("/") + "/api/chat"
        body = {"model": args.model, "messages": [{"role": "user", "content": prompt}],
                "stream": True, "keep_alive": "30m", "options": {"num_predict": max_tokens}}
        if args.num_ctx:
            body["options"]["num_ctx"] = args.num_ctx
        if think != "omit":
            body["think"] = think == "on"
    else:
        url = args.base_url.rstrip("/") + "/v1/chat/completions"
        body = {"model": args.model, "messages": [{"role": "user", "content": prompt}],
                "stream": True, "max_tokens": max_tokens,
                "stream_options": {"include_usage": True}}
    headers = {"Content-Type": "application/json"}
    if args.api_key:
        headers["Authorization"] = "Bearer " + args.api_key
    req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=args.timeout) as resp:
            for raw in resp:
                line = raw.decode("utf-8", "replace").strip()
                if not line:
                    continue
                if args.api == "openai":
                    if not line.startswith("data:"):
                        continue
                    line = line[5:].strip()
                    if line == "[DONE]":
                        break
                chunk = json.loads(line)
                if args.api == "ollama":
                    if chunk.get("error"):
                        raise RuntimeError(chunk["error"])
                    piece = chunk.get("message", {}).get("content", "")
                    if chunk.get("done"):
                        out["out_tokens"] = chunk.get("eval_count", out["out_tokens"])
                        out["prompt_tokens"] = chunk.get("prompt_eval_count")
                else:
                    choices = chunk.get("choices") or []
                    piece = (choices[0].get("delta", {}).get("content") or "") if choices else ""
                    if chunk.get("usage"):
                        out["out_tokens"] = chunk["usage"].get("completion_tokens", out["out_tokens"])
                        out["prompt_tokens"] = chunk["usage"].get("prompt_tokens")
                    elif piece:
                        out["out_tokens"] += 1
                if piece and out["ttft"] is None:
                    out["ttft"] = time.perf_counter() - t0
                out["text"] += piece
        out["ok"] = True
    except urllib.error.HTTPError as e:
        out["error"] = f"HTTP {e.code}: {e.read().decode('utf-8', 'replace')[:200]}"
    except Exception as e:  # timeouts, refused connections, server errors
        out["error"] = f"{type(e).__name__}: {e}"
    out["total"] = time.perf_counter() - t0
    return out


def pct(values, p):
    if not values:
        return float("nan")
    values = sorted(values)
    k = (len(values) - 1) * p / 100
    lo, hi = int(k), min(int(k) + 1, len(values) - 1)
    return values[lo] + (values[hi] - values[lo]) * (k - lo)


def resolve_think(args):
    """Ollama rejects think for models that can't think; fall back to omitting it."""
    if args.api != "ollama" or args.think == "omit":
        return args.think
    probe = stream_request(args, "Say OK.", args.think, 5)
    if probe["error"] and "think" in probe["error"].lower():
        print("  note: this model doesn't support thinking; sending requests without the think flag")
        return "omit"
    return args.think


def load_test(args):
    csv_text = pathlib.Path(args.csv).read_text(encoding="utf-8")
    kinds = ["short", "brief", "csv"] if args.prompt == "mix" else [args.prompt]
    print(f"Warming up {args.model} at {args.base_url} ...")
    think = resolve_think(args)
    warm = stream_request(args, "Say OK.", think, 5)
    if not warm["ok"]:
        print("  warm-up failed:", warm["error"])
        return
    print(f"  ready ({warm['total']:.1f} s)\n")

    results = [None] * args.users
    barrier = threading.Barrier(args.users)

    def user(i):
        kind = kinds[i % len(kinds)]
        prompt = nonce() + build_prompt(kind, csv_text, args.csv_rows)
        barrier.wait()
        if args.stagger:
            time.sleep(random.uniform(0, args.stagger))
        r = stream_request(args, prompt, think, args.max_tokens)
        r["kind"], r["est_prompt_tokens"] = kind, len(prompt) // 4
        results[i] = r

    print(f"{args.users} users, prompt '{args.prompt}', thinking {think}, up to {args.max_tokens} tokens each"
          + (f", arrivals spread over {args.stagger} s" if args.stagger else ", all at once"))
    wall0 = time.perf_counter()
    threads = [threading.Thread(target=user, args=(i,)) for i in range(args.users)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    wall = time.perf_counter() - wall0

    ok = [r for r in results if r["ok"]]
    bad = [r for r in results if not r["ok"]]
    print(f"\n{'#':>3} {'prompt':<6} {'first word':>10} {'done':>7} {'tokens':>6} {'tok/s':>6}  note")
    for i, r in enumerate(results):
        if not r["ok"]:
            print(f"{i + 1:>3} {r['kind']:<6} {'':>10} {r['total']:>6.1f}s {'':>6} {'':>6}  FAILED {r['error']}")
            continue
        gen = r["total"] - (r["ttft"] or 0)
        tps = r["out_tokens"] / gen if gen > 0 and r["out_tokens"] else 0
        note = ""
        if r["prompt_tokens"] and r["prompt_tokens"] < 0.6 * r["est_prompt_tokens"]:
            note = f"prompt CUT: server saw {r['prompt_tokens']} of ~{r['est_prompt_tokens']} tokens"
        ttft = f"{r['ttft']:.1f}s" if r["ttft"] is not None else "-"
        print(f"{i + 1:>3} {r['kind']:<6} {ttft:>10} {r['total']:>6.1f}s {r['out_tokens']:>6} {tps:>6.1f}  {note}")

    ttfts = [r["ttft"] for r in ok if r["ttft"] is not None]
    tps_each = [r["out_tokens"] / (r["total"] - r["ttft"]) for r in ok
                if r["ttft"] is not None and r["total"] > r["ttft"] and r["out_tokens"]]
    total_tokens = sum(r["out_tokens"] for r in ok)
    print("\nSummary")
    print(f"  completed {len(ok)} of {args.users}, failed {len(bad)}, wall time {wall:.1f} s")
    if ttfts:
        print(f"  wait for first word: median {pct(ttfts, 50):.1f} s, 90th percentile {pct(ttfts, 90):.1f} s, worst {max(ttfts):.1f} s")
    if tps_each:
        print(f"  writing speed per person: median {statistics.median(tps_each):.1f} tokens/s (reading speed is about 5 to 8)")
    print(f"  whole server: {total_tokens / wall:.1f} tokens/s")
    cut = [r for r in ok if r["prompt_tokens"] and r["prompt_tokens"] < 0.6 * r["est_prompt_tokens"]]
    if cut:
        print(f"  WARNING: {len(cut)} prompts were cut short. Raise the context length (num_ctx) on the server.")
    p90 = pct(ttfts, 90) if ttfts else float("inf")
    verdict = ("good: people will barely notice the queue" if p90 < 10 and not bad else
               "usable: some will wait, warn the room" if p90 < 30 and len(bad) <= args.users // 10 else
               "struggling: try a smaller model, fewer parallel slots, or don't offer it for this exercise")
    print(f"  verdict: {verdict}")


def truth(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8")))
    def avg(xs):
        return sum(xs) / len(xs)
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["category"], []).append(float(r["satisfaction_score"]))
    low = min(by_cat, key=lambda c: avg(by_cat[c]))
    chan = lambda c: avg([float(r["response_time_hours"]) for r in rows if r["channel"] == c])
    sunday = avg([float(r["response_time_hours"]) for r in rows if r["day_of_week"] == "Sunday"])
    overall = avg([float(r["response_time_hours"]) for r in rows])
    return [
        ("How many rows of data are there?", str(len(rows)), [len(rows)]),
        ("Which category has the lowest average satisfaction score, and what is that average?",
         f"{low}, {avg(by_cat[low]):.2f}", [round(avg(by_cat[low]), 1)], low),
        ("What is the average response time in hours for Email, and for Live Chat?",
         f"Email {chan('Email'):.1f}, Live Chat {chan('Live Chat'):.1f}", [round(chan("Email"), 1), round(chan("Live Chat"), 1)]),
        ("What is the average response time in hours on Sundays, and overall?",
         f"Sunday {sunday:.1f}, overall {overall:.2f}", [round(sunday, 1), round(overall, 1)]),
    ]


def analysis_test(args):
    csv_text = pathlib.Path(args.csv).read_text(encoding="utf-8")
    think = resolve_think(args)
    checks = truth(args.csv)
    questions = "\n".join(f"{i + 1}. {c[0]}" for i, c in enumerate(checks))
    prompt = (f"Here is a CSV file of customer service tickets.\n\n{csv_text}\n\n"
              f"Answer these questions from the data. Give each number to one decimal place.\n{questions}")
    est = len(prompt) // 4
    print(f"Analysis test: whole RetailFlow CSV (~{est} tokens) plus {len(checks)} questions, thinking {think}")
    r = stream_request(args, prompt, think, 800)
    if not r["ok"]:
        print("  failed:", r["error"])
        return
    if r["prompt_tokens"]:
        seen = r["prompt_tokens"]
        flag = "  <-- CUT: most of the CSV never reached the model. Raise num_ctx." if seen < 0.6 * est else ""
        print(f"  the server read {seen} prompt tokens of ~{est}{flag}")
    print(f"  answered in {r['total']:.1f} s\n\n--- model's answer ---\n{r['text'].strip()}\n--- end ---\n")
    numbers = [float(n) for n in re.findall(r"\d+(?:\.\d+)?", r["text"])]
    score = 0
    for i, c in enumerate(checks):
        targets = c[2]
        hit = all(any(abs(n - t) <= 0.15 for n in numbers) for t in targets)
        if len(c) > 3:
            hit = hit and c[3].lower() in r["text"].lower()
        score += hit
        print(f"  Q{i + 1} {'right' if hit else 'WRONG':<6} true answer: {c[1]}")
    print(f"\n  {score} of {len(checks)} right. A chat model without code execution reads the rows as text,")
    print("  so expect counting and averaging errors. For data work, have it write the formula or script instead (prompt 14).")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base-url", default="http://localhost:11434", help="model server (default: local Ollama)")
    ap.add_argument("--api", choices=["ollama", "openai"], default="ollama")
    ap.add_argument("--api-key", default="")
    ap.add_argument("--model", required=True)
    ap.add_argument("--users", type=int, default=25, help="simulated participants (default 25)")
    ap.add_argument("--prompt", choices=["short", "brief", "csv", "mix"], default="mix",
                    help="what each user sends (default: a mix of all three)")
    ap.add_argument("--csv-rows", type=int, default=60, help="rows of RetailFlow pasted in the csv prompt (default 60)")
    ap.add_argument("--stagger", type=float, default=0, help="spread arrivals over this many seconds (default 0: all at once)")
    ap.add_argument("--max-tokens", type=int, default=300, help="answer length cap per request (default 300)")
    ap.add_argument("--num-ctx", type=int, default=0, help="Ollama context length to request (default: server's setting)")
    ap.add_argument("--think", choices=["off", "on", "omit"], default="off")
    ap.add_argument("--timeout", type=float, default=300)
    ap.add_argument("--csv", default=str(DEFAULT_CSV))
    ap.add_argument("--analysis", action="store_true", help="run the analysis test instead of the load test")
    args = ap.parse_args()
    analysis_test(args) if args.analysis else load_test(args)


if __name__ == "__main__":
    main()
