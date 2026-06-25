# Project Structure: The Human Edge

How this repo is organised. The repo is a **Quarto website** (`type: website`)
that renders the companion site into `docs/`, which GitHub Pages serves.

## Source vs. generated

- **Edit:** the `.qmd`/`.md`/`.scss` source at the repo root and in
  `readings/`, `activities/`, `handouts/`, `content/`.
- **Generated:** everything in `docs/`, produced by `scripts/build-site.sh`.
  Don't hand-edit `docs/`.

## What renders into the site

`_quarto.yml`'s `render:` list controls what becomes site pages:

| Source | Becomes | Notes |
|---|---|---|
| `index/before/workshop/frameworks/team/series.qmd` | the site's pages | nav defined in `_quarto.yml` |
| `readings/*.qmd` | pre-reading pages | listed on `before.qmd` |
| `activities/morning/*.md` | the 2 morning worksheets | listed on `workshop.qmd` |
| `activities/initiative-cards/*.md` | the 4 initiative pages | listed on `workshop.qmd` |
| `activities/worksheets/*.md` | the 3 sprint worksheets | listed on `workshop.qmd` |
| `handouts/**/*.md` | take-home frameworks | listed on `frameworks.qmd` |
| `content/slide-deck.md` | the deck | rendered **separately** by `build-site.sh` into `docs/content/` (not a nav page) |

**Not rendered / not published:** `instructor-materials/`, `PROJECT_STRUCTURE.md`,
`README.md`. Theme lives in `brand.scss`.

## Theming & front matter

- Site theme: `_quarto.yml` → dual theme `light: [cosmo, brand.scss]` /
  `dark: [darkly, brand.scss]`, reader-toggleable dark mode. All visual tokens
  live in `brand.scss`. Brand fonts (Fraunces display + Inter body) load via
  `_includes/fonts.html`. The navbar logo is `favicon.svg`.
- Listing pages pull `title` + `description` from each content file's YAML front
  matter; keep those fields when adding material.

## Build & deploy

```bash
./scripts/build-site.sh     # clean docs/, render website + deck, add .nojekyll
# then:
git add -A && git commit -m "..." && git push   # Pages serves main /docs
```

Local preview: `open docs/index.html`.

## Adding material (common tasks)

- **A new reading:** add `readings/my-reading.qmd` with `title`, `description`,
  `order` front matter → appears on *Before the day* automatically.
- **A new handout:** add `handouts/frameworks/my-handout.md` with `title` +
  `description` → appears under *Frameworks*.
- **Edit the deck:** edit `content/slide-deck.md`, then `./scripts/build-site.sh`.
- After any change: `./scripts/build-site.sh`, then commit + push.

## Relationship to the sibling courses

This course merges the former **AI in Practice** and **AI in Delivery**
masterclasses (each kept in its own repo for reuse). The afternoon sprints and
the RetailFlow case study are carried over from `ai-in-delivery`; the morning
fluency material draws on `ai-in-practice`. The unifying move is the **trust
tool**, taught once in the morning and reused at project scale in the afternoon.
