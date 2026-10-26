# AI for professionals: building everyday capability

Materials and companion site for a one-day Curtin Executive Education masterclass, the first course in the AI capability series.

**Live site:** https://michael-borck.github.io/ai-in-practice/

## The course

Everyone has the same AI tools now, so the edge is judgement. The day runs four sessions, each built around one tool, with the rhythm *a few slides, then an exercise* all day.

| Session | Time | Tool | Question | Exercises |
|---|---|---|---|---|
| 1 · Judge | 9:00 | Trust tool | How much should I trust this output? | 1 Same prompt, two tools · 2 Place it (card vote and game) |
| 2 · Brief | 11:00 | RTCF and four upgrades | How do I ask for what I need? | 3 Brief it · 4 Upgrade and save |
| 3 · Check | 1:15 | Check loop | How do I know it's right? | 5 RetailFlow analysis · 6 Verification challenge |
| 4 · Redesign | 3:00 | Opportunity Finder (spot, assign, prioritise) | Where does it fit in my week? | 7 Redesign one workflow · 8 Action plan |

What participants leave with, as marketed: a personal prompt library (Exercise 4), four reusable tools (the field guide), and an action plan for the coming week, month and quarter (Exercise 8).

## Layout

```
deck/            The slides: deck.html (with speaker notes), deck.css, deck.js
handouts/        Field guide and voting cards (HTML, printed to PDF), workbook (Markdown), print.css
site/            Companion site pages (Markdown, rendered with pandoc)
assets/          Site stylesheet, favicon, and local copies of the fonts
data/            RetailFlow customer service dataset (Exercise 5)
instructor/      Facilitator guide, room-mode spec, optional agent demo kit (not published)
build/           build.py, screens.py, pandoc templates
docs/            Generated site, served by GitHub Pages. Don't edit; rebuild.
```

## Build

Needs `pandoc`, `weasyprint`, Python with `playwright`, and Google Chrome.

```sh
python3 build/build.py            # site, public deck, PDFs, workbook.docx
python3 build/build.py --no-pdf   # quick rebuild of pages and deck
python3 build/screens.py          # render every slide to PNG for checking
```

The build publishes a copy of the deck with all speaker notes removed and the instructor-only answer slide (`data-private="true"`) dropped. The repository is public, so `instructor/` is readable on GitHub even though it isn't on the site.

Preview locally with `python3 -m http.server -d docs`.

## Presenting

Open `deck/deck.html` from the repo (not the site): it has the notes and the answer slide. Keys: arrows, Space or a clicker to advance; `1` to `4` to jump to a session; `N` for the presenter window; `T` to start the exercise timer; `B` to blank the screen; `F` for full screen. It uses local fonts and runs offline. See `instructor/facilitator-guide.md` for the run sheet, card-vote scenarios and answer keys.

## Editing

- **Slides:** edit `deck/deck.html`. Each slide is a `<section>` with `data-ch` (session 0 to 3). Steps reveal with `data-s="1"`, `data-s="2"` and so on. Exercise slides use `class="slide ex"`, `data-min` for the timer, and `data-steps="1"` to switch from instructions to debrief. Speaker notes go in `<aside class="notes">`.
- **Site:** edit `site/*.md`. Pandoc fenced divs (`::: card`) give the cards and notes.
- **Handouts:** edit `handouts/field-guide.html`, `handouts/voting-cards.html` or `handouts/workbook.md`.

The trust tool's corner names and orientation (precision across, consequences up) match the practice game at trusttool.borck.education. Keep them in step.

## Licence

MIT for code. Course content © Michael Borck. Fonts (Domine, Funnel Sans, Nanum Gothic Coding) are under the SIL Open Font License.
