#!/usr/bin/env python3
"""Build the editorial 'Human Edge' deck as a real, editable PowerPoint.

Same visual language as the bespoke HTML deck (cream paper, ink, vermilion
accent; Impact display + Georgia serif + Arial body + JetBrains Mono labels;
hero sketches in bordered hard-shadow frames; colour-block section dividers;
big pull-quotes) — but as a genuine .pptx you can edit, present and add speaker
notes to. Editable > bespoke.

Usage:  python3 scripts/build-deck-pptx.py
Output: content/the-human-edge-deck.pptx
"""
from __future__ import annotations
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "content" / "images"
OUT = ROOT / "content" / "the-human-edge-deck.pptx"

# palette
PAPER   = RGBColor(0xf4, 0xef, 0xe3)
PAPER2  = RGBColor(0xec, 0xe5, 0xd4)
INK     = RGBColor(0x18, 0x16, 0x13)
INKSOFT = RGBColor(0x4a, 0x44, 0x3c)
VERM    = RGBColor(0xe3, 0x4f, 0x29)
OCHRE   = RGBColor(0xcf, 0x9a, 0x2f)
WHITE   = RGBColor(0xff, 0xff, 0xff)
FAINT   = RGBColor(0xcb, 0xc3, 0xb0)

# fonts (installed on the build Mac; graceful substitute elsewhere)
FD, FS, FN, FM = "Impact", "Georgia", "Arial", "JetBrains Mono"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = 13.333, 7.5
BLANK = prs.slide_layouts[6]
ML = 0.95  # left margin
CW = SW - 2 * ML  # content width


def slide(bg=PAPER):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = bg
    return s


def rect(s, l, t, w, h, fill=None, line=None, lw=1.0):
    sh = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    if fill is None:
        sh.fill.background()
    else:
        sh.fill.solid(); sh.fill.fore_color.rgb = fill
    if line is None:
        sh.line.fill.background()
    else:
        sh.line.color.rgb = line; sh.line.width = Pt(lw)
    sh.shadow.inherit = False
    return sh


def text(s, l, t, w, h, paras, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, wrap=True):
    """paras: list of paragraphs; each paragraph is a string, a (text, style) tuple,
    or a list of (text, style) run-tuples. style is a dict of font/size/color/bold/italic/spacing."""
    tb = s.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = wrap
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        runs = para if isinstance(para, list) else [para if isinstance(para, tuple) else (para, {})]
        for rtext, st in runs:
            r = p.add_run(); r.text = rtext
            r.font.name = st.get("font", FN)
            r.font.size = Pt(st.get("size", 16))
            r.font.bold = st.get("bold", False)
            r.font.italic = st.get("italic", False)
            r.font.color.rgb = st.get("color", INK)
            if "spacing" in st:
                p.line_spacing = st["spacing"]
            if st.get("space_after") is not None:
                p.space_after = Pt(st["space_after"])
    return tb


def kicker(s, label, l=ML, t=0.7, color=VERM):
    text(s, l, t, CW, 0.4, [(label.upper(), dict(font=FM, size=11, color=color, bold=True))])


def bignum(s, n):
    text(s, SW - 3.4, 0.35, 3.0, 2.2, [(f"{n:02d}", dict(font=FD, size=120, color=FAINT))],
         align=PP_ALIGN.RIGHT)


def foot(s, left):
    text(s, ML, SH - 0.6, CW, 0.3,
         [(left, dict(font=FM, size=9, color=INKSOFT)),
          ("", dict(font=FM, size=9, color=INKSOFT))])
    # right-aligned page note via second textbox
    text(s, SW - 3.0, SH - 0.6, 2.05, 0.3, [("", {})], align=PP_ALIGN.RIGHT)


def img_frame(s, name, l, t, w, h):
    rect(s, l + 0.14, t + 0.14, w, h, fill=INK)  # hard shadow
    pic = s.shapes.add_picture(str(IMG / name), Inches(l), Inches(t), Inches(w), Inches(h))
    pic.line.color.rgb = INK; pic.line.width = Pt(1.75)
    pic.shadow.inherit = False
    return pic


