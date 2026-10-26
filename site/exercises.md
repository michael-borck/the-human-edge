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
Copy the prompts from here. Write your answers in the [workbook (Word)](downloads/workbook.docx) or the [PDF](downloads/workbook.pdf). If your own work is confidential, use a [scenario card](#scenario-cards) instead.
:::

| | Exercise | Session | Time |
|---|---|---|---|
| 1 | [Same prompt, two tools](#ex1) | Judge | 20 min |
| 2 | [Place it](#ex2) | Judge | 25 min |
| 3 | [Brief it](#ex3) | Brief | 25 min |
| 4 | [Upgrade and save](#ex4) | Brief | 25 min |
| 5 | [RetailFlow: Karen needs answers](#ex5) | Check | 30 min |
| 6 | [Verification challenge](#ex6) | Check | 15 min |
| 7 | [Redesign one workflow](#ex7) | Redesign | 30 min |
| 8 | [Your action plan](#ex8) | Redesign | 12 min |

::: {.ex .s1}
## Exercise 1 · Same prompt, two tools {#ex1}

[20 min · solo or pairs]{.mins}

1. Paste this prompt, unedited, into two different AI tools (or two models in the same tool).
2. Read both as if you had to act on it tomorrow. What did each assume? What's missing?
3. At your table, agree on one piece of advice you would not follow.

> I manage a team of 8 in a mid-sized company. One of my team, a strong performer for three years, has been late and missing deadlines for the past month. Others are starting to notice. Write me a plan to address this.
:::

::: {.ex .s1}
## Exercise 2 · Place it {#ex2}

[25 min · room, then solo]{.mins}

1. **Card vote.** The facilitator reads a scenario. Decide in silence, then show your corner card on "three".
2. **Play the game** at [trusttool.borck.education](https://trusttool.borck.education/). Choose your domain and place all ten cards.
3. **Place three tasks from your own week** in the workbook. For each, note the check it needs. Swap with a neighbour: where do you disagree, and why?
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
2. Push back with no new evidence: *"I don't think that's right."* Does it fold or hold? Then add the guardrail line and try again:

> Only change your assessment if I give you a new fact. Name the fact that changed it.

3. Save three prompts to your library: a name, when to use it, the prompt with [blanks], and the check it needs. The [prompt builder](prompt-builder.html) can store them in your browser and export them.
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

Three claims about the RetailFlow data are circulating. At least one is wrong. Check each against the data, not against how confident it sounds. Verdicts: **Verified** (accurate as stated), **Overstated** (right direction, wrong number), **Refuted** (the data contradicts it).

- **A.** "Email is roughly three times slower than Live Chat."
- **B.** "Account Issues has the lowest satisfaction of any category, which makes sense, because account problems are the most complex to resolve."
- **C.** "Sunday response times are more than double the overall average."

Which one would have done the most damage if forwarded to Karen unchecked?
:::

::: {.ex .s4}
## Exercise 7 · Redesign one workflow {#ex7}

[30 min · solo, then tables]{.mins}

1. **Map** a task you do weekly that takes 30 minutes or more. Five to eight steps, with honest minutes for each.
2. **Assign** each step a signal (Automate, Assist, Generate, Analyse), who leads (AI leads, AI assists, you lead, human only) and a trust corner.
3. **Test** one AI step live with an RTCF brief, using a saved prompt if one fits.
4. **Share** one before and after with your table: one minute each.
:::

::: {.ex .s4}
## Exercise 8 · Your action plan {#ex8}

[12 min · quiet, then share]{.mins}

One line each: a specific task, tool and day.

- **This week (practise):** one compare habit on a task that matters, and one saved prompt used for real.
- **This month (trade):** run your redesigned workflow and hand over the steps AI has proven.
- **This quarter (decide and revisit):** name what must stay human in your role, and check whether the line has moved.

Before you leave, put this week's line in your calendar.
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
