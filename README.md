<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Portfólio Acadêmico — Lucas Viana de Freitas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&family=Fraunces:ital,wght@0,300;0,700;1,300&display=swap" rel="stylesheet">
<style>
/* ─── TOKENS ──────────────────────────────────────────────── */
:root {
  --bg:       #080c14;
  --surface:  #0e1520;
  --panel:    #131b2b;
  --border:   rgba(255,255,255,0.07);
  --border-hi:rgba(255,255,255,0.14);

  --ink:      #e8edf5;
  --ink-2:    #8a97b0;
  --ink-3:    #4a5568;

  --accent:   #3a7dff;
  --accent-2: #6fa3ff;
  --glow:     rgba(58,125,255,0.18);

  --green:    #22c55e;
  --amber:    #f59e0b;
  --red:      #ef4444;

  --r-sm:  8px;
  --r-md:  14px;
  --r-lg:  22px;
  --r-xl:  32px;

  --mono: 'DM Mono', monospace;
  --sans: 'DM Sans', sans-serif;
  --serif: 'Fraunces', serif;

  --ease: cubic-bezier(.22,.68,0,1.2);
}

/* ─── RESET ───────────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: var(--sans);
  font-size: 15px;
  line-height: 1.65;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}
a { color: var(--accent-2); text-decoration: none; }
a:hover { text-decoration: underline; }
button { font-family: inherit; }

/* ─── SCROLLBAR ───────────────────────────────────────────── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--surface); }
::-webkit-scrollbar-thumb { background: var(--panel); border-radius: 99px; }

/* ─── NOISE OVERLAY ───────────────────────────────────────── */
body::before {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.03'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 0;
  opacity: .4;
}

/* ─── HERO ────────────────────────────────────────────────── */
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  padding: clamp(60px,10vw,120px) clamp(24px,8vw,120px);
  overflow: hidden;
}

/* radial ambient lights */
.hero::before, .hero::after {
  content: '';
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(80px);
  opacity: .35;
}
.hero::before {
  width: 600px; height: 600px;
  background: radial-gradient(circle, #1e40af 0%, transparent 70%);
  top: -200px; right: -100px;
}
.hero::after {
  width: 400px; height: 400px;
  background: radial-gradient(circle, #0f4c81 0%, transparent 70%);
  bottom: -100px; left: 40%;
}

.hero-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--accent-2);
  letter-spacing: .12em;
  text-transform: uppercase;
  margin-bottom: 28px;
}
.hero-eyebrow::before {
  content: '';
  display: block;
  width: 28px; height: 1px;
  background: var(--accent-2);
}

.hero h1 {
  font-family: var(--serif);
  font-weight: 700;
  font-size: clamp(2.8rem, 7vw, 6.5rem);
  line-height: 1.05;
  letter-spacing: -.02em;
  max-width: 820px;
  margin-bottom: 24px;
  position: relative;
  z-index: 1;
}
.hero h1 em {
  font-style: italic;
  font-weight: 300;
  color: var(--accent-2);
}

.hero-sub {
  font-size: 1.05rem;
  color: var(--ink-2);
  max-width: 520px;
  margin-bottom: 48px;
  position: relative;
  z-index: 1;
}

.hero-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  position: relative;
  z-index: 1;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 7px 14px;
  border-radius: 99px;
  font-size: .78rem;
  font-family: var(--mono);
  border: 1px solid var(--border-hi);
  background: rgba(255,255,255,0.04);
  color: var(--ink-2);
}
.badge .dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: var(--green);
  animation: pulse 2s infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.4; }
}

.scroll-hint {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  color: var(--ink-3);
  font-size: .72rem;
  font-family: var(--mono);
  letter-spacing: .1em;
  text-transform: uppercase;
  z-index: 2;
}
.scroll-hint svg {
  animation: scrollBounce 1.8s ease-in-out infinite;
}
@keyframes scrollBounce {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(6px); }
}

/* ─── NAV ─────────────────────────────────────────────────── */
.nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(8,12,20,0.8);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border);
  padding: 0 clamp(24px,8vw,120px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 56px;
}

.nav-brand {
  font-family: var(--mono);
  font-size: .78rem;
  color: var(--ink-2);
  letter-spacing: .06em;
}
.nav-brand span { color: var(--accent-2); }

.nav-links {
  display: flex;
  gap: 2px;
}
.nav-links a {
  color: var(--ink-2);
  font-size: .82rem;
  padding: 6px 14px;
  border-radius: var(--r-sm);
  transition: color .2s, background .2s;
}
.nav-links a:hover {
  color: var(--ink);
  background: rgba(255,255,255,0.06);
  text-decoration: none;
}

/* ─── LAYOUT ──────────────────────────────────────────────── */
.wrap {
  max-width: 1360px;
  margin: 0 auto;
  padding: 0 clamp(24px,8vw,120px);
}

section { padding: 100px 0; }

.section-label {
  display: flex;
  align-items: center;
  gap: 12px;
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--ink-3);
  letter-spacing: .14em;
  text-transform: uppercase;
  margin-bottom: 48px;
}
.section-label::after {
  content: '';
  flex: 1;
  height: 1px;
  background: var(--border);
}

.section-title {
  font-family: var(--serif);
  font-weight: 700;
  font-size: clamp(1.9rem, 4vw, 3rem);
  line-height: 1.15;
  letter-spacing: -.02em;
  margin-bottom: 16px;
}
.section-title em {
  font-style: italic;
  font-weight: 300;
  color: var(--accent-2);
}

