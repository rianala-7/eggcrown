"""Generate an EggCrown logo inspired by traditional egg-producer codes.

Common visual conventions in French/European egg producer logos:
  - Hen silhouette in side profile
  - Eggs at the hen's feet (clutch)
  - Sun rising behind (dawn / freshness)
  - Banner ribbon with farm name
  - Warm terracotta + cream + gold palette
  - Modern execution of traditionally rustic codes

This logo combines those codes — hen, sun, eggs — in a clean
parametric Python build. Hand-drawn-feeling silhouette, harmonized
warm palette, modern serif wordmark.

Run:    python build_hen_logo.py
Output: eggcrown-hen.svg
"""

from __future__ import annotations
from pathlib import Path

OUT = Path(__file__).parent / "eggcrown-hen.svg"

# ----- Palette (harmonized warm farm) ---------------------------------------
BG       = "#F4ECD8"   # cream / pale wheat
SUN_HOT  = "#F9C74F"   # gold core
SUN_WARM = "#F28C5A"   # warm transition
HEN      = "#9A4F2A"   # warm terracotta
HEN_DARK = "#5A2810"   # shadow / details
COMB     = "#C7384A"   # red-brick (comb + wattle)
BEAK     = "#E89154"   # warm orange
EGG      = "#F8F0DC"   # cream egg
EGG_LINE = "#B5A88A"   # subtle outline
INK      = "#2A1810"   # deep espresso
SOFT     = "#7A5A38"   # tagline brown

# ----- Canvas ---------------------------------------------------------------
W, H = 800, 720
CX = W / 2


