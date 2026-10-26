# Exercise 2: Prompt Engineering Workshop, Facilitator Guide

**Duration:** 60 minutes (11:30 AM - 12:30 PM)
**Frameworks used:** RTCF Prompt Framework
**Core learning:** Structured briefs produce dramatically better output than naive prompts, because the brief supplies what the tool can't: your context, your intent, your standard. Conversation, not delegation.

---

## Pre-Exercise Setup

**Materials needed:**
- Prompt Engineering Worksheet (1 per participant, printed)
- Frameworks Reference Sheet (already distributed)
- Projector showing RTCF framework as a reminder

**Room check:**
- Participants should already have AI tools open from Exercise 1
- RTCF framework should be clearly visible (projector or whiteboard)

---

## The Exercise Structure

Three rounds, each building on the previous:

| Round | Time | What Happens | Purpose |
|-------|------|-------------|---------|
| **Round 1: Baseline** | 15 min | Naive prompts → see what you get | Feel the pain of vague prompting |
| **Round 2: Apply RTCF** | 20 min | Structured prompts → compare improvement | Experience the framework's value |
| **Round 3: Advanced** | 15 min | Chain-of-thought, iteration, multi-turn | Stretch skills further |
| **Debrief** | 10 min | Share best prompts, discuss lessons | Consolidate learning |

---

## Setup (5 min), 11:25 AM

Distribute the Prompt Engineering Worksheet (if not already distributed).

**Your script:**

> "You have a worksheet with 3 workplace scenarios (pick 2). Each one gives you a realistic situation and enough context to write a good prompt. Here's how this works:
>
> **Round 1:** Pick 2 scenarios. For each one, write the prompt you'd naturally write, the first thing that comes to mind. Type it into your AI tool and note the quality of the output. Don't try to be fancy. Write what you'd normally write.
>
> **Round 2:** Go back to the same 3 scenarios. This time, brief the AI properly, the mindset is conversation, not delegation: you're briefing a capable junior colleague who knows nothing about your job. Use the RTCF structure, Role, Task, Context, Format, and compare the output to Round 1.
>
> **Round 3:** Pick your best scenario and try an advanced technique, I'll explain those when we get there.
>
> The goal is to feel the difference between a vague request and a proper brief. Ready? Start Round 1 now."

---

## Round 1: Baseline (15 min), 11:30 AM

**What participants do:** Choose 3 of 6 scenarios, write quick natural prompts, note output quality.

**Your role:** Circulate and observe. **Do not help them write better prompts yet.** This round is about experiencing the gap.

**What you're looking for:**

| Sign | What It Means |
|------|--------------|
| "This is pretty generic" | They're noticing the problem, good |
| "It didn't include [thing I needed]" | They didn't give context, they'll see why in Round 2 |
| "Actually this is decent" | Some tasks with simple requirements do get decent output from naive prompts, that's real too |
| Frustration | Good, they'll appreciate the framework more |

**Things to say while circulating:**
- "Don't worry about quality yet, just note what you get"
- "Rate it honestly: would you send this as-is?"
- "Save your Round 1 output, you'll compare it to Round 2"

