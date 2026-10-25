#!/bin/bash

# Render participant print items to PDF in print/
# Usage: bash build/scripts/make-print.sh
# Requires: pandoc, weasyprint (brew install weasyprint)

set -e
cd "$(dirname "$0")/../.."

OUT=print
mkdir -p "$OUT"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

# Print CSS: site styles + A4 page setup
cp build/templates/materials.css "$TMP/print.css"
cat > "$TMP/page.css" <<'EOF'
@page { size: A4; margin: 15mm 14mm; }
body { font-size: 10.5pt; background: #fff; }
h1 { font-size: 1.6rem; }
h2 { font-size: 1.3rem; }
h3 { font-size: 1.1rem; }
EOF

FILES=(
  "participant-materials/frameworks-reference-sheet.md"
  "activities/prompt-engineering-worksheet.md"
  "activities/data-analysis-worksheet.md"
  "activities/workflow-mapping-template.md"
  "participant-materials/personal-action-plan-template.md"
)

for f in "${FILES[@]}"; do
  base=$(basename "$f" .md)
  html="$TMP/$base.html"
  pandoc "$f" \
    --from markdown-smart \
    --to html5 \
    --standalone \
    --metadata title="$base" \
    -c print.css -c page.css \
    -o "$html"
  weasyprint "$html" "$OUT/$base.pdf" 2>/dev/null
  echo "  $OUT/$base.pdf"
done

echo "Done. PDFs in print/"
