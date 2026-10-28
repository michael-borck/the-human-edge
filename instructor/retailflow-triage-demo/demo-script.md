# Ticket Triage Demo: Run of Show

**Where it fits:** Session 4, on the "Agents run the loop" slide (37), or on "Test it blind" (27) in Session 3. **Time: 3 minutes maximum.** It is a flourish, not an exercise. If anything is unready, skip it; the slide and its talking points carry the content on their own.

---

## The one idea the demo proves

Same model, same prompt. The only thing that changes is a plain-text skill file the harness loads. The model goes from "cannot triage" to producing a clean triage table, because the brief it needed was supplied from outside and stored in the harness. That is the day's whole thesis in one move: the tool returns the form; you supply the substance. A skill is that substance, written once.

---

## Before the day (one-time, on the laptop you present from)

1. Ollama installed with a small model pulled (`ollama pull qwen3:4b` is plenty; triage is not a hard task). Test it boots from the presentation laptop and the venue power; a local model needs no venue wifi, which is itself a talking point.
2. Pi installed and connected to the local model (`ollama launch pi`).
3. Do **not** pre-install the skill. The before-shot (model failing to triage) only lands if the audience sees it live or on screen.
4. If the presentation laptop is weak, rehearse and capture screenshots of both halves as a fallback.
5. Model and harness names change quickly. Re-check the install commands the week before each run.

**Fallbacks, in order of preference:**

| Situation | Move |
|-----------|------|
| Model slow on the day | Pre-run both halves and show the two screenshots |
| Pi misbehaves | Demo the skill file in any chat: paste the skill as a system prompt or first message, then the tickets; the before/after still works |
| No time | Skip it. Say the one line from the slide notes and move on |

---

## The demo (3 minutes)

### Beat 1: the baseline, no skill (60 seconds)

Paste into Pi:

```
Ticket 1 (RF-5175, phone): I've been billed twice for my July order. I want the duplicate charge refunded today; I've already called once and nobody called me back.

Ticket 2 (RF-5030, phone): My delivery was due eight days ago. The courier says the parcel is lost. I work from home and this box has my work equipment in it.

Ticket 3 (RF-5149, email): I have tried twice to return my order and the portal keeps failing. This is the worst service I have ever had. I want my money back and I am posting about this online.

Ticket 4 (RF-5189, live chat): Where is my order? The tracking page hasn't updated in three days.

Triage these four tickets.
```

Expected: the bare model waffles. It may answer conversationally, triage one ticket and chat about the rest, or invent a table-shaped guess with no rules behind it. **Say:** "Watch what it does. It has no triage rules. Whatever this is, it is not triage. This is the baseline: a capable model with no brief."

### Beat 2: the skill (30 seconds)

Show the file. It is one page of plain text: a role, four rules, an output format. Point out that it reads like the RTCF briefs they wrote this morning, because it is one.

```
mkdir -p ~/.agents/skills/retailflow-triage
```

Copy `SKILL.md` (this folder) to `~/.agents/skills/retailflow-triage/SKILL.md`, then quit and relaunch Pi (skills are scanned at startup).

### Beat 3: same prompt, now it triages (60 seconds)

Paste the identical tickets again. Expected: one markdown table, all four tickets, categories from the RetailFlow set they saw in Exercise 5, severities, owners, first actions, and an escalation sentence (typically RF-5149, the public-refund risk, and that ticket is a real row from the dataset they analysed: email channel, 20-hour response, satisfaction 1.0).

**Say:** "Nothing about the model changed. The harness loaded a brief. The brief is the substance only we could supply, and now it is written once and reused every morning."

### Beat 4: the trust tool close (30 seconds)

"Would you let this auto-send? Triage is average-shaped and low stakes, so it sits in the light-review corner, but the escalation decision is a real decision, so a person owns it. And if this ran overnight as an agent, the loop would be automated. The standard would not be. Someone still checks the table against reality. That is the whole game."

---

## Details that make it cohere with the rest of the day

- The four tickets match real rows in the Exercise 5 dataset (`retailflow-customer-service-data.csv`): RF-5175, RF-5030, RF-5149, RF-5189. The categories are the dataset's six categories, so the triage output looks like the data participants just analysed.
- The skill's rules section is the dataset's own answer key in miniature: money involved raises severity; the Returns Team owner echoes the Returns & Refunds finding from Exercise 5.
- If someone asks "is this an agent?": not yet. It is a model with a skill; add a loop and tools (read the mailbox, write to the queue) and it becomes one. The skill file does not change.
