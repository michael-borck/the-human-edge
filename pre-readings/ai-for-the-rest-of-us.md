# AI for the Rest of Us: A Practical Introduction

## Summary

AI tools like ChatGPT, Claude, and Gemini are now freely available to anyone with a browser. They can draft emails, summarise documents, analyse data, write code, and brainstorm ideas, but they also hallucinate facts, miss nuance, and confidently deliver nonsense. This pre-reading gives you the conceptual foundation you need before the workshop: how these tools actually work (pattern-matching, not thinking), what they're reliably good at, where they fall apart, and how to stay safe with company data. The goal isn't to make you an expert, it's to get you comfortable enough that the workshop can focus on building real skills, not explaining basics.

**Reading time:** 20 minutes
**Key takeaway:** AI tools are powerful pattern-matching assistants, not intelligent colleagues, the better you understand what's actually happening, the better results you'll get.

---

## Who This Is For

This is not a reading for executives making investment decisions or project managers leading AI initiatives. This is for **you**: a professional who wants to use AI tools effectively in your daily work.

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

When people say "AI" today, they usually mean one of these:

| Tool | Made By | What It Is |
|------|---------|------------|
| ChatGPT | OpenAI | Conversational AI, chat, write, analyse, code |
| Claude | Anthropic | Conversational AI, similar to ChatGPT, different strengths |
| Gemini | Google | Conversational AI, integrated with Google Workspace |
| Microsoft Copilot | Microsoft | AI embedded in Word, Excel, PowerPoint, Outlook |
| Notion AI | Notion | AI built into the Notion workspace |
| Grammarly | Grammarly | AI writing assistant |

These are all built on the same underlying technology: **large language models (LLMs)**.

### How They Actually Work

Here's the most important thing to understand about AI tools:

**They predict the next word.**

That's it. When you type "Write me an email to a client about...", the AI doesn't *understand* your request the way a colleague would. It predicts what words are most likely to come next, based on patterns it learned from billions of pages of text during training.

Think of it as **autocomplete on steroids:**
- Your phone's autocomplete predicts one word at a time
- AI tools predict thousands of words at a time
- The result often *looks* like understanding, but it's pattern-matching

**Why this matters to you:**
- AI is incredibly good at tasks where patterns exist (writing styles, document formats, data structures)
- AI is unreliable at tasks requiring genuine understanding (novel reasoning, factual accuracy, nuanced judgment)
- Your job is to know the difference

### The "Confident Nonsense" Problem

AI tools have a distinctive failure mode: **they never say "I don't know."**

Ask a colleague a question they can't answer, and they'll say "I'm not sure, let me check." Ask an AI the same question, and it will give you a confident, well-structured, completely wrong answer.

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
- Specific numbers, dates, names, and citations are frequently wrong
- Recent events may be unknown (training data has a cutoff date)

**The fix:** Always verify facts, especially numbers and references. Use AI for structure and drafting, not as a source of truth.

**2. Maths and Precise Calculations**
- AI makes arithmetic errors regularly
- Complex calculations are unreliable
- It may round, estimate, or hallucinate numbers
- Spreadsheet formulas it writes may contain errors

**The fix:** Use AI to write formulas or set up analysis, then verify the results. Don't trust AI-generated numbers without checking.

**3. Logical Reasoning**
- Multi-step logic problems trip AI up
- It can miss obvious contradictions
- Complex "if-then" chains become unreliable
- It may agree with you even when you're wrong

**The fix:** For complex reasoning, break the problem into small steps and verify each one. Don't rely on AI for critical logical deductions.

**4. Understanding Your Specific Context**
- AI doesn't know your company, your team, your industry norms
- It gives generic advice unless you provide specific context
- It can't read the room or understand office politics
- It doesn't know what happened in yesterday's meeting

**The fix:** Provide context explicitly. The more specific information you give, the more relevant the output. This is what prompt engineering is about, and it's the core of the workshop.

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
- Notion AI for notes and documentation
- Canva AI for design

**AI in Specialist Tools:**
- Grammarly (writing quality)
- Otter.ai (meeting transcription)
- Beautiful.ai (presentation design)
- Tableau AI (data visualisation)

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

- **Free tiers:** Your input may be used to train future models. Don't enter sensitive data.
- **Paid tiers:** Most providers (OpenAI, Anthropic, Google) have "no training" policies for paid accounts, but read the terms.
- **Enterprise tiers:** Typically the strongest data protection guarantees.

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

- **Your prompts:** You own what you write
- **AI output:** Copyright status is legally unclear in most jurisdictions
- **Training data:** AI may reproduce patterns from copyrighted material
- **Practical advice:** Treat AI output as a starting point that you modify and make your own. The more you edit and add your expertise, the more clearly it's your work.

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

### It's OK to Be Skeptical

Healthy skepticism is an asset with AI tools:
- Question outputs, especially facts and numbers
- Test claims before relying on them
- Compare AI suggestions to your own knowledge
- Start small and build trust gradually

The workshop will help you develop practical judgment about when to trust AI output and when to verify it.

---

## Part 7: Preparing for the Workshop

### Before You Arrive

**Set up accounts (10 minutes):**

You'll need active accounts on at least two of these (free tiers are fine):

1. **ChatGPT**: [chat.openai.com](https://chat.openai.com)
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

1. **AI tools predict the next word**: they're pattern-matching engines, not thinking machines. Understanding this changes how you use them.

2. **Strong at drafting, weak at facts**: use AI for structure, writing, brainstorming, and formatting. Verify facts, numbers, and references yourself.

3. **Hallucination is the key risk**: AI delivers wrong answers with total confidence. Always review output critically.

4. **Context is everything**: the more specific information you provide, the better the output. Vague prompts produce vague results.

5. **Your data isn't necessarily private**: check your company's AI policy and never enter sensitive information into free-tier tools.

6. **AI is a tool, not a replacement**: the best results come from human expertise combined with AI speed. Know which parts to delegate.

7. **Healthy skepticism is an asset**: question, verify, and test. The professionals who get the most from AI are the ones who know its limits.

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
| **Token** | A chunk of text (roughly 3/4 of a word), how AI measures input/output |
| **Fine-tuning** | Customising an AI model for a specific use case |
| **RAG (Retrieval-Augmented Generation)** | Connecting AI to specific documents so it answers from your data |
| **Prompt engineering** | The skill of writing effective prompts to get good AI output |
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