# ---------- slide builders ----------
def cover():
    s = slide()
    bignum(s, 1)
    rect(s, ML, 1.0, 2.5, 0.45, fill=VERM)
    text(s, ML, 1.0, 4.0, 0.45, [("ONE-DAY MASTERCLASS", dict(font=FM, size=11, color=WHITE, bold=True))],
         anchor=MSO_ANCHOR.MIDDLE)
    kicker(s, "Curtin Executive Education · Dr Michael Borck", t=1.7)
    text(s, ML, 2.2, 11.4, 4.4,
         [("THE\n", dict(font=FD, size=118, color=INK, spacing=0.88)),
          ("HUMAN\n", dict(font=FD, size=118, color=INK, spacing=0.88)),
          ("EDGE", dict(font=FD, size=118, color=INK, spacing=0.88))])
    text(s, ML, 6.65, 11.4, 0.5,
         [("Using & delivering AI with judgement.", dict(font=FS, size=26, italic=True, color=INKSOFT))])


def section(bg, eyebrow, title_lines, lead):
    s = slide(bg)
    text(s, ML, 1.7, 11.4, 0.5, [(eyebrow.upper(), dict(font=FM, size=14, color=WHITE, bold=True))])
    paras = [(line + "\n", dict(font=FD, size=92, color=WHITE, spacing=0.9)) for line in title_lines]
    text(s, ML, 2.5, 11.8, 3.8, paras)
    text(s, ML, SH - 1.7, 9.5, 1.2, [(lead, dict(font=FS, size=24, italic=True, color=WHITE))])


def quote(idx, label, qtext, attr):
    s = slide(); bignum(s, idx)
    kicker(s, label)
    text(s, ML, 1.9, 1.5, 1.5, [("“", dict(font=FS, size=200, color=VERM))])
    text(s, ML + 0.6, 2.7, 11.2, 3.2, [(qtext, dict(font=FS, size=40, color=INK, spacing=1.05))])
    text(s, ML + 0.6, SH - 1.4, 11.2, 0.5, [(attr.upper(), dict(font=FM, size=11, color=INKSOFT, bold=True))])


def concept(idx, label, title, body_runs, img_name):
    s = slide(); bignum(s, idx)
    img_frame(s, img_name, ML, 1.4, 6.0, 5.0)
    tx, tw = 7.5, 5.0
    text(s, tx, 1.5, tw, 0.4, [(label.upper(), dict(font=FM, size=11, color=VERM, bold=True))])
    text(s, tx, 2.0, tw, 2.4, [(title, dict(font=FS, size=40, color=INK, bold=True, spacing=0.98))])
    text(s, tx, 4.3, tw, 2.6, [(body_runs, dict(font=FN, size=15, color=INKSOFT, spacing=1.25))])


def grid(idx, label, title, title_italic_tail, items, cols=2, footleft=None):
    s = slide(); bignum(s, idx)
    kicker(s, label)
    tline = [(title, dict(font=FS, size=46, color=INK, bold=True))]
    if title_italic_tail:
        tline.append((" " + title_italic_tail, dict(font=FS, size=46, color=INK, italic=True, bold=False)))
    text(s, ML, 1.5, CW, 1.6, [tline])
    # items
    top = 3.5
    colw = (CW - (cols - 1) * 0.6) / cols
    for i, (lab, desc) in enumerate(items):
        c = i % cols; r = i // cols
        x = ML + c * (colw + 0.6); y = top + r * 1.85
        rect(s, x, y, colw, 0.03, fill=INK)  # top rule
        text(s, x, y + 0.12, colw, 0.6, [(lab, dict(font=FD, size=22, color=VERM))])
        text(s, x, y + 0.72, colw, 1.0, [(desc, dict(font=FN, size=12.5, color=INKSOFT, spacing=1.12))])
    if footleft:
        foot(s, footleft)


def feature(idx, label, title, body_html, footleft=None):
    s = slide(); bignum(s, idx)
    kicker(s, label)
    text(s, ML, 1.7, 10.5, 2.4, [(title, dict(font=FS, size=46, color=INK, bold=True, spacing=1.0))])
    text(s, ML, 4.0, 10.8, 3.0, [(body_html, dict(font=FN, size=16, color=INKSOFT, spacing=1.3))])
    if footleft:
        foot(s, footleft)