/* ─── STATS BAR ───────────────────────────────────────────── */
.stats-bar {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px,1fr));
  gap: 1px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: var(--r-lg);
  overflow: hidden;
  margin-bottom: 80px;
}
.stat {
  background: var(--surface);
  padding: 28px 24px;
  text-align: center;
}
.stat-num {
  font-family: var(--serif);
  font-weight: 700;
  font-size: 2.4rem;
  color: var(--accent-2);
  line-height: 1;
  margin-bottom: 6px;
}
.stat-label {
  font-size: .75rem;
  color: var(--ink-3);
  font-family: var(--mono);
  text-transform: uppercase;
  letter-spacing: .08em;
}

/* ─── PROFILE CARD ────────────────────────────────────────── */
.profile-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px;
  background: var(--border);
  border: 1px solid var(--border);
  border-radius: var(--r-lg);
  overflow: hidden;
}
.profile-cell {
  background: var(--surface);
  padding: 32px;
}
.profile-cell.span2 { grid-column: span 2; }
.profile-kv {
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.profile-kv small {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: .1em;
}
.profile-kv strong {
  font-size: .95rem;
  color: var(--ink);
  font-weight: 500;
}
.profile-cell h3 {
  font-family: var(--serif);
  font-weight: 700;
  font-size: 1.6rem;
  margin-bottom: 6px;
}
.profile-cell p { color: var(--ink-2); font-size: .88rem; }

/* ─── TIMELINE ────────────────────────────────────────────── */
.timeline {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.tl-line {
  position: absolute;
  left: 31px;
  top: 0; bottom: 0;
  width: 1px;
  background: var(--border);
  pointer-events: none;
}

.tl-item {
  position: relative;
  display: grid;
  grid-template-columns: 64px 1fr;
  gap: 0 24px;
  padding-bottom: 12px;
}

.tl-dot-wrap {
  position: relative;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  padding-top: 22px;
  z-index: 1;
}
.tl-dot {
  width: 14px; height: 14px;
  border-radius: 50%;
  border: 2px solid var(--surface);
  background: var(--border-hi);
  flex-shrink: 0;
  transition: background .2s, box-shadow .2s;
}
.tl-item:hover .tl-dot {
  background: var(--accent);
  box-shadow: 0 0 0 4px var(--glow);
}
.tl-item.has-file .tl-dot { background: var(--accent); }

.tl-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  padding: 20px 22px;
  transition: border-color .2s, transform .25s var(--ease), box-shadow .25s;
  cursor: default;
  margin-bottom: 12px;
}
.tl-card:hover {
  border-color: var(--border-hi);
  transform: translateX(4px);
  box-shadow: 0 8px 32px rgba(0,0,0,.3);
}

.tl-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 8px;
}

.tl-num {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--accent-2);
  letter-spacing: .08em;
  flex-shrink: 0;
  margin-top: 2px;
}

.tl-title {
  font-size: .93rem;
  font-weight: 500;
  color: var(--ink);
  flex: 1;
  line-height: 1.45;
}

.tl-date {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--ink-3);
  flex-shrink: 0;
  white-space: nowrap;
}

.tl-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 10px;
}
.tag {
  font-family: var(--mono);
  font-size: .65rem;
  padding: 3px 9px;
  border-radius: 99px;
  background: rgba(58,125,255,0.1);
  color: var(--accent-2);
  border: 1px solid rgba(58,125,255,0.2);
}
.tag.green {
  background: rgba(34,197,94,0.1);
  color: var(--green);
  border-color: rgba(34,197,94,0.2);
}
.tag.amber {
  background: rgba(245,158,11,0.1);
  color: var(--amber);
  border-color: rgba(245,158,11,0.2);
}

.tl-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 14px;
  padding: 8px 16px;
  border-radius: var(--r-sm);
  background: rgba(58,125,255,0.12);
  color: var(--accent-2);
  font-size: .78rem;
  border: 1px solid rgba(58,125,255,0.2);
  cursor: pointer;
  transition: background .2s, border-color .2s;
}
.tl-btn:hover {
  background: rgba(58,125,255,0.22);
  border-color: rgba(58,125,255,0.4);
}
.tl-btn svg { transition: transform .25s var(--ease); }
.tl-btn.open svg { transform: rotate(180deg); }

/* viewer ↓ */
.tl-viewer {
  overflow: hidden;
  max-height: 0;
  transition: max-height .4s ease;
  margin-top: 0;
}
.tl-viewer.open { max-height: 650px; }

.tl-viewer-inner {
  margin-top: 12px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--r-sm);
  overflow: auto;
  max-height: 480px;
  padding: 12px;
}
.tl-viewer-inner img { width: 100%; border-radius: 6px; display: block; }
.tl-viewer-inner iframe { width: 100%; height: 400px; border: none; border-radius: 6px; }
.tl-viewer-inner pre {
  color: var(--accent-2);
  font-family: var(--mono);
  font-size: .75rem;
  white-space: pre-wrap;
  word-break: break-word;
  line-height: 1.7;
}

.file-tabs {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 10px;
}
.file-tab {
  font-family: var(--mono);
  font-size: .72rem;
  padding: 5px 11px;
  border-radius: var(--r-sm);
  background: rgba(255,255,255,0.05);
  color: var(--ink-2);
  border: 1px solid var(--border);
  cursor: pointer;
  transition: .2s;
}
.file-tab:hover, .file-tab.active {
  background: rgba(58,125,255,0.18);
  color: var(--accent-2);
  border-color: rgba(58,125,255,0.3);
}

.no-digital {
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--ink-3);
  margin-top: 8px;
}

.heic-notice {
  background: rgba(245,158,11,0.08);
  border: 1px solid rgba(245,158,11,0.25);
  border-radius: var(--r-sm);
  padding: 12px 14px;
  color: var(--amber);
  font-size: .8rem;
}

