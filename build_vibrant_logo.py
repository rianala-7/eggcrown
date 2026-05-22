"""Generate an EggCrown modern · dynamic · colorful logo.

Direction: Retro Futurism (per skill trends-2026.md §6) — 70s/80s sci-fi
nostalgia meets sleek 2026 execution. Sunset multi-stop gradients,
orbital rings, atomic curves, deep wine cosmic background. Built in
Python to compute parametric orbital geometry and scattered spark
positions.

Run:    python build_vibrant_logo.py
Output: eggcrown-vibrant.svg
"""

from __future__ import annotations
import math
import random
from pathlib import Path

OUT = Path(__file__).parent / "eggcrown-vibrant.svg"

# ----- Palette (Harmonized sunset — single hue progression 47° → 327° → 273°)
# All five accents share a similar lightness band (55–67) and saturation
# range (75–95) so the eye reads them as one luminous family. The
# background extends the curve into deep plum rather than breaking it
# with a cold navy — every element belongs to the same gradient.
BG    = "#1A0E2E"   # deep wine / midnight plum
DEEP  = "#2A1844"   # secondary surface
CREAM = "#FAF4E4"   # warm white (replaces pure #FFFFFF)
GOLD  = "#F9C74F"   # solar core
CORAL = "#F28C5A"   # warm transition (rose-leaning orange)
ROSE  = "#E5577B"   # heat (less acid than magenta)
PLUM  = "#9B5DE5"   # cool transition (red-purple, not blue-purple)

# ----- Canvas ---------------------------------------------------------------
W, H = 900, 720
CX = W / 2
CY = 290

EGG_HW = 88
EGG_HH = 120
TILT = -8


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


def sparks(seed: int = 7, count: int = 14) -> str:
    rng = random.Random(seed)
    out = []
    palette = [CREAM, GOLD, CORAL, ROSE, PLUM]
    for _ in range(count):
        angle = rng.uniform(0, 2 * math.pi)
        radius = rng.uniform(220, 360)
        x = CX + radius * math.cos(angle)
        y = CY + radius * math.sin(angle) * 0.55
        size = rng.uniform(1.4, 3.2)
        color = rng.choice(palette)
        opacity = rng.uniform(0.45, 0.95)
        out.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{size:.1f}" '
            f'fill="{color}" opacity="{opacity:.2f}"/>'
        )
    return "\n  ".join(out)


def build() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <radialGradient id="cosmic" cx="50%" cy="50%" r="55%">
      <stop offset="0%"  stop-color="{DEEP}"/>
      <stop offset="100%" stop-color="{BG}"/>
    </radialGradient>
    <radialGradient id="halo" cx="50%" cy="50%" r="50%">
      <stop offset="0%"   stop-color="{GOLD}"  stop-opacity="0.95"/>
      <stop offset="35%"  stop-color="{CORAL}" stop-opacity="0.85"/>
      <stop offset="70%"  stop-color="{ROSE}"  stop-opacity="0.50"/>
      <stop offset="100%" stop-color="{PLUM}"  stop-opacity="0.00"/>
    </radialGradient>
    <linearGradient id="sunset" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"   stop-color="{GOLD}"/>
      <stop offset="35%"  stop-color="{CORAL}"/>
      <stop offset="70%"  stop-color="{ROSE}"/>
      <stop offset="100%" stop-color="{PLUM}"/>
    </linearGradient>
    <linearGradient id="eggSheen" x1="20%" y1="10%" x2="80%" y2="90%">
      <stop offset="0%"   stop-color="{CREAM}"/>
      <stop offset="60%"  stop-color="#F0E8D2"/>
      <stop offset="100%" stop-color="#D6C9A8"/>
    </linearGradient>
    <linearGradient id="yolk" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="{GOLD}"/>
      <stop offset="100%" stop-color="{CORAL}"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#cosmic)"/>

  <circle cx="{CX:.1f}" cy="{CY:.1f}" r="260" fill="url(#halo)"/>

  <ellipse cx="{CX:.1f}" cy="{CY:.1f}" rx="220" ry="62"
           fill="none" stroke="url(#sunset)" stroke-width="2.5"
           stroke-linecap="round"
           transform="rotate(-18 {CX:.1f} {CY:.1f})"
           stroke-dasharray="320 1200" opacity="0.85"/>
  <ellipse cx="{CX:.1f}" cy="{CY:.1f}" rx="195" ry="48"
           fill="none" stroke="{PLUM}" stroke-width="1.5"
           stroke-linecap="round"
           transform="rotate(22 {CX:.1f} {CY:.1f})"
           stroke-dasharray="200 1200" opacity="0.75"/>

  {sparks()}

  <g transform="rotate({TILT} {CX:.1f} {CY:.1f})">
    <ellipse cx="{CX:.1f}" cy="{CY + EGG_HH + 14:.1f}"
             rx="{EGG_HW + 6:.0f}" ry="6"
             fill="{BG}" opacity="0.65"/>
    <path d="{egg_path(CX, CY, EGG_HW, EGG_HH)}"
          fill="url(#eggSheen)" stroke="{CREAM}" stroke-width="0.6"/>
    <circle cx="{CX - 14:.1f}" cy="{CY + 28:.1f}" r="22" fill="url(#yolk)"/>
    <ellipse cx="{CX - EGG_HW * 0.36:.1f}" cy="{CY - EGG_HH * 0.40:.1f}"
             rx="{EGG_HW * 0.22:.1f}" ry="{EGG_HH * 0.28:.1f}"
             fill="{CREAM}" opacity="0.65"/>
  </g>

  <text x="{CX:.1f}" y="540"
        font-family="'Helvetica Neue', 'Inter', Arial, sans-serif"
        font-size="108" font-weight="900" text-anchor="middle"
        fill="url(#sunset)" letter-spacing="-3">eggcrown</text>

  <g transform="translate({CX:.1f},580)">
    <line x1="-220" y1="0" x2="-90" y2="0" stroke="{PLUM}" stroke-width="0.8"/>
    <circle cx="-80" cy="0" r="2.5" fill="{PLUM}"/>
    <circle cx="0"   cy="0" r="3"   fill="{CORAL}"/>
    <circle cx="80"  cy="0" r="2.5" fill="{ROSE}"/>
    <line x1="90" y1="0" x2="220" y2="0" stroke="{ROSE}" stroke-width="0.8"/>
  </g>

  <text x="{CX:.1f}" y="615"
        font-family="'Helvetica Neue', Arial, sans-serif"
        font-size="13" font-weight="600" text-anchor="middle"
        fill="{CREAM}" letter-spacing="14" opacity="0.85">
    CRACK · BRIGHT · DAILY
  </text>
</svg>
"""


def main() -> None:
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
