#!/bin/bash

# Build Course Materials for GitHub Pages
# AI for Professionals — Executive Education, Curtin Business School
# Runs locally or in CI (GitHub Actions)

set -e  # Exit on error

# Colors (work in CI logs too)
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Directories
SOURCE_DIR="participant-materials"
PREREADINGS_DIR="pre-readings"
INSTRUCTOR_DIR="instructor-materials"
OUTPUT_DIR="docs"
OUTPUT_INSTRUCTOR="docs/instructor"
TEMPLATE_DIR="build/templates"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Building Course Materials${NC}"
echo -e "${BLUE}AI for Professionals${NC}"
echo -e "${BLUE}========================================${NC}\n"

# Create output directories
mkdir -p "$OUTPUT_DIR"
mkdir -p "$OUTPUT_DIR/css"
mkdir -p "$OUTPUT_DIR/js"
mkdir -p "$OUTPUT_DIR/images"
mkdir -p "$OUTPUT_INSTRUCTOR"

# Copy images from content/images to docs/images
if [ -d "content/images" ]; then
  image_count=0
  for ext in png jpg jpeg gif svg; do
    for img in content/images/*.$ext; do
      [ -f "$img" ] || continue
      cp "$img" "$OUTPUT_DIR/images/"
      image_count=$((image_count + 1))
    done
  done
  if [ $image_count -gt 0 ]; then
    echo -e "${GREEN}✓${NC} Copied $image_count image(s) to docs/images/\n"
  fi
fi

# Copy CSS and JS to output
if [ -f "$TEMPLATE_DIR/materials.css" ]; then
  cp "$TEMPLATE_DIR/materials.css" "$OUTPUT_DIR/css/"
  echo -e "${GREEN}✓${NC} Copied materials.css\n"
fi

if [ -f "$TEMPLATE_DIR/shared.css" ]; then
  cp "$TEMPLATE_DIR/shared.css" "$OUTPUT_DIR/css/"
  echo -e "${GREEN}✓${NC} Copied shared.css\n"
fi

if [ -f "$TEMPLATE_DIR/auth.js" ]; then
  cp "$TEMPLATE_DIR/auth.js" "$OUTPUT_DIR/js/"
  echo -e "${GREEN}✓${NC} Copied auth.js\n"
fi

# Participant materials to convert (markdown to HTML)
FILES=(
  "frameworks-reference-sheet"
  "personal-action-plan-template"
)

# Pre-readings to convert
PREREADING_FILES=(
  "ai-for-the-rest-of-us"
)

# Instructor materials to convert (will be password protected)
INSTRUCTOR_FILES=(
  "FACILITATOR-START-HERE"
  "exercise-1-facilitator-guide"
  "exercise-2-facilitator-guide"
  "exercise-3-facilitator-guide"
  "exercise-4-facilitator-guide"
  "answer-keys"
)

# Function: Convert markdown to HTML for web
convert_to_html() {
  local filename=$1
  local source_dir=$2
  local output_dir=$3
  local template=${4:-"material-page.html"}

  local source="$source_dir/${filename}.md"
  local output_basename=$(basename "$filename")
  local output="$output_dir/${output_basename}.html"
  local title=$(echo "$output_basename" | sed 's/-/ /g' | sed 's/\b\(.\)/\u\1/g')

  if [ ! -f "$source" ]; then
    echo -e "${YELLOW}⚠${NC} Warning: File not found: $source\n"
    return
  fi

  echo -e "${GREEN}Converting${NC} $(basename $source) → HTML..."

  pandoc "$source" \
    --from markdown-smart \
    --to html5 \
    --template="$TEMPLATE_DIR/$template" \
    --standalone \
    --toc \
    --toc-depth=2 \
    --variable title="$title" \
    --variable filename="$output_basename" \
    --css="css/materials.css" \
    -o "$output" 2>/dev/null

  if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓${NC} Created: $output\n"
  else
    echo -e "${RED}✗${NC} Failed to create HTML for $filename\n"
  fi
}

# Convert participant materials
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Building Participant Materials${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

for file in "${FILES[@]}"; do
  convert_to_html "$file" "$SOURCE_DIR" "$OUTPUT_DIR"
done

# Convert pre-readings
echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Building Pre-Readings${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

for file in "${PREREADING_FILES[@]}"; do
  convert_to_html "$file" "$PREREADINGS_DIR" "$OUTPUT_DIR"
done

# Convert instructor materials (with password protection)
echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Building Instructor Materials (Password Protected)${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

for file in "${INSTRUCTOR_FILES[@]}"; do
  if [ -f "$INSTRUCTOR_DIR/${file}.md" ]; then
    convert_to_html "$file" "$INSTRUCTOR_DIR" "$OUTPUT_INSTRUCTOR" "instructor-page.html"
  else
    echo -e "${YELLOW}⚠${NC} Warning: Instructor file not found: $INSTRUCTOR_DIR/${file}.md\n"
  fi
done

# Build instructor materials index
echo -e "${GREEN}Creating${NC} instructor materials index...\n"
cat > "$OUTPUT_INSTRUCTOR/index.html" << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Instructor Materials | AI for Professionals</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/materials.css">
  <script src="../js/auth.js"></script>
  <meta name="robots" content="noindex, nofollow">
</head>
<body onload="checkAuth()">
  <nav class="topnav">
    <div class="container">
      <a href="../index.html" class="logo">AI for Professionals</a>
      <div class="nav-links">
        <a href="../index.html">Home</a>
        <a href="../materials.html">Materials</a>
      </div>
    </div>
  </nav>

  <main class="container" id="protected-content" style="display:none;">
    <article class="material-content">
      <header class="material-header">
        <h1>Instructor Materials</h1>
        <p style="color: #7f8c8d;">Password-protected resources for course facilitators</p>
      </header>

      <div class="content">
        <h2>Quick Start</h2>
        <div class="resource-grid" style="display: grid; gap: 2rem; margin: 2rem 0;">
          <div class="resource-item" style="border: 3px solid #667eea; padding: 1.5rem; border-radius: 8px; background: #f0f4ff;">
            <h3>START HERE</h3>
            <p>Master delivery guide: teaching philosophy, day timeline, facilitation moves, troubleshooting, materials checklist.</p>
            <div style="margin-top: 1rem;">
              <a href="FACILITATOR-START-HERE.html" class="btn-primary">Read Now</a>
            </div>
          </div>
        </div>

        <hr style="margin: 3rem 0; border: none; border-top: 1px solid #e5e7eb;">

        <h2>Exercise Facilitator Guides (Use During Course)</h2>
        <div class="resource-grid" style="display: grid; gap: 2rem; margin: 2rem 0;">
          <div class="resource-item" style="border: 2px solid #e5e7eb; padding: 1.5rem; border-radius: 8px;">
            <h3>1. AI Tool Test Drive (40 min)</h3>
            <p>Compare ChatGPT, Claude, and Gemini on a management scenario. Debrief on tool differences.</p>
            <div style="margin-top: 1rem;">
              <a href="exercise-1-facilitator-guide.html" class="btn-primary">View Guide</a>
            </div>
          </div>

          <div class="resource-item" style="border: 2px solid #e5e7eb; padding: 1.5rem; border-radius: 8px;">
            <h3>2. Prompt Engineering Workshop (60 min)</h3>
            <p>Three rounds: baseline, RTCF, advanced techniques. Coaching-intensive with 6 workplace scenarios.</p>
            <div style="margin-top: 1rem;">
              <a href="exercise-2-facilitator-guide.html" class="btn-primary">View Guide</a>
            </div>
          </div>

          <div class="resource-item" style="border: 2px solid #e5e7eb; padding: 1.5rem; border-radius: 8px;">
            <h3>3. Data Analysis Challenge (45 min)</h3>
            <p>RetailFlow CSV dataset with baked-in patterns. Progressive questioning and verification.</p>
            <div style="margin-top: 1rem;">
              <a href="exercise-3-facilitator-guide.html" class="btn-primary">View Guide</a>
            </div>
          </div>

          <div class="resource-item" style="border: 2px solid #e5e7eb; padding: 1.5rem; border-radius: 8px;">
            <h3>4. AI-Enhanced Workflow (40 min)</h3>
            <p>Participants redesign a real task from their job. Coaching on task selection and realistic redesign.</p>
            <div style="margin-top: 1rem;">
              <a href="exercise-4-facilitator-guide.html" class="btn-primary">View Guide</a>
            </div>
          </div>
        </div>

        <hr style="margin: 3rem 0; border: none; border-top: 1px solid #e5e7eb;">

        <h2>Reference Materials</h2>
        <div class="resource-grid" style="display: grid; gap: 2rem; margin: 2rem 0;">
          <div class="resource-item" style="border: 2px solid #e5e7eb; padding: 1.5rem; border-radius: 8px;">
            <h3>Answer Keys &amp; Sample Outputs</h3>
            <p>What "good thinking" looks like for all exercises. Calibration guidance, not prescriptive answers.</p>
            <div style="margin-top: 1rem;">
              <a href="answer-keys.html" class="btn-primary">View Online</a>
            </div>
          </div>
        </div>

        <hr style="margin: 3rem 0; border: none; border-top: 1px solid #e5e7eb;">

        <p style="text-align: center; color: #7f8c8d;">
          <a href="#" onclick="logout(); return false;" style="color: #e74c3c; font-weight: 600;">Logout</a>
        </p>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>AI for Professionals | Curtin Business School</p>
    </div>
  </footer>
</body>
</html>
EOF

echo -e "${GREEN}✓${NC} Created instructor materials index\n"

# Copy slide deck to docs/ (if rendered versions exist)
echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Copying Slide Decks${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"

SLIDE_FORMATS=("pptx" "docx" "html" "pdf")
for format in "${SLIDE_FORMATS[@]}"; do
  if [ -f "content/slide-deck.$format" ]; then
    cp "content/slide-deck.$format" "$OUTPUT_DIR/slide-deck.$format"
    echo -e "${GREEN}✓${NC} Copied: slide-deck.$format\n"
  else
    echo -e "${YELLOW}⚠${NC} Slide deck not found: content/slide-deck.$format (render with Quarto/Pandoc first)\n"
  fi
done

echo -e "\n${BLUE}========================================${NC}"
echo -e "${GREEN}Build Complete!${NC}"
echo -e "${BLUE}========================================${NC}"
echo -e "HTML files: ${OUTPUT_DIR}/"
echo -e "Instructor materials: ${OUTPUT_INSTRUCTOR}/ ${YELLOW}(password protected)${NC}"
echo -e "\nReady for GitHub Pages deployment."