/* ─── SKILLS ──────────────────────────────────────────────── */
.skills-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 16px;
}
.skill-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  padding: 28px;
  transition: border-color .2s, box-shadow .2s;
}
.skill-card:hover {
  border-color: var(--border-hi);
  box-shadow: 0 8px 32px rgba(0,0,0,.25);
}
.skill-icon {
  font-size: 1.8rem;
  margin-bottom: 14px;
}
.skill-name {
  font-weight: 600;
  font-size: .92rem;
  margin-bottom: 4px;
}
.skill-desc {
  font-size: .8rem;
  color: var(--ink-2);
  margin-bottom: 16px;
}
.skill-bar-wrap {
  height: 3px;
  background: var(--border);
  border-radius: 99px;
  overflow: hidden;
}
.skill-bar {
  height: 100%;
  border-radius: 99px;
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  transform-origin: left;
  transform: scaleX(0);
  transition: transform .8s var(--ease);
}
.skill-bar.animated { transform: scaleX(1); }

/* ─── TOOLS ───────────────────────────────────────────────── */
.tools-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.tool-chip {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 10px 16px;
  border-radius: var(--r-md);
  background: var(--surface);
  border: 1px solid var(--border);
  font-size: .82rem;
  color: var(--ink-2);
  transition: .2s;
}
.tool-chip:hover {
  border-color: var(--border-hi);
  color: var(--ink);
}
.tool-chip .ic {
  width: 20px; height: 20px;
  border-radius: 4px;
  display: flex; align-items: center; justify-content: center;
  font-size: .8rem;
}

/* ─── PROJECT BLOCK ───────────────────────────────────────── */
.project-hero {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--r-xl);
  padding: clamp(32px,5vw,56px);
  display: grid;
  grid-template-columns: 1fr auto;
  align-items: start;
  gap: 40px;
}

.project-tag {
  font-family: var(--mono);
  font-size: .68rem;
  color: var(--accent-2);
  letter-spacing: .1em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.project-title {
  font-family: var(--serif);
  font-weight: 700;
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  margin-bottom: 14px;
  line-height: 1.2;
}

.project-desc {
  color: var(--ink-2);
  font-size: .9rem;
  max-width: 540px;
  margin-bottom: 28px;
}

.project-links {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 22px;
  border-radius: var(--r-md);
  background: var(--accent);
  color: #fff;
  font-size: .85rem;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background .2s, transform .15s;
  text-decoration: none;
}
.btn-primary:hover {
  background: #2563ff;
  transform: translateY(-1px);
  text-decoration: none;
  color: #fff;
}

.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 11px 22px;
  border-radius: var(--r-md);
  background: transparent;
  color: var(--ink);
  font-size: .85rem;
  border: 1px solid var(--border-hi);
  cursor: pointer;
  transition: .2s;
  text-decoration: none;
}
.btn-secondary:hover {
  background: rgba(255,255,255,0.06);
  text-decoration: none;
  color: var(--ink);
}

.commit-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  border-radius: var(--r-sm);
  background: rgba(34,197,94,0.08);
  border: 1px solid rgba(34,197,94,0.2);
  font-family: var(--mono);
  font-size: .75rem;
  color: var(--green);
  margin-top: 16px;
}
.commit-dot {
  width: 7px; height: 7px;
  border-radius: 50%;
  background: var(--green);
}

.project-aside {
  display: flex;
  flex-direction: column;
  gap: 10px;
  flex-shrink: 0;
}
.aside-stat {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  padding: 20px 24px;
  text-align: center;
  min-width: 140px;
}
.aside-stat-num {
  font-family: var(--serif);
  font-size: 2rem;
  font-weight: 700;
  color: var(--accent-2);
  line-height: 1;
  margin-bottom: 4px;
}
.aside-stat-label {
  font-family: var(--mono);
  font-size: .65rem;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: .08em;
}

/* ─── REFLECTION ──────────────────────────────────────────── */
.reflection-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px,1fr));
  gap: 16px;
}
.reflection-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  padding: 28px;
}
.reflection-q {
  font-family: var(--serif);
  font-style: italic;
  font-weight: 300;
  font-size: 1.05rem;
  color: var(--accent-2);
  margin-bottom: 12px;
  line-height: 1.4;
}
.reflection-a {
  font-size: .85rem;
  color: var(--ink-2);
  line-height: 1.7;
}

/* ─── FOOTER ──────────────────────────────────────────────── */
footer {
  border-top: 1px solid var(--border);
  padding: 40px clamp(24px,8vw,120px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 16px;
  color: var(--ink-3);
  font-size: .78rem;
  font-family: var(--mono);
}
footer a { color: var(--ink-3); }
footer a:hover { color: var(--ink-2); text-decoration: none; }

/* ─── DIVIDER ─────────────────────────────────────────────── */
.divider {
  height: 1px;
  background: var(--border);
  margin: 0;
}

/* ─── RESPONSIVE ──────────────────────────────────────────── */
@media (max-width: 768px) {
  .profile-grid { grid-template-columns: 1fr; }
  .profile-cell.span2 { grid-column: span 1; }
  .project-hero { grid-template-columns: 1fr; }
  .project-aside { flex-direction: row; flex-wrap: wrap; }
  .nav-links { display: none; }
  .tl-item { grid-template-columns: 40px 1fr; }
  .tl-line { left: 19px; }
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}

/* ─── PROGRESS RING ───────────────────────────────────────── */
.progress-section {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 40px;
  align-items: center;
  margin-bottom: 80px;
}
@media (max-width: 640px) {
  .progress-section { grid-template-columns: 1fr; }
}
.ring-wrap {
  display: flex;
  justify-content: center;
}
svg.ring circle {
  fill: none;
  stroke-width: 10;
  stroke-linecap: round;
}
.ring-bg { stroke: var(--border); }
.ring-fg {
  stroke: var(--accent);
  stroke-dasharray: 283;
  stroke-dashoffset: 283;
  transition: stroke-dashoffset 1.2s var(--ease);
}
.ring-center {
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
.ring-wrap { position: relative; }
.ring-num {
  font-family: var(--serif);
  font-weight: 700;
  font-size: 2.2rem;
  color: var(--ink);
  line-height: 1;
}
.ring-sub {
  font-family: var(--mono);
  font-size: .65rem;
  color: var(--ink-3);
  text-transform: uppercase;
  letter-spacing: .08em;
}

.progress-items {
  display: flex;
  flex-direction: column;
  gap: 14px;
}
.progress-row {
  display: grid;
  grid-template-columns: 120px 1fr 36px;
  align-items: center;
  gap: 12px;
}
.progress-label {
  font-size: .8rem;
  color: var(--ink-2);
  font-family: var(--mono);
  white-space: nowrap;
}
.progress-track {
  height: 4px;
  background: var(--border);
  border-radius: 99px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  border-radius: 99px;
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  transform-origin: left;
  transform: scaleX(0);
  transition: transform .8s var(--ease);
}
.progress-fill.animated { transform: scaleX(1); }
.progress-pct {
  font-family: var(--mono);
  font-size: .72rem;
  color: var(--ink-3);
  text-align: right;
}

/* ─── LEARNING PATH ───────────────────────────────────────── */
.path-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
}
.path-card {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: var(--r-md);
  padding: 22px;
  position: relative;
  overflow: hidden;
}
.path-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 3px; height: 100%;
  border-radius: 0 2px 2px 0;
}
.path-card.done::before { background: var(--green); }
.path-card.in-progress::before { background: var(--accent); }
.path-card.upcoming::before { background: var(--ink-3); }

