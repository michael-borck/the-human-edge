---
title: "Practical AI for Professionals"
subtitle: "A Hands-On Workshop for Using AI in Your Daily Work"
author: "Dr. Michael Borck"
format:
  html:
    embed-resources: true
  pdf: default
  docx: default
  pptx: default
---


# Welcome

![](./images/welcome-human-ai-collaboration.png)

::: {.notes}
- "Welcome to Practical AI for Professionals"
- "Today is about doing, not just listening"
- "Here's the idea the whole day hangs on: everyone in this room has access to the same AI. Same tools, same models. So generic AI competence isn't an advantage anymore, it's the baseline everyone shares. The edge moves to what the tool can't manufacture: your judgement. Knowing what to ask for, when to trust the answer, and where a human stays in charge. That's what we train today."
- "By the end of today, you'll have real skills you can use at your desk on Monday morning"
- "This isn't a course for executives deciding where to invest in AI, and it's not for project managers leading AI projects. Those are the other two courses in this series."
- "This course is for YOU, a professional who wants to use AI tools effectively in your daily work."
:::

---

# About Today

**This is a workshop, not a lecture.**

- You'll spend most of the day with your hands on a keyboard
- You'll use real AI tools on real tasks
- You'll make mistakes, that's where the learning happens
- You'll leave with techniques you can apply immediately

::: {.notes}
- "Look around the room. Some of you have been using ChatGPT for months. Some of you opened it for the first time yesterday. Both are fine."
- "The exercises are designed so everyone can participate regardless of starting point"
- "If you're experienced, there are stretch challenges. If you're new, the basics are powerful."
- "One ground rule: there are no stupid questions. The technology is new and everyone is figuring it out."
:::

---

# Today's Journey

**Timeline for the Day:**

- 9:00-10:30 → **AI Foundations & Orientation**
- 10:30-11:00 → Morning Tea
- 11:00-12:30 → **Prompt & Context Engineering**
- 12:30-1:15 → Lunch & Networking
- 1:15-2:30 → **AI-Powered Data Analysis**
- 2:30-3:00 → Afternoon Tea
- 3:00-4:00 → **AI in Your Workflow**
- 4:00-4:30 → **Personal Action Planning**

::: {.notes}
- "Four sessions, four frameworks, four hands-on exercises"
- "Each session builds on the previous one"
- "By the end: you'll know WHEN to use AI, HOW to talk to it, how to use it with DATA, and WHERE it fits in your actual work"
- "The morning builds skills, the afternoon applies them to your real job"
:::

---

# What You'll Learn

**One spine. Four frameworks. Four exercises. One day.**

**The spine:** The Trust Tool, how much to trust any AI output, on any tool

1. **Know when** to use AI → AI Task Suitability Spectrum
2. **Know how** to brief AI → RTCF Prompt Framework
3. **Know how** to use AI with data → AI-Assisted Analysis Workflow
4. **Know where** AI fits in your work → AI Opportunity Finder

::: {.notes}
- "These aren't academic frameworks. They're practical tools."
- "And there's one thread that runs through all of them: the trust tool. You'll learn it in the next few minutes and use it in every exercise today."
- "By 4:30 you'll have used each one at least once"
- "You'll also have a personal prompt library and a redesigned workflow from your own job"
- "Let's start with the foundation: what is AI, really?"
:::

---

# What AI Actually Is

![](./images/ai-pattern-matching.png)

::: {.notes}
**The Simple Truth: AI Predicts the Next Word**

- "When you type something into ChatGPT or Claude, the AI isn't thinking. It's predicting."
- "It's been trained on billions of pages of text, and it's learned patterns, what word comes after what, what sentences follow what questions, what format fits what request"
- "Think of it as autocomplete on steroids"
- "Your phone predicts one word at a time. These tools predict thousands of words at a time."
- "The result often LOOKS like understanding, but it's pattern-matching"
- "Why does this matter? Because it tells you what AI is good at and what it's bad at."
:::

---

# What AI Is Good At

**Tasks where patterns exist:**

