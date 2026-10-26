#!/usr/bin/env python3
"""Render content/slide-deck.md into docs/deck.html: a dark, cinematic HTML deck.

Own engine (fixed 1280x720 stage, staged reveals, keyboard/click nav).
Parse rules: '---' separates slides; '# Title' is the slide title; '~~~' fenced
blocks render as mono figures; '::: {.notes}' blocks are skipped (presenter uses
the pptx for notes). The 'The Trust Tool' slide gets an animated quadrant figure.
"""
import html
import re
import sys

SRC = "content/slide-deck.md"
OUT = "docs/deck.html"

def parse_slides(md):
    # strip notes blocks
    md = re.sub(r'::: \{\.notes\}.*?:::', '', md, flags=re.S)
    # strip front matter
    md = re.sub(r'\A---\n.*?\n---\n', '', md, flags=re.S)
    chunks = [c.strip() for c in re.split(r'\n---\n', md) if c.strip()]
    slides = []
    for c in chunks:
        m = re.match(r'#\s+(.+)', c)
        if not m:
            continue
        title = m.group(1).strip()
        body = c[m.end():].strip()
        blocks = []  # (kind, payload)
        # fenced mono figures
        def fence_sub(mo):
            blocks.append(("pre", mo.group(1).rstrip()))
            return ""
        body = re.sub(r'```\n(.*?)```', fence_sub, body, flags=re.S)
        # split remaining into lines, group bullets
        lines = body.splitlines()
        i = 0
        buf_bullets = []
        def flush():
            if buf_bullets:
                blocks.append(("ul", list(buf_bullets)))
                buf_bullets.clear()
        while i < len(lines):
            ln = lines[i].rstrip()
            if not ln.strip():
                i += 1; continue
            if re.match(r'^-\s+', ln) or re.match(r'^\d+\.\s+', ln):
                while i < len(lines) and (re.match(r'^-\s+', lines[i]) or re.match(r'^\d+\.\s+', lines[i]) or (lines[i].startswith('  ') and lines[i].strip() and buf_bullets)):
                    ln2 = lines[i].rstrip()
                    ln2 = re.sub(r'^-\s+', '', ln2)
                    ln2 = re.sub(r'^\d+\.\s+', '', ln2)
                    if ln2.strip():
                        buf_bullets.append(ln2.strip())
                    i += 1
                flush()
                continue
            if ln.startswith('|'):
                tbl = []
                while i < len(lines) and lines[i].strip().startswith('|'):
                    row = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                    if not all(re.match(r'^:?-+:?$', cell) for cell in row):
                        tbl.append(row)
                    i += 1
                if tbl:
                    blocks.append(("table", tbl))
                continue
            # paragraph (possibly multi-line until blank)
            para = [ln]
            i += 1
            while i < len(lines) and lines[i].strip() and not re.match(r'^(-\s|\d+\.\s|\||#|```)', lines[i]):
                para.append(lines[i].rstrip()); i += 1
            blocks.append(("p", " ".join(para)))
        slides.append({"title": title, "blocks": blocks})
    return slides

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s

