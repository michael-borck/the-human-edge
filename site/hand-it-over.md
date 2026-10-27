---
pagetitle: Hand it over
description: "Teach one decision to decide like you: the sort, the three extraction paths, the lean skill, the blind test, the patch and the cold rerun. Method after Dylan Davis."
nav-more: true
---

::: kicker
Hand it over
:::

# Teach it to decide like you. <em>Then prove it blind.</em>

::: lede
The course taught you to check everything AI produces. This is the step further: one decision you make twice, externalised into a lean, reusable skill — and proven against your own record before it decides anything that matters. The method is Dylan Davis's; the wording here is ours.
:::

::: note
**Before anything else:** this only suits decisions that are repeatable, explainable, and checkable against history. If a call is different every time, or rests on accountability you can't hand over, it stays in the top-right corner of the trust tool. Automating a decision doesn't move it out of the grid.
:::

## The sort

One diagnostic question routes you: **could you explain the *why* to a new hire, out loud, right now?**

| Your answer | Path | How it works | What you get |
|---|---|---|---|
| Yes, easily | **Say it** | Dictate the reasoning — out loud, not typed. Typing edits; talking keeps the exceptions, the tells and the gut checks. Then it asks three to five follow-up questions, one at a time. | Your process, with the edge cases caught |
| "It depends" | **Interview it out** | It interviews you: one question at a time, each answer shaping the next, until every "it depends" has become an if-then branch. Fifteen to twenty questions is the working range. | Explicit if-then rules for each branch |
| No, but it's written down | **Mine it** | Your history holds the rules: sent folder, quotes, approvals, rejections. It reads past input-decision pairs and extracts the patterns — including rules you never stated and the losses you repeat. | Reverse-engineered rules from real choices |

The branch is the judgment. "Discount? It depends" becomes: *if they're new, hold the price; if it's year five and renewal is at risk, flex to keep them.* That map is what you're extracting.

## Install it

In the **same conversation** where the rules came out, so it keeps the context:

```text
Turn these decision rules into a lean, reusable skill I can apply to any future case of this decision. Strip out every example, name and number we used. Keep only the logic.
```

Then make it **lean**. A model's attention is finite: a prompt padded with prose, history and examples dilutes the weight on the rules that matter. One screen of structured if-then beats three pages of explanation. Save it as a skill, a project instruction, or your custom instructions — it's the finished draft of the prompt library from Exercise 4.

## Prove it blind

This is the step that makes the handover safe, and the one people skip. The skill must make calls you already know the answer to, without knowing the answers.

1. **Choose three to five past cases.** Real ones, spanning routine, complex and edge. More than five is overhead; fewer than three proves nothing.
2. **Write the inputs only.** The email, the figures, the résumé — what you saw at the time. No outcomes, no commentary.
3. **Write your calls down first.** From memory, before running anything. Hidden outcomes are the whole test.
4. **Run it cold**, in a fresh chat with the skill installed. Require a decision *and* the rule it relied on, in three steps of reasoning.

Then compare:

| Case | Its call | Your call | Verdict |
|---|---|---|---|
| 1 | Reject — below minimum deal size | Reject | Match |
| 2 | Approve — tenure over three years | Approve | Match |
| 3 | Decline — credit variance flags it | **Approve** — volume over $200k waived it | **Mismatch** |

A mismatch is not the skill failing. It's your unstated rule surfacing. Every split falls into one of three classes:

- **A missing boundary rule** — you used a threshold you never said out loud.
- **An unstated exception** — a precedent or context you weigh without noticing.
- **A weighting error** — it applied as absolute a rule you hold loosely.

Four out of five, with a clean patch on the fifth, is a good day. Don't chase a hundred percent in one sitting; the point of the test is what it teaches you about your own rules.

## Patch, then rerun cold

Patch surgically: add the missing rule as a condition, change nothing else, add no prose. Then the non-negotiable part — **re-test in a brand-new chat**. In the interview thread, the model has watched you decide; a skill re-tested there gets credit for context, not rules, and passes falsely. Cold thread, whole batch, every case.

One honest caveat: models aren't deterministic. The same inputs can flip on a rerun. One flip isn't a broken skill — judge the batch, and re-test any case that matters before you rely on it.

## After sign-off

The skill proposes; you still decide what it may decide.

- **Place each new case on the trust tool.** The skill inherits your rules, not your accountability.
- **Keep a human checkpoint where the stakes are large**, and tell people when a skill decided something that affected them.
- **Set a 30-day gate**, same as any workflow: is it holding, does the checking cost more than it saves, scale or kill?
- **Revisit each quarter.** The corners move, your rules drift, and the skill should be re-proved when either does.

::: note
**Governance first.** Mining your history means showing your history to a tool — classify before you paste, or describe the patterns instead. And expect the skill to praise itself; sycophancy is why the test is blind and the outcomes stay hidden until after its calls.
:::
