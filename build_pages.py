"""Split the single-page EggCrown site into a real multi-page website.

- Extracts the shared <style> block into style.css (linked by every page)
- Extracts the shared footer + floating WhatsApp button
- Extracts each <section> by id
- Rebuilds 6 standalone pages with a page-based navigation, fixing all
  internal #anchor links so they point to the right page.

Run: python build_pages.py
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
html = (ROOT / "eggcrown-website.html").read_text(encoding="utf-8")

# ---- 1. Shared CSS ---------------------------------------------------------
style = re.search(r"<style>(.*?)</style>", html, re.S).group(1).strip()
style += (
    "\n\n  /* Active nav state (multi-page) */\n"
    "  .nav a.current { color: var(--gold-soft); border-bottom-color: var(--gold); }\n"
)
(ROOT / "style.css").write_text(style, encoding="utf-8")

# ---- 2. Shared fragments ---------------------------------------------------
body   = re.search(r"<body>(.*)</body>", html, re.S).group(1)
footer = re.search(r"<footer>.*?</footer>", body, re.S).group(0)
wa     = re.search(r'<a class="wa-float".*?</a>', body, re.S).group(0)

# ---- 3. Sections by id -----------------------------------------------------
sections = {}
for s in re.findall(r"<section\b.*?</section>", body, re.S):
    m = re.search(r'id="([^"]+)"', s[:120])
    sections[m.group(1) if m else "hero"] = s

# ---- 4. Anchor → page remap ------------------------------------------------
REMAP = {
    'href="#values"':    'href="index.html#values"',
    'href="#why"':       'href="index.html#why"',
    'href="#eggs"':      'href="nos-oeufs.html"',
    'href="#order"':     'href="nos-oeufs.html"',
    'href="#where"':     'href="livraison.html"',
    'href="#subscribe"': 'href="livraison.html"',
    'href="#story"':     'href="histoire.html"',
    'href="#reviews"':   'href="histoire.html"',
    'href="#faq"':       'href="faq.html"',
    'href="#contact"':   'href="contact.html"',
}
def fix(text: str) -> str:
    for a, b in REMAP.items():
        text = text.replace(a, b)
    return text

# ---- 5. Header builder -----------------------------------------------------
NAV = [
    ("nos-oeufs.html", "Nos œufs"),
    ("livraison.html", "Livraison"),
    ("histoire.html",  "Notre histoire"),
    ("faq.html",       "FAQ"),
    ("contact.html",   "Contact"),
]
def header(current: str) -> str:
    lis = ""
    for href, label in NAV:
        cls = ' class="current"' if href == current else ""
        lis += f'      <li><a href="{href}"{cls}>{label}</a></li>\n'
    return (
        "<header>\n"
        '  <div class="container nav">\n'
        '    <a href="index.html" class="wordmark">EggCrown</a>\n'
        "    <ul>\n" + lis + "    </ul>\n"
        '    <div class="lang-switch">\n'
        '      <a href="#" class="active">FR</a><span>·</span>\n'
        '      <a href="#">MG</a><span>·</span>\n'
        '      <a href="#">EN</a>\n'
        "    </div>\n"
        "  </div>\n"
        "</header>"
    )

# ---- 6. Page builder -------------------------------------------------------
def page(filename, title, desc, current, keys):
    content = "\n\n".join(fix(sections[k]) for k in keys)
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" type="image/png" href="eggcrown-logo-new-transparent.png">
<link rel="stylesheet" href="style.css">
</head>
<body>

{header(current)}

{content}

{fix(footer)}

{wa}

</body>
</html>
"""
    (ROOT / filename).write_text(doc, encoding="utf-8")
    print("wrote", filename)


page("index.html", "EggCrown · Œufs frais d'Antananarivo",
     "Producteur fermier d'œufs frais à Antananarivo. Pondu le matin, livré dans la journée.",
     "index.html", ["hero", "values", "why"])

page("nos-oeufs.html", "Nos œufs · EggCrown",
     "Carton de 6, 12 ou plateau de 30 œufs frais à 550 Ar l'œuf. Livré dans tout Antananarivo.",
     "nos-oeufs.html", ["eggs", "order"])

page("livraison.html", "Livraison · EggCrown",
     "Livraison à domicile dans tout Antananarivo, le jour même. Abonnement hebdomadaire.",
     "livraison.html", ["where", "subscribe"])

page("histoire.html", "Notre histoire · EggCrown",
     "Une petite ferme d'œufs à Antananarivo. Frais, locaux, sérieux.",
     "histoire.html", ["story", "reviews"])

page("faq.html", "FAQ · EggCrown",
     "Questions fréquentes : fraîcheur, conservation, livraison, paiement MVola.",
     "faq.html", ["faq"])

page("contact.html", "Contact · EggCrown",
     "Contactez EggCrown par WhatsApp, téléphone ou email à Antananarivo.",
     "contact.html", ["contact"])

print("Done — 6 pages + style.css")