.path-status {
  font-family: var(--mono);
  font-size: .63rem;
  text-transform: uppercase;
  letter-spacing: .1em;
  margin-bottom: 8px;
}
.done .path-status { color: var(--green); }
.in-progress .path-status { color: var(--accent-2); }
.upcoming .path-status { color: var(--ink-3); }

.path-name {
  font-weight: 500;
  font-size: .88rem;
  margin-bottom: 4px;
}
.path-desc {
  font-size: .78rem;
  color: var(--ink-2);
}
</style>
</head>
<body>

<!-- ──────── HERO ──────── -->
<section class="hero">
  <div class="hero-eyebrow">Portfólio Acadêmico · 2026</div>
  <h1>Lucas Viana<br>de <em>Freitas</em></h1>
  <p class="hero-sub">Estudante de Engenharia — Algoritmos &amp; Programação com Python.<br>
  Universidade Federal do Pampa · Alegrete, RS.</p>
  <div class="hero-meta">
    <span class="badge"><span class="dot"></span>Semestre em andamento</span>
    <span class="badge">Matrícula 2610101377</span>
    <span class="badge">Prof. Diego Luis Kreutz</span>
  </div>
  <div class="scroll-hint">
    <span>rolar</span>
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
      <path d="M2 5l5 5 5-5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
  </div>
</section>

<!-- ──────── NAV ──────── -->
<nav class="nav">
  <span class="nav-brand">lvf <span>/ portfolio</span></span>
  <div class="nav-links">
    <a href="#sobre">Sobre</a>
    <a href="#progresso">Progresso</a>
    <a href="#atividades">Atividades</a>
    <a href="#competencias">Competências</a>
    <a href="#projeto">Projeto</a>
    <a href="#reflexao">Reflexão</a>
  </div>
</nav>

<!-- ──────── SOBRE ──────── -->
<section id="sobre">
  <div class="wrap">
    <p class="section-label">01 — Identificação</p>
    <h2 class="section-title">Quem <em>sou eu</em></h2>

    <div class="stats-bar">
      <div class="stat">
        <div class="stat-num">23</div>
        <div class="stat-label">Atividades</div>
      </div>
      <div class="stat">
        <div class="stat-num">19</div>
        <div class="stat-label">Entregues</div>
      </div>
      <div class="stat">
        <div class="stat-num">16</div>
        <div class="stat-label">Semanas</div>
      </div>
      <div class="stat">
        <div class="stat-num">Python</div>
        <div class="stat-label">Linguagem principal</div>
      </div>
      <div class="stat">
        <div class="stat-num">2026</div>
        <div class="stat-label">Semestre</div>
      </div>
    </div>

    <div class="profile-grid">
      <div class="profile-cell span2">
        <h3>Lucas Viana de Freitas</h3>
        <p>Estudante de engenharia no curso de Algoritmos e Programação ministrado pelo Prof. Diego Luis Kreutz. Ao longo deste semestre desenvolvi habilidades em lógica de programação, Python, estruturas de dados, e uso de ferramentas de inteligência artificial como apoio ao aprendizado.</p>
      </div>
      <div class="profile-cell">
        <div class="profile-kv">
          <small>Matrícula</small>
          <strong>2610101377</strong>
        </div>
      </div>
      <div class="profile-cell">
        <div class="profile-kv">
          <small>Disciplina</small>
          <strong>Algoritmos e Programação</strong>
        </div>
      </div>
      <div class="profile-cell">
        <div class="profile-kv">
          <small>Professor</small>
          <strong>Diego Luis Kreutz</strong>
        </div>
      </div>
      <div class="profile-cell">
        <div class="profile-kv">
          <small>Semestre</small>
          <strong>2026/1 — UNIPAMPA Alegrete</strong>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ──────── PROGRESSO ──────── -->
