# The Human Edge: Using and Delivering AI with Judgement

A one-day masterclass for Curtin Executive Education that **merges individual AI fluency with project delivery** around one idea: when everyone has the same tools, your judgement is the edge.

This repo holds the teaching materials **and** builds the companion website (Quarto → GitHub Pages).

## The course in brief

**One idea, two scales.** The day builds one skill — knowing when to trust AI, and where you must stay in charge — and applies it twice:

- **Morning (task scale):** foundations, the trust tool, RTCF prompting, the two-pass demo, and a workflow redesign from each participant's own role.
- **Afternoon (project scale):** the five differences that make AI delivery break the rules, then a live workshop where participants are the delivery lead for one funded RetailFlow initiative — scoping it, designing human-in-the-loop checkpoints, and making the Scale/Pivot/Kill call.

The connective tissue is the **trust tool** (Average/Precise × Small/Large): learned once in the morning at the task level, reused in the afternoon at the project level. Anchored on *Conversation, Not Delegation*.

## How this course came about

It combines what were previously two separate masterclasses — **AI in Practice** (individual capability) and **AI in Delivery** (leading projects that ship) — into a single coherent day. The two already shared the same intellectual core (the trust tool, the "convincing average", the human-edge thesis); this course teaches that core once and applies it at two scales rather than running two thinly-attended days.

## Repo layout

```
_quarto.yml            Quarto website config (type: website, output-dir: docs)
brand.scss             Site theme — tokens, light navbar, hero, icon cards, dark mode
_includes/fonts.html   Brand fonts (Fraunces + Inter), loaded site-wide
index.qmd              Landing page (the thesis + what you leave with)
before.qmd             Readings landing (lists readings/)
workshop.qmd           Morning (task scale) + afternoon sprints (listings)
frameworks.qmd         Trust tool, RTCF, five differences, Scale/Pivot/Kill + handouts
team.qmd               Links to the RetailFlow staff chatbots
series.qmd             The masterclass series
readings/              3 pre-reading pages (.qmd)
activities/
  morning/             Morning worksheets (prompt library, workflow redesign)
  initiative-cards/    The 4 funded RetailFlow initiatives (one per group)
  worksheets/          The 3 afternoon sprint worksheets
handouts/              Take-home frameworks
content/slide-deck.md  The slide deck (rendered separately into docs/content)
scripts/build-site.sh  Build the site (website + deck) into docs/
docs/                  Generated site (GitHub Pages serves main /docs)
```

## Build & deploy

```bash
./scripts/build-site.sh      # renders the Quarto website + deck into docs/
```

Deploy: commit and push. GitHub Pages serves `main` `/docs` at
`michael-borck.github.io/the-human-edge`.

## The RetailFlow case study & chatbots (separate)

The fictional company **RetailFlow** lives in its own repo (`sites/retailflow` →
`retailflow.eduserver.au`): a storefront, an internal document repository (the
dossiers students discern through, code `pilot2024`), and **7 leadership
chatbots** the afternoon sprints interview. Those bots run on AnythingLLM
(`chat.eduserver.au`), built with [botstash](https://pypi.org/project/botstash/).

## Course-assistant chatbot

The site has a site-wide tutor/FAQ chatbot, injected on every page via
`course-bot.html` → `_quarto.yml` `include-after-body`. It runs on AnythingLLM
(`chat.eduserver.au`), workspace `the-human-edge-course`, built with
[botstash](https://pypi.org/project/botstash/). See
`instructor-materials/course-bot-setup.md` for the config and rebuild steps.

## Notes

- The slide deck carries full speaker notes (`:::: {.notes}` blocks) for each slide.

## License

Developed for Curtin University. MIT (see LICENSE).