**Don't:**
- Suggest improvements to their prompts (not yet)
- Help them rewrite (that's Round 2)
- Spend too long at one table, keep moving

**At 11:45, call time:**

> "Stop where you are. You should have tried at least 2 scenarios. How was the output? [Take a few quick reactions, don't spend more than 1 minute on this.] Now let's see what happens when we add structure."

---

## Round 2: Apply RTCF (20 min), 11:45 AM

**Your script:**

> "Go back to the same scenarios. This time, use the RTCF framework. For each prompt, fill in the table on your worksheet:
>
> - **Role:** Who should the AI be? Be specific, not just 'a writer' but 'a senior project manager with experience communicating with executives.'
> - **Task:** What exactly should it do? Include the verb and the scope.
> - **Context:** What does the AI need to know? Audience, background, constraints, tone.
> - **Format:** How should the output look? Bullet points, table, email format, word count.
>
> Same scenarios. Same AI tools. Different prompts. Go."

**Your role:** Now you can help. Circulate and:

**Coach prompt-writing:**
- "What's missing from your Context? Who's the audience?"
- "Your Task is still pretty vague, what specifically should the AI produce?"
- "Try adding a Format, right now you're letting the AI decide how to structure the output"

**Spot great examples:**
- When someone gets a dramatically better result, ask if you can share it in the debrief
- Note which RTCF components made the biggest difference for different scenarios

**Watch for common mistakes:**
| Mistake | Your Coaching Move |
|---------|-------------------|
| Role is too generic ("You are an expert") | "Expert in what? The more specific, the more it shifts the output" |
| Task is a topic, not an action ("About the project delay") | "What should the AI DO with the project delay? Summarise? Draft an email? Create a plan?" |
| Context is missing entirely | "Imagine you're briefing a brand-new colleague. What would they need to know to do this task?" |
| Format is missing | "If I sent you this output, how would you want it structured? Tell the AI that." |
| Prompt is 3 paragraphs long | "Good, detailed is better than vague. But check: is everything in there necessary?" |

**At 12:05, call time:**

> "Finish the prompt you're working on. Compare your Round 1 and Round 2 outputs side by side. How big is the difference?"

**Quick pulse check (1 minute):**

> "Hands up if your Round 2 output was significantly better than Round 1." [Most hands should go up.]
>
> "Hands up if there was barely any difference." [If anyone raises a hand: "Interesting, let's look at your prompts during the debrief. You may have been naturally detailed in Round 1, or there might be something we can tweak."]

---

## Round 3: Advanced Techniques (15 min), 12:05 PM

**Your script:**

> "Now pick your best scenario, the one where you got the best Round 2 result. We're going to push further with four advanced techniques. Try at least one:
>
> **Technique 1: Chain-of-thought.** Before the AI writes the output, ask it to think through the problem step by step. For example: 'Before writing the email, think step-by-step about what David is really concerned about, what his priorities are, and what tone would be most effective. Then write the email.'
>
> **Technique 2: Multiple versions.** Ask the AI to generate 2-3 different versions and explain the trade-offs. 'Write three versions of this email: one that's very direct, one that's empathetic, and one that's diplomatic. Then tell me which you'd recommend and why.'
>
> **Technique 3: Self-critique.** After getting an output, ask the AI to evaluate its own work. 'Review what you just wrote. What's weak? What would a senior executive find unconvincing? Rewrite to fix those issues.'
>
> **Technique 4: The fact-gated guardrail.** When the AI critiques your work, or you push back on its critique, add this: 'Only change your assessment if I give you new facts credible enough to change it. And when you do change it, tell me which fact changed it and why.' This stops the AI from folding just because you insisted. It has to either defend its analysis with reasons or name the fact that moved it. Watch what happens when you push back without new facts, it should hold its ground.
>
> Try one. See what happens."

**Your role:** This round is more exploratory. Let them experiment.

**For advanced participants:** Challenge them to combine techniques, chain-of-thought AND self-critique, for example. Technique 4 pairs especially well with self-critique: they'll see the model defend a weakness it just named unless they bring actual evidence. That's sycophancy training turned into a game.

**For struggling participants:** Suggest Technique 2 (multiple versions) as the easiest to try, it just requires adding one sentence to their existing prompt.

---

## Debrief (10 min), 12:20 PM

**Question 1: "What was the single biggest improvement from Round 1 to Round 2?"**

Listen for:
- "The output was actually usable instead of generic"
- "It got the tone right because I told it who the audience was"
- "Adding format meant I could paste it straight into my document"

**Your move:** Draw out 3-4 examples. Ask: "Which RTCF component made the most difference?" (Usually Context or Format.)

**Question 2: "Did anyone find a scenario where RTCF didn't help much?"**

Listen for:
- Very simple tasks where a naive prompt was already sufficient
- Tasks where the AI lacks real knowledge regardless of prompting

**Your move:** Validate this. "Not every task needs all four components. A simple 'summarise this into 3 bullet points' might only need Task and Format. The framework is a tool, not a rule."

**Question 3: "What happened in Round 3?"**

Listen for:
- Chain-of-thought produced more nuanced responses
- Multiple versions revealed options they hadn't considered
- Self-critique caught issues they would have missed

**Your move:** Highlight that iteration is the real skill. "The best prompters don't write one perfect prompt, they write a good prompt, evaluate the output, and refine. It's a conversation, not a command."

**Close the debrief:**

> "Before lunch, I want you to do one thing: save your best prompt from today into the template library at the bottom of your worksheet. This is the start of your personal prompt collection. Over time, you'll build a library of templates for your common tasks."

---

## Common Facilitation Moves

| Situation | Your Move |
|-----------|-----------|
| Someone's Round 2 isn't much better than Round 1 | Look at their prompts together, usually Context or Role is still missing. Coach in real-time. |
| Someone gets a perfect Round 1 output | Ask: "Were you already applying structure naturally? That's a strength. Try a harder scenario." |
| A table is working silently | Prompt discussion: "Share your Round 1 vs Round 2 with your neighbour. What's different?" |
| Someone is trying all 6 scenarios | Redirect: "Depth over breadth, pick 2 and really refine them." |
| The room is high-energy, lots of sharing | Let it run. This is the best part of the exercise. |
| Someone's AI gave an offensive or biased response | Address it: "This is real. AI reflects patterns from its training data, including biases. What would you do if this happened at work?" |

---

## Success Indicators

- [ ] Clear, visible improvement from Round 1 to Round 2 for most participants
- [ ] Participants can name which RTCF component made the biggest difference
- [ ] At least some participants tried and benefited from Round 3 techniques
- [ ] The debrief generated sharing of specific prompts (not just general impressions)
- [ ] Participants saved at least one prompt to their template library

---

## Your Checklist

**Before (11:20 AM):**
- [ ] Worksheets distributed
- [ ] RTCF framework visible on projector or whiteboard
- [ ] Confirmed all participants have working AI tool access

**During:**
- [ ] Did NOT help during Round 1 (let them feel the gap)
- [ ] Actively coached during Round 2 (helped with RTCF application)
- [ ] Circulated to all tables during each round
- [ ] Noted strong examples for the debrief

**After:**
- [ ] Debriefed with all three questions
- [ ] Prompted participants to save best prompt to template library
- [ ] Connected to afternoon: "You'll use RTCF again in the data analysis exercise"
