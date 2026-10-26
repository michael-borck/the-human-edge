# AI for the rest of us

Pre-reading for **The Human Edge: Using and Delivering AI with Judgement**

## Summary

AI tools like ChatGPT, Claude, and Gemini are now freely available to anyone with a browser. They can draft emails, summarise documents, analyse data, write code, and brainstorm ideas, but they also hallucinate facts, miss nuance, and confidently deliver nonsense. This pre-reading gives you the conceptual foundation you need before the workshop: how these tools actually work (pattern-matching, not thinking), what they're reliably good at, where they fall apart, and how to stay safe with company data. The goal isn't to make you an expert, it's to get you comfortable enough that the workshop can focus on building real skills, not explaining basics.

**Reading time:** about 25 minutes
**Key takeaway:** AI assistants are useful pattern-based tools, not accountable colleagues. The better you understand how an answer was produced, the better you can judge how far to trust it.

---

## Who This Is For

This reading is for professionals who want to use AI well in daily work. It stays at desk scale: your own tasks, documents, data, and decisions. Choosing which AI projects to fund belongs to the companion strategy course; applying the same judgement across a delivered project is the direction of future combined Human Edge runs.

You might be:
- A marketing coordinator who's heard ChatGPT can draft copy
- A finance analyst wondering if AI can help with spreadsheets
- An HR manager curious about using AI for policy documents
- An operations lead who wants to automate repetitive reporting
- A professional in any field who feels like everyone else "gets" AI and you're behind

**You're not behind.** Most people are still figuring this out. That's what the workshop is for.

---

## Part 1: What Are AI Tools, Actually?

### The Tools You'll Encounter

When people say "AI" today, they often mean a conversational assistant such as one of these. The examples matter less than the pattern, because products and names change quickly:

| Tool | Made By | What It Is |
|------|---------|------------|
| ChatGPT | OpenAI | Conversational AI, chat, write, analyse, code |
| Claude | Anthropic | Conversational AI, similar to ChatGPT, different strengths |
| Gemini | Google | Conversational AI, integrated with Google Workspace |
| Microsoft Copilot | Microsoft | AI embedded in Word, Excel, PowerPoint, Outlook |
| Notion AI | Notion | AI built into the Notion workspace |
| Grammarly | Grammarly | AI writing assistant |

Conversational assistants are generally built around a **large language model (LLM)**, often wrapped with file handling, web search, memory, code execution, and other tools. AI built into office or specialist software may use an LLM, another machine-learning model, deterministic rules, or a mixture. Do not assume every feature labelled AI works the same way.

### How They Actually Work

Here's the most important thing to understand about AI tools:

**An LLM generates plausible next tokens.**

A token is a chunk of text. Given your prompt and any supplied material, the model calculates likely continuations from patterns learned in training. Modern assistants may then reason over several steps, search, inspect files, run code, or call tools before answering. That machinery can make output much more useful. It does not make the system an accountable colleague who knows your situation or owns the result.

Autocomplete is a useful starting analogy, with limits:
- Your phone's autocomplete predicts one word at a time
- An LLM generates a whole response token by token, conditioned on the prompt, conversation, files, and tool results it can access
- Fluent output can look like understanding, so judge the evidence and reasoning you can inspect, not the polish

**Why this matters to you:**
- GenAI is often strong where form and patterns carry the work (writing styles, document formats, transformations)
- It needs outside checks for current facts, hidden calculations, unfamiliar context, and consequential judgement
- Your job is to know the difference

### The wider AI map

Generative AI is the slice you can talk to. It is not the whole pie.

- **Artificial intelligence (AI)** is the broad field: systems that perceive, predict, recommend, classify, decide, or generate. Spam filters, search ranking, fraud alerts, forecasts, recommendations, transcription, and image recognition are familiar examples.
- **Machine learning (ML)** learns patterns from examples rather than relying only on hand-written rules.
- **Neural networks and deep learning** use layered models to learn representations from data.
- **Generative AI (GenAI)** creates new text, images, audio, video, or code.
- **Large language models (LLMs)** are GenAI models centred on language and code. Today's assistants usually wrap an LLM in a wider product.
- **Natural language processing (NLP)** is the field of language tasks, including classification, translation, extraction, and summarisation. It cuts across the layers rather than sitting neatly inside one.

This course works mainly with GenAI assistants because natural language became the interface. You can direct and review work from a browser without code or a data-science team. The judgement travels to other AI — stakes, evidence, bias, verification, human accountability — but prompts are the local dialect. A predictive model is governed through its data, false-positive and false-negative costs, monitoring, and drift, not by asking it more nicely.

### The "confident nonsense" problem

AI tools have a distinctive failure mode: **they do not reliably know when they do not know.**

A colleague may say "I'm not sure, let me check." An assistant can also hedge or decline, but it may instead give a confident, well-structured, completely wrong answer. Confidence and correctness are not the same signal.