def hen_silhouette(cx: float, cy: float, scale: float = 1.0) -> str:
    """Side-profile hen, facing right.

    Constructed from a single closed path for body, plus separate small
    elements for comb, beak, wattle, eye, legs.
    """
    s = scale
    # Body silhouette — chubby, head facing right with tail feathers up-back
    body = f"""
    <path d="M {cx - 95*s:.1f} {cy + 10*s:.1f}
             C {cx - 110*s:.1f} {cy - 10*s:.1f}, {cx - 110*s:.1f} {cy - 50*s:.1f}, {cx - 90*s:.1f} {cy - 60*s:.1f}
             C {cx - 100*s:.1f} {cy - 80*s:.1f}, {cx - 80*s:.1f} {cy - 95*s:.1f}, {cx - 60*s:.1f} {cy - 78*s:.1f}
             C {cx - 70*s:.1f} {cy - 95*s:.1f}, {cx - 50*s:.1f} {cy - 105*s:.1f}, {cx - 35*s:.1f} {cy - 85*s:.1f}
             C {cx - 30*s:.1f} {cy - 110*s:.1f}, {cx + 5*s:.1f} {cy - 115*s:.1f}, {cx + 25*s:.1f} {cy - 95*s:.1f}
             C {cx + 50*s:.1f} {cy - 105*s:.1f}, {cx + 70*s:.1f} {cy - 88*s:.1f}, {cx + 70*s:.1f} {cy - 70*s:.1f}
             C {cx + 90*s:.1f} {cy - 75*s:.1f}, {cx + 95*s:.1f} {cy - 55*s:.1f}, {cx + 85*s:.1f} {cy - 45*s:.1f}
             C {cx + 90*s:.1f} {cy - 25*s:.1f}, {cx + 80*s:.1f} {cy + 5*s:.1f}, {cx + 60*s:.1f} {cy + 15*s:.1f}
             C {cx + 30*s:.1f} {cy + 25*s:.1f}, {cx - 20*s:.1f} {cy + 25*s:.1f}, {cx - 50*s:.1f} {cy + 20*s:.1f}
             C {cx - 75*s:.1f} {cy + 15*s:.1f}, {cx - 90*s:.1f} {cy + 18*s:.1f}, {cx - 95*s:.1f} {cy + 10*s:.1f} Z"
          fill="{HEN}"/>"""
    # Wing — slightly darker shape over body
    wing = f"""
    <path d="M {cx - 30*s:.1f} {cy - 50*s:.1f}
             C {cx - 50*s:.1f} {cy - 45*s:.1f}, {cx - 60*s:.1f} {cy - 25*s:.1f}, {cx - 50*s:.1f} {cy - 10*s:.1f}
             C {cx - 30*s:.1f} {cy - 5*s:.1f}, {cx - 5*s:.1f} {cy - 15*s:.1f}, {cx + 10*s:.1f} {cy - 35*s:.1f}
             C {cx + 5*s:.1f} {cy - 50*s:.1f}, {cx - 15*s:.1f} {cy - 55*s:.1f}, {cx - 30*s:.1f} {cy - 50*s:.1f} Z"
          fill="{HEN_DARK}" opacity="0.55"/>"""
    # Tail feathers (back-upper)
    tail = f"""
    <path d="M {cx - 90*s:.1f} {cy - 50*s:.1f}
             L {cx - 130*s:.1f} {cy - 80*s:.1f}
             L {cx - 110*s:.1f} {cy - 65*s:.1f}
             L {cx - 140*s:.1f} {cy - 55*s:.1f}
             L {cx - 115*s:.1f} {cy - 45*s:.1f}
             L {cx - 130*s:.1f} {cy - 25*s:.1f}
             L {cx - 100*s:.1f} {cy - 35*s:.1f} Z"
          fill="{HEN_DARK}"/>"""
    # Comb — 3 bumps on top of head
    comb = f"""
    <path d="M {cx + 30*s:.1f} {cy - 102*s:.1f}
             Q {cx + 35*s:.1f} {cy - 118*s:.1f} {cx + 42*s:.1f} {cy - 105*s:.1f}
             Q {cx + 50*s:.1f} {cy - 122*s:.1f} {cx + 58*s:.1f} {cy - 108*s:.1f}
             Q {cx + 66*s:.1f} {cy - 120*s:.1f} {cx + 72*s:.1f} {cy - 105*s:.1f}
             L {cx + 70*s:.1f} {cy - 90*s:.1f}
             L {cx + 30*s:.1f} {cy - 92*s:.1f} Z"
          fill="{COMB}"/>"""
    # Wattle — under chin
    wattle = f"""
    <path d="M {cx + 78*s:.1f} {cy - 60*s:.1f}
             Q {cx + 88*s:.1f} {cy - 50*s:.1f} {cx + 80*s:.1f} {cy - 42*s:.1f}
             Q {cx + 75*s:.1f} {cy - 50*s:.1f} {cx + 78*s:.1f} {cy - 60*s:.1f} Z"
          fill="{COMB}"/>"""
    # Beak — small triangle pointing right
    beak = f"""
    <path d="M {cx + 80*s:.1f} {cy - 70*s:.1f}
             L {cx + 100*s:.1f} {cy - 65*s:.1f}
             L {cx + 80*s:.1f} {cy - 60*s:.1f} Z"
          fill="{BEAK}"/>"""
    # Eye
    eye = f'''
    <circle cx="{cx + 65*s:.1f}" cy="{cy - 75*s:.1f}" r="{3*s:.1f}" fill="{INK}"/>
    <circle cx="{cx + 66*s:.1f}" cy="{cy - 76*s:.1f}" r="{1.2*s:.1f}" fill="{BG}"/>'''
    # Legs (2 thin verticals + 3 toes each)
    legs = f"""
    <line x1="{cx - 10*s:.1f}" y1="{cy + 22*s:.1f}" x2="{cx - 10*s:.1f}" y2="{cy + 60*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{3*s:.1f}" stroke-linecap="round"/>
    <line x1="{cx - 10*s:.1f}" y1="{cy + 60*s:.1f}" x2="{cx - 22*s:.1f}" y2="{cy + 68*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{2.4*s:.1f}" stroke-linecap="round"/>
    <line x1="{cx - 10*s:.1f}" y1="{cy + 60*s:.1f}" x2="{cx - 4*s:.1f}" y2="{cy + 68*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{2.4*s:.1f}" stroke-linecap="round"/>
    <line x1="{cx - 10*s:.1f}" y1="{cy + 60*s:.1f}" x2="{cx + 4*s:.1f}" y2="{cy + 68*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{2.4*s:.1f}" stroke-linecap="round"/>

    <line x1="{cx + 30*s:.1f}" y1="{cy + 22*s:.1f}" x2="{cx + 30*s:.1f}" y2="{cy + 60*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{3*s:.1f}" stroke-linecap="round"/>
    <line x1="{cx + 30*s:.1f}" y1="{cy + 60*s:.1f}" x2="{cx + 18*s:.1f}" y2="{cy + 68*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{2.4*s:.1f}" stroke-linecap="round"/>
    <line x1="{cx + 30*s:.1f}" y1="{cy + 60*s:.1f}" x2="{cx + 36*s:.1f}" y2="{cy + 68*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{2.4*s:.1f}" stroke-linecap="round"/>
    <line x1="{cx + 30*s:.1f}" y1="{cy + 60*s:.1f}" x2="{cx + 44*s:.1f}" y2="{cy + 68*s:.1f}"
          stroke="{HEN_DARK}" stroke-width="{2.4*s:.1f}" stroke-linecap="round"/>"""
    return body + wing + tail + comb + wattle + beak + eye + legs


