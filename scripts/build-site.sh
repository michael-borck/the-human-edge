#!/usr/bin/env bash
# Build The Human Edge companion site (Quarto website + slide deck) into docs/.
# The site is a Quarto `type: website` (see _quarto.yml); the deck is a separate
# artifact rendered into docs/content/. GitHub Pages serves docs/ on main.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

find . -name '._*' -delete 2>/dev/null
rm -rf docs

# Regenerate WebP copies of the deck images (HTML deck uses WebP via
# conditional content; PDF/PPTX keep the PNG). Needs `cwebp`; skips silently.
if command -v cwebp >/dev/null 2>&1; then
  for name in $(grep -oE 'images/[^)]+\.(png|webp)' content/slide-deck.md \
                | sed -E 's#images/##; s/\.(png|webp)$//' | sort -u); do
    png="content/images/$name.png"; webp="content/images/$name.webp"
    [ -f "$png" ] || continue
    if [ ! -f "$webp" ] || [ "$png" -nt "$webp" ]; then
      cwebp -q 85 "$png" -o "$webp" >/dev/null 2>&1 || true
    fi
  done
fi
echo ">> rendering website…"
quarto render || { echo "website render failed"; exit 1; }

echo ">> copying slide deck + workbook…"
# The deck is a hand-built .pptx (scripts/build-deck-pptx.py) exported to PDF
# via PowerPoint. Regenerate those manually; here we just publish them.
cp content/the-human-edge-deck.pptx docs/ 2>/dev/null
cp content/the-human-edge-deck.pdf docs/ 2>/dev/null
# Participant workbook PDF (built by scripts/build-packet.py) → site root
cp content/the-human-edge-participant-workbook.pdf docs/ 2>/dev/null

touch docs/.nojekyll
find . -name '._*' -delete 2>/dev/null
echo "Done. Built docs/ (website + deck). Preview: open docs/index.html"