<section id="progresso">
  <div class="wrap">
    <p class="section-label">02 — Avanço</p>
    <h2 class="section-title">Progresso <em>do semestre</em></h2>

    <div class="progress-section">
      <div class="ring-wrap">
        <svg class="ring" width="160" height="160" viewBox="0 0 100 100">
          <circle class="ring-bg" cx="50" cy="50" r="45"/>
          <circle class="ring-fg" id="ring-main" cx="50" cy="50" r="45"
                  transform="rotate(-90 50 50)"/>
        </svg>
        <div class="ring-center">
          <div class="ring-num">83%</div>
          <div class="ring-sub">concluído</div>
        </div>
      </div>
      <div class="progress-items">
        <div class="progress-row">
          <span class="progress-label">Lógica</span>
          <div class="progress-track"><div class="progress-fill" style="--w:.95"></div></div>
          <span class="progress-pct">95%</span>
        </div>
        <div class="progress-row">
          <span class="progress-label">Python</span>
          <div class="progress-track"><div class="progress-fill" style="--w:.85"></div></div>
          <span class="progress-pct">85%</span>
        </div>
        <div class="progress-row">
          <span class="progress-label">Estrut. Dados</span>
          <div class="progress-track"><div class="progress-fill" style="--w:.75"></div></div>
          <span class="progress-pct">75%</span>
        </div>
        <div class="progress-row">
          <span class="progress-label">LLMs / IA</span>
          <div class="progress-track"><div class="progress-fill" style="--w:.80"></div></div>
          <span class="progress-pct">80%</span>
        </div>
        <div class="progress-row">
          <span class="progress-label">GitHub / Web</span>
          <div class="progress-track"><div class="progress-fill" style="--w:.70"></div></div>
          <span class="progress-pct">70%</span>
        </div>
      </div>
    </div>

    <!-- Learning path -->
    <div class="path-grid">
      <div class="path-card done">
        <div class="path-status">✓ Concluído</div>
        <div class="path-name">Lógica de Programação</div>
        <div class="path-desc">Fundamentos, fluxogramas e pseudocódigo</div>
      </div>
      <div class="path-card done">
        <div class="path-status">✓ Concluído</div>
        <div class="path-name">Python Básico</div>
        <div class="path-desc">Variáveis, condicionais, laços e funções</div>
      </div>
      <div class="path-card done">
        <div class="path-status">✓ Concluído</div>
        <div class="path-name">Vetores e Listas</div>
        <div class="path-desc">Arrays, slicing, operações com coleções</div>
      </div>
      <div class="path-card done">
        <div class="path-status">✓ Concluído</div>
        <div class="path-name">LLMs como Ferramenta</div>
        <div class="path-desc">Geração e avaliação de exercícios com IA</div>
      </div>
      <div class="path-card in-progress">
        <div class="path-status">▶ Em andamento</div>
        <div class="path-name">Eng. de Software</div>
        <div class="path-desc">Modularização, projeto final e portfólio</div>
      </div>
      <div class="path-card upcoming">
        <div class="path-status">· Próximo</div>
        <div class="path-name">Projeto Final</div>
        <div class="path-desc">Entrega completa do portfólio — 30/06/2026</div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ──────── ATIVIDADES (TIMELINE) ──────── -->
