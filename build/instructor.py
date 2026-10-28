#!/usr/bin/env python3
"""Render the instructor pack to HTML and PDF in instructor/out/ (not published, not committed).

    python3 build/instructor.py

Makes, each as a self-contained .html and a .pdf:
    facilitator-guide       instructor/facilitator-guide.md
    sources-to-verify       instructor/sources-to-verify.md
    triage-demo             instructor/retailflow-triage-demo/*.md
    slides-with-notes       every slide (all steps shown, answers slide included) with its speaker notes

Needs pandoc, weasyprint and Python playwright with Google Chrome, as build.py does.
"""
import base64
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "instructor" / "out"
TEMPLATE = ROOT / "build" / "templates" / "instructor.html"
HANDOUTS = ROOT / "handouts"  # print.css and the font links resolve from here


def run(*cmd, **kw):
    print("  $", " ".join(str(c) for c in cmd)[:160])
    subprocess.run([str(c) for c in cmd], check=True, **kw)


def strip_front_matter(md):
    if md.startswith("---"):
        end = md.find("\n---", 3)
        if end != -1:
            return md[end + 4:].lstrip()
    return md


def render_md(name, title, markdown):
    """Markdown -> self-contained HTML (pandoc) -> PDF (weasyprint)."""
    src = HANDOUTS / f".{name}.tmp.md"
    src.write_text(markdown, encoding="utf-8")
    html = OUT / f"{name}.html"
    try:
        run("pandoc", src, "-f", "markdown", "-t", "html5", "--template", TEMPLATE,
            "-M", f"title={title}", "--embed-resources", "--standalone",
            "--resource-path", HANDOUTS, "-o", html, cwd=HANDOUTS)
    finally:
        src.unlink()
    run("weasyprint", "-q", html, OUT / f"{name}.pdf")


def guide():
    md = (ROOT / "instructor/facilitator-guide.md").read_text(encoding="utf-8")
    md = re.sub(r"\A# [^\n]*\n", "", md)  # the template prints the title
    render_md("facilitator-guide", "Facilitator guide", md)


def sources():
    md = (ROOT / "instructor/sources-to-verify.md").read_text(encoding="utf-8")
    md = re.sub(r"\A# [^\n]*\n", "", md)
    render_md("sources-to-verify", "Sources and figures to verify", md)


def triage():
    d = ROOT / "instructor/retailflow-triage-demo"
    parts = []
    for f in ("demo-script.md", "sample-tickets.md"):
        parts.append((d / f).read_text(encoding="utf-8"))
    skill = (d / "SKILL.md").read_text(encoding="utf-8")
    parts.append("# The skill file (SKILL.md)\n\nPaste or install exactly this.\n\n````markdown\n" + skill + "\n````\n")
    render_md("triage-demo", "Agent demo kit: RetailFlow ticket triage", "\n\n".join(parts))


def slides_with_notes():
    from playwright.sync_api import sync_playwright
    deck = (ROOT / "deck/deck.html").as_uri() + "?print"
    pages = []
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto(deck)
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        for n, el in enumerate(pg.query_selector_all(".slide"), 1):
            png = el.screenshot()
            info = el.evaluate("""s => ({
                title: s.dataset.title || '',
                priv: s.dataset.private === 'true',
                notes: (s.querySelector('aside.notes') || {}).innerHTML || ''})""")
            pages.append((n, info, base64.b64encode(png).decode()))
        b.close()

    css = (HANDOUTS / "print.css").read_text(encoding="utf-8").replace(
        "@import url('../assets/fonts/fonts.css');", "")
    fonts = (ROOT / "assets/fonts/fonts.css").read_text(encoding="utf-8")

    def font_data(m):
        f = ROOT / "assets/fonts" / m.group(1)
        return "url(data:font/ttf;base64," + base64.b64encode(f.read_bytes()).decode() + ")"

    fonts = re.sub(r"url\(['\"]?([^'\")]+\.ttf)['\"]?\)", font_data, fonts)
    body = []
    for n, info, img in pages:
        tag = ' <span class="priv">answers · not in the public deck</span>' if info["priv"] else ""
        body.append(f'<section class="sl"><h2><span class="num">{n}</span> {info["title"]}{tag}</h2>'
                    f'<img src="data:image/png;base64,{img}" alt="Slide {n}">'
                    f'<div class="notes">{info["notes"] or "<p><i>No notes.</i></p>"}</div></section>')
    html = f"""<!DOCTYPE html><html lang="en-AU"><head><meta charset="utf-8">
<title>Slides with speaker notes · The Human Edge</title>
<style>{fonts}
{css}
@page{{size:A4;margin:12mm 14mm 14mm 14mm}}
body{{font-size:9.2pt}}
.sl{{page-break-after:always}}
.sl h2{{font-size:12pt;margin:0 0 5pt;border:0;padding:0}}
.sl h2 .num{{font-family:var(--mono);color:var(--gold);margin-right:6pt}}
.sl h2 .priv{{font-family:var(--mono);font-size:7pt;letter-spacing:.12em;text-transform:uppercase;color:var(--coral);margin-left:8pt}}
.sl img{{width:100%;border:.6pt solid var(--rule);border-radius:3pt;display:block;margin:0 0 8pt}}
.notes p{{margin:0 0 4pt}} .notes ul{{margin:0 0 4pt;padding-left:14pt}} .notes li{{margin:0 0 3pt}}
.cover h1{{font-size:24pt;border:0;margin:0 0 4pt}}
@media screen{{body{{max-width:900px;margin:30px auto;padding:0 24px}} .sl{{margin-bottom:60px}}}}
</style></head><body>
<section class="sl cover"><div class="kicker">Curtin Executive Education · The Human Edge</div>
<h1>Slides with speaker notes</h1><p>Instructor only. Every slide with all its steps shown, including the answers slide left out of the public deck. Rebuild with <code>python3 build/instructor.py</code> after editing the deck.</p></section>
{''.join(body)}</body></html>"""
    out = OUT / "slides-with-notes.html"
    out.write_text(html, encoding="utf-8")
    run("weasyprint", "-q", out, OUT / "slides-with-notes.pdf")
    print(f"  {len(pages)} slides")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    print("facilitator guide"); guide()
    print("sources to verify"); sources()
    print("agent demo kit"); triage()
    print("slides with notes"); slides_with_notes()
    print("done:", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
