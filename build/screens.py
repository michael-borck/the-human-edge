"""Render every deck slide (all steps revealed) to PNG for visual checking.

Usage: python3 build/screens.py [deck.html] [outdir]
Defaults: deck/deck.html -> /tmp/deck-screens
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

root = pathlib.Path(__file__).resolve().parent.parent
deck = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else root / "deck" / "deck.html").resolve()
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "/tmp/deck-screens")
out.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")  # uses installed Google Chrome
    pg = b.new_page(viewport={"width": 1280, "height": 720})
    errors = []
    pg.on("console", lambda m: m.type == "error" and errors.append(m.text))
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.goto(deck.as_uri() + "?print")
    pg.wait_for_load_state("networkidle")
    pg.evaluate("document.fonts.ready")
    for n, el in enumerate(pg.query_selector_all(".slide"), 1):
        el.screenshot(path=str(out / f"slide-{n:02d}.png"))
    # live mode smoke test: step through everything, open on slide 5, start a timer
    pg.goto(deck.as_uri() + "#5")
    pg.wait_for_timeout(300)
    pg.keyboard.press("t")
    for _ in range(80):
        pg.keyboard.press("ArrowRight")
    pg.wait_for_timeout(600)
    pg.screenshot(path=str(out / "live-last.png"))
    print("slides:", n, "errors:", errors or "none")
    b.close()
