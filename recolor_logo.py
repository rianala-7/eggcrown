"""Generate 3 color variants of the EggCrown logo on white background.

Approach: detect gold pixels in HSV space (hue 30°-65°, saturation > 0.25),
shift their hue + saturation to the target color, preserve their value
(luminance variations). Cream / near-white pixels (the hen body) keep
their original color so contrast is maintained on white background.

Inputs:  eggcrown-logo-new-transparent.png
Outputs:
  eggcrown-logo-bronze.png  — bronze antique #A87C2D (recommended)
  eggcrown-logo-brown.png   — brun terre #3A2310 (monochrome utilitaire)
  eggcrown-logo-gold.png    — or chaud #C8941F (palette warm minimalism)
"""

from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(__file__).parent
SOURCE = ROOT / "eggcrown-logo-new-transparent.png"

VARIANTS = [
    ("bronze",     "#A87C2D"),
    ("brown",      "#3A2310"),
    ("gold",       "#C8941F"),
    ("forest",     "#3F6B3D"),
    ("burgundy",   "#7B2C36"),
    ("navy",       "#1B2A4E"),
    ("copper",     "#B87333"),
    ("terracotta", "#A8553A"),
    ("rosegold",   "#C08A6E"),
    ("pine",       "#2A4A38"),
    ("rust",       "#9C4A2D"),
    ("aubergine",  "#5B3A4E"),
    ("mocha",      "#4A3528"),
    ("charcoal",   "#2B2B2B"),
    ("mustard",    "#C9962E"),
    ("teal",       "#1F5A5A"),
    ("taupe",      "#6E6259"),
    ("dustyrose",  "#B5836E"),
]

# When True, output keeps the transparent background (no white composite).
TRANSPARENT = True


def rgb_to_hsv_vec(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    maxc = np.maximum(np.maximum(r, g), b)
    minc = np.minimum(np.minimum(r, g), b)
    v = maxc
    delta = maxc - minc
    safe_delta = np.maximum(delta, 1e-10)
    s = np.where(maxc > 0, delta / np.maximum(maxc, 1e-10), 0)
    rc = (maxc - r) / safe_delta
    gc = (maxc - g) / safe_delta
    bc = (maxc - b) / safe_delta
    h = np.where(r == maxc, bc - gc,
         np.where(g == maxc, 2.0 + rc - bc, 4.0 + gc - rc))
    h = (h / 6.0) % 1.0
    h = np.where(delta == 0, 0, h)
    return np.stack([h, s, v], axis=-1)


def hsv_to_rgb_vec(hsv: np.ndarray) -> np.ndarray:
    h, s, v = hsv[..., 0], hsv[..., 1], hsv[..., 2]
    i = np.floor(h * 6).astype(int) % 6
    f = h * 6 - np.floor(h * 6)
    p = v * (1 - s)
    q = v * (1 - s * f)
    t = v * (1 - s * (1 - f))
    out = np.zeros(hsv.shape, dtype=np.float32)
    for idx, (rr, gg, bb) in enumerate([
        (v, t, p), (q, v, p), (p, v, t), (p, q, v), (t, p, v), (v, p, q),
    ]):
        mask = (i == idx)
        out[..., 0] = np.where(mask, rr, out[..., 0])
        out[..., 1] = np.where(mask, gg, out[..., 1])
        out[..., 2] = np.where(mask, bb, out[..., 2])
    return out


def hex_to_rgb01(h: str) -> tuple[float, float, float]:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))


def recolor(img: Image.Image, target_hex: str) -> Image.Image:
    """Replace gold pixels' hue+saturation with target color's, keep value."""
    arr = np.array(img, dtype=np.float32) / 255.0
    rgb = arr[..., :3]
    alpha = arr[..., 3]

    hsv = rgb_to_hsv_vec(rgb)

    # Gold mask: hue in [30°, 65°] (= 0.083..0.181) AND saturation > 0.25
    h = hsv[..., 0]
    s = hsv[..., 1]
    is_gold = (h >= 0.083) & (h <= 0.181) & (s >= 0.25)

    tr, tg, tb = hex_to_rgb01(target_hex)
    target_hsv = rgb_to_hsv_vec(np.array([[[tr, tg, tb]]]))[0, 0]
    th, ts, tv = target_hsv

    # Replace hue and saturation, keep original value
    new_hsv = hsv.copy()
    new_hsv[..., 0] = np.where(is_gold, th, hsv[..., 0])
    new_hsv[..., 1] = np.where(is_gold, ts, hsv[..., 1])

    # Adjust value for the gold zone so darker targets read as deep tones
    # (and not just the gold's original luminance with a different hue).
    # Smooth curve: bright targets → mild dimming, dark targets → strong dimming.
    v_factor = 0.40 + 0.60 * tv
    new_hsv[..., 2] = np.where(is_gold, hsv[..., 2] * v_factor, hsv[..., 2])

    new_rgb = hsv_to_rgb_vec(new_hsv)
    arr[..., :3] = new_rgb
    return Image.fromarray((arr * 255).astype(np.uint8), mode="RGBA")


def composite_on_white(img: Image.Image) -> Image.Image:
    bg = Image.new("RGB", img.size, (255, 255, 255))
    bg.paste(img, mask=img.split()[3])
    return bg


def main() -> None:
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing {SOURCE.name}")
    print(f"Reading {SOURCE.name}...")
    img = Image.open(SOURCE).convert("RGBA")

    for name, hex_code in VARIANTS:
        print(f"  variant '{name}' ({hex_code})...")
        recolored = recolor(img, hex_code)
        if TRANSPARENT:
            out = ROOT / f"eggcrown-logo-{name}-transparent.png"
            recolored.save(out, "PNG")
        else:
            out = ROOT / f"eggcrown-logo-{name}.png"
            composite_on_white(recolored).save(out, "PNG")
        print(f"    -> {out.name}")


if __name__ == "__main__":
    main()
