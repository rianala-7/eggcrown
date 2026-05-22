"""Build the Logo Design Guide 2026 PDF."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    Flowable, KeepTogether,
)
from reportlab.platypus.tableofcontents import TableOfContents
from reportlab.pdfgen.canvas import Canvas

OUTPUT = r"C:\Users\PC\Documents\claude\poule\logo-design-guide-2026.pdf"

INK = colors.HexColor("#1B1B1B")
GOLD = colors.HexColor("#C8941F")
GOLD_LIGHT = colors.HexColor("#E9B848")
CREAM = colors.HexColor("#FAF7F0")
CLOUD = colors.HexColor("#F0EEE9")
MUTED = colors.HexColor("#7A6A4A")


# ----- Styles -----
styles = getSampleStyleSheet()

H1 = ParagraphStyle(
    "H1", parent=styles["Heading1"],
    fontName="Times-Bold", fontSize=22, leading=28,
    spaceBefore=18, spaceAfter=10, textColor=INK,
)
H2 = ParagraphStyle(
    "H2", parent=styles["Heading2"],
    fontName="Times-Bold", fontSize=15, leading=20,
    spaceBefore=14, spaceAfter=6, textColor=INK,
)
H3 = ParagraphStyle(
    "H3", parent=styles["Heading3"],
    fontName="Times-Bold", fontSize=12, leading=16,
    spaceBefore=10, spaceAfter=4, textColor=GOLD,
)
BODY = ParagraphStyle(
    "Body", parent=styles["BodyText"],
    fontName="Times-Roman", fontSize=10.5, leading=15,
    alignment=TA_JUSTIFY, textColor=INK, spaceAfter=6,
)
ITALIC = ParagraphStyle(
    "Italic", parent=BODY,
    fontName="Times-Italic", textColor=MUTED,
)
TITLE = ParagraphStyle(
    "Title", parent=styles["Title"],
    fontName="Times-Bold", fontSize=44, leading=50,
    alignment=TA_CENTER, textColor=INK, spaceAfter=14,
)
SUBTITLE = ParagraphStyle(
    "Subtitle", parent=styles["Title"],
    fontName="Times-Italic", fontSize=18, leading=24,
    alignment=TA_CENTER, textColor=GOLD, spaceAfter=24,
)
SMALL = ParagraphStyle(
    "Small", parent=BODY, fontSize=8.5, leading=11, textColor=MUTED,
)
CAPTION = ParagraphStyle(
    "Caption", parent=BODY, fontName="Times-Italic",
    fontSize=9, leading=12, alignment=TA_CENTER, textColor=MUTED,
)


# ----- Custom flowables -----

class HRule(Flowable):
    def __init__(self, width, thickness=0.6, color=GOLD):
        super().__init__()
        self.width = width
        self.thickness = thickness
        self.color = color

    def wrap(self, *_):
        return self.width, self.thickness + 4

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 2, self.width, 2)


class ColorSwatch(Flowable):
    """A small colored rectangle for color reference tables."""

    def __init__(self, hex_code, size=12):
        super().__init__()
        self.color = colors.HexColor(hex_code)
        self.size = size

    def wrap(self, *_):
        return self.size, self.size

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.setStrokeColor(INK)
        self.canv.setLineWidth(0.4)
        self.canv.rect(0, 0, self.size, self.size, stroke=1, fill=1)


# ----- Page decorations -----

def cover_page(c, doc):
    w, h = A4
    c.setFillColor(CREAM)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setStrokeColor(INK)
    c.setLineWidth(2.4)
    c.rect(1.5 * cm, 1.5 * cm, w - 3 * cm, h - 3 * cm, stroke=1, fill=0)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.8)
    c.rect(1.8 * cm, 1.8 * cm, w - 3.6 * cm, h - 3.6 * cm, stroke=1, fill=0)
    c.setFont("Times-Italic", 11)
    c.setFillColor(GOLD)
    c.drawCentredString(w / 2, h - 3 * cm, "EggCrown Studio")


def chapter_page(c, doc):
    w, h = A4
    c.setFillColor(CREAM)
    c.rect(0, 0, w, h, fill=1, stroke=0)
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.4)
    c.line(2 * cm, h - 2.2 * cm, w - 2 * cm, h - 2.2 * cm)
    c.line(2 * cm, 2.2 * cm, w - 2 * cm, 2.2 * cm)
    c.setFont("Times-Italic", 9)
    c.setFillColor(MUTED)
    c.drawString(2 * cm, h - 1.6 * cm, "Logo Design Guide 2026")
    c.drawRightString(w - 2 * cm, h - 1.6 * cm, "Trends · Colors · Typography")
    c.setFont("Times-Roman", 9)
    c.drawCentredString(w / 2, 1.5 * cm, f"— {doc.page} —")


# ----- Content builder -----

def build_content():
    story = []

    # Cover
    story.append(Spacer(1, 5 * cm))
    story.append(Paragraph("LOGO DESIGN", TITLE))
    story.append(Paragraph("GUIDE 2026", TITLE))
    story.append(Spacer(1, 0.5 * cm))
    story.append(HRule(14 * cm, thickness=1, color=GOLD))
    story.append(Spacer(1, 0.5 * cm))
    story.append(Paragraph(
        "Trends · Colors · Typography · Principles", SUBTITLE))
    story.append(Spacer(1, 4 * cm))
    story.append(Paragraph(
        "A complete reference for designing modern, "
        "memorable and timeless logos in 2026.",
        ParagraphStyle("CoverDesc", parent=BODY,
                       alignment=TA_CENTER, fontSize=11,
                       textColor=MUTED, leading=16)))
    story.append(PageBreak())

    # Table of Contents
    story.append(Paragraph("Contents", H1))
    story.append(HRule(15 * cm))
    toc_items = [
        ("01", "Foundations — Timeless Principles"),
        ("02", "Logo Categories & When to Use Each"),
        ("03", "2026 Style Trends"),
        ("04", "2026 Color Trends & Hex Codes"),
        ("05", "2026 Typography Trends"),
        ("06", "Composition, Grid & Negative Space"),
        ("07", "Workflow — From Brief to Delivery"),
        ("08", "Practical Checklist"),
        ("A",  "Appendix — Color Codes Reference"),
        ("B",  "Appendix — Sources"),
    ]
    toc_data = [[Paragraph(f"<b>{n}</b>", BODY),
                 Paragraph(t, BODY)] for n, t in toc_items]
    toc_table = Table(toc_data, colWidths=[1.5 * cm, 14 * cm])
    toc_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TEXTCOLOR", (0, 0), (0, -1), GOLD),
    ]))
    story.append(toc_table)
    story.append(PageBreak())

    # ===== Chapter 1 =====
    story.append(Paragraph("01 · Foundations", H1))
    story.append(Paragraph("Timeless Logo Principles", H2))
    story.append(HRule(15 * cm))
    story.append(Paragraph(
        "Trends will fade. Principles won't. The most enduring marks of the "
        "past century — Nike, Apple, FedEx, Chanel — share the same DNA. "
        "Master these eight principles before reaching for any 2026 trend.",
        BODY))

    principles = [
        ("Simplicity",
         "The fewer elements, the stronger the recall. A logo must work at "
         "16 px in a browser tab and at 5 m on a storefront. If you can't "
         "describe it in one sentence, simplify."),
        ("Distinctiveness",
         "Memorability lives in unexpected angles, hidden meaning or unique "
         "silhouette. The FedEx arrow, the Amazon smile, the Toblerone bear "
         "— they reward a second look."),
        ("Versatility",
         "One logo, many surfaces: favicon, embroidery, monochrome fax, "
         "neon sign. Always design in vector, always test in single-color, "
         "and at three sizes (24 px, 200 px, 1000 px)."),
        ("Color Psychology",
         "Color carries 60–80% of brand recognition (Pantone Institute). "
         "Choose based on emotion, not preference. Reds energize, blues "
         "calm, greens ground, golds elevate, blacks anchor."),
        ("Balanced Typography",
         "If your mark already speaks, your wordmark should whisper. "
         "Pair only two type weights at most. Letter-spacing matters more "
         "than the font choice."),
        ("Negative Space",
         "What's missing is what people remember. The white space between "
         "shapes is part of the design — treat it as a positive element."),
        ("Emotional Resonance",
         "A logo isn't art, it's a promise. Ask: what does the customer "
         "feel one second after seeing it? That feeling is the brand."),
        ("Avoid Fads",
         "If a trend is new today, it will look dated in 36 months. "
         "Use trends as flavor, not foundation. Anchor the design to "
         "geometry, proportion and meaning that have worked for centuries."),
    ]
    for title, desc in principles:
        story.append(Paragraph(title, H3))
        story.append(Paragraph(desc, BODY))
    story.append(PageBreak())

    # ===== Chapter 2 =====
    story.append(Paragraph("02 · Logo Categories", H1))
    story.append(Paragraph("Choose the right format before drawing a pixel", H2))
    story.append(HRule(15 * cm))

    categories = [
        ("Wordmark (Logotype)",
         "The brand name set in distinctive type — Google, Coca-Cola, "
         "FedEx, Visa.",
         "Strong brand name, short word, type-driven personality."),
        ("Lettermark (Monogram)",
         "Initials only — IBM, HBO, NASA, CNN, EC.",
         "Long company names, premium / heritage feel, seal-style brands."),
        ("Pictorial Mark (Iconic)",
         "A recognizable image — Apple's apple, Twitter's bird.",
         "Established brands, direct symbolic meaning."),
        ("Abstract Mark",
         "Geometric symbol with no literal meaning — Nike swoosh, Adidas, BP.",
         "Flexible meaning, future-proof, strong tech / fashion fit."),
        ("Mascot",
         "A character face or figure — KFC's Colonel, Pringles' Julius.",
         "Family-friendly, sport, food, retail with strong personality."),
        ("Combination Mark",
         "Symbol + wordmark, lockup-able — Adidas, Lacoste, Doritos.",
         "Most flexible; mark and word can also work alone."),
        ("Emblem / Badge / Seal",
         "Type integrated inside a contained shape — Starbucks, Harley, "
         "BMW, EggCrown's monogram seal.",
         "Heritage, food & drink, university, artisan, premium farm."),
    ]
    cat_data = [["Category", "Examples", "Best for"]]
    for n, e, w in categories:
        cat_data.append([Paragraph(f"<b>{n}</b>", BODY),
                         Paragraph(e, BODY),
                         Paragraph(w, BODY)])
    cat_table = Table(cat_data, colWidths=[4.5 * cm, 6 * cm, 5 * cm])
    cat_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), CREAM),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, 0), 0.6, GOLD),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CREAM, colors.white]),
    ]))
    story.append(cat_table)
    story.append(PageBreak())

    # ===== Chapter 3 =====
    story.append(Paragraph("03 · 2026 Style Trends", H1))
    story.append(Paragraph("What modern brands are reaching for", H2))
    story.append(HRule(15 * cm))

    trends = [
        ("Warm Minimalism",
         "Minimalism kept its quiet, lost its sterility. Soft curves replace "
         "harsh geometry; gentle fades replace stark contrasts. Approachable, "
         "human, premium-without-being-cold."),
        ("Gothic & Historic Influences",
         "Gothic letterforms, blackletter ornament and historic engraving "
         "give brands rooted, confident weight. Common in hospitality, "
         "indie spirits, fashion labels and heritage food."),
        ("Tactile & Artisanal Detail",
         "Fine-line engraving, hand-drawn marks, etched textures. Reads as "
         "premium, crafted, slow-made. Perfect for farm, bakery, distillery, "
         "ceramics, perfume."),
        ("Subtle 3D & Dimensional",
         "Logos return to depth — soft lighting, gentle gradients, single "
         "highlight. Not maximalist 3D, but a hint of physicality. Strong "
         "fit for tech, gaming, beauty."),
        ("Adaptive / Dynamic Logos",
         "One identity, many states. Logo shape, color or detail responds "
         "to platform, season, user, or context. Required of tech / "
         "media brands; nice-to-have everywhere else."),
        ("Retro Futurism",
         "70s–80s sci-fi nostalgia meets sleek modern execution. Curved "
         "sans-serifs, atomic shapes, sunset gradients. Strong in music, "
         "streaming, fitness, indie tech."),
        ("Circular Emblems & Badges",
         "Trust, lineage, terroir. Circular seal logos are returning "
         "fast — coffee roasters, cheesemakers, breweries, family farms, "
         "fashion ateliers."),
        ("Organic + Geometric Blends",
         "Fluid curves carrying movement, anchored by sharp geometric "
         "containers. Energy + stability in one mark."),
    ]
    for t, d in trends:
        story.append(Paragraph(t, H3))
        story.append(Paragraph(d, BODY))
    story.append(PageBreak())

    # ===== Chapter 4 =====
    story.append(Paragraph("04 · 2026 Color Trends", H1))
    story.append(Paragraph("Pantone, palettes & hex codes", H2))
    story.append(HRule(15 * cm))

    story.append(Paragraph("Pantone Color of the Year — Cloud Dancer", H3))
    story.append(Paragraph(
        "<b>PANTONE 11-4201 · #F0EEE9</b> — A soft, airy off-white sitting "
        "between warm and cool tones. The first white in 27 years from "
        "Pantone. It signals calm, clarity and creative spaciousness — and "
        "becomes the ideal background for logo work in 2026.", BODY))

    story.append(Paragraph("The Six Trending 2026 Palettes", H3))

    def palette_table(name, colors_list):
        rows = [[Paragraph(f"<b>{name}</b>", BODY), "", ""]]
        for hex_code, label, role in colors_list:
            rows.append([
                ColorSwatch(hex_code, size=14),
                Paragraph(f"<font name='Courier'>{hex_code}</font>", BODY),
                Paragraph(f"<b>{label}</b> — <i>{role}</i>", BODY),
            ])
        t = Table(rows, colWidths=[0.8 * cm, 2.6 * cm, 12 * cm])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BACKGROUND", (0, 0), (-1, 0), CLOUD),
            ("LINEBELOW", (0, 0), (-1, 0), 0.4, GOLD),
            ("SPAN", (0, 0), (-1, 0)),
        ]))
        return t

    palettes = [
        ("Warm Minimalism", [
            ("#F0EEE9", "Cloud Dancer", "Background / canvas"),
            ("#E8DCC4", "Warm Sand", "Secondary surface"),
            ("#C9A788", "Dusty Apricot", "Accent / mid-tone"),
            ("#7C6F5A", "Driftwood", "Body type"),
            ("#2C2A26", "Espresso", "Primary type"),
        ]),
        ("Nature / Farm-Fresh", [
            ("#F2E8D0", "Kraft Paper", "Background"),
            ("#A0B27D", "Sage Olive", "Foliage / freshness"),
            ("#8B5A2B", "Clay Brown", "Earth / wood"),
            ("#C8941F", "Honey Gold", "Highlight"),
            ("#3A2310", "Bark", "Primary type"),
        ]),
        ("Digital Contrast", [
            ("#D9E0CC", "Muted Olive", "Background"),
            ("#FF5A4D", "Electric Coral", "Accent"),
            ("#E5D7B3", "Sand Card", "Secondary surface"),
            ("#0C5664", "Deep Teal", "Primary type"),
            ("#0E1B26", "Ink Navy", "Anchor"),
        ]),
        ("Oceanic Biophilic", [
            ("#EEF4F4", "Foam White", "Background"),
            ("#9CC5C7", "Sea Glass", "Light accent"),
            ("#3F8C8E", "Turquoise", "Highlight"),
            ("#1B4F58", "Deep Lagoon", "Primary type"),
            ("#0A2730", "Abyss", "Anchor"),
        ]),
        ("Tech-Forward Neon", [
            ("#0E0E10", "Pitch", "Background"),
            ("#1B1F24", "Graphite", "Surface"),
            ("#D8FF3D", "Wasabi Chartreuse", "Signal accent"),
            ("#7E6BFF", "Iris", "Secondary accent"),
            ("#F2F2F2", "Pearl", "Type"),
        ]),
        ("Floral / Confident", [
            ("#FBF5F2", "Cream Petal", "Background"),
            ("#C9A6CF", "Burnished Lilac", "Accent"),
            ("#9B5F94", "Amethyst Orchid", "Mid-tone"),
            ("#E89154", "Mandarin", "Highlight"),
            ("#A24E2C", "Burnt Sienna", "Type"),
        ]),
    ]
    for name, lst in palettes:
        story.append(palette_table(name, lst))
        story.append(Spacer(1, 6))
    story.append(PageBreak())

    # Color psychology
    story.append(Paragraph("Color Psychology Cheat Sheet", H3))
    psych_rows = [["Color", "Conveys", "Caution"]]
    psych_data = [
        ("Red",   "Energy · appetite · urgency",       "Avoid for trust-led brands"),
        ("Orange","Warmth · friendly · creativity",    "Can read cheap if oversaturated"),
        ("Yellow","Optimism · attention · sun",        "Hard to read on white"),
        ("Green", "Growth · nature · health",          "Avoid muddy mid-greens"),
        ("Blue",  "Trust · calm · authority",          "Saturated by tech industry"),
        ("Purple","Luxury · imagination · premium",    "Strong gender associations"),
        ("Pink",  "Care · approachable · modern",      "Avoid bubblegum tones"),
        ("Brown", "Earth · craft · heritage",          "Can feel dated"),
        ("Black", "Power · luxury · timeless",         "Cold without warm accents"),
        ("White", "Clarity · openness · purity",       "Needs structural support"),
        ("Gold",  "Premium · achievement · warmth",    "Use as accent only"),
    ]
    for r in psych_data:
        psych_rows.append([Paragraph(f"<b>{r[0]}</b>", BODY),
                           Paragraph(r[1], BODY),
                           Paragraph(r[2], SMALL)])
    psych_table = Table(psych_rows, colWidths=[3 * cm, 7 * cm, 5.5 * cm])
    psych_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), CREAM),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CREAM, colors.white]),
    ]))
    story.append(psych_table)
    story.append(PageBreak())

    # ===== Chapter 5 =====
    story.append(Paragraph("05 · 2026 Typography Trends", H1))
    story.append(Paragraph("Fonts that read as 'now'", H2))
    story.append(HRule(15 * cm))

    typo = [
        ("Chunky / Juicy Serifs",
         "Serif revival in bold form: high contrast, sharp wedge serifs, "
         "playful weight. Eventbrite's 2024 rebrand was the bellwether. "
         "Try: <i>Tiempos, Recoleta, Domaine, Chunkfive, Boldonse.</i>"),
        ("The Italic Moment",
         "Italics step out of supporting roles into hero positions: liquid, "
         "loopy, full of personality. Reads literary, editorial, cinematic. "
         "Try: <i>Migra Italic, Editorial New Italic, Antarctica.</i>"),
        ("Quiet, Nuanced Sans-Serifs",
         "Geometric sans-serifs with character in small details — "
         "alternate terminals, optical sizes, soft corners. "
         "Try: <i>General Sans, Söhne, Inter Display, Nohemi.</i>"),
        ("Italian-Inspired & Editorial",
         "Wide caps, high contrast, condensed lockups — vintage Italian "
         "magazine energy. Try: <i>Migra, Editorial New, Reckless, "
         "PP Editorial.</i>"),
        ("Type as Graphic",
         "Letters become the design — oversized, cropped, intersecting "
         "shapes, used as containers themselves. Best when the wordmark "
         "is the brand's core mark."),
        ("Cute & Cosy",
         "Rounded geometric sans, soft serifs, hand-leanings. Strong fit "
         "for kids, food, wellness, indie. "
         "Try: <i>Coolvetica, Recoleta, Nunito, Marsden.</i>"),
        ("Monospace & Technical",
         "Engineering aesthetic for AI/tech brands. Try: <i>JetBrains Mono, "
         "Berkeley Mono, IBM Plex Mono.</i>"),
    ]
    for t, d in typo:
        story.append(Paragraph(t, H3))
        story.append(Paragraph(d, BODY))
    story.append(PageBreak())

    # ===== Chapter 6 =====
    story.append(Paragraph("06 · Composition & Grid", H1))
    story.append(Paragraph("Math behind beauty", H2))
    story.append(HRule(15 * cm))

    story.append(Paragraph("The Golden Ratio (φ ≈ 1.618)", H3))
    story.append(Paragraph(
        "Used in art and architecture for 2,500 years. In logo work, it "
        "defines proportional relationships between circles, rectangles "
        "and curves that the human eye reads as 'right'. Apple, Twitter, "
        "Google, Adobe, Pepsi — all built on φ-derived grids.", BODY))

    story.append(Paragraph("How to use it in practice", H3))
    story.append(Paragraph(
        "1. Start with a master circle (radius = R). <br/>"
        "2. Place the next supporting circle at radius R / 1.618. <br/>"
        "3. Continue dividing — each step yields a visually balanced "
        "child element. <br/>"
        "4. Letters, counters and curves built on this skeleton "
        "feel structurally inevitable.",
        BODY))

    story.append(Paragraph("Negative Space — design what's missing", H3))
    story.append(Paragraph(
        "Treat the empty area as a positive shape. The FedEx arrow, the "
        "Toblerone bear, the WWF panda — what's <i>not</i> there carries "
        "the meaning. Always check your logo against its inverted version: "
        "if the negative shape is ugly, the positive shape isn't done yet.",
        BODY))

    story.append(Paragraph("The 4-zoom test", H3))
    story.append(Paragraph(
        "Before signing off, view your logo at: <b>16 px</b> (browser tab), "
        "<b>72 px</b> (mobile app icon), <b>400 px</b> (web hero), "
        "<b>2000 px</b> (billboard). It must hold up at every size, in "
        "color, monochrome and inverted.", BODY))
    story.append(PageBreak())

    # ===== Chapter 7 =====
    story.append(Paragraph("07 · Workflow", H1))
    story.append(Paragraph("From brief to delivery in eight steps", H2))
    story.append(HRule(15 * cm))

    workflow = [
        ("1. Brief & Discovery",
         "Capture brand promise, audience, competitors, three adjectives "
         "the logo must convey, three it must avoid."),
        ("2. Research & Mood Board",
         "30+ logos in the same category. Identify clichés to avoid and "
         "white-space opportunities."),
        ("3. Concept Sketches",
         "20+ sketches by hand, no software. Quantity unlocks quality."),
        ("4. Refine Top 3",
         "Tighten silhouettes, test typography pairings."),
        ("5. Vector Build",
         "Reconstruct in Illustrator / Figma / SVG with golden-ratio grid. "
         "Every curve placed deliberately, every node minimized."),
        ("6. Variant System",
         "Full color · single-color (positive) · single-color (reversed) · "
         "horizontal lockup · vertical lockup · favicon (16 px stripped)."),
        ("7. Test in Context",
         "Mockups: business card, packaging, website nav, embroidery, "
         "favicon, billboard. Reject anything that breaks."),
        ("8. Deliver",
         "Master vector (SVG / AI), production formats (PNG @1x, @2x, "
         "@3x; PDF), brand book (clear-space rules, minimum sizes, "
         "do/don't, color codes in HEX/RGB/CMYK/Pantone)."),
    ]
    for t, d in workflow:
        story.append(Paragraph(t, H3))
        story.append(Paragraph(d, BODY))
    story.append(PageBreak())

    # ===== Chapter 8 =====
    story.append(Paragraph("08 · Practical Checklist", H1))
    story.append(Paragraph("Before you ship", H2))
    story.append(HRule(15 * cm))

    checklist = [
        "Logo is recognizable at 16 px (favicon).",
        "Logo works in pure black on white.",
        "Logo works in pure white on black.",
        "Negative shape is intentional and balanced.",
        "Typography is custom or modified — not default.",
        "Colors have hex / RGB / CMYK / Pantone defined.",
        "Color contrast passes WCAG AA against intended backgrounds.",
        "Vector file has no rasterized elements.",
        "Curves are smooth (no kinked Bézier handles).",
        "Anchor points are minimized (each curve uses ≤ 4 points).",
        "Mark is registered or trademark search clear.",
        "Brand book covers clear space, min sizes, do/don't.",
        "Delivered in: SVG, PDF, PNG (1x/2x/3x), AI, EPS.",
        "File names are normalized (e.g. brand-logo-color-light.svg).",
        "Stakeholders signed off on a printed proof, not just a screen.",
    ]
    for item in checklist:
        story.append(Paragraph(f"☐  {item}", BODY))
    story.append(PageBreak())

    # ===== Appendix A =====
    story.append(Paragraph("Appendix A · Color Codes Reference", H1))
    story.append(HRule(15 * cm))
    story.append(Paragraph(
        "Quick-reference table of every color cited in this guide.", ITALIC))
    ref_rows = [["", "HEX", "Name", "Best Use"]]
    ref_colors = [
        ("#F0EEE9", "Cloud Dancer (Pantone 2026)", "Backgrounds"),
        ("#FAF7F0", "Cream Ivory", "Premium backgrounds"),
        ("#F2E8D0", "Kraft Paper", "Rustic / farm"),
        ("#E8DCC4", "Warm Sand", "Secondary surface"),
        ("#C9A788", "Dusty Apricot", "Warm accent"),
        ("#A0B27D", "Sage Olive", "Nature / wellness"),
        ("#8B5A2B", "Clay Brown", "Earth / heritage"),
        ("#3A2310", "Bark", "Primary text"),
        ("#C8941F", "Honey Gold", "Premium accent"),
        ("#E9B848", "Light Gold", "Highlight"),
        ("#FF5A4D", "Electric Coral", "Tech accent"),
        ("#0C5664", "Deep Teal", "Primary text"),
        ("#3F8C8E", "Turquoise", "Biophilic accent"),
        ("#1B4F58", "Deep Lagoon", "Primary text"),
        ("#D8FF3D", "Wasabi Chartreuse", "Tech / signal"),
        ("#7E6BFF", "Iris", "Tech accent"),
        ("#C9A6CF", "Burnished Lilac", "Floral accent"),
        ("#9B5F94", "Amethyst Orchid", "Confident mid-tone"),
        ("#E89154", "Mandarin Orange", "Vibrant highlight"),
        ("#A24E2C", "Burnt Sienna", "Earthy text"),
        ("#1B1B1B", "Ink", "Primary text"),
        ("#0E0E10", "Pitch", "Tech background"),
        ("#FFFFFF", "Pure White", "Universal"),
    ]
    for hex_code, name, use in ref_colors:
        ref_rows.append([
            ColorSwatch(hex_code, size=14),
            Paragraph(f"<font name='Courier'>{hex_code}</font>", BODY),
            Paragraph(name, BODY),
            Paragraph(use, SMALL),
        ])
    ref_table = Table(ref_rows,
                      colWidths=[0.8 * cm, 2.6 * cm, 6 * cm, 6 * cm])
    ref_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), CREAM),
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, CREAM]),
    ]))
    story.append(ref_table)
    story.append(PageBreak())

    # ===== Appendix B =====
    story.append(Paragraph("Appendix B · Sources", H1))
    story.append(HRule(15 * cm))
    story.append(Paragraph(
        "All sources consulted in May 2026 to compile this guide.", ITALIC))
    sources = [
        "Pantone — Color of the Year 2026: Cloud Dancer (PANTONE 11-4201). "
        "pantone.com/color-of-the-year/2026",
        "Vistaprint — 10 Logo Design Trends for 2026. "
        "vistaprint.com/hub/logo-design-trends",
        "Shopify — 7 Logo Trends for 2026. shopify.com/blog/logo-trends",
        "Wix — 8 Logo Design Trends for 2026. wix.com/blog/logo-design-trends",
        "DigitalSynopsis — Top 10 Logo Design Trends for 2026.",
        "Kittl — Logo Design Trends 2026. kittl.com/blogs/logo-design-trends-2026",
        "Adobe Express — Color of the Year Trends for 2026.",
        "Coloro × WGSN — Color forecast 2026.",
        "Creative Boom — 50 fonts for 2026. creativeboom.com/resources/top-50-fonts-in-2026",
        "Creative Bloq — Top typography trends for 2026.",
        "Fontfabric — Top 10 Typography Trends for 2026.",
        "Envato — Font Trends 2026.",
        "I Love Typography — 10 Must-have Typefaces for 2026.",
        "Figma — The Golden Ratio resource library.",
        "Inkbot Design — Golden Ratio in Graphic Design 2026 Practical Guide.",
        "TheLogoCreative — 10 Timeless Logo Design Principles.",
        "Stone Group — 10 Timeless Principles of Effective Logo Design.",
        "Canva Learn — Logo Design Principles.",
    ]
    for s in sources:
        story.append(Paragraph(f"• {s}", SMALL))
        story.append(Spacer(1, 2))

    story.append(Spacer(1, 1.2 * cm))
    story.append(HRule(15 * cm))
    story.append(Paragraph(
        "Compiled May 2026 · for internal & educational use.", CAPTION))

    return story


def build():
    doc = SimpleDocTemplate(
        OUTPUT,
        pagesize=A4,
        leftMargin=2.2 * cm,
        rightMargin=2.2 * cm,
        topMargin=2.6 * cm,
        bottomMargin=2.4 * cm,
        title="Logo Design Guide 2026",
        author="EggCrown Studio",
        subject="Logo design trends, colors, typography & principles for 2026",
        creator="reportlab",
    )
    doc.build(build_content(),
              onFirstPage=cover_page,
              onLaterPages=chapter_page)
    print(f"PDF written to {OUTPUT}")


if __name__ == "__main__":
    build()
