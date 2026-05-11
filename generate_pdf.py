# -*- coding: utf-8 -*-
"""
PDF coaching personnalisé pour Marien — v2 avec schémas visuels.
"""

import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Flowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ---------- FONTS ----------
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Italic", "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Serif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Serif-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold", italic="DejaVu-Italic")

# ---------- COULEURS ----------
GOLD       = HexColor("#D4AF37")
GOLD_SOFT  = HexColor("#B8962E")
GOLD_PALE  = HexColor("#F2E5B4")
DARK_BG    = HexColor("#1A1A1A")
DARK_GREY  = HexColor("#2A2A2A")
MID_GREY   = HexColor("#5A5A5A")
LIGHT_GREY = HexColor("#E8E8E8")
TEXT       = HexColor("#1A1A1A")
RED_ACC    = HexColor("#B33A3A")
RED_SOFT   = HexColor("#E8B5B5")
GREEN      = HexColor("#2D5016")
GREEN_SOFT = HexColor("#B5D8A0")
PURPLE     = HexColor("#3A2A4A")
CREAM      = HexColor("#F8F4EC")
BLUE_SOFT  = HexColor("#A8C5D8")

# ---------- STYLES ----------
body = ParagraphStyle("body", fontName="DejaVu", fontSize=10.5, leading=15,
    textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=8)
body_center = ParagraphStyle("body_center", parent=body, alignment=TA_CENTER)
body_white = ParagraphStyle("body_white", parent=body, textColor=white)
body_dark = ParagraphStyle("body_dark", parent=body, textColor=DARK_BG)
body_italic = ParagraphStyle("body_italic", parent=body, fontName="DejaVu-Italic")

cell_st = ParagraphStyle("cell", fontName="DejaVu", fontSize=9.3, leading=12.5,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=0)
cell_bold = ParagraphStyle("cell_bold", parent=cell_st, fontName="DejaVu-Bold")
cell_gold = ParagraphStyle("cell_gold", parent=cell_st, fontName="DejaVu-Bold", textColor=GOLD)
cell_white = ParagraphStyle("cell_white", parent=cell_st, textColor=white)

h_chapter = ParagraphStyle("h_chapter", fontName="DejaVu-Serif-Bold", fontSize=22, leading=26,
    textColor=GOLD, alignment=TA_LEFT, spaceAfter=4)
h_chapter_sub = ParagraphStyle("h_chapter_sub", fontName="DejaVu-Italic", fontSize=12, leading=15,
    textColor=MID_GREY, alignment=TA_LEFT, spaceAfter=18)
h_section = ParagraphStyle("h_section", fontName="DejaVu-Bold", fontSize=13.5, leading=17,
    textColor=GOLD_SOFT, alignment=TA_LEFT, spaceBefore=12, spaceAfter=8)
cover_title = ParagraphStyle("cover_title", fontName="DejaVu-Serif-Bold", fontSize=42, leading=46,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10)
cover_sub = ParagraphStyle("cover_sub", fontName="DejaVu-Italic", fontSize=18, leading=22,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=80)
cover_for = ParagraphStyle("cover_for", fontName="DejaVu", fontSize=14, leading=18,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=4)
cover_name = ParagraphStyle("cover_name", fontName="DejaVu-Serif-Bold", fontSize=32, leading=38,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=80)
cover_quote = ParagraphStyle("cover_quote", fontName="DejaVu-Italic", fontSize=14, leading=20,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10)
callout_label = ParagraphStyle("callout_label", fontName="DejaVu-Bold", fontSize=10.5, leading=13,
    textColor=white, alignment=TA_LEFT, spaceAfter=6)
callout_label_dark = ParagraphStyle("callout_label_dark", parent=callout_label, textColor=DARK_BG)
callout_body = ParagraphStyle("callout_body", fontName="DejaVu", fontSize=10.3, leading=14.5,
    textColor=white, alignment=TA_JUSTIFY, spaceAfter=6)
callout_body_dark = ParagraphStyle("callout_body_dark", parent=callout_body, textColor=DARK_BG)
pull_quote = ParagraphStyle("pull_quote", fontName="DejaVu-Italic", fontSize=13, leading=18,
    textColor=GOLD_SOFT, alignment=TA_CENTER, spaceBefore=10, spaceAfter=14,
    leftIndent=30, rightIndent=30)
phase_title = ParagraphStyle("phase_title", fontName="DejaVu-Serif-Bold", fontSize=18, leading=22,
    textColor=GOLD, alignment=TA_LEFT, spaceBefore=14, spaceAfter=10)
small_label = ParagraphStyle("small_label", fontName="DejaVu-Bold", fontSize=9.5, leading=12,
    textColor=GOLD_SOFT, alignment=TA_LEFT, spaceAfter=2)
diagram_caption = ParagraphStyle("diagram_caption", fontName="DejaVu-Italic", fontSize=9, leading=12,
    textColor=MID_GREY, alignment=TA_CENTER, spaceBefore=4, spaceAfter=12)


# ---------- HELPERS ----------
def P(text, style=None):
    return Paragraph(text, style or body)

def C(text, style=None):
    """Cell wrapper — text becomes wrapping Paragraph for table cells."""
    return Paragraph(text, style or cell_st)


# ---------- CALLOUT ----------
def make_callout(label, text, bg, fg):
    label_style = callout_label if fg == white else callout_label_dark
    body_style = callout_body if fg == white else callout_body_dark
    inner = [Paragraph(label, label_style)]
    if isinstance(text, list):
        for t in text:
            inner.append(Paragraph(t, body_style))
    else:
        inner.append(Paragraph(text, body_style))
    t = Table([[inner]], colWidths=[16 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 3, GOLD),
    ]))
    return [Spacer(1, 6), t, Spacer(1, 10)]

def concept(text): return make_callout("◆  LE CONCEPT", text, DARK_GREY, white)
def miroir(text):  return make_callout("◈  TON MIROIR", text, GOLD, DARK_BG)
def action(text):  return make_callout("▶  ACTION CONCRÈTE", text, GREEN, white)
def journal(text): return make_callout("?  POUR TON JOURNAL", text, PURPLE, white)
def warning(text): return make_callout("!  VÉRITÉ BRUTALE", text, RED_ACC, white)

def hougaard_block(text):
    inner = [Paragraph("◇  CE QUE DIT HOUGAARD", small_label)]
    if isinstance(text, list):
        for t in text:
            inner.append(Paragraph(t, body))
    else:
        inner.append(Paragraph(text, body))
    t = Table([[inner]], colWidths=[16 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD_SOFT),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 10)]


# ---------- SCHEMAS / DIAGRAMS ----------
class Schema(Flowable):
    """Base flowable for canvas-drawn diagrams."""
    def __init__(self, height, draw_func, width=16*cm):
        super().__init__()
        self.height = height
        self.width = width
        self.draw_func = draw_func
    def wrap(self, *args):
        return self.width, self.height
    def draw(self):
        self.draw_func(self.canv, self.width, self.height)


class GoldRule(Flowable):
    def __init__(self, width=16 * cm, thickness=1.2, color=GOLD):
        super().__init__()
        self.width = width
        self.thickness = thickness
        self.color = color
        self.height = thickness + 4
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


def _arrow(c, x1, y1, x2, y2, color=GOLD, lw=1.4, head=5):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(lw)
    c.line(x1, y1, x2, y2)
    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx*dx + dy*dy) or 1
    ux, uy = dx/d, dy/d
    px, py = -uy, ux
    p1 = (x2 - head*ux + head*0.5*px, y2 - head*uy + head*0.5*py)
    p2 = (x2 - head*ux - head*0.5*px, y2 - head*uy - head*0.5*py)
    c.setStrokeColor(color)
    path = c.beginPath()
    path.moveTo(x2, y2)
    path.lineTo(*p1)
    path.lineTo(*p2)
    path.close()
    c.drawPath(path, fill=1, stroke=1)


def _draw_text_box(c, x, y, w, h, title, body_text=None, bg=DARK_GREY,
                   title_color=GOLD, body_color=white, title_size=8.5, body_size=7.5,
                   align="left", radius=4):
    c.setFillColor(bg)
    c.setStrokeColor(bg)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=0)
    c.setFillColor(title_color)
    c.setFont("DejaVu-Bold", title_size)
    if align == "center":
        c.drawCentredString(x + w/2, y + h - title_size - 4, title)
    else:
        c.drawString(x + 8, y + h - title_size - 4, title)
    if body_text:
        c.setFillColor(body_color)
        c.setFont("DejaVu", body_size)
        lines = body_text.split("\n")
        line_y = y + 8
        for line in reversed(lines):
            if align == "center":
                c.drawCentredString(x + w/2, line_y, line)
            else:
                c.drawString(x + 8, line_y, line)
            line_y += body_size + 2


# ---------- SCHEMA: 4 FORCES PSY (Ch 3) ----------
def draw_4_forces(c, w, h):
    cx, cy = w/2, h/2
    r = 1.4 * cm
    c.setFillColor(GOLD)
    c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillColor(DARK_BG)
    c.setFont("DejaVu-Bold", 10)
    c.drawCentredString(cx, cy + 4, "TOI")
    c.setFont("DejaVu", 8.5)
    c.drawCentredString(cx, cy - 8, "EN TRADE")

    box_w, box_h = 5.2*cm, 1.6*cm
    positions = [
        (0.4*cm,                  cy + 1.4*cm,        "BESOIN D'AVOIR RAISON", "L'ego refuse d'être contredit\npar un SL touché"),
        (w - box_w - 0.4*cm,      cy + 1.4*cm,        "AVERSION À LA PERTE",   "Kahneman : perdre fait\n2x plus mal que gagner"),
        (0.4*cm,                  cy - 1.4*cm - box_h, "BESOIN DE CERTITUDE",  "Le cerveau refuse l'aléa\ninvente du « je suis sûr »"),
        (w - box_w - 0.4*cm,      cy - 1.4*cm - box_h, "PROJECTION ÉMOTIONNELLE","Tu vois sur le chart\nce que tu veux voir"),
    ]
    for bx, by, title, sub in positions:
        _draw_text_box(c, bx, by, box_w, box_h, title, sub, bg=DARK_GREY, title_color=GOLD)
        bcx, bcy = bx + box_w/2, by + box_h/2
        dx, dy = cx - bcx, cy - bcy
        d = math.sqrt(dx*dx + dy*dy)
        ux, uy = dx/d, dy/d
        sx = bcx + ux*(box_w/2 - 4) if abs(ux) > abs(uy) else bcx + ux*(box_h/2 + 2)
        sy = bcy + uy*(box_h/2 - 4) if abs(uy) >= abs(ux) else bcy + uy*(box_h/2 + 2)
        ex, ey = cx - ux*r, cy - uy*r
        _arrow(c, bcx + ux*box_w*0.35, bcy + uy*box_h*0.45, ex, ey, color=RED_ACC, lw=1.3, head=5)


# ---------- SCHEMA: 80/20 BAR (Ch 4) ----------
def draw_80_20(c, w, h):
    bar_h = 1.3 * cm
    bar_y = h/2 - bar_h/2
    c.setFillColor(RED_ACC)
    c.rect(0, bar_y, 0.8*w, bar_h, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(0.8*w, bar_y, 0.2*w, bar_h, fill=1, stroke=0)
    c.setFont("DejaVu-Bold", 13)
    c.setFillColor(white)
    c.drawCentredString(0.4*w, bar_y + bar_h/2 - 4, "80 %  PERDENT")
    c.drawCentredString(0.9*w, bar_y + bar_h/2 - 4, "20 %")
    c.setFont("DejaVu", 8.5)
    c.setFillColor(DARK_BG)
    c.drawCentredString(0.4*w, bar_y + bar_h + 8, "Là où sont les traders retail — toi inclus aujourd'hui")
    c.drawCentredString(0.9*w, bar_y + bar_h + 8, "La sortie")
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8)
    c.drawCentredString(w/2, bar_y - 14, "Source : rapports publics des brokers et régulateurs européens (AMF, ESMA).")


# ---------- SCHEMA: +1500 PATTERN (Ch 7) ----------
def draw_1500_pattern(c, w, h):
    margin_l, margin_r = 1*cm, 0.5*cm
    margin_b, margin_t = 1.2*cm, 0.8*cm
    plot_w = w - margin_l - margin_r
    plot_h = h - margin_b - margin_t
    x0 = margin_l
    y0 = margin_b
    # axis
    c.setStrokeColor(MID_GREY)
    c.setLineWidth(0.5)
    c.line(x0, y0, x0 + plot_w, y0)
    c.line(x0, y0, x0, y0 + plot_h)
    # zero line
    zero_y = y0 + plot_h * 0.45
    c.setStrokeColor(LIGHT_GREY)
    c.line(x0, zero_y, x0 + plot_w, zero_y)
    c.setFont("DejaVu", 7.5)
    c.setFillColor(MID_GREY)
    c.drawString(x0 - 18, zero_y - 2, "0")
    c.drawString(x0 - 26, y0 + plot_h - 6, "+1500")
    c.drawString(x0 - 26, y0 + 4, "-800")
    # curve points (t in [0..1], pnl in [-1..1])
    pts = [
        (0.00, 0.00),   # entry
        (0.18, 0.45),   # +800
        (0.30, 0.95),   # +1500 (peak)
        (0.42, 0.70),
        (0.55, 0.35),
        (0.68, 0.00),
        (0.78, -0.35),  # SL touched, but décale
        (0.88, -0.65),
        (1.00, -0.95),  # compte cramé
    ]
    def px(t): return x0 + t * plot_w
    def py(v): return zero_y + v * (plot_h * 0.50)
    c.setStrokeColor(GOLD)
    c.setLineWidth(1.8)
    path = c.beginPath()
    path.moveTo(px(pts[0][0]), py(pts[0][1]))
    for t, v in pts[1:]:
        path.lineTo(px(t), py(v))
    c.drawPath(path, stroke=1, fill=0)
    # markers
    markers = [
        (pts[0], "Entrée XAUUSD",        "Calme, plan clair",      GREEN),
        (pts[1], "+800 — Dopamine ON",   "« ça monte, je tiens »", GOLD_SOFT),
        (pts[2], "+1500 — Préfrontal OFF","Tu es passager",        RED_ACC),
        (pts[5], "Retour à 0",           "« ça va repartir »",     RED_ACC),
        (pts[6], "SL touché → décalé",   "Acte autodestructeur",   RED_ACC),
        (pts[8], "Compte cramé",         "Game over",              DARK_BG),
    ]
    for (t, v), lab, sub, col in markers:
        x, y = px(t), py(v)
        c.setFillColor(col)
        c.circle(x, y, 3.5, fill=1, stroke=0)
        c.setFillColor(DARK_BG)
        c.setFont("DejaVu-Bold", 7.5)
        ly = y + 8 if v > 0 else y - 14
        c.drawCentredString(x, ly, lab)
        c.setFillColor(MID_GREY)
        c.setFont("DejaVu-Italic", 7)
        c.drawCentredString(x, ly - 9, sub)
    # axis labels
    c.setFont("DejaVu-Italic", 8)
    c.setFillColor(MID_GREY)
    c.drawString(x0, y0 - 14, "temps →")
    c.saveState()
    c.translate(x0 - 32, y0 + plot_h/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "PnL")
    c.restoreState()