def steps(idx, label, title, items):
    s = slide(); bignum(s, idx)
    kicker(s, label)
    text(s, ML, 1.5, CW, 1.2, [(title, dict(font=FS, size=46, color=INK, bold=True))])
    top = 3.3; colw = (CW - 2 * 0.7) / 3
    for i, (n, h, body) in enumerate(items):
        x = ML + i * (colw + 0.7)
        rect(s, x, top, colw, 0.04, fill=INK)
        text(s, x, top + 0.15, colw, 0.9, [(n, dict(font=FD, size=34, color=VERM))])
        text(s, x, top + 1.0, colw, 0.8, [(h, dict(font=FS, size=19, color=INK, bold=True))])
        text(s, x, top + 1.8, colw, 2.0, [(body, dict(font=FN, size=12.5, color=INKSOFT, spacing=1.15))])


def brk(idx, img_name, time, label, back):
    s = slide(); bignum(s, idx)
    rect(s, SW/2 - 1.7, 1.7 + 0.14, 3.4, 2.5, fill=INK)  # hard shadow first
    pic = s.shapes.add_picture(str(IMG / img_name), Inches(SW/2 - 1.7), Inches(1.7), Inches(3.4), Inches(2.5))
    pic.line.color.rgb = INK; pic.line.width = Pt(1.75); pic.shadow.inherit = False
    text(s, ML, 4.5, CW, 1.4, [(time, dict(font=FD, size=92, color=VERM))], align=PP_ALIGN.CENTER)
    text(s, ML, 5.8, CW, 0.8, [(label, dict(font=FS, size=34, italic=True, color=INK))], align=PP_ALIGN.CENTER)
    text(s, ML, SH - 0.95, CW, 0.4, [(back.upper(), dict(font=FM, size=11, color=INKSOFT, bold=True))], align=PP_ALIGN.CENTER)


def close_deck():
    s = slide()
    bignum(s, 99)
    text(s, ML, 2.0, CW, 0.5,
         [("THE AI IS YOUR STARTING POINT, NOT YOUR FINISH LINE", dict(font=FM, size=12, color=VERM, bold=True))],
         align=PP_ALIGN.CENTER)
    text(s, ML, 2.8, CW, 3.2,
         [("STAY THE ONE\n", dict(font=FD, size=72, color=INK, spacing=0.92)),
          ("HOLDING THE\n", dict(font=FD, size=72, color=INK, spacing=0.92)),
          ("JUDGEMENT.", dict(font=FD, size=72, color=INK, spacing=0.92))], align=PP_ALIGN.CENTER)
    text(s, ML, SH - 1.1, CW, 0.5,
         [("michael-borck.github.io/the-human-edge", dict(font=FS, size=20, italic=True, color=INKSOFT))],
         align=PP_ALIGN.CENTER)


# ---------- build ----------
cover()
quote(2, "The provocation we'll spend the day on",
      "If the AI is good at running your work, it's good at running everyone else's. Generic competence is the baseline — not the advantage.",
      "So where does your edge live?")
grid(3, "Today", "One idea. Two scales.", None,
     [("MORNING", "The judgement, at the level of your own work: the trust tool, RTCF, the two-pass demo."),
      ("AFTERNOON", "The same judgement, lifted to delivery: the five differences, human-in-the-loop, the go/no-go.")],
     footleft="The trust tool — taught once, reused at project scale")
section(VERM, "Part one", ["THE AVERAGE,", "THE TOOL,", "YOUR EDGE."],
        "Personal fluency — the judgement that lasts after the next model ships.")
concept(5, "What AI actually is", "It predicts the next word.",
        "Autocomplete, scaled up. Trained on billions of pages, it learned what tends to follow what. The result looks like understanding. It's pattern-matching.",
        "autocomplete-on-steroids.jpg")
concept(6, "The one mental model to keep", "A convincing average.",
        "Fluent, plausible, usually about-right. But \"about right\" and \"exactly right\" are not the same — and knowing which you need is the whole game.",
        "convincing-average.jpg")
