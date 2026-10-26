# Build

```bash
bash build/scripts/build.sh          # markdown -> docs/, copies deck + CSV + images
python3 -m http.server 8000 --directory docs   # preview at http://localhost:8000
```

Needs `pandoc`. No Quarto, no WeasyPrint, no print pipeline, no PPTX — all retired.

## What the build does

- `participant-materials/*.md` + `pre-readings/*.md` -> `docs/*.html` (templates in `build/templates/`)
- `instructor-materials/*.md` -> `docs/instructor/*.html` (password `instructor2025`; hash in `build/templates/auth.js`)
- `content/deck.html` -> `docs/deck.html` (edit the source, never the copy)
- `content/images/*.svg` -> `docs/images/`; `activities/retailflow-*.csv` -> `docs/data/`

Hand-written pages (`docs/index.html`, `frameworks.html`, `exercises.html` workbook, `trust-tool.html`, `overview.html`, `schedule.html`, `materials.html`) are edited directly and are not overwritten by the build.

## Deck notes

`content/deck.html` is self-contained apart from Google Fonts; cache the fonts or open it once online before presenting offline. Keys: Space/click next, arrows back/forward, `N` notes overlay, `1–4` chapter jump, `Home` restart. Stage scales uniformly (min of width/height) so 4:3 projectors letterbox instead of stretching.

## Adding material

New participant markdown: add the file, append its basename to `FILES` in `build/scripts/build.sh`, rebuild, link it from `docs/materials.html`. Instructor files: same with `INSTRUCTOR_FILES`.