# ---------- SCHEMA: DOPAMINE CYCLE (Ch 7) ----------
def draw_dopamine_cycle(c, w, h):
    cx, cy = w/2, h/2
    R = min(w, h) * 0.30
    node_r = 0.32 * cm
    # circle
    c.setStrokeColor(GOLD)
    c.setLineWidth(0.8)
    c.circle(cx, cy, R, fill=0, stroke=1)
    nodes = [
        ("1. ANTICIPATION",   "« et si je trade ? »",       90),
        ("2. CLIC / TRADE",   "ouverture de position",       30),
        ("3. PIC DOPAMINE",   "PnL bouge en ma faveur",     -30),
        ("4. CRASH",          "PnL reverse ou SL touché",   -90),
        ("5. BESOIN DE PLUS", "« je me refais »",          -150),
        ("6. RECHERCHE SETUP","scan compulsif du chart",    150),
    ]
    pts = []
    for label, sub, deg in nodes:
        rad = math.radians(deg)
        x = cx + R * math.cos(rad)
        y = cy + R * math.sin(rad)
        pts.append((x, y, label, sub, deg))
    # arrows between consecutive (raccourcies par rayon de noeud)
    for i in range(len(pts)):
        x1, y1, _, _, _ = pts[i]
        x2, y2, _, _, _ = pts[(i + 1) % len(pts)]
        dx, dy = x2 - x1, y2 - y1
        d = math.sqrt(dx*dx + dy*dy)
        ux, uy = dx/d, dy/d
        _arrow(c, x1 + ux*node_r*1.4, y1 + uy*node_r*1.4,
               x2 - ux*node_r*1.4, y2 - uy*node_r*1.4,
               color=GOLD_SOFT, lw=1.0, head=4.5)
    # nodes + labels OUTSIDE
    for x, y, label, sub, deg in pts:
        # node circle
        c.setFillColor(DARK_BG)
        c.circle(x, y, node_r, fill=1, stroke=0)
        c.setStrokeColor(GOLD); c.setLineWidth(1)
        c.circle(x, y, node_r, fill=0, stroke=1)
        # label positioned bien hors du cercle gold ring (R = 0.30*min(w,h))
        # Pour les angles horizontaux (30°, -30°, 150°, -150°) on pousse + à l'horizontal
        # Pour les angles verticaux (90°, -90°) le label monte/descend
        is_horizontal = abs(deg) in (30, 150)
        if is_horizontal:
            # offset horizontal large pour dégager le ring
            lx = x + (1 if deg > -90 and deg < 90 else -1) * 1.6*cm
            ly = y
            anchor = "left" if deg > -90 and deg < 90 else "right"
        else:
            # angle vertical : label centré sur x, décalé en y
            lx = x
            ly = y + (1 if deg == 90 else -1) * 1.0*cm
            anchor = "center"
        c.setFillColor(DARK_BG)
        c.setFont("DejaVu-Bold", 8.5)
        if anchor == "center":
            c.drawCentredString(lx, ly + 3, label)
        elif anchor == "left":
            c.drawString(lx, ly + 3, label)
        else:
            c.drawRightString(lx, ly + 3, label)
        c.setFillColor(MID_GREY)
        c.setFont("DejaVu-Italic", 7.5)
        if anchor == "center":
            c.drawCentredString(lx, ly - 9, sub)
        elif anchor == "left":
            c.drawString(lx, ly - 9, sub)
        else:
            c.drawRightString(lx, ly - 9, sub)
    # center text
    c.setFillColor(GOLD)
    c.setFont("DejaVu-Serif-Bold", 11)
    c.drawCentredString(cx, cy + 5, "BOUCLE")
    c.drawCentredString(cx, cy - 8, "DOPAMINE")


# ---------- SCHEMA: THERMOSTAT FINANCIER (Ch 8) ----------
def draw_thermostat(c, w, h):
    # title centré en haut
    c.setFillColor(DARK_BG)
    c.setFont("DejaVu-Bold", 12)
    c.drawCentredString(w/2, h - 16, "TON THERMOSTAT FINANCIER")
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 9)
    c.drawCentredString(w/2, h - 32, "le sabotage est mécanique, pas moral")

    # thermomètre vertical — placé à gauche-centre
    tx = 4.2*cm
    ty = 1.4*cm
    th = h - 3.6*cm
    tw = 1.4*cm
    c.setStrokeColor(DARK_GREY); c.setLineWidth(1)
    c.roundRect(tx, ty, tw, th, 8, fill=0, stroke=1)
    bands = [
        (0.0, 0.30, GREEN_SOFT),
        (0.30, 0.55, GOLD_PALE),
        (0.55, 0.80, GOLD),
        (0.80, 1.0, RED_ACC),
    ]
    for lo, hi, col in bands:
        c.setFillColor(col)
        c.rect(tx + 2, ty + 2 + lo*(th-4), tw - 4, (hi - lo)*(th-4), fill=1, stroke=0)

    # zone labels à gauche du thermomètre
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8)
    for ratio, lbl in [(0.90, "danger"), (0.65, "inconfort"), (0.42, "tolérable"), (0.15, "confort")]:
        c.drawRightString(tx - 10, ty + ratio * th - 3, lbl)

    # ceiling marker — annotations à droite
    ceiling_y = ty + 0.80 * th
    c.setStrokeColor(RED_ACC); c.setLineWidth(1.4)
    c.line(tx + tw, ceiling_y, tx + tw + 20, ceiling_y)
    c.setFillColor(RED_ACC)
    c.setFont("DejaVu-Bold", 10)
    c.drawString(tx + tw + 26, ceiling_y - 3, "PLAFOND")
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8)
    c.drawString(tx + tw + 26, ceiling_y - 15, "zone du sabotage  (+1500)")

    # baseline marker — annotations à droite
    base_y = ty + 0.30 * th
    c.setStrokeColor(DARK_BG); c.setLineWidth(1.4)
    c.line(tx + tw, base_y, tx + tw + 20, base_y)
    c.setFillColor(DARK_BG)
    c.setFont("DejaVu-Bold", 10)
    c.drawString(tx + tw + 26, base_y - 3, "BASELINE")
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8)
    c.drawString(tx + tw + 26, base_y - 15, "ton « normal pour moi »")

    # arrow rouge à l'intérieur du thermo (force de retour)
    _arrow(c, tx + tw/2, ceiling_y - 0.3*cm, tx + tw/2, base_y + 0.4*cm,
           color=DARK_BG, lw=1.4, head=6)

    # caption en bas centré
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8.5)
    c.drawCentredString(w/2, ty - 0.5*cm,
        "Tout profit qui dépasse le plafond est repris. Mécaniquement.")


# ---------- SCHEMA: SL ESCALATOR (Ch 12) ----------
def draw_sl_escalator(c, w, h):
    # 4 steps ascending
    n = 4
    pad = 0.4*cm
    step_w = (w - 2*pad) / n
    base_h = h - 1.4*cm
    titles = [
        ("NIVEAU 1", "SL placé\navec l'entrée", "Non négociable"),
        ("NIVEAU 2", "Alerte sonore\nau SL", "Anticipation déclenchée"),
        ("NIVEAU 3", "Engagement signé\nau mur", "Conscience activée"),
        ("NIVEAU 4", "Close the\nplatform", "Tu disparais"),
    ]
    for i in range(n):
        x = pad + i * step_w
        sh = (i + 1) * (base_h / n)
        y = 0.8*cm
        col = [GREEN_SOFT, GOLD_PALE, GOLD, GOLD_SOFT][i]
        c.setFillColor(col)
        c.setStrokeColor(DARK_BG)
        c.setLineWidth(0.6)
        c.rect(x, y, step_w - 4, sh, fill=1, stroke=1)
        ttl, mid, sub = titles[i]
        c.setFillColor(DARK_BG)
        c.setFont("DejaVu-Bold", 9)
        c.drawCentredString(x + step_w/2 - 2, y + sh - 14, ttl)
        c.setFont("DejaVu", 8)
        for k, line in enumerate(mid.split("\n")):
            c.drawCentredString(x + step_w/2 - 2, y + sh - 28 - k*10, line)
        c.setFillColor(MID_GREY)
        c.setFont("DejaVu-Italic", 7.5)
        c.drawCentredString(x + step_w/2 - 2, y + sh - 50, sub)
    # arrow going up
    _arrow(c, pad + 0.2*cm, 0.4*cm, w - pad - 0.2*cm, 0.4*cm, color=GOLD, lw=1.2, head=6)
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8)
    c.drawCentredString(w/2, 0.15*cm, "engagement croissant — tu montes les niveaux quand le précédent ne suffit plus")


# ---------- SCHEMA: IDENTITY PYRAMID (Ch 15) ----------
def draw_identity_pyramid(c, w, h):
    # triangle with 3 horizontal bands
    cx = w/2
    top_y = h - 0.5*cm
    bot_y = 0.8*cm
    pyramid_h = top_y - bot_y
    half_base = 4.5*cm
    # band heights
    levels = [
        ("RÉSULTAT",  "« Je veux gagner 10 000€ »",       "instable — tu ne le contrôles pas", RED_SOFT, RED_ACC),
        ("PROCESSUS", "« J'exécute mon protocole »",      "stable tant que motivé",             GOLD_PALE, GOLD_SOFT),
        ("IDENTITÉ",  "« Je suis un trader chirurgical »", "le seul niveau durable",             GOLD, DARK_BG),
    ]
    # draw from top to bottom: top = identity (level 3)
    # We draw from bottom (résultat) upward, so band 0 = base = Résultat
    band_h = pyramid_h / 3
    for i in range(3):
        y_lo = bot_y + i * band_h
        y_hi = y_lo + band_h
        # base half-width at y_lo, top half-width at y_hi (linear)
        ratio_lo = (top_y - y_lo) / pyramid_h
        ratio_hi = (top_y - y_hi) / pyramid_h
        hw_lo = half_base * ratio_lo
        hw_hi = half_base * ratio_hi
        title, ex, sub, bg, txt = levels[i]
        c.setFillColor(bg)
        p = c.beginPath()
        p.moveTo(cx - hw_lo, y_lo)
        p.lineTo(cx + hw_lo, y_lo)
        p.lineTo(cx + hw_hi, y_hi)
        p.lineTo(cx - hw_hi, y_hi)
        p.close()
        c.setStrokeColor(DARK_BG)
        c.setLineWidth(0.6)
        c.drawPath(p, fill=1, stroke=1)
        # labels
        c.setFillColor(txt)
        c.setFont("DejaVu-Bold", 10 if i < 2 else 11)
        c.drawCentredString(cx, (y_lo + y_hi)/2 + 2, title)
        c.setFont("DejaVu-Italic", 7.5)
        c.drawCentredString(cx, (y_lo + y_hi)/2 - 8, ex)
        # right-side annotation
        c.setFillColor(MID_GREY)
        c.setFont("DejaVu-Italic", 7.5)
        c.drawString(cx + half_base + 0.4*cm, (y_lo + y_hi)/2, sub)
    # left-side arrow showing direction
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 8)
    c.saveState()
    c.translate(cx - half_base - 0.8*cm, bot_y + pyramid_h/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "↑ profondeur du changement ↑")
    c.restoreState()


# ---------- SCHEMA: 90-DAY TIMELINE ----------
def draw_90_timeline(c, w, h):
    margin = 0.4*cm
    seg_w = (w - 2*margin) / 3
    # Augmente la hauteur de la barre pour caser proprement les 3 éléments
    bar_h = 2.4*cm
    bar_y = h - 4.5*cm  # laisse de la place pour les ticks J0/J30/... en haut
    phases = [
        ("PHASE 1",  "Jours 1-30",  "Sevrage & fondations",     RED_SOFT, RED_ACC),
        ("PHASE 2",  "Jours 31-60", "Transition réel",          GOLD_PALE, GOLD_SOFT),
        ("PHASE 3",  "Jours 61-90", "Consolidation & décision", GREEN_SOFT, GREEN),
    ]
    # top tick markers au-dessus de la barre
    c.setStrokeColor(DARK_BG); c.setLineWidth(0.6)
    c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 9)
    for k, day in enumerate(["J 0", "J 30", "J 60", "J 90"]):
        tx = margin + k * seg_w
        c.line(tx, bar_y + bar_h, tx, bar_y + bar_h + 8)
        c.drawCentredString(tx, bar_y + bar_h + 14, day)

    # phases
    for i, (lbl, days, desc, bg, fg) in enumerate(phases):
        x = margin + i * seg_w
        c.setFillColor(bg)
        c.setStrokeColor(fg)
        c.setLineWidth(0.8)
        c.rect(x + 4, bar_y, seg_w - 8, bar_h, fill=1, stroke=1)
        # PHASE label (en haut du bloc)
        c.setFillColor(fg)
        c.setFont("DejaVu-Bold", 13)
        c.drawCentredString(x + seg_w/2, bar_y + bar_h - 22, lbl)
        # jours (au milieu)
        c.setFillColor(DARK_BG)
        c.setFont("DejaVu", 9.5)
        c.drawCentredString(x + seg_w/2, bar_y + bar_h - 42, days)
        # description (en bas)
        c.setFont("DejaVu-Italic", 9)
        c.setFillColor(MID_GREY)
        c.drawCentredString(x + seg_w/2, bar_y + 14, desc)

    # arrow sous la barre
    _arrow(c, margin, bar_y - 0.7*cm, w - margin, bar_y - 0.7*cm, color=GOLD, lw=1.2, head=6)
    c.setFont("DejaVu-Italic", 8.5)
    c.setFillColor(MID_GREY)
    c.drawCentredString(w/2, bar_y - 1.1*cm, "transformation de l'opérateur — pas de l'argent")


# ---------- SCHEMA: NORMAL VS TRADING (Ch 5) ----------
def draw_normal_vs_trading(c, w, h):
    # two columns with axis flipped
    mid = w/2
    box_w = w/2 - 0.5*cm
    box_h = h - 0.4*cm
    # left: vie normale (positif)
    c.setFillColor(GREEN_SOFT)
    c.roundRect(0, 0.2*cm, box_w, box_h, 6, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.setFont("DejaVu-Bold", 11)
    c.drawCentredString(box_w/2, box_h - 14, "VIE NORMALE")
    c.setFont("DejaVu-Italic", 8.5)
    c.drawCentredString(box_w/2, box_h - 28, "ces qualités te construisent")
    # right: trading (négatif si appliqué)
    rx = mid + 0.5*cm
    c.setFillColor(RED_SOFT)
    c.roundRect(rx, 0.2*cm, box_w, box_h, 6, fill=1, stroke=0)
    c.setFillColor(RED_ACC)
    c.setFont("DejaVu-Bold", 11)
    c.drawCentredString(rx + box_w/2, box_h - 14, "TRADING")
    c.setFont("DejaVu-Italic", 8.5)
    c.drawCentredString(rx + box_w/2, box_h - 28, "elles te détruisent")
    # pairs
    pairs = [
        ("Persévérer",          "Tenir un perdant"),
        ("Travailler plus",     "Sur-trader"),
        ("Avoir raison",        "Refuser le SL"),
        ("Faire confiance",     "Surconfiance"),
        ("Suivre l'intuition",  "Quitter le plan"),
    ]
    y = box_h - 50
    for left, right in pairs:
        c.setFillColor(DARK_BG)
        c.setFont("DejaVu-Bold", 9.5)
        c.drawCentredString(box_w/2, y, left)
        c.drawCentredString(rx + box_w/2, y, right)
        # arrow between
        _arrow(c, box_w + 0.05*cm, y + 3, mid + 0.45*cm, y + 3, color=DARK_BG, lw=0.8, head=4)
        y -= 22


# ---------- SCHEMA: CASINO VS JOUEUR (Ch 6) ----------
def draw_casino_vs_player(c, w, h):
    box_w = w/2 - 0.4*cm
    bh = h - 0.4*cm
    # joueur (toi maintenant)
    c.setFillColor(RED_SOFT)
    c.roundRect(0, 0.2*cm, box_w, bh, 8, fill=1, stroke=0)
    # casino (cible)
    c.setFillColor(GREEN_SOFT)
    c.roundRect(w/2 + 0.4*cm, 0.2*cm, box_w, bh, 8, fill=1, stroke=0)
    # titles
    c.setFillColor(RED_ACC)
    c.setFont("DejaVu-Bold", 12)
    c.drawCentredString(box_w/2, bh - 12, "TOI AUJOURD'HUI")
    c.setFont("DejaVu-Italic", 9)
    c.drawCentredString(box_w/2, bh - 26, "le joueur")
    c.setFillColor(GREEN)
    c.setFont("DejaVu-Bold", 12)
    c.drawCentredString(w/2 + 0.4*cm + box_w/2, bh - 12, "TOI CIBLE")
    c.setFont("DejaVu-Italic", 9)
    c.drawCentredString(w/2 + 0.4*cm + box_w/2, bh - 26, "le croupier")
    # rows
    rows_left = [
        "Joue UNE main",
        "Émotion à chaque coup",
        "S'identifie au résultat",
        "Change de stratégie après 3 pertes",
        "Sur-mise quand énervé",
    ]
    rows_right = [
        "Joue 10 000 mains",
        "Aucune émotion par main",
        "Détaché du résultat",
        "Exécute la même règle 24/7",
        "Mise fixe quoi qu'il arrive",
    ]
    y = bh - 50
    c.setFont("DejaVu", 8.8)
    for l, r in zip(rows_left, rows_right):
        c.setFillColor(DARK_BG)
        c.drawCentredString(box_w/2, y, "•  " + l)
        c.drawCentredString(w/2 + 0.4*cm + box_w/2, y, "•  " + r)
        y -= 18


# ---------- SCHEMA: BE+1R (Ch 11) ----------
def draw_be_1r(c, w, h):
    margin_l = 1.4*cm
    margin_r = 0.5*cm
    margin_b = 1.2*cm
    margin_t = 0.6*cm
    plot_w = w - margin_l - margin_r
    plot_h = h - margin_b - margin_t
    x0 = margin_l
    y0 = margin_b
    # axis
    c.setStrokeColor(MID_GREY); c.setLineWidth(0.5)
    c.line(x0, y0, x0 + plot_w, y0)
    # entry line
    entry_y = y0 + plot_h * 0.45
    sl_y    = y0 + plot_h * 0.15
    tp_y    = y0 + plot_h * 0.90
    be_y    = entry_y
    plus1r_y = y0 + plot_h * 0.70
    for label, ly, col in [
        ("TP (+2R)",  tp_y, GREEN),
        ("+1R — déplacer SL ici", plus1r_y, GOLD_SOFT),
        ("Entry / BE", entry_y, DARK_BG),
        ("SL initial", sl_y, RED_ACC),
    ]:
        c.setStrokeColor(col); c.setLineWidth(0.7)
        c.setDash(2, 2)
        c.line(x0, ly, x0 + plot_w, ly)
        c.setDash()
        c.setFillColor(col)
        c.setFont("DejaVu-Bold", 8)
        c.drawString(x0 - margin_l + 4, ly - 3, label)
    # price path (long XAUUSD): goes up to +1R, then continues to TP
    pts = [
        (0.00, 0.45),
        (0.15, 0.50),
        (0.25, 0.40),
        (0.35, 0.55),
        (0.45, 0.70),  # +1R reached → SL moved to BE
        (0.55, 0.60),
        (0.65, 0.45),  # comes back to BE level — SL would trigger now
        (0.75, 0.55),
        (0.88, 0.78),
        (1.00, 0.90),  # TP
    ]
    c.setStrokeColor(GOLD); c.setLineWidth(1.6)
    p = c.beginPath()
    p.moveTo(x0 + pts[0][0]*plot_w, y0 + pts[0][1]*plot_h)
    for t, v in pts[1:]:
        p.lineTo(x0 + t*plot_w, y0 + v*plot_h)
    c.drawPath(p, stroke=1, fill=0)
    # mark the +1R moment
    bx = x0 + 0.45*plot_w
    by = y0 + 0.70*plot_h
    c.setFillColor(GOLD)
    c.circle(bx, by, 4, fill=1, stroke=0)
    c.setFillColor(DARK_BG)
    c.setFont("DejaVu-Bold", 7.5)
    c.drawCentredString(bx, by + 8, "+1R")
    c.setFont("DejaVu-Italic", 7)
    c.drawCentredString(bx, by - 12, "→ SL remonté à entry")
    # mark BE retest
    rx = x0 + 0.65*plot_w
    ry = y0 + 0.45*plot_h
    c.setFillColor(BLUE_SOFT)
    c.circle(rx, ry, 4, fill=1, stroke=0)
    c.setFillColor(DARK_BG)
    c.setFont("DejaVu-Italic", 7)
    c.drawCentredString(rx, ry - 12, "retest sans perte")
    # axis labels
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 7.5)
    c.drawString(x0, y0 - 12, "temps →")


