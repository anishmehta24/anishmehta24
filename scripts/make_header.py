"""Write assets/header-dark.svg and assets/header-light.svg for the profile README."""
import sys
from pathlib import Path

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)

THEMES = {
    "dark": dict(bg0="#0b1220", bg1="#13203b", border="#1e2a44", name="#f1f5f9", sub="#94a3b8",
                 accent="#38bdf8", chip="#0f1a30", chipline="#24324f", chiptext="#cbd5e1",
                 lane="#475569", b1="#38bdf8", b2="#a78bfa", dot="#1e293b"),
    "light": dict(bg0="#f8fafc", bg1="#e8eefc", border="#d0d7de", name="#1f2328", sub="#57606a",
                  accent="#0969da", chip="#ffffff", chipline="#d0d7de", chiptext="#24292f",
                  lane="#94a3b8", b1="#0969da", b2="#8250df", dot="#dbe3ef"),
}

SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'Cascadia Code', Consolas, 'Liberation Mono', monospace"

CHIPS = [  # (bold part, rest, width)
    ("150+", " merged PRs", 196),
    ("30+", " open-source projects", 262),
    ("SWE Intern", " @ Clootrack", 236),
    ("CSE '27", " · BIT Mesra", 206),
]


def graph(c):
    """A small git-graph motif: a main lane with two branches that merge back."""
    main_y, up_y, down_y = 150, 92, 206
    parts = [
        f'<path d="M760 {main_y} H1150" stroke="{c["lane"]}" stroke-width="3" fill="none" stroke-linecap="round"/>',
        # branch 1: out at 800, back at 1000
        f'<path d="M800 {main_y} C830 {main_y} 830 {up_y} 860 {up_y} H940 C970 {up_y} 970 {main_y} 1000 {main_y}" '
        f'stroke="{c["b1"]}" stroke-width="3" fill="none" stroke-linecap="round"/>',
        # branch 2: out at 1000, back at 1120
        f'<path d="M1000 {main_y} C1025 {main_y} 1025 {down_y} 1050 {down_y} H1070 C1095 {down_y} 1095 {main_y} 1120 {main_y}" '
        f'stroke="{c["b2"]}" stroke-width="3" fill="none" stroke-linecap="round"/>',
    ]
    nodes = [(760, main_y, c["lane"]), (880, main_y, c["lane"]), (1150, main_y, c["lane"]),
             (860, up_y, c["b1"]), (900, up_y, c["b1"]), (940, up_y, c["b1"]),
             (1050, down_y, c["b2"]), (1070, down_y, c["b2"])]
    for x, y, col in nodes:
        parts.append(f'<circle cx="{x}" cy="{y}" r="7" fill="{c["bg1"]}" stroke="{col}" stroke-width="3"/>')
    # merge commits: filled
    for x, col in ((1000, c["b1"]), (1120, c["b2"])):
        parts.append(f'<circle cx="{x}" cy="{main_y}" r="9" fill="{col}"/>')
    return "\n    ".join(parts)


def svg(theme):
    c = THEMES[theme]
    chips, x = [], 64
    for bold, rest, w in CHIPS:
        chips.append(
            f'<rect x="{x}" y="232" width="{w}" height="40" rx="20" fill="{c["chip"]}" stroke="{c["chipline"]}"/>'
            f'<text x="{x + w / 2}" y="258" text-anchor="middle" font-family="{SANS}" font-size="17" fill="{c["chiptext"]}">'
            f'<tspan font-weight="700" fill="{c["accent"]}">{bold}</tspan>{rest}</text>'
        )
        x += w + 14
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="320" viewBox="0 0 1200 320" role="img" aria-label="Anish Mehta, backend and systems engineer, open-source contributor">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{c["bg0"]}"/>
      <stop offset="1" stop-color="{c["bg1"]}"/>
    </linearGradient>
    <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.6" fill="{c["dot"]}"/>
    </pattern>
  </defs>
  <rect x="1" y="1" width="1198" height="318" rx="18" fill="url(#bg)" stroke="{c["border"]}" stroke-width="2"/>
  <rect x="744" y="24" width="432" height="196" fill="url(#dots)" opacity="0.9"/>
  <text x="64" y="84" font-family="{MONO}" font-size="18" fill="{c["accent"]}">~/anishmehta24</text>
  <text x="62" y="150" font-family="{SANS}" font-size="64" font-weight="700" fill="{c["name"]}">Anish Mehta</text>
  <text x="64" y="194" font-family="{SANS}" font-size="24" fill="{c["sub"]}">Backend and systems engineer · open-source contributor</text>
  <g>
    {graph(c)}
  </g>
  {"".join(chips)}
</svg>
'''


for t in THEMES:
    (out / f"header-{t}.svg").write_text(svg(t), encoding="utf-8")
    print("wrote", out / f"header-{t}.svg")
