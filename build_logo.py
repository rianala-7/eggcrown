"""Generate the EggCrown logo system — opaque + transparent variants + brand sheet.

Outputs (in this directory):

  eggcrown-primary.svg            full ornate badge with cream background
  eggcrown-primary-clear.svg      same, transparent background

  eggcrown-horizontal.svg         horizontal lockup with cream background
  eggcrown-horizontal-clear.svg   same, transparent

  eggcrown-mark.svg               square mark with cream background
  eggcrown-mark-clear.svg         same, transparent

  eggcrown-wordmark.svg           type lockup with cream background
  eggcrown-wordmark-clear.svg     same, transparent

  eggcrown-favicon.svg            dark-bg app icon (keep its own bg)

  eggcrown-mono.svg               single-ink monochrome with cream background
  eggcrown-mono-clear.svg         same, transparent

  eggcrown-pngs/                  PNG exports (best-effort via svglib)
  brand-guidelines.pdf            usage documentation

Run:   python build_logo.py
"""

from __future__ import annotations
import math
from pathlib import Path

OUT_DIR = Path(__file__).parent
PNG_DIR = OUT_DIR / "eggcrown-pngs"

# ----- Palette --------------------------------------------------------------
BG        = "#F0EEE9"   # Cloud Dancer (Pantone 2026)
EGG_LIGHT = "#FAF6EB"
EGG_MID   = "#EDE3CF"
EGG_DARK  = "#D8C9AB"
ACCENT    = "#C9A788"   # Dusty Apricot
SOFT      = "#7C6F5A"   # Driftwood
INK       = "#2C2A26"   # Espresso
PHI = 1.6180339887


# ===== Geometry helpers =====================================================

def egg_path(cx: float, cy: float, hw: float, hh: float, k: float = 0.18) -> str:
    return (
        f"M {cx:.2f} {cy - hh:.2f} "
        f"C {cx + 0.62 * hw:.2f} {cy - 0.95 * hh:.2f}, "
        f"{cx + hw:.2f} {cy - 0.30 * hh:.2f}, "
        f"{cx + hw:.2f} {cy + k * hh:.2f} "
        f"C {cx + hw:.2f} {cy + 0.62 * hh:.2f}, "
        f"{cx + 0.55 * hw:.2f} {cy + hh:.2f}, "
        f"{cx:.2f} {cy + hh:.2f} "
        f"C {cx - 0.55 * hw:.2f} {cy + hh:.2f}, "
        f"{cx - hw:.2f} {cy + 0.62 * hh:.2f}, "
        f"{cx - hw:.2f} {cy + k * hh:.2f} "
        f"C {cx - hw:.2f} {cy - 0.30 * hh:.2f}, "
        f"{cx - 0.62 * hw:.2f} {cy - 0.95 * hh:.2f}, "
        f"{cx:.2f} {cy - hh:.2f} Z"
    )


def sunburst(cx: float, cy: float, inner_r: float, outer_r: float,
             count: int = 32, color: str = ACCENT) -> str:
    out = []
    for i in range(count):
        a = 2 * math.pi * i / count - math.pi / 2
        r2 = outer_r if i % 2 == 0 else outer_r * 0.62
        x1, y1 = cx + inner_r * math.cos(a), cy + inner_r * math.sin(a)
        x2, y2 = cx + r2 * math.cos(a), cy + r2 * math.sin(a)
        out.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="0.7" stroke-linecap="round" '
            f'opacity="0.55"/>'
        )
    return "\n  ".join(out)


def laurel_branch(bx: float, by: float, side: int,
                  length: float = 130, leaves: int = 7,
                  leaf_a: str = ACCENT, leaf_b: str = SOFT,
                  stem: str = SOFT) -> str:
    tx, ty = bx + side * length * 0.78, by - length * 0.55
    qx, qy = bx + side * length * 0.30, by - length * 0.85
    parts = [
        f'<path d="M {bx:.1f} {by:.1f} Q {qx:.1f} {qy:.1f} {tx:.1f} {ty:.1f}" '
        f'fill="none" stroke="{stem}" stroke-width="1.6" stroke-linecap="round"/>'
    ]
    for i in range(leaves):
        t = (i + 1) / (leaves + 1)
        x = (1 - t) ** 2 * bx + 2 * (1 - t) * t * qx + t ** 2 * tx
        y = (1 - t) ** 2 * by + 2 * (1 - t) * t * qy + t ** 2 * ty
        dx = 2 * (1 - t) * (qx - bx) + 2 * t * (tx - qx)
        dy = 2 * (1 - t) * (qy - by) + 2 * t * (ty - qy)
        ang = math.degrees(math.atan2(dy, dx))
        leaf_len = 14 - i * 1.0
        leaf_w = 5 - i * 0.35
        for s, c in ((-1, leaf_a), (1, leaf_b)):
            parts.append(
                f'<ellipse cx="{x:.1f}" cy="{y:.1f}" '
                f'rx="{leaf_len:.1f}" ry="{leaf_w:.1f}" '
                f'fill="{c}" opacity="0.78" '
                f'transform="rotate({ang + s * 55:.1f} {x:.1f} {y:.1f})"/>'
            )
    parts.append(f'<circle cx="{tx:.1f}" cy="{ty:.1f}" r="3" fill="{leaf_a}"/>')
    return "\n  ".join(parts)