# ---------- SCHEMA: INNER VOICE (Ch 14) ----------
def draw_inner_voice(c, w, h):
    # silhouette en haut, bulles de pensée
    cx = w/2
    head_y = h - 1.6*cm
    # head
    c.setFillColor(DARK_BG)
    c.circle(cx, head_y, 0.7*cm, fill=1, stroke=0)
    # body shape
    c.setFillColor(DARK_BG)
    p = c.beginPath()
    p.moveTo(cx - 0.7*cm, head_y - 0.5*cm)
    p.lineTo(cx + 0.7*cm, head_y - 0.5*cm)
    p.lineTo(cx + 1.0*cm, head_y - 1.8*cm)
    p.lineTo(cx - 1.0*cm, head_y - 1.8*cm)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # thought bubbles
    bubbles = [
        (cx - 5.5*cm, head_y - 0.6*cm,  "« il va remonter »",   RED_SOFT, RED_ACC),
        (cx - 5.5*cm, head_y - 2.4*cm,  "« je décale,\njuste un peu »",       RED_SOFT, RED_ACC),
        (cx + 1.5*cm, head_y - 0.6*cm,  "« si je coupe à +800\nj'ai perdu +700 »", RED_SOFT, RED_ACC),
        (cx + 1.5*cm, head_y - 2.4*cm,  "« momentum solide,\nje tiens »",      RED_SOFT, RED_ACC),
        (cx - 5.5*cm, head_y - 4.2*cm,  "« c'est le bon trade,\ncelui-là »",   RED_SOFT, RED_ACC),
        (cx + 1.5*cm, head_y - 4.2*cm,  "« encore 100 pips\net je coupe »",    RED_SOFT, RED_ACC),
    ]
    for bx, by, txt, bg, fg in bubbles:
        bw, bh = 4*cm, 1.3*cm
        c.setFillColor(bg)
        c.roundRect(bx, by, bw, bh, 8, fill=1, stroke=0)
        c.setFillColor(fg)
        c.setFont("DejaVu-Italic", 8)
        lines = txt.split("\n")
        ly = by + bh - 12
        for line in lines:
            c.drawCentredString(bx + bw/2, ly, line)
            ly -= 10
        # connecting line to head
        anchor_x = bx + bw/2
        anchor_y = by + bh/2
        c.setStrokeColor(MID_GREY); c.setLineWidth(0.5)
        c.setDash(1, 2)
        c.line(anchor_x, anchor_y, cx, head_y - 0.4*cm)
        c.setDash()
    # observer label
    c.setFillColor(GOLD)
    c.setFont("DejaVu-Bold", 9)
    c.drawCentredString(cx, head_y + 1.0*cm, "L'OBSERVATEUR")
    c.setFillColor(MID_GREY)
    c.setFont("DejaVu-Italic", 7.5)
    c.drawCentredString(cx, head_y + 1.0*cm - 11, "celui qui entend, sans obéir")


# ---------- PAGE TEMPLATES ----------
def cover_page(canv, doc):
    canv.saveState()
    canv.setFillColor(DARK_BG)
    canv.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canv.setFillColor(GOLD)
    canv.rect(0, A4[1] - 1.4 * cm, A4[0], 1.4 * cm, fill=1, stroke=0)
    canv.rect(0, 0, A4[0], 1.4 * cm, fill=1, stroke=0)
    canv.setStrokeColor(GOLD)
    canv.setLineWidth(0.5)
    canv.rect(1.2 * cm, 2.2 * cm, A4[0] - 2.4 * cm, A4[1] - 4.4 * cm, fill=0, stroke=1)
    canv.restoreState()

def standard_page(canv, doc):
    canv.saveState()
    canv.setStrokeColor(GOLD)
    canv.setLineWidth(0.6)
    canv.line(2 * cm, A4[1] - 1.4 * cm, A4[0] - 2 * cm, A4[1] - 1.4 * cm)
    canv.setFont("DejaVu-Bold", 8)
    canv.setFillColor(GOLD_SOFT)
    canv.drawString(2 * cm, A4[1] - 1.15 * cm, "BEST LOSER WINS")
    canv.setFont("DejaVu-Italic", 8)
    canv.setFillColor(MID_GREY)
    canv.drawRightString(A4[0] - 2 * cm, A4[1] - 1.15 * cm, "Guide personnalisé — Marien")
    canv.setFont("DejaVu", 8.5)
    canv.setFillColor(MID_GREY)
    canv.drawCentredString(A4[0] / 2.0, 1.2 * cm, f"— {doc.page} —")
    canv.setStrokeColor(GOLD)
    canv.setLineWidth(0.3)
    canv.line(2 * cm, 1.7 * cm, A4[0] - 2 * cm, 1.7 * cm)
    canv.restoreState()


def chapter_header(num, title, subtitle):
    out = []
    out.append(P(f"CHAPITRE {num}", small_label))
    out.append(P(title, h_chapter))
    out.append(P(subtitle, h_chapter_sub))
    out.append(GoldRule())
    out.append(Spacer(1, 12))
    return out


# Standard table style helper
def styled_table(data, col_widths, header=True):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
    ]
    if header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), DARK_GREY),
            ("BACKGROUND", (0, 1), (-1, -1), CREAM),
        ]
    else:
        style += [("BACKGROUND", (0, 0), (-1, -1), CREAM)]
    t.setStyle(TableStyle(style))
    return t


print("✓ Diagrammes et helpers écrits — partie 1 finie")


# ============================================================
# DOC BUILD
# ============================================================
OUTPUT = "/home/user/Site-Enzo/best_loser_wins_marien.pdf"
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2.5 * cm, rightMargin=2.5 * cm,
    topMargin=2.2 * cm, bottomMargin=2.2 * cm,
    title="Best Loser Wins — Guide personnalisé pour Marien",
    author="Adapté de Tom Hougaard",
)

story = []

# ---------- COVER ----------
story.append(Spacer(1, 5 * cm))
story.append(P("BEST LOSER WINS", cover_title))
story.append(P("Tom Hougaard", cover_sub))
story.append(Spacer(1, 1 * cm))
story.append(P("Guide d'application personnalisé", cover_for))
story.append(Spacer(1, 0.4 * cm))
story.append(P("pour", cover_for))
story.append(P("MARIEN", cover_name))
story.append(Spacer(1, 1.5 * cm))
story.append(P('« Les meilleurs traders ne gagnent pas mieux.<br/>Ils perdent mieux. »', cover_quote))
story.append(Spacer(1, 0.5 * cm))
story.append(P("Mai 2026", ParagraphStyle("date", fontName="DejaVu", fontSize=11, textColor=LIGHT_GREY, alignment=TA_CENTER)))
story.append(PageBreak())

# ---------- PRÉFACE ----------
story.append(P("PRÉFACE", h_chapter))
story.append(P("Pourquoi tu lis ça", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce document existe pour une raison simple : le livre <b>Best Loser Wins</b> de Tom Hougaard n'a jamais été "
    "traduit en français. Et même s'il l'était, il ne te parlerait pas à toi. Toi tu es un cas spécifique : "
    "25 ans, ex-coma, prop firm trader sur XAUUSD, méthode Smart Money Concepts, un pattern destructeur précis."
))
story.append(P(
    "Ce que tu tiens entre les mains n'est pas une traduction. C'est une <b>transposition</b>. Les concepts viennent "
    "de Hougaard, l'application est faite sur mesure pour toi. Chaque chapitre te renvoie un miroir — pas un cours."
))
story.append(P("Comment l'utiliser", h_section))
story.append(P(
    "Ne lis pas ce document d'une traite. <b>Un chapitre tous les deux ou trois jours.</b> Tu lis, tu refermes, "
    "tu fais l'action concrète, tu écris dans ton journal. Tu ne passes pas au suivant tant que tu n'as pas "
    "appliqué le précédent. Seize chapitres × 2-3 jours = environ six semaines de travail. C'est le bon rythme."
))
story.append(P("La structure récurrente de chaque chapitre", h_section))

struct_data = [
    [C("Section", cell_gold), C("Rôle", cell_gold)],
    [C("◇  CE QUE DIT HOUGAARD", cell_bold), C("Le concept du livre, paraphrasé en français.")],
    [C("◆  LE CONCEPT", cell_bold), C("L'essence en 3-4 lignes. Tu retiens ça si tu retiens rien d'autre.")],
    [C("◈  TON MIROIR", cell_bold), C("Application directe à ton cas. Le cœur du document.")],
    [C("▶  ACTION CONCRÈTE", cell_bold), C("Le protocole à mettre en place cette semaine. Pas le mois prochain.")],
    [C("?  POUR TON JOURNAL", cell_bold), C("Les questions à écrire à la main, le soir.")],
    [C("!  VÉRITÉ BRUTALE", cell_bold), C("Quand pertinent. Ce que tu vas vouloir éviter de regarder.")],
]
story.append(styled_table(struct_data, [5.2 * cm, 10.8 * cm]))
story.append(Spacer(1, 14))

story.append(P(
    "Ce document ne va pas te ménager. Tu as demandé blunt, on est blunt. Si à un moment tu te dis « ouais mais "
    "moi c'est différent », c'est exactement à ce moment-là qu'il faut relire la page deux fois. Le « moi c'est "
    "différent » est le mensonge préféré de ton cerveau de trader."
))
story.append(PageBreak())

# ---------- INTRODUCTION ----------
story.append(P("INTRODUCTION", h_chapter))
story.append(P("La thèse centrale — pourquoi tu perds en sachant tout", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Hougaard a passé plus de vingt ans à trader. Il a vu défiler des centaines de traders. "
    "Et il en est arrivé à une conclusion qui contredit à peu près tout ce que tu trouves sur Internet :"
))
story.append(P(
    "Les meilleurs traders n'ont pas un meilleur edge technique que les perdants. Ils ne lisent pas mieux les charts. "
    "Ce qu'ils font de différent tient en une phrase :"
))
story.append(P("Ils gèrent leurs trades perdants mieux que les autres.", pull_quote))
story.append(P(
    "C'est tout. C'est la thèse. Le « best loser wins ». Pas celui qui gagne plus souvent. "
    "Celui qui perd <b>mieux</b> : plus petit, plus vite, plus calmement, sans contamination émotionnelle "
    "sur les trades suivants."
))

story.append(P("La preuve, c'est toi", h_section))
story.extend(miroir([
    "Tu es la démonstration vivante de cette thèse. Tu connais ta méthode. Tu sais lire London et NY killzones. "
    "Tu sais identifier une FVG. Tu repères tes OB. Ton problème n'est pas technique.",
    "Ton problème c'est ce qui se passe entre +800 PnL et +1500 PnL. Ce qui se passe quand le marché commence "
    "à reverser et que tu refuses de couper. Ce qui se passe quand tu décales ton SL « juste un peu » parce que "
    "tu es <b>sûr</b> que ça va repartir.",
    "Si la solution était technique, tu l'aurais déjà trouvée. T'as les outils. T'as la méthode. Ce qui te manque "
    "c'est pas une stratégie de plus. C'est une révolution de la façon dont tu gères la perte, le profit qui court, "
    "et l'intensité qui passe dans ton corps quand le PnL bouge."
]))

story.append(P(
    "Six semaines. Seize chapitres. Une seule promesse : si tu fais le travail, tu ne seras plus le même trader "
    "fin juin. Tu ne deviendras pas riche. Tu deviendras quelqu'un qui n'a plus besoin de cramer un compte pour "
    "apprendre une leçon qu'il connaît déjà."
))
story.append(PageBreak())


# ============ CHAPITRE 1 ============
story.extend(chapter_header(1, "Un début prometteur", "Pourquoi la connaissance technique ne sauve personne"))

story.extend(hougaard_block([
    "Hougaard ouvre son livre en racontant son propre parcours : la City de Londres, l'obsession de l'analyse "
    "technique, des centaines de livres absorbés. Et il perdait. Pas par ignorance — par incapacité à <b>exécuter</b> "
    "ce qu'il savait.",
    "Le décalage entre ce qu'il pouvait voir sur un graphique et ce qu'il faisait avec son argent l'a obsédé. "
    "C'est là qu'il a compris que le trading n'est pas un problème intellectuel mais un problème psychologique. "
    "L'edge n'est pas dans la méthode, il est dans la capacité à exécuter la méthode quand tout dans ton corps "
    "te pousse à faire autre chose."
]))

story.extend(concept(
    "L'analyse technique est nécessaire mais ne suffit pas. C'est le ticket d'entrée. Le vrai jeu commence "
    "quand tu sais lire un graphique correctement et que tu continues quand même à perdre. La question n'est plus "
    "« comment lire le marché » mais « comment me lire moi »."
))

