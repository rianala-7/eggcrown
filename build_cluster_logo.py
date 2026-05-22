"""Generate an EggCrown abstract-mark logo — hex cluster of seven eggs.

Departs from the seal/badge family. Concept: seven eggs in hex formation
(one centre + six around) reads as abundance and pattern, without ever
being an "egg with X" composition (per skill memory: no crown imagery).

Each egg is identical in size; variation comes from a deterministic
rotation per position, computed from the polar angle. Math owns the
arrangement; the wordmark sits below in Quiet Serif Revival.

Run:    python build_cluster_logo.py
Output: eggcrown-cluster.svg
"""

from __future__ import annotations
import math
from pathlib import Path

OUT = Path(__file__).parent / "eggcrown-cluster.svg"

# ----- Palette (Warm Minimalism) --------------------------------------------
BG        = "#F0EEE9"   # Cloud Dancer
EGG_LIGHT = "#FAF6EB"
EGG_MID   = "#EDE3CF"
EGG_DARK  = "#D8C9AB"
ACCENT    = "#C9A788"   # Dusty Apricot
SOFT      = "#7C6F5A"   # Driftwood
INK       = "#2C2A26"   # Espresso

# ----- Canvas ---------------------------------------------------------------
W, H = 720, 820
CX = W / 2
CLUSTER_CY = 290

EGG_HW = 36
EGG_HH = 48
HEX_R  = EGG_HW * 1.95   # ring radius — slightly larger than 2·hw avoids overlap


# ===== Helpers ==============================================================

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


def hex_positions(cx: float, cy: float, r: float):
    """Yield 7 (x, y, rotation_deg) — center first, then 6 outer."""
    yield (cx, cy, 0)
    for i in range(6):
        angle = 2 * math.pi * i / 6 - math.pi / 2
        yield (
            cx + r * math.cos(angle),
            cy + r * math.sin(angle),
            -8 + (i * 16) / 5,    # spread rotation -8 to +8 around the ring
        )


def render_egg(cx: float, cy: float, rot: float) -> str:
    return f'''
    <g transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})">
      <ellipse cx="{cx:.1f}" cy="{cy + EGG_HH + 4:.1f}"
               rx="{EGG_HW + 3:.1f}" ry="2.5"
               fill="{INK}" opacity="0.10"/>
      <path d="{egg_path(cx, cy, EGG_HW, EGG_HH)}"
            fill="url(#eggBody)" stroke="#B5A88A" stroke-width="0.6"/>
      <ellipse cx="{cx - EGG_HW * 0.36:.1f}" cy="{cy - EGG_HH * 0.36:.1f}"
               rx="{EGG_HW * 0.20:.1f}" ry="{EGG_HH * 0.25:.1f}"
               fill="#FFFFFF" opacity="0.42"/>
    </g>'''


# ===== Build ================================================================

def build() -> str:
    eggs = "".join(render_egg(x, y, r) for x, y, r in hex_positions(CX, CLUSTER_CY, HEX_R))

    enclosing_r = HEX_R + EGG_HW + 18

    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">
  <defs>
    <radialGradient id="eggBody" cx="35%" cy="30%" r="65%">
      <stop offset="0%"  stop-color="{EGG_LIGHT}"/>
      <stop offset="55%" stop-color="{EGG_MID}"/>
      <stop offset="100%" stop-color="{EGG_DARK}"/>
    </radialGradient>
  </defs>

  <rect width="{W}" height="{H}" fill="{BG}"/>

  <circle cx="{CX:.1f}" cy="{CLUSTER_CY:.1f}" r="{enclosing_r:.1f}"
          fill="none" stroke="{ACCENT}" stroke-width="0.5" opacity="0.45"/>
  <circle cx="{CX:.1f}" cy="{CLUSTER_CY:.1f}" r="{enclosing_r - 6:.1f}"
          fill="none" stroke="{ACCENT}" stroke-width="0.3"
          stroke-dasharray="2,4" opacity="0.35"/>

  {eggs}

  <text x="{CX:.1f}" y="525"
        font-family="'PP Editorial New', 'Recoleta', 'Tiempos Headline', Georgia, 'Times New Roman', serif"
        font-size="86" font-weight="700" text-anchor="middle"
        fill="{INK}" letter-spacing="2">EggCrown</text>

  <g transform="translate({CX:.1f},555)">
    <line x1="-180" y1="0" x2="-10" y2="0" stroke="{ACCENT}" stroke-width="0.8"/>
    <line x1="10"   y1="0" x2="180"  y2="0" stroke="{ACCENT}" stroke-width="0.8"/>
    <circle cx="0" cy="0" r="2.2" fill="{ACCENT}"/>
  </g>

  <text x="{CX:.1f}" y="592"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="12" font-weight="500" text-anchor="middle"
        fill="{SOFT}" letter-spacing="14">SEVEN  A  DAY  ·  BY  HAND</text>

  <text x="{CX:.1f}" y="638"
        font-family="Georgia, 'Times New Roman', serif" font-style="italic"
        font-size="13" text-anchor="middle"
        fill="{SOFT}" letter-spacing="2">
    Pasture-raised · Hand-collected · Naturally graded
  </text>

  <g transform="translate({CX:.1f},700)">
    <line x1="-90" y1="0" x2="-14" y2="0" stroke="{SOFT}" stroke-width="0.4"/>
    <line x1="14"  y1="0" x2="90"  y2="0" stroke="{SOFT}" stroke-width="0.4"/>
    <text x="0" y="4"
          font-family="Helvetica Neue, Arial, sans-serif"
          font-size="9" font-weight="500" text-anchor="middle"
          fill="{SOFT}" letter-spacing="6">FROM THE FARM</text>
  </g>
</svg>
"""


def main() -> None:
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