def banner_ribbon(cx: float, cy: float, width: float, height: float,
                  fill: str = ACCENT, tail: str = SOFT) -> str:
    hw, hh = width / 2, height / 2
    return f'''
    <g>
      <path d="M {cx - hw - 30:.1f} {cy - 6:.1f}
               L {cx - hw:.1f} {cy - hh - 4:.1f}
               L {cx - hw:.1f} {cy - hh:.1f}
               L {cx - hw - 22:.1f} {cy:.1f}
               L {cx - hw:.1f} {cy + hh:.1f}
               L {cx - hw:.1f} {cy + hh + 4:.1f}
               L {cx - hw - 30:.1f} {cy + 6:.1f}
               L {cx - hw - 22:.1f} {cy:.1f} Z"
            fill="{tail}" opacity="0.92"/>
      <path d="M {cx + hw + 30:.1f} {cy - 6:.1f}
               L {cx + hw:.1f} {cy - hh - 4:.1f}
               L {cx + hw:.1f} {cy - hh:.1f}
               L {cx + hw + 22:.1f} {cy:.1f}
               L {cx + hw:.1f} {cy + hh:.1f}
               L {cx + hw:.1f} {cy + hh + 4:.1f}
               L {cx + hw + 30:.1f} {cy + 6:.1f}
               L {cx + hw + 22:.1f} {cy:.1f} Z"
            fill="{tail}" opacity="0.92"/>
      <rect x="{cx - hw:.1f}" y="{cy - hh:.1f}"
            width="{width:.1f}" height="{height:.1f}" fill="{fill}"/>
      <line x1="{cx - hw:.1f}" y1="{cy - hh + 3:.1f}"
            x2="{cx + hw:.1f}" y2="{cy - hh + 3:.1f}"
            stroke="#FFFFFF" stroke-width="0.5" opacity="0.5"/>
      <line x1="{cx - hw:.1f}" y1="{cy + hh - 3:.1f}"
            x2="{cx + hw:.1f}" y2="{cy + hh - 3:.1f}"
            stroke="{INK}" stroke-width="0.4" opacity="0.4"/>
    </g>'''


def fleuron(cx: float, cy: float, size: float = 7, color: str = ACCENT) -> str:
    s = size
    return (
        f'<g transform="translate({cx:.1f},{cy:.1f})" fill="{color}">'
        f'<path d="M 0 -{s} L {s*0.55:.2f} 0 L 0 {s} L -{s*0.55:.2f} 0 Z"/>'
        f'<line x1="-{s*1.6:.2f}" y1="0" x2="-{s*0.55:.2f}" y2="0" '
        f'stroke="{color}" stroke-width="0.6"/>'
        f'<line x1="{s*0.55:.2f}" y1="0" x2="{s*1.6:.2f}" y2="0" '
        f'stroke="{color}" stroke-width="0.6"/>'
        f'<circle cx="-{s*1.6:.2f}" cy="0" r="1.4"/>'
        f'<circle cx="{s*1.6:.2f}" cy="0" r="1.4"/>'
        f'</g>'
    )


def ornament_rule(cx: float, cy: float, width: float = 360,
                  fleuron_size: float = 7, color: str = INK,
                  fleuron_color: str = ACCENT) -> str:
    half = width / 2
    return f'''
    <line x1="{cx - half:.1f}" y1="{cy:.1f}"
          x2="{cx - fleuron_size * 2:.1f}" y2="{cy:.1f}"
          stroke="{color}" stroke-width="0.7"/>
    <line x1="{cx + fleuron_size * 2:.1f}" y1="{cy:.1f}"
          x2="{cx + half:.1f}" y2="{cy:.1f}"
          stroke="{color}" stroke-width="0.7"/>
    {fleuron(cx, cy, fleuron_size, fleuron_color)}'''


