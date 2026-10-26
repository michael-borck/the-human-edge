#!/usr/bin/env python3
"""Build the companion site into docs/ (published by GitHub Pages).

    python3 build/build.py            # everything
    python3 build/build.py --no-pdf   # site and deck only (fast)

Needs: pandoc, weasyprint, and Python playwright with Google Chrome installed
(used to print the slide PDF). Sources:

    site/*.md            -> docs/*.html             (pandoc + build/templates/site.html)
    deck/                -> docs/deck/              (speaker notes and private slides removed)
    handouts/*.html      -> docs/downloads/*.pdf    (weasyprint)
    handouts/workbook.md -> docs/downloads/workbook.{pdf,docx}
    data/*.csv           -> docs/downloads/
"""
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
DL = DOCS / "downloads"
PDF = "--no-pdf" not in sys.argv


def run(*cmd, **kw):
    print("  $", " ".join(str(c) for c in cmd))
    subprocess.run([str(c) for c in cmd], check=True, **kw)


def public_deck(html: str) -> str:
    """Strip speaker notes and instructor-only slides (data-private) from the deck."""
    html = re.sub(r"\s*<aside class=\"notes\">.*?</aside>", "", html, flags=re.S)
    html = re.sub(r"\s*<!--[^>]*?instructor only[^>]*?-->", "", html)
    html = re.sub(r"\s*<section[^>]*data-private=\"true\"[^>]*>.*?</section>", "", html, flags=re.S)
    return html


def main():
    print("clean docs/")
    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "assets").mkdir(parents=True)
    DL.mkdir()
    (DOCS / ".nojekyll").touch()

    print("assets")
    for f in (ROOT / "assets").rglob("*"):
        if f.is_file() and not f.name.startswith("._"):
            dest = DOCS / "assets" / f.relative_to(ROOT / "assets")
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(f, dest)

    print("site pages")
    for md in sorted(m for m in (ROOT / "site").glob("*.md") if not m.name.startswith("._")):
        run("pandoc", md, "-f", "markdown", "-t", "html5", "--template", ROOT / "build/templates/site.html",
            "-o", DOCS / (md.stem + ".html"))

    print("deck (public copy)")
    (DOCS / "deck").mkdir()
    src = (ROOT / "deck/deck.html").read_text()
    (DOCS / "deck/index.html").write_text(public_deck(src))
    for f in ("deck.css", "deck.js"):
        shutil.copy2(ROOT / "deck" / f, DOCS / "deck" / f)
    n_all, n_pub = src.count('<section class="slide'), public_deck(src).count('<section class="slide')
    print(f"  {n_all} slides in source, {n_pub} public; notes removed")

    print("data")
    for f in (f for f in (ROOT / "data").glob("*.csv") if not f.name.startswith("._")):
        shutil.copy2(f, DL / f.name)

    print("workbook (docx)")
    run("pandoc", ROOT / "handouts/workbook.md", "-o", DL / "workbook.docx")

    if not PDF:
        print("done (no PDFs)")
        return

    print("handouts (pdf)")
    for name in ("field-guide", "voting-cards"):
        run("weasyprint", "-q", ROOT / f"handouts/{name}.html", DL / f"{name}.pdf")
    tmp = ROOT / "handouts/.workbook.tmp.html"
    run("pandoc", ROOT / "handouts/workbook.md", "-f", "markdown", "-t", "html5",
        "--template", ROOT / "build/templates/handout.html", "-o", tmp)
    run("weasyprint", "-q", tmp, DL / "workbook.pdf")
    tmp.unlink()

    print("slides (pdf)")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        pg.goto((DOCS / "deck/index.html").as_uri() + "?print")
        pg.wait_for_load_state("networkidle")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(DL / "slides.pdf"), width="1280px", height="720px", print_background=True)
        b.close()
    print("done")


if __name__ == "__main__":
    main()
