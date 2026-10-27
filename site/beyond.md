---
pagetitle: Beyond the day
description: "What the course skipped: setting your assistant up once (custom instructions, projects, Gems), the jargon decoded (MCP, harness, context window), images, audio and video, and agents in the terminal."
nav-more: true
---

::: kicker
Beyond the day
:::

# The course was tool-agnostic. <em>This page isn't.</em>

::: lede
The four tools work on any AI, including the ones that ship next, which is why the day named no vendor. This page names them: where each product keeps the standing brief, what the jargon in vendor pitches means, what the tools make beyond text, and where agents fit. The details here change monthly. The four tools don't.
:::

## Set it once

All day you typed the brief fresh, every chat: role, task, context, format, and its check. Every major tool lets you save that as the standing brief it sends with every message. The generic name is a **system prompt**. The trade names differ.

| Tool (web) | The setting is called | Where it lives |
|---|---|---|
| ChatGPT | Custom instructions · Projects · Memory | Settings → Personalization; each Project has its own instructions |
| Claude | Instructions · Projects · Memory | Settings → Your Claude; each Project has its own instructions |
| Gemini | Instructions for Gemini · Gems | Settings & help → Personal Intelligence; Gems in the sidebar |
| Microsoft Copilot | Custom instructions · Memory | Settings → Personalization |
| Msty, LibreChat, Open WebUI | System prompt | Per chat or per model. You edit the prompt itself, so these show most plainly what a system prompt is |

[Menu names checked October 2026. They move; if one has changed, search the tool's help for "instructions".]{.small}

What goes in: your RTCF brief, your Done line, the check you attach. What doesn't: anything confidential you wouldn't paste into a chat. Review the saved brief each quarter, because the corners move and the brief should move with them. [Write like me](go-deeper.html#write-like-me) is a worked example. [Decide like me](decide-like-me.html) uses the same setting to save a set of decision rules.

::: note
**The names differ; the idea doesn't.** When a demo says the AI "understands you", look for this setting. It's a text box. You wrote a better one in Exercise 4.
:::

## The jargon, decoded

You'll hear these in every vendor pitch. None of them removes the check.

| Term | What it actually is | What it changes |
|---|---|---|
| MCP · Model Context Protocol | A standard plug that lets a harness call outside tools and data: your calendar, your files, the web. | Each connection widens what the harness can read and do. The stakes go up, so place the work on the trust tool again. |
| Context window | The model's working memory. | Long chats drift and early instructions fade. That's why the two-chat workflow and the handover prompt on [Go deeper](go-deeper.html) help. |
| RAG · "grounded on your documents" | The tool reads your files first, then answers. | Better grounding, new failure mode: check what it read, not just what it said. |
| Harness | The software around the model: standing instructions, what it can read, what tools it may call. | You already use several. Configuring one well is "set it once", above. |
| Agent | A model in a loop with tools: plans, acts, checks, retries. | Automates the loop, not the standard. The check still comes from outside. |

## Beyond text

The day worked in text because judgement shows clearest there. The same models make images, audio, music and video, and the trust tool moves straight over.

| Output | On the grid | The check |
|---|---|---|
| Image mock-up, internal discussion | Green corner | Nothing formal. It's a sketch |
| Image in a client-facing deliverable | Red corner | Licence and rights, consent for any real likeness, a disclosure line |
| Voice mode, drafting while you walk | Green | The names and figures it "heard". Re-check before sending |
| Music or video for a public asset | Amber to red | Copyright here is unsettled; follow your organisation's policy and disclose |

Two habits from the day transfer exactly: classify before you paste (a face is personal information), and tell people when AI made the thing they're looking at ([Responsible use](responsible-use.html)).

## The terminal, if you want it

Everything above is the web interface on purpose: it's where the judgement work happens, and where your account already is. The same ideas carry over to developer tools. Agent CLIs take a brief in your terminal and work in a loop, and your review still decides what ships. Local models (Msty with a local engine, or LibreChat pointed at one) run on your laptop, which is the answer when your writing samples can't leave it. None of this is required. It's the same four tools, faster.

::: note
**Whatever the product,** set the standing brief once, connect tools on purpose, and keep the check outside the tool. More in [Resources](resources.html).
:::