def corner_flourish(x: float, y: float, rotation: int,
                    stroke: str = SOFT, dot: str = ACCENT) -> str:
    return f'''
    <g transform="translate({x:.1f},{y:.1f}) rotate({rotation})"
       fill="none" stroke="{stroke}" stroke-width="1.2" stroke-linecap="round">
      <line x1="0" y1="0" x2="40" y2="0"/>
      <line x1="0" y1="0" x2="0" y2="40"/>
      <path d="M 12 12 Q 26 16 30 28 M 12 12 Q 16 26 28 30"/>
      <circle cx="22" cy="22" r="2" fill="{dot}" stroke="none"/>
    </g>'''


def egg_block(cx: float, cy: float, hw: float, hh: float,
              outline: str = "#B5A88A", highlight: bool = True) -> str:
    blocks = [
        f'<ellipse cx="{cx:.1f}" cy="{cy + hh + 6:.1f}" '
        f'rx="{hw + 8:.0f}" ry="6" fill="{INK}" opacity="0.10"/>',
        f'<path d="{egg_path(cx, cy, hw, hh)}" '
        f'fill="url(#eggBody)" stroke="{outline}" stroke-width="0.9"/>',
    ]
    if highlight:
        blocks.append(
            f'<ellipse cx="{cx - hw * 0.36:.1f}" cy="{cy - hh * 0.36:.1f}" '
            f'rx="{hw * 0.20:.1f}" ry="{hh * 0.25:.1f}" '
            f'fill="#FFFFFF" opacity="0.45"/>'
        )
        blocks.append(
            f'<ellipse cx="{cx + hw * 0.33:.1f}" cy="{cy + hh * 0.26:.1f}" '
            f'rx="{hw * 0.08:.1f}" ry="{hh * 0.10:.1f}" '
            f'fill="#FFFFFF" opacity="0.18"/>'
        )
    return f'<g filter="url(#eggShadow)">{"".join(blocks)}</g>'


# ===== Reusable defs ========================================================

def common_defs(include_kraft: bool = True) -> str:
    kraft = ""
    if include_kraft:
        kraft = f'''
    <pattern id="kraft" x="0" y="0" width="3.5" height="3.5"
             patternUnits="userSpaceOnUse">
      <circle cx="1" cy="1" r="0.25" fill="{SOFT}" opacity="0.18"/>
    </pattern>'''
    return f'''
  <defs>
    <radialGradient id="eggBody" cx="35%" cy="30%" r="65%">
      <stop offset="0%"  stop-color="{EGG_LIGHT}"/>
      <stop offset="55%" stop-color="{EGG_MID}"/>
      <stop offset="100%" stop-color="{EGG_DARK}"/>
    </radialGradient>
    <filter id="eggShadow" x="-30%" y="-10%" width="160%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="6"/>
      <feOffset dx="0" dy="10" result="b"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.22"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>{kraft}
  </defs>'''


def mono_defs() -> str:
    return f'''
  <defs>
    <radialGradient id="eggBody" cx="35%" cy="30%" r="65%">
      <stop offset="0%"  stop-color="{INK}" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="{INK}" stop-opacity="0.95"/>
    </radialGradient>
    <filter id="eggShadow" x="-30%" y="-10%" width="160%" height="140%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="4"/>
      <feOffset dx="0" dy="6" result="b"/>
      <feComponentTransfer><feFuncA type="linear" slope="0.25"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>'''


def background(W: float, H: float, transparent: bool, kraft: bool = True) -> str:
    if transparent:
        return ""
    layers = [f'<rect width="{W}" height="{H}" fill="{BG}"/>']
    if kraft:
        layers.append(f'<rect width="{W}" height="{H}" fill="url(#kraft)"/>')
    return "\n".join(layers)


# ===== Variant builders =====================================================

