#!/usr/bin/env python3
"""Publish docs/deck.html as the participant copy of content/deck.html.

The presenter presents from content/deck.html (local file, never published).
The participant copy has all presenter notes stripped, the notes key and
hint removed, and the Exercise 3 verdicts held back so the reveal in the
room still works. After delivery, rerunning this script is harmless; the
verdicts also live in the instructor answer keys.
"""
import re
import pathlib

src = pathlib.Path("content/deck.html").read_text()

# strip presenter notes
src = re.sub(r'\s*<aside class="notes">.*?</aside>', "", src, flags=re.S)
src = src.replace('<div id="hint">SPACE NEXT &middot; N NOTES &middot; 1-4 CHAPTERS</div>',
                  '<div id="hint">SPACE NEXT &middot; 1-4 CHAPTERS</div>')
src = src.replace("if(e.key==='n'||e.key==='N'){notesOn=!notesOn;render();}", "")

# hold the verdicts: replace the verdict slide body with the claims only
verdict = re.search(
    r'(<section class="slide" data-mode="spot">\s*<div class="k">VERIFY &middot; THE VERDICTS</div>.*?)</section>',
    src, flags=re.S)
if verdict:
    held = ('<section class="slide">\n'
            '  <div class="k">VERIFY &middot; THE VERDICTS</div>\n'
            '  <div class="t">Verdicts revealed <em>in the room.</em></div>\n'
            '  <div class="body"><p>Three claims were tested against the data. '
            'The verdicts, and the evidence, are worked through live in the debrief '
            'so the check stays yours. Your own verdicts belong in the workbook, '
            'Exercise 3.</p>\n'
            '  <p><strong>After the session:</strong> the full verdicts are in the '
            'facilitator debrief and your exported workbook. If you are re-reading '
            'this deck later, the pattern to remember is the fluent, professional, '
            'plausible claim that the data refuted twice.</p></div>\n'
            '</section>')
    src = src[:verdict.start()] + held + src[verdict.end():]
else:
    raise SystemExit("verdict slide not found; participant deck would leak answers")

# also hold verdict wording that appears anywhere else
for leak in ("REFUTED TWICE", "Claim B is the lesson"):
    if leak in src:
        raise SystemExit(f"answer leak remains in participant deck: {leak}")

pathlib.Path("docs/deck.html").write_text(src)
print("participant deck written: notes stripped, verdicts held")