This is called **hallucination**: the AI generates plausible-sounding content that is factually incorrect.

**Examples of hallucination:**
- Citing academic papers that don't exist
- Inventing statistics with specific numbers
- Making up features of real products
- Creating fake but realistic-looking legal precedents

**The rule:** AI output needs human verification. Always. Especially for facts, numbers, quotes, and references.

---

## Part 2: What AI Tools Are Good At

### Reliable Strengths

These are tasks where AI tools consistently perform well:

**1. Drafting and Writing**
- First drafts of emails, reports, proposals
- Rewriting text for different audiences (formal → casual, technical → plain language)
- Expanding bullet points into paragraphs
- Condensing long documents into summaries

**Why it works well:** Writing follows patterns (grammar, structure, tone) that AI has seen billions of examples of.

**2. Summarising and Extracting**
- Condensing a 20-page report to key points
- Pulling specific information from long documents
- Creating meeting summaries from notes
- Extracting data from unstructured text

**Why it works well:** The information is already there, AI just needs to identify what's important based on your instructions.

**3. Brainstorming and Ideation**
- Generating options you haven't considered
- Exploring a problem from different angles
- Creating lists of possibilities
- Playing devil's advocate on your ideas

**Why it works well:** AI has seen enormous variety in how people approach problems, so it can suggest angles you might not think of.

**4. Formatting and Transforming**
- Converting data between formats (CSV to table, list to paragraph)
- Restructuring documents
- Creating consistent formatting across materials
- Generating templates from examples

**Why it works well:** Format conversion is pure pattern-matching, exactly what AI excels at.

**5. Explaining and Teaching**
- Breaking down complex concepts into simple language
- Explaining technical topics to non-technical audiences
- Creating step-by-step instructions
- Answering "how does X work?" questions

**Why it works well:** The AI has seen thousands of explanations of most topics and can adapt the level to your needs.

**6. Data Analysis (with the right approach)**
- Finding patterns in spreadsheets
- Creating charts and visualisations
- Running basic statistical analysis
- Answering questions about datasets

**Why it works well:** Data analysis follows well-defined procedures that AI can execute, but results need human interpretation.

---

## Part 3: Where AI Tools Fall Apart

### Known Weaknesses

These are tasks where AI tools regularly fail or produce unreliable results:

**1. Factual Accuracy**
- AI does not "know" facts the way you do
- It generates text that *sounds* factual based on patterns
- Specific numbers, dates, names, and citations can be wrong or fabricated
- An answer may rely on stale training data, a poor retrieved source, or supplied material read out of context. Ask what source supports each load-bearing claim

**The fix:** Always verify facts, especially numbers and references. Use AI for structure and drafting, not as a source of truth.

**2. Hidden calculations**
- Mental arithmetic inside a language model can go wrong, especially across many steps
- A model that writes and runs code, calls a calculator, or works in a spreadsheet can be much more reliable, but it can still choose the wrong method, fields, or filters
- Spreadsheet formulas it writes may contain errors

**The fix:** Ask how a number was produced. Prefer a visible calculation or code path you can inspect, then verify the result against the source.

**3. Long or hidden reasoning**
- Current models can work through some multi-step problems well
- They can also miss contradictions, lose constraints, or build a tidy argument on a false premise
- They may agree with you when pushed. That agreeable fold is called sycophancy

**The fix:** Surface assumptions and steps. Test each load-bearing step against evidence. Do not accept a change of assessment unless a new fact justifies it, and ask which fact did.

**4. Understanding Your Specific Context**
- AI doesn't know your company, your team, your industry norms
- It gives generic advice unless you provide specific context
- It can't read the room or understand office politics
- It doesn't know what happened in yesterday's meeting

**The fix:** Provide context explicitly. Relevant background, audience, stakes, constraints, and examples usually matter more than clever phrasing. Briefing well is the core of the workshop.

**5. Consistency Across Long Conversations**
- AI can contradict itself in long conversations
- It may "forget" instructions from earlier in the chat
- Style and tone can drift over time
- Complex multi-part tasks may lose coherence

**The fix:** For important work, start fresh conversations. Restate key requirements. Don't assume the AI "remembers" what you discussed 20 messages ago.

---

## Part 4: The AI Landscape Beyond Chatbots

### AI Is Bigger Than Chat

Chatbots are the most visible AI tools, but AI is increasingly embedded in software you already use:

**AI in Productivity Software:**
- Microsoft Copilot in Word, Excel, PowerPoint, Outlook
- Google Workspace AI in Docs, Sheets, Gmail
- Note and document workspaces with drafting and search assistance
- Design tools with image and layout generation

**AI in specialist tools:**
- Meeting transcription and action extraction
- Writing and presentation assistance
- Data visualisation and anomaly flagging
- Customer, finance, HR, and service platforms that classify, draft, or route work