grid(7, "Once you see it as an averaging machine", "Brilliant here. Quietly wrong there.", None,
     [("BRILLIANT", "Drafting, summarising, formatting, brainstorming, explaining, finding patterns — where \"the plausible version\" is the answer."),
      ("UNRELIABLE", "Precise facts, figures, citations, multi-step logic, your context, ethics — where there's one right answer it can't verify.")])
concept(8, "Not a bug — a property", "Confident. Wrong. Same polish.",
        "It never says \"I don't know.\" The fluent-but-wrong answer looks identical to the fluent-and-right one. Nothing in the tone warns you.",
        "confident-nonsense.jpg")
grid(9, "The spine of the day", "The trust tool.", None,
     [("AVERAGE → LEAN IN", "Low stakes, \"about right\" is fine. Let AI run; you glance."),
      ("PRECISE → HUMAN IN THE LOOP", "High stakes, one right answer. A person owns the decision.")],
     footleft="Learned once this morning — reused at project scale this afternoon")
feature(10, "The trust tool, on real tasks", "Average or precise? Small or large?",
        "Drafting an internal email. Average is fine, stakes small — lean in.\nBoard-paper figures. Precision required, stakes large — a human owns every number.\nSummarising fifty complaints for themes. Lean in for the themes, then skim for the one complaint the AI smoothed away.")
grid(11, "Talking to AI well", "RTCF — two halves.", None,
     [("R · T · F  SCAFFOLDING", "Weaker & self-hosted models need it spelled out. A frontier model infers it from clear writing."),
      ("C  ALWAYS MATTERS", "Context is the one thing only you supply. No model manufactures your edge.")],
     footleft="The durable skill: being clear about what you want")
feature(12, "Before & after", "Unusable. Then sendable.",
        "Without: \"Write an email about the project delay.\"\nWith RTCF: a senior PM, professional & empathetic, writes a client email explaining a 2-week delay (vendor integration; client values transparency; new date March 15), under 200 words — acknowledge → explain → new date → recommit.\nContext is where your edge enters.")
concept(13, "The money moment — live", "Add your edge. It gets a soul.",
        "Pass 1: a naive prompt → slick, correct, identical for everyone. Pass 2: layer in what only you hold. Watch the output turn yours.",
        "two-pass-demo.jpg")
feature(14, "Exercise — on your own work", "Redesign one workflow.",
        "Pick a task you own. List its steps. Judge each with the trust tool — where does AI genuinely help, where must your judgement stay in charge? Redesign so AI handles the average and you keep the high-stakes parts. You leave with something to trial next week.")
feature(15, "Where we are by lunch", "A mental model, a grid, a method.",
        "AI produces a convincing average. The trust tool tells you when to lean in. RTCF directs it well — and Context is the part that survives any model. One question for the afternoon: if this is how I trust AI on a single task, how do I trust it across a whole project?")
brk(16, "break-morning-tea.jpg", "10:30", "Morning tea", "Back at 11:00")
section(INK, "Part two", ["WHY AI", "DELIVERY IS", "DIFFERENT."],
        "You're the delivery lead. Ship one funded initiative — without the predictable failures.")
quote(18, "The fair question",
      "I've delivered projects before. What's actually different about an AI project?",
      "They don't fail more often. They fail differently — in places you didn't see coming.")
grid(19, "Five ways AI breaks the rules you usually lead by", "They fail", "differently.",
     [("01", "\"Done\" can't be specified."), ("02", "The demo is a trap."),
      ("03", "The data is the uncertainty."), ("04", "Verification is the product."),
      ("05", "Generic competence is the baseline."), ("→", "So you design the human in.")],
     cols=3)
concept(20, "Difference 01", "\"Done\" won't hold still.",
        "Ask twice, get two answers. There's no single correct output — only a spread. Stop chasing a fixed spec; decide what \"good enough\" looks like for this use.",
        "done-cant-be-specified.jpg")
