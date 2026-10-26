# Facilitator Guide, Start Here

## The Human Edge: Using and Delivering AI with Judgement Masterclass

**Read this first.** This is your master guide to delivering the one-day workshop. It covers the teaching philosophy, full timeline, preparation checklists, common situations, and materials list. Individual exercise guides provide the detailed facilitation scripts.

---

## Quick Navigation

| When | What to Do |
|------|-----------|
| **1 week before** | Read this guide end-to-end. Read all 4 exercise guides and `run-of-show.md` (minute-by-minute, cut plan, dry-run checklist). Check technology. Reply to the Exec Ed logistics email. The course is fully digital now, so no printing and no stationery. Ask for power at each table and wifi that holds 30 people. Wording is in `reply-to-nicole-logistics.md`. |
| **72 hours before** | Coordinator reminder goes out with pre-reading + BYOD tech check (laptop, AI accounts created and tested). |
| **Day before** | Nothing to print. Test venue wifi against AI tool access and the companion site. Open `docs/deck.html` once on the presentation machine (caches fonts). Set up room: power board per table. |
| **Morning of** | Arrive 30 min early. Test projector. Open all AI tools in browser tabs. |
| **During course** | Follow the timeline below. Open each exercise guide 10 min before that session. |

---

## What You're Teaching

This is a **hands-on skills workshop**, not a strategic masterclass. It teaches professionals to use AI with judgement in their daily work. Two boundaries to hold out loud. Choosing which AI projects to fund is the companion course, AI in Strategy: Choosing Where to Invest. And delivering an AI project is project-scale material approved for the afternoon of future combined Human Edge runs. Today is desk scale, delivered in full. If the room pushes for project delivery content, name it as where this course goes next and keep moving.

**The idea that runs through the day:** everyone has the same AI tools, so generic competence is the baseline. The edge is judgement, knowing what to ask for, when to trust the answer, and where a human stays in charge. The **trust tool** (Average/Precise × Small/Large) is how that judgement is taught: one grid, introduced in Session 1, reused in every exercise. Two framing phrases to keep returning to: **"a convincing average"** (why verification matters) and **"conversation, not delegation"** (prompting is briefing a capable junior colleague, not casting a spell).

### The Four Exercises Build on Each Other

| Exercise | What Participants Learn | The "Aha!" Moment |
|----------|------------------------|-------------------|
| **1. The Compare Drill** | Your judgement vs the convincing average, side by side | "I can name where I beat it, and that is my value" |
| **2. Prompt Engineering** | The quality of your input determines the quality of your output | "I got dramatically better results just by being more specific" |
| **3. Data Analysis** | AI can accelerate analysis but needs human verification | "The AI found something real, but it also got things wrong" |
| **4. Workflow Mapping** | AI fits into specific parts of real work, not all of it | "I can actually see where this saves me time in my job" |

**The arc of the day:** Orientation → Skill-building → Application → Personalisation

By 4:30 PM, every participant should be able to articulate: *"Here's what I'll use AI for, here's how I'll brief it, and here's how I'll decide what to trust."*

---

## Facilitation Philosophy

### This Is a Workshop, Not a Lecture

Your lecture segments total about 2 hours across the day. The other 5+ hours are exercises, discussion, and hands-on practice. Resist the urge to extend lecture time.

### Core Principles

**1. Let them experience it first, then explain why.**
Don't teach RTCF as theory, have them write bad prompts first (Round 1), feel the pain, then introduce the framework (Round 2). The contrast teaches better than any slide.

**2. Mistakes are the curriculum.**
When someone's AI hallucinates or gives a terrible answer, that's not a failure, it's the best teaching moment of the day. Celebrate it. "This is exactly what we need to see."

**3. Meet them where they are.**
The room will have people who've used ChatGPT daily for a year alongside people who've never opened it. Your job is to make both groups feel challenged. Use stretch challenges for advanced participants and pair beginners with more experienced users.

**4. Make it about their real work.**
Every exercise connects to real tasks from their jobs. Exercise 4 is explicitly about their own workflow. Keep pulling the thread: "How would you use this at your desk on Monday?"

**5. You don't need to be an AI expert.**
You need to be a good facilitator who understands the frameworks. If an AI tool does something unexpected, use it: "Interesting, why do we think it did that?" You're modelling good AI practice by not pretending to have all the answers.

---

## Full Day Timeline

### Loop 1 · Judge (9:00-10:30)

