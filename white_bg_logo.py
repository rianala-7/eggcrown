"""Composite the transparent EggCrown logo onto a white background.

Gold elements that look luminous on black tend to look washed-out on white
because the contrast direction inverts. To compensate, this script darkens
the gold tones slightly (multiplicative curve on RGB) BEFORE compositing,
so the gold stays readable and richer against white.

Usage:
    python white_bg_logo.py
Inputs:
    eggcrown-logo-new-transparent.png
Output:
    eggcrown-logo-white.png      (composited, gold deepened)
    eggcrown-logo-white-raw.png  (composited, no tone adjustment)
"""

from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).parent
SOURCE = ROOT / "eggcrown-logo-new-transparent.png"
OUT_DEEP = ROOT / "eggcrown-logo-white.png"
OUT_RAW  = ROOT / "eggcrown-logo-white-raw.png"


def composite_on_white(img: Image.Image) -> Image.Image:
    """Alpha-composite an RGBA image over an opaque white background."""
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    return bg


def deepen_gold(img: Image.Image) -> Image.Image:
    """Darken the gold tones so they remain readable on white.

    The transformation:
      - keeps near-white pixels (luminance > 240) close to themselves
      - shifts mid-luminance tones (gold, 80–220) toward warmer/deeper amber
      - leaves the alpha channel untouched
    """
    arr = np.array(img).astype(np.float32)
    rgb = arr[..., :3]
    alpha = arr[..., 3]

    lum = 0.299 * rgb[..., 0] + 0.587 * rgb[..., 1] + 0.114 * rgb[..., 2]

    # Strength of darkening per pixel: peaks around mid-luminance (gold zone),
    # tapers to 0 at very light and very dark ends so we don't crush blacks
    # or wash out near-whites further.
    norm = lum / 255.0
    # Bell curve centered on 0.55 (mid-gold), sigma ~0.30
    strength = np.exp(-((norm - 0.55) ** 2) / (2 * 0.30 ** 2))
    # Cap at 25% darkening
    factor = 1.0 - 0.25 * strength
    factor = factor[..., np.newaxis]

    rgb_out = np.clip(rgb * factor, 0, 255)
    arr[..., :3] = rgb_out
    return Image.fromarray(arr.astype(np.uint8), mode="RGBA")


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(
            f"Run remove_black_bg.py first to produce {SOURCE.name}."
        )

    print(f"Reading {SOURCE.name}...")
    img = Image.open(SOURCE).convert("RGBA")
    print(f"  size: {img.size[0]}×{img.size[1]} px")

    print("Compositing on white (no tone adjustment)...")
    raw = composite_on_white(img)
    raw.save(OUT_RAW, "PNG")
    print(f"  -> {OUT_RAW.name}")

    print("Compositing on white with deepened gold tones...")
    deepened = deepen_gold(img)
    final = composite_on_white(deepened)
    final.save(OUT_DEEP, "PNG")
    print(f"  -> {OUT_DEEP.name}")


if __name__ == "__main__":
    main()