concept(21, "Difference 02", "The demo is a trap.",
        "It shows the happy path. The messy real-world cases are where it falls over. Treat the demo as the start of the hard part — not the end.",
        "demo-is-a-trap.jpg")
concept(22, "Difference 03", "The data is the uncertainty.",
        "You don't order it; you discover it — its gaps, biases and surprises show up only when you work with it. Run delivery as discovery, and build the learning into the plan.",
        "data-is-the-uncertainty.jpg")
concept(23, "Difference 04", "Verification is the product.",
        "Outputs vary and can be confidently wrong. The value lives in how you check them, and where a human stays in the loop. Design the checking deliberately — make it part of what you ship.",
        "verification-is-the-product.jpg")
concept(24, "Difference 05", "Generic is the baseline, not the edge.",
        "When every rival runs the same models, the model isn't your advantage — anyone can have it. Compete on the human variation a rival's identical model can't reproduce.",
        "where-your-edge-lives.jpg")
quote(25, "The thread through all five",
      "AI gives you something fluent and roughly-right, fast — then asks you to decide when roughly-right is good enough, and who checks when it isn't.",
      "A leadership question. Which is why it lands on your desk.")
feature(26, "Your project · RetailFlow", "You're the delivery lead.",
        "The board funded one AI initiative. Ship it without the predictable failures. Carry it through three moves — scoping and stress-testing it by interviewing the RetailFlow team: live chatbots with opinions, who disagree, and won't do your job for you.   access code: pilot2024")
steps(27, "Three moves, one project", "Scope. Verify. Decide.",
      [("01", "Scope it against reality", "Interview Data & CIO. Reconcile \"move fast\" with \"the data isn't ready.\" → objectives, data needs, a defined \"good enough.\""),
       ("02", "Stakeholders & human-in-the-loop", "Interview MD, frontline, CFO. Decide where a human must stay in charge. → stakeholder plan + checkpoint design."),
       ("03", "Roadmap & the go/no-go", "Build the roadmap with gates and a risk register. Then make the call: Scale, Pivot, or Kill.")])
brk(28, "break-lunch.jpg", "12:30", "Lunch", "Back at 1:15")
concept(29, "The go / no-go call", "Scale. Pivot. Kill.",
        "At each gate the question isn't \"is it perfect?\" — it's whether the evidence justifies continuing. Killing early is success, not failure.",
        "scale-pivot-kill.jpg")
brk(30, "break-afternoon-tea.jpg", "2:30", "Afternoon tea", "Back at 3:00")
grid(31, "What you've built by 4:00", "A delivery design, not a theory.", None,
     [("SCOPE", "Objectives, data requirements, a defined \"good enough.\""),
      ("ROADMAP", "Milestones and go/no-go gates."),
      ("CHECKPOINTS", "A stakeholder plan and human-in-the-loop design."),
      ("RISK", "A register and a Scale / Pivot / Kill call you can defend.")])
concept(32, "Back to the provocation", "The edge is the part the tool can't average.",
        "Averages converge. Your taste, your contrarian calls, your specific customers — that's the variation a rival's identical model can't reproduce.",
        "where-your-edge-lives.jpg")
grid(33, "What you do next", "Your action plan.", None,
     [("WEEK", "Trial your redesigned workflow. Run one task through the trust tool first."),
      ("MONTH", "Make RTCF a habit. Start one conversation about where a human stays in the loop."),
      ("QUARTER", "Scope one real initiative — and defend the Scale / Pivot / Kill call.")],
     cols=3)
grid(34, "What you leave with", "Tools that don't expire.", None,
     [("DECISION TOOLS", "The trust tool, RTCF, the five differences, Scale / Pivot / Kill — any platform, any model."),
      ("YOUR WORK", "A redesigned workflow and a scoped project design you can act on."),
      ("A PLAN", "Specific commitments for the week, month and quarter."),
      ("GO DEEPER", "michael-borck.github.io/the-human-edge — incl. the two-page voice method.")])
close_deck()

OUT.parent.mkdir(parents=True, exist_ok=True)
prs.save(OUT)
print(f">> wrote {OUT.relative_to(ROOT)}  ({len(prs.slides.__iter__.__self__._sldIdLst)} slides)")