<section id="atividades">
  <div class="wrap">
    <p class="section-label">03 — Histórico</p>
    <h2 class="section-title">Todas as <em>atividades</em></h2>

    <div class="timeline">
      <div class="tl-line"></div>

      <!-- 01 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_1.png","type":"image","url":"Atividade_1.png"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A01</span>
            <span class="tl-title">Preenchimento do formulário de diagnóstico inicial</span>
            <span class="tl-date">17/03/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Diagnóstico</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg>
            Ver arquivo
          </button>
          <div class="tl-viewer">
            <div class="file-tabs"></div>
            <div class="tl-viewer-inner"></div>
          </div>
        </div>
      </div>

      <!-- 02 -->
      <div class="tl-item"
           data-files='[]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A02</span>
            <span class="tl-title">QUIZ – Lógica de Programação (Preparatório em aula)</span>
            <span class="tl-date">20/03/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Quiz</span>
            <span class="tag amber">Em aula</span>
          </div>
          <p class="no-digital">📋 Realizada presencialmente — sem arquivo digital.</p>
        </div>
      </div>

      <!-- 03 -->
      <div class="tl-item" data-files='[]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A03</span>
            <span class="tl-title">QUIZ – Diagnóstico de Lógica de Programação</span>
            <span class="tl-date">27/03/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Quiz</span>
            <span class="tag amber">Em aula</span>
          </div>
          <p class="no-digital">📋 Realizada presencialmente — sem arquivo digital.</p>
        </div>
      </div>

      <!-- 04 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_4.pdf","type":"pdf","url":"Atividade_4.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A04</span>
            <span class="tl-title">Lista de 15 exercícios: escolher e resolver</span>
            <span class="tl-date">31/03/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Exercícios</span>
            <span class="tag">Lógica</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 05 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_5.pdf","type":"pdf","url":"Atividade_5.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A05</span>
            <span class="tl-title">Lista de 10 Exercícios — Introdução a Algoritmos com Python</span>
            <span class="tl-date">10/04/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Python</span>
            <span class="tag">Algoritmos</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 06 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_6.pdf","type":"pdf","url":"Atividade_6.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A06</span>
            <span class="tl-title">Geração e Avaliação de Exercícios de Algoritmos com LLMs</span>
            <span class="tl-date">10/04/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">LLMs</span>
            <span class="tag">IA</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 07 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_7.jpg","type":"image","url":"Atividade_7.jpg"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A07</span>
            <span class="tl-title">Quiz de Avaliação — Uso de LLMs em Algoritmos</span>
            <span class="tl-date">10/04/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Quiz</span>
            <span class="tag">LLMs</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 08 -->
      <div class="tl-item has-file"
           data-files='[
             {"name":"A8.1.heic","type":"heic","url":"Atividade_8.1.heic"},
             {"name":"A8.2.heic","type":"heic","url":"Atividade_8.2.heic"},
             {"name":"A8.3.heic","type":"heic","url":"Atividade_8.3.heic"},
             {"name":"A8.4.heic","type":"heic","url":"Atividade_8.4.heic"},
             {"name":"A8.5.heic","type":"heic","url":"Atividade_8.5.heic"},
             {"name":"A8.6.heic","type":"heic","url":"Atividade_8.6.heic"}
           ]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A08</span>
            <span class="tl-title">Resolver os 5 exercícios em papel</span>
            <span class="tl-date">21/04/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Manual</span>
            <span class="tag">Algoritmos</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivos (6)
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 09 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_9.pdf","type":"pdf","url":"Atividade_9.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A09</span>
            <span class="tl-title">Resolver exercícios de listas / vetores / arrays em Python</span>
            <span class="tl-date">24/04/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Python</span>
            <span class="tag">Vetores</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 10 -->
      <div class="tl-item has-file"
           data-files='[
             {"name":"A10.1.heic","type":"heic","url":"Atividade_10.1.heic"},
             {"name":"A10.2.heic","type":"heic","url":"Atividade_10.2.heic"}
           ]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A10</span>
            <span class="tl-title">Formulação e Resolução de Problemas com Vetores/Listas</span>
            <span class="tl-date">24/04/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Vetores</span>
            <span class="tag">Listas</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivos (2)
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 11 -->
      <div class="tl-item has-file"
           data-files='[
             {"name":"Atividade_11.py","type":"code","url":"Atividade_11.py"},
             {"name":"Atividade_11a.py","type":"code","url":"Atividade_11a.py"},
             {"name":"Atividade_11b.py","type":"code","url":"Atividade_11b.py"}
           ]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A11</span>
            <span class="tl-title">Gerar versões do código com resultados visuais</span>
            <span class="tl-date">05/05/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Python</span>
            <span class="tag">Código</span>
            <span class="tag">Visualização</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver código (3 arquivos)
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 12 -->
      <div class="tl-item has-file"
           data-files='[
             {"name":"A12.1.png","type":"image","url":"Atividade_12.1.png"},
             {"name":"A12.2.png","type":"image","url":"Atividade_12.2.png"},
             {"name":"A12.3.png","type":"image","url":"Atividade_12.3.png"},
             {"name":"A12.4.png","type":"image","url":"Atividade_12.4.png"}
           ]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A12</span>
            <span class="tl-title">Problemas de outras disciplinas — múltiplas abordagens</span>
            <span class="tl-date">08/05/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Interdisciplinar</span>
            <span class="tag">Engenharia</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver imagens (4)
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 13 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_13.pdf","type":"pdf","url":"Atividade_13.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A13</span>
            <span class="tl-title">Escolher e entregar problema de engenharia</span>
            <span class="tl-date">12/05/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Engenharia</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 14 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_14.pdf","type":"pdf","url":"Atividade_14.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A14</span>
            <span class="tl-title">Entregar outro problema de engenharia</span>
            <span class="tl-date">15/05/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Engenharia</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 15 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_15.pdf","type":"pdf","url":"Atividade_15.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A15</span>
            <span class="tl-title">Escolher e resolver problema de engenharia</span>
            <span class="tl-date">19/05/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Engenharia</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 16 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_16.pdf","type":"pdf","url":"Atividade_16.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A16</span>
            <span class="tl-title">Evolução técnica da solução anterior</span>
            <span class="tl-date">22/05/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Refatoração</span>
            <span class="tag">Engenharia</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 17 -->
      <div class="tl-item" data-files='[]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A17</span>
            <span class="tl-title">Relato sobre entrevistas</span>
            <span class="tl-date">09/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Relato</span>
            <span class="tag amber">Em aula</span>
          </div>
          <p class="no-digital">📋 Realizada presencialmente — sem arquivo digital.</p>
        </div>
      </div>

      <!-- 18 -->
      <div class="tl-item" data-files='[]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A18</span>
            <span class="tl-title">Modularização de Código e LLMs</span>
            <span class="tl-date">09/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Modularização</span>
            <span class="tag">LLMs</span>
            <span class="tag amber">Em aula</span>
          </div>
          <p class="no-digital">📋 Realizada presencialmente — sem arquivo digital.</p>
        </div>
      </div>

      <!-- 19 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_19.pdf","type":"pdf","url":"Atividade_19.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A19</span>
            <span class="tl-title">Avaliar site alegrete.org</span>
            <span class="tl-date">16/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Web</span>
            <span class="tag">Avaliação</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 20 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_20.pdf","type":"pdf","url":"Atividade_20.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A20</span>
            <span class="tl-title">Desenvolvimento com IA — Alegrete.org</span>
            <span class="tl-date">16/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">IA</span>
            <span class="tag">Web</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 21 -->
      <div class="tl-item has-file"
           data-files='[
             {"name":"A21.1.png","type":"image","url":"Atividade_21.1.png"},
             {"name":"A21.2.png","type":"image","url":"Atividade_21.2.png"}
           ]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A21</span>
            <span class="tl-title">Postar link e print do GitHub.io</span>
            <span class="tl-date">19/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">GitHub</span>
            <span class="tag">Portfolio</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver imagens (2)
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

      <!-- 22 -->
      <div class="tl-item" data-files='[]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A22</span>
            <span class="tl-title">Projeto Final (Versão 1)</span>
            <span class="tl-date">23/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Projeto Final</span>
            <span class="tag amber">Em aula</span>
          </div>
          <p class="no-digital">📋 Realizada presencialmente — sem arquivo digital.</p>
        </div>
      </div>

      <!-- 23 -->
      <div class="tl-item has-file"
           data-files='[{"name":"Atividade_23.pdf","type":"pdf","url":"Atividade_23.pdf"}]'>
        <div class="tl-dot-wrap"><div class="tl-dot"></div></div>
        <div class="tl-card">
          <div class="tl-header">
            <span class="tl-num">A23</span>
            <span class="tl-title">Entrega Final do Portfólio GitHub.io</span>
            <span class="tl-date">30/06/2026</span>
          </div>
          <div class="tl-tags">
            <span class="tag">Portfólio</span>
            <span class="tag">GitHub</span>
            <span class="tag green">Entregue</span>
          </div>
          <button class="tl-btn">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M2 4l4 4 4-4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
            </svg> Ver arquivo
          </button>
          <div class="tl-viewer"><div class="file-tabs"></div><div class="tl-viewer-inner"></div></div>
        </div>
      </div>

    </div><!-- /timeline -->
  </div>