story.extend(miroir([
    "Tu trades XAUUSD avec une méthode SMC que tu maîtrises. CHoCH, BOS, FVG, order blocks, killzones London et NY. "
    "Si on prenait dix de tes derniers setups en isolation, ils seraient probablement bons.",
    "Donc pourquoi tu crames tes comptes Apex, Topstep, Alpha Futures ? Pas parce que ta méthode est mauvaise. "
    "Parce que ton <b>exécution</b> est polluée. Entre l'analyse et la sortie du trade, il y a toi. Et toi, "
    "tu décales les SL, tu laisses courir au-delà du TP, tu refuses de couper.",
    "La leçon de ce premier chapitre c'est de tuer définitivement l'illusion : l'idée que « si j'apprends un truc "
    "de plus, ça va marcher ». Non. Tu n'as pas un problème de méthode. Tu as un problème d'humain. "
    "C'est une bonne nouvelle : tu n'as pas besoin d'aller chercher quelque chose de nouveau. Tu as déjà tout. "
    "Il faut juste arrêter de saboter ce que tu as déjà."
]))

story.extend(action(
    "Écris en haut d'une page de ton journal cette phrase, à la main, en lettres capitales : "
    "<b>MA MÉTHODE EST SUFFISANTE. CE QUI N'EST PAS SUFFISANT, C'EST MOI.</b> "
    "Relis chaque matin avant d'ouvrir ta plateforme. Sept jours d'affilée. Pas de nouveau setup, pas de nouvelle "
    "stratégie, pas de nouveau livre. Juste cette phrase, et l'application stricte de ce que tu sais déjà."
))