def build_primary(transparent: bool = False) -> str:
    W, H = 900, 700
    CX = W / 2
    egg_cx, egg_cy = CX, 245
    margin = 28
    fx, fy = margin, margin
    fw, fh = W - 2 * margin, H - 2 * margin
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">
{common_defs(include_kraft=not transparent)}

  {background(W, H, transparent)}

  <rect x="{fx}" y="{fy}" width="{fw}" height="{fh}"
        fill="none" stroke="{INK}" stroke-width="2"/>
  <rect x="{fx + 9}" y="{fy + 9}" width="{fw - 18}" height="{fh - 18}"
        fill="none" stroke="{INK}" stroke-width="0.6"/>
  <rect x="{fx + 14}" y="{fy + 14}" width="{fw - 28}" height="{fh - 28}"
        fill="none" stroke="{ACCENT}" stroke-width="0.4"/>

  {corner_flourish(fx + 22, fy + 22, 0)}
  {corner_flourish(fx + fw - 22, fy + 22, 90)}
  {corner_flourish(fx + fw - 22, fy + fh - 22, 180)}
  {corner_flourish(fx + 22, fy + fh - 22, 270)}

  <g>{sunburst(egg_cx, egg_cy + 10, inner_r=125, outer_r=200)}</g>
  {laurel_branch(egg_cx - 80, egg_cy + 90, side=-1, length=160)}
  {laurel_branch(egg_cx + 80, egg_cy + 90, side=+1, length=160)}

  {banner_ribbon(CX, egg_cy + 75, width=440, height=32)}
  <text x="{CX - 80:.1f}" y="{egg_cy + 80:.1f}"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="19" font-weight="700" text-anchor="end"
        fill="{INK}" letter-spacing="9">EGG</text>
  <text x="{CX + 80:.1f}" y="{egg_cy + 80:.1f}"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="19" font-weight="700" text-anchor="start"
        fill="{INK}" letter-spacing="9">CROWN</text>

  {egg_block(egg_cx, egg_cy, hw=72, hh=98)}

  {ornament_rule(CX, 410, width=440, fleuron_size=8)}

  <text x="{CX:.1f}" y="490"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="86" font-weight="700" text-anchor="middle"
        fill="{INK}" letter-spacing="2">EggCrown</text>

  {ornament_rule(CX, 525, width=440, fleuron_size=8)}

  <text x="{CX:.1f}" y="558"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="13" font-weight="500" text-anchor="middle"
        fill="{SOFT}" letter-spacing="14">F A R M   ·   T A B L E   ·   E S T A T E</text>

  <g>
    <circle cx="{CX - 35:.1f}" cy="600" r="2" fill="{ACCENT}"/>
    <circle cx="{CX:.1f}"      cy="595" r="3" fill="{ACCENT}"/>
    <circle cx="{CX + 35:.1f}" cy="600" r="2" fill="{ACCENT}"/>
    <line x1="{CX - 90:.1f}" y1="600" x2="{CX - 50:.1f}" y2="600"
          stroke="{ACCENT}" stroke-width="0.6"/>
    <line x1="{CX + 50:.1f}" y1="600" x2="{CX + 90:.1f}" y2="600"
          stroke="{ACCENT}" stroke-width="0.6"/>
  </g>
</svg>
"""


def build_horizontal(transparent: bool = False) -> str:
    W, H = 1200, 380
    CY = H / 2
    egg_cx, egg_cy = 230, CY
    text_x = 470
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">
{common_defs(include_kraft=False)}

  {background(W, H, transparent, kraft=False)}

  <g>{sunburst(egg_cx, egg_cy + 10, inner_r=110, outer_r=170)}</g>
  {laurel_branch(egg_cx - 70, egg_cy + 70, side=-1, length=130)}
  {laurel_branch(egg_cx + 70, egg_cy + 70, side=+1, length=130)}
  {egg_block(egg_cx, egg_cy - 5, hw=58, hh=80)}

  <line x1="430" y1="80" x2="430" y2="{H - 80}"
        stroke="{INK}" stroke-width="0.8"/>

  <text x="{text_x}" y="170"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="92" font-weight="700"
        fill="{INK}" letter-spacing="2">EggCrown</text>

  <line x1="{text_x}" y1="200" x2="{text_x + 480}" y2="200"
        stroke="{ACCENT}" stroke-width="0.6"/>
  {fleuron(text_x + 240, 200, 6)}

  <text x="{text_x}" y="240"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="14" font-weight="500"
        fill="{SOFT}" letter-spacing="14">FARM-FRESH PREMIUM EGGS</text>

  <text x="{text_x}" y="290"
        font-family="Georgia, serif" font-style="italic"
        font-size="13" fill="{SOFT}" letter-spacing="3">
    Hand-collected · Pasture-raised · Family-owned
  </text>
</svg>
"""