</section>

<div class="divider"></div>

<!-- ──────── COMPETÊNCIAS ──────── -->
<section id="competencias">
  <div class="wrap">
    <p class="section-label">04 — Habilidades</p>
    <h2 class="section-title">Competências <em>desenvolvidas</em></h2>

    <div class="skills-grid" style="margin-bottom:48px;">
      <div class="skill-card">
        <div class="skill-icon">🐍</div>
        <div class="skill-name">Python</div>
        <div class="skill-desc">Variáveis, condicionais, laços, funções, listas, arrays e módulos.</div>
        <div class="skill-bar-wrap"><div class="skill-bar" style="--w:.85"></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">🧮</div>
        <div class="skill-name">Lógica de Programação</div>
        <div class="skill-desc">Fluxogramas, pseudocódigo, decomposição de problemas.</div>
        <div class="skill-bar-wrap"><div class="skill-bar" style="--w:.92"></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">📊</div>
        <div class="skill-name">Estruturas de Dados</div>
        <div class="skill-desc">Vetores, listas, dicionários e operações sobre coleções.</div>
        <div class="skill-bar-wrap"><div class="skill-bar" style="--w:.75"></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">🤖</div>
        <div class="skill-name">IA & LLMs</div>
        <div class="skill-desc">Uso de modelos de linguagem para geração e avaliação de exercícios.</div>
        <div class="skill-bar-wrap"><div class="skill-bar" style="--w:.80"></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">⚙️</div>
        <div class="skill-name">Engenharia Aplicada</div>
        <div class="skill-desc">Modelagem e resolução de problemas reais de engenharia com código.</div>
        <div class="skill-bar-wrap"><div class="skill-bar" style="--w:.70"></div></div>
      </div>
      <div class="skill-card">
        <div class="skill-icon">🌐</div>
        <div class="skill-name">Web & GitHub</div>
        <div class="skill-desc">HTML, CSS, publicação no GitHub Pages e versionamento básico.</div>
        <div class="skill-bar-wrap"><div class="skill-bar" style="--w:.68"></div></div>
      </div>
    </div>

    <p class="section-label">Ferramentas utilizadas</p>
    <div class="tools-list">
      <div class="tool-chip"><span class="ic">🐍</span> Python 3</div>
      <div class="tool-chip"><span class="ic">📓</span> Jupyter Notebook</div>
      <div class="tool-chip"><span class="ic">🐙</span> Git / GitHub</div>
      <div class="tool-chip"><span class="ic">🌐</span> GitHub Pages</div>
      <div class="tool-chip"><span class="ic">🤖</span> ChatGPT / Claude</div>
      <div class="tool-chip"><span class="ic">📄</span> Google Docs</div>
      <div class="tool-chip"><span class="ic">🖥️</span> VS Code</div>
      <div class="tool-chip"><span class="ic">📱</span> HEIC / fotos</div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ──────── PROJETO ──────── -->
<section id="projeto">
  <div class="wrap">
    <p class="section-label">05 — Repositório</p>
    <h2 class="section-title">Projeto <em>GitHub.io</em></h2>

    <div class="project-hero">
      <div>
        <div class="project-tag">Portfólio publicado</div>
        <h3 class="project-title">algoritimos2.github.io</h3>
        <p class="project-desc">
          Site estático publicado via GitHub Pages contendo todas as atividades do semestre,
          estruturado em HTML/CSS com JavaScript puro e sem dependências externas.
        </p>
        <div class="project-links">
          <a class="btn-primary" href="https://algoritimos2.github.io" target="_blank">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
              <path d="M2 7h10M7 2l5 5-5 5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Acessar site
          </a>
          <a class="btn-secondary" href="https://github.com/algoritimos2/algoritimos2.github.io/tree/main" target="_blank">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
              <path d="M7 1C3.69 1 1 3.69 1 7c0 2.65 1.72 4.9 4.1 5.69.3.06.41-.13.41-.29v-1.02c-1.67.36-2.02-.8-2.02-.8-.27-.69-.66-.87-.66-.87-.54-.37.04-.36.04-.36.6.04.91.61.91.61.53.9 1.38.64 1.72.49.05-.38.21-.64.38-.79-1.31-.15-2.69-.65-2.69-2.91 0-.64.23-1.17.61-1.58-.06-.15-.26-.75.06-1.56 0 0 .5-.16 1.63.61A5.66 5.66 0 017 4.59c.5 0 1.01.07 1.48.2 1.13-.77 1.63-.61 1.63-.61.32.81.12 1.41.06 1.56.38.41.61.94.61 1.58 0 2.27-1.38 2.76-2.7 2.91.21.18.4.54.4 1.09v1.62c0 .16.11.35.41.29C11.28 11.9 13 9.65 13 7c0-3.31-2.69-6-6-6z" fill="currentColor"/>
            </svg>
            Ver repositório
          </a>
        </div>
        <div class="commit-badge">
          <span class="commit-dot"></span>
          Último commit: <strong>b3638f3</strong>
        </div>
      </div>
      <div class="project-aside">
        <div class="aside-stat">
          <div class="aside-stat-num">23</div>
          <div class="aside-stat-label">Atividades</div>
        </div>
        <div class="aside-stat">
          <div class="aside-stat-num">1</div>
          <div class="aside-stat-label">Repositório</div>
        </div>
        <div class="aside-stat">
          <div class="aside-stat-num">16</div>
          <div class="aside-stat-label">Semanas</div>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ──────── REFLEXÃO ──────── -->