**AI in Automation Platforms:**
- Zapier (connecting apps with AI steps)
- Make (workflow automation)
- Power Automate (Microsoft ecosystem automation)

**The trend:** AI is moving from "a separate tool you go to" to "a capability built into every tool you already use." Within a few years, using AI won't feel like a separate activity, it'll just be how software works.

### Types of AI Assistance

Not all AI assistance is the same. Understanding the spectrum helps you set expectations:

| Type | What It Does | Example | Your Role |
|------|-------------|---------|-----------|
| **Autocomplete** | Finishes what you started | Gmail Smart Compose | Accept/reject suggestions |
| **Co-pilot** | Works alongside you in real-time | GitHub Copilot, Excel Copilot | Guide and review |
| **Chat assistant** | Responds to requests conversationally | ChatGPT, Claude | Ask, review, iterate |
| **Automation** | Executes multi-step workflows | Zapier AI, Power Automate | Set up, monitor, handle exceptions |
| **Agent** | Completes goals autonomously | AI research agents | Define goal, review output |

In the workshop, we'll focus primarily on **chat assistant** and **co-pilot** interactions, as these give you the most control and learning.

---

## Part 5: Staying Safe, Privacy, Security, and Common Sense

### What Happens to Your Data?

When you type something into an AI tool, you should assume:

- **Consumer and free accounts:** training, retention, memory, and sharing settings vary by product and can change. Check the current settings, not last year's summary.
- **Work and enterprise accounts:** your organisation's contract and admin settings matter more than the product label. Follow the approved-tool policy.
- **In every tier:** treat a cloud assistant as someone else's computer unless your organisation has approved that service for that class of data.

**Assistants can also remember you across sessions.** Modern AI assistants keep knowledge about you in up to three separate places: the facts you explicitly asked them to save, the inferences they've drawn from your conversations, and the chat history itself. Deleting a chat does not delete what the assistant learned from it, memory and personalisation settings are managed separately. If an assistant ever starts to feel "too personal", look in its settings for memory, personalisation, or data controls. And for conversations you'd rather it not learn from, use private or temporary chat mode, which doesn't read from or write to memory.

### The Golden Rules

**1. Never enter confidential or sensitive information into free AI tools**
- Customer personal data
- Financial information
- Proprietary business data
- Passwords, API keys, credentials
- Employee personal information

**2. Check your company's AI policy**
- Many organisations now have AI usage policies
- Some restrict which tools can be used
- Some require enterprise accounts for work data
- If your company doesn't have a policy yet, ask about it

**3. Never publish AI output without review**
- AI-generated content can contain errors, bias, or plagiarism
- You are responsible for anything you send, publish, or submit, even if AI wrote it
- "The AI wrote it" is not a defence

**4. Be transparent about AI use**
- If your organisation or client expects original work, disclose AI assistance
- Academic and professional contexts increasingly require AI disclosure
- When in doubt, mention it

### Copyright and Ownership

This area is evolving rapidly, but the current state:

- **Your input:** you remain responsible for having the right to supply it
- **AI output:** ownership and copyright protection can depend on jurisdiction, human contribution, and provider terms
- **Training and source material:** output may resemble or reuse patterns from existing work, so similarity and attribution still need checking
- **Practical advice:** Treat AI output as a draft. Add your expertise, verify sources, and follow your organisation's policy. Ask a qualified adviser for consequential legal questions.

---

## Part 6: The Right Mindset

### AI Is a Tool, Not a Colleague

The most productive way to think about AI tools:

**Think of AI as a very fast, very well-read intern:**
- Eager to help
- Can produce decent first drafts quickly
- Needs clear instructions
- Makes mistakes if not supervised
- Gets better with specific feedback
- Doesn't understand what it doesn't understand

**Don't think of AI as:**
- A replacement for your expertise
- A source of truth
- An infallible calculator
- A colleague who understands context
- A system you can set and forget

### The Human-AI Sweet Spot

The best results come from combining AI speed with human judgment:

| AI Does | You Do |
|---------|--------|
| Generate first draft | Edit, refine, add expertise |
| Find patterns in data | Interpret what patterns mean |
| Suggest options | Choose the right option |
| Format and structure | Verify accuracy and relevance |
| Work fast | Think deep |

**The professionals who get the most from AI aren't the ones who ask it to do everything, they're the ones who know exactly which parts to delegate and which to keep.** Everyone has access to the same tools, so generic AI skills are quickly becoming the baseline. The edge is your judgement: knowing what to ask for, when to trust the answer, and where a human must stay in charge. That judgement is the theme of the workshop, and you'll learn a simple grid for it, called the trust tool. If you want a head start, there is a two-minute practice game online: [trusttool.borck.education](https://trusttool.borck.education/).

### Scepticism is useful

