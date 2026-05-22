"""Remove black background from an image, preserve gold/light antialiased edges.

Approach: compute alpha from luminance, so anti-aliased gradients between
gold and black become smooth transparent gradients (rather than hard
thresholded edges that would jag).

Usage:
    1. Save the image at: eggcrown-logo-new.png in this directory
    2. Run:  python remove_black_bg.py
    Output: eggcrown-logo-new-transparent.png
"""

from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).parent
SOURCE = ROOT / "eggcrown-logo-new.png"
OUTPUT = ROOT / "eggcrown-logo-new-transparent.png"


def main() -> None:
    if not SOURCE.exists():
        # Allow .jpg / .jpeg fallback
        for ext in (".jpg", ".jpeg", ".webp"):
            alt = ROOT / f"eggcrown-logo-new{ext}"
            if alt.exists():
                src = alt
                break
        else:
            raise FileNotFoundError(
                f"Save the new logo as 'eggcrown-logo-new.png' (or .jpg/.jpeg/.webp) "
                f"in {ROOT} before running."
            )
    else:
        src = SOURCE

    print(f"Reading {src.name}...")
    img = Image.open(src).convert("RGBA")
    arr = np.array(img, dtype=np.float32)

    # Luminance per pixel (ITU-R BT.601 weights)
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    lum = 0.299 * r + 0.587 * g + 0.114 * b

    # Map luminance to alpha — bright stays opaque, dark becomes transparent.
    # Use a gentle curve: full alpha above 80, full transparent below 8,
    # smooth ramp between for anti-aliased edges.
    alpha = np.clip((lum - 8.0) / (80.0 - 8.0), 0.0, 1.0) * 255.0

    # The RGB channels themselves should be unaffected — we only change alpha.
    arr[..., 3] = alpha

    # Convert back and save
    out = Image.fromarray(arr.astype(np.uint8), mode="RGBA")
    out.save(OUTPUT, "PNG")
    print(f"Wrote {OUTPUT}")
    print(f"  size: {out.size[0]}×{out.size[1]} px")
    nonzero = np.count_nonzero(alpha > 0)
    total = alpha.size
    print(f"  {100 * nonzero / total:.1f}% pixels visible")


if __name__ == "__main__":
    main()