def build_mark_only(transparent: bool = False) -> str:
    S = 600
    C = S / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {S} {S}" width="{S}" height="{S}">
{common_defs(include_kraft=not transparent)}

  {background(S, S, transparent)}

  <circle cx="{C}" cy="{C}" r="270"
          fill="none" stroke="{INK}" stroke-width="1.6"/>
  <circle cx="{C}" cy="{C}" r="258"
          fill="none" stroke="{ACCENT}" stroke-width="0.5"/>

  <g>{sunburst(C, C + 5, inner_r=130, outer_r=215)}</g>
  {laurel_branch(C - 80, C + 90, side=-1, length=170)}
  {laurel_branch(C + 80, C + 90, side=+1, length=170)}

  {banner_ribbon(C, C + 80, width=440, height=34)}
  <text x="{C - 82:.1f}" y="{C + 86:.1f}"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="20" font-weight="700" text-anchor="end"
        fill="{INK}" letter-spacing="9">EGG</text>
  <text x="{C + 82:.1f}" y="{C + 86:.1f}"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="20" font-weight="700" text-anchor="start"
        fill="{INK}" letter-spacing="9">CROWN</text>

  {egg_block(C, C - 5, hw=78, hh=108)}
</svg>
"""


def build_wordmark(transparent: bool = False) -> str:
    W, H = 1000, 280
    CX = W / 2
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">

  {background(W, H, transparent, kraft=False)}

  {ornament_rule(CX, 70, width=520, fleuron_size=8)}

  <text x="{CX:.1f}" y="170"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="98" font-weight="700" text-anchor="middle"
        fill="{INK}" letter-spacing="2">EggCrown</text>

  {ornament_rule(CX, 210, width=520, fleuron_size=8)}

  <text x="{CX:.1f}" y="248"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="13" font-weight="500" text-anchor="middle"
        fill="{SOFT}" letter-spacing="14">F A R M   ·   T A B L E   ·   E S T A T E</text>
</svg>
"""


def build_favicon(transparent: bool = False) -> str:
    """Favicon keeps its dark rounded-square background by design;
    transparent variant drops the rounded-square but keeps the egg."""
    S = 256
    C = S / 2
    bg_layer = "" if transparent else (
        f'<rect width="{S}" height="{S}" rx="40" ry="40" fill="{INK}"/>'
    )
    egg_outline = ACCENT if not transparent else INK
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {S} {S}" width="{S}" height="{S}">
  <defs>
    <radialGradient id="eggBody" cx="35%" cy="30%" r="65%">
      <stop offset="0%"  stop-color="{EGG_LIGHT}"/>
      <stop offset="100%" stop-color="{EGG_DARK}"/>
    </radialGradient>
  </defs>

  {bg_layer}

  <path d="{egg_path(C, C - 5, hw=64, hh=86)}"
        fill="url(#eggBody)" stroke="{egg_outline}" stroke-width="1.4"/>
  <ellipse cx="{C - 22:.1f}" cy="{C - 38:.1f}" rx="11" ry="20"
           fill="#FFFFFF" opacity="0.55"/>
</svg>
"""


def build_mono(transparent: bool = False) -> str:
    W, H = 900, 700
    CX = W / 2
    egg_cx, egg_cy = CX, 245
    margin = 28
    fx, fy = margin, margin
    fw, fh = W - 2 * margin, H - 2 * margin
    bg_layer = "" if transparent else f'<rect width="{W}" height="{H}" fill="{BG}"/>'

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">
{mono_defs()}

  {bg_layer}

  <rect x="{fx}" y="{fy}" width="{fw}" height="{fh}"
        fill="none" stroke="{INK}" stroke-width="2"/>
  <rect x="{fx + 9}" y="{fy + 9}" width="{fw - 18}" height="{fh - 18}"
        fill="none" stroke="{INK}" stroke-width="0.6"/>

  {corner_flourish(fx + 22, fy + 22, 0, stroke=INK, dot=INK)}
  {corner_flourish(fx + fw - 22, fy + 22, 90, stroke=INK, dot=INK)}
  {corner_flourish(fx + fw - 22, fy + fh - 22, 180, stroke=INK, dot=INK)}
  {corner_flourish(fx + 22, fy + fh - 22, 270, stroke=INK, dot=INK)}

  <g>{sunburst(egg_cx, egg_cy + 10, inner_r=125, outer_r=200, color=INK)}</g>

  {laurel_branch(egg_cx - 80, egg_cy + 90, side=-1, length=160,
                 leaf_a=INK, leaf_b=INK, stem=INK)}
  {laurel_branch(egg_cx + 80, egg_cy + 90, side=+1, length=160,
                 leaf_a=INK, leaf_b=INK, stem=INK)}

  {banner_ribbon(CX, egg_cy + 75, width=440, height=32, fill=INK, tail=INK)}
  <text x="{CX - 80:.1f}" y="{egg_cy + 80:.1f}"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="19" font-weight="700" text-anchor="end"
        fill="{BG}" letter-spacing="9">EGG</text>
  <text x="{CX + 80:.1f}" y="{egg_cy + 80:.1f}"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="19" font-weight="700" text-anchor="start"
        fill="{BG}" letter-spacing="9">CROWN</text>

  {egg_block(egg_cx, egg_cy, hw=72, hh=98, outline=INK)}

  {ornament_rule(CX, 410, width=440, fleuron_size=8,
                 color=INK, fleuron_color=INK)}

  <text x="{CX:.1f}" y="490"
        font-family="Georgia, 'Times New Roman', serif"
        font-size="86" font-weight="700" text-anchor="middle"
        fill="{INK}" letter-spacing="2">EggCrown</text>

  {ornament_rule(CX, 525, width=440, fleuron_size=8,
                 color=INK, fleuron_color=INK)}

  <text x="{CX:.1f}" y="558"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="13" font-weight="500" text-anchor="middle"
        fill="{INK}" letter-spacing="14">F A R M   ·   T A B L E   ·   E S T A T E</text>
</svg>
"""