<section id="reflexao">
  <div class="wrap">
    <p class="section-label">06 — Aprendizado</p>
    <h2 class="section-title">Reflexão <em>final</em></h2>

    <div class="reflection-grid">
      <div class="reflection-card">
        <p class="reflection-q">"O que foi mais desafiador?"</p>
        <p class="reflection-a">Resolver os problemas de engenharia exigiu conectar a lógica de programação com conceitos de outras disciplinas, o que foi inicialmente difícil mas muito enriquecedor.</p>
      </div>
      <div class="reflection-card">
        <p class="reflection-q">"Como as LLMs ajudaram no aprendizado?"</p>
        <p class="reflection-a">Usar modelos de linguagem para gerar e avaliar exercícios acelerou minha compreensão dos tópicos. Aprendi a fazer perguntas melhores e a validar criticamente as respostas geradas.</p>
      </div>
      <div class="reflection-card">
        <p class="reflection-q">"Qual atividade mais me desenvolveu?"</p>
        <p class="reflection-a">As atividades de engenharia (A13–A16) foram as mais transformadoras, pois exigiram pensar em soluções completas e evoluir o código ao longo de múltiplas iterações.</p>
      </div>
      <div class="reflection-card">
        <p class="reflection-q">"O que levo para o próximo semestre?"</p>
        <p class="reflection-a">A disciplina de documentar o processo, o hábito de versionar o código com Git e a clareza de que saber perguntar é tão importante quanto saber programar.</p>
      </div>
    </div>
  </div>
</section>

<!-- ──────── FOOTER ──────── -->
<footer>
  <span>© 2026 · Lucas Viana de Freitas · UNIPAMPA</span>
  <span>
    <a href="https://github.com/algoritimos2/algoritimos2.github.io" target="_blank">GitHub</a>
    &nbsp;·&nbsp;
    <a href="https://algoritimos2.github.io" target="_blank">algoritimos2.github.io</a>
  </span>
</footer>

<!-- ──────── SCRIPTS ──────── -->
<script>
/* ─── Timeline viewer ───────────────────────────── */
document.querySelectorAll('.tl-item').forEach(item => {
  const files = JSON.parse(item.dataset.files || '[]');
  const btn = item.querySelector('.tl-btn');
  const viewer = item.querySelector('.tl-viewer');
  const tabsEl = item.querySelector('.file-tabs');
  const inner = item.querySelector('.tl-viewer-inner');
  if (!btn) return;

  let built = false;

  files.forEach((f, i) => {
    const tab = document.createElement('button');
    tab.className = 'file-tab' + (i === 0 ? ' active' : '');
    tab.textContent = f.name;
    tab.addEventListener('click', () => showFile(files, i, tabsEl, inner));
    tabsEl.appendChild(tab);
  });

  btn.addEventListener('click', () => {
    const open = viewer.classList.toggle('open');
    btn.classList.toggle('open', open);
    btn.querySelector('svg').style.transform = open ? 'rotate(180deg)' : '';
    if (open && !built) {
      built = true;
      if (files.length) showFile(files, 0, tabsEl, inner);
    }
  });
});

function showFile(files, idx, tabsEl, inner) {
  tabsEl.querySelectorAll('.file-tab').forEach((t,i)=> t.classList.toggle('active', i===idx));
  const f = files[idx];
  inner.innerHTML = '';

  if (f.type === 'image') {
    const img = document.createElement('img');
    img.src = f.url; img.alt = f.name;
    img.onerror = () => { inner.innerHTML = notFound(f.url); };
    inner.appendChild(img);

  } else if (f.type === 'pdf') {
    const fr = document.createElement('iframe');
    fr.src = f.url; fr.title = f.name;
    inner.appendChild(fr);
    const link = document.createElement('a');
    link.href = f.url; link.target = '_blank';
    link.className = 'file-tab'; link.style.marginTop = '8px';
    link.textContent = '↗ Abrir em nova aba';
    inner.appendChild(link);

  } else if (f.type === 'code') {
    fetch(f.url)
      .then(r => { if (!r.ok) throw 0; return r.text(); })
      .then(text => {
        const pre = document.createElement('pre');
        pre.textContent = text;
        inner.appendChild(pre);
      })
      .catch(() => { inner.innerHTML = notFound(f.url); });

  } else if (f.type === 'heic') {
    inner.innerHTML = `
      <div class="heic-notice">
        ⚠️ Arquivos .heic não são exibidos diretamente no navegador.<br>
        <a href="${f.url}" download style="color:var(--amber);margin-top:8px;display:inline-block;">⬇ Baixar ${f.name}</a>
      </div>`;
  }
}

function notFound(url) {
  return `<p style="color:var(--red);font-size:.8rem;">Arquivo não encontrado: <strong>${url}</strong></p>`;
}

/* ─── Intersection Observer for animations ─────── */
const obs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.querySelectorAll('.skill-bar, .progress-fill').forEach(el => {
      el.classList.add('animated');
      el.style.transform = `scaleX(${el.style.getPropertyValue('--w') || 1})`;
    });

    // ring
    const ring = e.target.querySelector('.ring-fg');
    if (ring) {
      const pct = 0.83;
      ring.style.strokeDashoffset = 283 * (1 - pct);
    }

    obs.unobserve(e.target);
  });
}, { threshold: 0.2 });

document.querySelectorAll('.skills-grid, .progress-section').forEach(el => obs.observe(el));
</script>
</body>
</html>