- ✅ Drafting and writing (follows language patterns)
- ✅ Summarising documents (identifies key information patterns)
- ✅ Formatting and transforming (structure is pure pattern)
- ✅ Brainstorming (seen enormous variety of ideas)
- ✅ Explaining concepts (thousands of explanations in training data)
- ✅ Finding patterns in data (what it's literally built to do)

::: {.notes}
- "AI excels at tasks where there are clear patterns to follow"
- "Writing an email? There are billions of email examples in the training data"
- "Summarising a document? AI has seen thousands of summaries"
- "The key insight: if a task has patterns, AI can probably help"
- "But there's a flip side..."
:::

---

# What AI Is Bad At

**Tasks where patterns aren't enough:**

- ❌ Factual accuracy (generates plausible text, not verified truth)
- ❌ Maths and precise calculations (regularly makes arithmetic errors)
- ❌ Logical reasoning (misses contradictions, gets multi-step logic wrong)
- ❌ Understanding YOUR context (doesn't know your company, team, politics)
- ❌ Ethical judgment (no values, no empathy, no accountability)

::: {.notes}
- "This is the critical part. AI NEVER says 'I don't know'"
- "It will give you a confident, well-structured, completely wrong answer"
- "This is called hallucination, and it's the biggest risk of using AI carelessly"
- "If you only remember one thing from this morning: AI output needs human verification. Always."
- "Let me show you an example of each tool handling the same task differently..."
:::

---

# The "Confident Nonsense" Problem

**AI never says "I don't know."**

Ask a colleague → "I'm not sure, let me check"

Ask AI → Confident, well-structured, completely wrong answer

**This is called hallucination.**

::: {.notes}
- "Hallucination isn't a bug that will be fixed. It's a fundamental property of how these tools work."
- "If the AI hasn't seen enough examples of something, it generates the most plausible-sounding text, which may be entirely fabricated"
- "It will cite academic papers that don't exist. It will invent statistics. It will create fake legal precedents."
- "The rule: verify facts, especially numbers, names, quotes, and references"
- "Here's the deeper point: hallucination isn't the exception. Everything AI produces is a version of this, a convincing average. Let me show you what I mean."
:::

---

# The Convincing Average

**AI produces a convincing average: fluent, well-shaped, usually about right.**

But "about right" and "exactly right" are not the same,
**and knowing which one you need is the whole game.**

**And here is the trap: weak human work announces itself.**

A rushed human draft looks rushed. Gaps show. Sloppiness shows.

AI's wrong work announces nothing: polished, complete, confident.

**Your inner alarm stays quiet exactly when you need it most.**

::: {.notes}
- "This is the single most useful thing to understand about today's AI"
- "It gives you back the most plausible, most typical response drawn from everything it has seen. That's its genius and its limit in one."
- "Most of the time, the average is genuinely useful: a first draft, a summary, a starting point"
- "But sometimes you need exactly right: a contract figure, a citation, an account balance. And on those, the average is just a confident guess that looks like an answer"
- "Here's the trap, and it's worth dwelling on: you have a lifetime of training at spotting weak work, because weak human work announces itself. Rushed work looks rushed. Gaps show. Sloppiness shows. Your alarm is well calibrated for people."
- "AI's wrong work announces nothing. It's polished, complete, confident. The error signals you've relied on your whole career are gone. Your alarm stays quiet exactly when you need it most."
- "So the skill of this day is not typing clever prompts. It's running the check your alarm can no longer run for you."
- "So: how do you know when an average is fine and when it isn't? You need a tool. Here it is."
:::

---

# The Trust Tool

**Two questions. Four corners.**

**Q1: Do you need an AVERAGE, or PRECISION?**

**Q2: Are the stakes SMALL, or LARGE?**

|  | **Small (low stakes)** | **Large (high stakes)** |
|---|---|---|
| **Average is fine** | **Lean in.** Let AI run. | **Lean in, with a glance.** Sanity-check before it goes out. |
| **Precision required** | **Use, then verify.** Confirm the specifics. | **Human in the loop.** A person owns the decision. |

::: {.notes}
- "This is the trust tool: Average/Precise crossed with Small/Large. It's the spine of everything we do today."
- "Walk the corners: internal email draft, average, small stakes, lean in. Board paper numbers, precision, large stakes, a human owns every figure."
- "The rule of thumb: lean in where 'about right' over low stakes is fine; keep a human in the loop where exactly-right meets high stakes."
- "Here's the part that makes this durable: verification comes from OUTSIDE the tool. Asking the AI to check its own work doesn't count, it will happily agree with itself. The check is yours: against the data, the source, the standard. That's not an AI skill. It's an old professional skill, and it's what makes you the edge."
- "This grid works on any tool, ChatGPT, Claude, Gemini, whatever ships next year. It doesn't expire when the next model does."
- "Now let's look at a framework for deciding which tasks to bring to AI in the first place."
:::

---

# Framework 1: AI Task Suitability Spectrum

![](./images/task-suitability-spectrum.png)

::: {.notes}
**The question: "Should I use AI for this?"**

**Four zones:**

- **AI-Led**: Routine, pattern-based tasks. AI does the heavy lifting, you review. Example: formatting notes into meeting minutes.
- **AI-Assisted**: Tasks requiring your judgment, but AI provides substantial help. Example: drafting a client proposal.
- **Human-Led, AI-Supported**: Complex tasks where AI handles sub-parts. Example: strategy document where AI helps with research and formatting.
- **Human-Only**: Tasks requiring empathy, ethics, novel judgment. Example: difficult conversation with a team member.

"The first question to ask with any task: where does it sit on this spectrum?"
"When in doubt, start with more human involvement and delegate to AI as you build trust."
:::

---

# The Four Zones

| Zone | AI Does | You Do |
|------|---------|--------|
| **AI-Led** | Heavy lifting | Review and approve |
| **AI-Assisted** | Substantial help | Guide and verify |
| **Human-Led** | Sub-tasks | Lead the work |
| **Human-Only** | Nothing | Full ownership |

::: {.notes}
- "The key skill is classification, quickly deciding which zone a task belongs in"
- "Most professionals will spend most of their time in the middle two zones"
- "AI-Led tasks are your quick wins, start there"
- "Human-Only tasks are where your value is irreplaceable, protect those"
- "Let's test this with real AI tools..."
:::

---

# Exercise 1: AI Tool Test Drive

![](./images/tool-comparison.png)

**Same task. Three tools. Compare the results.**

::: {.notes}
**What you'll do:**

1. I'm giving you a single workplace task
2. Type the EXACT same prompt into 2-3 different AI tools
3. Compare the outputs: what's different? What's better? What did any tool get wrong?

**The task (display on projector):**

"I manage a team of 8 people in a mid-sized company. One of my team members, who has been a strong performer for 3 years, has been consistently late to work and missing deadlines for the past month. Other team members are starting to notice. Write me a plan for how to address this situation."

- "You have 10 minutes to run the prompt, then 10 minutes to discuss at your table, then we'll debrief"
- "Don't modify the prompt, we want to see how different tools handle the same input"
- "Go."
:::

---

# What Did You Find?

**Three questions:**

1. What surprised you about the differences?
2. Did any tool give bad advice?
3. Which response would you actually use?

::: {.notes}
**Debrief (15 min):**

- Draw out 3-4 observations about differences (tone, structure, content, gaps)
- Spotlight any bad advice or hallucination, this is the highlight
- Connect to the Suitability Spectrum: "This scenario is Human-Led, AI-Supported. The AI helps you think, but the conversation is yours."
- Now apply the trust tool: "Where did an average suffice? Where did the output land in the precision quadrant, and did anyone actually check anything? Hold that thought."
- Name what they just did: "This exercise has a name: the compare habit. One task that matters, your rough pass, AI's pass, side by side. Every gap teaches you something. Where you beat it shows your strength. Where it beat you shows its limit. It is the highest-value practice move available, and it takes minutes."

**Key message:**
- "There's no objectively 'best' tool. Different tools suit different tasks."
- "What matters is that you try a few, find what works, and NEVER assume the first output is ready to use."

**Bridge to Session 2:**
- "You just saw what happens with a basic prompt. After the break, we'll learn how to dramatically improve what you get back, and the reframe might surprise you. It's less about clever words than you think."
:::

---

# The Art of Effective Prompting

![](./images/garbage-in-garbage-out.png)

**Conversation, not delegation: brief it like a capable junior colleague.**

::: {.notes}
- "This is the most important lesson of the day"
- "Most people type vague prompts and get vague results, then blame the tool"
- "Here's the reframe that makes prompting click: you are NOT casting a spell. There are no magic words. You are briefing a capable junior colleague, one who is smart, fast, and knows nothing about your job"
- "What would you tell a talented new hire before they drafted the client email for you? Who it's for. What happened last month. What good looks like. That's exactly what belongs in your prompt"
- "The tool produces the form of the work, the shape of an email, the structure of a summary. The substance, your intent, your context, your standard, only you can supply. The briefing is where you supply it."
- "The framework that follows makes the briefing repeatable"
:::

---

# Framework 2: RTCF Prompt Framework

**The briefing structure:**

**R**: Role (Who should the AI be?)

**T**: Task (What exactly should it do?)

**C**: Context (What does it need to know?, *the grounding only you can supply*)

**F**: Format (How should the output look?)

::: {.notes}
- "RTCF. Role, Task, Context, Format."
- "Think of each as part of the brief you'd give that junior colleague"
- "Not every prompt needs all four. A simple task might only need Task and Format."
- "But for anything important, all four dramatically improve the result."
- "Context deserves special attention: it's the part the AI genuinely cannot do for itself. It doesn't know your company, your client, your politics. The context component is where your value enters the machine."
- "Let me show you the difference..."
:::

---

# Before and After

**Without RTCF:**
> "Write an email about the project delay"

**With RTCF:**
> **Role:** Senior project manager, professional and empathetic
>
> **Task:** Write a client email explaining a 2-week delivery delay
>
> **Context:** Delay caused by vendor API integration. Client is understanding but values transparency. New delivery date March 15.
>
> **Format:** Under 200 words. Acknowledge → Explain → New date → Recommit.

::: {.notes}
**Do a LIVE DEMO here.**

1. Open an AI tool on the projector
2. Type the "without RTCF" prompt, show the generic result
3. Then type the "with RTCF" prompt, show the dramatically better result
4. Ask the room: "Which email would you actually send?"

- "The first one is generic filler. The second one is close to what you'd actually send."
- "The investment: 60 seconds writing a better prompt. The return: saving 30 minutes of rewriting."
- "Now it's your turn."
:::

---

# RTCF Quick Reference

| Component | Ask Yourself | Example |
|-----------|-------------|---------|
| **Role** | Who should the AI be? | "Senior financial analyst" |
| **Task** | What exactly should it do? | "Create a variance analysis" |
| **Context** | What does it need to know? | "For the CFO, 2-minute summary" |
| **Format** | How should the output look? | "Table: Category, Variance, Explanation" |

::: {.notes}
- "Keep this visible. You'll use it in every exercise for the rest of the day."
- "The most commonly missed components are Context and Format"
- "Role is powerful because it shifts the AI's entire approach, a 'financial analyst' writes differently than a 'marketing copywriter'"
- "Context tip worth stealing: a stakes line. 'Write this for someone who has to decide this week and can't undo it.' Real stakes in the Context sharpen everything that follows, no theatrical personas needed, just honest consequences."
- "Let's practise."
:::

---

# Exercise 2: Prompt Engineering Workshop

![](./images/prompt-workshop.png)

**Three rounds. Same scenarios. Better prompts.**

- **Round 1 (15 min):** Write a natural prompt. See what you get.
- **Round 2 (20 min):** Apply RTCF. Compare the improvement.
- **Round 3 (15 min):** Advanced techniques: chain-of-thought, multiple versions, self-critique, fact-gated pushback

::: {.notes}
- "Pick 3 of the 6 scenarios on your worksheet"
- "Round 1 is deliberately unstructured, write whatever comes naturally"
- "In Round 2, use RTCF. Fill in the table on your worksheet for each prompt."
- "Round 3 is a stretch, try asking the AI to think step-by-step before answering, or to generate multiple versions, or to critique its own work. My favourite: the fact-gated guardrail. Tell it 'only change your assessment if I give you new facts, and name which fact changed it.' Then push back with no evidence and watch whether it folds or holds its ground. That's how you keep a tool agreeable by training honest."
- "Start with Round 1 now. You have 15 minutes."
:::

---

# Prompt Engineering: Key Lessons

**What you just experienced:**

1. **Specificity wins**: vague prompts produce generic output
2. **Context is king**: the AI doesn't know what you don't tell it
3. **Format saves time**: specify output structure and paste directly
4. **Iteration beats perfection**: treat first output as a draft

::: {.notes}
**Debrief (10 min):**

- "What was the single biggest improvement from Round 1 to Round 2?"
- "Which RTCF component made the most difference?" (Usually Context or Format)
- "What happened in Round 3? Did chain-of-thought or self-critique improve things further?"

**Key message:**
- "The best prompters don't write one perfect prompt, they write a good prompt, evaluate the output, and refine"
- "Before lunch, save your best prompt to the template library on your worksheet"
:::

---

# Using AI for Data Work

![](./images/data-analysis-workflow.png)

::: {.notes}
- "This afternoon is about application"
- "First: using AI to analyse data"
- "AI can find patterns in spreadsheets, create visualisations, run analysis, and summarise findings"
- "But, and this is critical, AI makes arithmetic errors, confuses correlation with causation, and sometimes invents data points"
- "You need a process. That's Framework 3."
:::

---

# Framework 3: AI-Assisted Analysis Workflow

**Six steps:**

**Prepare** → Define the question first

**Upload** → Get data into the AI tool

**Question** → Ask progressively deeper questions

**Verify** → Cross-check findings against what you know

**Refine** → Iterate based on results

**Present** → Format for your audience

::: {.notes}
- "The most common mistake: skipping Prepare and jumping straight to Upload"
- "If you don't know what question you're answering, you can't evaluate whether the AI's answer is good"
- "Two parts to Prepare people miss: write the question down, and start a FRESH chat. Long conversations drift, after enough back-and-forth, the model has absorbed your framing and slowly stops challenging you. A fresh chat gives you an independent read."
- "The most important step: Verify. AI is fast but unreliable with numbers."
- "The discipline of checking is what separates useful AI-assisted analysis from dangerous AI-assisted analysis"
:::

---

# The Verification Step

**If a finding would change a decision, verify it, from outside the tool.**

Asking the AI to check its own work doesn't count. The check is yours.

AI analysis errors to watch for:

- Miscounting rows (especially with filtered data)
- Confusing correlation with causation
- Ignoring missing data without flagging it
- Producing mathematically impossible results
- **Inventing data points that aren't in the source**

::: {.notes}
- "AI finds patterns fast, but humans decide what patterns mean"
- "Here's the trust tool again: a number that will drive a decision is PRECISION. 'About right' is the same as wrong there, no matter how good the sentence looks."
- "And note the direction of the check: asking the model 'are you sure?' doesn't count. It will reaffirm its own answer. The check must come from outside, against the data, the source, an independent standard. That's an old professional skill, not a new AI skill."
- "Same reason you start a fresh chat for analysis: a long conversation drifts toward your view. By message twenty, you're not getting an independent assessment anymore, you're getting your own opinion echoed back with better grammar."
- "Spot-check totals and averages. Compare to what you already know."
- "If the AI says something surprising, that's either a genuine insight or a convincing fake. Your job is to figure out which."
- "In this exercise, you'll get to practise exactly that, with some claims that have been planted for you..."
:::

---

# Exercise 3: Data Analysis Challenge

![](./images/data-challenge.png)

**260 customer service tickets. 3 business questions. AI-assisted analysis.**

1. What are the top 3 drivers of customer dissatisfaction?
2. Are there patterns in when response times blow out?
3. What would you recommend to the customer service manager?

**Then: the Verification Challenge, three claims about this data. At least one is wrong.**

::: {.notes}
- "You have the RetailFlow customer service dataset, 6 months of ticket data"
- "Upload it to your AI tool and follow the Analysis Workflow on your worksheet"
- "Work individually or in pairs. Start by asking the AI to describe the dataset."
- "You have 20 minutes of working time, then the Verification Challenge, then we'll debrief"
- "Remember: Prepare your question, Upload, Question progressively, Verify, Refine, Present"
- "The Verification Challenge: your worksheet has three 'insights' about this data. Each sounds professional and plausible. At least one is wrong, and at least one is stated wrong. Trust nothing on fluency, verify against the data itself."
- "The brief at the end should be something you could hand to a real manager"
:::

---

# What the Data Told Us

**Key patterns you should have found:**

- Returns & Refunds: lowest satisfaction by far
- Delivery Problems: second worst
- Response time is a cross-cutting driver
- Sundays and Mondays: response times blow out
- December: holiday rush, no extra capacity
- Email: 3x slower than Live Chat

**The Verification Challenge verdicts:**

| Claim | Verdict |
|-------|---------|
| "Email ~3x slower than Live Chat" | ✅ Verified |
| "Account Issues: lowest satisfaction, most complex" | ❌ Refuted, twice |
| "Sundays: more than double the average" | ⚠️ Overstated (~1.5x, not 2x) |

::: {.notes}
**Debrief (10 min):**

- "What were the top drivers of dissatisfaction?" [Returns & Refunds, Delivery Problems, response time]
- "When do response times blow out?" [Sundays, Mondays, December, Email channel]
- "Did anyone catch the AI getting something wrong?" [THIS IS THE KEY QUESTION]
- If someone caught an error: spend time on it. This is the verification lesson.
- If nobody verified: "If you didn't verify, you don't actually know if those findings are correct."

**Then the claim reveal, take a vote per claim before revealing:**
- Claim A verified: 13.2h vs 4.0h is 3.3x. Accurate.
- Claim B refuted TWICE: Returns & Refunds is lowest (~1.6 vs ~3.1), and Account Issues actually has the HIGHEST resolution rate (~96%), so "most complex" collapses too. This is the convincing fake: plausible mechanism, professional tone, wrong on the data. If forwarded to Karen, she'd fix the wrong thing.
- Claim C overstated: 13.7h vs 9.2h overall is 1.5x, not 2x. Directionally right, number wrong. Trust tool check: that number drives a staffing decision, precision quadrant. Close is the same as wrong.

**The landing:**
- "Claim B is the one to remember. Fluent, professional, plausible, and wrong. That's what AI failure looks like: not nonsense, but a convincing average. The form of insight without the substance. The substance, the check, comes from outside the tool. That's your edge."

**Bridge:**
- "You just did in 25 minutes what would have taken hours manually. That's the promise. But the quality depended entirely on Step 4, Verify."
:::

---

# AI Beyond Chat

![](./images/ai-landscape.png)

**AI is moving from "a tool you go to" to "a capability in every tool you use."**

- Microsoft 365 Copilot, in Word, Excel, PowerPoint, Outlook
- Google Workspace AI, in Docs, Sheets, Gmail
- Automation platforms, Zapier, Make, Power Automate
- Specialist tools, Grammarly, Otter.ai, Beautiful.ai

::: {.notes}
- "Chat interfaces like ChatGPT and Claude are the most visible AI tools"
- "But AI is increasingly embedded in the software you already use"
- "Within a few years, using AI won't feel like a separate activity, it'll just be how software works"
- "The question isn't whether you'll use AI, it's whether you'll use it well"
- "Framework 4 helps you figure out where to start."
:::

---

# Your Assistant Remembers You

**Assistants learn across sessions. Three separate stores:**

1. **What you told it**: explicit facts you asked it to save
2. **What it inferred**: patterns drawn from your chats (deleting chats ≠ deleting this)
3. **The chats themselves**: the history you can see

**Review periodically. Use private mode for what you don't want learned.**

::: {.notes}
- "One responsible-use point that surprises people: your assistant accumulates knowledge about YOU"
- "It's three separate stores, and they're managed separately. The facts you explicitly saved. The inferences it drew from your conversations, that's the one that makes your assistant feel 'too personal', and deleting your chats does NOT delete it. And the chat history itself."
- "Expect this question within a week of using AI regularly: 'it knows too much about me, how do I make it forget?' The answer is in personalisation or privacy settings, every platform names them differently, so look for 'memory', 'personalisation', or 'data controls'."
- "And going forward: private or temporary chat mode. It doesn't read from or write to memory. Use it for anything you'd rather the assistant not learn, the same logic as a fresh chat for independent analysis, but for privacy instead of objectivity."
- "At work, your IT team controls the enterprise settings, check what's approved before assuming anything about where your data goes."
- "Framework 4 helps you figure out where AI fits in your actual work."
:::

---

# Framework 4: AI Opportunity Finder

**Four types of AI opportunity in your daily work:**

| Type | The Signal | Example |
|------|-----------|---------|
| **Automate** | High-volume, repetitive, no judgment | Formatting reports, sorting emails |
| **Assist** | Research, synthesis, gathering | Summarising documents, comparing proposals |
| **Generate** | Writing, drafting, content creation | Client emails, meeting agendas, job postings |
| **Analyse** | Data, patterns, trends | Monthly performance, customer feedback |

::: {.notes}
- "Not every part of your job benefits from AI. The skill is knowing WHERE it adds value."
- "Start with Automate, those are your Quick Wins. Low effort, high time saved."
- "Assist and Generate are where most professionals will spend the most time with AI."
- "Analyse is what you practised in Exercise 3."
- "Some tasks are Human-Only: empathy, ethics, relationships, novel judgment. Keep those."
:::

---

# Start with Quick Wins

![](./images/priority-matrix.png)

```
                HIGH time saved
                     |
     Quick Wins      |     Big Wins
   (do these first)  |   (plan for these)
                     |
LOW effort ——————————+———————————— HIGH effort
                     |
   Low Priority      |     Worth It Later
                     |
                LOW time saved
```

::: {.notes}
- "Start in the top-left. Quick Wins build confidence and momentum."
- "Don't try to automate your entire job on day one"
- "Pick the task you do most frequently that bores you the most. That's your first candidate."
- "Now let's apply this to YOUR work..."
:::

---

# Where This Is Heading: Agents and Skills

You'll hear three words over the next year: **agent**, **harness**, **skill**.

An **agent** is a model in a loop with tools: it drafts, checks, calls something, tries again, until the job is done.

What shapes that loop is the **harness**: the software around the model. Its standing instructions, the context it can read, the tools it may call, and the model it runs on.

The part you own is the **skill**: a plain-text brief in a folder that the harness loads when your request matches it. Write it once and it works in any harness.

**And the trust tool still rules: an agent automates the loop, not the standard.**

::: {.notes}
- "You'll hear 'agents' constantly over the next year. Here's the durable version, no hype."
- "An agent is a model in a loop with tools. It plans, drafts, checks, calls something, tries again."
- "What makes it good or dangerous is the harness around the model: the standing instructions, what context it can read, which tools it may call, and whether there's a real check at the end. ChatGPT's chat box is a harness. So is a coding agent. So is the booking system at your work that drafts replies."
- "The part you own is the skill: a plain-text brief saved in a folder. When your request matches its description, the harness loads it. It's your RTCF briefing, written once, reused forever, and because it's just text it moves between tools."
- "And the trust tool doesn't retire. An agent automates the loop, not the standard. A loop that checks its own work inherits the blind spot we saw in Exercise 3: the model reaffirms its own answer. The standard still has to come from outside. Your test, your data, your reviewer, your rubric."
- "Everything you built today is exactly what goes into a skill file: the brief, the format, the rules, the verification step. If agents arrive in your workplace, you're not starting from zero."
- "If you want to see a minimal working version, I can demo it in three minutes: a local model, a one-page skill file, and RetailFlow support tickets triaged into a table, same prompt before and after the skill exists. The demo kit is in the instructor materials. No installs today; the idea is what matters."
:::

---

# Exercise 4: Your AI-Enhanced Workflow

![](./images/workflow-redesign.png)

**Your real work. Your real workflow. Redesigned with AI.**

1. **Map** your current workflow (10 min)
2. **Redesign** with AI at each applicable step (15 min)
3. **Test** one step live (10 min)
4. **Share** your before/after with your table (5 min)

::: {.notes}
- "Everything today has used our scenarios and our data. This exercise is about YOU."
- "Pick one task you do at least weekly that takes 30+ minutes"
- "Map every step: what you do, what tool you use, how long it takes"
- "Then classify each step using the Opportunity Finder: Automate, Assist, Generate, Analyse, or Human-Only"
- "Redesign the workflow. Then test one step for real."
- "Take 2 minutes to choose your task. If you're stuck, I have suggestions."
:::

---

# What You Built Today

![](./images/four-frameworks.png)

**One spine. Four frameworks. Four skills.**

**The Trust Tool** → Know HOW MUCH to trust any output, on any tool

1. **AI Task Suitability Spectrum** → Know WHEN to use AI
2. **RTCF Prompt Framework** → Know HOW to brief AI
3. **AI-Assisted Analysis Workflow** → Know how to use AI with DATA
4. **AI Opportunity Finder** → Know WHERE AI fits in your work

::: {.notes}
- "Step back and look at what you've built today"
- "The trust tool is the thread: encounter an output → average or precise? small or large? → that tells you how much checking it needs"
- "You now have four tools that work together:"
- "Encounter a task → check the Spectrum → if AI is involved, write a brief using RTCF → if there's data, follow the Analysis Workflow with verification built in → once a week, use the Opportunity Finder to spot new tasks to try"
- "The key principle across all of it: conversation, not delegation. The tool returns the form of the work; you supply the substance, the context, the judgement, the check. You own the output and the decisions."
:::

---

# Key Principles

- **Conversation, not delegation**: brief it like a capable colleague; you supply the substance
- **Your judgement is the edge**: everyone has the same tools; what you add is what differentiates
- **Verify from outside**: the tool can't check its own work; that check is yours
- **Start small, build confidence**: quick wins first
- **Iterate, don't accept**: first drafts are starting points

::: {.notes}
- "If you remember five things from today, remember these"
- "Conversation, not delegation: the prompt is a briefing, not an incantation. The tool gives you the form of the work; you supply what it can't: intent, context, standards."
- "Your judgement is the edge: 27 people in this room, same tools. What separates you is the discipline you bring to it."
- "Verify from outside: the model will happily reaffirm its own wrong answer. The check is yours, against the data and the source."
- "One more thing, and it's the big picture: for a century, work trained people for free. The grunt work was the tuition, and everyone starting out paid it. AI just ended that arrangement, the grunt work is the first thing it takes over. Practice is now something you choose, like exercise. The compare habit is the workout. The action plan you're about to write is the schedule."
- "Never send AI output without reviewing it. Your name is on it, not ChatGPT's."
- "Start with one task this week. Not five. One. Build from there."
:::

---

# Your Action Plan

![](./images/action-plan.png)

**Four moves, then repeat:**

**Decide** → what must human eyes still judge?
**Practise** → run the compare drill there
**Trade** → hand over what AI has proven reliable
**Revisit** → every few months; the line has moved

**This Week:**
What is the ONE AI tool or technique you'll try?

**This Month:**
What workflow will you redesign with AI?

**This Quarter:**
What AI skill will you develop further?

::: {.notes}
- "Take out your Personal Action Plan template"
- "The template has four moves at the top: decide, practise, trade, revisit. They map onto the three timeframes. This week is practise: one compare drill on a task that matters. This month is trade: redesign one workflow and hand over what AI has proven. This quarter is decide and revisit: name what must stay human, and check whether the line has moved."
- "This is the most important part of the day, making it concrete"
- "Don't write 'use AI more.' Write: 'I will use Claude to draft my weekly status update on Thursday using RTCF.'"
- "Specific task. Specific tool. Specific day."
- Give 10 minutes of quiet time. Don't talk over this.
- Ask 2-3 volunteers to share their "this week" commitment
:::

---

# Continue the Journey

**Next in the series:**

**AI-Driven Business Innovation**
*"Which AI project should we fund?"*
Strategic frameworks for AI investment decisions.

**AI Leadership & Project Management**
*"How do I deliver this AI project?"*
Leading successful AI implementations.

::: {.notes}
- "This course gave you personal AI skills"
- "The Business Innovation course teaches you to evaluate AI opportunities strategically, which projects are worth investing in"
- "The Leadership course teaches you to lead and deliver those projects, stakeholders, crises, scale-or-kill decisions"
- "Together, the three courses cover the full AI capability stack: use it, choose it, lead it."
:::

---

# Thank You

**Apply what you learned.**
**Start small. Verify always. Build from there.**

Dr. Michael Borck
michael.borck@curtin.edu.au

![](./images/qr-feedback.png)

::: {.notes}
- "Please take 5 minutes to complete the feedback form, the QR code is on screen and we'll hold here until you're done"
- "Your honest input helps us improve these workshops"
- "Digital copies of all materials will be sent via email"
- "Good luck with your AI experiments this week, and remember: brief it, don't spell it. Trust the average where averages are fine, and run the check where only exact will do."
:::
