# Build System Guide

## Quick Start

### Build Course Materials
```bash
bash build/scripts/build.sh
```

**Output:** HTML files in `docs/` directory.

### Test Locally
```bash
cd docs
python3 -m http.server 8000
# Visit http://localhost:8000
```

### Deploy to GitHub Pages
1. Push to GitHub
2. Settings → Pages → Source: main branch, /docs folder
3. Site live at: `[username].github.io/ai-for-professionals/`

---

## What Gets Built

### From participant-materials/ (2 markdown files):
- frameworks-reference-sheet.md → HTML
- personal-action-plan-template.md → HTML

### From pre-readings/ (1 markdown file):
- ai-for-the-rest-of-us.md → HTML

### From instructor-materials/ (6 markdown files):
- FACILITATOR-START-HERE.md → HTML (password-protected)
- exercise-1-facilitator-guide.md → HTML (password-protected)
- exercise-2-facilitator-guide.md → HTML (password-protected)
- exercise-3-facilitator-guide.md → HTML (password-protected)
- exercise-4-facilitator-guide.md → HTML (password-protected)
- answer-keys.md → HTML (password-protected)

### Also Generated:
- Instructor materials index page (docs/instructor/index.html)

**Total Output:** 10 HTML files + CSS/JS assets.

---

## Folder Structure

```
participant-materials/  ← Participant-facing content (source)
  └── *.md             ← Converted to HTML by build

activities/            ← Exercise materials (instructor distributes directly)
  ├── *.md             ← Worksheets (NOT published to website)
  └── *.csv            ← Data files (distributed via email/USB)

instructor-materials/  ← Facilitator guides
  └── *.md             ← Converted to password-protected HTML

pre-readings/          ← Pre-course materials
  └── *.md             ← Converted to HTML

content/               ← Slide deck
  ├── slide-deck.md    ← Render with Quarto/Pandoc
  └── images/          ← Slide images

docs/                  ← GitHub Pages output (GENERATED)
  ├── *.html           ← Built from sources above
  ├── instructor/      ← Password-protected pages
  ├── css/             ← Copied from build/templates/
  ├── js/              ← Copied from build/templates/
  └── images/          ← Copied from content/images/

build/                 ← Build system
  ├── scripts/build.sh ← Main build script
  └── templates/       ← Pandoc templates + CSS/JS
```

---

## Key Features

### Print to PDF
Every material page has a "Print to PDF" button that opens the browser print dialog.

### Navigation
Dropdown "Materials" menu on all pages linking to:
- All Materials
- Frameworks Reference Sheet
- Action Plan Template
- Pre-Reading
- Instructor Portal

### Password Protection
Instructor materials protected with password: `instructor2025`

To change the password:
1. Open browser console on any page with auth.js loaded
2. Run: `generatePasswordHash('your-new-password')`
3. Copy the hash
4. Update `INSTRUCTOR_PASSWORD_HASH` in `build/templates/auth.js`
5. Rebuild

---

## How to Update Materials

### Update Existing Content:
1. Edit source file in `participant-materials/`, `pre-readings/`, or `instructor-materials/`
2. Run `bash build/scripts/build.sh`
3. Test locally
4. Commit and push

### Add New Participant Material:
1. Create .md file in `participant-materials/`
2. Add filename to `FILES` array in `build/scripts/build.sh`
3. Run build script
4. Add link to materials.html page
5. Commit and push

### Add New Instructor Material:
1. Create .md file in `instructor-materials/`
2. Add filename to `INSTRUCTOR_FILES` array in `build/scripts/build.sh`
3. Run build script
4. Update the instructor index HTML in build.sh if needed
5. Commit and push

---

## Rendering the Slide Deck

The slide deck (`content/slide-deck.md`) is separate from the web build. Render it with Quarto or Pandoc:

### With Quarto (recommended):
```bash
cd content
quarto render slide-deck.md --to revealjs  # HTML slides
quarto render slide-deck.md --to pptx      # PowerPoint
```

### With Pandoc:
```bash
cd content
pandoc slide-deck.md -t revealjs -o slide-deck.html --slide-level=2
pandoc slide-deck.md -o slide-deck.pptx
```

Rendered slide files are copied to `docs/` by the build script if they exist.

---

## Troubleshooting

**Build fails:**
- Check pandoc is installed: `pandoc --version`
- Check source files exist in correct folders

**Links broken:**
- Run build script to regenerate
- Check paths in materials.html

**CSS not updating:**
- Edit CSS in `build/templates/`
- Run build script to copy to `docs/css/`

**Password not working:**
- Default: `instructor2025`
- Hash in `build/templates/auth.js` line 19

**Images not showing:**
- Check images exist in `content/images/`
- Run build script to copy to `docs/images/`

---

## Dependencies

- **Pandoc**: Markdown to HTML conversion (`brew install pandoc` on macOS)
- **Python 3**: Local testing server (pre-installed on macOS)
- **Quarto** (optional), Slide deck rendering (`brew install --cask quarto`)
- **WeasyPrint** (optional), PDF rendering for print items (`brew install weasyprint`)

### Render Print PDFs

```bash
bash build/scripts/make-print.sh
```

Regenerates the five participant PDFs in `print/` (frameworks reference sheet, all three worksheets, action plan). Run after editing any participant material; the committed PDFs in `print/` should always match the markdown sources.

### Render the Slide Deck

```bash
cd content
pandoc slide-deck.md -o slide-deck.pptx --lua-filter=../build/scripts/drop-images.lua
```

Produces `content/slide-deck.pptx` (37 slides, speaker notes included — pandoc turns `::: {.notes}` blocks into PowerPoint speaker notes). The lua filter drops the not-yet-created illustration images (see `content/images/IMAGE-SPECS.md`); the deck is text-plus-notes until those are drawn. The pptx is gitignored on purpose: it carries instructor speaker notes, so do not publish it to the public site.

---

For detailed folder documentation, see FOLDER-STRUCTURE.md.
