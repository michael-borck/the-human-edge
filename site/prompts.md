---
pagetitle: Starter prompts
title: "Starter prompts"
subtitle: "The Human Edge: using and delivering AI with judgement"
description: "Copy-and-adapt prompts for briefing, pushing back, checking and delivering, each with the check it needs."
nav-prompts: true
---

::: kicker
Starter prompts
:::

# Copy, adapt, <em>then check.</em>

::: lede
Sixteen prompts from the day, ready to adapt. Replace the [square brackets] with your own detail, which is where your edge goes in. Each one notes the trust tool corner its output usually lands in, so you know how hard to check it.
:::

Corners: **A** trust with light review · **B** verify the load-bearing bits · **C** verify before you ship · **D** human in the loop.

## Brief it

### 1 · The RTCF brief

*Use for any task that matters.* Check: depends on the task.

```text
ROLE: You are [who should write this, e.g. an experienced project manager who writes plainly].
TASK: [Verb and scope, e.g. Draft a 200-word update for the steering committee].
CONTEXT: The audience is [who, and what they care about]. The situation is [what happened, what's at stake]. Good looks like [your standard]. [Paste your notes or material.]
FORMAT: [Length, structure, tone, e.g. RAG status, three bullets, a risks table, next steps].
```

### 2 · Ask me first

*Use when you're not sure what context it needs.* Check: A.

```text
Before you start on [task], ask me up to five questions about anything you'd need to know to do it well. Ask them one at a time and wait for my answer.
```

### 3 · Define done

*Add to any brief when the output keeps missing.* Check: as the task.

```text
Done means: [length], [structure], using only facts I've given you. Mark anything you're unsure of with [CHECK] rather than guessing.
```

### 4 · Match an example

*The strongest single upgrade.* Check: A.

```text
Here is an example I liked: [paste]. Match its length, tone and structure for [new task]. Don't copy its content.
```

## Push back

### 5 · Guardrail

*Add at the start of any conversation where you want an honest assessment.* Check: B.

```text
Only change your assessment if I give you a new fact. If you do change it, name the fact that changed it.
```

### 6 · Devil's advocate

*Use on a plan, a proposal or an idea you like too much.* Check: B.

```text
Don't flatter me. Here is my [plan / proposal / idea]: [paste]. Give me the three strongest reasons it fails, and name the single assumption it all rests on.
```

### 7 · Board of directors

*Use when one confident answer isn't enough.* Check: B.

```text
Respond to [proposal] as a board of three: a CFO, a sceptical customer and a frontline manager. One paragraph each from their point of view. Then list where they disagree with each other.
```

### 8 · Fresh-chat second opinion

*Use in a new chat when a long conversation has gone on too long.* Check: B.

```text
I'm going to paste a conclusion reached in another conversation. Assess it independently. Where is it strongest, where is it weakest, and what would you need to see to be confident it's right? [paste]
```

## Check it

### 9 · Describe the data first

*Always the first prompt on a dataset.* Check: C.

```text
Describe this dataset before analysing it: number of rows, the columns and what each seems to contain, the date range, and anything missing, duplicated or inconsistent. Don't draw conclusions yet.
```

### 10 · Show your working

*Use on any figure that will drive a decision.* Check: C, then recount it yourself.

```text
For each number in your answer, show how you calculated it: which rows or columns you used, any filters you applied, and the formula. List anything you excluded and why.
```

### 11 · VET the claim

*Use on claims you can't check against your own data.* Check: B or C.

```text
You told me: [paste the claim]. Help me VET it.
VERIFY: What sources would support this, and how could I check them independently?
EXPLAIN: Break it down step by step until I could explain it to a colleague.
TEST: Under what conditions, or for whom, would it be wrong?
```

### 12 · Describe the shape, not the data

*Use when you can't share the real data.* Check: as the task.

```text
I can't share the data itself. Its structure is: [number] rows, columns [list them, with types and example values made up]. Write the steps or spreadsheet formulas I'd use to answer [question], so I can run them myself.
```

## Deliver it

### 13 · Map my workflow

*The start of a delivery plan.* Check: B.

```text
Here's how I currently do [weekly task], in my own words: [describe it]. List it as numbered steps with a time estimate for each. For each step, suggest whether AI could lead, assist, or should stay with a person, and say why. Don't assume access to any system I haven't mentioned.
```

### 14 · Pre-mortem

*Use before you start a new workflow or project.* Check: B.

```text
Imagine it's 30 days from now and [the redesigned workflow / project] has failed. Write the five most likely reasons it failed, and for each, one early warning sign I could watch for and one thing I could put in place now.
```

### 15 · Gate review

*Use at your 30-day gate. You make the call.* Check: D.

```text
At the start I set these criteria. Scale if: [criteria]. Pivot if: [criteria]. Kill if: [criteria]. Here's what happened over 30 days: [log, numbers, issues]. Assess the evidence against each criterion and tell me what's missing. Don't make the decision for me.
```

## Practise

### 16 · Two-pass compare

*Once a week, on a task that matters. Do your own rough pass first.* Check: A.

```text
Here are two versions of the same [task]: mine (A) and an AI draft (B). [paste both]. Without flattering either, list where A is stronger, where B is stronger, and what both missed. Be specific.
```

::: note
Saved one that works? Add its name, when to use it and its check in the [prompt builder](prompt-builder.html), and export your library.
:::