| Time | Duration | Activity | Your Role |
|------|----------|----------|-----------|
| 9:00 | 15 min | **Welcome & Introductions** | Facilitate introductions, set expectations |
| 9:15 | 35 min | **Judge: tuition, your alarm, Trust Tool, Spectrum** (plus 5-min pair plot at 9:35) | Slides 3 to 6; see run-of-show.md |
| 9:50 | 40 min | **Exercise 1: The Compare Drill** | Circulate, observe, facilitate debrief |

**Key teaching points for the lecture:**
- AI predicts the next word, it's pattern-matching, not thinking
- The convincing average: output is fluent and usually about right, but "about right" and "exactly right" are different, and knowing which you need is the whole game
- **The trust tool (the spine):** Average/Precise × Small/Large → four corners (Lean in · Glance · Use, then verify · Human in the loop). Verification comes from outside the tool, the model can't check itself
- Optional 3-minute live game: project <https://trusttool.borck.education/> (executives pack), place 2-3 scenarios as a room and let the disagreements do the teaching. Theory page and embedded game on the course site under "Trust tool"
- Different tools, different strengths (no single "best" tool)
- The AI Task Suitability Spectrum: AI-Led → AI-Assisted → Human-Led → Human-Only (which tasks belong with AI; the trust tool then governs how much to trust the output)
- Hallucination is real and dangerous, AI never says "I don't know"

**Transition to Exercise 1:** "You have heard me talk about what AI can and cannot do. Now test it. First your own rough pass, in silence. Then the AI gets the identical task. The gaps between the two are the lesson."

→ Open `exercise-1-facilitator-guide.md`

### Morning Tea (10:30-11:00)

**During the break:**
- Check in with anyone who had tech issues during Exercise 1
- Note who seems advanced and who seems brand-new, adjust pairings for Exercise 2 if needed
- Reset projector for Session 2

### Loop 2 · Brief (11:00-12:30)

| Time | Duration | Activity | Your Role |
|------|----------|----------|-----------|
| 11:00 | 30 min | **Brief: conversation not delegation, RTCF, live demo, weaker-model ladder** | Slides 9 to 12 |
| 11:30 | 60 min | **Exercise 2: Prompt Engineering Workshop** | Circulate, compare outputs, facilitate debrief |

**Key teaching points for the lecture:**
- The reframe: conversation, not delegation, prompting is briefing a capable junior colleague, not reciting magic words
- RTCF: Role, Task, Context, Format, the briefing structure; Context is the grounding only the user can supply
- Show a live before/after demo: write a bad prompt, get bad output, rewrite with RTCF, get good output
- Common mistakes: too vague, no context, no format, not iterating
- Context windows: what they are, why they matter

**Live demo suggestion:** Pick Scenario 3 (project status update) from the worksheet. Show a naive prompt and the output, then rewrite it with RTCF live in front of the room. The contrast is immediate and convincing.

**Transition to Exercise 2:** "You just saw what a brief does. Pick 2 of the 3 workbook scenarios and feel the difference yourself."

→ Open `exercise-2-facilitator-guide.md`

### Lunch & Networking (12:30-1:15)

**During lunch:**
- Leave the projector showing the RTCF framework as a reminder
- Be available for questions but don't work through lunch yourself
- Mentally prepare for Session 3, the energy dip after lunch is real

### Session 3: AI-Powered Data Analysis (1:15-2:30)

| Time | Duration | Activity | Your Role |
|------|----------|----------|-----------|
| 1:15 | 25 min | **Verify: precision, VET, Analysis Workflow** | Slides 15 to 16 |
| 1:40 | 50 min | **Exercise 3: Data Analysis Challenge** | Circulate, check for errors, vote-then-reveal debrief |

