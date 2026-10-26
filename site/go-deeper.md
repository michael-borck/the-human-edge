---
pagetitle: Go deeper
description: "Self-paced extensions: VET in depth, the three cognitive traps, the two-chat workflow, the handover prompt, and making your voice persistent."
nav-more: true
---

::: kicker
Go deeper
:::

# Five minutes each. <em>All on your own work.</em>

::: lede
For fast finishers on the day, or the week after. Each one keeps your judgement in charge from a different angle. Most are drawn from the free companion book, [*Conversation, Not Delegation*](https://michael-borck.github.io/conversation-not-delegation/).
:::

## VET, in depth

The trust tool tells you *how much* to check. VET tells you *how*, for claims you can't check against your own data. The most dangerous output isn't the obvious mistake; it's the one that sounds completely right.

| The AI says... | Verify | Explain | Test |
|---|---|---|---|
| "Studies show..." | Find the actual studies. | Can I explain the mechanism? | Does it hold in a different context? |
| "The best figure is X." | Where does that number come from? | Why X, specifically? | What happens if I change one variable? |
| "This method is 95% effective." | Source? | What does 95% mean here? | Under what conditions? |

- **Verify:** can I find this independently? AI produces plausible references that don't exist, because a fake citation is generated the same way as any other text. [CiteSight](https://citesight.eduserver.au) checks references for you.
- **Explain:** can I say it in my own words? Where you struggle to rephrase is where your understanding has a gap.
- **Test:** does it survive a "what if"? Change a variable, try an edge case. Fragile answers break; robust ones flex.

Use it hardest when a decision hangs on the claim, or when people will assume you checked. [Full chapter: VET your AI](https://michael-borck.github.io/conversation-not-delegation/chapters/vet-your-ai.html).

## The three cognitive traps

Not technical problems: human ones. Knowing their names is the first defence.

- **Gell-Mann amnesia.** You catch AI's errors in your own field, then trust it on the law, the market or the numbers, exactly where you're least able to check. Be more sceptical where you know less. (Michael Crichton named it in 2002, after the physicist Murray Gell-Mann.)
- **The AI dismissal fallacy.** "That's just ChatGPT" is a refusal to engage, not a critique. Judge the reasoning, not where it came from.
- **Sycophancy.** Models are tuned on human approval, and people prefer agreeable answers. Don't ask "what do you think?"; ask "what are the three weakest points in this?" See the push-back moves in the [starter prompts](prompts.html).

## The two-chat workflow

Separate thinking from building.

1. **Thinking chat.** Explore, challenge your assumptions, follow tangents, find out what your actual question is. Messy by design, and disposable.
2. **In between: you curate.** Read what came out, keep what matters, drop what doesn't, and write a short, focused brief. Don't copy and paste. That curation is where your judgement lives.
3. **Building chat.** A fresh chat that produces the output from your brief. Better input, better output.

Neither chat has the whole picture. Only you hold both, which is what "human in the loop" really means.

## The handover prompt

Long chats drift and lose the thread. Before you close one, ask for a handover, then start fresh and paste it in. You keep the thinking and lose the noise.

```text
Write a handover prompt that captures everything important from this conversation: the context, the decisions made, open questions, and where we left off. I'll paste it into a new chat to continue.
```

Useful for anything that runs over several sessions: a proposal, a policy, a board paper.

## Make your voice persistent

Generic output sounds like everyone. The voice pass in Exercise 4 fixes one draft; this fixes every future one.

1. Collect three or four things you've written that sound like you at your best: emails, reports, a proposal. Remove anything confidential.
2. Ask a model to describe your style as a two-page brief: sentence length, structure, vocabulary, how you open and close, what you never do. [Style Mirror](https://stylemirror.eduserver.au) does this step for you.
3. Read the brief critically. It will be slightly off, and slightly a parody. Edit it until it's right; that editing is your judgement.
4. Paste it into your tool's custom instructions or a saved project. Every draft now starts closer to your voice.

If your samples are sensitive, do step 2 with a local model so nothing leaves your laptop.

::: note
**One thread through all of these:** each one stops you accepting fluent, generic output. Verify it, separate thinking from building, argue against it, make it sound like you. More in [Resources](resources.html).
:::
