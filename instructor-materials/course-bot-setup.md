# Course-assistant chatbot: setup & config

The site-wide tutor / live-FAQ bot on the companion site (injected on every page
via `course-bot.html` → `_quarto.yml` `include-after-body`).

| | |
|---|---|
| AnythingLLM workspace | `the-human-edge-course` (chat.eduserver.au) |
| Embed UUID | `10d0eb94-0c5a-4696-a41d-3ff83b9e1eea` (in `course-bot.html`) |
| Model | AnythingLLM system default |
| Retrieval | `similarityThreshold: 0`, `topN: 6` (defaults 0.25 / 4 are too strict; they made the delivery bot miss the schedule) |
| Chat mode | `chat` (uses retrieved docs **and** the model's own knowledge) |

## Knowledge (22 docs, student-facing only)
The 3 readings, the 6 site pages (`index/before/workshop/frameworks/team/series.qmd`),
the 4 initiative cards, the 3 sprint worksheets, the 2 morning worksheets
(prompt library, workflow redesign), `frameworks-overview.md` + the 2 framework
handouts, and the system-prompt text itself. **Not** included: instructor
materials, the slide deck's speaker notes, or the course proposal.

## Create the embed (one-time; UI-only in this AnythingLLM version)
Embed configs are created via the API endpoint that post-dates the older
`/workspace/{slug}/embed` route botstash expects:

```
POST /api/v1/embed/new      body: {"workspace_slug":"the-human-edge-course","chatMode":"chat"}
POST /api/v1/embed/{uuid}   body: {"chat_mode":"chat"}     # set to chat mode
```

`botstash chatbot` retrieval is incompatible with this server version (the old
`GET /workspace/{slug}/embed` route is SPA-caught), so the UUID is set directly
in `course-bot.html`.

## Rebuild (when course material changes)
Stage the student-facing files into a folder (macOS: delete `._*` AppleDouble
files first — they pollute the knowledge base), then:

```
find _botstash-staging -name '._*' -delete
botstash run _botstash-staging --workspace the-human-edge-course --reset
```

`--reset` clears + re-uploads docs and **preserves** the system prompt and
retrieval settings. After changing material, re-set the prompt/retrieval if
needed (see below).

## Set the prompt + retrieval (API)
`POST /api/v1/workspace/the-human-edge-course/update` with
`{"openAiPrompt": "<the tutor/FAQ prompt>", "similarityThreshold": 0.0, "topN": 6}`.
The current prompt is the "The Human Edge course assistant … tutor/FAQ" system
prompt in `_botstash-staging/_system_prompt.txt` (tutor stance + the
generic-is-the-baseline thesis + off-limits rules).

## Scope (what it will / won't answer)
- **Answers:** course content + logistics; and broader AI / AI-in-business /
  AI-delivery / AI-leadership questions from general knowledge, tying back to
  the course where it can. It's a *tutor*: it answers, then nudges critical
  thinking, and won't do a participant's workshop deliverable for them.
- **Declines:** anything unrelated to AI or the course (trivia, other subjects,
  personal advice), and NSFW/inappropriate content.
