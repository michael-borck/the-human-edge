---
pagetitle: Exercises
description: "The eight exercises, with copyable prompts, scenario cards and the RetailFlow data."
nav-exercises: true
---

::: kicker
Exercises
:::

# Eight exercises. <em>Mostly your own work.</em>

::: lede
Copy the prompts from here and write your answers in the [digital workbook](workbook.html); it saves in your browser and exports before you leave. If your own work is confidential, use a [scenario card](#scenario-cards) instead.
:::

| | Exercise | Session | Time |
|---|---|---|---|
| 1 | [Your pass first](#ex1) | Judge | 25 min |
| 2 | [Place it](#ex2) | Judge | 25 min |
| 3 | [Brief it](#ex3) | Brief | 25 min |
| 4 | [Upgrade and save](#ex4) | Brief | 25 min |
| 5 | [RetailFlow: Karen needs answers](#ex5) | Check | 30 min |
| 6 | [Verification challenge](#ex6) | Check | 15 min |
| 7 | [Plan one delivery](#ex7) | Deliver | 35 min |
| 8 | [Your action plan](#ex8) | Deliver | 12 min |

::: {.ex .s1}
## Exercise 1 · Your pass first {#ex1}

[25 min · solo, then tables]{.mins}

1. **Your pass first.** Five minutes, no AI: sketch your own plan for the task below, in the workbook.
2. **Then AI's.** Paste the task, unedited, into an AI tool (two tools if you have them).
3. **Compare side by side.** Where did you beat it? Where did it beat you? What did it get confidently wrong?

> I manage a team of 8 in a mid-sized company. One of my team, a strong performer for three years, has been late and missing deadlines for the past month. Others are starting to notice. Write me a plan to address this.
:::

::: {.ex .s1}
## Exercise 2 · Place it {#ex2}

[25 min · room, then solo]{.mins}

1. **Card vote.** The facilitator reads a scenario. Decide in silence, then show your corner card on "three".
2. **Play the game** at [trusttool.borck.education](https://trusttool.borck.education/). Choose your domain and place all ten cards.
3. **Place three tasks from your own week** in the [workbook](workbook.html). For each, note the check it needs. Swap with a neighbour: where do you disagree, and why?
:::

::: {.ex .s2}
## Exercise 3 · Brief it {#ex3}

[25 min · solo]{.mins}

1. Pick a real task from your week, or a scenario card below.
2. **Round 1:** write the prompt the way you normally would. Run it. Score the output from 1 (unusable) to 5 (ready to use).
3. **Round 2:** rewrite it with RTCF and run it in a fresh chat. Score it again.
4. Note which part moved the score most.

> ROLE: You are a ...
> TASK: Write / summarise / compare ... (how much?)
> CONTEXT: The audience is ... The situation is ... Good looks like ...
> FORMAT: Length ... Structure ... Tone ...

The [prompt builder](prompt-builder.html) assembles the four parts for you.
:::

::: {.ex .s2}
## Exercise 4 · Upgrade and save {#ex4}

[25 min · solo]{.mins}

1. Take your best Round 2 prompt. Add one upgrade and run it: an example, a definition of done, questions first, or steps.
2. Push back with no new evidence: *"I don't think that's right."* Does it fold or hold? Then try one of the three push-back moves:

> GUARDRAIL: Only change your assessment if I give you a new fact. Name the fact that changed it.
> DEVIL'S ADVOCATE: Don't flatter me. Give me three reasons this fails, and name the assumption it all rests on.
> BOARD: Respond as a board: a CFO, a sceptical customer and a frontline manager. One paragraph each, then where they disagree.

3. Save three prompts to your library: a name, when to use it, the prompt with [blanks], and the check it needs. Use the [workbook](workbook.html) or the [prompt builder](prompt-builder.html).
4. **Stretch: the voice pass.** Paste about 100 words you actually wrote (sanitised), then ask: *"Rewrite your last output in my voice, leading with the one thing only I would say."* What changed? Optionally, ask it to summarise your style as a short brief and paste that into your tool's custom instructions.
:::

::: {.ex .s3}
## Exercise 5 · RetailFlow: Karen needs answers by Monday {#ex5}

[30 min · solo or pairs]{.mins}

Karen manages customer service at RetailFlow, an online retailer. She has six months of ticket data and three questions:

1. What are the top three drivers of customer dissatisfaction?
2. When do our response times blow out?
3. What should I do about it?

::: btns
[Download the data (CSV)](downloads/retailflow-customer-service-data.csv)
:::

260 tickets, July to December 2024. Columns: `ticket_id`, `date`, `day_of_week`, `month`, `category`, `channel`, `priority`, `agent`, `response_time_hours`, `resolution_time_hours`, `satisfaction_score` (1 to 5), `resolved`.

1. **Frame.** Write Karen's questions down. Start a fresh chat.
2. **Explore.** Upload the CSV (or paste it) and start with:

> Describe this dataset: number of rows, columns, date range, and anything that looks incomplete. Don't analyse it yet.

3. **Verify two numbers yourself** with a spreadsheet filter, recount or pivot table. Not "are you sure?"
4. **Shape** a brief for Karen, under 300 words, ending with a line that starts *What I checked:*
:::

::: {.ex .s3}
## Exercise 6 · Verification challenge {#ex6}

[15 min · pairs, then card vote]{.mins}

Three claims about the RetailFlow data are circulating. At least one is wrong. Check each against the data, not against how confident it sounds. Verdicts: **Verified** (accurate as stated), **Overstated** (right direction, wrong number), **Refuted** (the data contradicts it), or **Can't tell yet** if you haven't been able to check it.

- **A.** "Email is roughly three times slower than Live Chat."
- **B.** "Account Issues has the lowest satisfaction of any category, which makes sense, because account problems are the most complex to resolve."
- **C.** "Sunday response times are more than double the overall average."

Which one would have done the most damage if forwarded to Karen unchecked?
:::

::: {.ex .s4}
## Exercise 7 · Plan one delivery {#ex7}

[35 min · solo, then tables]{.mins}

1. **Map** a task you do weekly that takes 30 minutes or more. Five to eight steps, with honest minutes for each. Note the owner, a success measure and today's baseline.
2. **Assign** each step: who leads (AI leads, AI assists, you lead, human only) and its trust corner.
3. **Design the checkpoints.** Who checks each amber or red step, and how? Who is affected, who has to agree, and who will do the checking?
4. **Test** one AI step live with an RTCF brief. Then **set your 30-day gate**: what result would make you scale, pivot or kill?

The [Map my workflow](prompts.html#map-my-workflow) and [Pre-mortem](prompts.html#pre-mortem) starter prompts help with steps 1 and 3.
:::

::: {.ex .s4}
## Exercise 8 · Your action plan {#ex8}

[12 min · quiet, then share]{.mins}

One line each: a specific task, tool and day.

- **This week (practise):** two-pass one task that matters, and use one saved prompt for real.
- **This month (deliver):** run your delivery plan, with checkpoints in place from day one.
- **Day 30 (gate):** scale, pivot or kill, against the criteria you set today.
- **This quarter (revisit):** name what must stay human in your role, and check whether the corners have moved.

Before you leave, put this week's line and your day-30 gate in your calendar.
:::

## Scenario cards {#scenario-cards}

Use one of these in Exercises 3 and 4 if your own work is confidential. Paste the details into your Context.

:::::: {.cards .two}
::: card
[Scenario 1]{.lab}

### The difficult client email

Your client, David Chen (VP Operations, GreenLeaf Industries), says your latest deliverable is "too generic". The work is solid, but his board changed priorities at a meeting you weren't in. It's an 18-month, mostly positive relationship. You want to acknowledge his frustration without conceding the work is poor, and propose a one-hour alignment meeting.
:::

::: card
[Scenario 2]{.lab}

### The policy summary

A new 22-page flexible work policy needs to become an email your 12-person marketing team will actually read: how many days from home, how to request changes, busy periods, and part-time rules. Friendly, practical, under 400 words. (Paste any policy you have, or ask the AI to invent a plausible one first.)
:::

::: card
[Scenario 3]{.lab}

### The Friday status update

CRM migration for a steering committee (CIO, sponsor, two business leads). Notes: data batch 2 done but 3 days late (2,300 duplicate records, Sarah leading review); vendor hasn't confirmed training dates; UAT going well, 2 minor bugs; $12K under budget; 68% complete against a 72% target. They want RAG status, wins, risks, next steps. No surprises.
:::

::: card
[Scenario 4]{.lab}

### The interview questions

Hiring a mid-level Digital Marketing Coordinator for a 5-person B2B team: social campaigns, Google Analytics and Meta Ads, agency coordination, monthly reports to leadership. 45-minute panel with the Marketing Director. HR's generic questions won't tell you whether they can do the job. You want behavioural and situational questions.
:::

::: card
[Scenario 5]{.lab}

### The logistics decision

Renew, switch or insource your third-party logistics? Current provider: $1.8M a year, 96.2% on time (benchmark 97%), 2.1% damage (benchmark 1.5%), slow on volume spikes, just raised prices 8%. Competitor: $1.65M, promises 97.5%. In-house: $2.5M upfront, $1.2M a year, 12 months to set up. 15,000 orders a month, growing 20% a year. A discussion starter for leadership, not the decision.
:::

::: card
[Scenario 6]{.lab}

### The process document

You're the only person who knows monthly invoicing: export billable hours from Harvest, group by client in Excel, apply the rate card ($250 strategy, $180 execution, $120 support), create invoices in Xero, add PO numbers from the account managers' Google Sheet, send, update the tracker, then email Finance a summary with anything unusual. Write it so a colleague can do it while you're on leave.
:::
::::::