**Key teaching points for the lecture:**
- Define the question BEFORE you touch the tool (Prepare step)
- Progressive questioning: start broad, go deeper
- Verification is non-negotiable, and it comes from outside the tool (the model can't reliably audit its own work). A number that drives a decision is a precision task: close is the same as wrong
- Privacy: what data should never go into free AI tools
- The 6-step workflow: Prepare → Upload → Question → Verify → Refine → Present
- Flag the Verification Challenge: three planted claims will test exactly this skill in the exercise

**Energy management:** This is the post-lunch slot. The data analysis exercise is interactive and hands-on, which helps. Keep your lecture tight (30 min max) and get them working with data quickly.

**Transition to Exercise 3:** "You now have a framework for prompting and a workflow for analysis. Let's put both together. You're about to receive 6 months of real customer service data from RetailFlow and three business questions that need answers."

→ Open `exercise-3-facilitator-guide.md`

### Afternoon Tea (2:30-3:00)

**During the break:**
- Note interesting findings from Exercise 3 to reference in Session 4
- Prepare for Exercise 4, this is the most personal exercise and some participants may need encouragement choosing a task

### Session 4: AI in Your Workflow (3:00-4:00)

| Time | Duration | Activity | Your Role |
|------|----------|----------|-----------|
| 3:00 | 20 min | **Redesign: beyond chat, Opportunity Finder, agents and skills** | Slides 19 to 21 (agents slide is the first cut if behind) |
| 3:20 | 40 min | **Exercise 4: Your AI-Enhanced Workflow** | Circulate, help with task selection, facilitate sharing |

**Key teaching points for the lecture:**
- AI is moving from "a tool you go to" to "a capability in every tool"
- Four opportunity types: Automate, Assist, Generate, Analyse
- Start with Quick Wins: low effort, high time saved
- Agents, harnesses, skills (acknowledge, don't build): an agent is a model in a loop with tools; the harness supplies instructions, context, tools and checks; a skill is a plain-text brief the harness loads when a request matches it. The trust tool still applies: the loop is automated, the standard is not. Today's RTCF briefs and verification habits are exactly what goes in a skill file
- Responsible use: company policies, human oversight, data governance
- What your assistant remembers about you: three stores (saved facts, inferences from chats, chat history), deleting a chat isn't deleting what was learned; review settings periodically; private/temporary mode for what you don't want learned
- Brief overview of platforms: Copilot, Zapier, Make, Power Automate (awareness, not training)

**Transition to Exercise 4:** "Everything today has used our scenarios and our data. This last exercise is about YOUR work. Pick one real task from your week and redesign it with what you've learned today."

→ Open `exercise-4-facilitator-guide.md`

### Wrap-up & Action Planning (4:00-4:30)

| Time | Duration | Activity | Your Role |
|------|----------|----------|-----------|
| 4:00 | 10 min | **Close: broken ladder + four moves** | Slides 23 to 24 |
| 4:10 | 12 min | **Personal Action Planning** | Workbook final section, ten quiet minutes |
| 4:22 | 8 min | **Close: export + feedback QR** | Hold the closing slide until phones go down |

**Framework synthesis, your script:**

> "Let's step back and look at what you've built today. One thread ran through everything: the **trust tool**. Average or precise? Small stakes or large? That grid told you how much to trust every output today, and it'll work on whatever tool exists next year.
>
> And you now have four frameworks hanging on that spine:
>
> 1. The **Suitability Spectrum** tells you WHEN to use AI, not every task needs it, and some tasks should stay human-only.
>
> 2. **RTCF** tells you HOW to brief AI, conversation, not delegation. You experienced the difference between a vague request and a proper brief.
>
> 3. The **Analysis Workflow** tells you how to use AI WITH DATA, and why verification comes from outside the tool. Some of you caught planted claims today that sounded perfect and weren't. That's the skill.
>
> 4. The **Opportunity Finder** tells you WHERE ELSE in your work AI can help, and you've already mapped one real workflow.
>
> The key principle across all of it: **everyone in this room has the same tools. Your judgement, the briefing, the trust call, the check, is the edge. You own the output and the decisions.**"

**Action planning:**
- Distribute the Personal Action Plan template
- Frame it with the four moves before quiet time:

> "The template starts with four moves: decide, practise, trade, revisit. This week is practise: one compare drill on a task that matters, your rough pass, then AI's, side by side. This month is trade: redesign one workflow and hand over only what AI has proven on your work. This quarter is decide and revisit: name what must stay human, then check in a few months whether the line has moved. It usually has."
>
> *(Idea source for the four moves and the compare habit: "AI Just Broke the Way People Become Experts", d-squared70.github.io. The course site links it in the go-deeper section.)*

- Give them 10 minutes of quiet time to fill it in, don't talk over this
- Ask 2-3 volunteers to share their "this week" commitment
- End with workbook export, the feedback QR hold, and the two-scales pointer (project scale in future combined runs, AI in Strategy for funding choices)

**Closing script:**

> "You're not going to be an AI expert tomorrow. But you have something better, a framework for getting started and a realistic sense of what these tools can and can't do. Start small. Pick one thing. Try it this week. Build from there."

---

## Common Situations & How to Handle Them

### "I've already been using ChatGPT for months, this is too basic"

**Your move:** Acknowledge their experience and make them a resource.

> "That's great, you'll get through the basics quickly. I'd love you to help others at your table who are newer to this. And in each exercise, there are stretch challenges designed for exactly your level."

In Exercise 2, ask them to try the advanced techniques. In Exercise 3, ask them to find patterns beyond the three questions. In Exercise 4, ask them to tackle a more complex workflow.

### "I've never used any AI tool before, I'm lost"

**Your move:** Normalise it and pair them.

> "That's exactly who this workshop is for. Let's make sure you're set up, and I'll pair you with someone at your table who can help with the mechanics while you focus on learning."

Check their account access during Exercise 1. If they're stuck on setup, troubleshoot quickly, don't let tech issues eat into their learning time.

### "AI just gave me completely wrong information"

**Your move:** Celebrate it.

> "Perfect, this is exactly what we need to see. Can you show the group? This is hallucination in action. The AI sounds confident but it's wrong. This is why verification matters."

Use it as a live teaching moment. Ask the group: "How would you know this was wrong if you didn't already know the answer?"

### "Isn't AI going to take our jobs?"

**Your move:** Address it honestly without dismissing the concern.

> "It's a fair question. Here's what we're seeing: AI is changing jobs, not eliminating most of them. The tasks that are routine and pattern-based, yes, AI will handle more of those. But the judgment, creativity, relationships, and ethical decisions? Those stay human. Today is about making sure you're the professional who knows how to work WITH AI, not the one who gets surprised by it."

### "My company doesn't allow us to use ChatGPT"

**Your move:** Validate the policy and redirect.

> "That's actually responsible of your organisation. Data privacy is serious, and we'll talk about that today. For now, you can use the tools here for the workshop exercises, we're using practice scenarios, not real company data. Take notes on the techniques, and when you're back at work, check with your IT team about which tools are approved."

### "My AI knows too much about me, it's getting too personal"

**Your move:** Normalise it, this is the most common privacy question in the weeks after the workshop. Explain the three stores, then give them the platform-specific path.

> "Your assistant keeps knowledge about you in three separate places, and they're managed separately: the facts you explicitly saved, the inferences it drew from your chats, and the chats themselves. Deleting a chat doesn't delete what it learned. Look in settings for 'memory', 'personalisation', or 'data controls', review and delete there. And going forward, private or temporary chat mode doesn't read from or write to memory, use it for anything you'd rather it not learn."

**If they use Copilot with a Curtin account** (most staff do), the specific path:

> "Copilot Chat (copilot.cloud.microsoft) → top-right '...' → Settings → Personalization. Three things: (1) **Saved memories** tile → Manage saved memories → delete them, note the toggle only stops Copilot *using* them, deleting is a separate action. (2) **Chat history** tile → toggle Off, this deletes the inferences, but takes 30 days to clear, and re-enabling inside 30 days cancels the deletion. (3) The **chats themselves** → delete per conversation, or in bulk at myaccount.microsoft.com → Settings & Privacy → Privacy → Copilot interaction history. And the **Temporary chat** button top-right skips memory entirely."

*(Platform UI changes frequently, verify the path before quoting it. The three-stores concept is the durable part.)*

### "The wifi is down / AI tool isn't loading"

**Your move:** Pair up.

> "Share with your neighbour for now, one person drives, the other navigates. Some of the best learning happens when two people discuss what to prompt."

If venue wifi is unreliable, have a mobile hotspot as backup. See Troubleshooting Tech section below.

### The room is split, some are way ahead, others are struggling

**Your move:** Use table-level differentiation.

Seat experienced users with beginners (if you can control seating). Give advanced participants explicit stretch challenges. Check in with struggling participants individually during exercises, don't call them out publicly.

---

## Troubleshooting Tech

| Problem | Solution |
|---------|----------|
| Participant can't log into AI tool | Have them try a different tool (Claude, Gemini, ChatGPT, any one will work) |
| Corporate firewall blocks AI tools | Try mobile data on their phone as a workaround; pair with neighbour if needed |
| Wifi is slow | Reduce the number of tools in Exercise 1 from 3 to 2; stagger uploads in Exercise 3 |
| AI tool is down (outage) | Switch everyone to a working tool; have backup screenshots of example outputs |
| CSV won't upload | Copy/paste the first 50 rows instead; it's enough to find the patterns |
| Projector fails | Use your laptop screen and walk the room; adjust to more hands-on, less presentation |

**Pre-test everything the day before.** Open ChatGPT, Claude, and Gemini from the venue network. Upload a test CSV. If anything is blocked, you need to know before participants arrive.

---

## Materials Checklist

### Digital pack (nothing is printed)

- Open the companion site on the projector at the start. The title slide carries the address. It holds the deck, the workbook with every worksheet and the action plan, the frameworks reference, and the dataset download.
- The workbook saves in each person's browser as they type and exports to a markdown file or a PDF. Test the export yourself the day before. It is the one failure you cannot fix live.
- The room needs a power board at each table, wifi tested with about 30 AI sessions running, and two spare laptops if you can get them. Skip the butchers paper and post-its. Work leaves on participants' laptops, not on a wall. Scrap paper is fine for thinking. Nobody collects it.

### Digital (distribute or make accessible)

| Material | File | When |
|----------|------|------|
| RetailFlow CSV dataset | `activities/retailflow-customer-service-data.csv` | Exercise 3 (1:45 PM) |
| Pre-reading | `pre-readings/ai-for-the-rest-of-us.md` | 48 hours before course |

### Facilitator Only

| Material | File | When to Open |
|----------|------|-------------|
| This guide | `FACILITATOR-START-HERE.md` | Before the course |
| Exercise 1 guide | `exercise-1-facilitator-guide.md` | 9:40 AM |
| Exercise 2 guide | `exercise-2-facilitator-guide.md` | 11:20 AM |
| Exercise 3 guide | `exercise-3-facilitator-guide.md` | 1:35 PM |
| Exercise 4 guide | `exercise-4-facilitator-guide.md` | 3:10 PM |
| Answer keys | `answer-keys.md` | Reference throughout, incl. Verification Challenge verdicts |
| Exec Ed logistics reply | `reply-to-nicole-logistics.md` | 1 week before (digital logistics: power, wifi, 72h reminder wording) |
| Ticket triage demo kit | `retailflow-triage-demo/` | Session 4, optional 3-min demo (skill file, script, sample tickets) |

### Room Setup

- Tables for 4-6 people (collaborative work)
- Power outlets accessible from all tables (full-day laptop use)
- Projector and screen visible from all seats
- Whiteboard or flipchart (optional, useful for Exercise 1 debrief)
- Spare power strips / extension cords

---

## Success Looks Like

By end of day, you should observe:

- [ ] Participants writing structured briefs without being reminded (RTCF is internalised)
- [ ] The trust tool language shows up in their conversations ("this is average, low stakes, lean in")
- [ ] At least one "the AI got it wrong!" moment that the group learned from
- [ ] Most tables caught Claim B (the convincing fake) in the Verification Challenge
- [ ] Participants talking about their real work, not just the exercises
- [ ] Multiple people saying some version of "I'm going to try this on Monday"
- [ ] The action plans have specific, concrete commitments, not vague intentions
- [ ] The room energy stays engaged through the afternoon (Exercise 3 and 4 keep energy up)
- [ ] Feedback QR completed by most participants in the final 5 minutes

---

## How this course sits beside AI in Strategy

| | This course (desk scale) | AI in Strategy |
|---|---|---|
| **Facilitator style** | Coach / workshop leader | Strategic facilitator |
| **Main activity type** | Hands-on practice with AI tools | Group frameworks + investment judgement |
| **Level of ambiguity** | Low, clear tasks, clear outputs | Medium, strategic judgment needed |
| **Participant emotion** | Curiosity, some anxiety | Confidence, strategic thinking |
| **Your biggest risk** | Tech issues, wide skill gap | Groups defaulting to safe choices |

Project-delivery teaching (pilot scoping, human checkpoints, scale/pivot/kill) is not a third course any more. Executive Education merged Practice and Delivery into this title for future runs. Until that afternoon is built, it is a closing-slide pointer in this run and nothing more.

**Your biggest facilitation challenge:** Managing the skill gap. Some participants will fly through exercises while others are still setting up accounts. Plan for this. Have stretch challenges ready. Use experienced participants as peer mentors.

---

**You're ready. Read the exercise guides, test the tech and the workbook export, and trust the design. The exercises do the teaching, you guide the conversation.**
