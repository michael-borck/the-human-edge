/* AI for professionals: deck engine
   Keys: → / Space / PageDown next · ← / PageUp back · 1-4 jump to session
         N presenter window · T start/pause exercise timer · R reset timer
         B blank screen · F fullscreen · Home / End
   URL:  #12 opens slide 12 · ?print lays out every slide for PDF export */
(function () {
  const CH = [
    { label: 'JUDGE',    time: '9:00',  acc: '#E8B54D' },
    { label: 'BRIEF',    time: '11:00', acc: '#4FC9A8' },
    { label: 'CHECK',    time: '1:15',  acc: '#E5745A' },
    { label: 'REDESIGN', time: '3:00',  acc: '#7FA8F0' },
  ];
  const $ = (q, el = document) => el.querySelector(q);
  const slides = [...document.querySelectorAll('.slide')];
  const chOf = sl => +(sl.dataset.ch || 0);
  const chStart = CH.map((_, c) => slides.findIndex(sl => chOf(sl) === c));

  function stepsOf(sl) {
    if (sl.dataset.steps !== undefined) return +sl.dataset.steps;
    const els = [...sl.querySelectorAll('[data-s]')];
    return els.length ? Math.max(...els.map(e => +e.dataset.s)) : 0;
  }
  const minOf = sl => (sl.dataset.mode === 'spot' ? 1 : 0);
  const titleOf = sl => sl.dataset.title || ($('.t', sl) ? $('.t', sl).textContent.trim() : '');

  function apply(sl, step, all) {
    sl.dataset.cur = step;
    sl.querySelectorAll('[data-s]').forEach(e => {
      const n = +e.dataset.s;
      if (sl.dataset.mode === 'spot') {
        e.classList.toggle('lit', all || n === step);
        e.classList.toggle('dimd', !all && n !== step);
      } else {
        e.classList.toggle('on', all || n <= step);
      }
    });
  }

  /* ---------- print mode ---------- */
  if (new URLSearchParams(location.search).has('print')) {
    document.body.classList.add('print');
    slides.forEach(sl => {
      sl.style.setProperty('--acc', CH[chOf(sl)].acc);
      const ps = sl.dataset.printStep;
      apply(sl, ps !== undefined ? +ps : stepsOf(sl), ps === undefined);
    });
    return;
  }

  /* ---------- chrome ---------- */
  const nav = $('#nav');
  CH.forEach((c, n) => {
    const d = document.createElement('div');
    d.className = 'nv';
    d.innerHTML = `<span class="bar"></span><span class="lb">0${n + 1} ${c.label}<span class="tm">${c.time}</span></span>`;
    nav.appendChild(d);
  });
  const nvs = [...nav.children];
  $('#ct').textContent = slides.length;

  let i = 0, s = 0;
  const h = parseInt(location.hash.slice(1), 10);
  if (h >= 1 && h <= slides.length) i = h - 1;
  s = minOf(slides[i]);

  function render() {
    const sl = slides[i], ci = chOf(sl);
    document.documentElement.style.setProperty('--acc', CH[ci].acc);
    slides.forEach((x, n) => x.classList.toggle('cur', n === i));
    nvs.forEach((n, x) => { n.classList.toggle('cur', x === ci); n.classList.toggle('done', x < ci); });
    $('#cn').textContent = i + 1;
    apply(sl, s);
    history.replaceState(null, '', '#' + (i + 1));
    showTimer();
    updatePresenter();
  }
  function go(dir) {
    const sl = slides[i];
    if (dir > 0) {
      if (s < stepsOf(sl)) s++;
      else if (i < slides.length - 1) { i++; s = minOf(slides[i]); }
    } else {
      if (s > minOf(sl)) s--;
      else if (i > 0) { i--; s = stepsOf(slides[i]); }
    }
    render();
  }
  function jump(n) { if (n >= 0 && n < slides.length) { i = n; s = minOf(slides[i]); render(); } }

  /* ---------- exercise timer ---------- */
  const tEl = $('#timer');
  const tm = { slide: -1, left: 0, run: false, last: 0 };
  const fmt = sec => {
    const a = Math.abs(Math.round(sec)), m = Math.floor(a / 60), r = a % 60;
    return (sec < 0 ? '+' : '') + m + ':' + String(r).padStart(2, '0');
  };
  function showTimer() {
    const vis = tm.slide === i || tm.run;
    tEl.classList.toggle('show', vis);
    tEl.classList.toggle('paused', vis && !tm.run);
    tEl.classList.toggle('over', tm.left < 0);
    tEl.textContent = fmt(tm.left);
  }
  function toggleTimer() {
    const mins = +slides[i].dataset.min || 0;
    if (tm.slide !== i) {
      if (!mins) return;
      Object.assign(tm, { slide: i, left: mins * 60, run: true, last: Date.now() });
    } else { tm.run = !tm.run; tm.last = Date.now(); }
    showTimer();
  }
  function resetTimer() { Object.assign(tm, { slide: -1, left: 0, run: false }); showTimer(); }
  setInterval(() => {
    if (tm.run) { const now = Date.now(); tm.left -= (now - tm.last) / 1000; tm.last = now; showTimer(); }
    tickPresenter();
  }, 250);

  /* ---------- presenter window ---------- */
  let pw = null, t0 = Date.now();
  const PRESENTER = `<!doctype html><html><head><meta charset="utf-8"><title>Presenter</title><style>
    body{margin:0;background:#0A0C10;color:#ECE7DB;font:16px/1.5 'Funnel Sans',system-ui,sans-serif;display:flex;flex-direction:column;height:100vh}
    header{display:flex;gap:28px;align-items:baseline;padding:16px 24px;border-bottom:1px solid rgba(236,231,219,.15);font-family:ui-monospace,monospace;font-size:13px;letter-spacing:.1em;color:rgba(236,231,219,.6)}
    header b{color:#E8B54D;font-size:22px}
    #ttl{font:600 26px/1.25 Georgia,serif;padding:18px 24px 4px}
    #step{padding:0 24px;font-family:ui-monospace,monospace;font-size:12px;letter-spacing:.12em;color:rgba(236,231,219,.5)}
    #notes{flex:1;overflow:auto;padding:12px 24px 24px;font-size:19px}
    #notes ul{padding-left:22px}#notes li{margin:6px 0}#notes p{margin:8px 0}
    #notes .none{color:rgba(236,231,219,.4)}
    footer{padding:12px 24px;border-top:1px solid rgba(236,231,219,.15);color:rgba(236,231,219,.6);font-size:15px}
    .grow{flex:1}#ex.over{color:#E5745A}button{background:none;border:1px solid rgba(236,231,219,.3);color:inherit;border-radius:6px;padding:2px 10px;cursor:pointer;font:inherit}
  </style></head><body>
  <header><span><b id="pn"></b> / <span id="pt"></span></span><span id="pch"></span><span class="grow"></span>
  <span>ELAPSED <b id="el">0:00</b> <button id="rs">reset</button></span><span>EXERCISE <b id="ex">-</b></span><span>CLOCK <b id="ck"></b></span></header>
  <div id="ttl"></div><div id="step"></div><div id="notes"></div>
  <footer>NEXT &nbsp; <span id="nx"></span></footer></body></html>`;

  function openPresenter() {
    pw = window.open('', 'ai-presenter', 'width=1000,height=720');
    if (!pw) return;
    pw.document.open(); pw.document.write(PRESENTER); pw.document.close();
    pw.document.addEventListener('keydown', onKey);
    pw.document.getElementById('rs').onclick = () => { t0 = Date.now(); };
    t0 = Date.now();
    updatePresenter();
  }
  function updatePresenter() {
    if (!pw || pw.closed) return;
    const d = pw.document, sl = slides[i], nx = slides[i + 1];
    d.getElementById('pn').textContent = i + 1;
    d.getElementById('pt').textContent = slides.length;
    d.getElementById('pch').textContent = `SESSION 0${chOf(sl) + 1} · ${CH[chOf(sl)].label}`;
    d.getElementById('ttl').textContent = titleOf(sl);
    const st = stepsOf(sl);
    d.getElementById('step').textContent = st ? `STEP ${s} OF ${st}` : '';
    const n = $('aside.notes', sl);
    d.getElementById('notes').innerHTML = n ? n.innerHTML : '<p class="none">No notes for this slide.</p>';
    d.getElementById('nx').textContent = nx ? titleOf(nx) : 'End of deck';
    tickPresenter();
  }
  function tickPresenter() {
    if (!pw || pw.closed) return;
    const d = pw.document;
    d.getElementById('el').textContent = fmt((Date.now() - t0) / 1000);
    d.getElementById('ck').textContent = new Date().toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
    const ex = d.getElementById('ex');
    ex.textContent = tm.slide >= 0 ? fmt(tm.left) + (tm.run ? '' : ' ‖') : '-';
    ex.className = tm.left < 0 ? 'over' : '';
  }

  /* ---------- input ---------- */
  function onKey(e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    if (['ArrowRight', 'PageDown', ' ', 'ArrowDown'].includes(k)) { e.preventDefault(); go(1); }
    else if (['ArrowLeft', 'PageUp', 'ArrowUp'].includes(k)) { e.preventDefault(); go(-1); }
    else if (k === 'Home') jump(0);
    else if (k === 'End') jump(slides.length - 1);
    else if (/^[1-4]$/.test(k)) jump(chStart[+k - 1]);
    else if (k === 'n' || k === 'N') openPresenter();
    else if (k === 't' || k === 'T') toggleTimer();
    else if (k === 'r' || k === 'R') resetTimer();
    else if (k === 'b' || k === 'B' || k === '.') $('#blank').classList.toggle('on');
    else if (k === 'f' || k === 'F') {
      if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen();
    }
  }
  addEventListener('keydown', onKey);
  let tx = null;
  addEventListener('touchstart', e => { tx = e.touches[0].clientX; }, { passive: true });
  addEventListener('touchend', e => {
    if (tx === null) return;
    const dx = e.changedTouches[0].clientX - tx;
    if (Math.abs(dx) > 50) go(dx < 0 ? 1 : -1);
    tx = null;
  });

  function fit() {
    const k = Math.min(innerWidth / 1280, innerHeight / 720);
    $('#stage').style.transform = `scale(${k})`;
  }
  addEventListener('resize', fit);
  fit();
  render();
})();