# ===== PNG export (best-effort, gradients flattened) ========================

def export_pngs() -> list[str]:
    try:
        from svglib.svglib import svg2rlg
        from reportlab.graphics import renderPM
    except ImportError:
        return []

    PNG_DIR.mkdir(exist_ok=True)
    written: list[str] = []
    for svg in OUT_DIR.glob("eggcrown-*.svg"):
        try:
            drawing = svg2rlg(str(svg))
            png_path = PNG_DIR / f"{svg.stem}.png"
            renderPM.drawToFile(drawing, str(png_path), fmt="PNG", dpi=150)
            written.append(png_path.name)
        except Exception as e:
            print(f"  skip {svg.name}: {e}")
    return written


# ===== Brand sheet PDF ======================================================

def build_brand_sheet() -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import cm
    from reportlab.lib import colors as rl
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
        Image, Flowable,
    )
    from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

    out_pdf = OUT_DIR / "brand-guidelines.pdf"
    styles = getSampleStyleSheet()

    H1 = ParagraphStyle("H1", parent=styles["Heading1"],
                        fontName="Times-Bold", fontSize=22, leading=28,
                        spaceAfter=10, textColor=rl.HexColor(INK))
    H2 = ParagraphStyle("H2", parent=styles["Heading2"],
                        fontName="Times-Bold", fontSize=14, leading=18,
                        spaceBefore=14, spaceAfter=6,
                        textColor=rl.HexColor(ACCENT))
    BODY = ParagraphStyle("Body", parent=styles["BodyText"],
                          fontName="Times-Roman", fontSize=10.5, leading=15,
                          alignment=TA_JUSTIFY, textColor=rl.HexColor(INK),
                          spaceAfter=6)
    SMALL = ParagraphStyle("Small", parent=BODY,
                           fontSize=9, leading=12,
                           textColor=rl.HexColor(SOFT))
    TITLE = ParagraphStyle("Title", parent=H1, fontSize=36, leading=42,
                           alignment=TA_CENTER, spaceAfter=20)

    class Swatch(Flowable):
        def __init__(self, hex_code: str, size: int = 14):
            super().__init__()
            self.color = rl.HexColor(hex_code)
            self.size = size
        def wrap(self, *_): return self.size, self.size
        def draw(self):
            self.canv.setFillColor(self.color)
            self.canv.setStrokeColor(rl.HexColor(INK))
            self.canv.setLineWidth(0.4)
            self.canv.rect(0, 0, self.size, self.size, stroke=1, fill=1)

    story = []
    story.append(Spacer(1, 6 * cm))
    story.append(Paragraph("EggCrown", TITLE))
    story.append(Paragraph("Brand Guidelines · Logo System",
                           ParagraphStyle("Sub", parent=BODY,
                                          fontSize=14, alignment=TA_CENTER,
                                          textColor=rl.HexColor(ACCENT),
                                          fontName="Times-Italic")))
    story.append(Spacer(1, 5 * cm))
    story.append(Paragraph(
        "Compiled May 2026 · for use across packaging, web, social and print.",
        ParagraphStyle("Caption", parent=SMALL, alignment=TA_CENTER)))
    story.append(PageBreak())

    # Variants table
    story.append(Paragraph("01 · Logo Variants", H1))
    story.append(Paragraph(
        "The logo system contains six variants, each with both opaque "
        "(cream-background) and transparent versions where applicable. "
        "Use the right variant for each context.",
        BODY))

    variant_rows = [["Variant", "File", "Best for"]]
    variants_doc = [
        ("Primary",
         "eggcrown-primary.svg",
         "Hero, packaging fronts, large-format print."),
        ("Horizontal",
         "eggcrown-horizontal.svg",
         "Web headers, email signatures, letterheads."),
        ("Mark only",
         "eggcrown-mark.svg",
         "App icons, social profile pictures, stamps, embroidery."),
        ("Wordmark",
         "eggcrown-wordmark.svg",
         "Footers, mentions, secondary placements without the mark."),
        ("Favicon",
         "eggcrown-favicon.svg",
         "Browser tabs, app store icons, very small contexts (16–256 px)."),
        ("Monochrome",
         "eggcrown-mono.svg",
         "Embossing, single-color print, fax, overprint on photos."),
    ]
    for n, f, u in variants_doc:
        variant_rows.append([
            Paragraph(f"<b>{n}</b>", BODY),
            Paragraph(f"<font name='Courier'>{f}</font>", SMALL),
            Paragraph(u, BODY),
        ])
    t = Table(variant_rows, colWidths=[3.0 * cm, 5.5 * cm, 7.5 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), rl.HexColor(INK)),
        ("TEXTCOLOR", (0, 0), (-1, 0), rl.HexColor(BG)),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [rl.HexColor(BG), rl.white]),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "Each variant ships in two flavors:<br/>"
        "<b>opaque</b> — `eggcrown-&lt;name&gt;.svg`, with the cream "
        "background, for stand-alone use.<br/>"
        "<b>transparent</b> — `eggcrown-&lt;name&gt;-clear.svg`, no "
        "background, for placement over photos, colored panels or other "
        "visuals.",
        BODY))
    story.append(PageBreak())

    # Colors
    story.append(Paragraph("02 · Color System", H1))
    story.append(Paragraph(
        "Five-color palette grounded in Pantone's 2026 Color of the Year "
        "(Cloud Dancer #F0EEE9). Use Cloud Dancer or pure white as default "
        "background. Never combine more than three of these colors in a "
        "single composition.",
        BODY))
    color_rows = [["", "Hex", "Name", "Role"]]
    colors_doc = [
        ("#F0EEE9", "Cloud Dancer",   "Default background"),
        ("#FAF6EB", "Egg Light",      "Egg highlight zone"),
        ("#EDE3CF", "Egg Mid",        "Egg body mid-tone"),
        ("#D8C9AB", "Egg Dark",       "Egg shadow side"),
        ("#C9A788", "Dusty Apricot",  "Primary accent (banner, fleurons)"),
        ("#7C6F5A", "Driftwood",      "Secondary text & ornaments"),
        ("#2C2A26", "Espresso",       "Primary type & ink"),
    ]
    for hex_code, name, role in colors_doc:
        color_rows.append([
            Swatch(hex_code, size=16),
            Paragraph(f"<font name='Courier'>{hex_code}</font>", BODY),
            Paragraph(name, BODY),
            Paragraph(role, SMALL),
        ])
    ct = Table(color_rows, colWidths=[1 * cm, 3 * cm, 4 * cm, 7.5 * cm])
    ct.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), rl.HexColor(INK)),
        ("TEXTCOLOR", (0, 0), (-1, 0), rl.HexColor(BG)),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))
    story.append(ct)
    story.append(PageBreak())

    # Clear space + sizes
    story.append(Paragraph("03 · Clear Space and Minimum Sizes", H1))
    story.append(Paragraph(
        "<b>Clear space.</b> Always leave a margin around the logo equal to "
        "the height of the lowercase 'g' in the wordmark. Never crowd the "
        "logo with other elements within that margin.",
        BODY))
    story.append(Paragraph(
        "<b>Minimum sizes.</b> Each variant has a minimum render size below "
        "which it stops being legible:",
        BODY))
    size_rows = [["Variant", "Minimum width (px)", "Minimum height (px)"]]
    for n, w, h in [
        ("Primary",     "320", "248"),
        ("Horizontal",  "480", "152"),
        ("Mark only",   "120", "120"),
        ("Wordmark",    "260", "73"),
        ("Favicon",     "16",  "16"),
        ("Monochrome",  "320", "248"),
    ]:
        size_rows.append([n, w, h])
    st = Table(size_rows, colWidths=[5 * cm, 5 * cm, 5 * cm])
    st.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), rl.HexColor(INK)),
        ("TEXTCOLOR", (0, 0), (-1, 0), rl.HexColor(BG)),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [rl.HexColor(BG), rl.white]),
    ]))
    story.append(st)
    story.append(Spacer(1, 0.6 * cm))

    # Do / Don't
    story.append(Paragraph("04 · Do · Don't", H1))
    do_dont = [
        ("DO place transparent variants on photos and colored panels.",
         "DO use the cream background variant when no clear placement exists."),
        ("DO use the monochrome variant for embossing and single-ink print.",
         "DO use the favicon below 64 px — the primary will not be readable."),
        ("DON'T recolor the logo outside the documented palette.",
         "DON'T add drop shadows, glows or strokes around the placed logo."),
        ("DON'T rotate, skew or stretch the logo in any way.",
         "DON'T crop the logo or remove individual elements (laurels, banner)."),
        ("DON'T place the logo on busy patterns without sufficient contrast.",
         "DON'T re-typeset the wordmark — always use the SVG."),
    ]
    for d, n in do_dont:
        story.append(Paragraph(f"✓ {d}", BODY))
        story.append(Paragraph(f"✗ {n}",
                     ParagraphStyle("DontPara", parent=BODY,
                                    textColor=rl.HexColor("#A24E2C"))))
        story.append(Spacer(1, 4))

    # Implementation tips
    story.append(PageBreak())
    story.append(Paragraph("05 · Implementation", H1))
    story.append(Paragraph("Web (HTML/CSS)", H2))
    story.append(Paragraph(
        "Use the SVG directly with <font name='Courier'>&lt;img src=...&gt;</font> "
        "or inline. For favicons add to your &lt;head&gt;:",
        BODY))
    story.append(Paragraph(
        "<font name='Courier'>"
        "&lt;link rel='icon' type='image/svg+xml' "
        "href='/eggcrown-favicon.svg'&gt;</font>",
        SMALL))

    story.append(Paragraph("Print", H2))
    story.append(Paragraph(
        "Convert SVG to PDF or high-resolution PNG (300 DPI minimum) before "
        "sending to print. Use the monochrome variant for any single-ink "
        "process. For CMYK conversion of brand colors, ask the printer to "
        "match the hex codes in §02.",
        BODY))

    story.append(Paragraph("Social media", H2))
    story.append(Paragraph(
        "Profile pictures: <b>eggcrown-mark.svg</b> (square). Cover banners: "
        "<b>eggcrown-horizontal.svg</b>. Story / post graphics: any "
        "transparent variant placed over photo, with at least 8% width "
        "of clear space around the logo.",
        BODY))

    story.append(Paragraph("Packaging", H2))
    story.append(Paragraph(
        "Front-of-pack: <b>eggcrown-primary.svg</b> at minimum 60 mm width. "
        "Sides and back: <b>eggcrown-mono.svg</b> for single-ink overprint. "
        "Foil-stamped emblems: use vector path of <b>eggcrown-mark-clear.svg</b> "
        "(remove gradient and highlight ellipses before sending to die-cutter).",
        BODY))

    SimpleDocTemplate(
        str(out_pdf),
        pagesize=A4,
        leftMargin=2.2 * cm, rightMargin=2.2 * cm,
        topMargin=2.5 * cm, bottomMargin=2.5 * cm,
        title="EggCrown · Brand Guidelines",
        author="EggCrown",
        subject="Logo system, color system, clear-space and implementation",
    ).build(story)


# ===== Main =================================================================

VARIANTS = [
    ("primary",    build_primary),
    ("horizontal", build_horizontal),
    ("mark",       build_mark_only),
    ("wordmark",   build_wordmark),
    ("favicon",    build_favicon),
    ("mono",       build_mono),
]


def main() -> None:
    print("Writing SVG variants...")
    for name, builder in VARIANTS:
        opaque = OUT_DIR / f"eggcrown-{name}.svg"
        clear  = OUT_DIR / f"eggcrown-{name}-clear.svg"
        opaque.write_text(builder(transparent=False), encoding="utf-8")
        clear .write_text(builder(transparent=True),  encoding="utf-8")
        print(f"  {opaque.name}, {clear.name}")

    print("Building brand-guidelines.pdf...")
    build_brand_sheet()
    print(f"  brand-guidelines.pdf")

    print("Exporting PNGs (best-effort, gradients flattened)...")
    pngs = export_pngs()
    if pngs:
        print(f"  {len(pngs)} PNGs in {PNG_DIR.name}/")
    else:
        print("  (skipped — install svglib for PNG export)")

    print(f"\nDone. {OUT_DIR}")


if __name__ == "__main__":
    main()
