#!/usr/bin/env python3
"""Build a clean, print-optimised participant workbook PDF.

Converts the morning worksheets, initiative cards and afternoon sprint
worksheets (plus a trust-tool quick reference) into one paginated PDF with no
navbar/chatbot/footer clutter — for printing as a handout. Source order tracks
the day: reference → morning → initiatives → afternoon sprints.

Usage:  python3 scripts/build-packet.py
Output: content/the-human-edge-participant-workbook.pdf
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "content" / "the-human-edge-participant-workbook.pdf"

# (path, section label) in day order
SECTIONS = [
    # Quick reference (every worksheet leans on it)
    ("handouts/frameworks/frameworks-trust-tool.md", "Quick reference"),
    # Morning — personal practice
    ("activities/morning/prompt-library.md", "Morning"),
    ("activities/morning/workflow-redesign.md", "Morning"),
    # The four scenarios (one per group)
    ("activities/initiative-cards/customer-service-chatbot.md", "Your initiative"),
    ("activities/initiative-cards/dynamic-pricing.md", "Your initiative"),
    ("activities/initiative-cards/fraud-detection.md", "Your initiative"),
    ("activities/initiative-cards/inventory-optimisation.md", "Your initiative"),
    # Afternoon — delivery sprints
    ("activities/worksheets/sprint-1-scope.md", "Afternoon"),
    ("activities/worksheets/sprint-2-stakeholders-hitl.md", "Afternoon"),
    ("activities/worksheets/sprint-3-roadmap-risk.md", "Afternoon"),
]

FRONT = """<h1 class="cover-title">The Human Edge</h1>
<p class="cover-sub">Using and Delivering AI with Judgement</p>
<p class="cover-meta">Participant workbook &middot; One-day masterclass<br>Dr Michael Borck &middot; Curtin Executive Education</p>
<table class="schedule">
<caption>The day at a glance</caption>
<tr><th>Time</th><th>Block</th></tr>
<tr><td>9:00&ndash;10:30</td><td>The average, the tool, the edge</td></tr>
<tr><td>10:30&ndash;11:00</td><td><em>Morning tea</em></td></tr>
<tr><td>11:00&ndash;12:30</td><td>Using AI well, yourself</td></tr>
<tr><td>12:30&ndash;1:15</td><td><em>Lunch</em></td></tr>
<tr><td>1:15&ndash;2:30</td><td>Why AI delivery is different</td></tr>
<tr><td>2:30&ndash;3:00</td><td><em>Afternoon tea</em></td></tr>
<tr><td>3:00&ndash;4:00</td><td>Designing the human in, then shipping</td></tr>
<tr><td>4:00&ndash;4:30</td><td>The edge that&rsquo;s left to humans</td></tr>
</table>
<p class="access"><strong>RetailFlow portal access code:</strong> pilot2024 &nbsp;(afternoon sprints only &mdash; your facilitator will confirm)</p>
<p class="access">This workbook is also available online at<br><strong>michael-borck.github.io/the-human-edge</strong></p>
"""

CSS = """
@page { size: A4; margin: 16mm 17mm; }
@page :first { margin: 28mm 17mm 20mm; }
* { box-sizing: border-box; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; color: #1a1a1a;
       font-size: 10.5pt; line-height: 1.45; }
.cover-title { font-size: 30pt; margin: 0 0 2pt; color: #14304a; letter-spacing: -.5px; }
.cover-sub { font-size: 14pt; color: #555; margin: 0 0 26mm; font-weight: 600; }
.cover-meta { font-size: 10pt; color: #444; margin: 0 0 10mm; }
.schedule { width: 100%; border-collapse: collapse; margin: 0 0 10mm; font-size: 10pt; }
.schedule caption { caption-side: top; text-align: left; font-weight: 700; color:#14304a;
                    font-size: 11pt; margin-bottom: 6px; }
.schedule th, .schedule td { border: 1px solid #ccc; padding: 5px 9px; text-align: left; }
.schedule th { background: #f1f5f9; }
.access { font-size: 9.5pt; color: #444; margin: 4mm 0; }
h1 { font-size: 16pt; color: #14304a; border-bottom: 2.5px solid #14304a; padding-bottom: 3px;
     margin: 0 0 8px; }
h2 { font-size: 12.5pt; color: #1d4e7a; margin: 14px 0 4px; }
h3 { font-size: 11pt; color: #333; margin: 11px 0 3px; }
p { margin: 4px 0; }
section { page-break-before: always; }
.kicker { font-size: 8.5pt; letter-spacing: 1.2px; text-transform: uppercase;
          color: #2a8; font-weight: 700; margin-bottom: 1px; }
ul, ol { margin: 4px 0 6px; padding-left: 20px; }
li { margin: 2px 0; }
table { width: 100%; border-collapse: collapse; margin: 6px 0 10px; font-size: 9.8pt; }
th, td { border: 1px solid #bbb; padding: 5px 7px; text-align: left; vertical-align: top; }
th { background: #eef3f8; }
blockquote { margin: 6px 0; padding: 7px 12px; background: #f6f8fa;
             border-left: 3px solid #2a8; color: #333; font-size: 10pt; }
/* Quarto callout fenced-divs → light boxes */
.callout, .callout-tip, .callout-note, .callout-important { margin: 7px 0; padding: 8px 12px;
    background: #fff8e6; border: 1px solid #e6cf8a; border-radius: 3px; font-size: 9.8pt; }
.callout-important { background: #fdecea; border-color: #e6b3af; }
code { font-family: "SF Mono", Menlo, monospace; font-size: 9.5pt; background:#f1f1f1; padding:0 3px; }
strong { color: #102a43; }
hr { border: none; border-top: 1px solid #ddd; margin: 10px 0; }
em { color: #555; }
"""

FRONT_MATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
TITLE_RE = re.compile(r'^title:\s*"?(.*?)"?\s*$', re.MULTILINE)


def md_to_html(md_path: Path) -> tuple[str, str]:
    """Return (title, body_html) for a worksheet .md via pandoc."""
    raw = md_path.read_text()
    title = (TITLE_RE.search(raw) or [None, md_path.stem])[1]
    body = subprocess.run(
        ["pandoc", str(md_path), "-f", "markdown", "-t", "html5",
         "--no-highlight", "--wrap=none"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    return title, body


def build() -> str:
    parts = [f"<!doctype html><html><head><meta charset='utf-8'>"
             f"<title>The Human Edge — Participant Workbook</title>"
             f"<style>{CSS}</style></head><body>",
             f"<section class='cover'>{FRONT}</section>"]
    for rel, label in SECTIONS:
        title, body = md_to_html(ROOT / rel)
        parts.append(f"<section><div class='kicker'>{label}</div>"
                     f"<h1>{title}</h1>{body}</section>")
    parts.append("</body></html>")
    return "\n".join(parts)


def main() -> None:
    html = build()
    html_path = OUT.with_suffix(".html")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html)
    print(f">> wrote {html_path.relative_to(ROOT)}")
    r = subprocess.run(["weasyprint", str(html_path), str(OUT)],
                       capture_output=True, text=True)
    if r.returncode != 0 or not OUT.exists():
        sys.stderr.write(r.stderr[-1500:] or "weasyprint failed with no message\n")
        sys.exit(1)
    kb = OUT.stat().st_size / 1024
    print(f">> wrote {OUT.relative_to(ROOT)}  ({kb:.0f} KB)")
    html_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