def render_blocks(blocks):
    out = []
    for kind, payload in blocks:
        if kind == "ul":
            items = "".join(f'<li class="st">{inline(x)}</li>' for x in payload)
            out.append(f'<ul class="decklist">{items}</ul>')
        elif kind == "p":
            cls = "big st" if payload.strip().startswith("**") else "st"
            out.append(f'<p class="{cls}">{inline(payload)}</p>')
        elif kind == "pre":
            out.append(f'<pre class="st fig-pre">{html.escape(payload)}</pre>')
        elif kind == "table":
            head = payload[0]
            th = "".join(f'<th>{inline(c)}</th>' for c in head)
            rows = "".join("<tr class='st'>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in payload[1:])
            out.append(f'<table class="decktable st"><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table>')
    return "\n".join(out)

TRUST_FIGURE = '''
<div class="ttgrid st">
  <div class="ttq g"><div class="qdot"></div><div class="qsub">average + small</div><div class="qname">Trust with light review</div><div class="qex">drafts, summaries, polish</div></div>
  <div class="ttq a"><div class="qdot"></div><div class="qsub">average + large</div><div class="qname">Verify the load-bearing bits</div><div class="qex">a strategic memo</div></div>
  <div class="ttq a"><div class="qdot"></div><div class="qsub">precise + small</div><div class="qname">Verify before you ship</div><div class="qex">a citation, a calculation</div></div>
  <div class="ttq r"><div class="qdot"></div><div class="qsub">precise + large</div><div class="qname">Human in the loop</div><div class="qex">money, people, safety</div></div>
</div>
<p class="st tcap">Lean in where about-right over low stakes is fine. Keep a human where exactly-right meets high stakes.</p>
'''

slides = parse_slides(open(SRC).read())

TITLE_SLIDE = '''
<section class="slide title-slide" data-i="0">
  <div class="k"><span class="kdash"></span>executive education &middot; curtin business school</div>
  <h1 class="t" style="font-size:58px;max-width:1000px;">Practical AI<br>for Professionals</h1>
  <p class="st" style="font-size:22px;color:var(--dim);">The judgement edge: briefing AI well, knowing what to trust, and keeping your thinking in charge.</p>
  <p class="st" style="font-size:16px;color:var(--muted);margin-top:26px;">Dr Michael Borck &middot; one-day masterclass &middot; bring your laptop</p>
</section>'''

parts = [TITLE_SLIDE]
for idx, s in enumerate(slides, 1):
    title = s["title"]
    if title == "The Trust Tool":
        inner = TRUST_FIGURE
    else:
        inner = render_blocks(s["blocks"])
    kicker = f"{idx:02d} / {len(slides):02d}"
    parts.append(f'''
<section class="slide" data-i="{idx}">
  <div class="k"><span class="kdash"></span>{html.escape(kicker)}</div>
  <h1 class="t">{inline(title)}</h1>
  <div class="content">{inner}</div>
</section>''')

CSS = '''
:root{--bg:#0b0e13;--ink:#eae5d9;--dim:#b3ad9f;--faint:rgba(234,229,217,.32);--hair:rgba(234,229,217,.14);
--card:#10141b;--gold:#d9a441;--green:#7fb069;--red:#c96f5e;--serif:'Domine',Georgia,serif;
--sans:'Funnel Sans',-apple-system,sans-serif;--mono:'Nanum Gothic Coding',monospace}
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%;background:var(--bg);overflow:hidden}
body{font-family:var(--sans);color:var(--ink)}
#viewport{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
#stage{position:relative;width:1280px;height:720px;background:var(--bg);overflow:hidden;transform-origin:center}
#stage::after{content:"";position:absolute;inset:0;z-index:4;pointer-events:none;
background:radial-gradient(ellipse 95% 85% at 50% 42%,transparent 58%,rgba(0,0,0,.45))}
#halo{position:absolute;left:240px;top:180px;width:940px;height:520px;z-index:1;
background:radial-gradient(closest-side,rgba(217,164,65,.07),transparent 72%)}
#counter{position:absolute;top:30px;right:44px;z-index:6;font-family:var(--mono);font-size:12px;
letter-spacing:.16em;color:var(--faint)}
#counter b{color:var(--gold)}
#bar{position:absolute;bottom:0;left:0;height:2px;background:var(--gold);z-index:6;transition:width .4s;box-shadow:0 0 10px rgba(217,164,65,.5)}
.slide{position:absolute;inset:0;opacity:0;pointer-events:none;transition:opacity .5s ease;z-index:2;padding:70px 90px 60px}
.slide.cur{opacity:1;pointer-events:auto}
.k{font-family:var(--mono);font-size:12px;letter-spacing:.2em;color:var(--gold);text-transform:uppercase;
display:flex;align-items:center;gap:13px;margin-bottom:18px}
.kdash{width:28px;height:2px;background:var(--gold);display:inline-block}
.t{font-family:var(--serif);font-weight:500;font-size:44px;line-height:1.15;color:var(--ink);max-width:1050px;margin-bottom:30px}
.content{max-width:1060px}
.big{font-size:23px;line-height:1.5;color:var(--ink);margin:14px 0}
.big strong{color:var(--gold)}
p{font-size:19px;line-height:1.6;color:var(--dim);margin:12px 0}
p strong{color:var(--ink)}
.decklist{list-style:none;margin:10px 0}
.decklist li{font-size:19.5px;line-height:1.5;color:var(--dim);padding:9px 0 9px 30px;position:relative}
.decklist li::before{content:"";position:absolute;left:2px;top:20px;width:14px;height:2px;background:var(--gold)}
.decklist li strong{color:var(--ink)}
.decktable{width:100%;border-collapse:collapse;margin:18px 0;font-size:16.5px}
.decktable th{text-align:left;font-family:var(--mono);font-size:11.5px;letter-spacing:.12em;text-transform:uppercase;
color:var(--faint);font-weight:400;padding:10px 14px;border-bottom:1px solid var(--hair)}
.decktable td{padding:12px 14px;border-bottom:1px solid var(--hair);color:var(--dim);line-height:1.5}
.decktable td:first-child{color:var(--ink)}
.decktable strong{color:var(--ink)}
.fig-pre{font-family:var(--mono);font-size:14px;line-height:1.5;color:var(--dim);background:var(--card);
border:1px solid var(--hair);border-radius:10px;padding:20px 24px;white-space:pre;overflow:hidden}
/* trust tool figure */
.ttgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:8px 0 4px;max-width:900px}
.ttq{border:1px solid var(--hair);background:var(--card);border-radius:12px;padding:16px 18px;min-height:104px;
transition:all .5s ease;position:relative}
.ttq .qdot{width:9px;height:9px;border-radius:50%;margin-bottom:8px;opacity:0;transition:opacity .5s}
.ttq.g .qdot{background:var(--green);box-shadow:0 0 12px rgba(127,176,105,.7)}
.ttq.a .qdot{background:var(--gold);box-shadow:0 0 12px rgba(217,164,65,.7)}
.ttq.r .qdot{background:var(--red);box-shadow:0 0 12px rgba(201,111,94,.7)}
.ttq .qsub{font-family:var(--mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);display:block;margin-bottom:5px}
.ttq .qname{font-family:var(--serif);font-size:19px;color:var(--ink);display:block}
.ttq .qex{font-size:13.5px;color:var(--faint);display:block;margin-top:5px}
.slide.lit-all .ttq{border-color:rgba(217,164,65,.35)}
.slide.lit-all .ttq .qdot{opacity:1}
.slide.lit-all .ttq.g{box-shadow:0 0 26px rgba(127,176,105,.08) inset}
.slide.lit-all .ttq.a{box-shadow:0 0 26px rgba(217,164,65,.08) inset}
.slide.lit-all .ttq.r{box-shadow:0 0 26px rgba(201,111,94,.10) inset}
.tcap{font-size:17px;color:var(--dim);font-style:italic}
/* staged reveals */
.st{opacity:0;transform:translateY(10px);transition:opacity .45s ease,transform .45s ease}
.st.on{opacity:1;transform:none}
.slide.fig-slide .st.on .qdot{opacity:1}
#hint{position:absolute;bottom:22px;right:44px;z-index:6;font-family:var(--mono);font-size:10.5px;
letter-spacing:.14em;color:var(--faint)}
'''

JS = '''
const slides=[...document.querySelectorAll('.slide')];let i=0;
const counter=document.getElementById('cn'),bar=document.getElementById('bar');
function stages(sl){return sl?sl.querySelectorAll('.st'):[],sl?[...sl.querySelectorAll('.st')]:[]}
function render(){
 slides.forEach((s,k)=>s.classList.toggle('cur',k===i));
 const sl=slides[i],st=stages(sl);
 const revealed=st.filter(x=>x.classList.contains('on')).length;
 document.getElementById('cn').textContent=i+1;
 bar.style.width=((i+ (st.length? revealed/st.length:1))/slides.length*100)+'%';
 const tt=sl&&sl.querySelector('.ttgrid');
 if(tt) sl.classList.toggle('lit-all', revealed>=st.length);
 document.getElementById('hint').textContent = (revealed<st.length)?'space / \u2192 to reveal':'space / \u2192 next';
}
function next(){const st=stages(slides[i]);const hid=st.find(x=>!x.classList.contains('on'));
 if(hid){hid.classList.add('on');render();}else if(i<slides.length-1){i++;render();}}
function prev(){const st=stages(slides[i]);const shown=[...st].reverse().find(x=>x.classList.contains('on'));
 if(shown){shown.classList.remove('on');render();}else if(i>0){i--;[...stages(slides[i])].forEach(x=>x.classList.add('on'));render();}}
document.addEventListener('keydown',e=>{
 if(['ArrowRight','ArrowDown',' ','PageDown'].includes(e.key)){e.preventDefault();next();}
 if(['ArrowLeft','ArrowUp','PageUp'].includes(e.key)){e.preventDefault();prev();}
 if(e.key==='Home'){i=0;render();} if(e.key==='End'){i=slides.length-1;[...stages(slides[i])].forEach(x=>x.classList.add('on'));render();}
});
document.addEventListener('click',e=>{if(!e.target.closest('a'))next();});
function fit(){const s=Math.min(innerWidth/1280,innerHeight/720);document.getElementById('stage').style.transform=`scale(${s})`;}
addEventListener('resize',fit);fit();render();
'''

html_out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Practical AI for Professionals | the deck</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Domine:wght@400..700&family=Funnel+Sans:ital,wght@0,300..800;1,300..800&family=Nanum+Gothic+Coding:wght@400;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<div id="viewport"><div id="stage">
<div id="halo"></div>
<div id="counter"><b id="cn">1</b>/{len(slides)+1}</div>
<div id="bar"></div>
<div id="hint"></div>
{"".join(parts)}
</div></div>
<script>{JS}</script>
</body>
</html>'''

open(OUT, "w").write(html_out)
print(f"docs/deck.html: {len(slides)} slides, {len(html_out)//1024} KB")
