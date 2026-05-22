"""Generate an EggCrown minimal-modern logo.

Direction: Subtle Dimensional / Modern Minimal flavor (per skill trends-2026.md).
Pure white canvas, single-line egg outline, geometric sans-serif wordmark.
A complete reset from the warm-cream artisanal family.

The distinctive moment is the single hairline egg with a small filled dot
inside (yolk hint) — an entire object expressed in two strokes.

Run:    python build_minimal_logo.py
Output: eggcrown-minimal.svg
"""

from __future__ import annotations
import math
from pathlib import Path

OUT = Path(__file__).parent / "eggcrown-minimal.svg"

# ----- Palette (Modern Minimal — pure white-and-ink) ------------------------
WHITE   = "#FFFFFF"
INK     = "#0E0E10"   # near-black, slightly warmer than pure black
SOFT    = "#8C8A85"   # mid-grey for tagline
ACCENT  = "#E07A4F"   # warm coral — single shot of color in the dot

# ----- Canvas ---------------------------------------------------------------
W, H = 900, 560
CX = W / 2

EGG_CY = 215
EGG_HW = 78
EGG_HH = 105


def egg_outline(cx: float, cy: float, hw: float, hh: float, k: float = 0.18) -> str:
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


def build() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
     viewBox="0 0 {W} {H}" width="{W}" height="{H}">

  <rect width="{W}" height="{H}" fill="{WHITE}"/>

  <path d="{egg_outline(CX, EGG_CY, EGG_HW, EGG_HH)}"
        fill="none" stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"/>

  <circle cx="{CX:.1f}" cy="{EGG_CY + EGG_HH * 0.18:.1f}" r="9"
          fill="{ACCENT}"/>

  <text x="{CX:.1f}" y="410"
        font-family="Helvetica Neue, 'Helvetica', Arial, sans-serif"
        font-size="64" font-weight="600" text-anchor="middle"
        fill="{INK}" letter-spacing="-1">eggcrown</text>

  <text x="{CX:.1f}" y="450"
        font-family="Helvetica Neue, Arial, sans-serif"
        font-size="11" font-weight="500" text-anchor="middle"
        fill="{SOFT}" letter-spacing="6">PASTURE-RAISED · DAILY</text>
</svg>
"""


def main() -> None:
    OUT.write_text(build(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
