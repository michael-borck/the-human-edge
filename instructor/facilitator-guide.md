# Facilitator guide

*AI for professionals: building everyday capability.* One day, 9:00 to 4:30, four sessions, eight exercises. This guide replaces the old start-here note, the four exercise guides and the answer keys. It isn't published: the build only publishes `docs/`. The repo itself is public, though, so don't add anything here you wouldn't want a participant to read.

## The design in one paragraph

Everyone has the same AI tools, so the edge is judgement. The day teaches four tools, one per session, each answering one question: the **trust tool** (how much should I trust this?), **RTCF** (how do I ask?), the **check loop** (how do I know it's right?) and the **Opportunity Finder** (where does it fit?). The task spectrum (AI leads, AI assists, you lead, human only) is the "assign" step of the Opportunity Finder. The rhythm all day is two or three slides, then an exercise, then a short debrief. The close takes the personal half of the "broken ladder" idea (practice is now a choice: decide, practise, trade, revisit) and points managers to course 3 for the organisational half.

## Before the day

**Two weeks out**
- Confirm the room has Wi-Fi for every participant, power at the tables, and a projector input for your laptop.
- Ask Exec Ed to include the course site link and the "Before the day" page in the joining instructions: `michael-borck.github.io/ai-in-practice/before.html`.

**Three days out**
- Print the **voting cards**, one A4 sheet per participant plus spares: `docs/downloads/voting-cards.pdf`, double-sided, flip on the long edge. Cut into four cards per person (a guillotine takes five minutes for 30 sheets). Each card: A/Verified, B/Overstated, C/Refuted, D/Can't tell yet.
- Optional: print the field guide (10 pages) for anyone who prefers paper. Everything else is digital.
- Check the trust tool game loads: trusttool.borck.education.
- Re-check fast-moving facts (see "Before each run" at the end).

**On the day, before 9:00**
- Open `deck/deck.html` **from the repo** (it has your notes and the answer slide). Press **F** for full screen and **N** for the presenter window on your laptop screen.
- Wi-Fi details on the whiteboard. Voting cards on every seat.
- Load an AI tool on the projector for the live demos: one chat open, one fresh chat ready.

## Presenting

| Key | Action |
|---|---|
| → / Space / PageDown | Next step or slide (works with a clicker) |
| ← / PageUp | Back |
| 1 2 3 4 | Jump to the start of a session |
| N | Presenter window: notes, next slide, elapsed time, clock, exercise timer |
| T | Start or pause the exercise timer (exercise slides only; shows top right) |
| R | Reset the timer |
| B | Blank the screen for discussion |
| F | Full screen |

Exercise slides have two states: instructions, then (one click) the debrief questions. Slide 22 (the verification answers) exists only in the repo copy; the public deck and PDF skip it. The deck uses local fonts, so it runs without internet.

## Run sheet

| Time | Slides | What happens | Minutes |
|---|---|---|---|
| **9:00** | 1–2 | Welcome, the day, show of hands, tool check | 10 |
| 9:10 | 3–4 | The convincing average; AI's mistakes don't look like mistakes | 10 |
| 9:20 | 5 | **Exercise 1** · Same prompt, two tools | 20 |
| 9:40 | 6–8 | Trust tool: two questions, four corners, check from outside | 15 |
| 9:55 | 9 | **Exercise 2** · Place it (card vote, game, own tasks) | 25 |
| 10:20 | 10 | Three rules before you paste; questions | 10 |
| 10:30 | | Morning tea | 30 |
| **11:00** | 11–13 | Brief like a colleague; RTCF; live before/after demo | 15 |
| 11:15 | 14 | **Exercise 3** · Brief it | 25 |
| 11:40 | 15–16 | Four upgrades; pushback and the guardrail | 10 |
| 11:50 | 17 | **Exercise 4** · Upgrade and save (library) | 25 |
| 12:15 | | Debrief; download the CSV before lunch | 15 |
| 12:30 | | Lunch | 45 |
| **1:15** | 18–19 | Check loop; five failure modes | 10 |
| 1:25 | 20 | **Exercise 5** · RetailFlow | 30 |
| 1:55 | 21 | **Exercise 6** · Verification challenge (pairs, then card vote) | 15 |
| 2:10 | 22 | Reveal; full debrief of Exercise 5 | 20 |
| 2:30 | | Afternoon tea | 30 |
| **3:00** | 23–25 | Opportunity Finder: spot, assign, prioritise | 10 |
| 3:10 | 26 | **Exercise 7** · Redesign one workflow | 30 |
| 3:40 | 27 | Agents, harnesses, skills (optional 3-minute demo) | 5 |
| 3:45 | 28–33 | Why practice matters now: evidence, compare habit, the moving line, the loop, if you lead people | 12 |
| 3:57 | 34 | **Exercise 8** · Action plan, calendar entry, two or three shares | 12 |
| 4:10 | 35 | Close, series, feedback form | 20 |
| 4:30 | | Finish | |

If you're running late, cut in this order: slide 31 (the moving line), the Exercise 4 pushback step, the agents slide, the "if you lead people" slide. Never cut the verification challenge or the action plan.

## Session notes

### Session 1 · Judge

**The point:** fluent isn't the same as correct, and AI's errors don't trigger the alarm you use on human work. The trust tool turns "can I trust this?" into a ten-second placement.

**Exercise 1.** Look for different assumptions (firm vs caring), nobody asking about personal circumstances, confident employment-law advice nobody can verify, advice that's too punitive or too soft. Amplify comments like "I'd take A's structure and B's tone". Name the move as the compare habit; it comes back at 3:45.

**Exercise 2 card vote.** Read a scenario, pause, "one, two, three", everyone shows a card. Ask one person from each corner to explain. Blind voting stops people following the most senior person in the room. Scenarios, with the usual answer:

1. Rewrite your out-of-office message to sound friendlier. *A.*
2. Summarise a 40-page tender so your team can decide whether to bid. *B: the deadline, eligibility rules and budget carry the decision.*
3. The publication year of a study you'll cite in an internal newsletter. *C.*
4. Talking points for a difficult conversation with a team member. *Splits B and D. Let it: the argument is about stakes.*
5. A letter telling a staff member their role is redundant. *D: entitlements, law, a livelihood.*

Spares: meeting minutes from your own notes (A); a dosage or safety figure in a site procedure (D); the agenda for a team offsite (A); a formula in a budget spreadsheet the CFO will use (C or D, depending on who sees it next).

**Debrief line:** when the room splits, it's almost always about stakes, and stakes depend on who sees the output next.

### Session 2 · Brief

**The point:** prompting is briefing a capable new colleague. Context does most of the work. Be honest that Role matters least on current models.

**Live demo (slide 13).** Run the before prompt, then the after prompt in a fresh chat. Ask "which would you send?" If the Wi-Fi fails, describe both outputs and go straight to Exercise 3.

**Exercise 3 coaching.** Round 2 barely different from Round 1? Ask "what would you tell a new hire?" Added a Role and nothing else? Coach Context and Format. Good Round 2 prompts are four to eight sentences. Push people towards real work; the scenario cards are a fallback.

**Exercise 4.** The upgrades matter most for people whose workplace has approved an older or cheaper model. Make sure everyone leaves for lunch with three saved prompts, each with its check (trust corner). That's the promised prompt library.

### Session 3 · Check

**The point:** fast analysis, slow trust. Verification comes from outside the tool.

**Exercise 5.** If uploads are blocked, most tools accept pasted CSV text; the file is small. Watch for people skipping the "describe the data first" step.

**Exercise 6.** 8 minutes checking in pairs, then the card vote per claim (Verified, Overstated, Refuted, or Can't tell yet). Reveal on slide 22, one claim per click. Expect B to fool the most people and C to split the room.

## Answer key: RetailFlow

Checked against `data/retailflow-customer-service-data.csv` (260 rows, 3 July to 29 December 2024, 8 agents).

**By category**

| Category | Tickets | Satisfaction | Response (h) | Resolved |
|---|---|---|---|---|
| Returns & Refunds | 48 | 1.56 | 13.3 | 77% |
| Delivery Problems | 43 | 2.17 | 11.0 | 77% |
| Billing Queries | 40 | 2.79 | 9.8 | 92% |
| Account Issues | 28 | 3.06 | 8.8 | 96% |
| Product Information | 37 | 3.88 | 5.5 | 89% |
| Order Tracking | 64 | 3.90 | 6.7 | 92% |

**Response time (hours).** Overall 9.17. By day: Thursday 7.4, Saturday 8.3, Wednesday 8.5, Friday 8.6, Tuesday 8.8, Monday 9.8, Sunday 13.7. By month: November 7.2, August 8.1, July 8.5, September 9.0, October 9.2, December 13.6. By channel: Live Chat 4.0, Phone 6.1, Social Media 9.4, Email 13.2.

**Response time and satisfaction.** Average satisfaction 2.92 overall. Over 8 hours: 2.09 (123 tickets). Over 12 hours: 1.64 (69 tickets). Up to 4 hours: 4.09.

**Verification challenge**

- **A · Verified.** Email 13.2 h vs Live Chat 4.0 h: 3.3 times. Teaching point: the true claim sounded no more confident than the false ones. Checking also earns you the right to trust.
- **B · Refuted, twice.** The lowest category is Returns & Refunds (1.56); Account Issues is mid-table (3.06). And Account Issues has the *highest* resolution rate (96%), so "most complex" collapses too. This is the convincing fake: a plausible reason, a professional tone, wrong twice. Forwarded to Karen, she'd fix the wrong thing.
- **C · Overstated.** Sunday 13.7 h against an overall average of 9.2 h is 1.5 times, not double. Used in a staffing case, "double" inflates the argument by a third. Precise and large: close is the same as wrong.

**A strong brief for Karen** names Returns & Refunds and Delivery Problems as the worst categories; response time as the factor cutting across all of them; Sundays, Mondays, December and Email as the blow-outs; and recommends fixing the returns process, steering customers to Live Chat, and staffing for predictable peaks. It ends with what was checked.

**A trap to watch for.** Tools often explain the Sunday spike with "nobody works on Sunday". That's false: agents handle Sunday tickets (Amy T, David L and Marcus B among them). It's a good live example of a plausible explanation the data doesn't support.

### Session 4 · Redesign

**The point:** find where AI fits in your own week, decide who leads each step, and keep practising on purpose because work no longer trains you for free.

**Exercise 7.** Strong redesigns mix AI and human steps, keep a human check before anything leaves the building, and claim realistic savings. Push back on "every step AI-led", grand automation plans, and redesigns nobody tested. Ask: "What could you do with your current tool tomorrow?"

**The evidence slide (28).** Keep it balanced: the Stanford finding is a 19% gap for 22 to 25 year olds in AI-exposed jobs, mostly through fewer hires, with no comparable gap for experienced workers and no economy-wide job loss. It's descriptive, not causal.

**Exercise 8.** Eight minutes of quiet. Reject "use AI more"; ask "which task, which tool, which day?" Watch for people actually creating the calendar entry.

**Optional agent demo (slide 27).** Kit in `instructor/retailflow-triage-demo/`. Three minutes, the same prompt before and after a skill file exists. Skip it if anything is flaky; the idea matters more than the demo.

## What you'll hear, and how to respond

| You hear | It usually means | Try |
|---|---|---|
| "I use it for everything." | Enthusiasm without a check | "What's one thing you'd still do yourself? Why?" |
| "It got everything wrong." | Vague prompts | "Show me the prompt. Let's add Context." |
| "I don't trust it enough to use at work." | Healthy scepticism | "Start in the green corner: low stakes, easy to check." |
| "This will save me hours every week." | Overestimating | "Start with one task this week and time it, including the checking." |
| "My company won't let me use these." | A real constraint | "Take the tools and the thinking. When tools are approved, you'll be ready." |
| "Which tool is best?" | Looking for a shortcut | "The one you're allowed to use. The skills transfer; the rankings change monthly." |

## Before each run: update checklist

AI changes fast. Check these the week before; most take a minute.

- [ ] Stanford "Canaries in the Coal Mine?" paper: is there a newer revision? Update slide 28 and the field guide if the 19% figure has moved.
- [ ] Data and training defaults for consumer vs business plans of the main tools. Slide 10, the field guide and the pre-reading speak in general terms; make sure that's still true.
- [ ] Product names in "Before the day" and slide 27 (Copilot, Gemini and so on).
- [ ] The trust tool game is up and its corner names still match the deck.
- [ ] The feedback form link for this run (slide 35 notes).
- [ ] Rebuild: `python3 build/build.py`, then commit `docs/`.

## After the day

- Send the course site link and the field guide PDF to participants.
- Note which exercises ran long and which scenarios split the room; update the card-vote list above.