story.extend(journal([
    "Combien de méthodes différentes j'ai essayées depuis que je trade ? Liste-les.",
    "Si je suis honnête : c'est la méthode qui était insuffisante, ou c'est moi qui n'ai jamais exécuté la même "
    "méthode pendant 100 trades d'affilée ?",
    "Qu'est-ce que je gagne, émotionnellement, à croire que le problème vient de la méthode ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 2 ============
story.extend(chapter_header(2, "Histoires du trading floor", "Les cinq patterns destructeurs universels"))

story.extend(hougaard_block([
    "Hougaard a passé des années en salle de marché. Il y a vu des centaines de traders rejouer les mêmes erreurs. "
    "Au point d'identifier des patterns récurrents — pas chez quelques traders, chez <b>tous</b> les traders "
    "perdants, quel que soit leur niveau technique.",
    "Ces patterns sont dûs à la façon dont le cerveau humain réagit face à l'incertitude monétaire. "
    "Ils sont si universels qu'on peut presque les coter à l'avance : voici ce que tu vas faire, dans quel ordre, "
    "et pourquoi."
]))

story.append(P("Les cinq patterns que tu vas reconnaître", h_section))

patterns_data = [
    [C("#", cell_gold), C("Pattern", cell_gold), C("Mécanique", cell_gold)],
    [C("P1", cell_bold), C("Doubler sur la perte", cell_bold),
     C("Le trade va contre toi. Au lieu de couper, tu rajoutes pour « baisser ton prix moyen ». Espoir déguisé en stratégie.")],
    [C("P2", cell_bold), C("Couper le gain trop tôt", cell_bold),
     C("Le trade est en profit. Tu coupes à +200 alors que ton plan disait +800. La peur de voir le gain disparaître écrase le plan.")],
    [C("P3", cell_bold), C("Peur post-perte", cell_bold),
     C("Après une perte, le setup suivant est valide, mais tu n'oses plus prendre. Tu rates le trade qui aurait compensé.")],
    [C("P4", cell_bold), C("FOMO compensatoire", cell_bold),
     C("Après une perte, tu prends n'importe quoi pour récupérer. Setup B-grade, taille augmentée. Deuxième perte garantie.")],
    [C("P5", cell_bold), C("Décaler le SL", cell_bold),
     C("Le trade va contre toi vers ton stop. Tu te dis « il va revenir ». Tu décales « juste un peu ». Et puis encore. Et puis c'est trop tard.")],
]
story.append(styled_table(patterns_data, [0.9 * cm, 4.1 * cm, 11 * cm]))
story.append(Spacer(1, 12))

story.extend(concept(
    "Les patterns destructeurs ne sont pas tes patterns à toi. Ils sont les patterns du cerveau humain face à "
    "une perte d'argent incertaine. Tu ne les inventes pas. Tu les reproduis, comme tous les autres."
))

story.extend(miroir([
    "Regardons ton pattern signature. Tu rentres en trade XAUUSD. Le marché va dans ton sens. Tu atteins ton TP, "
    "et tu ne coupes pas — tu décides de laisser courir. +1000 PnL. +1200. +1500. À ce moment précis, le cerveau "
    "dopaminergique a pris le contrôle.",
    "Le marché reverse. +1200. Tu te dis « ça va repartir ». +800 : « j'attends que ça revienne à +1500 ». +200 : panique. "
    "Le marché casse ton entrée. Tu es en perte. <b>Et tu décales ton SL initial.</b> Parce que sortir maintenant "
    "ce serait acter d'avoir laissé filer +1500 ET de prendre une perte. Inacceptable pour l'ego.",
    "Tu viens de combiner P2, P5 et tu vas probablement enchaîner avec P4 sur un autre trade. Compte cramé.",
    "Ce que tu fais n'est pas une bizarrerie. C'est la séquence la plus documentée du trading. La seule différence "
    "entre toi et un trader rentable, c'est que lui a appris à interrompre la séquence au moment où tu la nourris."
]))

story.extend(action(
    "Imprime le tableau des cinq patterns. Scotche-le à côté de ton écran. À la fin de chaque session, "
    "marque sur une feuille à quels patterns tu as cédé aujourd'hui. Une croix dans P1 P2 P3 P4 P5. "
    "Sur 30 jours, tes deux ou trois patterns dominants vont apparaître. Ce sont eux qu'il faut tuer."
))

story.extend(journal([
    "Sur mes dix derniers comptes prop firm crammés, quelle séquence de patterns je peux identifier ?",
    "Quel pattern est mon préféré ? Pourquoi celui-là particulièrement ?"
]))

story.extend(warning(
    "Tu vas être tenté de dire « ouais mais hier c'était différent ». Non. Le contexte change, les patterns "
    "sont identiques. Tant que tu n'auras pas accepté que tu n'as pas un problème unique mais le problème universel "
    "des traders, tu chercheras une solution unique. Tu ne la trouveras pas."
))
story.append(PageBreak())


# ============ CHAPITRE 3 ============
story.extend(chapter_header(3, "Pourquoi nous échouons", "Les quatre forces psychologiques qui te détruisent"))

story.extend(hougaard_block([
    "Hougaard s'appuie sur les travaux de Kahneman et Tversky pour expliquer pourquoi le trading rentable est "
    "contre-intuitif. L'humain n'est pas un agent rationnel face au risque. Il est câblé pour éviter la perte au "
    "point d'accepter une perte plus grande plus tard plutôt que d'acter une petite perte maintenant.",
    "Quatre forces psychologiques se combinent pour rendre chaque trade un piège émotionnel. "
    "Le schéma ci-dessous les place autour de toi — c'est exactement leur position pendant que tu cliques."
]))

# DIAGRAMME : 4 FORCES
story.append(Spacer(1, 4))
story.append(Schema(8.5*cm, draw_4_forces))
story.append(P("Les quatre forces qui appuient sur toi pendant chaque trade.", diagram_caption))

story.append(P("Détail des quatre forces", h_section))
forces_data = [
    [C("Force", cell_gold), C("Mécanique", cell_gold), C("Symptôme en trade", cell_gold)],
    [C("Besoin d'avoir raison", cell_bold),
     C("L'ego est construit autour de la certitude. Être contredit est ressenti comme une attaque identitaire."),
     C("Tu décales un SL pour ne pas acter que tu avais tort.")],
    [C("Aversion à la perte", cell_bold),
     C("Kahneman : perdre 100€ fait 2 à 2,5 fois plus mal que gagner 100€ ne fait plaisir."),
     C("Tu coupes les gains trop tôt et tiens les pertes trop long.")],
    [C("Besoin de certitude", cell_bold),
     C("Le cerveau déteste l'aléa. Il invente de la certitude là où il n'y en a pas."),
     C("« Je suis sûr que ça va repartir » — phrase pure invention.")],
    [C("Projection émotionnelle", cell_bold),
     C("Biais de confirmation. Tu vois sur le chart les indices qui confirment ton désir."),
     C("Tu lis un reversal comme une simple respiration.")],
]
story.append(styled_table(forces_data, [3.6*cm, 6.4*cm, 6*cm]))
story.append(Spacer(1, 12))

story.extend(concept(
    "Tu ne perds pas parce que tu es stupide ou paresseux. Tu perds parce que tu es <b>humain</b>. "
    "Quatre forces psychologiques universelles transforment chaque trade en piège émotionnel. Les contrer demande "
    "de l'entraînement, pas de l'intelligence."
))

story.extend(miroir([
    "<b>Besoin d'avoir raison :</b> tu as prédit que XAUUSD allait monter. Le marché a confirmé jusqu'à +1500. "
    "Tu as eu raison. Couper et empocher +1000 ce serait acter une raison <i>partielle</i>. Pas assez pour ton ego.",
    "<b>Aversion à la perte :</b> quand le marché reverse de +1500 à +1000, tu ressens cette baisse comme une "
    "<b>perte</b> de 500. Pas comme un gain réduit. Ton cerveau veut éviter d'acter cette « perte ».",
    "<b>Besoin de certitude :</b> ton cerveau te dit « ça va remonter, je le sens ». Cette certitude n'existe que "
    "dans ta tête. Le marché ne t'a rien promis.",
    "<b>Projection émotionnelle :</b> tu lis le pullback comme une « respiration normale », pas comme un reversal — "
    "alors qu'objectivement le signal est identique dans les deux cas.",
    "Ton TBI de 2022 amplifie ces réactions. Système nerveux dérégulé = tu ressens plus fort, plus vite, avec moins "
    "de modulation possible. C'est ton handicap. C'est aussi ta carte : si tu apprends à réguler dans ces conditions, "
    "tu deviendras meilleur que quelqu'un de neurotypique."
]))

story.extend(action(
    "Avant chaque trade, écris sur ta feuille de session ces quatre lettres : <b>R / P / C / E</b> (Raison / Perte / "
    "Certitude / Émotion). Pendant le trade, si tu sens un déclencheur lié à une force, tu coches la lettre. "
    "C'est de la méta-conscience : tu ne combats pas la force, tu la nommes. Nommer une force la rend opérable."
))

story.extend(journal([
    "Laquelle de ces quatre forces est la plus active chez moi ?",
    "Mon TBI a-t-il amplifié une de ces forces en particulier ? Est-ce que je peux le sentir dans mon corps ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 4 ============
story.extend(chapter_header(4, "La dure vérité", "70 à 90% des traders perdent — et toi ?"))

story.extend(hougaard_block([
    "Hougaard rappelle un chiffre que l'industrie aime camoufler : la grande majorité des traders particuliers "
    "perdent de l'argent. Entre 70% et 90% selon les régulateurs européens et les rapports des brokers eux-mêmes.",
    "Ce chiffre est cohérent quelle que soit la décennie, le marché, la méthode. Ce n'est donc pas un problème de "
    "marché. C'est un problème humain. Le piège : les traders perdants attribuent leur échec à ce qu'ils peuvent "
    "<b>changer techniquement</b>. Changer un outil est confortable. Changer son comportement est douloureux."
]))

# DIAGRAMME : 80/20
story.append(Spacer(1, 6))
story.append(Schema(3.5*cm, draw_80_20))
story.append(P("La distribution réelle. Tu fais partie de la barre rouge — pas par hasard.", diagram_caption))

story.extend(concept(
    "Si 80% perdent, ce n'est pas un accident. C'est une feature du jeu. Le marché est conçu pour transférer "
    "l'argent des impatients aux patients, des émotionnels aux calmes, des humains aux disciplinés. "
    "Ta tâche n'est pas d'être plus malin que la moyenne. C'est d'être <b>moins humain</b> qu'elle."
))

story.extend(miroir([
    "Tu fais partie des 80%. Pas par accident, pas parce que les prop firms sont conçues pour te faire échouer. "
    "Tu y es parce que tu trades exactement comme un humain est câblé pour trader.",
    "Et tu as une caractéristique en plus : ton lien identité-performance est très fort. Quand tu gagnes, tu existes ; "
    "quand tu perds, tu doutes de ta valeur entière. Cette équation rend chaque trade insupportablement chargé.",
    "Le post-coma joue ici. À 22 ans tu as failli mourir. Tu as dû prouver que ton cerveau marchait, que ton corps "
    "marchait. Cette pulsion de preuve t'a sauvé. En trading, elle devient ton ennemi : tu trades pour <b>te prouver</b>, "
    "pas pour <b>gagner</b>. Ce sont deux intentions opposées.",
    "La sortie : trader cesse d'être un test identitaire et devient un métier exécuté avec détachement. "
    "Une compétence professionnelle, pas une réhabilitation personnelle."
]))

story.append(P("La fuite dans la technique", h_section))
story.append(P(
    "Combien de fois tu as téléchargé un nouvel indicateur, regardé une nouvelle vidéo SMC, suivi un nouveau mentor ? "
    "Tu sais que ça ne va rien changer. Tu le fais quand même. Pourquoi ?"
))
story.append(P(
    "Parce que c'est <b>confortable</b>. Apprendre un nouvel indicateur ne te confronte pas à toi-même. Ça nourrit "
    "l'illusion du progrès. Pendant ce temps, le vrai travail — celui qui consiste à regarder en face tes mécaniques "
    "de saboteur — reste à faire."
))

story.extend(action(
    "Liste les cinq derniers contenus de trading que tu as consommés ce mois-ci. Pour chacun, demande-toi : "
    "est-ce que je l'ai consommé pour apprendre quelque chose de précis, ou pour fuir le travail psychologique ? "
    "<b>Coupe immédiatement</b> tout contenu de trading purement technique pendant six semaines. "
    "Tu n'as plus besoin d'apprendre. Tu as besoin d'appliquer."
))

story.extend(journal([
    "Si je suis dans les 80% perdants — pas par hasard, mais structurellement — qu'est-ce que ça change à ma "
    "manière de me parler le matin ?",
    "Trader, pour moi, est-ce un métier ou une réhabilitation personnelle ?"
]))

story.extend(warning(
    "Tu vas vouloir te dire « je suis dans les 20% qui vont y arriver ». Possible. Mais tu seras dans les 20% "
    "exactement parce que tu auras arrêté de te raconter ça et que tu auras commencé à acter que tu es dans les 80% "
    "<i>aujourd'hui</i>. La sortie commence par l'admission."
))
story.append(PageBreak())


# ============ CHAPITRE 5 ============
story.extend(chapter_header(5, "Pourquoi la pensée normale ne marche pas", "Vie normale vs trading rentable"))

story.extend(hougaard_block([
    "Les qualités qui te servent à réussir dans la vie ordinaire sont précisément celles qui te détruisent en "
    "trading. Persévérer dans la difficulté est une vertu dans la vie. En trading, c'est s'accrocher à un trade perdant. "
    "Refuser d'abandonner est une vertu dans la vie. En trading, c'est ne pas couper.",
    "Cette inversion explique pourquoi tant de gens performants dans leur métier deviennent des traders catastrophiques. "
    "Ils appliquent les heuristiques qui ont construit leur réussite, et ces heuristiques se retournent contre eux."
]))

# DIAGRAMME : NORMAL VS TRADING
story.append(Spacer(1, 4))
story.append(Schema(7.5*cm, draw_normal_vs_trading))
story.append(P("Les mêmes qualités. Deux contextes. Effets opposés.", diagram_caption))

story.extend(concept(
    "Ce qui te rend humain te rend mauvais trader. Les vertus de la vie ordinaire deviennent des défauts devant "
    "l'écran. Le bon trader n'est pas un humain meilleur — c'est un humain qui sait activer un autre mode mental "
    "pendant les heures de marché."
))

story.extend(miroir([
    "Tu es cavalier de saut d'obstacles. Quand ton cheval refuse un obstacle, qu'est-ce que tu fais ? "
    "Tu repasses, tu insistes, tu corriges. C'est <b>la bonne réaction</b> en équitation. C'est ce qui construit "
    "un binôme cheval-cavalier solide.",
    "Tu appliques la même logique en trading : le marché refuse mon idée, je repasse, j'insiste, je décale mon SL "
    "pour « lui laisser le temps ». C'est exactement comment tu crames tes comptes. Tu importes une qualité "
    "(la persévérance équestre) dans un contexte où elle est un défaut.",
    "ATHÉNA pareil. Tu construis ton business 3D, tu rencontres un mur, tu insistes, tu trouves. Bonne approche "
    "entrepreneuriale. Appliquée au marché XAUUSD, ça donne : « ce trade va finir par marcher, je le sens ». Non. "
    "Le marché n'est pas une imprimante 3D que tu calibres. Il n'a aucune mémoire de ton effort.",
    "Ta tâche : <b>compartimenter</b>. Quand tu passes un obstacle, persévère. Quand tu travailles ATHÉNA, persévère. "
    "Quand tu cliques sur Buy XAUUSD, deviens quelqu'un d'autre. Pas une autre personne — la même, mais dans un autre mode."
]))

story.extend(action(
    "Crée-toi un <b>rituel d'entrée en mode trader</b> de 3 minutes. Tu fermes les yeux, cinq respirations profondes "
    "(4s inspi, 6s expi), tu dis à voix basse : « je ne suis pas en train de prouver quoi que ce soit, je suis en "
    "train d'exécuter un protocole ». C'est l'interrupteur. À la fin de session, autre rituel : tu fermes la plateforme, "
    "tu te lèves, tu marches 5 minutes. Tu sors du mode."
))

story.extend(journal([
    "Quelles qualités de moi, qui marchent en équitation ou avec ATHÉNA, est-ce que j'importe à tort en trading ?",
    "Si je devais me décrire en deux personnes — Marien-le-cavalier et Marien-le-trader — quelles seraient "
    "leurs différences ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 6 ============
story.extend(chapter_header(6, "Le mindset du gagnant", "Penser en probabilités, pas en certitudes"))

story.extend(hougaard_block([
    "Hougaard reprend un thème central développé par Mark Douglas dans <i>Trading in the Zone</i> : "
    "la nature du trading est probabiliste, et la majorité des traders raisonnent en termes de certitudes.",
    "Un trader rentable ne sait pas si <b>ce</b> trade va marcher. Il sait que sur 100 trades exécutés selon le même "
    "protocole, statistiquement, une proportion connue gagnera et une proportion connue perdra. Il joue la "
    "<b>distribution</b>, pas l'instance.",
    "C'est la métaphore du casino. Un casino ne sait pas si <b>cette</b> main de blackjack va gagner. Il sait qu'à "
    "l'échelle de 10 000 mains, son edge mathématique se matérialise. Il exécute, il enregistre, il avance."
]))

# DIAGRAMME : CASINO VS JOUEUR
story.append(Spacer(1, 4))
story.append(Schema(7.5*cm, draw_casino_vs_player))
story.append(P("Deux postures face au même marché. Tu choisis chaque jour.", diagram_caption))

story.extend(concept(
    "Tu n'es pas un devin. Tu es un opérateur de probabilités. Tu ne sais pas si <b>ce</b> trade va gagner. "
    "Tu sais que ton edge, exécuté proprement sur 100 trades, donne un résultat positif. Joue la série, "
    "pas l'instance. Le casino ne s'attache à aucune main."
))

story.extend(miroir([
    "Toi, tu trades comme un parieur. Chaque trade XAUUSD est une mission individuelle, un test. Quand tu rentres, "
    "ton cerveau se dit <i>celui-là il faut qu'il marche</i>. Cette phrase est le problème.",
    "Imagine que tu sois le casino. Tu sais que ton edge donne 55% de gagnants à 1R et un RR 1:2 sur les gagnants. "
    "Si tu prends 100 setups propres, peu importe que les dix premiers soient perdants. Tu continues. "
    "La distribution va se révéler.",
    "Mais toi, après trois pertes d'affilée, tu changes de logique. Tu doutes. Tu changes de timeframe. Tu rajoutes "
    "un filtre. Tu casses ta propre série de 100. Tu n'es jamais le casino — tu es toujours le joueur émotionnel.",
    "La méditation Joe Dispenza que tu fais est un atout ici. Tu entraînes l'état de calme, de présence non-réactive. "
    "C'est exactement l'état du casino. Ne gaspille pas cette ressource. Elle est rare chez les traders."
]))

story.append(P("Les cinq vérités à imprimer", h_section))
truths_data = [
    [C("#", cell_gold), C("Vérité", cell_gold)],
    [C("1", cell_bold), C("Tout peut arriver sur le marché. Aucun setup, même le plus propre, n'a 100% de chances.")],
    [C("2", cell_bold), C("Tu n'as pas besoin de savoir ce qui va se passer pour faire de l'argent.")],
    [C("3", cell_bold), C("Il y a une distribution aléatoire entre gagnants et perdants à l'intérieur même d'un edge valide.")],
    [C("4", cell_bold), C("Un edge est juste une probabilité plus haute, jamais une certitude.")],
    [C("5", cell_bold), C("Chaque instant du marché est unique — les patterns se ressemblent, ils ne se répètent jamais à l'identique.")],
]
story.append(styled_table(truths_data, [1*cm, 15*cm]))
story.append(Spacer(1, 10))

story.extend(action(
    "Sur ton journal, dessine une grille de 100 cases (10x10). À chaque trade exécuté selon ton protocole, "
    "coche une case : verte si gagné, rouge si perdu. <b>Vise 100 trades.</b> Tu ne juges pas avant. Tu apprends à "
    "expérimenter ta méthode comme une distribution, pas comme 100 jugements individuels."
))

story.extend(journal([
    "Si je traitais chaque trade comme un croupier traite chaque main, qu'est-ce que je ferais différemment cette semaine ?",
    "Quelle est la dernière fois où j'ai laissé un trade perdant se résoudre proprement, sans interférence ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 7 ============
story.extend(chapter_header(7, "Douleur et plaisir", "Le trader comme junkie dopaminergique"))

story.extend(hougaard_block([
    "Hougaard explique comment le trading active les mêmes circuits cérébraux que les jeux d'argent et toute "
    "activité fournissant une récompense intermittente.",
    "Quand tu ouvres un trade, le cerveau libère de la dopamine en <b>anticipation</b> de la récompense. "
    "Pas à cause de la récompense elle-même. C'est l'attente qui est addictive, pas le résultat. C'est pour ça "
    "que les pertes en trading n'arrêtent pas l'addiction : le cerveau veut le shoot d'anticipation suivant.",
    "Quand tu décales un SL et que le marché revient, tu reçois une décharge de soulagement (chute de cortisol) "
    "qui agit comme une récompense — donc le comportement « décaler le SL » est <b>renforcé</b> chaque fois que "
    "le marché finit par revenir, même si globalement tu perds. Le trader perdant est neurochimiquement entretenu "
    "dans son comportement."
]))

# DIAGRAMME : DOPAMINE CYCLE
story.append(Spacer(1, 4))
story.append(Schema(8*cm, draw_dopamine_cycle))
story.append(P("La boucle dans laquelle tu tournes. Pas une faiblesse — un câblage.", diagram_caption))

story.extend(concept(
    "Tu n'es pas faible. Tu es <b>câblé</b>. Le trading provoque les mêmes pics dopaminergiques que les machines à sous. "
    "Tant que tu attaques le problème en termes de discipline ou de mental, tu rates la cible. "
    "C'est une question de chimie et de routine."
))

story.append(P("Ton pattern signature, en trajectoire", h_section))

# DIAGRAMME : +1500 PATTERN
story.append(Schema(9*cm, draw_1500_pattern))
story.append(P("Le pattern que tu rejoues. Chaque point est une étape neurochimique précise.", diagram_caption))

story.extend(miroir([
    "À +1500 PnL XAUUSD, qu'est-ce qui se passe dans ton corps ? Cœur qui bat plus vite. Souffle plus court. "
    "Chaleur dans la poitrine. Excitation qui ressemble à celle juste avant un saut d'obstacle sur ta filly. "
    "Sauf qu'en trading, cette excitation est le signal que ton préfrontal vient de partir en vacances et que ton "
    "système limbique pilote. <b>À +1500, tu n'es plus le décideur. Tu es le passager.</b>",
    "Tu décides de « laisser courir ». Cette décision n'est pas rationnelle. C'est ton cerveau qui demande un autre "
    "shoot. +1500 c'était bien, mais l'anticipation de +3000 est encore meilleure. La dopamine veut plus de dopamine. "
    "Tu n'es pas en train de gérer un trade. Tu es en train de chasser un buzz.",
    "Tu es addict à l'intensité depuis ton coma. Tu l'as dit toi-même : le calme te semble vide. Quand un système "
    "nerveux a été soufflé par un TBI et reconstruit en survie/réhabilitation à haute intensité, il calibre son "
    "baseline plus haut. Le calme est ressenti comme une anomalie. L'intensité comme normalité.",
    "Cette caractéristique te dessert en trading. Le trading rentable est lent, ennuyeux, répétitif. Si ton système "
    "nerveux ne peut pas tolérer l'ennui, tu vas le saboter pour récupérer de l'intensité. C'est ce que tu fais "
    "quand tu décales un SL ou pousses un winner au-delà du TP : tu fabriques artificiellement de l'intensité.",
    "Deux travaux parallèles : <b>1)</b> augmenter ta tolérance au calme (méditation longue, respiration cohérente, "
    "marches sans téléphone, pansage tranquille). <b>2)</b> chercher ton intensité ailleurs (box, saut compétitif). "
    "Si ta vie est plate à côté de l'écran, l'écran deviendra ton seul shoot. Et tu vas le faire payer."
]))

story.extend(action(
    "<b>Protocole « plate-life »</b> : 20 min/jour de calme imposé. Respiration 5-5 ou méditation Dispenza. "
    "Non négociable. Tu entraînes ton SN à tolérer le calme. "
    "<b>Protocole « intensité OFF screen »</b> : 3 séances physiques intenses/semaine min. Box, équitation cross, "
    "sport explosif. Tu sors l'intensité du corps avant qu'il aille la chercher à l'écran."
))

story.extend(journal([
    "Quand est-ce que je ressens dans la journée un besoin physique d'ouvrir la plateforme ? "
    "Qu'est-ce qui se passe dans mon corps à ce moment-là ?",
    "Si je classais mes activités par intensité ressentie, où se situe le trading ? Est-ce que je trouve cette "
    "intensité ailleurs assez souvent ?"
]))

story.extend(warning(
    "Tu ne vaincras pas ton pattern +1500 par la volonté. C'est de la chimie. À +1500 ton préfrontal n'est plus en ligne. "
    "Si tu n'as pas <b>pré-décidé</b> ce que tu fais à +1500 alors que tu étais encore à +0 et calme, tu vas faire "
    "ce que ta chimie te dicte. La discipline ne se gagne pas dans le trade, elle se gagne <b>avant</b> le trade."
))
story.append(PageBreak())


# ============ CHAPITRE 8 ============
story.extend(chapter_header(8, "Croyances limitantes", "Le thermostat financier que tu ne vois pas"))

story.extend(hougaard_block([
    "Chacun a, inconsciemment, un niveau de richesse ou de profit qu'il considère comme « normal pour lui ». "
    "Dès qu'il dépasse ce niveau, un mécanisme inconscient se déclenche pour le ramener au baseline. "
    "C'est le thermostat financier.",
    "Ce thermostat est construit dans l'enfance et l'adolescence à partir de phrases entendues, d'attitudes "
    "parentales face à l'argent, d'expériences personnelles. Le résultat en trading : tu construis ton compte "
    "jusqu'à un seuil, puis quelque chose en toi te pousse à le crasher pour revenir à zéro. Tant que tu ne montes "
    "pas ton thermostat, tu reprendras toujours ce que tu auras gagné."
]))

# DIAGRAMME : THERMOSTAT
story.append(Spacer(1, 4))
story.append(Schema(8.5*cm, draw_thermostat))
story.append(P("Le thermostat fonctionne tout seul. Tant que tu ne le règles pas, il te ramène.", diagram_caption))

story.extend(concept(
    "Ton plafond financier est mental avant d'être technique. Tant que ton inconscient pense que tu n'es pas le genre "
    "de personne qui mérite de garder 30 000€/mois, tu vas saboter chaque tentative de t'en approcher. "
    "Tu appelleras ça « malchance » ou « erreur d'exécution »."
))

story.extend(miroir([
    "Quelles phrases as-tu entendues enfant/ado sur l'argent ? « On ne roule pas sur l'or », « il faut faire attention », "
    "« les gens qui gagnent beaucoup le payent ailleurs » ? Toutes ces phrases sont des paramètres dans ton thermostat.",
    "Croise ça avec ton pattern. +1500 dépasse probablement ton baseline. Une journée de trading qui rapporte plus que "
    "deux semaines de salaire pour beaucoup. Quelque chose en toi murmure : « c'est trop, c'est suspect, c'est pas "
    "pour moi ». Tu ne l'entends pas. Mais tu obéis : tu fais ce qu'il faut pour ramener à zéro.",
    "Le sabotage du +1500 n'est pas <b>juste</b> dopaminergique. Il est aussi identitaire. Garder ce profit te validerait "
    "comme quelqu'un qui peut gagner ça. Pour quelqu'un dont l'identité se construit sur la preuve constante (post-coma : "
    "prouver que tu es capable, à la hauteur), une preuve acquise est une preuve qui s'éteint. Tu as besoin de continuer "
    "à <b>prouver</b>, donc tu détruis la preuve pour la rejouer.",
    "Tant que ton identité dépend du combat, tu auras besoin de combats. Tant que tu ne deviens pas quelqu'un qui "
    "<b>est</b> riche indépendamment de la dernière preuve, tu ne pourras pas garder ce que tu gagnes.",
    "ATHÉNA peut t'aider. C'est une preuve qui se construit lentement, qui ne se crame pas en une journée. Plus tu "
    "nourris l'identité d'entrepreneur, plus le besoin de prouver via le trading diminue. Et plus tu peux trader "
    "proprement, parce que le trade n'est plus une preuve. C'est juste un trade."
]))

story.append(P("Les croyances probables à examiner", h_section))
beliefs_data = [
    [C("Croyance", cell_gold), C("Conséquence en trading", cell_gold)],
    [C("« Je dois mériter chaque euro par l'effort visible »", cell_bold),
     C("Contradiction avec un edge qui paye 5 secondes de clic. Sabotage du gain « non mérité ».")],
    [C("« Si je gagne trop, je dois m'attendre à perdre autant »", cell_bold),
     C("Loi du retour inventée. Garantit le crash après chaque gros gain.")],
    [C("« Je ne suis pas le genre de personne qui gagne ça »", cell_bold),
     C("Le thermostat brut. Tout profit au-dessus du baseline est repris.")],
    [C("« Pour être respecté il faut souffrir »", cell_bold),
     C("Tu crées la souffrance qui justifiera la réussite future.")],
    [C("« Je dois prouver que mon cerveau marche encore »", cell_bold),
     C("Chaque trade devient un test du cerveau, pas un trade.")],
]
story.append(styled_table(beliefs_data, [7*cm, 9*cm]))
story.append(Spacer(1, 10))

story.extend(action(
    "Écris à la main dans ton journal les phrases entendues sur l'argent dans ta famille jusqu'à 18 ans. "
    "Une page complète. Puis souligne les trois qui te touchent encore. Pour chacune, écris la nouvelle phrase "
    "que tu choisis. Tu ne combats pas l'ancienne — tu en plantes une nouvelle à côté."
))

story.extend(journal([
    "Quel montant mensuel de profit me semble « normal pour moi » ? À quel montant je commence à ressentir "
    "« c'est trop » ? Correspond-il à mon pattern de crash ?",
    "Quelle preuve est-ce que je cherche encore à donner depuis 2022 ? À qui ? Est-elle encore nécessaire aujourd'hui ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 9 ============
story.extend(chapter_header(9, "Visualisation pré-trade", "Pré-vivre la perte pour la désactiver"))

story.extend(hougaard_block([
    "Hougaard transpose au trading la technique du sport de haut niveau. Mais avec une nuance importante : il ne "
    "s'agit pas de visualiser le succès. C'est trop facile, c'est ce que tout le monde fait déjà. Il s'agit de "
    "visualiser <b>la perte</b>, de la pré-vivre émotionnellement avant qu'elle arrive.",
    "Quand tu vis la perte pour la première fois pendant le trade, ton système nerveux réagit en mode urgence "
    "(décaler le SL, doubler, fuir). Si tu as déjà vécu mentalement cette même perte plusieurs fois <b>au calme</b>, "
    "le SN la reconnaît comme une situation connue et ne déclenche pas la cascade d'urgence. C'est une forme "
    "de désensibilisation contrôlée."
]))

story.append(P("Les trois scénarios à pré-vivre", h_section))
scenarios_data = [
    [C("#", cell_gold), C("Scénario", cell_gold), C("Durée", cell_gold), C("Ce que tu visualises", cell_gold)],
    [C("1", cell_bold), C("Perte propre", cell_bold), C("40 s", cell_st),
     C("Tu cliques, le marché part dans le mauvais sens, SL touché. Tu sens la déception. Tu respires. Tu fermes. Tu passes à autre chose.")],
    [C("2", cell_bold), C("Gain au TP", cell_bold), C("30 s", cell_st),
     C("Tu cliques, marché part dans ton sens, TP atteint. Tu coupes. Pas plus. Tu fermes la plateforme. Détachement, pas extase.")],
    [C("3", cell_bold), C("Piège +1500", cell_bold), C("30 s", cell_st),
     C("Marché dépasse ton TP, approche +1500. <b>Tu te visualises en train de couper.</b> Pas le rêve de +3000. Tu absorbes la frustration.")],
]
story.append(styled_table(scenarios_data, [0.7*cm, 2.6*cm, 1.5*cm, 11.2*cm]))
story.append(Spacer(1, 12))

story.extend(concept(
    "Tu visualises ton SL touché avant de cliquer Buy. Pendant 60 à 90 secondes, tu te vois perdre exactement "
    "la somme prévue, calmement, en exécutant le SL. Ton SN apprend que cette issue est gérable. Pendant le trade, "
    "si le SL est touché, c'est juste une répétition de quelque chose de déjà vécu."
))

story.extend(miroir([
    "Toi, tu fais le contraire. Tu visualises le gain. Tu te projettes à +1500 avant même de cliquer. Tu pré-vis l'extase. "
    "Le problème : cette pré-vision charge émotionnellement le trade. Quand le marché t'offre +800, tu refuses de "
    "couper parce que tu <b>vises</b> +1500 — c'est dans ta visualisation, c'est presque acquis. Et quand le marché "
    "reverse, tu refuses d'acter parce que +1500 t'avait été mentalement promis.",
    "Le scénario 3 est le plus important pour toi. Tu prépares ton système nerveux à <b>survivre à un gros gain</b>. "
    "C'est un travail aussi important que la préparation à une grosse perte. Pour quelqu'un avec ton pattern, "
    "c'est même plus important."
]))

story.extend(action(
    "À partir de demain : <b>aucun trade exécuté sans visualisation préalable de 90 secondes</b>. Trois scénarios, "
    "dans l'ordre, à voix basse si nécessaire. C'est ton sas. Si tu n'as pas fait la visualisation, tu ne cliques pas. "
    "Tu peux attendre le prochain setup. Mais tu ne cliques pas sans le sas."
))

story.extend(journal([
    "Quand je visualise la coupe à +1500 (alors que je pourrais aller plus loin), qu'est-ce que je ressens dans le corps ?",
    "Le scénario 3 (couper à +1500 dans le plan) déclenche-t-il plus d'inconfort que le scénario 1 (perdre proprement) ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 10 ============
story.extend(chapter_header(10, "Lâcher prise", "Le paradoxe du contrôle"))

story.extend(hougaard_block([
    "Plus tu essayes de contrôler le marché, plus tu perds. Le contrôle est une illusion. Tu ne contrôles pas où va "
    "le prix. Tu ne contrôles pas qui achète, qui vend, quelles nouvelles tombent. La seule chose que tu contrôles, "
    "c'est <b>toi</b> : ton entrée, ta taille, ton SL, ton TP, et le bouton de fermeture.",
    "Le paradoxe : c'est en lâchant prise sur ce que tu ne contrôles pas que tu deviens efficace sur ce que tu "
    "contrôles. Cette posture s'appelle le « surrender opérationnel ». Tu te rends. Tu acceptes que ce trade peut "
    "perdre. Tu acceptes que tu ne sais pas. Et paradoxalement, cette acceptation te rend libre d'exécuter sereinement."
]))

story.extend(concept(
    "Le contrôle du marché n'existe pas. Plus tu serres, plus tu te brûles. La paix du trader vient d'un acte de "
    "reddition : j'accepte que je ne sais pas. Je joue mon edge, je laisse le marché faire ce qu'il fait."
))

story.append(P("Ce que tu contrôles vs ce que tu ne contrôles pas", h_section))
ctrl_data = [
    [C("✓  TU CONTRÔLES", cell_gold), C("✗  TU NE CONTRÔLES PAS", cell_gold)],
    [C("Ton point d'entrée"), C("La direction que prend le prix")],
    [C("La taille de ta position"), C("Le timing exact des mouvements")],
    [C("La position de ton SL"), C("Les nouvelles macro qui tombent")],
    [C("La position de ton TP"), C("Le comportement des autres acteurs")],
    [C("Ton respect du plan"), C("Si ce trade va être gagnant ou perdant")],
    [C("Le moment où tu fermes la plateforme"), C("La volatilité de la session")],
    [C("Ton état émotionnel avant la session"), C("Ce qui s'est passé hier sur le marché")],
]
story.append(styled_table(ctrl_data, [8*cm, 8*cm]))
story.append(Spacer(1, 12))

story.extend(miroir([
    "Toi, tu es un contrôleur. À cheval, tu contrôles le binôme. Sur ATHÉNA, tu contrôles la production. Dans ton "
    "entraînement post-coma, tu as dû reconstruire un contrôle sur un corps et un cerveau qui ne t'obéissaient plus. "
    "Le contrôle est ta stratégie de survie.",
    "Et tu importes cette stratégie en trading. Tu serres. Tu décales un SL pour ne pas perdre le contrôle. Tu refuses "
    "de couper parce que couper c'est admettre que tu ne contrôlais pas. Tu négocies avec le marché alors que le "
    "marché ne négocie pas.",
    "Le « close the platform » est puissant pour toi. Quand un trade va contre toi vers le SL : tu fermes la "
    "plateforme. Pas le trade — la plateforme. Tu te lèves. Tu sors. Le SL fait son boulot sans toi. Tu reviens "
    "30 minutes plus tard. Tu vois le résultat. C'est tout. Tu n'as pas pu interférer parce que tu n'étais pas là.",
    "Au début ça va être atroce. C'est le sevrage du contrôle. Tu l'as fait avec d'autres choses, tu peux le faire avec ça."
]))

story.extend(action(
    "Règle <b>« close the platform »</b> activée cette semaine. Dès que SL et TP sont placés, tu fermes l'application. "
    "Téléphone retourné. Tu te lèves. Tu fais autre chose : pansage, marche, tâche ATHÉNA. Tu reviens uniquement quand "
    "le trade s'est résolu (notification de SL ou TP). Trois jours d'application stricte."
))

story.extend(journal([
    "Dans quels domaines de ma vie le contrôle me sert vraiment ? Dans lesquels il me détruit ?",
    "Quand j'imagine fermer la plateforme avec un trade en cours, qu'est-ce que mon corps fait ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 11 ============
story.extend(chapter_header(11, "Ajouter aux gagnants", "Contre-instinct — mais pas encore pour toi"))

story.extend(hougaard_block([
    "Hougaard observe que les grands traders rajoutent à leurs trades <b>gagnants</b>, pas à leurs trades perdants. "
    "Tu rajoutes au gagnant quand il a déjà prouvé qu'il est dans la bonne direction, pas au perdant pour « moyenner ».",
    "Cette technique demande une discipline d'exécution irréprochable. Si tu n'as pas déjà cette discipline sur des "
    "trades simples, ajouter au gagnant va juste démultiplier tes problèmes d'exécution. Tu vas pyramider la "
    "quantité d'erreur."
]))

story.extend(concept(
    "Tu rajoutes uniquement aux trades qui ont déjà prouvé. Jamais à ceux qui essayent encore de prouver. "
    "Mais c'est une technique avancée : avant de l'utiliser, tu dois être capable de gérer un seul trade proprement. "
    "Sinon tu pyramides ton désordre."
))

story.append(P("Pour toi, à ce stade : seulement BE+1R", h_section))

# DIAGRAMME : BE+1R
story.append(Schema(7.5*cm, draw_be_1r))
story.append(P("Dès que le prix atteint +1R, tu remontes le SL à l'entrée. Downside gelé.", diagram_caption))

story.extend(miroir([
    "Tu vas être tenté de lire ce chapitre et de te dire « ah ouais c'est exactement ça qu'il me faut pour atteindre "
    "+3000 ». <b>Non.</b> À ce stade, ajouter aux gagnants serait du carburant sur ton pattern destructeur.",
    "Pour les 90 prochains jours, la seule technique « avancée » que je t'autorise est celle-ci : <b>SL au break-even "
    "dès que le trade atteint +1R</b>. Pas d'ajout. Pas de pyramide. Juste la sécurité du capital.",
    "Concrètement sur XAUUSD : tu rentres à 2 400, SL à 2 397 (3$), TP à 2 406 (6$). Dès que le prix touche 2 403 "
    "(1R en ta faveur), tu remontes manuellement ton SL à 2 400 — break-even. Le pire qui peut t'arriver est de "
    "sortir à zéro. Tu as gelé ton downside.",
    "Cette technique a un effet psychologique massif : elle <b>désamorce</b> le piège du gain perdu. Tu sais que tu "
    "ne peux plus perdre. Donc tu n'as plus besoin de défendre la position désespérément. Tu peux laisser le trade "
    "respirer jusqu'au TP sans interférer.",
    "Quand tu auras tenu cette règle 100 trades d'affilée sans la casser, on parlera d'ajouter aux gagnants. Pas avant."
]))

story.extend(action(
    "Règle <b>BE à +1R</b> non négociable pendant 90 jours. Alarme TradingView ou alerte plateforme au niveau +1R. "
    "Dès que ça sonne, tu remontes le SL à l'entrée. C'est mécanique. Tu ne discutes pas avec toi-même. "
    "Logge dans ton journal : « BE déplacé à temps : OUI/NON »."
))

story.extend(journal([
    "Quand j'imagine déplacer mon SL au BE (donc renoncer à plus de gain si ça reverse direct), qu'est-ce que je ressens ?",
    "Quelle voix intérieure dit « laisse-le tranquille » ?"
]))

story.extend(warning(
    "Si tu commences à pyramider sans avoir d'abord maîtrisé BE+1R sur 100 trades, tu vas accélérer ta destruction. "
    "Le sevrage de l'intensité passe d'abord par la simplification, pas par l'optimisation."
))
story.append(PageBreak())


# ============ CHAPITRE 12 ============
story.extend(chapter_header(12, "Couper les perdants vite", "La compétence numéro un"))

story.extend(hougaard_block([
    "Si Hougaard ne devait retenir qu'une seule compétence du trading, ce serait celle-ci. La capacité à couper ses "
    "perdants vite est l'écart le plus net entre les traders rentables et les autres. Avant la lecture du marché. "
    "Avant le money management.",
    "Une perte non coupée n'est pas linéaire. Elle a quatre effets cumulés : 1) elle prend du capital, 2) elle prend "
    "du temps mental, 3) elle prend de l'attention sur les setups suivants, 4) elle conditionne ton cerveau à "
    "accepter des pertes plus grandes au prochain tour.",
    "Le décalage de SL est la version pathologique du « ne pas couper ». C'est une <b>action</b> contre toi-même. "
    "C'est, statistiquement, le geste qui détruit le plus de comptes."
]))

story.extend(concept(
    "Couper vite n'est pas une option. C'est la compétence centrale. Le SL est sacré : tu le poses avec l'entrée, "
    "et il ne bouge que dans une direction — vers le profit, jamais loin de lui. Décaler un SL est un acte "
    "autodestructeur déguisé en patience."
))

story.append(P("Le protocole anti-décalage en 4 niveaux", h_section))

# DIAGRAMME : SL ESCALATOR
story.append(Schema(7*cm, draw_sl_escalator))
story.append(P("Tu montes les niveaux quand le précédent ne suffit plus à te tenir.", diagram_caption))

story.extend(miroir([
    "Ton pattern de décalage est documenté. Tu rentres, le trade va contre toi, tu te dis « il va revenir », tu décales "
    "« juste un peu pour lui laisser le temps ». Cette phrase est ton mensonge personnel. Le marché n'a pas besoin de temps. "
    "Le marché a besoin que tu te trompes pour empocher ton SL. Tu personnalises ce qui n'est pas personnel.",
    "Facteur aggravant : les prop firms. Apex, Topstep, Alpha Futures ont toutes des règles de drawdown qui amplifient "
    "la sanction. Tu décales un SL, le marché te tape -300, tu décales encore, -600. À -800 tu casses la règle trailing "
    "drawdown du compte Apex. Compte mort. Tu n'as pas juste perdu 800$, tu as perdu le compte. Avec les frais "
    "d'inscription tu es à -1 000 à -1 500$ réels.",
    "La prop firm utilise ce mécanisme comme business model : elle parie que des traders comme toi vont casser la "
    "règle de drawdown rapidement. Elle ne te veut pas du mal — elle exécute son edge. <b>Toi, tu peux refuser "
    "d'être le carburant.</b>",
    "Les quatre niveaux du diagramme sont un escalier que tu construis cette semaine. Tu commences par le niveau 1 "
    "(SL placé à l'entrée), et si le niveau 1 ne suffit pas, tu ajoutes le 2, puis le 3, puis le 4. Au niveau 4, "
    "tu disparais physiquement de l'écran pour ne pas pouvoir tricher."
]))

story.extend(action(
    "Implémente les quatre niveaux dès demain matin. Imprime le protocole. Affiche-le. Sur ton journal de session, "
    "en bas de chaque page, une croix verte si tu n'as pas décalé, une croix rouge si tu as décalé. Vise "
    "<b>zéro croix rouge sur 20 sessions consécutives</b>. Si tu casses une fois, tu repars à zéro. Sans drame. "
    "Mais tu repars à zéro."
))

story.extend(journal([
    "Sur mes 10 derniers décalages de SL, à quel niveau de PnL flottant je l'ai fait ? Y a-t-il un seuil récurrent ?",
    "Quelle est la phrase exacte que je me dis dans la tête au moment de décaler ? Écris-la mot pour mot.",
    "Quel serait le coût total sur 12 mois si je ne décalais plus jamais ?"
]))

story.extend(warning(
    "Le décalage qui paye une fois sur dix te conditionne plus solidement que celui qui paye à chaque fois. "
    "C'est le renforcement intermittent — la forme de conditionnement la plus puissante connue. "
    "<b>La règle est : zéro décalage. Pas même un.</b>"
))
story.append(PageBreak())


# ============ CHAPITRE 13 ============
story.extend(chapter_header(13, "Le journal", "L'outil de transformation numéro un"))

story.extend(hougaard_block([
    "Le journal de trading est l'outil de transformation le plus puissant à la disposition du trader. Pas un journal "
    "de PnL — n'importe quel logiciel fait ça. Un journal <b>introspectif</b>, manuscrit, où tu écris ton état "
    "émotionnel avant, pendant et après chaque trade.",
    "Pourquoi manuscrit ? L'acte d'écrire à la main mobilise différemment le cerveau que la frappe au clavier. "
    "Tu écris plus lentement, donc tu réfléchis plus profondément. Tu peux moins fuir.",
    "Le journal sert trois fonctions : <b>1)</b> acter ce qui s'est passé (mémoire externe), <b>2)</b> repérer tes "
    "patterns à travers le temps, <b>3)</b> construire l'identité du trader que tu deviens (en t'observant écrire, "
    "tu deviens cette personne)."
]))

story.extend(concept(
    "Pas de journal manuscrit, pas de transformation. C'est aussi simple que ça. Tout le reste est consommation "
    "passive de contenu. Le journal est le seul endroit où ta tête se rencontre vraiment, et où le changement "
    "peut s'enraciner."
))

story.extend(miroir([
    "Toi, tu prends des notes sur ton téléphone, parfois. Ou rien. Ou tu te promets de tenir un journal et tu craques "
    "après trois jours. C'est l'erreur classique. Tu rates l'outil qui est précisément celui dont tu as besoin.",
    "Tu vas acheter un <b>vrai cahier</b>, pas un carnet bas de gamme. Cuir, papier épais, ce que tu veux mais que "
    "tu respectes. Sur la page de couverture intérieure : « Cahier de Marien, trader chirurgical en formation. "
    "Ouvert le [date]. » Ce cahier devient sacré.",
    "Le template à utiliser est en annexe à la fin de ce document. Tu le recopies à la main au début. Pas de tablette, "
    "pas de Notion, pas d'Excel.",
    "Pour quelqu'un qui pratique Joe Dispenza, le journal est la version écrite de ta méditation : c'est l'observation "
    "consciente de tes patterns en mode écrit. Tu installes la position d'observateur. À force, tu deviens cet "
    "observateur même pendant le trade — et c'est là que tu reprends le contrôle de tes décisions."
]))

story.extend(action(
    "Cette semaine : tu achètes le cahier. Tu recopies à la main la première page du template d'annexe. "
    "Tu remplis le journal à chaque session — sans exception — pendant les six semaines à venir. Si tu skip une "
    "session, tu ne trades pas la suivante. Pas négociable. Le journal est la condition d'accès à l'écran."
))

story.extend(journal([
    "Quel cahier je vais choisir ? Vais-je le prendre au sérieux ou est-ce que je vais saboter cet outil aussi ?",
    "Quelle est ma résistance face à écrire à la main mes émotions ? Honte, paresse, peur de me voir ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 14 ============
story.extend(chapter_header(14, "L'inner game", "Le vrai adversaire est intérieur"))

story.extend(hougaard_block([
    "L'idée de l'inner game vient du tennis (Timothy Gallwey) : l'adversaire que tu affrontes n'est pas l'extérieur "
    "(l'autre joueur, le marché) mais une voix intérieure qui te commente, te juge, te déstabilise.",
    "Cette voix est constamment active. En trading elle te dit « tu vas le rater », « tu vas exploser », ou "
    "inversement « tu maîtrises, tu peux y aller plus fort ». Les deux versions sont des interférences.",
    "Le but n'est pas de faire taire cette voix — c'est impossible. C'est d'apprendre à <b>l'observer sans lui "
    "obéir</b>. Tu l'entends parler, tu la reconnais, tu continues à exécuter ton protocole."
]))

# DIAGRAMME : INNER VOICE
story.append(Spacer(1, 4))
story.append(Schema(8*cm, draw_inner_voice))
story.append(P("Les bulles parlent en boucle. Tu n'as pas à les croire pour les entendre.", diagram_caption))

story.extend(concept(
    "Ton adversaire n'est pas le marché. C'est la voix dans ta tête qui commente le marché. Le jeu intérieur "
    "consiste à entendre cette voix sans lui obéir. Tu la prends en flagrant délit. Tu la nommes. Tu la regardes "
    "parler. Et tu cliques selon ton plan, pas selon elle."
))

story.extend(miroir([
    "Le diagramme du dessus est une version condensée de ta voix typique en trade. Elle est rapide, crédible "
    "parce qu'elle <b>est toi</b> — du moins une partie de toi. Elle te ment à chaque phrase, mais sur le ton "
    "de l'évidence.",
    "Le travail pour toi : apprendre à entendre cette voix comme une radio qui passe en arrière-plan. Pas comme la "
    "commande de l'avion. Tu peux dire à voix basse pendant le trade : « j'entends ma voix qui veut que je laisse "
    "courir, je la note, et j'exécute mon plan ». Cette phrase casse l'identification. Tu n'es plus la voix. "
    "Tu es la conscience qui écoute la voix.",
    "La méditation Dispenza t'a déjà entraîné à cette posture. Quand tu observes tes pensées sans les suivre, c'est "
    "exactement le même muscle. Le problème : tu n'utilises pas ce muscle devant l'écran. Tu médites le matin, "
    "tu deviens un junkie l'après-midi. Il faut que ce soit le <b>même</b> Marien dans les deux contextes."
]))

story.extend(action(
    "Pendant tes trades cette semaine, dis à voix basse — vraiment à voix basse — une phrase au moment des "
    "déclencheurs : « j'entends la voix, je continue le plan » ou simplement « voix notée ». L'intérêt n'est pas "
    "la phrase. L'intérêt est la rupture entre toi et ta voix. Cette distance est le siège de la liberté."
))

story.extend(journal([
    "Si je devais nommer la voix qui me parle pendant les trades, comment je l'appellerais ? (Donne-lui un nom.)",
    "Cette voix a-t-elle l'âge de Marien aujourd'hui, ou celui de Marien adolescent ? À quel moment elle s'est installée ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 15 ============
story.extend(chapter_header(15, "Devenir le trader", "Le changement identitaire en trois niveaux"))

story.extend(hougaard_block([
    "Hougaard rejoint James Clear (<i>Atomic Habits</i>) : les niveaux de transformation sont superposés, et seul le "
    "plus profond produit du changement durable.",
    "<b>Niveau 1 — Résultat.</b> Tu vises un résultat (« je veux gagner 10 000€ ce mois »). Le plus instable. "
    "Tu ne le contrôles pas. Tu peux faire tout juste et le rater.",
    "<b>Niveau 2 — Processus.</b> Tu vises un processus (« j'exécute mon protocole 100 trades »). Plus stable. "
    "Mais tient tant que tu te récompenses pour le résultat.",
    "<b>Niveau 3 — Identité.</b> Tu deviens quelqu'un dont le processus est l'expression naturelle. « Je suis un "
    "trader chirurgical. » À ce niveau, le processus ne demande plus de discipline — il demande de la cohérence "
    "avec qui tu es."
]))

# DIAGRAMME : IDENTITY PYRAMID
story.append(Spacer(1, 4))
story.append(Schema(9.5*cm, draw_identity_pyramid))
story.append(P("Plus tu descends vers la base de la pyramide, plus le changement est profond et durable.", diagram_caption))

story.extend(concept(
    "Tu ne deviens pas un trader rentable en gagnant de l'argent. Tu gagnes de l'argent parce que tu es devenu un "
    "trader rentable. L'ordre compte. Identité d'abord, comportement ensuite, résultat enfin. Pas l'inverse."
))

story.extend(miroir([
    "Ton identité de trader est instable. Quand tu gagnes, tu es « un trader qui réussit ». Quand tu perds, tu es "
    "« un trader qui galère ». Ton identité fluctue avec ton PnL. L'opérateur change selon le résultat de l'opération "
    "précédente.",
    "Identité cible proposée : <b>« Je suis un trader chirurgical. »</b> Chirurgical = précis, calme, ennuyeux à "
    "observer de l'extérieur, exécution propre, pas de geste superflu, pas d'émotion visible. Un chirurgien ne « croit » "
    "pas qu'une opération va marcher. Il ouvre, il fait le geste prévu, il referme.",
    "Quand tu adoptes cette identité, plusieurs choses deviennent <b>cohérentes</b>. Un chirurgien ne double pas sur "
    "une perte. Ça n'a aucun sens. Un chirurgien ne décale pas son SL. Tu vois comment l'identité résout le problème "
    "de discipline ? Tu n'as pas à te forcer. C'est juste qui tu es.",
    "Chaque fois que tu coupes un SL sans le décaler, tu déposes un vote pour cette identité. Chaque fois que tu prends "
    "ton TP sans le pousser, tu déposes un vote. À force de votes, l'identité devient majoritaire.",
    "Tu l'as déjà fait pour l'équitation. Tu ne t'es pas réveillé un matin cavalier compétitif. Tu as fait des milliers "
    "d'heures, et à un moment l'identité « cavalier » est devenue ta vérité, pas un projet. Le trading suit la même loi."
]))

story.extend(action(
    "Écris dans ton journal cette phrase, en majuscules, sur une page dédiée : "
    "<b>« JE SUIS UN TRADER CHIRURGICAL. »</b> "
    "Avant chaque session, relis. Avant chaque trade, demande-toi : « est-ce qu'un trader chirurgical ferait ce clic ? ». "
    "Si la réponse est non, tu ne cliques pas. Tu attends le clic dont la réponse est oui."
))

story.extend(journal([
    "Quelle identité de trader je porte actuellement, sans m'en rendre compte ?",
    "Si je devenais un trader chirurgical à 30 ans (donc dans cinq ans), quelle première décision je dois prendre "
    "aujourd'hui pour que ça soit possible ?"
]))
story.append(PageBreak())


# ============ CHAPITRE 16 ============
story.extend(chapter_header(16, "Conclusion", "Les dix principes finaux"))

story.extend(hougaard_block([
    "En clôture, Hougaard récapitule sa pensée en une série de principes. Aucun ne te dit comment lire un graphique. "
    "Tous te disent comment <b>te tenir</b> face au marché."
]))

story.append(P("Les dix principes en synthèse rapide", h_section))

principles_data = [
    [C("#", cell_gold), C("Principe", cell_gold), C("Application Marien", cell_gold)],
    [C("1", cell_bold), C("L'edge n'est pas dans la méthode", cell_bold), C("Ta méthode SMC est suffisante. Le levier est dans l'exécution.")],
    [C("2", cell_bold), C("Tu joues une distribution", cell_bold), C("Tu ne sais pas si celui-là va gagner. Tu sais ce que donne ta série.")],
    [C("3", cell_bold), C("Tes pertes sont sacrées", cell_bold), C("Ce qui définit un grand trader, c'est comment il perd. Petit, vite, calme.")],
    [C("4", cell_bold), C("Ton SL ne se touche pas", cell_bold), C("Sauf pour le serrer vers le profit. Jamais l'éloigner.")],
    [C("5", cell_bold), C("Tu n'es pas tes trades", cell_bold), C("Un trade qui rate n'est pas Marien qui rate. Sépare résultat et identité.")],
    [C("6", cell_bold), C("Tu pré-vis la perte", cell_bold), C("Avant chaque clic, scénarios visualisés. Sas non négociable.")],
    [C("7", cell_bold), C("Tu fermes la plateforme", cell_bold), C("SL/TP placés, tu sors physiquement. Tu laisses faire.")],
    [C("8", cell_bold), C("Tu tiens un journal manuscrit", cell_bold), C("Chaque session, chaque trade. C'est ton outil principal.")],
    [C("9", cell_bold), C("Tu nourris une vie hors écran", cell_bold), C("ATHÉNA, chevaux, box, relations. Vie plate = trader saboteur.")],
    [C("10", cell_bold), C("Tu deviens, tu ne forces pas", cell_bold), C("Trader chirurgical n'est pas un objectif. C'est l'identité que tu installes.")],
]
story.append(styled_table(principles_data, [0.7*cm, 5.3*cm, 10*cm]))
story.append(Spacer(1, 12))

story.extend(concept(
    "Tu as maintenant lu ce que dit Hougaard. La phase suivante n'est plus dans les pages. Elle est dans le cahier, "
    "devant l'écran, et dans tes décisions du jour. Le livre est terminé. Ton vrai travail commence."
))

story.extend(miroir([
    "Tu es au bout des seize chapitres. Si tu as appliqué un par un, tu as déjà commencé à devenir quelqu'un d'autre. "
    "Si tu as juste lu en diagonale, tu n'as rien changé — tu as juste ajouté un livre à ta bibliothèque.",
    "Ce qui suit dans ce document est la cartographie pratique des 90 prochains jours. Si tu sautes cette partie, "
    "tout ce qui précède est intellectuel. C'est dans la suite que tout se joue."
]))
story.append(PageBreak())


# ============================================================
# SYNTHÈSE — LES 10 COMMANDEMENTS DE MARIEN
# ============================================================
story.append(P("SYNTHÈSE", h_chapter))
story.append(P("Les dix commandements de Marien", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "À imprimer en grand, à scotcher au-dessus de ton écran, à relire à voix haute chaque matin avant la session. "
    "Si tu trouves ça ridicule, tant mieux : ton cerveau émotionnel n'a pas honte du ridicule, il a juste besoin d'ancrage."
))
story.append(Spacer(1, 14))

commandments = [
    ("I",   "Ma méthode est suffisante. Je suis le problème, et je suis aussi la solution.",
     "SMC + killzones + risk fixe = système viable. Le levier n'est pas technique. Il est dans ma main qui clique."),
    ("II",  "Je joue une série, jamais un trade.",
     "Cent setups exécutés proprement. Je ne tire aucune conclusion avant cent. Je suis le casino, pas le joueur."),
    ("III", "Mon stop loss est sacré et ne bouge jamais vers la perte.",
     "Placé avec l'entrée. Déplacé uniquement vers le BE à +1R, puis vers le profit. Jamais agrandi."),
    ("IV",  "Je coupe à mon TP. Point.",
     "Le piège +1500 est ma signature destructrice. Je le casse en respectant le TP préfixé."),
    ("V",   "Je pré-vis chaque trade pendant 90 secondes avant de cliquer.",
     "Trois scénarios : perte propre, gain propre, gain qui dépasse mon TP et que je coupe quand même."),
    ("VI",  "Je ferme la plateforme dès que les ordres sont placés.",
     "Une fois SL et TP en place, je me lève. Je sors de la pièce. Je laisse le trade respirer sans moi."),
    ("VII", "J'écris mon journal manuscrit à chaque session, sans exception.",
     "Pas de journal = pas de session le lendemain. C'est la condition d'accès à l'écran."),
    ("VIII","Je ne consomme aucun contenu trading hors application.",
     "Pas de nouvelle vidéo, pas de nouveau mentor. Six semaines de purge. J'applique, point."),
    ("IX",  "Je nourris ma vie hors écran chaque jour.",
     "ATHÉNA, chevaux, ma filly, box, lectures, relations, soleil. Vie plate = trader saboteur."),
    ("X",   "Je suis un trader chirurgical. Ce n'est pas un objectif, c'est qui je deviens.",
     "Chaque clic est un vote. Je vote pour cette identité, ou contre. Pas d'entre-deux."),
]

cmd_style_roman = ParagraphStyle("cmd_roman", fontName="DejaVu-Serif-Bold", fontSize=20,
    textColor=GOLD, alignment=TA_CENTER, leading=22)
cmd_style_title = ParagraphStyle("cmd_title", fontName="DejaVu-Bold", fontSize=11, leading=14,
    textColor=DARK_BG, alignment=TA_LEFT)
cmd_style_detail = ParagraphStyle("cmd_detail", fontName="DejaVu", fontSize=9.5, leading=13,
    textColor=MID_GREY, alignment=TA_JUSTIFY)

cmd_rows = []
for roman, titre, detail in commandments:
    cmd_rows.append([
        Paragraph(roman, cmd_style_roman),
        [Paragraph(titre, cmd_style_title), Spacer(1, 3), Paragraph(detail, cmd_style_detail)]
    ])

t = Table(cmd_rows, colWidths=[1.6*cm, 14.4*cm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 10),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ("LINEBELOW", (0, 0), (-1, -2), 0.4, GOLD_SOFT),
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
]))
story.append(t)

story.append(Spacer(1, 14))
story.append(P(
    "Imprime cette liste. Plastifie-la si tu veux. Mais qu'elle soit visible. Tous les jours.",
    body_italic
))
story.append(PageBreak())


# ============================================================
# PLAN D'ACTION 90 JOURS
# ============================================================
story.append(P("PLAN D'ACTION", h_chapter))
story.append(P("90 jours pour devenir un autre trader", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

# DIAGRAMME : TIMELINE
story.append(Schema(6.5*cm, draw_90_timeline))
story.append(P("Trois phases. Tu ne passes à la suivante que si tu valides la précédente.", diagram_caption))

story.append(P(
    "Trois phases de 30 jours. Chacune a un objectif spécifique, des règles de trading précises, un travail "
    "psychologique dédié, des soins du corps, et des métriques claires. <b>Si tu rates les métriques d'une phase, "
    "tu ne passes pas à la suivante. Tu refais la phase.</b>"
))
story.append(Spacer(1, 8))


# ---- PHASE 1 ----
story.append(P("Phase 1 — Jours 1 à 30", phase_title))
story.append(P("Sevrage et fondations", h_section))

phase1_data = [
    [C("Domaine", cell_gold), C("Contenu", cell_gold)],
    [C("Objectif", cell_bold),
     C("Casser les automatismes destructeurs. Sevrer du shoot. Installer les routines de base.")],
    [C("Trading semaines 1-2", cell_bold),
     C("Arrêt total. Aucun ordre passé. Aucune connexion Apex/Topstep/Alpha. Apps désinstallées du téléphone.")],
    [C("Trading semaines 3-4", cell_bold),
     C("Démo uniquement. Protocole strict : SL non négociable, BE+1R, TP fixe, close the platform. 30 trades minimum sans décalage.")],
    [C("Psychologie", cell_bold),
     C("Un chapitre tous les 2 jours. Action concrète appliquée. Cahier ouvert jour 1. 15 min écriture chaque soir. Méditation Dispenza 20 min/matin.")],
    [C("Corps", cell_bold),
     C("3 séances physiques intenses/semaine min (box, équitation cross, sport explosif). Couché avant 23h. Pas de téléphone après 22h.")],
    [C("Validation pour passer", cell_bold),
     C("30 jours sans trade réel. 30 trades démo selon protocole. Zéro décalage SL. Journal rempli 28/30 jours min. Méditation 25/30 jours min.")],
]
story.append(styled_table(phase1_data, [4.3*cm, 11.7*cm]))
story.append(Spacer(1, 10))

story.extend(warning(
    "Si à J+30 tu as triché — même une fois sur un compte réel — tu reprends la phase 1 à zéro. Pas par punition. "
    "Parce que la phase 1 a pour seul objectif de désinstaller le réflexe. Si l'envie a gagné une fois, le réflexe "
    "est encore là. Non négociable."
))
story.append(PageBreak())


# ---- PHASE 2 ----
story.append(P("Phase 2 — Jours 31 à 60", phase_title))
story.append(P("Transition réel", h_section))

phase2_data = [
    [C("Domaine", cell_gold), C("Contenu", cell_gold)],
    [C("Objectif", cell_bold),
     C("Repasser en réel avec exposition contrôlée. Installer le comportement où le PnL réactive les circuits dopaminergiques.")],
    [C("Trading", cell_bold),
     C("UN seul compte prop firm. Le plus petit possible. 1 à 2 trades XAUUSD/session max. Risque 0,5% du compte par trade. SL+TP préfixés. BE+1R. Plateforme fermée.")],
    [C("Stop sessions", cell_bold),
     C("3 pertes consécutives dans une session → arrêt immédiat. 2 pertes consécutives dans une semaine → pause complète d'une journée.")],
    [C("Psychologie", cell_bold),
     C("Relecture ch 7, 11, 12, 15. Journal obligatoire (sinon pas de session demain). Visualisation 90s systématique. Méditation maintenue.")],
    [C("Corps", cell_bold),
     C("3 séances physiques min/semaine. Suivi sommeil. Si dégradation neuro-vag : pause trading 48h.")],
    [C("Validation pour passer", cell_bold),
     C("30 jours sans casser une règle prop firm. Zéro décalage SL sur toute la phase. BE+1R systématique. Aucune session sans journal (28/30 min). PnL non pertinent — seul le protocole compte.")],
]
story.append(styled_table(phase2_data, [4.3*cm, 11.7*cm]))
story.append(Spacer(1, 10))

story.extend(concept(
    "En phase 2, tu ne juges pas ta réussite à ton PnL. Tu la juges à ton respect du protocole. "
    "Si tu respectes à 100% et que tu es en perte de 5%, tu as réussi. Si tu casses le protocole une fois et que "
    "tu es en profit de 10%, tu as raté. Protocole d'abord."
))
story.append(PageBreak())


# ---- PHASE 3 ----
story.append(P("Phase 3 — Jours 61 à 90", phase_title))
story.append(P("Consolidation et décision", h_section))

phase3_data = [
    [C("Domaine", cell_gold), C("Contenu", cell_gold)],
    [C("Objectif", cell_bold),
     C("Ancrer l'identité du trader chirurgical. Décider à J+90 comment scaler. Phase identitaire, pas technique.")],
    [C("Trading", cell_bold),
     C("Continuation des règles phase 2 sur le compte unique. Si funded en fin de phase 2 : exécution sur funded, mêmes règles. Pas d'augmentation de taille avant J+90.")],
    [C("À partir de J+75", cell_bold),
     C("Possibilité de tester « ajouter aux gagnants » <b>en démo seulement</b>. Pas en réel avant J+90.")],
    [C("Psychologie", cell_bold),
     C("Relecture quotidienne des 10 commandements. Question journalière dans le journal : « Aujourd'hui, j'ai voté pour le trader chirurgical, ou contre ? »")],
    [C("Travail somatique", cell_bold),
     C("Envisager un thérapeute spécialisé trauma. Le TBI 2022 a probablement laissé des séquelles régulatrices que la méditation seule ne résoudra pas. TRE, somatic experiencing.")],
    [C("Corps", cell_bold),
     C("Maintien et progression. Reprise compétitions équestres si possible. ATHÉNA prend plus de place. Le trading occupe MOINS d'espace mental relatif.")],
]
story.append(styled_table(phase3_data, [4.3*cm, 11.7*cm]))
story.append(Spacer(1, 12))

story.append(P("Les 3 questions à J+90", h_section))
decision_data = [
    [C("#", cell_gold), C("Question", cell_gold)],
    [C("1", cell_bold), C("Suis-je devenu le trader chirurgical ? (oui / partiellement / non, avec preuves dans le journal)")],
    [C("2", cell_bold), C("Mon protocole est-il rentable sur 90 jours ? (analyse honnête du PnL, sans excuses)")],
    [C("3", cell_bold), C("Ai-je trouvé une vie hors écran qui me nourrit ? (ATHÉNA, chevaux, box, relations — concret)")],
]
story.append(styled_table(decision_data, [0.8*cm, 15.2*cm]))
story.append(Spacer(1, 10))

story.append(P(
    "Selon les réponses : tu scales (taille augmentée, deuxième compte, ajout au gagnant), tu prolonges la phase 3 "
    "de 30 jours, ou tu reviens à la phase 2. Pas d'orgueil dans la décision. C'est de l'ingénierie."
))
story.append(Spacer(1, 10))

story.extend(miroir([
    "À J+90, ce qui aura changé n'est pas seulement ton PnL. C'est l'opérateur. Le Marien qui tradera ce jour-là "
    "ne sera plus celui qui a cramé son dernier compte. Il aura 90 jours de comportement aligné derrière lui. "
    "C'est ça la vraie richesse de la phase. Pas l'argent — la transformation du décideur. L'argent suit toujours "
    "le décideur."
]))
story.append(PageBreak())


# ============================================================
# ANNEXE — TEMPLATE DE JOURNAL
# ============================================================
story.append(P("ANNEXE", h_chapter))
story.append(P("Template de journal manuscrit", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Voici les quatre sections à recopier à la main au début de ton cahier, puis à reproduire à chaque session. "
    "Reproduis-les exactement. Le copier-coller mental tue le journal. La main qui trace les questions fait partie "
    "du processus."
))
story.append(Spacer(1, 10))

# ---- Avant session ----
story.append(P("AVANT SESSION  —  5 minutes", h_section))
avant_data = [
    [C("Champ", cell_gold), C("À remplir", cell_gold)],
    [C("Date", cell_bold), C("____")],
    [C("État émotionnel (1 à 10)", cell_bold), C("____")],
    [C("Qualité du sommeil", cell_bold), C("____")],
    [C("Niveau d'énergie", cell_bold), C("____")],
    [C("Killzone visée", cell_bold), C("London / NY")],
    [C("Bias macro XAUUSD", cell_bold), C("____")],
    [C("Setup que je guette", cell_bold), C("____")],
    [C("Taille max autorisée", cell_bold), C("____")],
    [C("Phrase d'ancrage", cell_bold), C("Je suis un trader chirurgical.")],
    [C("Engagement de session", cell_bold), C("Aucun décalage de SL. BE à +1R systématique. TP fixe.")],
]
story.append(styled_table(avant_data, [6*cm, 10*cm]))
story.append(Spacer(1, 14))

# ---- Pour chaque trade ----
story.append(P("POUR CHAQUE TRADE", h_section))
trade_data = [
    [C("Champ", cell_gold), C("À remplir", cell_gold)],
    [C("Heure d'entrée", cell_bold), C("____")],
    [C("Direction", cell_bold), C("Long / Short")],
    [C("Prix d'entrée / SL / TP", cell_bold), C("____ / ____ / ____")],
    [C("Taille", cell_bold), C("____")],
    [C("Justification SMC (1 phrase)", cell_bold), C("____")],
    [C("Visualisation 90s faite ?", cell_bold), C("OUI / NON")],
    [C("État corps à l'entrée", cell_bold), C("____")],
    [C("BE déplacé à +1R ?", cell_bold), C("OUI / NON / N/A")],
    [C("Résultat", cell_bold), C("TP / SL / BE / Manuel (pourquoi ?)")],
    [C("Décalage SL ?", cell_bold), C("OUI (raison) / NON")],
    [C("Plateforme fermée après ordres ?", cell_bold), C("OUI / NON")],
    [C("État corps à la sortie", cell_bold), C("____")],
]
story.append(styled_table(trade_data, [6*cm, 10*cm]))
story.append(PageBreak())

# ---- Après session ----
story.append(P("APRÈS SESSION  —  10 minutes", h_section))
apres_data = [
    [C("Champ", cell_gold), C("À remplir", cell_gold)],
    [C("Nombre de trades", cell_bold), C("____")],
    [C("Gagnants / Perdants", cell_bold), C("____ / ____")],
    [C("PnL session", cell_bold), C("____")],
    [C("Protocole respecté à 100% ?", cell_bold), C("OUI / NON (détails)")],
    [C("Pattern destructeur déclenché ?", cell_bold), C("P1 / P2 / P3 / P4 / P5 / aucun")],
    [C("Voix intérieure dominante", cell_bold), C("____")],
    [C("Émotion la plus présente", cell_bold), C("____")],
    [C("Une chose à corriger demain", cell_bold), C("____")],
    [C("Une chose à célébrer", cell_bold), C("____")],
    [C("Vote du jour", cell_bold), C("Trader chirurgical / Trader émotionnel")],
]
story.append(styled_table(apres_data, [6*cm, 10*cm]))
story.append(Spacer(1, 14))

# ---- Revue hebdomadaire ----
story.append(P("REVUE HEBDOMADAIRE  —  30 minutes, dimanche soir", h_section))
revue_data = [
    [C("Champ", cell_gold), C("À remplir", cell_gold)],
    [C("Semaine du", cell_bold), C("____")],
    [C("Sessions / Trades", cell_bold), C("____ / ____")],
    [C("Win rate", cell_bold), C("____")],
    [C("PnL semaine", cell_bold), C("____")],
    [C("Pattern destructeur le plus fréquent", cell_bold), C("____")],
    [C("Vote de la semaine", cell_bold), C("Chirurgical : ____ / Contre : ____")],
    [C("3 leçons de la semaine", cell_bold), C("____")],
    [C("Engagement principal pour la semaine prochaine", cell_bold), C("____")],
    [C("État du corps (sommeil/énergie/SN)", cell_bold), C("____")],
    [C("Vie hors écran (qualité, quantité)", cell_bold), C("____")],
    [C("Méditation (sessions tenues)", cell_bold), C("____ / 7")],
]
story.append(styled_table(revue_data, [6*cm, 10*cm]))
story.append(Spacer(1, 14))

story.append(P(
    "Le journal n'est pas joli. Il n'a pas besoin de l'être. Il a besoin d'être <b>fait</b>. Si tu écris mal, "
    "c'est OK. Si tu raies, c'est OK. Mais tu fais.", body_italic
))
story.append(PageBreak())


# ============================================================
# MOT DE LA FIN
# ============================================================
story.append(P("MOT DE LA FIN", h_chapter))
story.append(P("Pour Marien, mai 2026", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 16))

story.append(P(
    "Tu es arrivé à la dernière page d'un document qui ne devait pas exister. Le livre que tu voulais lire en français "
    "n'existe pas. Alors on a fait mieux : on a fait celui qui te parle à toi. Pas à un trader moyen. Pas à un débutant. "
    "À toi, Marien, 25 ans, retour de coma, prop firm, XAUUSD, ATHÉNA, ta filly, ton ambition, ton intensité, "
    "tes patterns destructeurs, et ta part qui veut autre chose."
))
story.append(Spacer(1, 6))

story.append(P(
    "Si tu n'as retenu qu'une seule idée de tout ce que tu as lu, retiens celle-ci : "
    "<b>tu n'as pas un problème de méthode, tu as un problème d'identité.</b> "
    "Et l'identité, ça se sculpte. Pas en un week-end. Pas en un mois. En milliers de petits gestes alignés "
    "avec qui tu décides de devenir."
))
story.append(Spacer(1, 6))

story.append(P(
    "Tu as 25 ans. Tu aurais pu en avoir zéro. En 2022 quelque chose a presque tout fauché. Et tu es là. Tu tiens debout. "
    "Tu trades. Tu construis une boîte. Tu sautes des obstacles. Tu fais des affirmations. Tu te bats avec un système "
    "nerveux qui n'a pas envie de coopérer. Et tu continues. C'est déjà énorme. Ne le banalise pas pour aller chercher "
    "la preuve suivante. La preuve, c'est toi qui lis cette phrase. Tout le reste n'est qu'élaboration."
))
story.append(Spacer(1, 6))

story.append(P(
    "Le trading n'est pas ta valeur. C'est un métier. C'est une compétence. Quand tu la possèdes, elle te donne de la "
    "liberté. Quand elle te possède, elle te bouffe. Aujourd'hui elle te bouffe. Dans 90 jours, si tu fais le travail, "
    "l'équilibre commencera à basculer. Dans un an, si tu maintiens la cohérence, tu seras quelqu'un que ton « toi "
    "de 2024 » n'aurait pas reconnu en bien."
))
story.append(Spacer(1, 6))

story.append(P(
    "Continue à monter à cheval. Continue à boxer. Continue ATHÉNA — c'est un beau projet, il a une logique propre, "
    "tu peux y faire ce que tu n'as pas pu faire dans le trading : construire patiemment quelque chose qui se cumule "
    "au lieu de se cramer. Le 3D printing equestrian, personne d'autre ne va le faire avec ta sensibilité. C'est rare. "
    "Protège-le."
))
story.append(Spacer(1, 6))

story.append(P(
    "Et ta filly. Tu la regardes, elle te regarde. Vous êtes deux jeunes êtres en construction. Elle apprend à faire "
    "confiance. Toi aussi, à ta façon. Ne néglige pas ce binôme pendant que tu construis le trader. Les chevaux ont "
    "une fonction régulatrice neuro-vagale documentée. Ce n'est pas du folklore. Le pansage, la respiration partagée, "
    "le calme imposé par le rythme animal — tout ça travaille pour toi, même quand tu ne trades pas."
))
story.append(Spacer(1, 6))

story.append(P(
    "Une dernière chose. Tu vas peut-être te dire que tu es en retard, que tu as déjà cramé X comptes, perdu Y temps, "
    "qu'à 25 ans tu devrais déjà avoir réussi. C'est faux. Tu n'es pas en retard. Tu es <b>à l'heure</b>. Le calendrier "
    "de ta vie n'est pas celui de Twitter trading. Tu as un coma derrière toi, un système nerveux qui se reconstruit, "
    "une intelligence rare, une ambition intacte, et désormais une méthode psychologique sérieuse à appliquer. "
    "C'est largement assez pour les vingt prochaines années."
))
story.append(Spacer(1, 6))

story.append(P(
    "Va, applique, échoue parfois, reprends, écris dans ton cahier, ferme la plateforme, rentre chez toi, monte à cheval, "
    "dors sept heures, et reviens demain avec la même intention. C'est tout. C'est tout ce qu'il y a à faire."
))
story.append(Spacer(1, 14))

story.append(P('« Les meilleurs traders ne gagnent pas mieux. Ils perdent mieux. »', pull_quote))
story.append(Spacer(1, 4))
story.append(P("Et toi, à partir d'aujourd'hui, tu fais partie de ceux qui apprennent à perdre mieux.", body_center))
story.append(Spacer(1, 30))

story.append(P("— Fin du document —", ParagraphStyle("end", fontName="DejaVu-Italic", fontSize=11,
    textColor=MID_GREY, alignment=TA_CENTER)))


# ---------- BUILD ----------
def on_first_page(canv, doc): cover_page(canv, doc)
def on_later_pages(canv, doc): standard_page(canv, doc)

doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
print(f"✓ PDF généré : {OUTPUT}")