Healthy scepticism is an asset with AI tools:
- Question outputs, especially facts and numbers
- Test claims before relying on them
- Compare AI suggestions to your own knowledge
- Start small and build trust gradually

The workshop will help you develop practical judgement about when to trust AI output and when to verify it.

---

## Part 7: Preparing for the Workshop

### Before You Arrive

**Set up accounts (10 minutes):**

Set up **one** of these before the day (a free tier is fine). A second account is a useful backup if setup is quick:

1. **ChatGPT**: [chatgpt.com](https://chatgpt.com)
   - Create account with email
   - Free tier is sufficient

2. **Claude**: [claude.ai](https://claude.ai)
   - Create account with email
   - Free tier is sufficient

3. **Google Gemini**: [gemini.google.com](https://gemini.google.com)
   - Uses your Google account
   - Free tier is sufficient

**Test your access (5 minutes):**
- Log in to each tool
- Type a simple prompt: "Explain what you do in one sentence"
- Make sure you get a response
- If you're on a corporate network, check that the sites aren't blocked

**Think about your work (5 minutes):**
- What's one task you do every week that feels repetitive?
- What's one type of document you create regularly?
- What's one area where you wish you had a smart assistant?

You'll use these in the workshop exercises.

### What to Bring

- **Laptop** (not tablet, you'll need multiple browser tabs open)
- **Charger** (full day of screen work)
- **A real task** from your work (optional but valuable for Exercise 4)
- **Curiosity** and willingness to experiment

### What to Expect

The workshop is hands-on. You'll spend most of the day working with AI tools, not listening to lectures. Expect to:

- Try things that don't work on the first attempt
- See others get different results from the same tools
- Be surprised by what AI can do well
- Be equally surprised by what it gets wrong
- Leave with techniques you can use immediately

**There's no such thing as a stupid question in this workshop.** Everyone is at a different starting point, and the pace is designed to challenge both beginners and experienced users.

---

## Key Takeaways

1. **LLMs generate plausible next tokens; assistants may add search, files, memory, code, and tools**: they're pattern-matching engines, not thinking machines. Understanding this changes how you use them.

2. **Strong at drafting, weak at facts**: use AI for structure, writing, brainstorming, and formatting. Verify facts, numbers, and references yourself.

3. **Hallucination is the key risk**: AI delivers wrong answers with total confidence. Always review output critically.

4. **Context is everything**: the more specific information you provide, the better the output. Vague prompts produce vague results.

5. **Your data isn't necessarily private**: check your company's AI policy and never enter sensitive information into free-tier tools.

6. **AI is a tool, not a replacement**: the best results come from human expertise combined with AI speed. Know which parts to delegate.

7. **Healthy scepticism is an asset**: question, verify, and test. The professionals who get the most from AI are the ones who know its limits.

8. **Everyone is still figuring this out**: you're not behind. The technology is new and evolving. The workshop will give you practical skills to start using it effectively.

---

## Glossary

Terms you'll hear in the workshop:

| Term | Plain English |
|------|--------------|
| **Prompt** | The instructions or question you type into an AI tool |
| **LLM (Large Language Model)** | The technology behind ChatGPT, Claude, Gemini, trained on text to predict words |
| **Hallucination** | When AI generates confident but incorrect information |
| **Context window** | How much text the AI can "see" at once (like short-term memory) |
| **Token** | A chunk of text an LLM processes; only a rough guide to words |
| **Machine learning (ML)** | Software that learns patterns from examples rather than only following hand-written rules |
| **Neural network / deep learning** | A layered model that learns representations from data |
| **NLP** | Natural language processing: language tasks such as classification, translation, extraction, and summarisation |
| **Briefing (prompting)** | Giving an assistant the role, task, context, examples, constraints, and format it needs |
| **Agent** | A model in a loop with tools that can plan and take steps toward a goal |
| **Skill** | A reusable plain-text brief a tool loads when a request matches it |
| **BYOD** | Bring Your Own Device, you'll need your laptop for the workshop |
| **Generative AI** | AI that creates new content (text, images, code) rather than just classifying or predicting |

---

## Further Reading

These are optional, the pre-reading above is sufficient preparation for the workshop.

- Mollick, Ethan. 2024. *Co-Intelligence: Living and Working with AI.* New York: Portfolio/Penguin.
- Mollick, Ethan. "One Useful Thing" (Substack). Practical, regularly updated AI insights for professionals. [oneusefulthing.org](https://www.oneusefulthing.org/)
- Anthropic. 2024. "Prompt Engineering Guide." [docs.anthropic.com/en/docs/build-with-claude/prompt-engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- OpenAI. 2024. "Prompt Engineering Guide." [platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- Harvard Business Review. 2023. "AI Won't Replace Humans, But Humans With AI Will Replace Humans Without AI." HBR Digital.