def egg_oval(cx: float, cy: float, hw: float = 22, hh: float = 28) -> str:
    return (
        f'<ellipse cx="{cx + 2:.1f}" cy="{cy + hh + 4:.1f}" '
        f'rx="{hw:.0f}" ry="3" fill="{INK}" opacity="0.10"/>'
        f'<path d="M {cx:.1f} {cy - hh:.1f} '
        f'C {cx + 0.62*hw:.1f} {cy - 0.95*hh:.1f}, {cx + hw:.1f} {cy - 0.30*hh:.1f}, {cx + hw:.1f} {cy + 0.18*hh:.1f} '
        f'C {cx + hw:.1f} {cy + 0.62*hh:.1f}, {cx + 0.55*hw:.1f} {cy + hh:.1f}, {cx:.1f} {cy + hh:.1f} '
        f'C {cx - 0.55*hw:.1f} {cy + hh:.1f}, {cx - hw:.1f} {cy + 0.62*hh:.1f}, {cx - hw:.1f} {cy + 0.18*hh:.1f} '
        f'C {cx - hw:.1f} {cy - 0.30*hh:.1f}, {cx - 0.62*hw:.1f} {cy - 0.95*hh:.1f}, {cx:.1f} {cy - hh:.1f} Z" '
        f'fill="{EGG}" stroke="{EGG_LINE}" stroke-width="0.8"/>'
        f'<ellipse cx="{cx - 7:.1f}" cy="{cy - 10:.1f}" rx="5" ry="9" '
        f'fill="#FFFFFF" opacity="0.55"/>'
    )


def build() -> str:
    sun_cx, sun_cy = CX + 30, 220
    hen_cx, hen_cy = CX, 280

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <radialGradient id="sunGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%"  stop-color="{SUN_HOT}"/>
      <stop offset="60%" stop-color="{SUN_WARM}" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="{SUN_WARM}" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="{W}" height="{H}" fill="{BG}"/>

  <circle cx="{sun_cx}" cy="{sun_cy}" r="160" fill="url(#sunGrad)"/>
  <circle cx="{sun_cx}" cy="{sun_cy}" r="68" fill="{SUN_HOT}" opacity="0.9"/>

  <line x1="80" y1="380" x2="{W - 80}" y2="380"
        stroke="{HEN_DARK}" stroke-width="1.4" opacity="0.55"/>
  <line x1="120" y1="385" x2="{W - 120}" y2="385"
        stroke="{HEN_DARK}" stroke-width="0.6" opacity="0.35"
        stroke-dasharray="2 4"/>

  {hen_silhouette(hen_cx, hen_cy, scale=1.0)}

  {egg_oval(hen_cx - 80, 370, hw=20, hh=26)}
  {egg_oval(hen_cx - 50, 372, hw=18, hh=23)}
  {egg_oval(hen_cx + 80, 370, hw=20, hh=26)}

  <text x="{CX:.1f}" y="500"
        font-family="'PP Editorial New', 'Recoleta', 'Tiempos Headline', Georgia, 'Times New Roman', serif"
        font-size="86" font-weight="700" text-anchor="middle"
        fill="{INK}" letter-spacing="3">EggCrown</text>

  <g transform="translate({CX:.1f},540)">
    <line x1="-180" y1="0" x2="-12" y2="0" stroke="{COMB}" stroke-width="0.8"/>
    <circle cx="0" cy="0" r="2.5" fill="{SUN_HOT}"/>
    <line x1="12" y1="0" x2="180" y2="0" stroke="{COMB}" stroke-width="0.8"/>
  </g>

  <text x="{CX:.1f}" y="578"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="13" font-weight="600" text-anchor="middle"
        fill="{SOFT}" letter-spacing="14">F E R M E   ·   F R A I S</text>

  <text x="{CX:.1f}" y="615"
        font-family="Georgia, 'Times New Roman', serif" font-style="italic"
        font-size="14" text-anchor="middle"
        fill="{SOFT}" letter-spacing="2">
    Œufs de poules élevées en plein air
  </text>

  <g transform="translate({CX:.1f},660)">
    <line x1="-90" y1="0" x2="-14" y2="0" stroke="{SOFT}" stroke-width="0.4"/>
    <line x1="14"  y1="0" x2="90"  y2="0" stroke="{SOFT}" stroke-width="0.4"/>
    <text x="0" y="4"
          font-family="Helvetica Neue, Arial, sans-serif"
          font-size="9" font-weight="500" text-anchor="middle"
          fill="{SOFT}" letter-spacing="6">PRODUCTEUR FERMIER</text>
  </g>
</svg>
"""


def main() -> None:
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
