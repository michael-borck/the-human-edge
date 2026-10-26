# The Human Edge: Using and Delivering AI with Judgement

One-day BYOD masterclass, Curtin Business School Executive Education.
Booked as *AI for Professionals: Building Everyday Capability* — the deck opens by striking that title through. Everything in this repo uses the new title; ask Curtin to update the marketing page when convenient. "Delivering" means delivering your work with AI, not delivering AI projects (Courses 2 and 3).

**The one idea:** everyone has the same AI tools, so generic competence is the baseline. The edge is judgement — brief well, decide how much to trust, verify from outside the tool, keep a human where precision meets high stakes.

## The day (9:00–4:30, four loops)

| Loop | Framework | Exercise (digital workbook) |
|---|---|---|
| 1 Judge 9:00–10:30 | Trust Tool (spine) + Suitability Spectrum | The compare drill: your rough pass vs AI's |
| 2 Brief 11:00–12:30 | RTCF + weaker-model ladder | Prompt workshop (2 of 3 scenarios) |
| 3 Verify 1:15–2:30 | AI-Assisted Analysis Workflow | RetailFlow data challenge + verification of 3 planted claims |
| 4 Redesign 3:00–4:00 | AI Opportunity Finder (sequencing inside it) | Redesign a real weekly workflow, test one step live |
| Close 4:00–4:30 | Decide · Practise · Trade · Revisit | Action plan: week / month / quarter |

Breaks 10:30 and 2:30; lunch 12:30–1:15. No teaching block runs over 15 minutes before hands-on work.

Marketed outcomes, all delivered: RTCF, Opportunity Finder, workflow redesign, responsible-use safeguards (memory/privacy slide, Verify loop), a personal prompt library, four reusable decision tools plus the Trust Tool spine, and a week/month/quarter action plan.

## Deliverables

- **Deck:** present from `content/deck.html` (your local presenter copy with notes and verdicts). The build publishes a participant copy to `docs/deck.html` with notes stripped and the Exercise 3 verdicts held back, so the reveal survives participants clicking ahead. Bespoke single-file HTML (engine forked from *The Broken Ladder* `a.html`): 26 slides, chapter rail, `Space` next, `N` presenter notes, `1–4` chapter jump. No PowerPoint. Print-to-PDF from the browser is the emergency fallback.
- **Workbook:** `docs/exercises.html`. All four exercises + action plan as one digital workbook. Autosaves in the browser (localStorage), exports to markdown or PDF. No paper, no butchers paper, no post-its — artefacts leave on participants' laptops.
- **Frameworks reference:** `participant-materials/frameworks-reference-sheet.md` → `docs/frameworks-reference-sheet.html`, with `docs/frameworks.html` as the brochure page. Diagrams are shared SVGs in `content/images/`.
- **Instructor:** `instructor-materials/` (password portal). Start at FACILITATOR-START-HERE.md.

## Sources vs output

Edit markdown in `participant-materials/`, `pre-readings/`, `instructor-materials/`, and the deck in `content/deck.html`. Hand-written site pages live in `docs/*.html` (index, frameworks, exercises/workbook, trust-tool, schedule, materials, overview). Everything else in `docs/` is generated — see BUILD.md.
