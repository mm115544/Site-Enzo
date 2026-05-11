# -*- coding: utf-8 -*-
"""
DEVENIR UN TRADER STABLE — Manuel personnel de transformation mentale
Pour Marien.
Toutes les analyses sont des paraphrases pédagogiques originales de concepts
généraux des champs (neurosciences, polyvagal, behavioral finance, etc.),
personnalisées au profil de Marien. Aucune reproduction de livre.
"""

import math
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Flowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# ---------- FONTS ----------
pdfmetrics.registerFont(TTFont("DV", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-Italic", "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DV-Serif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DV-Serif-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-Mono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))
registerFontFamily("DV", normal="DV", bold="DV-Bold", italic="DV-Italic")

# ---------- COULEURS PREMIUM ----------
GOLD       = HexColor("#C9A14A")
GOLD_DEEP  = HexColor("#9E7B30")
GOLD_PALE  = HexColor("#E8D8A8")
NAVY       = HexColor("#1A2842")
NAVY_DEEP  = HexColor("#0F1A2E")
SLATE      = HexColor("#3A4458")
MID_GREY   = HexColor("#6A7080")
LIGHT_GREY = HexColor("#E8E8E8")
PAPER      = HexColor("#FAF7F0")
TEXT       = HexColor("#1A1A1A")
RED_ACC    = HexColor("#A8392A")
RED_SOFT   = HexColor("#E8C0B5")
GREEN      = HexColor("#2D5016")
GREEN_SOFT = HexColor("#C5DAB5")
PURPLE     = HexColor("#3A2A4A")
CREAM      = HexColor("#F5EFE0")
WARM_BG    = HexColor("#FBF5E8")

# Part accent colors
PART_COLORS = [
    HexColor("#C9A14A"),  # 1 perdre - or
    HexColor("#B8642E"),  # 2 dopamine - cuivre
    HexColor("#7B3E5C"),  # 3 trauma - prune
    HexColor("#A04A2C"),  # 4 décharger - terracotta
    HexColor("#2D6A8E"),  # 5 probabiliste - bleu
    HexColor("#5C7A3E"),  # 6 corps dit stop - vert sauge
    HexColor("#8A5F2E"),  # 7 habitudes - bronze
    HexColor("#4A3E6E"),  # 8 lâcher prise - indigo
    HexColor("#2E6A5C"),  # 9 argent - vert profond
]

# ---------- STYLES ----------
body = ParagraphStyle("body", fontName="DV", fontSize=10.3, leading=14.5,
    textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=7)
body_c = ParagraphStyle("body_c", parent=body, alignment=TA_CENTER)
body_i = ParagraphStyle("body_i", parent=body, fontName="DV-Italic")
body_w = ParagraphStyle("body_w", parent=body, textColor=white)

cell = ParagraphStyle("cell", fontName="DV", fontSize=9, leading=12,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=0)
cell_b = ParagraphStyle("cell_b", parent=cell, fontName="DV-Bold")
cell_g = ParagraphStyle("cell_g", parent=cell, fontName="DV-Bold", textColor=GOLD)
cell_w = ParagraphStyle("cell_w", parent=cell, textColor=white)
cell_wb = ParagraphStyle("cell_wb", parent=cell_w, fontName="DV-Bold")

h_part = ParagraphStyle("h_part", fontName="DV-Serif-Bold", fontSize=28, leading=32,
    textColor=GOLD, alignment=TA_LEFT, spaceAfter=4)
h_part_sub = ParagraphStyle("h_part_sub", fontName="DV-Italic", fontSize=13, leading=17,
    textColor=MID_GREY, alignment=TA_LEFT, spaceAfter=18)
h_concept = ParagraphStyle("h_concept", fontName="DV-Serif-Bold", fontSize=15, leading=19,
    textColor=NAVY, alignment=TA_LEFT, spaceBefore=10, spaceAfter=6)
h_section = ParagraphStyle("h_section", fontName="DV-Bold", fontSize=12, leading=15,
    textColor=GOLD_DEEP, alignment=TA_LEFT, spaceBefore=10, spaceAfter=5)
h_sub = ParagraphStyle("h_sub", fontName="DV-Bold", fontSize=10.5, leading=13,
    textColor=SLATE, alignment=TA_LEFT, spaceBefore=4, spaceAfter=2)

cover_main = ParagraphStyle("cm", fontName="DV-Serif-Bold", fontSize=44, leading=48,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10)
cover_sub = ParagraphStyle("cs", fontName="DV-Italic", fontSize=15, leading=19,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=40)
cover_for = ParagraphStyle("cf", fontName="DV", fontSize=13, leading=17,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=4)
cover_name = ParagraphStyle("cn", fontName="DV-Serif-Bold", fontSize=32, leading=38,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=40)

callout_label = ParagraphStyle("cl", fontName="DV-Bold", fontSize=10, leading=12,
    textColor=white, alignment=TA_LEFT, spaceAfter=5)
callout_label_d = ParagraphStyle("cld", parent=callout_label, textColor=NAVY)
callout_body = ParagraphStyle("cb", fontName="DV", fontSize=10, leading=14,
    textColor=white, alignment=TA_JUSTIFY, spaceAfter=5)
callout_body_d = ParagraphStyle("cbd", parent=callout_body, textColor=NAVY)

pull_quote = ParagraphStyle("pq", fontName="DV-Italic", fontSize=13, leading=18,
    textColor=GOLD_DEEP, alignment=TA_CENTER, spaceBefore=8, spaceAfter=12,
    leftIndent=30, rightIndent=30)
small_label = ParagraphStyle("sl", fontName="DV-Bold", fontSize=9, leading=11,
    textColor=GOLD_DEEP, alignment=TA_LEFT, spaceAfter=2)
caption = ParagraphStyle("cap", fontName="DV-Italic", fontSize=8.5, leading=11,
    textColor=MID_GREY, alignment=TA_CENTER, spaceBefore=2, spaceAfter=10)


def P(t, s=None): return Paragraph(t, s or body)
def C(t, s=None): return Paragraph(t, s or cell)


# ---------- CALLOUTS PREMIUM ----------
def make_callout(label, text, bg, fg, accent=None):
    lab_style = callout_label if fg == white else callout_label_d
    body_style = callout_body if fg == white else callout_body_d
    inner = [Paragraph(label, lab_style)]
    if isinstance(text, list):
        for t in text:
            inner.append(Paragraph(t, body_style))
    else:
        inner.append(Paragraph(text, body_style))
    t = Table([[inner]], colWidths=[16*cm])
    style = [
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 11),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 11),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]
    if accent:
        style.append(("LINEBEFORE", (0, 0), (0, -1), 3, accent))
    t.setStyle(TableStyle(style))
    return [Spacer(1, 4), t, Spacer(1, 8)]


def retenir(text, accent=GOLD):
    return make_callout("◆  À RETENIR", text, NAVY, white, accent=accent)
def danger(text):
    return make_callout("⚠  DANGER", text, RED_ACC, white, accent=GOLD)
def application(text):
    return make_callout("▶  APPLICATION TRADING", text, GREEN, white, accent=GOLD)
def exercice(text):
    return make_callout("◐  EXERCICE", text, GOLD, NAVY, accent=NAVY)
def phrase_ancre(text):
    return make_callout("✦  PHRASE D'ANCRAGE", text, PURPLE, white, accent=GOLD)
def explication(text):
    inner = []
    if isinstance(text, list):
        for t in text:
            inner.append(Paragraph(t, body))
    else:
        inner.append(Paragraph(text, body))
    t = Table([[inner]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD_DEEP),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 8)]


# ---------- SCHEMAS ----------
class Schema(Flowable):
    def __init__(self, height, draw_func, width=16*cm):
        super().__init__()
        self.height = height
        self.width = width
        self.draw_func = draw_func
    def wrap(self, *a): return self.width, self.height
    def draw(self): self.draw_func(self.canv, self.width, self.height)


class GoldRule(Flowable):
    def __init__(self, width=16*cm, thickness=1.2, color=GOLD):
        super().__init__()
        self.width = width; self.thickness = thickness; self.color = color
        self.height = thickness + 4
    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 0, self.width, 0)


def _arrow(c, x1, y1, x2, y2, color=GOLD, lw=1.4, head=6):
    c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(lw)
    c.line(x1, y1, x2, y2)
    dx, dy = x2-x1, y2-y1
    d = math.sqrt(dx*dx + dy*dy) or 1
    ux, uy = dx/d, dy/d
    px, py = -uy, ux
    p1 = (x2 - head*ux + head*0.45*px, y2 - head*uy + head*0.45*py)
    p2 = (x2 - head*ux - head*0.45*px, y2 - head*uy - head*0.45*py)
    path = c.beginPath()
    path.moveTo(x2, y2); path.lineTo(*p1); path.lineTo(*p2); path.close()
    c.drawPath(path, fill=1, stroke=1)


# ---------- MINDMAP (carte mentale) ----------
def draw_mindmap(c, w, h, title, branches, accent=GOLD):
    cx, cy = w/2, h/2
    longest = max((len(w_) for w_ in title.upper().split()), default=0)
    central_r = max(1.5*cm, longest * 0.13*cm)
    c.setFillColor(NAVY); c.circle(cx, cy, central_r, fill=1, stroke=0)
    c.setStrokeColor(accent); c.setLineWidth(1.8)
    c.circle(cx, cy, central_r, fill=0, stroke=1)
    c.setFillColor(accent); c.setFont("DV-Bold", 10)
    words = title.upper().split()
    lines = []; cur = []
    max_w = central_r * 1.6
    for word in words:
        test = (" ".join(cur + [word])) if cur else word
        if c.stringWidth(test, "DV-Bold", 10) > max_w and cur:
            lines.append(" ".join(cur)); cur = [word]
        else:
            cur.append(word)
    if cur: lines.append(" ".join(cur))
    th = len(lines) * 11
    for i, ln in enumerate(lines):
        c.drawCentredString(cx, cy + th/2 - 11 - i*11 + 3, ln)

    n = len(branches)
    if n == 3:
        positions = [("left", "top"), ("right", "middle"), ("left", "bottom")]
    elif n == 4:
        positions = [("left", "top"), ("right", "top"), ("left", "bottom"), ("right", "bottom")]
    else:
        positions = []
        for i in range(n):
            side = "left" if i % 2 == 0 else "right"
            row = ["top", "middle", "bottom"][i // 2 % 3]
            positions.append((side, row))

    bw, bh = 3.4*cm, 1*cm
    for br, (side, row) in zip(branches, positions):
        bx = 0.5*cm if side == "left" else w - bw - 0.5*cm
        if row == "top": by = h - bh - 0.6*cm
        elif row == "bottom": by = 0.6*cm
        else: by = (h - bh) / 2
        col = br.get("color", accent)
        c.setFillColor(col)
        c.roundRect(bx, by, bw, bh, 5, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("DV-Bold", 9.5)
        c.drawCentredString(bx + bw/2, by + bh/2 - 3, br["label"])
        attach_x = bx + bw if side == "left" else bx
        attach_y = by + bh/2
        dx, dy = attach_x - cx, attach_y - cy
        d = math.sqrt(dx*dx + dy*dy) or 1
        ux, uy = dx/d, dy/d
        c.setStrokeColor(accent); c.setLineWidth(1.3)
        c.line(cx + ux*central_r, cy + uy*central_r, attach_x, attach_y)
        # leaves
        leaves = br.get("leaves", [])
        if leaves:
            c.setFillColor(MID_GREY); c.setFont("DV", 7.8)
            if row == "bottom":
                ly = by + bh + 4; step = 10
            else:
                ly = by - 8; step = -10
            for leaf in leaves:
                if side == "left":
                    c.drawString(bx + 4, ly, "• " + leaf)
                else:
                    c.drawRightString(bx + bw - 4, ly, leaf + " •")
                ly += step


# ---------- FLOW VERTICAL (boucle) ----------
def draw_flow(c, w, h, steps, accent=GOLD, color_first=None, color_last=None):
    n = len(steps)
    available = h - 0.4*cm
    box_h = 0.85*cm
    spacing = (available - n*box_h) / max(n-1, 1) if n > 1 else 0
    box_w = w * 0.55
    bx = (w - box_w) / 2
    for i, step in enumerate(steps):
        by = h - 0.2*cm - (i+1)*box_h - i*spacing
        col = accent
        if i == 0 and color_first: col = color_first
        if i == n-1 and color_last: col = color_last
        c.setFillColor(col); c.roundRect(bx, by, box_w, box_h, 5, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("DV-Bold", 9)
        c.drawCentredString(w/2, by + box_h/2 - 3, step)
        if i < n - 1:
            _arrow(c, w/2, by, w/2, by - spacing + 4, color=SLATE, lw=1, head=5)


# ---------- COMPARISON (deux colonnes) ----------
def draw_comparison(c, w, h, l_title, l_items, r_title, r_items,
                    l_color=RED_ACC, r_color=GREEN):
    gap = 0.4*cm
    box_w = (w - 2*gap) / 2
    bh = h - 0.4*cm
    # left
    c.setFillColor(RED_SOFT)
    c.roundRect(0, 0.2*cm, box_w, bh, 8, fill=1, stroke=0)
    c.setFillColor(l_color); c.setFont("DV-Bold", 12)
    c.drawCentredString(box_w/2, bh - 14, l_title)
    # right
    rx = box_w + 2*gap
    c.setFillColor(GREEN_SOFT)
    c.roundRect(rx, 0.2*cm, box_w, bh, 8, fill=1, stroke=0)
    c.setFillColor(r_color); c.setFont("DV-Bold", 12)
    c.drawCentredString(rx + box_w/2, bh - 14, r_title)
    # items
    n_items = max(len(l_items), len(r_items))
    start_y = bh - 36
    step = (bh - 50) / max(n_items, 1) if n_items else 0
    c.setFont("DV", 9); c.setFillColor(NAVY)
    for i in range(n_items):
        y = start_y - i*step
        if i < len(l_items):
            c.drawCentredString(box_w/2, y, "• " + l_items[i])
        if i < len(r_items):
            c.drawCentredString(rx + box_w/2, y, "• " + r_items[i])


# ---------- BASCULE plaisir/douleur ----------
def draw_seesaw(c, w, h, state="balanced"):
    cx, cy = w/2, h/2
    beam_w = 11*cm; beam_h = 0.35*cm
    # pivot
    c.setFillColor(NAVY)
    p = c.beginPath()
    p.moveTo(cx, cy - 0.2*cm)
    p.lineTo(cx - 1*cm, cy - 1.4*cm)
    p.lineTo(cx + 1*cm, cy - 1.4*cm)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # tilt
    tilt = 0
    if state == "pleasure": tilt = -10
    elif state == "pain": tilt = 10
    c.saveState()
    c.translate(cx, cy)
    c.rotate(tilt)
    c.setFillColor(GOLD)
    c.roundRect(-beam_w/2, -beam_h/2, beam_w, beam_h, 0.08*cm, fill=1, stroke=0)
    box_size = 1.3*cm
    # douleur (gauche)
    c.setFillColor(RED_ACC)
    c.roundRect(-beam_w/2 + 0.3*cm, beam_h/2, box_size, box_size, 4, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("DV-Bold", 9)
    c.drawCentredString(-beam_w/2 + 0.3*cm + box_size/2, beam_h/2 + box_size/2 - 3, "DOULEUR")
    # plaisir (droite)
    c.setFillColor(GOLD_DEEP)
    c.roundRect(beam_w/2 - 0.3*cm - box_size, beam_h/2, box_size, box_size, 4, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("DV-Bold", 9)
    c.drawCentredString(beam_w/2 - 0.3*cm - box_size/2, beam_h/2 + box_size/2 - 3, "PLAISIR")
    c.restoreState()


# ---------- 3 ÉTATS SN (polyvagal) ----------
def draw_polyvagal(c, w, h):
    # 3 stacked horizontal bars showing hierarchy
    bar_h = (h - 0.6*cm) / 3 - 0.1*cm
    states = [
        ("VAGAL VENTRAL", "calme social, présence ouverte", GREEN_SOFT, GREEN),
        ("SYMPATHIQUE", "mobilisation, fight / flight", GOLD_PALE, GOLD_DEEP),
        ("VAGAL DORSAL", "figement, effondrement, vide", RED_SOFT, RED_ACC),
    ]
    for i, (name, desc, bg, fg) in enumerate(states):
        y = h - 0.3*cm - (i+1)*bar_h - i*0.1*cm
        c.setFillColor(bg); c.roundRect(0.3*cm, y, w - 0.6*cm, bar_h, 5, fill=1, stroke=0)
        c.setFillColor(fg); c.setFont("DV-Bold", 12)
        c.drawString(0.6*cm, y + bar_h - 18, name)
        c.setFillColor(NAVY); c.setFont("DV-Italic", 9.5)
        c.drawString(0.6*cm, y + bar_h - 33, desc)
    # arrow down on right showing cascade
    _arrow(c, w - 0.5*cm, h - 0.6*cm, w - 0.5*cm, 0.5*cm, color=SLATE, lw=1.2, head=6)
    c.saveState()
    c.setFillColor(SLATE); c.setFont("DV-Italic", 8)
    c.translate(w - 0.2*cm, h/2)
    c.rotate(-90)
    c.drawCentredString(0, 0, "cascade descendante sous trauma")
    c.restoreState()


# ---------- 80/20 BAR ----------
def draw_8020(c, w, h):
    bar_h = 1.2*cm; bar_y = h/2 - bar_h/2
    c.setFillColor(RED_ACC); c.rect(0, bar_y, 0.8*w, bar_h, fill=1, stroke=0)
    c.setFillColor(GREEN); c.rect(0.8*w, bar_y, 0.2*w, bar_h, fill=1, stroke=0)
    c.setFont("DV-Bold", 13); c.setFillColor(white)
    c.drawCentredString(0.4*w, bar_y + bar_h/2 - 4, "80%  PERDENT")
    c.drawCentredString(0.9*w, bar_y + bar_h/2 - 4, "20%")
    c.setFont("DV", 8.5); c.setFillColor(NAVY)
    c.drawCentredString(0.4*w, bar_y + bar_h + 8, "Là où tu es aujourd'hui")
    c.drawCentredString(0.9*w, bar_y + bar_h + 8, "La sortie")


# ---------- HABIT LOOP ----------
def draw_habit_loop(c, w, h):
    nodes = [("DÉCLENCHEUR", "signal / contexte"),
             ("DÉSIR", "anticipation"),
             ("RÉPONSE", "comportement"),
             ("RÉCOMPENSE", "gratification")]
    cx, cy = w/2, h/2
    R = min(w, h) * 0.30
    node_r = 0.7*cm
    pts = []
    for i, (lab, sub) in enumerate(nodes):
        deg = 90 - i * 90
        rad = math.radians(deg)
        x = cx + R * math.cos(rad); y = cy + R * math.sin(rad)
        pts.append((x, y, lab, sub, rad))
    for i in range(4):
        x1, y1, _, _, _ = pts[i]
        x2, y2, _, _, _ = pts[(i+1) % 4]
        dx, dy = x2-x1, y2-y1
        d = math.sqrt(dx*dx + dy*dy)
        ux, uy = dx/d, dy/d
        _arrow(c, x1 + ux*node_r, y1 + uy*node_r, x2 - ux*node_r, y2 - uy*node_r,
               color=GOLD_DEEP, lw=1.3, head=6)
    for i, (x, y, lab, sub, rad) in enumerate(pts):
        c.setFillColor(NAVY); c.circle(x, y, node_r, fill=1, stroke=0)
        c.setStrokeColor(GOLD); c.setLineWidth(1.5)
        c.circle(x, y, node_r, fill=0, stroke=1)
        c.setFillColor(GOLD); c.setFont("DV-Bold", 9)
        c.drawCentredString(x, y + 2, str(i+1))
        c.setFillColor(NAVY); c.setFont("DV-Bold", 9)
        ux, uy = math.cos(rad), math.sin(rad)
        lx, ly = x + ux*1.5*cm, y + uy*1*cm
        c.drawCentredString(lx, ly + 4, lab)
        c.setFillColor(MID_GREY); c.setFont("DV-Italic", 8)
        c.drawCentredString(lx, ly - 7, sub)
    c.setFillColor(GOLD); c.setFont("DV-Serif-Bold", 11)
    c.drawCentredString(cx, cy + 5, "BOUCLE")
    c.drawCentredString(cx, cy - 8, "D'HABITUDE")


# ---------- PYRAMID 3-niveaux ----------
def draw_pyramid(c, w, h, levels, accent=GOLD):
    """levels du bas vers haut : list of (title, ex, sub, bg, txt)"""
    cx = w/2
    top_y = h - 0.4*cm; bot_y = 0.8*cm
    pyramid_h = top_y - bot_y; half_base = 4.5*cm
    band_h = pyramid_h / 3
    for i in range(3):
        y_lo = bot_y + i * band_h
        y_hi = y_lo + band_h
        ratio_lo = (top_y - y_lo) / pyramid_h
        ratio_hi = (top_y - y_hi) / pyramid_h
        hw_lo = half_base * ratio_lo
        hw_hi = half_base * ratio_hi
        title, ex, sub, bg, txt = levels[i]
        c.setFillColor(bg)
        p = c.beginPath()
        p.moveTo(cx - hw_lo, y_lo); p.lineTo(cx + hw_lo, y_lo)
        p.lineTo(cx + hw_hi, y_hi); p.lineTo(cx - hw_hi, y_hi); p.close()
        c.setStrokeColor(NAVY); c.setLineWidth(0.6)
        c.drawPath(p, fill=1, stroke=1)
        c.setFillColor(txt); c.setFont("DV-Bold", 10 if i < 2 else 11)
        c.drawCentredString(cx, (y_lo + y_hi)/2 + 2, title)
        c.setFont("DV-Italic", 7.5)
        c.drawCentredString(cx, (y_lo + y_hi)/2 - 8, ex)
        c.setFillColor(MID_GREY); c.setFont("DV-Italic", 7.5)
        c.drawString(cx + half_base + 0.4*cm, (y_lo + y_hi)/2, sub)


# ---------- TABLE styled ----------
def styled_table(data, col_widths, accent=GOLD):
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("BACKGROUND", (0, 1), (-1, -1), CREAM),
        ("BOX", (0, 0), (-1, -1), 0.6, accent),
        ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_DEEP),
    ]))
    return t


# ---------- ASCII schema (réservé aux cas où visuel pas adapté) ----------
def ascii_box(text, accent=GOLD):
    lines = text.strip("\n").split("\n")
    paras = []
    for ln in lines:
        ln_html = ln.replace(" ", "&nbsp;")
        paras.append(Paragraph(ln_html,
            ParagraphStyle("sl", fontName="DV-Mono", fontSize=8.2, leading=10.5,
                textColor=NAVY, alignment=TA_LEFT)))
    t = Table([[paras]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LEFTPADDING", (0, 0), (-1, -1), 14),
        ("RIGHTPADDING", (0, 0), (-1, -1), 14),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.6, accent),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]


# ---------- PAGE TEMPLATES ----------
_part_color = [GOLD]
_part_num = [None]
_part_name = [""]

def cover_page(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY_DEEP)
    canv.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # gold bands
    canv.setFillColor(GOLD)
    canv.rect(0, A4[1] - 1.6*cm, A4[0], 1.6*cm, fill=1, stroke=0)
    canv.rect(0, 0, A4[0], 1.6*cm, fill=1, stroke=0)
    # frame
    canv.setStrokeColor(GOLD); canv.setLineWidth(0.6)
    canv.rect(1.2*cm, 2.4*cm, A4[0] - 2.4*cm, A4[1] - 4.8*cm, fill=0, stroke=1)
    canv.restoreState()

def standard_page(canv, doc):
    canv.saveState()
    color = _part_color[0]
    # header bar
    canv.setStrokeColor(color); canv.setLineWidth(0.6)
    canv.line(2*cm, A4[1] - 1.3*cm, A4[0] - 2*cm, A4[1] - 1.3*cm)
    canv.setFont("DV-Bold", 8); canv.setFillColor(color)
    canv.drawString(2*cm, A4[1] - 1.05*cm, "DEVENIR UN TRADER STABLE")
    canv.setFont("DV-Italic", 8); canv.setFillColor(MID_GREY)
    if _part_num[0]:
        canv.drawRightString(A4[0] - 2*cm, A4[1] - 1.05*cm, f"Partie {_part_num[0]} — {_part_name[0]}")
    else:
        canv.drawRightString(A4[0] - 2*cm, A4[1] - 1.05*cm, "Manuel personnel")
    # footer
    canv.setFont("DV", 8.5); canv.setFillColor(MID_GREY)
    canv.drawCentredString(A4[0]/2.0, 1.2*cm, f"— {doc.page} —")
    canv.setStrokeColor(color); canv.setLineWidth(0.3)
    canv.line(2*cm, 1.6*cm, A4[0] - 2*cm, 1.6*cm)
    canv.restoreState()

def part_separator_page_canvas(canv, doc):
    canv.saveState()
    canv.setFillColor(NAVY_DEEP)
    canv.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    color = _part_color[0]
    canv.setFillColor(color)
    canv.rect(0, A4[1] - 1.6*cm, A4[0], 1.6*cm, fill=1, stroke=0)
    canv.rect(0, 0, A4[0], 1.6*cm, fill=1, stroke=0)
    canv.setStrokeColor(color); canv.setLineWidth(0.6)
    canv.rect(1.2*cm, 2.4*cm, A4[0] - 2.4*cm, A4[1] - 4.8*cm, fill=0, stroke=1)
    canv.restoreState()


def part_separator(num, title, subtitle, accent):
    out = []
    out.append(Spacer(1, 6*cm))
    out.append(P(f"PARTIE {num}", ParagraphStyle("pn", fontName="DV-Serif-Bold",
        fontSize=48, leading=52, textColor=accent, alignment=TA_CENTER, spaceAfter=8)))
    out.append(Spacer(1, 1*cm))
    out.append(P(title, ParagraphStyle("pt", fontName="DV-Serif-Bold", fontSize=32,
        leading=38, textColor=GOLD, alignment=TA_CENTER, spaceAfter=6)))
    out.append(P(subtitle, ParagraphStyle("ps", fontName="DV-Italic", fontSize=14,
        leading=18, textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=10)))
    out.append(PageBreak())
    return out


def part_intro_header(num, title, subtitle, accent):
    out = []
    out.append(P(f"PARTIE {num}", small_label))
    out.append(P(title, h_part))
    out.append(P(subtitle, h_part_sub))
    out.append(GoldRule(color=accent))
    out.append(Spacer(1, 12))
    return out


def concept_header(num, name, accent):
    out = []
    out.append(P(f"CONCEPT {num}", small_label))
    out.append(P(name, h_concept))
    out.append(GoldRule(color=accent, thickness=0.6))
    out.append(Spacer(1, 8))
    return out


def orientation_box(book_title, author, year, theme, why_read, accent=GOLD):
    """Encadré d'orientation bibliographique en début de partie.
    Non dérivatif — seulement référence générale."""
    inner = [
        Paragraph("◇  ORIENTATION DE LECTURE",
            ParagraphStyle("ob_label", fontName="DV-Bold", fontSize=9.5,
                textColor=accent, alignment=TA_LEFT, spaceAfter=4)),
        Paragraph(f"<b>Livre conseillé en parallèle :</b> <i>{book_title}</i> — {author} ({year}).",
            ParagraphStyle("ob_body", fontName="DV", fontSize=9.5, leading=13,
                textColor=NAVY, alignment=TA_LEFT, spaceAfter=2)),
        Paragraph(f"<b>Thème général :</b> {theme}",
            ParagraphStyle("ob_body2", fontName="DV", fontSize=9.5, leading=13,
                textColor=NAVY, alignment=TA_LEFT, spaceAfter=2)),
        Paragraph(f"<b>Pourquoi le lire :</b> {why_read}",
            ParagraphStyle("ob_body3", fontName="DV", fontSize=9.5, leading=13,
                textColor=NAVY, alignment=TA_LEFT, spaceAfter=4)),
        Paragraph(
            "<i>Note : cette partie est un manuel original d'intégration appliqué à mon profil. "
            "Elle ne résume pas le livre et ne suit pas sa structure.</i>",
            ParagraphStyle("ob_disc", fontName="DV-Italic", fontSize=8.5, leading=11,
                textColor=MID_GREY, alignment=TA_LEFT)),
    ]
    t = Table([[inner]], colWidths=[16*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 10)]


print("✓ Infrastructure chargée")


# ============================================================
# DOCUMENT
# ============================================================
OUTPUT = "/home/user/Site-Enzo/devenir_trader_stable_v4.pdf"
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2.5*cm, rightMargin=2.5*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
    title="Devenir un trader stable",
    author="Manuel personnel pour Marien"
)
story = []

# ---------- COVER ----------
story.append(Spacer(1, 5*cm))
story.append(P("DEVENIR UN", cover_main))
story.append(P("TRADER STABLE", cover_main))
story.append(P("Psychologie, trauma, dopamine,<br/>discipline et argent", cover_sub))
story.append(P("Manuel personnel de transformation mentale",
    ParagraphStyle("sub2", fontName="DV-Italic", fontSize=12, leading=15,
        textColor=GOLD_PALE, alignment=TA_CENTER, spaceAfter=60)))
story.append(P("Pour", cover_for))
story.append(P("MARIEN", cover_name))
story.append(Spacer(1, 1*cm))
story.append(P("Mai 2026",
    ParagraphStyle("d", fontName="DV", fontSize=11, textColor=LIGHT_GREY,
        alignment=TA_CENTER)))
story.append(PageBreak())


# ---------- PRÉFACE ----------
_part_color[0] = GOLD
_part_num[0] = None
story.append(P("PRÉFACE", h_part))
story.append(P("Comment utiliser ce manuel", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce manuel n'est pas un livre à lire. C'est un protocole à appliquer. Neuf parties, chacune adresse une "
    "dimension de ton problème de trading : la psychologie de la perte, la dopamine, le trauma de 2022, la "
    "décharge somatique, la pensée probabiliste, les limites du corps, les habitudes, le lâcher-prise, "
    "et ton rapport à l'argent. Lues dans l'ordre et appliquées, elles forment un système."
))
story.append(P(
    "<b>Une partie à la fois.</b> Tu lis la partie. Tu fais les exercices pendant 7 à 14 jours. Tu remplis "
    "ton journal. Puis seulement, tu passes à la suivante. Si tu sautes les exercices, tu fais de la consommation "
    "de contenu — exactement le piège que ce manuel décrit. Une partie tous les 15 jours = 4-5 mois pour "
    "boucler le manuel. C'est le bon rythme."
))
story.append(P(
    "<b>La main qui écrit.</b> Chaque exercice est conçu pour être fait <b>à la main</b>, dans un cahier dédié. "
    "Écrire à la main mobilise différemment ton cerveau. Tape sur un clavier et tu restes en surface. Écris à "
    "la main et tu descends en toi."
))
story.append(P(
    "<b>Le corps avant le mental.</b> Quatre parties parlent du corps (Parties 3, 4, 6, et partiellement 8). "
    "Ton TBI 2022 a fait de ton système nerveux ton premier terrain de travail. Aucun mental ne s'apaise dans "
    "un corps en alerte. Si tu n'as pas le temps de tout faire, fais au moins les parties corporelles. "
    "Le reste suivra."
))
story.append(Spacer(1, 8))

# Codes visuels
story.append(P("Les codes visuels du manuel", h_section))
codes_data = [
    [C("Code", cell_g), C("Sens", cell_g)],
    [C("◆  À RETENIR", cell_b), C("L'idée centrale du concept. Si tu retiens rien d'autre, retiens ça.")],
    [C("⚠  DANGER", cell_b), C("Le piège à voir venir. Le moment où tu vas vouloir saboter.")],
    [C("▶  APPLICATION TRADING", cell_b), C("Le geste concret à faire devant ton écran.")],
    [C("◐  EXERCICE", cell_b), C("L'exercice à appliquer cette semaine.")],
    [C("✦  PHRASE D'ANCRAGE", cell_b), C("La phrase à mémoriser. À répéter en cas de crise.")],
]
story.append(styled_table(codes_data, [4.5*cm, 11.5*cm]))
story.append(PageBreak())


# ---------- SOMMAIRE ----------
_part_color[0] = GOLD
story.append(P("SOMMAIRE", h_part))
story.append(P("Architecture du manuel", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 14))

sommaire_data = [
    [C("Partie", cell_g), C("Thème", cell_g), C("Adresse...", cell_g)],
    [C("1", cell_b), C("Apprendre à perdre sans s'effondrer", cell_b),
     C("ton pattern +1500, ton décalage de SL, ton rapport à l'échec")],
    [C("2", cell_b), C("Comprendre la dopamine et la recherche du pic", cell_b),
     C("ton addiction à l'intensité, ton besoin de shoot, ton calme qui te semble vide")],
    [C("3", cell_b), C("Comprendre le trauma et le système nerveux", cell_b),
     C("ton TBI 2022, ton SN dérégulé, ton hypervigilance silencieuse")],
    [C("4", cell_b), C("Décharger le stress bloqué dans le corps", cell_b),
     C("l'énergie figée depuis 2022, les mouvements inachevés, les pratiques somatiques")],
    [C("5", cell_b), C("Penser en probabilités comme un vrai trader", cell_b),
     C("ta recherche de certitude, ton besoin d'avoir raison, ta pensée binaire")],
    [C("6", cell_b), C("Comprendre quand le corps dit stop", cell_b),
     C("ta tendance à pousser, ton hyper-responsabilité, le coût de tes émotions refoulées")],
    [C("7", cell_b), C("Construire des habitudes qui tiennent", cell_b),
     C("tes cycles de motivation, tes systèmes instables, tes plateaux abandonnés")],
    [C("8", cell_b), C("Lâcher prise émotionnellement", cell_b),
     C("ton contrôle compulsif, ta résistance, ton serrement chronique")],
    [C("9", cell_b), C("Développer une patience financière", cell_b),
     C("ta course au coup, l'absence de définition de « assez », ton plan 30 ans")],
    [C("—", cell_b), C("Conclusion + plans + checklist", cell_b),
     C("intégration des 9 parties, plan 30 jours, plan 12 mois, checklist quotidienne")],
]
story.append(styled_table(sommaire_data, [1.2*cm, 5.8*cm, 9*cm]))
story.append(PageBreak())


# ---------- COMPAGNONS DE LECTURE ----------
_part_color[0] = GOLD
story.append(P("COMPAGNONS DE LECTURE", h_part))
story.append(P("Ta carte bibliographique pour le plan 12 mois", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce manuel est un cours <b>original</b> sur des concepts généraux de psychologie, neurosciences et "
    "sciences comportementales. Il n'est ni un résumé, ni un dérivé, ni un substitut des ouvrages ci-dessous. "
    "Les 9 livres listés ici sont des références <b>indépendantes</b> à lire en parallèle, dans ton propre rythme, "
    "selon les thèmes que tu veux approfondir avec la voix de leurs auteurs."
))
story.append(P(
    "Tu peux intégrer ces lectures à partir du <b>Mois 7</b> de ton plan 12 mois (à raison d'un livre par mois). "
    "Avant le Mois 7, concentre-toi sur l'application des modules de ce manuel — pas sur la consommation de "
    "contenu nouveau."
))
story.append(Spacer(1, 10))

companions_data = [
    [C("Thème de partie", cell_g), C("Livre conseillé en parallèle", cell_g), C("Quand le lire", cell_g)],
    [C("P1 — Apprendre à perdre", cell_b),
     C("Best Loser Wins — Tom Hougaard (2022)"),
     C("Mois 7")],
    [C("P2 — Dopamine", cell_b),
     C("Un monde sous dopamine — Anna Lembke (2021)"),
     C("Mois 8")],
    [C("P3 — Trauma & SN", cell_b),
     C("Le corps n'oublie rien — Bessel van der Kolk (2014)"),
     C("Mois 9 — prioritaire pour ton TBI")],
    [C("P4 — Décharger le stress", cell_b),
     C("Réveiller le tigre — Peter Levine (1997)"),
     C("Mois 9-10")],
    [C("P5 — Pensée probabiliste", cell_b),
     C("Trader dans la zone — Mark Douglas (2000)"),
     C("Mois 10")],
    [C("P6 — Corps qui dit stop", cell_b),
     C("Quand le corps dit non — Gabor Maté (2003)"),
     C("Mois 11")],
    [C("P7 — Habitudes", cell_b),
     C("Un rien peut tout changer (Atomic Habits) — James Clear (2018)"),
     C("Mois 7 ou 8 (court et opérationnel)")],
    [C("P8 — Lâcher prise", cell_b),
     C("Lâcher prise — David R. Hawkins (2012)"),
     C("Mois 11-12")],
    [C("P9 — Patience financière", cell_b),
     C("La psychologie de l'argent — Morgan Housel (2020)"),
     C("Mois 12")],
]
story.append(styled_table(companions_data, [4*cm, 7.5*cm, 4.5*cm]))
story.append(Spacer(1, 14))

story.append(P("Important", h_section))
story.append(P(
    "Ne lis PAS ces livres avant d'avoir appliqué les modules de ce manuel. Les premières 6 semaines, tu "
    "appliques. Tu ne consommes pas. Sinon tu fais exactement ce que le Concept 1 de la Partie 1 te décrit : "
    "fuir l'exécution dans l'apprentissage. Six semaines de purge contenu trading, puis tu reprends la lecture "
    "à un rythme contrôlé."
))
story.append(P(
    "Ne t'attends pas non plus à retrouver le contenu de mon manuel dans ces livres — ni l'inverse. Ce sont "
    "des chemins parallèles vers les mêmes territoires. Chaque auteur a sa propre approche, son propre angle, "
    "ses propres anecdotes cliniques. Mon manuel a la sienne. Ces deux corpus se complètent, ils ne se "
    "substituent pas."
))
story.append(PageBreak())


# ---------- MASTER INDEX DES EXERCICES ----------
_part_color[0] = GOLD
_part_name[0] = "Index exercices"

story.append(P("MASTER INDEX DES EXERCICES", h_part))
story.append(P("Tous les exercices du manuel, classés par fréquence", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Le manuel contient ~70 exercices répartis dans les 9 parties. Cet index te permet de naviguer : qu'est-ce "
    "que je fais aujourd'hui ? Cette semaine ? Ce mois ? Tu peux imprimer cette page et la cocher au fur et à mesure."
))
story.append(Spacer(1, 10))

story.append(P("QUOTIDIEN — tous les jours", h_section))
story.append(styled_table([
    [C("Exercice", cell_g), C("Partie", cell_g), C("Durée", cell_g)],
    [C("Méditation / pleine présence matinale"), C("P2, P3"), C("20 min")],
    [C("Respiration 4-6 (5 sessions × 2-5 min)"), C("P3, P4"), C("15 min cumulé")],
    [C("Cold shower"), C("P2, P4"), C("2-5 min")],
    [C("Scan corporel matin et soir"), C("P3, P4"), C("10 min")],
    [C("Journal manuscrit — pré + post session"), C("P7"), C("15-20 min")],
    [C("Récitation des 5 vérités"), C("P5"), C("3 min")],
    [C("Relecture du protocole personnel"), C("P1"), C("2 min")],
    [C("Phrase d'ancrage du jour (1 des 9)"), C("Toutes"), C("1 min")],
], [9*cm, 2.5*cm, 4.5*cm]))
story.append(Spacer(1, 10))

story.append(P("HEBDOMADAIRE — une fois par semaine", h_section))
story.append(styled_table([
    [C("Exercice", cell_g), C("Partie", cell_g), C("Durée", cell_g)],
    [C("Pansage conscient avec ta filly"), C("P3, P4"), C("45 min")],
    [C("Sortie nature sans téléphone"), C("P4"), C("90 min")],
    [C("3 séances sport (box / équitation / course)"), C("P2, P4, P6"), C("3 × 60 min")],
    [C("Journée OFF complète (1 jour fixe)"), C("P6"), C("Toute la journée")],
    [C("Revue hebdo dans le journal (dimanche)"), C("P7"), C("30 min")],
    [C("Pratique d'expression émotionnelle"), C("P6"), C("15 min × plusieurs jours")],
    [C("5 « non » à dire dans la semaine"), C("P6"), C("Opportuniste")],
    [C("Exercice de pendulation"), C("P4"), C("5 min")],
], [9*cm, 2.5*cm, 4.5*cm]))
story.append(Spacer(1, 10))

story.append(P("BIMENSUEL — toutes les 2 semaines", h_section))
story.append(styled_table([
    [C("Exercice", cell_g), C("Partie", cell_g)],
    [C("Séance praticien somatique (SE / EMDR)"), C("P3, P4")],
    [C("Exploration mouvement inachevé"), C("P4")],
    [C("Compteur d'extinction (révision sessions sans décalage SL)"), C("P2")],
], [11*cm, 5*cm]))
story.append(Spacer(1, 10))

story.append(P("MENSUEL — une fois par mois", h_section))
story.append(styled_table([
    [C("Exercice", cell_g), C("Partie", cell_g)],
    [C("Bilan grille 100 trades (avancement)"), C("P5")],
    [C("Lettre à l'un des 3 Marien (rotation : avant / reconstruction / après)"), C("Section Identité")],
    [C("Bilan financier — règle 50/30/20"), C("P9")],
    [C("Calcul de progression vers ton « assez »"), C("P9")],
    [C("Test calibration style trading (à partir du Mois 2)"), C("Section Style")],
    [C("Audit du risque de ruine"), C("P9")],
], [11*cm, 5*cm]))
story.append(Spacer(1, 10))

story.append(P("FONDATIONS — à faire une seule fois (et puis maintenir)", h_section))
story.append(styled_table([
    [C("Exercice fondateur", cell_g), C("Partie", cell_g)],
    [C("Acheter le cahier journal — page 1 manuscrite"), C("P7")],
    [C("Écrire le protocole personnel (9 lignes) — signé, affiché"), C("P1")],
    [C("Écrire la méthode de trading en A4 (mode systématique)"), C("P5")],
    [C("Calculer ton « assez » (capital cible + délai + plan mensuel)"), C("P9")],
    [C("Ouvrir un compte épargne dédié au surplus trading"), C("P9")],
    [C("Désinstaller les apps de trading du téléphone"), C("P2, P7")],
    [C("Trouver un praticien somatique — premier RDV pris"), C("P3, P4")],
    [C("Bilan neuropsychologique post-TBI"), C("Section Ressources")],
    [C("Identifier 3 ressources somatiques disponibles 24h/24"), C("P4")],
    [C("Écriture des 3 lettres aux 3 Marien"), C("Section Identité")],
    [C("Audit de l'environnement (téléphone, bureau, chambre)"), C("P7")],
    [C("Identifier ton seuil corporel personnel (red flag)"), C("P6")],
], [11*cm, 5*cm]))
story.append(Spacer(1, 14))

story.extend(retenir(
    "Tu n'es pas censé tout faire en même temps. Le plan 30 jours te dit par où commencer. Cet index te "
    "permet de savoir quel exercice appartient à quelle fréquence — pour ne pas le confondre avec une tâche "
    "ponctuelle ou oublier qu'il est récurrent."
))
story.append(PageBreak())


# ---------- INTRODUCTION GÉNÉRALE ----------
story.append(P("INTRODUCTION GÉNÉRALE", h_part))
story.append(P("Le diagnostic complet — ton cas", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Marien, voici le diagnostic complet qui structure ce manuel. Lis-le attentivement — c'est la carte "
    "à partir de laquelle tout le reste s'organise."
))
story.append(P("Ton pattern signature", h_section))
story.append(Schema(8*cm, lambda c, w, h: draw_flow(c, w, h,
    ["Gain", "Dopamine + Euphorie", "Sensation de puissance",
     "Augmentation du risque", "Overtrading", "Perte",
     "Honte / Colère", "Besoin de me refaire", "COMPTE CRAMÉ"],
    accent=GOLD_DEEP, color_first=GREEN, color_last=RED_ACC)))
story.append(P("Ta boucle destructrice en 9 étapes. Chaque étape est neurologiquement documentée.", caption))

story.append(P("Les 5 leviers qui te détruisent", h_section))
story.append(P(
    "<b>Levier 1 — Neurochimique.</b> Ta boucle est dopaminergique. Ce n'est pas un manque de discipline. "
    "C'est une chimie cérébrale. La Partie 2 décortique le mécanisme."
))
story.append(P(
    "<b>Levier 2 — Traumatique.</b> Ton TBI 2022 a recalibré ton système nerveux. Tu cherches l'intensité parce "
    "que ton baseline a changé. Les Parties 3 et 4 adressent ce levier corporellement."
))
story.append(P(
    "<b>Levier 3 — Cognitif.</b> Tu raisonnes en certitudes alors que le marché est probabiliste. La Partie 5 "
    "reconfigure ta pensée."
))
story.append(P(
    "<b>Levier 4 — Identitaire.</b> Ton identité dépend de ta performance. Chaque trade devient un test "
    "existentiel. La Partie 6 adresse ce poids."
))
story.append(P(
    "<b>Levier 5 — Habitudes & rapport à l'argent.</b> Tu n'as pas de système d'habitudes qui tienne. Tu n'as "
    "pas défini ton « assez ». Les Parties 7 et 9 construisent l'architecture durable."
))

story.append(P("La Partie 8 (lâcher prise) est la compétence transversale qui traverse toutes les autres.", body_i))
story.append(Spacer(1, 10))

story.extend(retenir(
    "Tu n'as pas UN problème. Tu as cinq couches superposées. Ce manuel les traite une par une. "
    "Le traiter dans l'ordre, c'est dérouler une corde du nœud — pas tirer dessus au hasard."
))
story.append(PageBreak())


# ============================================================
# SECTION SPÉCIALE — IDENTITÉ MARIEN POST-2022
# ============================================================
_part_color[0] = GOLD
_part_num[0] = None
_part_name[0] = "Identité post-2022"

story.append(P("SECTION FONDATRICE", h_part))
story.append(P("Identité Marien post-2022 — qui es-tu depuis ?", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Avant d'entrer dans les 9 parties techniques, il faut nommer ce qui traverse tout : l'événement de 2022 "
    "n'est pas un épisode médical à oublier. C'est probablement <b>l'événement fondateur</b> de la vie adulte "
    "que tu vis maintenant. Toute ta psychologie de trader, ton rapport à l'intensité, ton besoin de prouver, "
    "ton lien identité-performance — tout part de là."
))
story.append(P(
    "Cette section spéciale est dédiée à cette question : qui es-tu depuis 2022 ? Comment habiter ce qui s'est "
    "passé sans en faire ni un trauma figé, ni une histoire effacée. C'est un travail à part entière, qui "
    "soutient tout le reste."
))

story.append(P("1.  La rupture biographique", h_section))
story.append(P(
    "En psychologie, une « rupture biographique » désigne un événement qui sépare ta vie en un <b>avant</b> et "
    "un <b>après</b>. Pas un simple changement — une césure. Ton accident de 2022 en est une, manifestement. "
    "Pour la plupart des gens, la vie suit un fil continu (école → études → travail → famille). Pour quelqu'un "
    "qui a vécu un coma, des opérations multiples, une reconstruction longue, la continuité est cassée. "
    "Quelque chose s'est terminé en 2022. Quelque chose d'autre a commencé. La continuité n'existe plus en "
    "ligne droite."
))
story.append(P(
    "Cette rupture biographique n'est pas une malédiction. C'est un fait. Tu peux la nier (« je suis toujours "
    "le même »), la fuir (« je n'en parle pas »), ou l'habiter (« oui, je suis Marien-d'après-2022, et alors ? »). "
    "Seule la troisième option ouvre quelque chose. Les deux premières te bloquent dans des comportements "
    "compensatoires."
))

story.append(P("2.  Les trois Marien", h_section))
story.append(P(
    "Il y a probablement trois figures de toi qui coexistent en ce moment, sans que tu les distingues clairement :"
))
story.append(styled_table([
    [C("Figure", cell_g), C("Caractéristiques", cell_g)],
    [C("Marien-d'avant", cell_b),
     C("Le Marien d'avant l'accident. Continuité, projets, identité non-troublée. Tu le portes en nostalgie possible.")],
    [C("Marien-en-reconstruction", cell_b),
     C("Celui qui a survécu, qui a refait son corps et son cerveau pendant des mois. Combatif, intense, déterminé. C'est celui qui parle quand tu trades pour prouver.")],
    [C("Marien-d'après", cell_b),
     C("Celui qui est sorti de la reconstruction. Plus ancien d'expérience, mais à construire encore. Tu n'as probablement pas encore fini de le faire émerger.")],
], [4.5*cm, 11.5*cm]))
story.append(Spacer(1, 10))

story.append(P(
    "La plupart de ton temps mental, tu es probablement en mode « Marien-en-reconstruction » — encore en "
    "preuve, encore en combat, encore en démonstration. C'est la posture qui t'a sauvé pendant 1-2 ans après "
    "l'accident. C'est aussi celle qui te détruit aujourd'hui en trading, parce qu'elle te pousse à transformer "
    "chaque trade en test identitaire."
))
story.append(P(
    "Le travail psychologique de fond, c'est de <b>laisser émerger Marien-d'après</b>. Pas par effort. Par "
    "permission. Lui n'a plus à prouver, parce qu'il est déjà sorti de la phase de preuve. Lui peut trader "
    "sans drama, parce que le trading n'est plus son terrain de validation."
))
story.append(PageBreak())

story.append(P("3.  Le besoin de prouver — d'où il vient, où il va", h_section))
story.append(P(
    "Quand tu te lèves le matin avec l'intention « il faut que je gagne », tu n'es pas en mode trader rentable. "
    "Tu es en mode survivant qui prouve qu'il existe encore. Ce besoin de prouver a une racine claire : pendant "
    "ta reconstruction post-2022, chaque progrès (re-marcher, retrouver une mémoire, gérer un effort cognitif) "
    "était une preuve VITALE que tu allais récupérer. Le besoin de prouver a sauvé ta récupération."
))
story.append(P(
    "Mais le besoin de prouver ne s'éteint pas tout seul quand la phase aiguë est terminée. Il continue, "
    "désormais sans cible. Il cherche un terrain. Le trading devient ce terrain — chaque trade est devenu, "
    "sans que tu le décides, une mini-preuve que ton cerveau marche, que ta volonté tient, que tu n'es pas "
    "réduit à ton accident."
))
story.append(P(
    "Cette logique est <b>inadaptée</b> au trading. Le trading rentable demande du détachement, pas de la preuve. "
    "Aussi longtemps que tu portes la preuve dans chaque clic, tu vas perdre. Pas par incompétence — par "
    "mauvais combat. Ton besoin de prouver gagnerait à se réorienter vers des terrains qui le portent bien : "
    "compétitions équestres, projets ATHÉNA qui se construisent dans la durée, peut-être un projet créatif ou "
    "sportif personnel. Pas le marché — qui ne te demande aucune preuve et qui sanctionne le besoin d'en donner."
))

story.append(P("4.  Le « grand sommeil » du coma", h_section))
story.append(P(
    "Quelque chose de spécifique au coma mérite d'être nommé. Pendant le coma, ta conscience était suspendue. "
    "Pour toi, le temps écoulé du coma n'a pas existé — tu t'es endormi en septembre 2022 et tu t'es réveillé "
    "« plus tard », sans expérience subjective intermédiaire. Cette discontinuité phénoménologique n'est pas "
    "anodine. Elle crée souvent une sensation d'irréalité, de flottement, ou d'impossibilité à se sentir "
    "« vraiment de retour »."
))
story.append(P(
    "Ce phénomène est documenté chez les patients post-coma. Il peut s'exprimer par : sensation que la vie est "
    "un rêve, difficulté à se prendre au sérieux soi-même, recherche d'événements intenses pour « s'assurer "
    "que je suis là », fragilité du sentiment de continuité personnelle. Si tu reconnais l'un de ces signaux, "
    "il appartient probablement à cette dimension."
))
story.extend(make_callout("◈  CE QUI CHANGE QUAND TU NOMMES ÇA",
    "Le sentiment d'irréalité que tu portes peut-être en arrière-plan n'est pas de la « faiblesse mentale ». "
    "C'est une conséquence neurologique d'une discontinuité de conscience. Le nommer ne le supprime pas. Mais "
    "ça te permet de cesser de le combattre comme une défaillance — et de le traiter comme une caractéristique "
    "à intégrer.",
    GOLD, NAVY, accent=NAVY))

story.append(P("5.  Réintégrer les trois Marien", h_section))
story.append(P(
    "Le travail identitaire n'est pas de « redevenir Marien-d'avant ». Cette personne est partie. C'est aussi "
    "de ne pas rester bloqué en Marien-en-reconstruction. C'est d'<b>intégrer les trois figures</b> dans une "
    "identité élargie qui les contient toutes."
))
story.append(P(
    "Marien-d'après n'est pas Marien-d'avant + récupération. C'est une figure entièrement nouvelle, qui inclut "
    "l'expérience de 2022 sans en être prisonnière, qui inclut la force de la reconstruction sans rester en "
    "mode preuve, qui inclut une connaissance corporelle de ta propre finitude que la plupart des gens de 25 "
    "ans n'ont pas. C'est, potentiellement, une figure plus profonde que celle que tu aurais été sans 2022."
))
story.append(PageBreak())

story.append(P("6.  Pratiques d'intégration identitaire", h_section))

story.append(styled_table([
    [C("Pratique", cell_g), C("Comment", cell_g), C("Effet", cell_g)],
    [C("Écriture autobiographique"), C("1 page/mois, manuscrit, sur un événement de 2022"),
     C("Cohérence narrative reconstruite")],
    [C("Dialogue avec Marien-d'avant"), C("Lettre à toi-d'avant-l'accident"),
     C("Reconnaissance de la perte")],
    [C("Dialogue avec Marien-en-recons."), C("Lettre de remerciement à toi-survivant"),
     C("Reconnaissance de la dette + permission de passer à l'après")],
    [C("Photo de toi avant et après"), C("Regarde-les côte à côte 5 min"),
     C("Sensation directe des trois Marien")],
    [C("Activité non-performance"), C("1h/sem dédiée à une activité sans enjeu"),
     C("Marien-d'après s'exprime")],
    [C("Thérapie identitaire"), C("Un psy spécialisé trauma OU coach identitaire"),
     C("Accompagnement professionnel du processus")],
], [4*cm, 6.5*cm, 5.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>L'exercice fondateur — 3 lettres.</b> Sur 3 séances séparées (1 par semaine) : "
    "(1) Une lettre à Marien-d'avant. Tu lui dis ce qui s'est passé, ce que tu perds en n'étant plus lui, "
    "ce que tu gardes de lui. "
    "(2) Une lettre à Marien-en-reconstruction. Tu le remercies. Tu lui dis qu'il peut se reposer. Tu lui "
    "donnes la permission de céder la place. "
    "(3) Une lettre à Marien-d'après. Tu lui demandes qui il veut être. Tu écoutes ce qui vient. "
    "Tu gardes les 3 lettres. Tu les relis dans 6 mois. Tu vois ce qui a bougé."
]))

story.append(P("7.  Le risque du sur-investissement dans la performance", h_section))
story.append(P(
    "Pour quelqu'un qui sort d'une rupture biographique, la tentation est massive de <b>tout miser sur la "
    "performance</b> pour reconstruire un sens. Performance sportive (saut d'obstacles), performance "
    "entrepreneuriale (ATHÉNA), performance financière (trading), parfois performance relationnelle. C'est "
    "compréhensible. C'est aussi un piège."
))
story.append(P(
    "La performance ne reconstruit pas une identité. Elle ne fait que reporter le moment où la question "
    "identitaire doit être posée. Tant que tu performes assez, tu ne te demandes pas qui tu es. Le jour où la "
    "performance baisse (crash de compte, blessure, échec ATHÉNA), la question revient brutalement — souvent "
    "sous forme de crise."
))
story.append(P(
    "La voie alternative : <b>nourrir une identité non-performance en parallèle</b>. Pas à la place. En "
    "parallèle. Tu maintiens tes terrains de performance (ils sont utiles et valent quelque chose), mais tu "
    "construis aussi des terrains où tu existes sans accomplir. Lecture, pansage avec ta filly, conversations "
    "gratuites, présence à des proches qui ne te jugent pas par tes résultats. Ces terrains-là, lentement, "
    "construisent Marien-d'après."
))
story.extend(retenir(
    "Ton accident de 2022 est l'événement fondateur de ton identité adulte actuelle. Le nier le rend toxique. "
    "L'habiter le rend constitutif. Les trois Marien (avant / en reconstruction / d'après) coexistent en toi. "
    "L'enjeu est de les intégrer — pas d'en sauver un ou de revenir à un autre."
))
story.append(PageBreak())


# ============================================================
# PARTIE 1 — APPRENDRE À PERDRE SANS S'EFFONDRER
# ============================================================
_part_color[0] = PART_COLORS[0]
_part_num[0] = 1
_part_name[0] = "Apprendre à perdre"
ACCENT = PART_COLORS[0]

story.extend(part_separator(1, "Apprendre à perdre", "sans s'effondrer", ACCENT))

story.extend(part_intro_header(1, "Apprendre à perdre sans s'effondrer",
    "Pourquoi tu cramés après avoir bien gagné — et comment l'arrêter", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tu connais ta méthode (SMC, killzones, FVG, OB). Tu lis les marchés. Et pourtant tu crames tes comptes "
    "Apex/Topstep/Alpha. La cause n'est pas dans ton savoir — elle est dans <b>ce que tu fais sous pression</b>. "
    "Cette première partie pose les fondations psychologiques de tout le reste. Sans elle, le reste flotte."
))
story.append(P(
    "Tu vas comprendre ici les 6 mécanismes psychologiques qui expliquent pourquoi tu perds après avoir bien "
    "gagné. Ce ne sont pas tes mécanismes — ce sont ceux de tout humain qui trade. Tu n'es pas faible. Tu es "
    "<b>câblé</b>, comme tout le monde. La différence va se faire dans ce que tu fais de ce câblage."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "Le décalage savoir / exécution", ACCENT))
story.extend(retenir(
    "Savoir quoi faire et faire ce qu'on sait sont DEUX compétences. La première vit dans ta tête (rapide à "
    "acquérir). La seconde vit dans ton système nerveux sous pression (lente à installer)."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Trois étages dans toute compétence humaine : <b>(1) cognitif</b> — tu peux expliquer ; "
    "<b>(2) procédural</b> — tu peux faire au calme ; <b>(3) identitaire</b> — tu fais quand ton préfrontal "
    "est désactivé sous pression. À +1500 PnL, ton préfrontal est OFF. Tout ce qui n'est pas devenu réflexe "
    "corporel disparaît. Tes connaissances SMC sont à l'étage 1. Ton edge réel doit être à l'étage 3.",
    "<b>Pourquoi le cerveau préfère l'étage 1.</b> Apprendre une nouvelle méthode est dopaminergiquement agréable "
    "(sensation de progrès). Travailler son comportement est dopaminergiquement désagréable (confrontation avec "
    "le saboteur). Ton cerveau choisit la voie agréable — il te pousse vers le prochain livre. Piège déguisé "
    "en discipline."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Combien de méthodes différentes as-tu testées depuis 18 mois ? Combien de mentors, formations, Discords ? "
    "Quand tu galères, ton premier réflexe est-il d'observer ou de chercher un nouvel outil ?",
    "Si ton ratio « apprendre/observer » est >> 5:1, tu es bloqué à l'étage 1. Signal d'alerte : quand tu te dis "
    "« il me manque encore un truc », c'est ton cerveau qui fuit l'étage 3."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Saboteur :</b> tu cramés un compte 50K. Tu te dis « il me manque un confluence delta volume ». "
    "Vidéo YouTube de 47 min à 3h du matin. Productif en apparence. Rien réglé.",
    "<b>Cible :</b> tu cramés. Tu écris : « mon edge n'a pas changé. À +1700 j'ai senti une chaleur dans la "
    "poitrine, j'ai joué. C'est un problème de SN à +1700, pas de signal. » Demain je m'attaque à ça."
]))

story.append(Schema(6*cm, lambda c, w, h: draw_flow(c, w, h,
    ["ÉTAGE 1 — Savoir cognitif", "ÉTAGE 2 — Savoir-faire au calme", "ÉTAGE 3 — Être sous pression"],
    accent=ACCENT, color_first=GOLD_PALE, color_last=GREEN)))
story.append(P("La descente verticale, pas l'extension horizontale.", caption))

story.append(styled_table([
    [C("Concept", cell_g), C("Chez moi", cell_g), C("Correction", cell_g)],
    [C("Étage 1 (savoir)"), C("Je connais SMC parfait"), C("Stop d'ajouter. Purge 6 semaines.")],
    [C("Étage 2 (calme)"), C("Je gère bien en démo"), C("Tester en réel doses progressives")],
    [C("Étage 3 (pression)"), C("Je craque à +1500"), C("Répétition consciente + somatique")],
], [3.5*cm, 6*cm, 6.5*cm]))
story.append(Spacer(1, 8))

story.extend(exercice([
    "<b>L'inventaire de fuite.</b> Liste tout le contenu trading consommé en 6 mois (vidéos, mentors, formations). "
    "À côté de chaque ligne, écris ce que ça a réellement changé dans ton COMPORTEMENT. Pas dans ton SAVOIR. "
    "La colonne droite sera quasi vide. C'est ton diagnostic."
]))
story.extend(phrase_ancre(
    "« Je n'ai pas un problème de savoir. J'ai un problème d'exécution. J'arrête d'apprendre, j'installe. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "L'asymétrie psychologique de la perte", ACCENT))
story.extend(retenir(
    "Perdre 100€ fait neurologiquement 2 fois plus mal que gagner 100€ ne fait plaisir. Ce n'est pas une faiblesse "
    "— c'est documenté chez tous les humains (Kahneman, prix Nobel 2002). Cette asymétrie pourrit toutes tes "
    "décisions."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Le cerveau humain a évolué dans un environnement où perdre 100 calories pouvait signifier "
    "mourir, tandis que gagner 100 calories était juste un peu de marge. L'asymétrie est ancrée dans le câblage "
    "de survie. En trading : tu coupes les gains trop tôt (peur de les voir s'évaporer = douleur anticipée) et "
    "tu tiens les pertes trop long (refus d'acter la douleur = espoir).",
    "<b>Conséquence directe.</b> Sans correction, ton edge mathématique est négatif même avec une méthode positive. "
    "Tu tronques systématiquement la queue droite de ta distribution (gains coupés tôt) et tu allonges la queue "
    "gauche (pertes laissées traîner). C'est exactement l'inverse de ce qu'il faut."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "À +600 avec TP à +1000, tu coupes parfois plus tôt « au cas où ». À -300 avec SL à -400, tu décales parce "
    "que « -400 c'est trop, je veux juste -200 ». L'asymétrie pilote les deux décisions, dans la même direction "
    "destructrice."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(5.5*cm, lambda c, w, h: draw_seesaw(c, w, h, state="pain")))
story.append(P("La balance émotionnelle penche TOUJOURS du côté douleur. C'est le câblage à compenser.", caption))

story.extend(application([
    "<b>Saboteur :</b> XAUUSD long. +400 PnL. Tu coupes par peur de voir disparaître. Plan disait +800. Tu as "
    "tronqué ton edge.",
    "<b>Cible :</b> tu sens monter la peur. Tu nommes : « asymétrie qui parle, pas info marché ». Tu fermes la "
    "plateforme. TP fait son boulot. Tu reviens au TP atteint."
]))

story.append(styled_table([
    [C("Concept", cell_g), C("Chez moi", cell_g), C("Correction", cell_g)],
    [C("Aversion à la perte"), C("Je décale les SL"), C("Plateforme fermée mécanique")],
    [C("Coupe précoce gain"), C("TP à +400 au lieu +800"), C("BE à +1R + laisser courir")],
    [C("Tenue pertes"), C("Décalage chronique"), C("SL sacré, jamais déplacé loin")],
], [4*cm, 5.5*cm, 6.5*cm]))
story.append(Spacer(1, 8))

story.extend(exercice([
    "<b>Visualisation pré-trade — version perte.</b> Avant chaque trade, 60 sec : tu te visualises perdre la somme "
    "prévue calmement, le SL touché, la plateforme fermée. Tu sens la déception. Tu respires. Tu nommes : « OK, "
    "c'est dans la distribution ». Tu pré-désensibilises ton SN. Quand la perte arrive vraiment, c'est une "
    "répétition, pas une surprise."
]))
story.extend(phrase_ancre(
    "« Perdre fait deux fois plus mal qu'il ne devrait. Je le sais. Je compense par mécanique, pas par volonté. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "La revanche émotionnelle après une perte", ACCENT))
story.extend(retenir(
    "Après une perte, ton cerveau cherche immédiatement à effacer la douleur par un gain qui « annule ». Ce besoin "
    "est si fort qu'il te fait prendre des trades que tu n'aurais jamais pris à froid. La deuxième perte est "
    "presque garantie."
))
story.extend(explication([
    "<b>Le mécanisme.</b> La perte produit (1) une chute de dopamine, (2) une activation de cortisol, (3) une "
    "atteinte identitaire (« je ne suis pas un trader qui gagne »). Pour compenser ces trois, le cerveau cherche "
    "un grand pic dopaminergique rapide. Tu prends un trade B-grade avec taille augmentée. Le risque est démesuré "
    "par rapport à un setup A+ taille normale. La deuxième perte est plus grosse. Le cycle s'enclenche."
]))
story.extend(danger(
    "C'est la séquence qui crame les comptes le plus vite. Pas une perte isolée. C'est la perte + la revanche + "
    "la deuxième perte + la troisième revanche... 1 à 2 heures suffisent pour casser un compte funded."
))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu perds -300 à 10h30. À 10h45, tu reprends un trade « pour me refaire ». Setup pas optimal. Taille 2x. "
    "-700. Tu enchaînes. -1500. Drawdown trailing cassé. Compte mort à 11h pour un setup A+ raté à 10h30."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(7*cm, lambda c, w, h: draw_flow(c, w, h,
    ["Perte -300", "Cerveau réclame pic compensatoire IMMÉDIAT",
     "Trade B-grade taille augmentée", "Perte -700",
     "Urgence amplifiée → cycle", "COMPTE CRAMÉ en 1-2h"],
    accent=ACCENT, color_first=ACCENT, color_last=RED_ACC)))
story.append(P("La cascade de la revanche — 1-2 heures suffisent.", caption))

story.extend(application([
    "<b>Cible :</b> -300 à 10h30. Tu reconnais le signal. Tu fermes la plateforme PHYSIQUEMENT. Téléphone autre "
    "pièce. Tu sors marcher 30 min. Tu reviens à 12h. Tu décides à froid si tu reprends. La revanche est désamorcée."
]))

story.extend(exercice([
    "<b>Règle de pause obligatoire post-perte.</b> Écris dans ton cahier en haut : « Après chaque perte > 1% du "
    "compte, je ferme la plateforme 2 heures minimum. Pas de discussion. » Tu signes. Tu colles. Tu appliques "
    "30 jours sans exception. Une seule exception efface tout le travail."
]))
story.extend(phrase_ancre(
    "« Mon cerveau réclame une revanche. Je ne lui donne pas. Je lui donne du temps. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "La toxicité du gain qui te rend invincible", ACCENT))
story.extend(retenir(
    "Un gros gain est NEUROLOGIQUEMENT plus dangereux qu'une grosse perte. La perte te rend prudent. Le gain te "
    "rend imprudent. L'imprudence après un gain crame les comptes plus vite que la peur après une perte."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Le gain produit un pic dopaminergique massif + une distorsion de l'auto-perception "
    "(« je maîtrise »). Cette distorsion s'appelle l'illusion de contrôle. Tu attribues le gain entièrement à "
    "ta compétence (alors qu'il y a une part de chance) et tu en déduis que tu peux prendre plus de risque. "
    "C'est exactement à ce moment que les pros parlent de « se croire invincible ». La perte qui suit est "
    "statistiquement plus grosse que ce que tu venais de gagner."
]))
story.extend(make_callout("◈  CHEZ TOI — TON PATTERN +1500", [
    "+1500 PnL. Tu coupes pas. Tu pousses parce que « le marché est avec moi ». +1800. +2200. Reverse. -300 par "
    "rapport à l'entrée. SL touché — ou décalé. Compte cramé. Le crash n'est pas dû à un mauvais setup. Il est "
    "dû à l'euphorie qui a fait disparaître ton plan."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(7*cm, lambda c, w, h: draw_flow(c, w, h,
    ["Gain (+1500)", "Pic dopamine massif", "Illusion de contrôle",
     "Sentiment d'invincibilité", "Taille augmentée / B-grade",
     "Perte = 2-3x le gain"],
    accent=ACCENT, color_first=GREEN, color_last=RED_ACC)))
story.append(P("Le gain est ton pire signal de danger. Pas la perte.", caption))

story.extend(application([
    "<b>Saboteur :</b> 3 trades gagnants matinée. Tu te sens flow. Tu rentres un 4e B-grade en augmentant la "
    "taille. Tu te crashes. Tu donnes 80% du gain. Tu finis à +200 au lieu de +1200.",
    "<b>Cible :</b> 3 gagnants. Tu reconnais que ton cerveau va vouloir doubler. Tu décides à 11h : « j'arrête "
    "pour aujourd'hui. Je sécurise +1000. » Tu fermes. Tu pansa ta filly. Le gain reste."
]))

story.extend(exercice([
    "<b>La règle du quota positif.</b> Décide à l'avance qu'au-dessus de X% de gain dans la session, tu fermes la "
    "plateforme — peu importe la qualité des setups suivants. Exemple : +1500 atteint = fin de journée, point. "
    "Tu protèges contre toi-même quand ton préfrontal est OFF."
]))
story.extend(phrase_ancre(
    "« Le danger n'est pas dans la perte. Il est dans le gain qui me croit invincible. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Couper une perte comme victoire mentale", ACCENT))
story.extend(retenir(
    "Couper une perte au SL n'est pas un échec — c'est un succès. C'est la preuve que ton plan a été respecté, "
    "que ton système fonctionne, que tu es plus fort que ton émotion. Tant que tu vis ça comme un échec, tu "
    "décaleras toujours."
))
story.extend(explication([
    "<b>Le renversement de valeur.</b> Le mot « perte » est mal choisi. Un SL touché = ton edge fonctionne "
    "(tu as la moitié de ta distribution sur la queue gauche, c'est mathématique). Le seul vrai échec en trading "
    "n'est PAS la perte — c'est le <b>non-respect du plan</b>. Si tu coupes ton SL exactement où tu l'avais "
    "prévu, tu as GAGNÉ mentalement. Si tu décales (même si le marché finit par revenir), tu as PERDU mentalement.",
    "<b>Conséquence pratique.</b> Tu sépares deux notations dans ton journal : (1) PnL pur — neutre — (2) discipline — "
    "OUI/NON. Tu ne te juges que sur la note 2 pendant 30 jours. Tu déconnectes ton estime de toi du PnL. "
    "C'est l'inversion qui change tout."
]))

story.append(Schema(5*cm, lambda c, w, h: draw_comparison(c, w, h,
    "ANCIEN", ["« j'ai perdu »", "ego blessé", "envie de revanche", "trade impulsif"],
    "NOUVEAU", ["« j'ai respecté »", "ego renforcé", "continuer le plan", "trade discipliné"]
)))
story.append(P("Le même événement, deux interprétations. La deuxième construit.", caption))

story.append(styled_table([
    [C("Événement", cell_g), C("Vieux jugement", cell_g), C("Nouveau jugement", cell_g)],
    [C("SL touché"), C("Échec"), C("Discipline ✓")],
    [C("TP touché"), C("Succès"), C("Discipline ✓")],
    [C("SL décalé qui revient"), C("« Bien joué »"), C("ÉCHEC mental")],
    [C("Plan respecté"), C("(ignoré)"), C("Vraie victoire")],
], [4.5*cm, 5*cm, 6.5*cm]))
story.append(Spacer(1, 8))

story.extend(exercice([
    "<b>La double notation.</b> Pour chaque trade, deux notes séparées dans ton journal. <b>Note 1 (PnL)</b> : "
    "neutre, juste un chiffre. <b>Note 2 (discipline)</b> : OUI/NON sur respect du plan. Pendant 30 jours, tu "
    "félicites/critiques uniquement sur la note 2."
]))
story.extend(phrase_ancre(
    "« Couper au SL n'est pas perdre. C'est gagner contre moi-même. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Le protocole personnel anti-sabotage", ACCENT))
story.extend(retenir(
    "Aucun trader rentable ne s'en remet à sa volonté ou à son humeur. Tous ont un PROTOCOLE écrit qui décide à "
    "leur place quand leur préfrontal est désactivé. Le protocole est l'outil le plus puissant du trader rentable."
))
story.extend(explication([
    "<b>Pourquoi pré-décider.</b> Trois fonctions du protocole : <b>(1) Pré-décision</b> — il décide à l'avance, "
    "quand tu es calme, ce que tu feras dans les moments chauds. <b>(2) Externalisation</b> — il sort la décision "
    "de ton cerveau émotionnel en la déléguant à une règle externe. <b>(3) Engagement</b> — écrit, signé, "
    "affiché, il crée une obligation contre laquelle ton cerveau émotionnel doit lutter (et perd souvent). "
    "Sans protocole, tu prends des décisions en moment de crise — précisément le pire moment."
]))

story.append(P("Ton protocole personnel — version 1", h_section))
story.append(styled_table([
    [C("Moment", cell_g), C("Règle non négociable", cell_g)],
    [C("Avant session", cell_b),
     C("Check 6 questions (sommeil, énergie, état SN, plan, taille, prêt à perdre). Si <4/6 OUI → pas de trade.")],
    [C("Entrée trade", cell_b),
     C("SL placé AVEC l'ordre. Visualisation 90s faite.")],
    [C("À +1R", cell_b),
     C("Remonter SL au break-even. Mécanique. Pas de discussion.")],
    [C("TP atteint", cell_b),
     C("Couper. Pas de négociation. Fermer la plateforme.")],
    [C("SL approché", cell_b),
     C("Plateforme fermée. Téléphone autre pièce. SL fait son boulot sans moi.")],
    [C("Après gain > seuil jour", cell_b),
     C("Stop session. Pause 24h. Pas de trade le lendemain.")],
    [C("Après perte > seuil", cell_b),
     C("Stop session. Pause 24h.")],
    [C("Après 2 pertes consécutives", cell_b),
     C("Stop session immédiat.")],
    [C("Après crash compte", cell_b),
     C("Sevrage 4 semaines. Non négociable.")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Écriture du protocole.</b> Cette semaine, tu écris à la main, sur une feuille, ton protocole personnel. "
    "Tu remplis les 9 lignes du tableau ci-dessus avec TES seuils précis. Tu signes en bas. Tu colles au mur "
    "derrière ton écran. Tu le relis avant chaque session pendant 30 jours."
]))
story.extend(phrase_ancre(
    "« Ma volonté ne tient pas dans le moment chaud. Mon protocole, oui. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "La pensée en série — 100 trades, pas 1", ACCENT))
story.extend(retenir(
    "Le trader rentable ne juge JAMAIS un trade individuel. Il juge une série de 100 trades. Tant que tu juges "
    "trade par trade, tu es dans le piège émotionnel. La loi des grands nombres ne s'applique pas à 5 ou 10 "
    "trades — elle se révèle sur 100, 500, 1000."
))
story.extend(explication([
    "<b>Le principe.</b> Un edge à 55% de win rate avec RR 1:2 produit mathématiquement de l'argent — mais "
    "seulement sur la durée. Sur 5 trades, tu peux avoir 5 pertes successives (probabilité ~1,8% mais possible). "
    "Sur 100 trades, la distribution se révèle. Si tu ARRÊTES après les 5 pertes, tu ne sauras jamais si ton "
    "edge marchait. Tu auras quitté la roulette avant qu'elle ne te paye.",
    "<b>Le piège du jugement précoce.</b> 3 pertes consécutives ne disent RIEN sur ton edge. C'est statistiquement "
    "normal. Si tu changes ta méthode après 3 pertes, tu fais deux erreurs : (1) tu abandonnes potentiellement "
    "un edge valide, (2) tu casses la série de 100 nécessaire pour valider quoi que ce soit."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu juges trop tôt. Tu changes de méthode tous les 15-30 trades. Tu n'as JAMAIS eu une série de 100 trades "
    "exécutés selon le même protocole strict. Donc tu ne sais pas si ton edge marche. Tu sais seulement que tu "
    "n'as jamais tenu assez longtemps pour le découvrir."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> tu écris dans ton journal en page de garde : « Série en cours — Trade n° X / 100. Méthode "
    "stricte : SMC + killzones London/NY. Risque 0,5%. SL+TP préfixés. BE à +1R. » Tu coches chaque trade. "
    "Avant le trade 100, INTERDIT de modifier la méthode."
]))

story.append(styled_table([
    [C("Nombre trades", cell_g), C("Conclusion possible", cell_g)],
    [C("5"), C("Aucune. Bruit statistique pur.")],
    [C("20"), C("Très limitée. Tendance possible, pas validée.")],
    [C("50"), C("Indicative. Direction se dessine.")],
    [C("100"), C("Premier vrai signal. Tu peux commencer à juger.")],
    [C("300+"), C("Solide. Tu connais ton edge réel.")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Grille 100 trades.</b> Dans ton cahier, dessine une grille de 100 cases (10×10). Chaque trade exécuté "
    "selon protocole = 1 case cochée (vert = gain, rouge = perte). Tu vises les 100. Tu ne tires AUCUNE "
    "conclusion avant. C'est l'engagement de discipline le plus puissant que tu puisses prendre.",
    "<b>Règle de gel.</b> Pendant la série de 100, tu ne modifies RIEN : méthode, taille, indicateur, timeframe. "
    "Même si tu prends 8 pertes consécutives. La modification se décide UNIQUEMENT après les 100 trades, à froid."
]))
story.extend(phrase_ancre(
    "« Je joue la série de 100. Pas ce trade. Le résultat individuel ne dit rien. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "L'opérateur stable — sommeil, énergie, état de base", ACCENT))
story.extend(retenir(
    "Ton edge technique ne peut s'exprimer que si l'opérateur (toi) est dans un état de base correct. Sommeil, "
    "alimentation, hydratation, énergie, état émotionnel : ce sont les variables muettes qui décident de tes "
    "performances bien plus que le setup."
))
story.extend(explication([
    "<b>L'effet du sommeil.</b> Une nuit à 5h de sommeil produit un déficit cognitif équivalent à 0,5g d'alcool "
    "dans le sang. Les recherches montrent que les traders qui dorment moins de 6h prennent significativement "
    "plus de risques, sous-estiment les pertes potentielles et surestiment leur edge. Tu ne le ressens pas — "
    "ton cerveau ne sait pas qu'il est dégradé.",
    "<b>L'effet de la glycémie.</b> Une glycémie qui chute (jeûne prolongé, mauvais petit-déjeuner) produit "
    "irritabilité, impatience, prise de décision dégradée. Tu confonds l'urgence physiologique de manger avec "
    "« faut que je trade maintenant ».",
    "<b>L'effet du baseline émotionnel.</b> Une dispute, un stress relationnel, une mauvaise nouvelle non digérée "
    "te suit dans la session. Tu ne traites pas l'émotion — elle traite ton trading à ta place."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Post-TBI, ton besoin de sommeil est probablement supérieur à la moyenne — 8-9h pour récupération neuronale "
    "complète. Si tu dors 6h, tu trades dégradé sans le savoir. Tu attribues les mauvaises décisions à un "
    "manque de discipline. La cause réelle est physiologique."
], GOLD, NAVY, accent=NAVY))

story.append(P("Check pré-session — l'opérateur est-il en état ?", h_sub))
story.append(styled_table([
    [C("Variable", cell_g), C("État OK", cell_g), C("État RED FLAG = pas de trade", cell_g)],
    [C("Sommeil"), C("7-9h, qualité"), C("< 6h ou agité")],
    [C("Petit-déjeuner"), C("Pris, équilibré"), C("Sauté ou junk food")],
    [C("Hydratation"), C("Eau le matin"), C("Café seul à jeun")],
    [C("Émotion baseline"), C("Calme, neutre"), C("Conflit récent, news perso")],
    [C("Énergie"), C("Stable, 6+/10"), C("< 5/10 ou hyperexcité")],
    [C("Substances"), C("Aucune dernières 24h"), C("Alcool hier, drogue récréative")],
], [3.5*cm, 4*cm, 8.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> avant chaque session, 2 minutes de check des 6 variables. Si ≥2 sont en red flag → "
    "PAS de trading aujourd'hui. Tu fais autre chose. Tu protèges ta série de 100."
]))

story.extend(exercice([
    "<b>Journal d'état pré-session.</b> Pendant 30 jours, note chaque matin les 6 variables sur 10. Note "
    "aussi ton PnL de la session. Au bout de 30 jours, tu vas voir une corrélation claire entre tes variables "
    "low (< 5/10) et tes journées perdantes. Tu sauras précisément quels états bloquent ton edge.",
    "<b>Routine de coucher.</b> 22h max au lit (pour 23h endormi). Pas d'écran 60 min avant. Lecture papier. "
    "Respiration cohérente 5 min. C'est ton outil de productivité trading le plus rentable."
]))
story.extend(phrase_ancre(
    "« Mon edge ne peut pas s'exprimer si l'opérateur est dégradé. Je protège l'opérateur. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 1 ---
story.append(P("Carte mentale — Partie 1", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Apprendre à perdre",
    [
        {"label": "MÉCANISMES", "leaves": ["décalage savoir/exé", "aversion perte", "revanche émotionnelle", "toxicité du gain"], "color": NAVY},
        {"label": "INVERSIONS", "leaves": ["perte = victoire", "gain = danger", "PnL ≠ identité"], "color": ACCENT},
        {"label": "OUTIL CLÉ", "leaves": ["protocole écrit", "signé / affiché", "non négociable"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Comprendre → Inverser → Installer le protocole.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 1", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  APPRENDRE À PERDRE — FICHE D'ANCRAGE                     ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Le gain qui me rend invincible (+1500 puis crash).      ║
║    Le décalage de SL pour éviter la douleur immédiate.     ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Chaleur dans la poitrine à +1500                      ║
║    - Phrase « ça va revenir » quand SL touché              ║
║    - Envie urgente de reprendre après perte                ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    Plateforme fermée. Téléphone autre pièce.               ║
║    90 secondes de respiration.                             ║
║                                                            ║
║  RÈGLE DE TRADING                                          ║
║    SL bouge UNIQUEMENT vers le profit (BE à +1R).          ║
║    TP coupé sans négociation.                              ║
║    Aucun trade en revanche.                                ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Je joue ma série de 100. Pas ce trade-ci.             ║
║      Couper au SL est une victoire. »                      ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


print("✓ Cover, préface, sommaire, intro, Partie 1 écrits")


# ============================================================
# PARTIE 2 — DOPAMINE ET RECHERCHE DU PIC
# ============================================================
_part_color[0] = PART_COLORS[1]
_part_num[0] = 2
_part_name[0] = "Dopamine"
ACCENT = PART_COLORS[1]

story.extend(part_separator(2, "Comprendre la dopamine", "et la recherche du pic", ACCENT))

story.extend(part_intro_header(2, "Comprendre la dopamine et la recherche du pic",
    "La chimie cérébrale de ton addiction à l'intensité", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tu n'as pas un problème mental. Tu as un problème <b>neurochimique</b>. Ta boucle destructrice (gain → "
    "euphorie → risque → perte → revanche) n'est pas une faiblesse de caractère — c'est une boucle dopaminergique "
    "qui s'auto-entretient. Tant que tu attaques le problème comme une question de discipline, tu rates la cible. "
    "C'est de la chimie cérébrale."
))
story.append(P(
    "Tu as aussi un facteur aggravant majeur : ton TBI 2022 a probablement modifié ton baseline dopaminergique. "
    "Combiné à une attirance documentée pour l'intensité (« le calme me semble vide »), tu portes un système "
    "nerveux qui cherche en permanence à compenser un manque. Cette partie te donne la carte neurochimique "
    "de ce qui se passe dans ton cerveau quand tu trades, et le protocole de réparation."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "La bascule plaisir-douleur", ACCENT))
story.extend(retenir(
    "Le plaisir et la douleur occupent le même réseau cérébral, organisé comme une bascule. Chaque pic de "
    "plaisir produit une douleur compensatoire proportionnelle quelques heures plus tard. C'est mécanique, "
    "pas moral."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Principe d'homéostasie neurochimique. Le cerveau humain est obsédé par l'équilibre. "
    "Quand tu envoies un pic dopaminergique (gain XAUUSD, alcool, sucre, validation, pornographie), des "
    "récepteurs s'activent en compensation pour produire un état désagréable proportionnel — quelques minutes "
    "à plusieurs heures plus tard. Plus le pic est fort, plus le creux qui suit est profond.",
    "<b>Conséquence pratique.</b> Après une grosse journée gagnante, tu ressens souvent un vide étrange le "
    "lendemain. Ce n'est pas une humeur — c'est de la dette neurochimique. Tu ouvres la plateforme « pour "
    "combler le vide ». Tu prends un B-grade. Tu te crashes. Le crash n'est pas dû au B-grade — il est dû "
    "au creux de la bascule."
]))
story.append(Schema(4*cm, lambda c, w, h: draw_seesaw(c, w, h, state="pleasure")))
story.append(P("Le pic de plaisir produit le creux qui suit. Pas de bonheur sans dette.", caption))

story.extend(make_callout("◈  CHEZ TOI", [
    "Lundi tu fais +2000. Tu te couches euphorique. Mardi tu te lèves vaseux, vide. Tu ouvres la plateforme "
    "pour combler le vide. Tu prends un setup B-grade. Tu cramés -2000. Le marché n'a fait que t'offrir le "
    "moyen — la cause était dans le creux de la bascule."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> tu fais +1500 vendredi. Tu reconnais le pic. Tu sais que le creux arrive. Tu décides à "
    "l'avance : pas de trading lundi. Journée OFF avec sport, lecture, ta filly. Tu donnes à ton baseline "
    "le temps de remonter. Au retour, tu trades propre."
]))

story.append(styled_table([
    [C("Phase", cell_g), C("Sensation", cell_g), C("Durée", cell_g), C("Risque", cell_g)],
    [C("Pic"), C("Euphorie, puissance"), C("30 min-2h"), C("Pousser, taille augmentée")],
    [C("Plateau"), C("Stabilité fausse"), C("2-6h"), C("Setups bof acceptés")],
    [C("Creux"), C("Vide, irritabilité"), C("12-48h"), C("Chercher nouveau pic")],
    [C("Retour baseline"), C("Calme retrouvé"), C("Si pas re-stimulé"), C("Trading propre possible")],
], [2.5*cm, 4*cm, 3*cm, 6.5*cm]))
story.append(Spacer(1, 8))

story.extend(exercice([
    "<b>Cartographie 7 jours.</b> Chaque soir, note (1) ton plus gros pic dopaminergique de la journée (gain, "
    "sucre, validation, alcool, écran intense), (2) ton état émotionnel 12-24h après. Tu vas voir le pattern "
    "de bascule apparaître clairement. Tu sauras quand le creux frappe."
]))
story.extend(phrase_ancre(
    "« Chaque pic produit un creux. Je n'alimente pas le creux par un autre pic. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "La tolérance dopaminergique", ACCENT))
story.extend(retenir(
    "À force de pics répétés, le cerveau diminue le nombre de récepteurs dopaminergiques actifs. Conséquence : "
    "il te faut une stimulation plus forte pour ressentir pareil. C'est le même mécanisme que la tolérance à "
    "l'alcool — appliqué au trading."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Le cerveau perçoit l'excès de dopamine comme un déséquilibre. Pour se protéger, il "
    "réduit sa sensibilité (down-regulation des récepteurs D2). Tu as donc besoin d'envoyer plus de signal pour "
    "produire la même sensation. Cycle : tu pousses plus → baseline baisse → tu pousses encore plus → baseline "
    "encore plus bas. Au bout : rien ne te fait plus rien. C'est l'anhédonie."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu ne peux plus tolérer un trade XAUUSD propre qui rapporte +500 sans vouloir le pousser à +1500. +500 ne "
    "suffit pas à ton cerveau pour produire un signal de plaisir. Ce n'est pas une décision consciente — c'est "
    "ton baseline qui réclame plus. Ta phrase « le calme me semble vide » est le diagnostic neurochimique de "
    "cette tolérance avancée."
], GOLD, NAVY, accent=NAVY))

story.extend(ascii_box("""
Mois 0 (baseline sain)         →  +500 = plaisir réel
Mois 6 (stimulé)               →  +500 = rien. Faut +1500.
Mois 12 (sans pause)           →  +1500 = rien. Faut +3000.
Mois 18 (anhédonie)            →  rien ne fait rien.

+ 4 semaines de sevrage strict →  baseline remonte. +500 = plaisir.
""", accent=ACCENT))

story.extend(application([
    "<b>Saboteur :</b> tu prends un setup A+ qui paye +600. Tu te dis « ça ne vaut pas le coup ». Tu laisses "
    "courir. Le pic à +1500 produit enfin une sensation. Reverse. Compte cassé.",
    "<b>Cible :</b> tu prends le setup. Tu coupes à +600 comme prévu. Tu reconnais : « tolérance — pas besoin "
    "réel ». Tu fermes. À force de répéter, le baseline remonte. Dans 4 semaines, +600 redonne une vraie satisfaction."
]))

story.extend(exercice([
    "<b>Test du baseline.</b> Liste 5 choses qui te procuraient du plaisir AVANT 2022 et qui te procurent moins "
    "maintenant. Ces 5 mesurent ta perte de baseline. Pendant 14 jours, fais une chose simple et lente par jour "
    "(marche sans téléphone 45 min, repas sans écran, pansage 30 min). Évalue 1-10 le plaisir ressenti. "
    "Tu vas voir : ça remonte."
]))
story.extend(phrase_ancre(
    "« Mon cerveau réclame plus. Je n'ai pas besoin de plus. Je laisse remonter mon baseline. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "L'anticipation est plus puissante que la récompense", ACCENT))
story.extend(retenir(
    "Ce qui te shoote en dopamine n'est PAS le gain réalisé — c'est l'ATTENTE du gain. Le pic est avant le "
    "résultat, pas après. C'est pour ça que les pertes ne t'arrêtent pas : ton cerveau cherche le shoot "
    "d'anticipation suivant."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Les recherches de Wolfram Schultz ont montré que les neurones dopaminergiques s'activent "
    "au moment où l'animal ANTICIPE la récompense, pas au moment où il la reçoit. C'est ce qui rend les jeux "
    "d'argent si addictifs — c'est le « est-ce que ça va tomber ? » qui shoote. Appliqué au trading : ouvrir "
    "un trade est plus dopaminergique que voir son TP atteint."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu ouvres un trade et tu sens immédiatement la montée. La position est encore à zéro — aucune info — mais "
    "ton cerveau est déjà en pic. Tu ne traites pas le trading comme une exécution rationnelle — tu traites "
    "chaque clic comme un shoot. C'est pour ça que tu ouvres parfois des trades B-grade : pas pour le profit, "
    "pour le shoot d'ouverture."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Saboteur :</b> 14h, pas de A+. Tu sens un creux. Tu ouvres un B-grade « juste pour voir ». Pas la "
    "qualité — le shoot d'attente. Tu rationalises ensuite. Tu cramés -400.",
    "<b>Cible :</b> 14h, pas de A+. Tu reconnais : « creux qui réclame un shoot, pas une opportunité ». Tu ne "
    "cliques pas. Marche, lecture, sport. Le creux passe en 60-90 min."
]))

story.extend(exercice([
    "<b>Le test du clic.</b> Pendant une session, avant chaque clic Buy/Sell, tu pauses 30 secondes et tu te "
    "demandes : « est-ce que je cherche à exécuter un A+ ou à recevoir un shoot d'anticipation ? » Si la réponse "
    "honnête est « shoot », tu ne cliques pas. Cette pause coupe le pattern à la source."
]))
story.extend(phrase_ancre(
    "« Le clic me shoot avant que le marché bouge. C'est ça que je chasse — pas le profit. Je le sais. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "Le renforcement intermittent (pourquoi le décalage SL est si addictif)", ACCENT))
story.extend(retenir(
    "En psychologie expérimentale, le mode de conditionnement le plus puissant connu n'est PAS la récompense "
    "régulière — c'est la récompense imprévisible et intermittente. Une récompense qui tombe 1 fois sur 10 "
    "addicte plus solidement qu'une récompense systématique."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Skinner a démontré qu'un pigeon récompensé une fois sur dix appuie sur le levier plus "
    "longtemps et plus intensément qu'un pigeon récompensé à chaque fois. Le renforcement intermittent produit "
    "un comportement d'extinction lente — extrêmement résistant à l'arrêt.",
    "<b>Appliqué à toi.</b> Chaque fois que tu décales un SL et que le marché revient (1 fois sur 5 à 1 fois sur "
    "10), tu renforces massivement le comportement. Tu deviens neuro-conditionné à décaler. Tu sais "
    "rationnellement que c'est destructeur. Tu décales quand même. Ce n'est pas un manque de volonté — c'est "
    "un conditionnement neuronal plus puissant que ta volonté."
]))

story.extend(danger(
    "La fois où le décalage marche te tient plus solidement que les 8 fois où il te crame. C'est la définition "
    "neurologique d'une addiction. Tu ne peux pas arrêter par la volonté seule. Il faut une règle externe."
))

story.extend(ascii_box("""
RÉCOMPENSE RÉGULIÈRE                RÉCOMPENSE INTERMITTENTE
───────────────────                 ─────────────────────────
Tu reçois X à chaque fois.          Tu reçois X 1 fois sur 5-10.
   ↓                                   ↓
Extinction RAPIDE                   Extinction TRÈS LENTE
si X disparaît.                     Tu continues longtemps même
                                    sans récompense.
                                        ↓
                              CONDITIONNEMENT LE PLUS
                              PUISSANT CONNU EN PSYCHO.
                                        ↓
                              Décalage SL qui paye parfois
                              = TU NE PEUX PAS ARRÊTER
                                par la volonté seule.
""", accent=ACCENT))

story.extend(exercice([
    "<b>Compteur d'extinction.</b> Tu comptes les sessions consécutives SANS décalage de SL. Chaque session "
    "sans : +1. À la première rechute : retour à zéro. Vise 50 sessions consécutives. À 50, le conditionnement "
    "est neutralisé. Le compteur visible (sur ton mur) devient lui-même un renforçateur positif."
]))
story.extend(phrase_ancre(
    "« Mon conditionnement est plus fort que ma volonté. Donc je rends le geste mécaniquement impossible. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Le jeûne dopaminergique", ACCENT))
story.extend(retenir(
    "Pour restaurer ton baseline, il faut t'abstenir totalement de la substance/comportement addictif pendant "
    "4 semaines minimum (idéalement 12 semaines). Le cerveau remonte progressivement les récepteurs D2. "
    "C'est biologique, pas mental."
))
story.extend(explication([
    "<b>Les phases du sevrage.</b> Les 14 premiers jours sont les plus durs : sevrage caractérisé "
    "(irritabilité, ennui intense, anxiété, sommeil perturbé, envie compulsive). Ce n'est PAS la preuve que "
    "le sevrage est mauvais — c'est la signature même du sevrage. Jours 14-28 : stabilisation. À partir de "
    "J+28, le baseline remonte visiblement. Réduire au lieu d'arrêter ne marche pas — le baseline ne remonte "
    "que si la stimulation est à zéro."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Si tu te dis « impossible d'arrêter 4 semaines », c'est précisément la preuve que tu dois le faire. Ce "
    "que tu ne peux pas lâcher 4 semaines te domine."
], GOLD, NAVY, accent=NAVY))

story.append(P("Protocole 4 semaines", h_sub))
story.append(styled_table([
    [C("Jours", cell_g), C("Phase", cell_g), C("Ce qui se passe", cell_g), C("Ce que tu fais", cell_g)],
    [C("1-7"), C("Sevrage aigu"),
     C("Manque, irritabilité, ennui"),
     C("Sport, pansage, sommeil, méditation")],
    [C("8-14"), C("Sevrage moyen"),
     C("Anxiété, désir, vide"),
     C("Tu tiens. Tu nommes le manque.")],
    [C("15-21"), C("Stabilisation"),
     C("Désir baisse, énergie revient"),
     C("Bases : lectures, ATHÉNA, relations")],
    [C("22-28"), C("Restauration"),
     C("Baseline qui remonte"),
     C("Validation par plaisirs simples")],
], [1.5*cm, 3*cm, 5.5*cm, 6*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Engagement signé.</b> Sur ton journal, à la main : « Du [date] au [date+28], je m'abstiens totalement "
    "de tout trading et tout contenu trading. Je signe pour Marien-du-futur. — [signature] ». Affiche au mur.",
    "<b>Désinstallation physique.</b> Apps de trading désinstallées, TradingView mot de passe changé et donné "
    "à un proche, Discord trading mute. Tu rends impossible la rechute impulsive."
]))
story.extend(phrase_ancre(
    "« Le sevrage n'est pas un test mental. C'est un protocole biologique. Je suis le protocole. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "L'inconfort volontaire et les substituts constructifs", ACCENT))
story.extend(retenir(
    "Logique inversée de la bascule : si chaque plaisir produit une douleur, alors chaque douleur volontairement "
    "endurée produit un plaisir. Cold exposure, sport intense, jeûne = dopamine endogène, sans tolérance."
))
story.extend(explication([
    "<b>Le mécanisme.</b> La douleur volontaire et brève active la libération de dopamine et d'endorphines en "
    "compensation. Mais cette dopamine-là est endogène — elle ne crée pas de down-regulation. Au contraire, "
    "elle re-sensibilise le système. Bain froid 2-5 min produit un afflux dopaminergique soutenu 4-6 heures. "
    "Sport intense produit un effet équivalent. Jeûne 16h améliore la sensibilité dopaminergique générale.",
    "<b>Substituts toxiques vs constructifs.</b> Quand tu sèvres le trading, ton cerveau cherche un autre shoot. "
    "Si tu laisses faire : alcool, sucre, écrans, scroll. Si tu pré-choisis : sport, lecture, pansage, "
    "relations qualitatives. Pré-décider est essentiel."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu es déjà très bien équipé : box, équitation explosive, rééducation post-TBI t'a entraîné à tolérer "
    "l'inconfort. Tu as la compétence — tu ne l'utilises pas systématiquement comme outil de régulation "
    "neurochimique. C'est la pièce manquante de ton sevrage."
], GOLD, NAVY, accent=NAVY))

story.append(P("Menu d'inconfort volontaire", h_sub))
story.append(styled_table([
    [C("Protocole", cell_g), C("Durée", cell_g), C("Fréquence", cell_g), C("Effet", cell_g)],
    [C("Cold shower"), C("2-5 min"), C("Quotidien"), C("Dopamine soutenue 4-6h")],
    [C("Sport HIIT / box"), C("30-60 min"), C("3x/sem"), C("Endorphines + dopamine 2-4h")],
    [C("Jeûne intermittent 16:8"), C("16h"), C("Quotidien"), C("Sensibilité globale")],
    [C("Marche sans téléphone"), C("60+ min"), C("Quotidien"), C("Tolérance ennui")],
    [C("Lecture papier"), C("1h"), C("Quotidien"), C("Plaisirs lents restaurés")],
    [C("Méditation Dispenza"), C("20-60 min"), C("Quotidien"), C("Système récompense réorganisé")],
], [4*cm, 2*cm, 2.5*cm, 7.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Protocole 14 jours.</b> Engage-toi : 1 douche froide quotidienne + 1 séance sport intense tous les 2 "
    "jours. Note ton état émotionnel le soir 1-10. Tu vas voir le baseline remonter rapidement.",
    "<b>Carte de substitution.</b> À gauche : tes 5 comportements toxiques de compensation. À droite : "
    "l'équivalent constructif. Affiche au mur. Tu sais quoi faire quand le besoin monte."
]))
story.extend(phrase_ancre(
    "« Pour que mon plaisir naturel revienne, j'enseigne à mon cerveau à passer par la douleur volontaire. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "L'effet du presque — pourquoi tu reviens même quand tu perds", ACCENT))
story.extend(retenir(
    "Le near-miss effect : un PRESQUE-gain produit un pic dopaminergique presque équivalent à un vrai gain. "
    "Documenté chez les joueurs de machines à sous. C'est pour ça que perdre ne t'arrête pas — chaque trade "
    "« presque gagné » te recharge en envie de continuer."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Imagerie cérébrale chez les joueurs de machines à sous : un near-miss (deux symboles "
    "alignés sur trois) produit une activation dopaminergique presque identique à un vrai jackpot — alors que "
    "rationnellement c'est une PERTE. Ton cerveau ne distingue pas. Il enregistre le « presque » comme un "
    "signal positif. Tu reviens jouer.",
    "<b>En trading.</b> Tu prends un trade qui atteint +800 puis reverse à -200. Tu te dis « j'étais à +800, "
    "j'ai presque gagné, ma prochaine sera la bonne ». Ton cerveau a enregistré +800 comme une quasi-réussite — "
    "alors que tu as perdu de l'argent réel. La frustration produit de l'élan, pas de l'arrêt."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tes pertes ne t'arrêtent pas parce que tu vois TOUJOURS des « presque-gains » dedans. « Si j'avais coupé "
    "+800 j'aurais gagné. » « Si j'avais pas décalé j'aurais sorti à zéro. » Chaque presque te recharge. C'est "
    "pour ça que tu reviens, encore et encore, malgré l'évidence des pertes accumulées."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> tu reformules systématiquement les « presque » en réalité. Pas « j'ai presque gagné +800 ». "
    "Mais « j'ai PERDU -200, point. Le +800 n'a jamais existé — c'était du PnL non réalisé, donc pas un gain. » "
    "Cette reformulation désarme la recharge dopaminergique."
]))

story.extend(exercice([
    "<b>Journal anti-near-miss.</b> Après chaque perte, dans ton journal, INTERDIT d'écrire la phrase « j'étais "
    "à +X PnL ». Tu écris uniquement le résultat final. -200, c'est -200. Pas « j'étais à +800 ». Le PnL flottant "
    "n'existe pas. Seul le PnL final compte. Tu coupes l'alimentation de la boucle."
]))
story.extend(phrase_ancre(
    "« Un presque-gain est une perte. Le PnL flottant n'existe pas. Seul le PnL final compte. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "La pleine présence comme antidote", ACCENT))
story.extend(retenir(
    "L'addiction se nourrit de l'évasion mentale — tu n'es pas là, tu es dans l'attente du prochain shoot. "
    "La pleine présence (être ici, maintenant, dans ce corps) est l'antidote neurologique direct. Pas une "
    "pratique mystique — une compétence d'attention dirigée."
))
story.extend(explication([
    "<b>Le mécanisme.</b> La pleine présence active le cortex préfrontal et désactive le réseau de mode par "
    "défaut (DMN — le réseau de rumination/projection). En clair : quand tu es pleinement présent à ce que tu "
    "fais maintenant, ton cerveau cesse de chasser le prochain shoot. La compulsion s'éteint temporairement.",
    "<b>Effet cumulatif.</b> Des études longitudinales montrent que 8 semaines de pratique régulière de mindfulness "
    "modifient mesurablement la structure de l'amygdale et du cortex préfrontal. Tu changes physiquement ton "
    "cerveau, pas juste tes pensées."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fais déjà de la méditation Dispenza. C'est excellent. Mais l'enjeu est de faire descendre cette compétence "
    "dans tes moments compulsifs — pas seulement le matin. Quand l'envie de cliquer monte à 14h, c'est LÀ que "
    "la présence te sauve. 90 secondes de présence corporelle = pic compulsif désamorcé."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Pratique", cell_g), C("Durée", cell_g), C("Effet immédiat", cell_g)],
    [C("Scan corporel"), C("5 min"), C("Recentre, calme le SN")],
    [C("Respiration consciente"), C("3 min"), C("Active le vagal ventral")],
    [C("Pleine présence aux sens"), C("2 min"), C("Sort de la rumination")],
    [C("Marche méditative"), C("10 min"), C("Désactive la chasse au shoot")],
    [C("Pleine présence en pansage"), C("30 min"), C("Co-régulation profonde")],
], [4.5*cm, 2*cm, 9.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Test du 5-4-3-2-1.</b> Quand tu sens monter la compulsion : nomme 5 choses que tu VOIS, 4 que tu "
    "ENTENDS, 3 que tu TOUCHES (peau, chaise, vêtement), 2 que tu SENS, 1 que tu GOÛTES. 2 minutes. Tu te "
    "ramènes dans le corps. La compulsion baisse de plusieurs crans.",
    "<b>Présence avant chaque session.</b> 3 min de présence corporelle pure (yeux fermés, attention au "
    "souffle, scan rapide) AVANT d'ouvrir la plateforme. C'est l'antidote préventif au mode compulsif."
]))
story.extend(phrase_ancre(
    "« Quand je suis ici, maintenant, dans mon corps, la compulsion ne peut pas piloter. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 2 ---
story.append(P("Carte mentale — Partie 2", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Dopamine",
    [
        {"label": "MÉCANIQUES", "leaves": ["bascule", "tolérance", "anticipation > récompense", "renforcement intermittent"], "color": NAVY},
        {"label": "CHEZ TOI", "leaves": ["baseline TBI bas", "calme = vide", "clic = shoot"], "color": ACCENT},
        {"label": "RÉPARATION", "leaves": ["jeûne 4 sem", "inconfort volontaire", "substituts constructifs"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Comprendre la chimie → Sevrer → Reconstruire le baseline.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 2", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  DOPAMINE — FICHE D'ANCRAGE                               ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Mon cerveau cherche le shoot d'anticipation,            ║
║    pas le profit. Je le confonds avec une intuition.       ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - « Le calme me semble vide »                           ║
║    - Envie de cliquer sans A+ identifié                    ║
║    - Lendemain de gros gain = vide / agitation             ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Cold shower 2-5 min (interrupt pattern)              ║
║    2. Sport intense ou marche 30 min                       ║
║    3. Pas de substitut toxique                             ║
║                                                            ║
║  RÈGLE DE TRADING                                          ║
║    Sevrage 4 semaines si je n'arrive pas à 30 jours        ║
║    sans craquer.                                           ║
║    Pause obligatoire le lendemain de tout pic.             ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Chaque pic produit un creux.                          ║
║      Je n'alimente pas le creux par un autre pic. »        ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


# ============================================================
# PARTIE 3 — TRAUMA ET SYSTÈME NERVEUX
# ============================================================
_part_color[0] = PART_COLORS[2]
_part_num[0] = 3
_part_name[0] = "Trauma et SN"
ACCENT = PART_COLORS[2]

story.extend(part_separator(3, "Comprendre le trauma", "et le système nerveux", ACCENT))

story.extend(part_intro_header(3, "Comprendre le trauma et le système nerveux",
    "Comment ton TBI 2022 pilote encore tes décisions", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Ton accident de 2022 — coma, traumatisme crânien, opérations multiples, immobilisation prolongée — est "
    "un <b>trauma au sens technique</b>. Pas une métaphore. Un événement où ton organisme a été confronté à "
    "une menace vitale qu'il n'a pas pu fuir ni combattre. La majorité des traders n'a pas vécu ça. Toi si. "
    "C'est probablement la variable la plus importante pour comprendre tes comportements actuels."
))
story.append(P(
    "Ton SN porte encore des empreintes de 2022 que ton mental ne perçoit pas mais que ton corps actionne "
    "quotidiennement. L'intolérance au calme. La crispation à +1500. La recherche d'intensité. L'hypervigilance "
    "discrète. Le sommeil parfois interrompu. Ce ne sont pas des traits — ce sont des conséquences neurologiques "
    "d'un trauma non pleinement digéré."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "Le trauma comme empreinte vivante", ACCENT))
story.extend(retenir(
    "Le trauma n'est pas un souvenir du passé. C'est un état présent du système nerveux qui n'a jamais digéré "
    "l'événement original. Le corps continue de reproduire les réflexes de survie de la menace originelle — "
    "des années plus tard."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Quand une menace vitale survient, le SN active une cascade : adrénaline, cortisol, "
    "mobilisation musculaire, hypervigilance. Normalement, après la menace, le corps DÉCHARGE cette énergie "
    "(tremblements, pleurs, mouvements involontaires). Quand cette décharge ne peut pas avoir lieu (anesthésie, "
    "immobilisation, coma), l'énergie reste FIGÉE. Le SN reste branché sur le mode urgence."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "2022 : accident + coma + opérations sous anesthésie + immobilisation. Ton SN a vécu une menace vitale ET "
    "n'a jamais pu décharger l'énergie de survie. Trois ans après, ton corps est réparé. Mais ton SN porte "
    "encore l'empreinte. Ce que tu vis aujourd'hui (intolérance au calme, recherche d'intensité, crispation, "
    "hypervigilance discrète) sont des conséquences directes — pas des choix conscients."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Symptôme actuel", cell_g), C("Interprétation erronée", cell_g), C("Interprétation juste", cell_g)],
    [C("Intolérance au calme"), C("« J'aime l'intensité »"), C("SN en alerte chronique")],
    [C("Crispation +1500"), C("« J'aime le risque »"), C("Activation extrême sur trigger")],
    [C("Décalage SL"), C("« Manque de discipline »"), C("SN qui fuit l'activation")],
    [C("Recherche pic"), C("« Je suis ambitieux »"), C("SN cherche décharge")],
], [4.5*cm, 5*cm, 6.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Reconnaissance.</b> Pendant 7 jours, à chaque moment où tu ressens agitation/irritation/envie de pic, "
    "tu écris dans ton journal : « SN figé qui parle, pas Marien qui parle. » Cette nomination casse "
    "l'identification. Tu cesses de croire que c'est toi qui réclames — c'est ton SN qui décharge un signal "
    "vieux de 3 ans."
]))
story.extend(phrase_ancre(
    "« Mon TBI 2022 n'est pas dans mon passé. Il est dans mon corps présent. Je travaille là où il est. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "Les 3 états du système nerveux", ACCENT))
story.extend(retenir(
    "Ton SN autonome a TROIS états — pas deux. Calme social (vagal ventral), mobilisation (sympathique : "
    "fight/flight), figement (vagal dorsal : freeze). Le trauma fige souvent dans les deux derniers et empêche "
    "le retour au premier."
))
story.extend(explication([
    "<b>La théorie polyvagale (Stephen Porges).</b> Le nerf vague a une structure hiérarchique. Si le vagal "
    "ventral (calme social) n'arrive pas à gérer la situation, le sympathique prend la suite. Si le sympathique "
    "ne suffit pas, le vagal dorsal prend le relais en figement. Cascade descendante. Pour remonter, il faut "
    "faire le chemin INVERSE : du figement → mobilisation → calme. On ne saute pas d'étape."
]))
story.append(Schema(7*cm, lambda c, w, h: draw_polyvagal(c, w, h)))
story.append(P("Hiérarchie polyvagale — connaître ton état à chaque instant.", caption))

story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fonctionnes la plupart du temps en SYMPATHIQUE. Devant l'écran tu accentues encore. À +1500 PnL, tu es "
    "en hyper-sympathique extrême. Quand le marché reverse et que tu perds gros, tu peux basculer dans le VAGAL "
    "DORSAL (vide, dissociation, « je ne sens plus rien »). Ton trading active donc les deux états traumatiques. "
    "Le vagal ventral, tu le rencontres rarement — peut-être en pansage avec ta filly, peut-être en méditation."
], GOLD, NAVY, accent=NAVY))

story.append(P("Comment activer chaque état", h_sub))
story.append(styled_table([
    [C("État", cell_g), C("Sensation", cell_g), C("Comment activer", cell_g)],
    [C("Vagal ventral", cell_b),
     C("Calme, ouvert, présent"),
     C("Respiration 4-6, chant, contact lent, eau froide visage")],
    [C("Sympathique utile", cell_b),
     C("Mobilisé, vigilant"),
     C("Sport intense, douche froide — pour SORTIR du figement")],
    [C("Vagal dorsal", cell_b),
     C("Vide, dissociation"),
     C("Mouvement physique léger d'abord, puis vagal ventral")],
], [3*cm, 4*cm, 9*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Cartographie quotidienne.</b> Pendant 7 jours, à 8h, 12h, 16h, 20h : note l'état (V / S / D). Sur 7 jours "
    "tu vois ton baseline réel — probablement S 70% du temps. C'est ton diagnostic.",
    "<b>Retour au vagal ventral.</b> 5 fois par jour, 2 min de respiration 4-6 (4s inspi, 6s expi). Tu installes "
    "un point d'ancrage. À force, ton SN sait où retrouver ce calme."
]))
story.extend(phrase_ancre(
    "« Trois états. Je sais lequel je suis. Je sais comment remonter au calme. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "L'hypervigilance silencieuse", ACCENT))
story.extend(retenir(
    "L'hypervigilance est l'état où ton SN scanne en permanence l'environnement pour détecter une menace. "
    "C'est épuisant et c'est souvent invisible — tu crois que c'est ta façon normale d'être. Le trauma installe "
    "cette hypervigilance comme état permanent."
))
story.extend(explication([
    "<b>Le mécanisme.</b> L'amygdale (centre de la peur) reste sur-activée après un trauma. Elle interprète des "
    "stimuli ordinaires comme potentiellement menaçants. Conséquences : sursauts faciles, sommeil dégradé, "
    "fatigue chronique, irritabilité au bruit, hyper-attention au visage des autres, agitation diffuse, "
    "difficulté à rester immobile. Le SN se comporte comme un soldat en zone de combat — même dans ton salon."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Signaux probables : réveils sans raison, fatigué. Sursauts faciles. Mal à rester immobile. Épaules ou "
    "mâchoire serrées. Ventre tendu. En trading : tu n'arrives pas à vraiment fermer la plateforme et oublier "
    "le trade en cours. Cette vigilance perpétuelle te coûte énormément d'énergie et nourrit le besoin de "
    "décharge intense."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> tu places le trade. Tu sais que ton SN va vouloir vérifier. Tu décides à l'avance : "
    "téléphone dans une autre pièce, plateforme fermée. Tu vas faire pansage 30 min, mouvement qui occupe le "
    "SN. Quand tu reviens, c'est terminé. Tu n'as pas alimenté l'hypervigilance par micro-checks."
]))

story.extend(exercice([
    "<b>Scan des tensions.</b> 3 fois par jour, 1 min : épaules, mâchoire, ventre, front. Sont-ils tendus ? Tu "
    "relâches consciemment. C'est un acte de signal pour ton SN : « la menace est partie ».",
    "<b>Routine de coucher.</b> 30 min avant dormir : lumière baissée, aucun écran, respiration 4-6 pendant "
    "10 min, lecture papier. Tu indiques à ton SN que la journée est terminée."
]))
story.extend(phrase_ancre(
    "« Mon SN scanne en permanence. Je lui apprends, dose après dose, qu'il peut se reposer. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "L'interoception altérée", ACCENT))
story.extend(retenir(
    "L'interoception est ta capacité à percevoir et interpréter les signaux internes du corps : faim, fatigue, "
    "tension, joie, anxiété. Le trauma altère cette capacité. Tu confonds des signaux. Tu n'entends plus tes "
    "besoins. Tu agis à l'aveugle physiologiquement."
))
story.extend(explication([
    "<b>Le mécanisme.</b> L'insula (zone cérébrale de l'interoception) est régulièrement perturbée chez les "
    "traumatisés. Tu peux confondre faim et anxiété, fatigue et ennui, tension corporelle et besoin de pic, "
    "signal de stop et signal de continuer. Ton système informatif interne est déréglé."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Pour toi en trade : (1) Tu ressens « ça doit marcher » dans ta poitrine. Tu crois que c'est de l'intuition. "
    "C'est en fait de la mobilisation sympathique liée à l'attente. (2) Tu ressens un creux après une session "
    "calme. Tu crois que c'est de l'ennui qui appelle un trade. C'est en fait une fatigue mentale qui appelle "
    "du repos."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Sensation", cell_g), C("Interprétation par défaut", cell_g), C("Interprétation correcte", cell_g)],
    [C("Chaleur poitrine"), C("« Je sens un mouvement »"), C("Activation sympathique")],
    [C("Agitation 14h"), C("« Il va y avoir une opportunité »"), C("Fatigue mentale, tolérance calme")],
    [C("Excitation pré-trade"), C("« Bon feeling »"), C("Anticipation dopaminergique")],
    [C("Vide post-pic"), C("« Faut trader pour le combler »"), C("Creux compensatoire normal")],
    [C("Tension ventre"), C("« Quelque chose va bouger »"), C("Stress chronique")],
], [4*cm, 5.5*cm, 6.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Journal interoceptif.</b> 3 fois par jour, 2 min : qu'est-ce que je ressens dans mon corps maintenant ? "
    "(faim, soif, tension, fatigue, calme, agitation). Tu écris. Tu réapprends à percevoir.",
    "<b>Test du décodage pré-trade.</b> Avant chaque trade : qu'est-ce que je ressens corporellement ? Signal "
    "de marché ou signal interne déconnecté ? Si interne (agitation, désir de pic, FOMO), tu ne cliques pas."
]))
story.extend(phrase_ancre(
    "« Mes sensations corporelles ne disent pas toujours ce que je crois. J'apprends à les lire. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Les chevaux comme co-régulateurs", ACCENT))
story.extend(retenir(
    "Tu as un atout rare : tes chevaux. La présence rapprochée d'un cheval régule directement ton SN. Ta filly "
    "est une thérapeute non diplômée. Si tu fais ton pansage tranquille en conscience, tu fais une vraie "
    "séance de régulation vagale."
))
story.extend(explication([
    "<b>La co-régulation.</b> Mécanisme par lequel deux systèmes nerveux en proximité ajustent mutuellement leurs "
    "états. Les chevaux sont particulièrement efficaces : cœur de grande taille avec une fréquence basse "
    "(~25-40 bpm au repos), SN très lisible pour l'humain, présence non-jugeante qui désactive l'amygdale "
    "humaine. Effet mesurable : variabilité cardiaque humaine qui augmente, cortisol qui baisse, vagal ventral "
    "qui s'active."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fais probablement de l'équitation comme PERFORMANCE (saut d'obstacles compétitif). C'est bien mais "
    "ce n'est pas thérapeutique en soi — la compétition active ton sympathique. Le PANSAGE, en revanche, "
    "est l'outil thérapeutique majeur. Si tu le fais sans téléphone, sans penser au trading, en présence totale, "
    "tu installes activement le vagal ventral. C'est un médicament gratuit que tu utilises probablement à 10% "
    "de son potentiel."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Activité", cell_g), C("Effet SN", cell_g), C("Quand l'utiliser", cell_g)],
    [C("Compétition obstacle"), C("Sympathique fort"), C("Décharge d'intensité saine")],
    [C("Pansage conscient"), C("Vagal ventral fort"), C("Régulation thérapeutique")],
    [C("Marche en main lente"), C("Vagal ventral"), C("Co-régulation profonde")],
    [C("Présence en pré"), C("Vagal ventral"), C("Méditation incarnée")],
], [4*cm, 4.5*cm, 7.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Pansage conscient hebdomadaire.</b> 1 fois/semaine minimum, 30-45 min : pansage à ta filly en présence "
    "totale. Pas de téléphone. Pas de pensée trading. Tu sens tes mains, son souffle, sa chaleur. Tu coordonnes "
    "ta respiration à la sienne. C'est de la thérapie somatique gratuite."
]))
story.extend(phrase_ancre(
    "« Ma filly est ma thérapeute. Je l'utilise comme telle, pas seulement comme partenaire de performance. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Le besoin d'un praticien somatique", ACCENT))
story.extend(retenir(
    "Pour ton cas spécifique (TBI 2022 sévère), tu ne peux pas faire tout le travail seul. Tu as besoin d'un "
    "praticien formé qui peut accompagner la décharge somatique. Sans accompagnement, certaines libérations "
    "peuvent être déstabilisantes ou superficielles. C'est un investissement non négociable."
))
story.extend(explication([
    "<b>Les approches documentées.</b> Somatic Experiencing (Peter Levine), EMDR, Sensorimotor Psychotherapy, "
    "TRE. Toutes partagent un principe : passer par le corps en présence d'un praticien qui sait doser, "
    "contenir, accompagner. La parole seule (psychothérapie classique) ne suffit pas pour des traumas "
    "corporels. Le corps doit être inclus."
]))

story.extend(application([
    "Coût typique : 70-120€ la séance. Au rythme d'1 séance par 2-3 semaines, ça représente ~250-400€/mois. "
    "À l'échelle de tes pertes prop firm récentes, c'est peu. À l'échelle de la transformation potentielle, "
    "c'est l'investissement le plus rentable possible."
]))

story.append(P("Les approches à considérer", h_sub))
story.append(styled_table([
    [C("Approche", cell_g), C("Principe", cell_g), C("Pour toi", cell_g)],
    [C("Somatic Experiencing"), C("Décharge progressive énergie figée"), C("Très pertinent — TBI typique")],
    [C("EMDR"), C("Mouvements oculaires bilatéraux"), C("Pertinent, orienté souvenirs")],
    [C("TRE"), C("Tremblements thérapeutiques"), C("Bon complément")],
    [C("Bilan neuropsychologique"), C("Évaluer séquelles cognitives"), C("À faire si pas encore fait")],
], [4.5*cm, 5.5*cm, 6*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Cette semaine — action concrète.</b> 30 min de recherche en ligne. Annuaire Somatic Experiencing France "
    "ou EMDR France. Note 3 praticiens dans ta région. Contacte 1 pour un premier rendez-vous. C'est ton action "
    "non négociable de la semaine."
]))
story.extend(phrase_ancre(
    "« Pour mon TBI, je ne suis pas obligé de tout porter seul. Je m'accompagne. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "Le sommeil — consolidation et réparation post-trauma", ACCENT))
story.extend(retenir(
    "Le sommeil n'est pas du repos passif. C'est le moment où ton cerveau CONSOLIDE les apprentissages, "
    "PROCESSE les émotions, ÉLIMINE les déchets neuronaux. Après un trauma comme le tien, le sommeil de "
    "qualité est probablement ton outil de réparation le plus puissant — et le plus négligé."
))
story.extend(explication([
    "<b>Sommeil paradoxal et processing émotionnel.</b> Pendant le REM (sommeil paradoxal, riche en rêves), "
    "ton cerveau traite les expériences émotionnelles intenses. Il les « désactive » émotionnellement tout en "
    "gardant l'info. Sans REM suffisant, les émotions s'accumulent à l'état brut — pour quelqu'un avec ton "
    "historique, c'est particulièrement coûteux.",
    "<b>Système glymphatique.</b> Pendant le sommeil profond, ton cerveau s'auto-nettoie via le système "
    "glymphatique — il évacue les déchets métaboliques (dont les protéines liées à la neurodégénérescence). "
    "Après un TBI, ce nettoyage est encore plus crucial. Manquer de sommeil = ralentir ta réparation neuronale."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Ton TBI demande plus de sommeil que la moyenne. 8-9h en moyenne. Si tu dors 6h en pensant que c'est OK, tu "
    "rates non seulement de la performance — tu rates de la réparation. Ce que tu compromets le soir, ton "
    "trading le paye le lendemain. Et ta reconstruction neuronale globale paie sur des années."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Heures de sommeil", cell_g), C("Effet le lendemain", cell_g)],
    [C("8-9h qualité"), C("Réparation optimale. Décisions claires.")],
    [C("7h"), C("Acceptable. Léger déficit.")],
    [C("6h"), C("Déficit cognitif équivalent à 0,3g d'alcool. Décisions dégradées.")],
    [C("≤ 5h"), C("Équivalent à 0,8g d'alcool. NE PAS TRADER.")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> coucher 22h30-23h max. Levé naturel sans réveil si possible. Avant 22h : pas d'écran, pas "
    "de café, lumière baissée. Si tu dors moins de 6h une nuit : INTERDIT de trader le lendemain. Tu fais "
    "autre chose — pansage, lecture, sport doux."
]))

story.extend(exercice([
    "<b>Routine de coucher en 4 étapes.</b> (1) Couper écrans 60 min avant coucher. (2) Douche tiède ou bain. "
    "(3) Lecture papier 20-30 min. (4) Respiration cohérente 5 min dans le lit. Reproduits chaque soir 30 jours.",
    "<b>Si tu mets > 30 min à dormir.</b> Tu te lèves. Tu vas dans une autre pièce. Lecture papier seule, "
    "lumière faible. Tu retournes te coucher quand tu sens venir le sommeil. Pas avant."
]))
story.extend(phrase_ancre(
    "« Le sommeil n'est pas optionnel. C'est la condition de ma réparation et de mon trading. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "La dissociation — quand tu te déconnectes de toi-même", ACCENT))
story.extend(retenir(
    "La dissociation est un mécanisme de protection : face à un stress trop intense, ton SN te « déconnecte » "
    "de la sensation, des émotions, parfois de la réalité présente. C'est utile en situation de danger. C'est "
    "destructeur quand ça devient un mode par défaut."
))
story.extend(explication([
    "<b>Les signaux.</b> Pendant un trade qui tourne mal : tu sens un détachement étrange, comme si tu regardais "
    "quelqu'un d'autre cliquer. Tu agis sans vraiment être là. Tu te dis après « je ne sais même pas pourquoi "
    "j'ai fait ça ». Ce n'est pas du déni — c'est de la dissociation. Ton SN t'a déconnecté pour te protéger.",
    "<b>Le coût.</b> Pendant la dissociation, tu ne peux pas appliquer le protocole. Tu n'es pas là pour "
    "l'appliquer. Tu reviens après l'événement. Tu constates les dégâts. Tu te flagelles. Mais la décision "
    "était déjà prise dans un état où tu n'avais pas accès à tes ressources."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Après ton TBI 2022, la dissociation peut être plus facilement déclenchée — ton SN a appris cette "
    "stratégie en survie. Pendant un crash de compte, tu peux te retrouver à cliquer sans être pleinement là. "
    "Reconnaître ce moment est crucial : c'est précisément à ce moment qu'il faut FERMER LA PLATEFORME, pas "
    "essayer de raisonner avec toi-même."
], GOLD, NAVY, accent=NAVY))

story.append(P("Reconnaître la dissociation — signaux précoces", h_sub))
story.append(styled_table([
    [C("Signal", cell_g), C("Description", cell_g)],
    [C("Sensation de flottement"), C("« Je ne suis pas vraiment là »")],
    [C("Voix qui vient de loin"), C("Tes propres pensées te paraissent étrangères")],
    [C("Mains qui agissent seules"), C("Tu cliques sans avoir décidé consciemment")],
    [C("Anesthésie émotionnelle"), C("Tu ne ressens rien — alors que tu devrais")],
    [C("Temps qui s'étire"), C("Tu perds la notion du temps écoulé")],
    [C("Vision rétrécie"), C("Tunnel visuel sur l'écran")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> à la première reconnaissance d'UN de ces signaux, action mécanique : FERMER LA PLATEFORME. "
    "Pas négocier. Pas analyser. Fermer. Puis 5 minutes de pleine présence corporelle (5-4-3-2-1) pour te "
    "ramener dans le corps."
]))

story.extend(exercice([
    "<b>Test du « suis-je là ? ».</b> Pendant tes sessions, 3 fois minimum : tu te demandes à voix basse "
    "« suis-je là ? ». Si la réponse honnête est non ou « pas vraiment » → tu fermes la session. Tu pratiques "
    "la reconnaissance.",
    "<b>Ancres corporelles.</b> Garde près de toi 3 objets sensoriels : pierre froide (toucher), bougie "
    "(odeur), eau fraîche (boire). Si tu sens la dissociation venir, tu actives une ancre. Le sensoriel "
    "ramène dans le corps."
]))
story.extend(phrase_ancre(
    "« Si je ne suis pas là, je ne décide pas. Je ferme et je reviens d'abord à moi. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 3 ---
story.append(P("Carte mentale — Partie 3", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Trauma et SN",
    [
        {"label": "MÉCANIQUES", "leaves": ["empreinte vivante", "3 états SN", "hypervigilance"], "color": NAVY},
        {"label": "CHEZ TOI", "leaves": ["TBI 2022", "interoception altérée", "calme intolérable"], "color": ACCENT},
        {"label": "RÉPARATION", "leaves": ["praticien SE/EMDR", "pansage conscient", "respiration 4-6"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Reconnaître → Réguler → Travailler avec un professionnel.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 3", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  TRAUMA ET SN — FICHE D'ANCRAGE                           ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Mon TBI 2022 pilote encore mes décisions actuelles      ║
║    via mon SN dérégulé. Je ne le vois pas, il agit.        ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Tension chronique nuque/mâchoire/ventre               ║
║    - Intolérance au calme («le calme me semble vide»)      ║
║    - Sommeil interrompu sans raison                        ║
║    - Hypervigilance discrète (check compulsif)             ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Nommer l'état SN (V / S / D)                         ║
║    2. Si S ou D : régulation AVANT toute décision          ║
║    3. Reconnaître que c'est mon SN, pas Marien             ║
║                                                            ║
║  RÈGLE DE TRADING                                          ║
║    Pas de trade en sympathique élevé.                      ║
║    Check SN obligatoire avant chaque session.              ║
║    Pansage conscient hebdomadaire NON négociable.          ║
║    Praticien somatique 1x / 2-3 semaines.                  ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Je soigne par le corps.                               ║
║      C'est là que mon trauma est stocké. »                 ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


print("✓ Parties 2 et 3 écrites")


# ============================================================
# PARTIE 4 — DÉCHARGER LE STRESS BLOQUÉ DANS LE CORPS
# ============================================================
_part_color[0] = PART_COLORS[3]
_part_num[0] = 4
_part_name[0] = "Décharger le stress"
ACCENT = PART_COLORS[3]

story.extend(part_separator(4, "Décharger le stress", "bloqué dans le corps", ACCENT))

story.extend(part_intro_header(4, "Décharger le stress bloqué dans le corps",
    "Le protocole somatique pour libérer l'énergie figée depuis 2022", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "La Partie 3 a posé le diagnostic : ton SN porte l'empreinte de 2022. Cette partie est le <b>traitement</b>. "
    "Le diagnostic seul ne soigne pas. Comprendre que ton corps porte une énergie figée ne suffit pas — il "
    "faut la décharger. Cette partie te donne les outils corporels concrets, applicables seul ou avec un "
    "praticien."
))
story.append(P(
    "Une observation centrale issue de la recherche sur le trauma : les animaux sauvages se libèrent du trauma "
    "naturellement par tremblements, secouements, mouvements involontaires après une menace. Les humains "
    "inhibent ces réflexes (par éducation, anesthésie, immobilisation). L'énergie reste figée. Le travail "
    "somatique consiste à réactiver ces décharges dans un cadre sécurisé."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "L'énergie figée — pourquoi ton corps ne s'est pas vidé", ACCENT))
story.extend(retenir(
    "Une menace vitale active une énergie de survie massive (adrénaline, cortisol, mobilisation musculaire). "
    "Cette énergie doit ensuite être déchargée. Si elle ne peut pas l'être (immobilisation, coma, anesthésie), "
    "elle reste piégée dans le corps. Pour des années."
))
story.extend(explication([
    "<b>Le modèle animal.</b> Les animaux sauvages survivent à des centaines de menaces vitales sans développer "
    "de trauma chronique. Pourquoi ? Parce qu'après la menace, ils déchargent automatiquement par tremblements, "
    "secouements, respirations amples. Tu peux le voir chez un chien après une grosse frayeur — il se secoue "
    "violemment pendant 30-60 secondes puis revient au calme. Trauma intégré, pas figé.",
    "<b>Pourquoi les humains figent.</b> Trois raisons : (1) inhibition sociale (on apprend à ne pas trembler, "
    "pleurer, crier), (2) immobilisation médicale (anesthésie, plâtres, alitement), (3) traumatismes prolongés "
    "où il n'y a jamais de « après ». Ton cas combine les trois."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Septembre 2022 : accident → coma → anesthésie générale (inhibe toute décharge) → opérations multiples "
    "(autres anesthésies) → immobilisation longue. L'énergie de survie de l'accident n'a JAMAIS pu se "
    "décharger. Trois ans plus tard, elle est encore là. C'est ce qui produit ta sensation de pression sourde, "
    "ton agitation diffuse, ton besoin de décharge intense."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(7*cm, lambda c, w, h: draw_flow(c, w, h,
    ["Accident 2022", "Mobilisation totale du SN",
     "COMA + Anesthésie (bloque décharge)", "Énergie FIGÉE dans le corps",
     "3 ans après — pression sourde, agitation, besoin de pic"],
    accent=ACCENT, color_first=ACCENT, color_last=RED_ACC)))
story.append(P("Le cycle interrompu de 2022 — qui continue d'agir aujourd'hui.", caption))

story.extend(application([
    "<b>Saboteur :</b> tu trades en sentant en permanence une pression diffuse dans la poitrine, les épaules. "
    "Tu ne fais pas le lien. Tu prends des trades pour décharger cette pression — l'action de cliquer fait "
    "baisser la pression 30 secondes. Tu transformes une décharge somatique en trade.",
    "<b>Cible :</b> tu reconnais la pression comme énergie figée 2022. Tu ne la décharges pas par le trading. "
    "Tu la décharges par du mouvement structuré : box, course, danse, écriture à la main, ou idéalement "
    "séance SE avec praticien. La pression baisse durablement."
]))

story.extend(exercice([
    "<b>Reconnaissance corporelle.</b> 3 fois par jour, 2 min : où dans ton corps tu sens une pression, une "
    "tension, une vibration ? Note dans ton journal. Sur 7 jours, tu vas cartographier les zones où l'énergie "
    "est stockée (probablement nuque, mâchoire, ventre, poitrine, jambes)."
]))
story.extend(phrase_ancre(
    "« Mon corps a une décharge à faire depuis 2022. Je lui donne le cadre pour la faire. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "La sensation ressentie (felt sense)", ACCENT))
story.extend(retenir(
    "La sensation ressentie est ta capacité à percevoir ton corps de l'INTÉRIEUR — pas en pensée, en sensation. "
    "Sans cette capacité, aucun travail somatique n'est possible. Pour la plupart des traumatisés, elle est "
    "très atrophiée. La restaurer est le PREMIER travail."
))
story.extend(explication([
    "<b>Le principe.</b> Quand tu te demandes « comment je vais ? », tu réponds normalement par un mot (« bien », "
    "« fatigué »). C'est une réponse cognitive. La sensation ressentie c'est différent : tu fermes les yeux, "
    "tu diriges ton attention DANS ton corps, et tu remarques des sensations subtiles — une chaleur dans la "
    "poitrine, une tension dans la nuque, un creux dans le ventre, un picotement dans les mains. Ces sensations "
    "précèdent les mots. Elles sont la voix de ton corps avant traduction mentale."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu vis beaucoup en tête. Le trading t'a renforcé dans cette habitude — analyser, prédire, calculer. Tu as "
    "développé une compétence verticale (mentale) au prix de ta compétence horizontale (corporelle). C'est "
    "pour ça que tu te fais surprendre par tes états : tu ne sens pas venir, tu te retrouves d'un coup à cliquer "
    "sans avoir vu l'élan monter. Si tu restaurais ta sensation ressentie, tu remarquerais l'élan au stade 2 "
    "sur 10, pas au stade 9 sur 10."
], GOLD, NAVY, accent=NAVY))

story.append(P("Le vocabulaire de la sensation ressentie", h_sub))
story.append(styled_table([
    [C("Catégorie", cell_g), C("Exemples de descripteurs", cell_g)],
    [C("Température"), C("chaud, brûlant, frais, glacé, tiède")],
    [C("Texture / qualité"), C("dense, fluide, granuleux, lisse, vide, plein, vibrant, immobile")],
    [C("Mouvement"), C("monte, descend, irradie, palpite, pousse, tire, s'étend, se contracte")],
    [C("Localisation"), C("poitrine, ventre, gorge, épaules, mâchoire, nuque, bassin, jambes, mains")],
    [C("Intensité (1-10)"), C("noter sur 10 — permet de mesurer la pendulation")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Scan corporel quotidien.</b> Matin et soir, 5 min, allongé. Tu balaies de la tête aux pieds. À chaque "
    "zone, tu cherches une sensation. Tu décris avec le vocabulaire du tableau. Tu ne corriges rien. Tu observes.",
    "<b>Sensation au cheval.</b> Pendant le pansage, 5 min de présence totale au contact. Qu'est-ce que tu "
    "ressens dans TES mains ? Dans TON ventre ? Le cheval est ton coach somatique gratuit.",
    "<b>Stop sensations pré-trade.</b> Avant CHAQUE clic, 30 sec : qu'est-ce que je ressens dans mon corps ? "
    "Si dominant : agitation, désir, précipitation → tu ne cliques pas. Tu attends que la sensation soit du "
    "calme stable."
]))
story.extend(phrase_ancre(
    "« Mon corps parle avant ma tête. J'apprends à écouter le corps en premier. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "La pendulation — osciller au lieu de plonger", ACCENT))
story.extend(retenir(
    "La pendulation est le mouvement naturel du SN entre activation et calme. Dans un SN sain, cette oscillation "
    "se fait fluidement. Dans un SN traumatisé, elle est bloquée. Le travail consiste à restaurer la pendulation "
    "en DOUCEUR, par doses, sans jamais forcer."
))
story.extend(explication([
    "<b>Le principe.</b> Quand tu touches une sensation corporelle inconfortable (tension, peur, vide), la "
    "tendance est de soit PLONGER dedans (s'y noyer), soit FUIR (changer de sujet). Les deux sont contre-productifs. "
    "La pendulation consiste à : (1) toucher BRIÈVEMENT la sensation inconfortable, (2) revenir vers une "
    "RESSOURCE (sensation agréable, image apaisante), (3) revenir au matériel inconfortable plus brièvement, "
    "(4) revenir à la ressource. À force, tu enseignes à ton SN qu'il peut traverser l'inconfort et revenir."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fonctionnes typiquement par plongée puis fuite. Tu plonges dans le trade — toute ton énergie, ta "
    "tension, ton désir. Quand ça crashe, tu fuis (Netflix, alcool, écran, isolement). Pas d'oscillation "
    "contrôlée. Soit tout, soit rien. Ton SN ne sait plus pendulator."
], GOLD, NAVY, accent=NAVY))

story.extend(ascii_box("""
PROTOCOLE PENDULATION — 6 étapes
─────────────────────────────────

1. RESSOURCE        →  Identifie une sensation agréable disponible
                       (chaleur ventre, image de ta filly, contact d'un
                       être aimé). Tu la ressens 30 sec - 1 min.

2. MATÉRIEL DIFFICILE → Tu touches BRIÈVEMENT (5-10 sec max) la sensation
                       inconfortable. Tu remarques. Tu ne plonges pas.

3. RETOUR RESSOURCE → Tu reviens à ta sensation agréable. 30 sec - 1 min.

4. MATÉRIEL DIFFICILE → Tu touches à nouveau, plus brièvement. 3-5 sec.

5. RESSOURCE        →  Retour.

6. ITÉRATIONS       →  Tu continues 6-10 cycles.

Effet : le SN apprend que l'inconfort est traversable.
        L'énergie figée se libère par micro-doses.
        Tu ne retraumatises jamais.
""", accent=ACCENT))

story.extend(application([
    "<b>Cible (après un crash) :</b> tu identifies une ressource (image de ta filly broutant calme). Tu touches "
    "5 sec la honte (« j'ai cramé »). Tu reviens 30 sec à la filly. Tu touches 5 sec la colère envers toi-même. "
    "Retour. Tu fais 8 cycles. Au bout, l'émotion est traversée — pas refoulée, pas explosée."
]))

story.extend(exercice([
    "<b>Pendulation quotidienne.</b> 1 fois/jour, 5 min : tu choisis une petite gêne corporelle (tension nuque, "
    "agitation, malaise vague). Tu fais le protocole 1-2-3-4-5-6. C'est ton entraînement.",
    "<b>Identification de ressources stables.</b> Liste 5 ressources somatiques disponibles 24h/24 : image, "
    "sensation, lieu, personne, son. Ces 5 sont tes points d'ancrage pour toute pendulation."
]))
story.extend(phrase_ancre(
    "« J'oscille, je ne plonge pas. Toucher 5 secondes. Revenir 30. C'est la voie. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "La titration — doses minuscules toujours", ACCENT))
story.extend(retenir(
    "La titration est un terme de chimie : ajouter une substance goutte par goutte pour ne pas faire exploser "
    "la réaction. Appliqué au trauma : tu n'affrontes JAMAIS le matériel traumatique frontalement. Tu y vas "
    "par gouttes. Toujours."
))
story.extend(explication([
    "<b>Le principe.</b> Si tu plonges dans le matériel traumatique entier, ton SN se retrouve à nouveau dans "
    "l'état originel — tu RETRAUMATISES. C'est pour ça que beaucoup de thérapies par exposition forte échouent "
    "ou aggravent. La titration force la digestion graduelle. Une goutte. Tu intègres. Une autre goutte. Tu "
    "intègres. Le système digère sans déborder."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Pour ton TBI 2022, ne PAS essayer de « repenser à l'accident » en bloc, ni « revivre le coma » mentalement. "
    "Ça t'épuiserait ou retraumatiserait. Plutôt : un thérapeute SE te ferait travailler par micro-bouts. Une "
    "sensation. Un détail périphérique. Une petite tension. Tu intègres chacun. À force, le tout est digéré."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Saboteur :</b> tu cramés un compte. Tu décides « ce soir je vais ENFIN comprendre ce qui m'arrive ». "
    "Tu t'enfermes 3h à ressasser. Tu finis épuisé, parfois submergé. Tu as retraumatisé.",
    "<b>Cible :</b> tu cramés. Tu te donnes 15 min pour écrire. Pas plus. Tu décris UNE scène : « à 14h32, "
    "juste avant de décaler le SL, j'ai ressenti dans la poitrine... ». Tu explores ce SEUL moment. Tu arrêtes. "
    "Pendulation. Tu fais autre chose. Le lendemain, autre moment, 15 min."
]))

story.extend(exercice([
    "<b>Règle des 15 minutes.</b> Aucune session d'introspection ne dépasse 15 min consécutives. Au-delà, tu sors, "
    "tu fais autre chose. Le SN ne tolère pas l'introspection longue après trauma.",
    "<b>Journal en gouttes.</b> Quand tu écris sur un événement difficile : 3-5 phrases par session. Tu reprends "
    "le lendemain, autres 3-5 phrases. À force, tu construis sans accabler.",
    "<b>Rythme thérapeutique.</b> Avec un praticien SE, le rythme typique est 1 séance par 2-3 semaines. PAS "
    "plus. Le temps entre séances est aussi important que les séances — c'est le temps d'intégration."
]))
story.extend(phrase_ancre(
    "« Goutte par goutte. Jamais le grand débordement. Mon SN intègre à son rythme. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Les mouvements inachevés — laisser le corps les compléter", ACCENT))
story.extend(retenir(
    "Chaque trauma laisse dans le corps un mouvement bloqué — une action qui aurait dû se faire et qui n'a pas "
    "pu (fuir, se protéger, repousser, crier). Permettre à ce mouvement de se compléter dans un cadre sécurisé "
    "libère l'énergie associée. Pas mentalement — corporellement."
))
story.extend(explication([
    "<b>Le principe.</b> Le SN garde la mémoire des actions INACHEVÉES. Si tu allais courir mais qu'on t'a "
    "immobilisé, tes muscles des jambes gardent l'impulsion de course en attente. Cette impulsion produit une "
    "légère contraction permanente, une vigilance musculaire chronique, une fatigue diffuse. Le travail "
    "somatique permet de réveiller ces impulsions, doucement, et de les laisser s'ACHEVER par micro-mouvements "
    "consciemment habités."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "En 2022, les mouvements inachevés sont nombreux : ton corps a voulu se protéger les mains, tourner la tête, "
    "freiner avec les jambes, crier. Aucun n'a pu se faire correctement. Pendant le coma, ton corps a peut-être "
    "voulu bouger, dire quelque chose — anesthésie a tout bloqué. Pendant les opérations, idem. Tous ces "
    "mouvements sont en ATTENTE dans ton corps."
], GOLD, NAVY, accent=NAVY))

story.append(P("Les micro-mouvements à explorer (en solo, doucement)", h_sub))
story.append(styled_table([
    [C("Mouvement", cell_g), C("Quand l'utiliser", cell_g)],
    [C("Push (mains poussent un mur)"),
     C("Quand tu sens pression / colère figée. Le geste de repousser une menace.")],
    [C("Pull (tirer une corde imaginée)"),
     C("Quand tu sens déconnexion / vide. Le geste de ramener.")],
    [C("Reach (tendre les bras loin)"),
     C("Quand tu sens un manque de lien / désir refoulé. Le geste de chercher.")],
    [C("Run (courir sur place lentement)"),
     C("Quand tu sens agitation figée dans les jambes. Le geste de fuir.")],
    [C("Voice (crier dans l'oreiller)"),
     C("Quand tu sens blocage à la gorge / poitrine. Le geste de protester.")],
], [5*cm, 11*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Box conscient.</b> Tu fais déjà de la box. Fais-en aussi DE LA THÉRAPIE SOMATIQUE. Choisis 2 minutes "
    "par séance où tu frappes avec INTENTION corporelle complète — pas pour la perf, pour la décharge. Tu "
    "sentiras ton corps libérer."
]))

story.extend(exercice([
    "<b>Exploration douce hebdomadaire.</b> 1 fois/semaine, 15 min, en privé. Choisis UN micro-mouvement du "
    "tableau. Fais-le LENTEMENT, avec conscience corporelle complète. Si tremblements ou émotions montent : "
    "laisse, sans forcer. Reviens à la respiration calme à la fin.",
    "<b>Travail avec praticien.</b> Pour ton TBI, ce module est trop important pour le faire seul. Cherche "
    "cette semaine un praticien SE ou TRE certifié."
]))
story.extend(phrase_ancre(
    "« Mon corps a des mouvements en attente depuis 2022. Je leur donne le cadre pour s'achever. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "La respiration polyvagale — outil de poche", ACCENT))
story.extend(retenir(
    "La respiration est le SEUL accès conscient et direct à ton système nerveux autonome. Aucune autre fonction "
    "n'est à la fois automatique ET modifiable volontairement. C'est ton outil de régulation portable, "
    "gratuit, disponible 24h/24."
))
story.extend(explication([
    "<b>Pourquoi ça marche.</b> L'expiration LONGUE active le nerf vague ventral (calme, parasympathique). "
    "L'inspiration courte active légèrement le sympathique. Donc une respiration où expi > inspi calme le SN. "
    "Inversement, hyper-inspiration ample = activation. Tu pilotes ton état neurochimique par le souffle.",
    "<b>Les ratios utiles.</b> 4-6 (4s inspi, 6s expi) = apaisement. 5-5 (cohérence cardiaque) = équilibre. "
    "4-7-8 (4 inspi, 7 retenue, 8 expi) = endormissement et anti-stress aigu. Box breathing 4-4-4-4 = concentration."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu pratiques déjà Dispenza. Pas besoin de te convertir. Ajoute juste ces ratios précis en outils ciblés. "
    "Avant chaque session de trading : 4-6 pendant 5 min. Pendant un trade tendu : 4-7-8 pendant 3 cycles. "
    "Le soir : 4-7-8 pendant 5 cycles dans le lit. Tu auras un outil par situation."
], GOLD, NAVY, accent=NAVY))

story.append(P("Les 4 ratios principaux", h_sub))
story.append(styled_table([
    [C("Ratio", cell_g), C("Effet", cell_g), C("Quand l'utiliser", cell_g)],
    [C("4-6"), C("Apaisement progressif"), C("Avant session, entre trades")],
    [C("5-5 (cohérence cardiaque)"), C("Équilibre, focus"), C("Pendant analyse, méditation")],
    [C("4-7-8"), C("Anti-stress aigu, endormissement"), C("Pic émotionnel, coucher")],
    [C("Box 4-4-4-4"), C("Concentration militaire"), C("Décision technique précise")],
], [3.5*cm, 5*cm, 7.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Pratique quotidienne minimum.</b> 5 sessions/jour de respiration 4-6 (3-5 min chacune). Au réveil, "
    "avant repas, avant session trading, après session, avant coucher. Tu installes un point d'ancrage SN "
    "régulier.",
    "<b>Test du ratio.</b> Cette semaine, expérimente chaque ratio dans son contexte indiqué. Note 1-10 son "
    "effet. Tu identifies ton outil personnel le plus efficace."
]))
story.extend(phrase_ancre(
    "« Mon souffle est mon télécommande SN. Je l'utilise en conscience, pas par hasard. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "Les tremblements thérapeutiques (TRE)", ACCENT))
story.extend(retenir(
    "Les Tension & Trauma Releasing Exercises (TRE), développés par David Berceli, sont une méthode qui active "
    "VOLONTAIREMENT les tremblements neurogéniques — la décharge naturelle que ton corps n'a pas pu faire "
    "après 2022. C'est inconfortable au début. C'est puissant."
))
story.extend(explication([
    "<b>Le principe.</b> Le tremblement neurogénique est un réflexe naturel des mammifères pour décharger "
    "l'activation post-stress. Les humains l'inhibent socialement. TRE consiste à fatiguer modérément les "
    "muscles du psoas (zone du bassin, lien clé entre stress et corps) puis à les LAISSER trembler — sans "
    "résister, sans amplifier. Le tremblement s'auto-dose. Le corps libère ce qu'il peut, à son rythme.",
    "<b>Effets documentés.</b> Diminution de la tension de fond, amélioration du sommeil, réduction de "
    "l'hypervigilance, sensation de relâchement profond. Utilisé en zones de guerre, en post-trauma médical, "
    "en burnout sévère. Reconnu par plusieurs systèmes de santé publique."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Pour ton cas (TBI + énergie figée), TRE peut être un outil très puissant — mais à apprendre avec un "
    "praticien certifié pour les premières séances. Une fois la technique acquise, tu peux la pratiquer "
    "seul 2-3 fois par semaine. C'est complémentaire (pas substitut) à un travail SE avec praticien."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Combinaison puissante.</b> Box thérapeutique (décharge musculaire intense) + 10 min TRE après (laisser "
    "trembler) + 5 min respiration calme (intégration). Cycle complet de décharge somatique structurée. "
    "1-2 fois par semaine."
]))

story.extend(exercice([
    "<b>Découverte TRE.</b> Recherche un praticien TRE certifié en France. 3-5 séances pour apprendre la "
    "technique. Coût : 60-100€/séance. Investissement total ~300-500€. Tu acquiers un outil pour la vie.",
    "<b>Alternative douce.</b> Si pas accessible : exercices de mobilisation du psoas (postures de yoga "
    "thérapeutique) + relâchement conscient + observation des tremblements éventuels. Plus lent à installer "
    "mais accessible seul."
]))
story.extend(phrase_ancre(
    "« Mon corps sait trembler pour se libérer. Je lui rends ce droit. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "Le contact à la nature comme régulateur", ACCENT))
story.extend(retenir(
    "La nature n'est pas un agrément optionnel. C'est un régulateur du SN documenté. Marche en forêt, contact "
    "avec la terre, exposition à la lumière naturelle, présence d'eau : chacun produit un effet mesurable "
    "sur ton baseline. C'est gratuit et tu le sous-utilises."
))
story.extend(explication([
    "<b>Effets documentés.</b> Marche en forêt (shinrin-yoku, étudié au Japon) → baisse du cortisol, hausse "
    "des cellules NK immunitaires, baisse de la tension artérielle, sur 2h de marche. Contact direct avec la "
    "terre (pieds nus, sol naturel) → effet anti-inflammatoire mesurable. Exposition à la lumière naturelle "
    "matinale → régulation circadienne, mélatonine du soir.",
    "<b>Effet sur ton SN.</b> La nature désactive le réseau de mode par défaut (rumination/projection) plus "
    "efficacement que la plupart des environnements urbains. Ton cerveau bascule plus facilement en vagal "
    "ventral. C'est physiologique, pas symbolique."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as les chevaux et probablement l'accès à des espaces naturels. C'est un atout massif. Combinaison "
    "parfaite pour toi : 1 fois par semaine, marche longue (60-90 min) en forêt ou nature, sans téléphone, "
    "suivie d'1 heure avec ta filly. C'est de la thérapie SN gratuite, profonde, durable."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Pratique", cell_g), C("Durée", cell_g), C("Effet SN", cell_g)],
    [C("Marche forêt sans téléphone"), C("60-90 min"), C("Cortisol ↓, vagal ventral ↑")],
    [C("Pieds nus sur terre/herbe"), C("10-15 min"), C("Anti-inflammatoire, ancrage")],
    [C("Lumière naturelle matinale"), C("15-30 min"), C("Régulation circadienne")],
    [C("Eau (rivière, mer, lac)"), C("Présence"), C("Apaisement profond, ions négatifs")],
    [C("Présence animale"), C("30-60 min"), C("Co-régulation interspécifique")],
], [5*cm, 3*cm, 8*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Sortie nature hebdomadaire.</b> 1 fois par semaine minimum, 90 min de nature sans téléphone. Forêt, "
    "campagne, parc. Tu marches lentement. Tu observes. Tu respires. C'est non négociable.",
    "<b>Lumière matinale.</b> Chaque matin, 15-30 min de lumière naturelle dans les 60 min après réveil "
    "(idéalement sans lunettes solaires). Tu régules ton horloge interne. Sommeil meilleur le soir."
]))
story.extend(phrase_ancre(
    "« La nature régule mon SN gratuitement. Je l'utilise comme un médicament. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 4 ---
story.append(P("Carte mentale — Partie 4", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Décharger",
    [
        {"label": "PRINCIPES", "leaves": ["énergie figée", "modèle animal", "inhibition humaine"], "color": NAVY},
        {"label": "OUTILS", "leaves": ["sensation ressentie", "pendulation", "titration", "mouvements inachevés"], "color": ACCENT},
        {"label": "PRATIQUES", "leaves": ["scan corporel 5min", "box consciente", "praticien SE"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Restaurer la sensation → osciller → décharger progressivement.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 4", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  DÉCHARGER LE STRESS — FICHE D'ANCRAGE                    ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Décharger l'énergie 2022 par le trading                 ║
║    (artificiel, dégradant) au lieu du somatique            ║
║    structuré (réel, restaurateur).                         ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Pression sourde dans le corps sans cause              ║
║    - Tension chronique nuque/épaules/ventre                ║
║    - Besoin compulsif de cliquer                           ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Scan corporel 2 min — où est la pression ?           ║
║    2. Pendulation : 5s inconfort / 30s ressource           ║
║    3. Si charge forte : décharge structurée (box, course)  ║
║       puis retour au calme 10 min.                         ║
║                                                            ║
║  RÈGLE                                                     ║
║    Pas plus de 15 min d'introspection consécutive.         ║
║    Titration toujours. Goutte par goutte.                  ║
║    Praticien somatique 1x / 2-3 semaines.                  ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Goutte par goutte.                                    ║
║      Mon corps se libère à son rythme. »                   ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


# ============================================================
# PARTIE 5 — PENSER EN PROBABILITÉS COMME UN VRAI TRADER
# ============================================================
_part_color[0] = PART_COLORS[4]
_part_num[0] = 5
_part_name[0] = "Probabilités"
ACCENT = PART_COLORS[4]

story.extend(part_separator(5, "Penser en probabilités", "comme un vrai trader", ACCENT))

story.extend(part_intro_header(5, "Penser en probabilités comme un vrai trader",
    "Reconfigurer ta pensée binaire en pensée distributionnelle", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tu raisonnes en certitudes alors que le marché est fondamentalement probabiliste. Cette dissonance est "
    "la source de la majorité de tes comportements destructeurs. Quand tu te dis « ça VA marcher », tu charges "
    "le trade émotionnellement et tu rends toutes les décisions suivantes piégées."
))
story.append(P(
    "Cette partie reconfigure ta grammaire mentale. Tu vas passer du « ça va monter » au « 55% de chances que "
    "ça monte selon mon setup, sur ma série de 100 ». Ce changement de langage modifie le cerveau, pas juste "
    "la pensée. C'est l'un des leviers les plus puissants de la transformation."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "Le piège de la certitude", ACCENT))
story.extend(retenir(
    "Le trader rentable a fait la paix avec l'incertitude. Le trader perdant la combat encore. Tout se joue là. "
    "Le marché ne te donnera jamais de certitude — chercher plus de signaux ne la créera pas non plus."
))
story.extend(explication([
    "<b>Le mécanisme.</b> La nature du marché est statistique. Chaque trade individuel a un résultat probabiliste. "
    "Aucune analyse, même parfaite, ne peut transformer une probabilité en certitude. Quand tu cherches plus "
    "d'analyse, tu cherches à apaiser une anxiété (« et si je me trompais ? ») par un moyen qui ne peut pas "
    "marcher. C'est comme essayer d'éteindre un feu en y jetant de l'huile."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Quand tu galères, ton premier réflexe est d'apprendre encore. Un nouveau confluence, un nouveau timeframe, "
    "un nouveau mentor SMC. Tu cherches LA pièce manquante qui va te donner la certitude. Cette pièce n'existe "
    "pas. Plus tu la cherches, plus tu construis un système complexe qui aggrave ta rigidité mentale."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Saboteur :</b> 3 trades perdants en 2 jours. Tu te dis « il me manque un confirm de plus ». Tu passes "
    "ta soirée à étudier le delta volume. Tu rajoutes ce filtre. Tu perds quand même.",
    "<b>Cible :</b> 3 perdants. Tu reconnais : « 3 trades ne disent rien sur mon edge. Je joue 100. » Tu "
    "n'ajoutes RIEN. Le 4e trade : setup A+ comme tu sais le voir. Tu acceptes que le résultat ne sera connu "
    "que sur 100 occurrences."
]))

story.extend(exercice([
    "<b>Audit des sur-additions.</b> Liste tous les outils, filtres, confluences que tu utilises actuellement. "
    "Probablement 8-15 paramètres. Identifie les 3-5 essentiels. Les autres sont probablement des additions "
    "anxieuses. Tu peux en enlever sans dégrader ton edge.",
    "<b>Règle du minimum viable.</b> 4 semaines : aucune nouvelle source d'info. Aucun nouveau paramètre. Tu "
    "travailles avec exactement ce que tu as aujourd'hui. Tu observes ce qui se passe."
]))
story.extend(phrase_ancre(
    "« La certitude n'existe pas. Plus d'analyse ne la crée pas. J'arrête d'ajouter. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "Réécrire le câblage qui veut du oui / non", ACCENT))
story.extend(retenir(
    "Le cerveau humain est câblé pour la pensée BINAIRE — oui/non, sécurité/danger, bon/mauvais. Cette pensée "
    "a été utile dans la savane. Elle est désastreuse pour le trading. Penser en probabilités demande un "
    "entraînement actif."
))
story.extend(explication([
    "<b>Le principe.</b> Internaliser que chaque événement a une probabilité, pas une certitude. Un setup A+ "
    "XAUUSD en NY killzone n'est pas « ça va marcher ». C'est « ça a, disons, 58% de chances de marcher selon "
    "ma série historique ». Cette transformation grammaticale change tout : tu ne cherches plus à avoir raison, "
    "tu joues une probabilité. Le résultat individuel ne porte plus la charge identitaire."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fonctionnes encore en binaire. Quand tu prends un trade : « ce trade VA marcher ». Cette phrase EST "
    "l'origine de ton problème +1500. Si ça VA marcher, alors quand le marché te donne raison, tu veux encore "
    "plus de validation (tu pousses). Quand le marché te contredit, tu refuses (tu décales)."
], GOLD, NAVY, accent=NAVY))

story.append(P("Substitution grammaticale", h_sub))
story.append(styled_table([
    [C("Pensée binaire (à éviter)", cell_g), C("Pensée probabiliste (cible)", cell_g)],
    [C("« Ça va monter »"), C("« 55% de chances selon mon setup »")],
    [C("« J'ai raison »"), C("« Mon hypothèse a une probabilité plus haute »")],
    [C("« Ce trade doit marcher »"), C("« Ce trade est une instance de ma série »")],
    [C("« Je me suis trompé »"), C("« Ce trade est dans les 45% qui perdent normalement »")],
    [C("« Mon edge ne marche plus »"), C("« Sur 5 trades, je n'ai pas assez de données »")],
], [7.5*cm, 8.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Le journal probabiliste.</b> Pour chaque trade, écris la phrase : « Ce setup donne X% de gagnants "
    "historiquement avec RR Y:Z. Je joue ma série. » Si tu ne peux pas remplir cette phrase, tu ne dois pas "
    "prendre le trade.",
    "<b>Substitution grammaticale 30 jours.</b> Chaque fois que tu te surprends à dire « ça va », « ça doit », "
    "« j'ai raison » : tu reformules en probabilité. Le langage modifie la pensée."
]))
story.extend(phrase_ancre(
    "« Je ne dis plus 'ça va marcher'. Je dis 'ce setup a X% selon ma série'. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "Les 5 vérités axiomatiques", ACCENT))
story.extend(retenir(
    "Cinq vérités du trader rentable, à intégrer au niveau réflexe (pas intellectuel). Tant qu'elles sont "
    "seulement au niveau intellectuel, elles ne te protègent pas. Au niveau réflexe, elles deviennent ton armure."
))

story.append(styled_table([
    [C("#", cell_g), C("Vérité", cell_g), C("Conséquence pratique", cell_g)],
    [C("V1"), C("Tout peut arriver sur le marché.", cell_b),
     C("Aucun setup n'a 100%. Le SL est sacré.")],
    [C("V2"), C("Tu n'as pas besoin de savoir ce qui va arriver pour gagner.", cell_b),
     C("La prédiction n'est pas l'objectif. Le plan oui.")],
    [C("V3"), C("Distribution aléatoire des gagnants/perdants à l'intérieur d'un edge.", cell_b),
     C("3 pertes consécutives ne disent rien sur l'edge.")],
    [C("V4"), C("Un edge est juste une probabilité plus haute.", cell_b),
     C("55% n'est pas une certitude. C'est un edge.")],
    [C("V5"), C("Chaque instant du marché est unique.", cell_b),
     C("Le passé informe, ne détermine pas. Pas de revanche.")],
], [0.8*cm, 6.5*cm, 8.7*cm]))
story.append(Spacer(1, 10))

story.extend(explication([
    "<b>Pourquoi ces 5 sont contre-intuitives.</b> V1 contredit le besoin de prédiction. V2 contredit le besoin "
    "de contrôle. V3 contredit le pattern recognition à court terme. V4 contredit le besoin de certitude. "
    "V5 contredit la mémoire affective (« la dernière fois ça a marché donc cette fois aussi »). Intégrer ces "
    "vérités au niveau réflexe demande de la répétition consciente sur 6-12 mois."
]))

story.extend(exercice([
    "<b>Récitation matinale.</b> Chaque matin, avant ouverture des marchés, tu lis à voix basse les 5 vérités. "
    "Pas en les lisant — en les HABITANT. Pause après chaque pour ressentir si elle est vraie pour toi.",
    "<b>Mémorisation 30 jours.</b> Tu dois pouvoir réciter les 5 vérités de mémoire, dans l'ordre, sans regarder. "
    "Pas par discipline scolaire — parce que tu auras besoin de les actionner en situation de stress.",
    "<b>Application pré-trade.</b> Avant chaque trade, identifie laquelle des 5 est la plus pertinente pour ce "
    "moment. Tu l'évoques. Tu cliques."
]))
story.extend(phrase_ancre(
    "« Les 5 vérités ne sont pas des slogans. Ce sont les axiomes de mon nouveau système d'exploitation. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "Les 4 peurs fondamentales du trader", ACCENT))
story.extend(retenir(
    "Le trader perdant agit sous l'influence de quatre peurs : peur de perdre, peur de rater, peur de se tromper, "
    "peur de laisser de l'argent sur la table. Chaque peur produit des comportements spécifiques. Identifier "
    "tes deux dominantes te permet de les désamorcer."
))

story.append(styled_table([
    [C("Peur", cell_g), C("Symptôme typique", cell_g), C("Antidote", cell_g)],
    [C("Peur de perdre", cell_b),
     C("Couper les gains tôt, hésiter à entrer"),
     C("Accepter le risque corporellement. Visualisation pré-trade.")],
    [C("Peur de rater (FOMO)", cell_b),
     C("Entrer en retard, prendre B-grade"),
     C("Pré-décision écrite : si pas A+, pas de trade.")],
    [C("Peur de se tromper", cell_b),
     C("Décaler le SL, doubler sur la perte"),
     C("V1 + V3 : se tromper est dans la distribution.")],
    [C("Peur de laisser argent", cell_b),
     C("Pousser au-delà du TP (pattern +1500)"),
     C("Pré-décider à PnL=0 ce que tu fais à TP.")],
], [3.5*cm, 6*cm, 6.5*cm]))
story.append(Spacer(1, 10))

story.extend(make_callout("◈  CHEZ TOI", [
    "Tes deux peurs dominantes sont probablement la peur de SE TROMPER (donc tu décales) et la peur de LAISSER "
    "DE L'ARGENT SUR LA TABLE (donc tu pousses — pattern +1500). Elles travaillent en tandem : tu pousses parce "
    "que tu ne veux pas rater plus, et quand ça reverse, tu refuses parce que tu ne veux pas avoir eu tort. "
    "Ces deux peurs sont fondamentalement liées à ton lien identité-performance."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible (peur 4 — laisser argent) :</b> +800 PnL. TP à +1000. Récitation : « si ça continue à monter sans "
    "moi après mon TP, c'est dans la distribution. Je ne suis pas censé capturer chaque mouvement. Mon edge "
    "se joue sur 100 trades. » Tu coupes au TP. Tu fermes la plateforme."
]))

story.extend(exercice([
    "<b>Diagnostic des 4 peurs.</b> Sur tes 10 derniers crashs/erreurs, identifie laquelle des 4 peurs était à "
    "l'œuvre. Probablement les peurs 3 et 4 dominent. C'est ta cible prioritaire.",
    "<b>Pré-décisions écrites.</b> Pour chaque peur, écris UNE phrase de pré-décision à te réciter avant chaque "
    "trade. Exemple peur 4 : « Je coupe au TP. Si le marché monte sans moi, c'est OK. C'est dans le plan. »"
]))
story.extend(phrase_ancre(
    "« Les 4 peurs ne sont pas miennes. Elles sont humaines. Je les nomme, je les désamorce. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "L'état de zone", ACCENT))
story.extend(retenir(
    "La zone est l'état mental où tu exécutes ton plan sans friction interne. Pas de questionnement, pas de "
    "drame émotionnel, pas d'hésitation. Le trade est exécuté comme un chirurgien ferme une plaie : geste calme, "
    "précis, sans charge identitaire. Ce n'est PAS un don. C'est le résultat d'une préparation."
))
story.extend(explication([
    "<b>Trois composants assemblés.</b> (1) <b>Confiance</b> dans la méthode (validée statistiquement par une "
    "série antérieure). (2) <b>Discipline</b> (capacité réflexe à exécuter le plan même sous pression). "
    "(3) <b>Perspective probabiliste</b> (chaque trade est une instance d'une série). Quand les trois sont "
    "présents, la zone émerge naturellement. Quand l'un manque, l'état est instable."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu n'as JAMAIS été dans la zone, probablement. Tu as eu des sessions où tu te sentais en flow — mais "
    "c'était un flow émotionnel (l'euphorie d'une bonne séance), pas la zone (le calme exécutif). Différence "
    "cruciale : le flow émotionnel est instable et se retourne en crash. La zone est stable et reproductible."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(6*cm, lambda c, w, h: draw_flow(c, w, h,
    ["Méthode validée 100 trades", "Discipline installée 6-12 mois",
     "5 vérités au niveau réflexe", "★ ZONE — exécution sans friction"],
    accent=ACCENT, color_last=GREEN)))
story.append(P("La zone est l'aboutissement d'un travail intégré. Pas un état magique.", caption))

story.extend(exercice([
    "<b>Le test de la zone.</b> Pendant une session, observe ton état corporel après chaque trade. Si tu "
    "ressens euphorie, excitation, soulagement intense, angoisse : tu n'es PAS dans la zone. Tu es en émotion. "
    "La zone se sent comme... rien. Comme respirer. C'est le signe.",
    "<b>Carnet de zone.</b> Chaque session, note 1-10 ton niveau de zone (1 = drame émotionnel, 10 = neutralité "
    "chirurgicale). Sur 90 jours, tu vas voir l'évolution."
]))
story.extend(phrase_ancre(
    "« La zone n'est pas un état magique. C'est le résultat naturel d'un travail intégré. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Discipline face aux prop firms — règles structurelles", ACCENT))
story.extend(retenir(
    "Les prop firms (Apex, Topstep, Alpha Futures) imposent des règles structurelles : drawdown trailing, "
    "limite de perte journalière, ratio gain/perte. Ces règles ne sont pas tes ennemies — elles sont une "
    "discipline EXTERNE qui peut compenser ta discipline interne défaillante. Apprends à les aimer."
))
story.extend(explication([
    "<b>Les règles typiques.</b> Drawdown trailing (ton compte ne peut pas baisser de plus de X depuis son "
    "plus haut atteint). Daily loss limit (perte max par jour, souvent 2-3% du compte). Ratio profit-perte "
    "(certaines exigent une cohérence). Ces règles existent pour protéger la firme. Mais elles te protègent "
    "AUSSI — elles t'empêchent d'aller dans les zones les plus destructrices.",
    "<b>Le piège classique.</b> Tu vois les règles comme une contrainte. Tu cherches à les contourner. Tu "
    "t'épuises mentalement à les négocier. Tu finis par les casser et perdre le compte. Reframe : la règle "
    "EST ton allié structurel. Sans elle, tu irais plus loin dans ta destruction."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as cramé plusieurs comptes Apex/Topstep/Alpha. Diagnostic honnête : les règles n'étaient pas le "
    "problème — elles t'ont arrêté avant que tu ailles plus loin. Le problème était ton incapacité à "
    "respecter même ces règles. Sans elles, tu aurais perdu plus. Avec elles, tu as au moins limité la casse."
], GOLD, NAVY, accent=NAVY))

story.append(P("Re-cadrage des règles prop firm", h_sub))
story.append(styled_table([
    [C("Règle prop firm", cell_g), C("Lecture saboteur", cell_g), C("Lecture cible", cell_g)],
    [C("Trailing drawdown"), C("« contrainte qui me bloque »"), C("« filet de sécurité contre ma folie »")],
    [C("Daily loss limit"), C("« faut respecter ce plafond »"), C("« arrêt obligatoire avant catastrophe »")],
    [C("Consistency rule"), C("« je dois lisser mes gains »"), C("« preuve que mon edge est réel »")],
    [C("Pas de news trading"), C("« je rate des opportunités »"), C("« évite les pièges de volatilité »")],
], [4.5*cm, 5.5*cm, 6*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu te fixes tes propres limites PLUS STRICTES que celles de la prop firm. Si le compte "
    "Apex tolère -3% par jour, tu te fixes -1,5%. Tu utilises 50% de la marge pour avoir un coussin. La règle "
    "externe te protège, ta règle interne plus stricte t'évite de tester la règle externe."
]))

story.extend(exercice([
    "<b>Audit de tes derniers comptes cramés.</b> Pour chaque compte cramé, écris : (1) quelle règle prop firm "
    "tu as cassée, (2) à quelle perte tu en étais quand tu l'as cassée. Tu vas voir un pattern. Tu sauras "
    "exactement quelle marge tu dois te garder.",
    "<b>Marge personnelle stricte.</b> Pour chaque règle prop firm, fixe ta version 50% plus stricte. Affiche "
    "au mur. C'est ton vrai cadre — pas celui de la firme."
]))
story.extend(phrase_ancre(
    "« La règle prop firm est ma sauvegarde. Je l'aime. Je me fixe ma propre version, encore plus stricte. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "Exécuter un plan vs avoir raison", ACCENT))
story.extend(retenir(
    "Le trader amateur cherche à avoir raison. Le trader pro cherche à exécuter un plan. Deux postures opposées. "
    "Avoir raison nourrit l'ego — et tue le compte. Exécuter le plan nourrit l'opérateur — et construit l'edge."
))
story.extend(explication([
    "<b>La différence interne.</b> Quand tu cherches à avoir raison, chaque trade est un test de toi-même. "
    "Une victoire te valide. Une défaite t'attaque. Tu charges chaque clic d'enjeu identitaire. Quand tu "
    "cherches à exécuter un plan, chaque trade est une instance d'un protocole. Une victoire confirme la "
    "distribution. Une défaite confirme la distribution aussi. Aucune charge identitaire.",
    "<b>Le test pratique.</b> Demande-toi : « si je découvrais après-coup que ce trade aurait été gagnant "
    "mais que je ne l'ai pas pris parce qu'il n'était pas dans mon plan, je me sentirais comment ? » Si la "
    "réponse est « furieux d'avoir raté » → tu cherches à avoir raison. Si c'est « OK, c'était hors plan » → "
    "tu cherches à exécuter."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu cherches massivement à avoir raison. Le pattern +1500 EST ça : tu ne veux pas couper parce que couper "
    "= avoir eu raison partiellement, et tu veux raison ENTIÈREMENT. Tu pousses pour valider ton hypothèse "
    "jusqu'au bout. Le marché te dément. Tu refuses parce que ça remettrait en cause ta justesse. C'est "
    "l'ego — pas l'analyse."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Posture", cell_g), C("Question intérieure", cell_g), C("Effet sur le trade", cell_g)],
    [C("Avoir raison"), C("« J'avais raison ? »"), C("Charge identitaire, pousser, décaler")],
    [C("Exécuter"), C("« J'ai suivi le plan ? »"), C("Détachement, couper aux niveaux fixés")],
], [3.5*cm, 5*cm, 7.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> à la fin de chaque trade, ne te demande PAS « ai-je eu raison ». Demande-toi « ai-je "
    "respecté le plan ». Cette question seule peut être posée. Ta seule responsabilité est l'exécution. "
    "Le résultat appartient au marché."
]))

story.extend(exercice([
    "<b>Le tribunal de l'exécution.</b> Chaque fin de session, dans ton journal, pour chaque trade : "
    "« exécution = OUI / NON ». Pas « gagnant / perdant ». Juste exécution. Sur 30 jours, tu mesures ta "
    "vraie compétence — qui est l'exécution, pas le résultat.",
    "<b>Reframe linguistique.</b> Si tu te surprends à dire « j'avais raison sur ce trade », corrige : « j'ai "
    "exécuté ce trade ». Cette substitution déconnecte progressivement ton ego du résultat."
]))
story.extend(phrase_ancre(
    "« Je n'ai pas à avoir raison. J'ai à exécuter. Le résultat appartient au marché. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "Trader émotionnel vs trader systématique", ACCENT))
story.extend(retenir(
    "Deux modes de trader. <b>Émotionnel</b> : décide en temps réel selon le feeling, le contexte, l'humeur. "
    "<b>Systématique</b> : exécute des règles pré-établies, identiques à chaque occurrence. Pour quelqu'un "
    "comme toi, le mode émotionnel est mortel. Le mode systématique te sauve."
))
story.extend(explication([
    "<b>Le mode émotionnel.</b> Tu rentres parce que « ça sent bon ». Tu modifies parce que « j'ai un doute ». "
    "Tu coupes parce que « j'ai peur ». Tu pousses parce que « le momentum est solide ». Chaque décision est "
    "prise dans l'instant, avec l'état émotionnel du moment. C'est ingouvernable sur 100 trades.",
    "<b>Le mode systématique.</b> Tu as un setup A+ défini précisément (conditions techniques, contexte, "
    "killzone). Si toutes les conditions sont remplies, tu rentres. Sinon, tu ne rentres pas. Pas de "
    "discussion. Le SL est à X (calculé). Le TP est à Y (calculé). BE à +1R. Plateforme fermée. Tu reviens "
    "pour le résultat. Reproduis 100 fois."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fonctionnes principalement en mode émotionnel — même si tu crois être systématique. Indice : si tu "
    "ne peux pas écrire ta méthode en une page A4 avec des conditions précises, tu n'es pas systématique. "
    "Tu es émotionnel avec un vernis de méthode. Le travail est de tout coucher par écrit, précisément, et "
    "de ne plus jamais dévier."
], GOLD, NAVY, accent=NAVY))

story.append(P("Ta méthode systématique — à écrire en une page A4", h_sub))
story.append(styled_table([
    [C("Élément", cell_g), C("À définir précisément", cell_g)],
    [C("Contexte macro"), C("Bias daily / weekly clair. Si pas clair → pas de trade.")],
    [C("Niveau structurel"), C("OB / FVG / liquidité ciblée. Localisation exacte.")],
    [C("Killzone"), C("London / NY. Horaires fixés.")],
    [C("Confirmation"), C("CHoCH sur LTF. Indicateur de raison. Précisé.")],
    [C("Entrée"), C("Limite / market. Précisé.")],
    [C("Stop loss"), C("Calculé selon structure. % du capital fixé.")],
    [C("Take profit"), C("Niveau précis. RR minimum 1:2.")],
    [C("Gestion"), C("BE à +1R obligatoire. Pas de modification après.")],
    [C("Conditions d'invalidation"), C("Si X arrive avant l'entrée → annulé.")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Écriture de la méthode A4.</b> Cette semaine, tu écris ta méthode en une page A4. Conditions précises, "
    "sans ambiguïté. Tu signes en bas. Tu colles au mur. C'est ta loi pour 100 trades.",
    "<b>Le test de Turing.</b> Donne ta page A4 à quelqu'un qui ne trade pas. Demande-lui de te dire si tel "
    "setup serait valide ou pas. Si la réponse est ambiguë → ta méthode n'est pas assez précise. Tu reprends."
]))
story.extend(phrase_ancre(
    "« Je passe du trader émotionnel au trader systématique. C'est juste de l'écriture précise. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 5 ---
story.append(P("Carte mentale — Partie 5", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Probabilités",
    [
        {"label": "PRINCIPES", "leaves": ["paix avec incertitude", "distribution > instance", "100 trades, pas 1"], "color": NAVY},
        {"label": "OUTILS", "leaves": ["5 vérités", "substitution grammaticale", "diagnostic 4 peurs"], "color": ACCENT},
        {"label": "CIBLE", "leaves": ["état de zone", "exécution sans friction", "chirurgical"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Reconfigurer la pensée → installer les vérités → atteindre la zone.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 5", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  PROBABILITÉS — FICHE D'ANCRAGE                           ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Vouloir savoir si CE trade va marcher.                  ║
║    Ajouter de l'analyse pour calmer l'anxiété.             ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Phrase "ça VA monter" / "ça DOIT marcher"             ║
║    - Recherche d'un nouvel outil après 3 pertes            ║
║    - Changement de méthode dans la semaine                 ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Reformuler en probabilité ("X% selon ma série")      ║
║    2. Réciter la vérité pertinente (V1 à V5)               ║
║    3. Identifier la peur active (P1-P4) + antidote         ║
║                                                            ║
║  RÈGLE DE TRADING                                          ║
║    Je joue 100. Celui-ci ne dit rien sur mon edge.         ║
║    Stricte intangibilité de la méthode pendant 100 trades. ║
║    Récitation matinale des 5 vérités.                      ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Je joue 100. Celui-ci ne dit rien sur mon edge. »     ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


print("✓ Parties 4 et 5 écrites")


# ============================================================
# PARTIE 6 — QUAND LE CORPS DIT STOP
# ============================================================
_part_color[0] = PART_COLORS[5]
_part_num[0] = 6
_part_name[0] = "Corps dit stop"
ACCENT = PART_COLORS[5]

story.extend(part_separator(6, "Comprendre quand", "le corps dit stop", ACCENT))
story.extend(part_intro_header(6, "Comprendre quand le corps dit stop",
    "Le coût somatique des émotions refoulées et de la sur-activation", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tu as la capacité de pousser. Ta rééducation post-2022, ATHÉNA, le saut d'obstacles, le trading — tu sais "
    "tout encaisser, tout porter, tout maintenir. Cette qualité t'a sauvé après l'accident. Mais à long terme, "
    "sans modulation, elle a un <b>coût somatique</b>. Le corps tient un compte. Tôt ou tard, il présente l'addition."
))
story.append(P(
    "Cette partie t'apprend à reconnaître les signaux corporels avant qu'ils deviennent des problèmes, à dire "
    "non, à respecter les limites physiologiques de récupération, et à reconnaître les patterns du « gentil "
    "performant » qui s'épuise en silence."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "Le stress chronique de bas niveau", ACCENT))
story.extend(retenir(
    "Le stress aigu intense est métabolisé par l'organisme. Le stress chronique de bas niveau (la pression "
    "sourde permanente) ne l'est pas. C'est lui qui dérègle l'immunité, accélère le vieillissement cellulaire, "
    "prépare les maladies chroniques. Le coût n'est pas dans l'intensité — il est dans la DURÉE."
))
story.extend(explication([
    "<b>Physiologie.</b> Un stress aigu déclenche cortisol + adrénaline, puis retour à la normale. Cycle court, "
    "métabolisé. Un stress chronique maintient le cortisol élevé en permanence — inflammation systémique, "
    "résistance à l'insuline, suppression immunitaire, érosion des télomères. Sur 5-10 ans, ce système cuit "
    "lentement. Tu ne le sens pas — jusqu'au jour où tu le sens."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Stress chroniques superposés : trading (pression financière), ATHÉNA (charge mentale), post-TBI (pression "
    "discrète de prouver), saut d'obstacles compétitif. Tu ne ressens probablement aucun comme « écrasant ». "
    "Mais cumulés et permanents, ils maintiennent ton cortisol à un niveau élevé en continu. Indicateurs : "
    "sommeil pas complètement réparateur, tensions chroniques, digestion irrégulière, humeur en yo-yo."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> tu instaures une <b>journée OFF complète par semaine</b> — pas de trade, pas d'ATHÉNA, pas "
    "d'écran professionnel. Tu fais une marche longue, tu lis, tu cuisines, tu dors. Tu donnes à ton système "
    "le temps de redescendre. Sur l'année, ça change ta physiologie."
]))

story.extend(exercice([
    "<b>Audit du stress chronique.</b> Liste tes 5 principales sources de stress chronique de bas niveau. Note "
    "pour chacune si elle est négociable (tu peux la réduire) ou non. Tu vas voir qu'une partie est négociable "
    "et que tu la maintiens par habitude.",
    "<b>Sabbat hebdomadaire.</b> Choisis un jour fixe par semaine où tu décroches complètement. Vraiment. C'est "
    "un investissement de santé."
]))
story.extend(phrase_ancre(
    "« Le coût n'est pas dans l'intensité d'un événement. Il est dans la permanence d'un régime. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "La suppression émotionnelle a un coût", ACCENT))
story.extend(retenir(
    "Quand une émotion est activée mais que son expression est bloquée, la réaction physiologique ne disparaît "
    "pas — elle se prolonge en tension corporelle, en inflammation. Répétée des milliers de fois, elle "
    "devient un état chronique."
))
story.extend(explication([
    "<b>Le principe.</b> Une émotion est avant tout un état corporel. L'expression (parole, mouvement, larmes) "
    "complète le cycle physiologique. Sans expression, le corps reste en activation. Refouler chroniquement "
    "produit un coût mesurable sur l'immunité et le système autonome."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Deux émotions probablement souvent supprimées. <b>La colère</b> : à propos de l'accident 2022, des "
    "conséquences sur ton temps, de certaines personnes pas à la hauteur. <b>La lassitude</b> : tu pousses "
    "tellement que tu ne t'autorises pas à être fatigué. Cette suppression a été utile en phase aiguë post-2022. "
    "Trois ans après, c'est devenu un automatisme. Le travail est de retrouver l'accès aux émotions qui sont "
    "là sans être dites."
], GOLD, NAVY, accent=NAVY))

story.append(P("Protocole d'expression émotionnelle (5 étapes)", h_sub))
story.extend(ascii_box("""
1. RECONNAÎTRE   →  "Là, maintenant, je ressens quoi ?"
                    Nomme : colère, tristesse, peur, lassitude, honte.

2. AUTORISER     →  "J'ai le droit de ressentir ça."
                    Pas de jugement. Pas de "je devrais pas".

3. LOCALISER     →  Où dans le corps ? Quelle qualité ?

4. EXPRIMER      →  À voix haute (seul) / par écrit (3 pages sans censure)
                    / par mouvement (marche rapide, sac de frappe)
                    / par les larmes (si elles viennent)

5. RETOUR CALME  →  Respiration ou présence corporelle.
""", accent=ACCENT))

story.extend(exercice([
    "<b>Quart d'heure émotionnel quotidien.</b> Chaque soir, 15 min, seul, en silence : tu identifies et "
    "exprimes ce qui n'a pas été exprimé dans la journée. Préventif. Tu vides régulièrement.",
    "<b>Travail de la colère 2022.</b> 1 séance dédiée par mois : tu écris une lettre à ton accident, à ton "
    "corps, à ce qui s'est passé. Tu n'envoies pas. Tu exprimes ce qui n'a pas pu être exprimé à l'époque."
]))
story.extend(phrase_ancre(
    "« Ce que je ne dis pas, mon corps le portera. J'exprime régulièrement pour ne pas accumuler. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "Apprendre à dire non", ACCENT))
story.extend(retenir(
    "Dire non n'est pas une mauvaise éducation. C'est une compétence de PROTECTION des ressources. Tes ressources "
    "énergétiques sont finies. Chaque oui consomme. Si tu dis oui à tout, tu finis sans rien pour ce qui compte "
    "vraiment."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Le réflexe de dire oui est souvent installé en enfance : l'enfant comprend que dire "
    "non = retrait de l'amour parental. Adulte, ce réflexe est automatique — il dit oui avant même d'évaluer "
    "la ressource. Coût qui s'accumule : surcharge, ressentiment, épuisement."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Le « non » est un muscle atrophié chez toi. Pas par lâcheté — par habitude. Trois domaines à entraîner : "
    "(1) social (demandes d'amis, obligations familiales), (2) professionnel (engagements ATHÉNA qui dépassent "
    "ta capacité), (3) envers toi-même (le non à un trade B-grade, le non à une journée de plus sans repos). "
    "La dernière catégorie est la plus difficile."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Niveau", cell_g), C("Formulation", cell_g), C("Quand", cell_g)],
    [C("1 — Non poli"), C("« Merci de penser à moi. Je ne peux pas. »"),
     C("Refus standard")],
    [C("2 — Non avec proposition"), C("« Pas maintenant. Dans X semaines OK. »"),
     C("Maintenir le lien")],
    [C("3 — Non ferme"), C("« Non, ce ne sera pas possible. »"),
     C("Pas d'aménagement")],
    [C("4 — Non avec limite"), C("« Je ne peux plus accepter ce type de demande. »"),
     C("Pattern problématique")],
], [3.5*cm, 7*cm, 5.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>5 non par semaine.</b> Cette semaine, identifie 5 occasions de dire non. Petites ou grandes. Dis-les. "
    "Observe ce qui se passe en toi (culpabilité ? soulagement ?). Souvent rien chez l'autre — la peur est "
    "plus grande que la conséquence réelle.",
    "<b>Délai de 24h.</b> Pour toute demande qui peut attendre, tu ne réponds jamais immédiatement. 24h pour "
    "évaluer la ressource. La majorité de tes oui regrettés sont des oui immédiats.",
    "<b>Le non à toi-même.</b> 1x/jour, dis non à toi-même sur quelque chose que tu fais par habitude et qui "
    "te coûte (trade B-grade, session d'écran prolongée, suralimentation). Le non à toi-même est le plus "
    "libérateur."
]))
story.extend(phrase_ancre(
    "« Dire non n'est pas un refus de l'autre. C'est un oui à ce qui compte vraiment pour moi. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "L'identité construite sur la performance", ACCENT))
story.extend(retenir(
    "Beaucoup construisent leur identité sur leur utilité — pour autrui, pour leur estime. C'est une identité "
    "FRAGILE : elle dépend de la production continue. Le jour où tu ne produis pas, tu ne sais plus qui tu es. "
    "Cette fragilité génère une anxiété de fond permanente."
))
story.extend(explication([
    "<b>Le mécanisme.</b> L'identité d'utilité est souvent installée dans l'enfance : l'enfant comprend qu'il "
    "est aimé/valorisé quand il produit (bonnes notes, succès visibles). Il intériorise : « je vaux par ce que "
    "je donne ». Adulte, il ne sait plus se reposer sans culpabilité, vit dans une anxiété permanente de "
    "ne pas être « assez ». La performance devient une thérapie qui ne soigne jamais."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as installé en plus, après 2022, une couche supplémentaire : « je dois prouver que mon cerveau marche, "
    "que mon corps marche, que ce qui m'est arrivé ne m'a pas réduit. » Cette preuve permanente te pousse à la "
    "performance constante. Trading, ATHÉNA, équitation, box — autant de terrains de preuve. Mais tu "
    "n'arriveras jamais à LA preuve qui te libère. La preuve dont tu as besoin n'est pas dans la performance — "
    "elle est dans l'acceptation que tu vaux indépendamment de ce que tu produis."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Saboteur :</b> dimanche après-midi, rien à faire. Pas de marchés, ATHÉNA en pause. Tu ressens un vide, "
    "une agitation, une vague culpabilité. Tu ouvres ton ordinateur, tu analyses des charts « pour avancer ». "
    "Tu ne te reposes pas — tu compenses le vide identitaire par de la pseudo-production.",
    "<b>Cible :</b> dimanche, vide. Tu nommes : « identité d'utilité qui s'angoisse — c'est normal, je laisse "
    "passer ». Bon livre. Longue marche sans téléphone. Tu existes sans produire. Au début inconfortable. "
    "À force, possible. Puis agréable. Puis nécessaire."
]))

story.extend(exercice([
    "<b>L'audit identitaire.</b> Réponds par écrit : « si je ne produisais rien pendant un mois (pas de trading, "
    "pas d'ATHÉNA, pas de compétition, juste de l'existence), qui serais-je ? » La difficulté de la réponse "
    "mesure ton degré d'identité d'utilité.",
    "<b>L'heure d'inutilité.</b> Chaque jour, 1h de présence sans production. Marche, lecture, contemplation. "
    "Ton entraînement à l'existence non-conditionnelle.",
    "<b>Liste des « je suis » non-performance.</b> Identifie 10 attributs de toi qui n'ont rien à voir avec la "
    "performance. Pas « je suis trader », « je suis cavalier » — plutôt « je suis curieux », « je suis sensible "
    "aux animaux », « je suis loyal »."
]))
story.extend(phrase_ancre(
    "« Je ne vaux pas par ce que je produis. Je vaux. Point. La production vient ensuite. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Le repos comme nécessité physiologique", ACCENT))
story.extend(retenir(
    "Le repos n'est pas l'inverse de la productivité. C'est sa CONDITION. Un système qui ne récupère pas se "
    "dégrade — c'est la même loi pour un muscle, un système immunitaire, un cerveau. Le repos est une compétence "
    "à entraîner, pas un cadeau qu'on s'accorde."
))
story.extend(explication([
    "<b>Les 4 cycles à respecter.</b> Ultradien (~90 min), circadien (24h), hebdomadaire (7 jours), saisonnier "
    "(3 mois). Chaque cycle a une phase d'activation et une phase de récupération. Si tu force l'activation "
    "permanente, tu compromets la récupération. Sur le long terme : dégradation immunitaire, déclin cognitif, "
    "fragilité émotionnelle."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Pour ton cas post-TBI, c'est particulièrement coûteux. Les traumas crâniens demandent plus de récupération "
    "que la moyenne — ton cerveau a besoin de sommeil de qualité pour ses processus de réparation continus. Si "
    "tu dors mal ou peu, tu compromis directement ta reconstruction neurologique."
], GOLD, NAVY, accent=NAVY))

story.append(P("Les 4 cycles de récupération", h_sub))
story.append(styled_table([
    [C("Cycle", cell_g), C("Durée", cell_g), C("Récupération à respecter", cell_g)],
    [C("Ultradien"), C("~90 min"),
     C("Toutes les 90 min : pause de 5-15 min. Pas d'écran.")],
    [C("Circadien"), C("24h"),
     C("Sommeil 7-9h. Couché avant 23h. Pas de café après 14h.")],
    [C("Hebdomadaire"), C("7 jours"),
     C("1 jour OFF complet. Pas de production. Repos réel.")],
    [C("Saisonnier"), C("3 mois"),
     C("5-10 jours OFF par trimestre minimum.")],
], [3*cm, 2.5*cm, 10.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Audit de récupération.</b> Sur les 4 cycles, note 1-10 ton respect actuel. Identifie le plus négligé. "
    "C'est ta cible prioritaire pour 30 jours.",
    "<b>Implémentation du jour OFF.</b> Choisis un jour fixe par semaine. Bloque-le dans ton calendrier. "
    "Non négociable.",
    "<b>Routine de coucher.</b> 30-60 min avant le sommeil : pas d'écran, lumière basse, lecture ou méditation, "
    "respiration. À force, cette séquence devient un déclencheur biologique de sommeil."
]))
story.extend(phrase_ancre(
    "« Le repos n'est pas le contraire du travail. C'est sa condition. Je récupère pour pouvoir agir. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Les signaux corporels avant le sabotage", ACCENT))
story.extend(retenir(
    "Ton sabotage n'arrive jamais d'un coup. Le corps envoie des signaux 30 minutes à 2 heures AVANT que la "
    "décision destructrice soit prise. Apprendre à les lire = interception précoce. Le sabotage de +1500 "
    "se prépare physiquement avant que tu cliques."
))
story.extend(explication([
    "<b>Le pattern précurseur.</b> Avant que tu décides de pousser au-delà du TP : ta respiration s'est "
    "accélérée légèrement. Tes épaules se sont contractées. Une chaleur est montée dans la poitrine. Tes "
    "mâchoires se sont serrées. Tu n'as pas remarqué — mais ton corps était déjà en mode pre-saboteur. "
    "Quand le moment de décision arrive, le terrain est préparé.",
    "<b>L'avantage stratégique.</b> Si tu détectes ces signaux 30 min avant, tu peux intervenir AVANT que le "
    "préfrontal soit complètement OFF. Tu peux fermer la session, marcher, respirer, te ramener à un baseline "
    "calme. Tu retires l'opportunité au saboteur. C'est 100 fois plus efficace que d'essayer de résister "
    "au moment du clic."
]))

story.append(P("Les signaux précurseurs à reconnaître", h_sub))
story.append(styled_table([
    [C("Zone du corps", cell_g), C("Signal précoce", cell_g), C("Ce que ça annonce", cell_g)],
    [C("Respiration"), C("Plus rapide, moins profonde"), C("Activation sympathique en cours")],
    [C("Épaules / nuque"), C("Contraction progressive"), C("Tension narrative qui monte")],
    [C("Mâchoire"), C("Serrement involontaire"), C("Résistance interne")],
    [C("Ventre"), C("Noeud, vide, ou chaleur"), C("Émotion non identifiée")],
    [C("Poitrine"), C("Chaleur, oppression"), C("Charge dopaminergique ou anxiété")],
    [C("Mains"), C("Moiteur, agitation"), C("Excitation pré-impulsion")],
    [C("Yeux"), C("Tunnel visuel sur l'écran"), C("Focus restreint, dissociation possible")],
], [3*cm, 5*cm, 8*cm]))
story.append(Spacer(1, 10))

story.extend(make_callout("◈  CHEZ TOI", [
    "Tu n'as probablement aucune conscience de ces signaux actuellement. C'est normal — ton interoception est "
    "altérée (cf. Partie 3 concept 4). Le travail est de RESTAURER cette capacité. Une fois restaurée, tu vas "
    "te surprendre : tu sentiras les choses 1h avant que ton mental ne s'en rende compte."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> 3 scans corporels par session de trading (avant ouverture, mi-session, fin de session). "
    "À chaque scan, tu notes 1-10 l'intensité de chaque zone. Si une zone dépasse 7/10 → SIGNAL. Tu prends "
    "une pause AVANT de prendre un autre trade. Tu ne pousses pas la session."
]))

story.extend(exercice([
    "<b>Calibrage du seuil personnel.</b> Pendant 14 jours, à chaque session, scan corporel + notation. Après "
    "chaque crash ou décision regrettée, retour en arrière : quel score corporel avais-je 30 min avant ? "
    "Tu vas identifier TON seuil personnel (probablement 6-7/10 sur 1-2 zones). C'est ton red flag personnalisé.",
    "<b>Journal pré-sabotage.</b> Pour chaque session : score corporel d'entrée + score à la fin + qualité "
    "des décisions. Tu construis ta propre courbe de corrélation."
]))
story.extend(phrase_ancre(
    "« Mon corps annonce le sabotage avant qu'il arrive. J'apprends à le lire pour intercepter. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "La fatigue cumulée — l'ennemi invisible", ACCENT))
story.extend(retenir(
    "La fatigue ne s'additionne pas linéairement. Elle se CUMULE. Trois nuits courtes consécutives produisent "
    "un déficit cognitif plus grand que trois nuits courtes isolées. Tu peux te sentir « OK » et être en "
    "réalité massivement dégradé. C'est précisément à ce moment que les comptes se craament."
))
story.extend(explication([
    "<b>Le mécanisme du cumul.</b> Chaque nuit de sommeil insuffisant produit un déficit qui ne se résorbe "
    "qu'en partie la nuit suivante. Sur 5-7 jours de sommeil dégradé, tu accumules un déficit qui dégrade ton "
    "préfrontal de 30-40%. Tu prends des décisions avec un cerveau « ralenti » sans le savoir.",
    "<b>L'illusion de l'habitude.</b> Le pire : tu ne ressens PLUS la fatigue après quelques jours. Le corps "
    "compense par cortisol et adrénaline élevés. Tu te sens « normal ». En réalité, ton cerveau prend des "
    "décisions plus risquées, moins planifiées, plus impulsives. Tu attribues les erreurs à un manque de "
    "discipline. La cause réelle est physiologique."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Post-TBI, ton seuil de fatigue cumulée est plus bas que la moyenne. Ce qui passerait pour quelqu'un "
    "d'autre te détruit plus vite. Une semaine intense de trading + ATHÉNA + équitation + sommeil léger = "
    "terrain parfait pour un crash de compte le vendredi. Tu attribues au stress, à la malchance. Cause "
    "réelle : fatigue cumulée non reconnue."
], GOLD, NAVY, accent=NAVY))

story.append(P("Les marqueurs de fatigue cumulée", h_sub))
story.append(styled_table([
    [C("Marqueur", cell_g), C("Signal", cell_g)],
    [C("Réveils sans raison"), C("Sommeil fragmenté → SN saturé")],
    [C("Café qui ne fait plus rien"), C("Cortisol déjà au max")],
    [C("Irritabilité disproportionnée"), C("Préfrontal en sous-régime")],
    [C("Erreurs bêtes répétées"), C("Attention dégradée")],
    [C("Perte d'envie pour ce que tu aimes"), C("Système dopaminergique épuisé")],
    [C("Tension musculaire constante"), C("Sympathique bloqué en haut")],
], [5*cm, 11*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu instaures la « semaine de récupération ». Toutes les 3-4 semaines de trading actif, "
    "une semaine où tu réduis significativement la charge (équitation, ATHÉNA, sport). Tu dors plus. Tu "
    "fais des marches longues. Tu reconstitues ton baseline. Sur l'année, c'est ce qui te garde performant."
]))

story.extend(exercice([
    "<b>Score de fatigue quotidien.</b> Chaque matin, score 1-10 de ton état (sommeil + énergie + clarté "
    "mentale). Si tu enchaînes 3 jours ≤ 6/10 → SIGNAL ROUGE. Pas de trading ce jour-là. Tu prends une "
    "demi-journée OFF.",
    "<b>Variabilité cardiaque (HRV).</b> Si tu as une montre connectée, surveille ton HRV. Baisse marquée "
    "sur 3-5 jours = fatigue cumulée mesurable. Indicateur le plus fiable disponible."
]))
story.extend(phrase_ancre(
    "« La fatigue cumulée est invisible et destructrice. Je la traque, je la respecte. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "Le protocole d'arrêt complet", ACCENT))
story.extend(retenir(
    "L'arrêt n'est pas l'inverse du trading. C'est une COMPÉTENCE distincte qui demande son propre protocole. "
    "Tu ne sais pas arrêter — c'est ce qui te crame. Voici le protocole en 4 niveaux pour acquérir la "
    "compétence d'arrêt."
))

story.append(P("Protocole d'arrêt en 4 niveaux", h_sub))
story.extend(ascii_box("""
NIVEAU 1 — Arrêt de trade
─────────────────────────
TP atteint OU SL touché OU décision de couper.
Tu coupes. Tu ne discutes pas. Tu fermes la position.

NIVEAU 2 — Arrêt de session
──────────────────────────
Limite quotidienne atteinte (gain OU perte) OU
2 pertes consécutives OU 3 trades chaotiques OU
fatigue manifeste OU émotion forte non gérable.
→ Plateforme fermée. Téléphone autre pièce.
   Plus de trade aujourd'hui. Pas de discussion.

NIVEAU 3 — Arrêt de semaine
──────────────────────────
3 sessions difficiles consécutives OU
crash de compte OU pic émotionnel non résolu OU
fatigue cumulée 5+ jours.
→ Pause complète 3-7 jours. Pas de chart, pas de plateforme.
   Reconstruction du baseline.

NIVEAU 4 — Arrêt de cycle
─────────────────────────
Crash de compte prop firm OU 2+ comptes perdus en 2 mois OU
épuisement majeur.
→ Sevrage 4 semaines minimum. Désinstallation apps.
   Travail somatique intensif. Retour au protocole zéro.
""", accent=ACCENT))

story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as l'habitude de t'arrêter UNIQUEMENT quand le compte est cramé (niveau 4 forcé). Tu n'as jamais "
    "pratiqué les niveaux 1, 2, 3 proprement. Tu sautes directement au 4 quand tout explose. Apprendre les "
    "niveaux 1-3 = ne plus jamais arriver au niveau 4."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> tu écris les SEUILS personnels pour chaque niveau. Niveau 1 : tes règles d'entrée/sortie "
    "claires. Niveau 2 : ta limite quotidienne (par exemple -1% du compte). Niveau 3 : tes critères de "
    "pause semaine. Niveau 4 : tes critères de sevrage. Tu signes, tu colles. Tu appliques."
]))

story.extend(exercice([
    "<b>Le contrat d'arrêt.</b> Sur une feuille A4, à la main : « Mes 4 niveaux d'arrêt. Seuils précis. "
    "Signé : Marien. » Affiche au mur. Tu lis avant chaque session.",
    "<b>Le décompte des niveaux pratiqués.</b> Chaque mois, tu comptes : combien de fois j'ai pratiqué le "
    "niveau 1 (arrêt trade) ? Le niveau 2 (arrêt session) ? Le niveau 3 (arrêt semaine) ? Si le niveau 2 "
    "n'est pas pratiqué AU MOINS 2 fois par mois, c'est que tu ne respectes pas tes propres limites."
]))
story.extend(phrase_ancre(
    "« Savoir s'arrêter est une compétence distincte du trader rentable. Je l'entraîne à chaque niveau. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 6 ---
story.append(P("Carte mentale — Partie 6", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Corps dit stop",
    [
        {"label": "MÉCANIQUES", "leaves": ["stress chronique", "suppression émotionnelle", "identité d'utilité"], "color": NAVY},
        {"label": "OUTILS", "leaves": ["dire non", "quart d'heure émotionnel", "audit identitaire"], "color": ACCENT},
        {"label": "REPOS", "leaves": ["4 cycles respectés", "jour OFF/sem", "5j OFF/trimestre"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Reconnaître les coûts cachés → moduler → respecter les cycles.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 6", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  CORPS DIT STOP — FICHE D'ANCRAGE                         ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Supprimer émotions + identité d'utilité +               ║
║    sur-activation chronique = dégradation programmée.      ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Dire oui automatiquement à tout                       ║
║    - Sentir une fatigue qu'on masque par stimulation       ║
║    - Repos qui génère culpabilité                          ║
║    - Tensions chroniques                                   ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Délai 24h avant toute réponse à demande              ║
║    2. Audit ressource avant d'accepter                     ║
║    3. Si non, dire non sans culpabilité                    ║
║    4. 15 min d'expression émotionnelle quotidienne         ║
║                                                            ║
║  RÈGLE                                                     ║
║    5 non par semaine minimum.                              ║
║    1 jour OFF / semaine non négociable.                    ║
║    5 jours OFF / trimestre.                                ║
║    Sommeil 7-9h, couché avant 23h.                         ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Je vaux. Indépendamment de ce que je produis. »       ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


# ============================================================
# PARTIE 7 — CONSTRUIRE DES HABITUDES QUI TIENNENT
# ============================================================
_part_color[0] = PART_COLORS[6]
_part_num[0] = 7
_part_name[0] = "Habitudes"
ACCENT = PART_COLORS[6]

story.extend(part_separator(7, "Construire des habitudes", "qui tiennent", ACCENT))
story.extend(part_intro_header(7, "Construire des habitudes qui tiennent",
    "L'architecture qui transforme les insights en système quotidien", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tout ce que tu as compris dans les parties précédentes ne te servira à rien sans <b>architecture "
    "d'habitudes</b>. Tu opères actuellement en cycles de motivation : tu te dis « cette semaine je m'y mets "
    "vraiment », tu tiens 5 jours intensément, puis tu retombes. Tu confonds intensité ponctuelle et changement "
    "durable. La transformation se joue dans l'inverse : <b>petits gestes consistants sur la durée</b>."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "L'agrégation des gains marginaux", ACCENT))
story.extend(retenir(
    "Une amélioration de 1% par jour produit, par effet composé, environ 37 fois mieux au bout d'un an. Une "
    "dégradation de 1% par jour produit l'inverse. La différence entre trajectoire ascendante et descendante "
    "se joue dans des écarts quotidiens qui semblent négligeables."
))
story.extend(explication([
    "<b>L'arithmétique du temps long.</b> Mathématiquement : 1,01^365 = 37,8. Sur 5 ans : 1,01^1825 ≈ "
    "98 milliards (théorique). Les humains pensent linéairement et la composition est exponentielle. "
    "Quand tu vois « 1% par jour », tu te dis « c'est rien ». C'est en réalité énorme sur la durée."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu vis l'inverse de cette logique. Tu cherches le coup ponctuel qui change tout — le compte funded qui "
    "débloque, la session +5000 qui transforme. Tu mises sur l'amplitude instantanée. C'est pour ça que tu peux "
    "faire 2 ans de trading sans avoir progressé significativement : tu n'as pas accumulé de 1%.",
    "Pour toi en pratique : 1% de MEILLEURE EXÉCUTION par jour. Pas une session miracle. Un protocole un peu "
    "mieux respecté. Une décision marginalement plus calme. À l'échelle de 6-12 mois, transformation radicale."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(5.5*cm, lambda c, w, h: draw_flow(c, w, h,
    ["Jour 1 : 1.00", "Jour 90 : 2.46", "Jour 180 : 6.05", "Jour 365 : 37.78"],
    accent=ACCENT, color_first=GOLD_PALE, color_last=GREEN)))
story.append(P("L'arithmétique des 1%. Lente au début, explosive à la fin.", caption))

story.extend(exercice([
    "<b>Le carnet des 1%.</b> Chaque soir, écris une ligne : « aujourd'hui qu'est-ce que j'ai fait à 1% mieux ? » "
    "Tu cherches une chose, même minuscule. Cette pratique installe le mindset des micro-gains.",
    "<b>Sortie des cycles motivation.</b> Identifie ton dernier cycle « cette semaine je vais m'y mettre "
    "vraiment » qui a échoué. Pourquoi ? Probablement parce que tu as visé trop haut. Refais avec 1% — et "
    "observe la différence sur 30 jours."
]))
story.extend(phrase_ancre(
    "« Je ne mise pas sur le coup miracle. Je mise sur 1% par jour pendant 365 jours. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "Le plateau du potentiel latent", ACCENT))
story.extend(retenir(
    "Le changement n'est presque jamais linéaire. Tu pratiques des semaines, des mois, sans aucun résultat "
    "visible. C'est la phase du plateau. La majorité abandonne ici. Ceux qui tiennent voient soudain un "
    "basculement, parfois spectaculaire."
))
story.extend(explication([
    "<b>Métaphore du glaçon.</b> Un glaçon dans une pièce à -10°. Tu chauffes. À -8°, rien. À -6°, rien. À 0°, "
    "le glaçon fond brutalement. Tous les degrés précédents étaient nécessaires — mais invisibles. Le changement "
    "humain fonctionne pareil. Le travail accumulé est réel mais sous le seuil de visibilité."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as probablement un long historique de plateaux abandonnés. Tu commences une discipline (méditation, "
    "sport, journal trading). Au bout de 3-4 semaines tu ne vois aucun résultat évident. Tu arrêtes. Tu repars "
    "sur autre chose. Tu refais ça 5 fois en 2 ans. Tu n'as JAMAIS dépassé le plateau d'aucune discipline."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(6*cm, lambda c, w, h: draw_comparison(c, w, h,
    "CE QUE TU ATTENDS",
    ["progression linéaire", "résultats visibles dès J+30", "récompense fréquente", "abandon si rien à 1 mois"],
    "CE QUI SE PASSE",
    ["plateau invisible", "basculement à J+60-90", "récompense différée", "tenir → basculer"]
)))
story.append(P("Différentiel attente / réalité. Tenir le plateau = condition du basculement.", caption))

story.extend(exercice([
    "<b>L'engagement temporel.</b> Pour chaque nouvelle habitude, décide à l'avance la durée minimale avant de "
    "pouvoir juger. Recommandation : 90 jours minimum. 12 semaines pour le journal. 6 semaines pour la "
    "respiration quotidienne. Tu n'évalues pas avant.",
    "<b>L'observation des micro-signaux.</b> Pendant le plateau, ne cherche pas les gros résultats. Cherche les "
    "micro-changements : « j'ai hésité 2 secondes de plus avant de cliquer ». Ces signaux sont la preuve que "
    "le travail souterrain se fait."
]))
story.extend(phrase_ancre(
    "« Le plateau n'est pas l'absence de progrès. C'est la phase invisible du progrès. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "La hiérarchie en 3 couches — identité d'abord", ACCENT))
story.extend(retenir(
    "Trois niveaux de changement : RÉSULTAT (le plus instable), PROCESSUS, IDENTITÉ (le plus profond). "
    "La plupart visent le résultat. Quelques-uns travaillent le processus. Très peu vont à l'identité. "
    "Or c'est l'identité qui pilote durablement."
))

story.append(Schema(7*cm, lambda c, w, h: draw_pyramid(c, w, h, [
    ("RÉSULTAT", "« Je veux gagner 10000€ »", "instable, tu ne le contrôles pas", RED_SOFT, RED_ACC),
    ("PROCESSUS", "« J'exécute mon protocole »", "stable tant que motivé", GOLD_PALE, GOLD_DEEP),
    ("IDENTITÉ", "« Je suis trader chirurgical »", "le seul niveau durable", GOLD, NAVY),
])))
story.append(P("La pyramide du changement — plus tu descends, plus le changement est profond.", caption))

story.extend(make_callout("◈  CHEZ TOI", [
    "Identité cible : <b>« Je suis un trader chirurgical. »</b> Chirurgical = précis, calme, ennuyeux à observer, "
    "exécution propre. Un chirurgien ne « croit » pas qu'une opération va marcher. Il ouvre, il fait le geste "
    "prévu, il referme. Il ne double pas sur une perte. Il ne décale pas son SL. Ces gestes n'ont aucun sens "
    "pour qui il est. L'identité résout le problème de discipline — tu n'as pas à te forcer."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Cible :</b> avant chaque session, tu relis la page identité. Avant chaque trade : « est-ce qu'un trader "
    "chirurgical ferait ce clic ? ». Si non, tu ne cliques pas. À force, le filtre devient automatique."
]))

story.extend(exercice([
    "<b>La page identité.</b> Une page de ton journal dédiée. En majuscules, l'identité cible. En dessous, chaque "
    "jour, 1 ligne : « aujourd'hui qu'est-ce qu'un trader chirurgical a fait que j'ai fait aussi ? » Tu cumules "
    "les preuves.",
    "<b>Le compteur des votes.</b> En fin de journée : « Aujourd'hui combien de votes CHIRURGICAL j'ai déposés ? "
    "Combien CONTRE ? » Ratio sur la semaine. Tu vois l'identité s'installer."
]))
story.extend(phrase_ancre(
    "« Je ne vise pas un résultat. Je deviens une personne dont le résultat découle. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "La boucle d'habitude", ACCENT))
story.extend(retenir(
    "Toute habitude — bonne ou mauvaise — fonctionne sur la même mécanique : DÉCLENCHEUR → DÉSIR → RÉPONSE → "
    "RÉCOMPENSE. Comprendre ces 4 éléments te permet de démonter une mauvaise habitude et d'en installer une "
    "bonne en jouant sur les leviers."
))

story.append(Schema(7*cm, lambda c, w, h: draw_habit_loop(c, w, h)))
story.append(P("La boucle universelle. Modifier UN élément suffit à transformer l'ensemble.", caption))

story.append(P("Désinstaller le décalage de SL", h_sub))
story.append(styled_table([
    [C("Élément", cell_g), C("Actuellement", cell_g), C("Modification", cell_g)],
    [C("Déclencheur"), C("Voir le prix s'approcher du SL"),
     C("Fermer la plateforme dès l'ordre placé")],
    [C("Désir"), C("Éviter la perte ressentie comme injuste"),
     C("Visualisation pré-trade. SN pré-désensibilisé.")],
    [C("Réponse"), C("Modifier le SL"),
     C("Close the platform = impossible de tricher")],
    [C("Récompense"), C("Soulagement temporaire si revient"),
     C("Reframe : récompense = ne pas avoir trahi le plan")],
], [3*cm, 5.5*cm, 7.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Cartographier 3 habitudes destructrices.</b> Pour chacune (décalage SL, sur-trading après perte, "
    "consommation contenu post-crash), remplis le tableau des 4 éléments. Identifie l'élément le plus facile "
    "à modifier (souvent le déclencheur).",
    "<b>Une habitude à la fois.</b> Ne change pas 6 habitudes simultanément. Choisis-en une, installe-la "
    "proprement sur 6-8 semaines, puis passe à la suivante."
]))
story.extend(phrase_ancre(
    "« Mes habitudes se construisent en 4 éléments. Je modifie un élément, le tout bascule. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Empilement + règle des 2 minutes + environnement", ACCENT))
story.extend(retenir(
    "Trois techniques d'installation puissantes. <b>Empilement</b> : rattacher une nouvelle habitude à une "
    "existante. <b>Règle des 2 minutes</b> : commencer ridiculement petit. <b>Environnement</b> : modifier "
    "le contexte plutôt que d'utiliser la volonté."
))

story.append(P("Empilement d'habitudes — exemples pour toi", h_sub))
story.append(styled_table([
    [C("Habitude existante", cell_g), C("Nouvelle habitude empilée", cell_g)],
    [C("Après mon café du matin"), C("→ 2 min de respiration cohérente")],
    [C("Après ma respiration"), C("→ Relire les 5 vérités à voix basse")],
    [C("Après ma session de trading"), C("→ Remplir la section APRÈS SESSION du journal")],
    [C("Après ma douche du soir"), C("→ 5 min de scan corporel")],
    [C("Après pansage avec ma filly"), C("→ Noter 1 chose ressentie dans le corps")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 10))

story.append(P("Règle des 2 minutes — versions ridiculement petites", h_sub))
story.append(styled_table([
    [C("Habitude ambitieuse", cell_g), C("Version 2 min pour démarrer", cell_g)],
    [C("Méditer 30 min/jour"), C("Méditer 2 min/jour")],
    [C("Tenir un journal complet"), C("Écrire 1 phrase par jour")],
    [C("Lire 1 livre/mois"), C("Lire 1 page/jour")],
    [C("Sport 1h/jour"), C("Mettre la tenue de sport (c'est tout)")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Modifier l'environnement bat la discipline.</b> Apps de trading désinstallées du téléphone = "
    "friction insurmontable pour un geste impulsif. Cahier journal toujours visible = friction 0 pour écrire. "
    "Tu calibres : bonne habitude accessible en moins de 5 sec, mauvaise habitude > 20 sec de friction."
]))

story.extend(exercice([
    "<b>Empiler 3 nouvelles habitudes ce mois.</b> Choisis 3 nouvelles (version 2 min). Empile chacune sur une "
    "existante. Suivi quotidien sur 30 jours.",
    "<b>L'audit environnement.</b> Pour chaque domaine (téléphone, bureau, chambre), 1 modification anti-mauvaise "
    "habitude + 1 modification pro-bonne habitude. Cette semaine."
]))
story.extend(phrase_ancre(
    "« Je commence ridiculement petit. La consistance bat l'ambition à chaque fois. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Le journal — outil maître de transformation", ACCENT))
story.extend(retenir(
    "Le journal de trading n'est pas un outil parmi d'autres. C'est L'OUTIL maître. Sans journal manuscrit "
    "régulier, aucun travail psychologique ne se sédimente. Tu observes en surface — tu n'ancres pas dans "
    "le temps long. Le journal change le cerveau, physiquement, par la main qui écrit."
))
story.extend(explication([
    "<b>Pourquoi manuscrit.</b> Écrire à la main mobilise une chaîne neuronale (moteur fin + langage + "
    "mémoire) qui ne s'active pas en tapant. La main qui écrit RALENTIT le débit — tu ne peux pas écrire "
    "vite, donc tu réfléchis plus. Tu ne peux pas fuir comme en tapant. L'engagement physique est plus fort.",
    "<b>Trois fonctions du journal.</b> (1) <b>Mémoire externe</b> : sortir l'expérience de ta tête pour la "
    "voir. (2) <b>Pattern recognition</b> : sur 30-90 jours, tu vois les répétitions, les déclencheurs, les "
    "régularités. (3) <b>Identité</b> : en t'observant écrire « j'ai été un trader chirurgical aujourd'hui », "
    "tu deviens cette identité. Le journal sculpte qui tu es."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu n'as probablement jamais tenu un journal trading manuscrit pendant plus de 2 semaines. C'est l'erreur "
    "centrale. Tous les exercices de ce manuel reposent sur un journal manuscrit régulier. Sans lui, le "
    "manuel reste de la lecture. Avec lui, il devient transformation."
], GOLD, NAVY, accent=NAVY))

story.append(P("Template de journal — sections obligatoires", h_sub))
story.append(styled_table([
    [C("Section", cell_g), C("Quand", cell_g), C("Contenu", cell_g)],
    [C("Pré-session"), C("Avant"),
     C("État SN, sommeil, énergie, intention, taille max")],
    [C("Trade par trade"), C("Pendant"),
     C("Setup, entrée, SL, TP, score corporel, décision")],
    [C("Post-session"), C("Après"),
     C("Bilan PnL, bilan EXÉCUTION, émotions, leçons")],
    [C("Hebdo"), C("Dimanche"),
     C("Pattern de la semaine, vote chirurgical/contre, ajustement")],
    [C("Mensuel"), C("Fin du mois"),
     C("Statistiques 100 trades en cours, identité, projection")],
], [3*cm, 2*cm, 11*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu achètes un cahier sérieux (pas un carnet bon marché). Cuir, papier épais, format A5 "
    "ou A4. Page 1 : « Cahier de Marien, trader chirurgical en formation. Ouvert le [date]. » C'est un "
    "objet sacré. Tu le respectes. Tu l'ouvres à chaque session."
]))

story.extend(exercice([
    "<b>Engagement 90 jours.</b> Tu écris dans le cahier à chaque session pendant 90 jours, sans exception. "
    "Pas de session sans journal = pas de session le lendemain. Cette règle est non négociable.",
    "<b>Revue hebdomadaire.</b> Dimanche soir, 30 min : tu relis ta semaine. Tu identifies 3 patterns. Tu "
    "écris une page de synthèse. Tu projettes la semaine suivante."
]))
story.extend(phrase_ancre(
    "« Pas de journal manuscrit = pas de transformation. Le cahier est sacré. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "L'automatisation du bon comportement", ACCENT))
story.extend(retenir(
    "Le bon comportement automatisé bat le bon comportement volontaire. Tu as peu de volonté disponible "
    "(elle s'épuise dans la journée). Mais tu as une capacité infinie d'automatisation. Le travail est de "
    "DÉPLACER tes bons comportements de la zone « volonté requise » vers la zone « automatique »."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Toute action répétée 50-100 fois dans le même contexte devient un automatisme "
    "neuronal — un programme stocké dans les noyaux gris centraux, indépendant du préfrontal. Tu n'as plus "
    "à décider — ça se fait. C'est ce qui fait la différence entre un débutant qui force et un expert qui "
    "exécute sans effort. Tu vises ce stade pour tes gestes de trader.",
    "<b>Les gestes à automatiser en priorité.</b> Placer SL avec l'ordre. Fermer la plateforme après ordres "
    "placés. Remonter au BE à +1R. Écrire dans le journal après chaque trade. Méditer le matin. Cold shower. "
    "Pansage hebdomadaire. Plus tu les répètes dans le même contexte, plus ils deviennent invisibles à ta "
    "volonté."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fais souvent les bonnes choses... quand tu y penses. Le problème : tu n'y penses pas toujours. "
    "L'automatisation supprime le besoin d'y penser. Quand fermer la plateforme après les ordres devient "
    "aussi automatique que verrouiller ta porte en sortant, le piège du décalage SL disparaît à la racine."
], GOLD, NAVY, accent=NAVY))

story.append(P("Les 8 gestes à automatiser absolument", h_sub))
story.append(styled_table([
    [C("Geste", cell_g), C("Déclencheur (ancre)", cell_g)],
    [C("Placer SL avec l'ordre"), C("Avant tout clic Buy/Sell")],
    [C("Fermer la plateforme post-ordres"), C("Dès que SL et TP placés")],
    [C("Remonter au BE à +1R"), C("Alerte sonore au +1R")],
    [C("Scan corporel pré-session"), C("Après le café du matin")],
    [C("Écriture pré-session"), C("Après le scan corporel")],
    [C("Méditation"), C("Après le réveil, avant café")],
    [C("Pansage conscient"), C("Mercredi soir 18h fixé")],
    [C("Cold shower"), C("Immédiatement au lever")],
], [6.5*cm, 9.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu choisis UN geste à automatiser pendant 30 jours. Tu le rattaches à un déclencheur "
    "existant. Tu le fais sans exception 30 jours. À la fin, il est devenu automatique. Tu passes au suivant. "
    "Sur 12 mois = 12 gestes automatisés. Ton trading change de nature."
]))

story.extend(exercice([
    "<b>Carte d'automatisation.</b> Liste les 8 gestes. Identifie le déclencheur existant pour chacun. Choisis "
    "l'ORDRE d'installation (commence par le plus facile). Affiche au mur.",
    "<b>Le compteur des répétitions.</b> Pour chaque geste en cours d'automatisation, tu coches dans un "
    "calendrier visible. Vise 30 jours consécutifs. À la 30e coche, le geste est ancré."
]))
story.extend(phrase_ancre(
    "« Ma volonté est limitée. Mon automatisme est infini. Je déplace tout vers l'automatique. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "Le système anti-rechute", ACCENT))
story.extend(retenir(
    "Tu vas rechuter. Pas peut-être — certainement. Tous les humains qui changent passent par des rechutes. "
    "La différence entre ceux qui s'en sortent et ceux qui restent piégés : un SYSTÈME pré-établi pour gérer "
    "la rechute. Sans système, chaque rechute te détruit. Avec système, chaque rechute te renforce."
))
story.extend(explication([
    "<b>Le piège de la perfection.</b> Tu te promets « plus jamais ». Tu tiens 23 jours. Tu craques. Tu te "
    "dis « j'ai tout cassé ». Tu retournes au pattern complet, en pire. C'est l'effet « WHAT THE HELL » "
    "documenté : une transgression mineure produit un abandon total parce que la règle absolue est cassée. "
    "C'est plus destructeur que la transgression elle-même.",
    "<b>Le système anti-rechute.</b> 3 composants : (1) <b>Reconnaissance précoce</b> de la rechute (signaux). "
    "(2) <b>Protocole immédiat</b> d'arrêt + soin. (3) <b>Reprise structurée</b> sans culpabilité massive. "
    "Tu pré-écris ce système quand tu vas bien, pour l'utiliser quand tu vas mal."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "À chaque crash de compte, tu vis le scénario complet : rechute → catastrophe émotionnelle → arrêt total "
    "pendant 1-3 mois → reprise sans rien avoir traité → autre rechute. Tu n'as PAS de système anti-rechute. "
    "Tu vis chaque rechute comme la première. C'est ce qui doit changer."
], GOLD, NAVY, accent=NAVY))

story.append(P("Ton plan anti-rechute en 6 étapes", h_sub))
story.extend(ascii_box("""
ÉTAPE 1 — RECONNAÎTRE
─────────────────────
Signaux : décalage de SL, sur-trading, taille augmentée, FOMO.
Action : nommer « rechute en cours ». Pas de jugement.

ÉTAPE 2 — ARRÊT IMMÉDIAT
────────────────────────
Plateforme fermée. Téléphone autre pièce.
Pas de tentative de se refaire. Sortie physique.

ÉTAPE 3 — SOIN CORPOREL
───────────────────────
Marche 30 min. Cold shower. Respiration. Eau. Repas simple.
Tu reviens à un état physiologique baseline.

ÉTAPE 4 — JOURNAL HONNÊTE
─────────────────────────
Tu écris : qu'est-ce qui s'est passé ? Quel signal j'ai
manqué ? Quelle leçon ? Pas de flagellation. Analyse.

ÉTAPE 5 — RÉ-ENGAGEMENT MINIMAL
───────────────────────────────
Tu écris l'engagement nouveau, SANS exiger la perfection.
« Je reprends demain avec UN ajustement. » Pas tout reprendre.

ÉTAPE 6 — REPRISE STRUCTURÉE
────────────────────────────
24-72h après la rechute, reprise avec UN protocole modifié.
La rechute t'a appris quelque chose. Tu intègres. Tu continues.
""", accent=ACCENT))

story.extend(application([
    "<b>Cible :</b> tu écris ce plan en 6 étapes sur une feuille A5, à la main. Tu le glisses dans ton "
    "portefeuille. Tu l'as physiquement avec toi. Quand la rechute arrive (et elle arrivera), tu sors la "
    "feuille. Tu suis les étapes."
]))

story.extend(exercice([
    "<b>Simulation pré-rechute.</b> Cette semaine, simule mentalement une rechute. Imagine que tu viens de "
    "casser ta règle de SL. Tu suis les 6 étapes mentalement. Tu sentirais quoi à chaque étape ? Tu te "
    "prépares.",
    "<b>Carnet des rechutes.</b> Une page dédiée dans ton cahier journal : « Mes rechutes ». Chaque rechute "
    "y est consignée : date, signal manqué, leçon. Pas de honte — c'est ton corpus d'apprentissage."
]))
story.extend(phrase_ancre(
    "« La rechute n'est pas l'échec. L'absence de système anti-rechute, oui. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 7 ---
story.append(P("Carte mentale — Partie 7", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Habitudes",
    [
        {"label": "PRINCIPES", "leaves": ["1% par jour", "plateau latent", "identité d'abord"], "color": NAVY},
        {"label": "BOUCLE", "leaves": ["déclencheur", "désir", "réponse", "récompense"], "color": ACCENT},
        {"label": "MÉTHODE", "leaves": ["empilement", "règle 2 min", "environnement modifié"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Vise identité → décompose la boucle → installe par micro-doses.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 7", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  HABITUDES — FICHE D'ANCRAGE                              ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Cycles de motivation au lieu de systèmes.               ║
║    Vouloir tout changer en même temps.                     ║
║    Abandonner pendant le plateau.                          ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - « Lundi je m'y mets vraiment »                        ║
║    - Ambition trop grande pour le départ                   ║
║    - Abandon à la semaine 4-8                              ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Identifier l'identité cible                          ║
║    2. Choisir UNE habitude version 2 min                   ║
║    3. L'empiler sur une habitude existante                 ║
║    4. Modifier l'environnement pour faciliter              ║
║    5. Suivre 12 semaines minimum avant évaluation          ║
║                                                            ║
║  RÈGLE                                                     ║
║    Une habitude à la fois pendant 6-8 semaines.            ║
║    Suivi visuel quotidien (grille / calendrier).           ║
║    Jamais manquer 2 fois de suite.                         ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « 1% par jour. Pendant 365 jours. »                     ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


print("✓ Parties 6 et 7 écrites")


# ============================================================
# PARTIE 8 — LÂCHER PRISE ÉMOTIONNELLEMENT
# ============================================================
_part_color[0] = PART_COLORS[7]
_part_num[0] = 8
_part_name[0] = "Lâcher prise"
ACCENT = PART_COLORS[7]

story.extend(part_separator(8, "Lâcher prise", "émotionnellement", ACCENT))
story.extend(part_intro_header(8, "Lâcher prise émotionnellement",
    "L'antidote opérationnel à ton contrôle compulsif", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tu es un contrôleur. C'est documenté dans ton parcours. Le contrôle t'a sauvé après 2022 — il a fallu "
    "reconstruire un corps, une mémoire, un avenir. Mais cette compétence a un coût gigantesque : tu ne sais "
    "plus lâcher quand il faudrait lâcher. Tu serres dans des contextes où serrer aggrave (un trade qui tourne "
    "mal, une émotion qui veut s'exprimer, une journée qui demande du repos)."
))
story.append(P(
    "Cette partie t'apprend que le lâcher-prise n'est pas une faiblesse opposée au contrôle. C'est une "
    "<b>compétence complémentaire</b>. Le maître n'est pas celui qui contrôle tout — c'est celui qui sait "
    "QUAND contrôler et QUAND lâcher, et peut faire les deux à volonté."
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "Le paradoxe : la résistance amplifie", ACCENT))
story.extend(retenir(
    "Quand tu résistes à une émotion, tu lui donnes de l'énergie. La résistance la renforce. Quand tu cesses "
    "de résister — quand tu l'accueilles sans la combattre — elle perd progressivement sa charge. "
    "« Ce à quoi tu résistes persiste. Ce que tu acceptes traverse. »"
))
story.extend(explication([
    "<b>Physiologie.</b> Une émotion est avant tout un état corporel transitoire. Si tu la laisses traverser, "
    "elle dure typiquement 60 à 90 secondes (neurosciences l'ont mesuré). Si tu lui résistes (jugement, "
    "suppression, agitation mentale), tu réactives le circuit. L'émotion qui aurait duré 90 secondes peut "
    "alors durer des heures, des jours, des années."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu résistes presque tout le temps. Quand une perte arrive, tu résistes à la tristesse / colère / honte — "
    "tu te dis « faut pas, faut tenir ». Tu repousses. L'émotion ne passe pas — elle se loge dans le corps. "
    "Tu finis par porter en permanence un mélange de tristesse, colère et honte non traitées."
], GOLD, NAVY, accent=NAVY))

story.append(Schema(7*cm, lambda c, w, h: draw_comparison(c, w, h,
    "RÉSISTANCE",
    ["émotion → tu juges/refuses", "circuit RÉACTIVÉ", "émotion reste/amplifie", "accumulation chronique"],
    "ACCUEIL",
    ["émotion → tu observes", "cycle physiologique complet", "dissipation 60-90s", "SN retourne au baseline"]
)))
story.append(P("Le paradoxe — accueillir traverse, résister amplifie.", caption))

story.extend(application([
    "<b>Cible :</b> tu cramés un compte. Tu sens la honte monter. Tu te poses 3 min. Tu te dis intérieurement : "
    "« voilà la honte. Je la sens. Je ne la combats pas. » Tu la sens dans le ventre, la poitrine. Tu respires. "
    "Tu ne fais rien d'autre. Après 60-90 sec, la vague passe. Tu reprends ta journée — sans cette honte accumulée."
]))

story.extend(exercice([
    "<b>Pratique des 90 secondes.</b> Prochaine fois qu'une émotion désagréable monte, pose-toi 90 secondes. "
    "Pas plus. Tu fais juste sentir, sans rien faire d'autre. Tu vas être étonné : la plupart des émotions "
    "ne durent vraiment que ça quand on ne leur résiste pas.",
    "<b>Phrase de désamorçage.</b> « Je laisse cette émotion être là. Je n'ai pas à la résoudre maintenant. "
    "Je la sens. C'est tout. » Cette phrase coupe court à la résistance automatique."
]))
story.extend(phrase_ancre(
    "« Ce à quoi je résiste persiste. Ce que je laisse être traverse. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "Le protocole du lâcher en 6 étapes", ACCENT))
story.extend(retenir(
    "Le lâcher-prise n'est pas une attitude mystique. C'est une TECHNIQUE précise avec des étapes concrètes. "
    "Comme toute technique, elle s'apprend, elle se rate au début, elle s'améliore avec la pratique."
))

story.extend(ascii_box("""
LES 6 ÉTAPES DU LÂCHER

1. NOMMER          →  Identifier l'émotion qui monte.
                      "C'est de la peur / colère / honte." Le mot exact.

2. LOCALISER       →  Où dans le corps ? "Ma poitrine. Ma gorge."
                      Tu poses ton attention dessus.

3. ACCEPTER        →  "J'autorise cette émotion à être ici maintenant.
                      Je n'ai pas à la résoudre. Elle peut être là."
                      L'antidote à la résistance.

4. RESPIRER VERS   →  Tu inspires doucement vers la zone.
                      Tu expires lentement. 4-6 cycles.

5. ATTENDRE        →  60 à 90 secondes minimum.
                      Tu observes ce qui se passe.
                      Elle va changer — devenir plus forte un instant,
                      puis se diluer.

6. CONSTATER       →  La charge a diminué. Pas forcément disparu —
                      diminuée. Tu reprends ta journée.
""", accent=ACCENT))

story.extend(make_callout("◈  CHEZ TOI", [
    "L'étape 3 (accepter) est la plus difficile pour toi. Tu es entraîné à ne PAS accepter ce qui te ralentit. "
    "Pour toi, accepter = « valider une faiblesse ». C'est une croyance erronée. Accepter ≠ se résigner. "
    "Accepter signifie : reconnaître ce qui EST déjà là. La différence : si tu l'acceptes, ça peut traverser. "
    "Si tu refuses, ça reste."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Application en trade.</b> +1200 PnL. Désir intense de pousser. Tu pratiques. <b>1) Nommer :</b> « avidité ». "
    "<b>2) Localiser :</b> « ça monte dans ma poitrine ». <b>3) Accepter :</b> « je peux ressentir cet élan. Je n'ai "
    "pas à agir dessus. » <b>4) Respirer :</b> 4 cycles vers la poitrine. <b>5) Attendre :</b> 60 sec. La vague "
    "monte puis redescend. <b>6) Constater :</b> charge à 4/10. Tu peux maintenant exécuter ton plan : couper au TP."
]))

story.extend(exercice([
    "<b>Pratique quotidienne.</b> 1 fois par jour, sur une émotion mineure : tu fais les 6 étapes complètes. "
    "Tu écris une ligne dans ton journal pour valider que tu l'as fait.",
    "<b>Pratique en situation aiguë.</b> Quand tu sens une émotion forte en plein trade, version rapide en 30 sec. "
    "Tu fermes la plateforme pendant ce temps."
]))
story.extend(phrase_ancre(
    "« Le lâcher est une technique. 6 étapes. 90 secondes. Pratiquées, elles deviennent réflexes. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "Le piège du contrôle — linéaire vs stochastique", ACCENT))
story.extend(retenir(
    "Le contrôle est utile dans les domaines où ton effort a un impact direct (ton corps, ATHÉNA, ta filly). "
    "Il est DESTRUCTEUR dans les domaines où ton effort n'a aucun impact direct (la direction du marché, le "
    "résultat d'un trade individuel). Confondre les deux est le piège classique."
))
story.extend(explication([
    "<b>Linéaire vs Stochastique.</b> Le contrôle marche dans les systèmes LINÉAIRES (effort → résultat "
    "proportionnel). Le marché est NON-LINÉAIRE et STOCHASTIQUE. Appliquer la stratégie linéaire à un système "
    "stochastique produit systématiquement de l'échec. Plus tu serres dans un système où serrer n'a pas de "
    "prise, plus tu te crispes inutilement, et plus tu fais des erreurs."
]))

story.append(P("Audit des domaines de ta vie", h_sub))
story.append(styled_table([
    [C("Domaine", cell_g), C("Type", cell_g), C("Stratégie", cell_g)],
    [C("Ta méthode SMC"), C("Linéaire (entraînement)"), C("CONTRÔLER. Plus tu pratiques, mieux tu lis.")],
    [C("Résultat d'un trade individuel"), C("Stochastique"), C("LÂCHER. Aucun contrôle possible.")],
    [C("Ton respect du protocole"), C("Linéaire"), C("CONTRÔLER. Choix à chaque clic.")],
    [C("Direction du marché"), C("Stochastique"), C("LÂCHER. Aucun pouvoir.")],
    [C("Ton corps en rééducation"), C("Linéaire"), C("CONTRÔLER. Discipline donne résultat.")],
    [C("Tes émotions qui montent"), C("Stochastique"), C("LÂCHER. Tu choisis ce que tu en fais, pas si elles montent.")],
    [C("ATHÉNA — production"), C("Linéaire"), C("CONTRÔLER. Effort = résultat moyen terme.")],
    [C("Ce que les autres pensent"), C("Stochastique"), C("LÂCHER. Aucun contrôle direct.")],
], [4.5*cm, 4.5*cm, 7*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu rentres dans un trade. Tu te récites : « je contrôle ma méthode, ma taille, mon SL, mon "
    "TP, mon respect du plan, le moment où je ferme la plateforme. Je ne contrôle rien d'autre. » Cette "
    "récitation t'aide à rester dans ta zone d'action."
]))

story.extend(exercice([
    "<b>Audit du contrôle.</b> Pour chacun de tes domaines de vie (5-7), classe linéaire/stochastique. Cette "
    "carte mentale doit être claire et tu dois t'y référer.",
    "<b>L'exercice du serrement.</b> Quand tu te surprends à serrer (mâchoire, poings, épaules) en trade : "
    "signal que tu essayes de contrôler quelque chose qui ne se contrôle pas. Tu relâches physiquement. Tu "
    "observes ce qui change mentalement."
]))
story.extend(phrase_ancre(
    "« Je contrôle mes gestes. Je lâche les résultats. Cette distinction est ma liberté. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "Le lâcher comme compétence opérationnelle en trading", ACCENT))
story.extend(retenir(
    "Le lâcher s'applique à 7 moments précis de la journée trading. Voici la carte opérationnelle."
))

story.append(styled_table([
    [C("Moment", cell_g), C("Ce qu'il faut LÂCHER", cell_g), C("Comment", cell_g)],
    [C("Avant un trade"), C("Le besoin de savoir si ça va marcher"),
     C("Récitation V2 : « je n'ai pas besoin de savoir »")],
    [C("Au TP atteint"), C("Le désir de pousser au-delà"),
     C("Protocole 6 étapes en 90s + couper")],
    [C("Au SL approché"), C("Le besoin d'éviter cette perte"),
     C("Close the platform. SL fait son boulot.")],
    [C("Après une perte"), C("La narration « j'ai eu tort »"),
     C("Reframe : « trade dans les 45% qui perdent normalement »")],
    [C("Après série de pertes"), C("L'urgence de se refaire"),
     C("Pause 24h. Pas de revanche.")],
    [C("Après un gros gain"), C("Le sentiment d'invincibilité"),
     C("Pause 24h aussi. Pas confiance à l'euphorie.")],
    [C("En fin de session"), C("Le besoin de checker encore"),
     C("Plateforme désactivée. Vie reprise.")],
], [3.2*cm, 5.5*cm, 7.3*cm]))
story.append(Spacer(1, 10))

story.extend(make_callout("◈  CHEZ TOI", [
    "Les 3 moments critiques chez toi : au TP atteint (ton pattern +1500), au SL approché (ton décalage "
    "signature), après une série de pertes (ton FOMO compensatoire). Si tu maîtrises le lâcher dans ces "
    "trois moments, ton trading change de nature."
], GOLD, NAVY, accent=NAVY))

story.extend(exercice([
    "<b>Cartographier tes lâchers difficiles.</b> Sur les 7 moments, identifie tes 2-3 plus difficiles. Pour "
    "chacun, écris une stratégie spécifique.",
    "<b>Journal du lâcher.</b> Chaque session, une ligne dédiée : « moments où j'ai lâché aujourd'hui / "
    "moments où je n'ai pas lâché ». Tu mesures ta compétence sur 30 jours.",
    "<b>Un moment à la fois.</b> Choisis UN seul des 7 moments à travailler intensément pendant 30 jours. "
    "Pas les 7. Un. Puis tu passes au suivant."
]))
story.extend(phrase_ancre(
    "« Le lâcher est ma compétence à entraîner. Pas un événement à attendre. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Lâcher le besoin d'avoir raison", ACCENT))
story.extend(retenir(
    "L'attachement à avoir raison est l'une des causes les plus invisibles et destructrices en trading. Tu "
    "ne le ressens pas comme « j'ai besoin d'avoir raison » — tu le ressens comme « je suis sûr de ma "
    "lecture ». C'est la même chose. Lâcher ce besoin libère ton edge."
))
story.extend(explication([
    "<b>Le mécanisme.</b> Tu as fait une analyse. Tu as une hypothèse. Tu y as mis de l'énergie, du temps, "
    "de l'ego. Quand le marché te contredit, ton cerveau perçoit la contradiction comme une attaque "
    "identitaire — pas comme une information. Tu défends ton hypothèse au lieu de l'abandonner. C'est ce "
    "qui produit les décalages de SL, les ajouts au perdant, le refus de couper.",
    "<b>L'inversion à installer.</b> Ton edge n'est PAS d'avoir raison. C'est d'avoir une distribution de "
    "trades à edge positif. Sur cette distribution, environ 40-50% de tes hypothèses seront fausses — c'est "
    "mathématique. Avoir tort est statistiquement NORMAL. Le combat contre cette réalité est ce qui te crame."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Reprends ton pattern +1500. Tu as raison sur la direction (le marché monte). Couper à +1000 = avoir "
    "raison PARTIELLEMENT. Pour ton ego, c'est insuffisant. Tu pousses pour avoir raison TOTALEMENT. Le "
    "marché reverse. Tu refuses de l'admettre. Tu décales. La cascade vient de ton besoin d'avoir TOTALEMENT "
    "raison, pas du marché."
], GOLD, NAVY, accent=NAVY))

story.append(P("Le diagnostic du besoin d'avoir raison", h_sub))
story.append(styled_table([
    [C("Signal", cell_g), C("Ce que ça révèle", cell_g)],
    [C("« J'avais raison sur ce trade »"), C("Tu t'identifies au résultat correct")],
    [C("« Le marché s'est trompé »"), C("Tu personnifies le marché contre ton ego")],
    [C("Décalage de SL"), C("Refus de la contradiction du marché")],
    [C("Ajout au perdant"), C("Insistance sur ta justesse initiale")],
    [C("Rumination post-perte"), C("Difficulté à intégrer d'avoir eu tort")],
], [5*cm, 11*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu reformules tes pensées de trader. Pas « j'ai raison de penser que ça monte ». "
    "Plutôt « mon hypothèse est X% probable, le contraire est Y% probable, je joue ma distribution ». "
    "Cette reformulation enlève l'ego."
]))

story.extend(exercice([
    "<b>Le test du droit d'avoir tort.</b> Chaque matin, dis à voix basse : « aujourd'hui, j'ai le droit "
    "d'avoir tort sur 40% de mes trades. C'est dans le plan. C'est normal. » Tu donnes la permission à "
    "l'avance.",
    "<b>Reframe linguistique 30 jours.</b> Si tu te surprends à dire « j'avais raison », tu reformules en "
    "« j'ai bien exécuté ». L'identification au résultat est remplacée par l'identification à l'exécution."
]))
story.extend(phrase_ancre(
    "« Mon edge n'est pas d'avoir raison. C'est de jouer ma distribution. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Lâcher la honte et la colère post-perte", ACCENT))
story.extend(retenir(
    "Après une perte, deux émotions montent presque toujours : HONTE (je suis nul, je n'y arriverai jamais) "
    "et COLÈRE (contre toi-même, le marché, les prop firms). Sans protocole, elles te submergent. Avec "
    "protocole, elles passent en 90 secondes."
))
story.extend(explication([
    "<b>La honte spécifique du trader.</b> Honte d'avoir cassé son protocole. Honte d'avoir cramé un compte. "
    "Honte de devoir le cacher aux proches. Cette honte est particulièrement toxique parce qu'elle est "
    "SILENCIEUSE — tu la portes seul. Elle nourrit ensuite la revanche : tu veux te REVAUDOR par un gros "
    "gain qui efface la honte. Tu retournes trader. Cycle.",
    "<b>La colère post-perte.</b> Activation sympathique massive, recherche de cible. Tu peux la diriger "
    "contre toi (auto-flagellation), contre le marché (revenge trading), contre les conditions externes "
    "(prop firms, broker, conjoncture). Aucune direction n'est utile. Toute énergie dirigée vers la colère "
    "post-perte est de l'énergie qui n'est pas dirigée vers la récupération."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu portes probablement une couche de honte chronique liée à tes crashs successifs — non dite, non "
    "traitée. Cette honte chronique te pousse paradoxalement à retourner trader plus rapidement (pour "
    "« effacer » par un gain). C'est exactement contre-productif."
], GOLD, NAVY, accent=NAVY))

story.append(P("Protocole anti-honte / anti-colère post-perte", h_sub))
story.extend(ascii_box("""
PHASE 1 (les 5 premières minutes après la perte)
───────────────────────────────────────────────
- Fermer la plateforme. Téléphone autre pièce.
- Si la colère monte : SORTIR (marche, course, pousser un mur).
- Pas d'analyse. Pas de journal. Décharge corporelle d'abord.

PHASE 2 (30 minutes - 2 heures)
──────────────────────────────
- Quand corps stabilisé : protocole 6 étapes lâcher prise.
- Nommer l'émotion (honte / colère / tristesse / dégoût).
- L'observer 90 secondes sans agir.
- Si vague forte : pendulation avec ressource.

PHASE 3 (le soir)
─────────────────
- Journal détaillé : SANS jugement, SANS flagellation.
- Identifier ce qui s'est passé corporellement et techniquement.
- Si la honte est forte : DIRE à un proche. La cacher l'aggrave.

PHASE 4 (le lendemain)
──────────────────────
- Reprise normale SI prêt. Pas avant.
- Pas de « se refaire ». Pas de revanche.
- Trader comme si la perte d'hier n'avait jamais existé.
""", accent=ACCENT))

story.extend(application([
    "<b>Cible :</b> la honte se dissout en partie par la VERBALISATION. Tu as au moins UNE personne de "
    "confiance à qui tu peux dire honnêtement « j'ai cramé un compte aujourd'hui ». Pas pour aide, juste "
    "pour le dire à voix haute. La honte cachée grandit. La honte dite décroît."
]))

story.extend(exercice([
    "<b>L'inventaire des hontes cachées.</b> Sur une page de ton journal, écris toutes les hontes liées au "
    "trading que tu portes en silence. Tu n'as pas à les dire à quelqu'un — seulement à les écrire et à les "
    "voir. La conscience seule réduit déjà la charge.",
    "<b>Le rituel de décharge corporelle.</b> Identifie UNE activité physique intense que tu peux faire dans "
    "l'heure qui suit une grosse perte. Pour toi probablement : sac de frappe, course rapide, monter à "
    "cheval en cross. Tu décharges la colère par le corps avant qu'elle ne devienne revanche."
]))
story.extend(phrase_ancre(
    "« La honte cachée grandit. La honte dite décroît. La colère, je la décharge dans le corps. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "Lâcher prise ≠ abandon", ACCENT))
story.extend(retenir(
    "Confusion classique et destructrice : croire que lâcher prise = abandonner. C'est l'inverse. "
    "L'abandon vient de l'épuisement, du désespoir, du « j'arrête tout ». Le lâcher-prise vient de la "
    "lucidité, de la capacité à distinguer ce que tu contrôles de ce que tu ne contrôles pas. Ce sont "
    "deux postures opposées."
))
story.extend(explication([
    "<b>L'abandon.</b> Posture d'écrasement. Tu lâches parce que tu n'en peux plus. C'est passif, résigné, "
    "désespéré. Tu lâches tout — y compris ce qui mérite d'être tenu. Après une grosse perte, tu peux "
    "passer en mode abandon : tu arrêtes le trading, tu arrêtes la méditation, tu arrêtes le sport, tu "
    "scrolles Netflix. Ce n'est pas du lâcher-prise. C'est de la dissociation déguisée.",
    "<b>Le lâcher-prise.</b> Posture lucide. Tu lâches ce que tu ne contrôles pas (le résultat d'un trade, "
    "la direction du marché, le passé). Tu maintiens ce que tu contrôles (ton protocole, tes gestes, ta "
    "discipline). Tu continues à pratiquer tes routines. Tu acceptes ce qui est, et tu CONTINUES à faire "
    "ce qui dépend de toi."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu confonds probablement les deux. Quand tu cramés un compte, tu passes en abandon : tout s'arrête, tu "
    "te désorganises, tu abandonnes tes pratiques régulières. C'est l'inverse de ce qu'il faut. Lâcher le "
    "résultat du compte cramé, oui. Abandonner tes pratiques quotidiennes, non. Les deux sont indépendantes."
], GOLD, NAVY, accent=NAVY))

story.append(styled_table([
    [C("Situation", cell_g), C("Abandon (à éviter)", cell_g), C("Lâcher-prise (cible)", cell_g)],
    [C("Crash de compte"), C("J'arrête tout"), C("Je lâche le compte. Je maintiens mes pratiques.")],
    [C("Perte de session"), C("Je m'effondre, soirée détruite"), C("Je lâche la perte. Je vais courir.")],
    [C("Série perdante"), C("Je doute de tout, change de méthode"), C("Je lâche le besoin de comprendre vite. Je continue ma série.")],
    [C("Émotion difficile"), C("Je la fuis (alcool, écran)"), C("Je la laisse passer 90 sec. Je continue.")],
], [3.5*cm, 5.5*cm, 7*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu sépares CONSCIEMMENT les deux. Lâcher = je relâche ce que je ne contrôle pas. "
    "Maintenir = je continue ce qui dépend de moi. Après chaque crash, tu fais l'audit : qu'est-ce que je "
    "lâche (le compte, le résultat) ? Qu'est-ce que je MAINTIENS (méditation, sport, journal, sommeil) ?"
]))

story.extend(exercice([
    "<b>Liste de maintien.</b> Écris 5 pratiques que tu maintiens QUOI QU'IL ARRIVE : méditation matinale, "
    "sport hebdomadaire, pansage avec ta filly, journal, sommeil 8h. Ce sont tes invariants. Même après "
    "le pire crash, ils continuent.",
    "<b>Le check abandon vs lâcher.</b> Quand tu sens un « j'en peux plus », demande-toi : suis-je en train "
    "d'abandonner (rejet de tout) ou de lâcher prise (relâcher ce que je ne contrôle pas) ? Si abandon : "
    "tu te rapproches d'un proche, tu maintiens UNE pratique, tu te ramènes."
]))
story.extend(phrase_ancre(
    "« Lâcher prise n'est pas abandonner. Je relâche ce que je ne contrôle pas. Je maintiens le reste. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "Le retour au corps comme ancre", ACCENT))
story.extend(retenir(
    "Quand le mental dérape (rumination, panique, dissociation, compulsion), le corps est l'ancre la plus "
    "fiable pour revenir. Tu ne peux pas penser « je vais arrêter de penser ». Mais tu peux SENTIR ton "
    "souffle, tes pieds, ton ventre. La sensation corporelle court-circuite le mental."
))
story.extend(explication([
    "<b>Le principe.</b> Le cortex préfrontal (cognition) et le cortex insulaire (interoception) sont en "
    "concurrence pour l'attention consciente. Plus tu portes attention au corps, moins tu rumines. Plus "
    "tu rumines, moins tu sens ton corps. Le travail de retour au corps désactive activement la rumination.",
    "<b>Pourquoi le corps est plus fiable que le mental.</b> Tu peux contrôler ton souffle. Tu peux sentir "
    "tes pieds. Tu peux nommer la température de tes mains. Ce sont des points d'ancrage solides, indépendants "
    "de ton état mental. Quand le mental est dans le chaos, le corps est encore là, calme, accessible."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu vis beaucoup en tête — analyse, prédiction, calcul. Le trading t'a renforcé dans cette habitude. "
    "Ton accès au corps est probablement faible. C'est pour ça que tu te fais déborder par les émotions : "
    "tu n'as pas d'ancre corporelle pour les traverser. La restauration de l'accès au corps (Partie 3 et 4) "
    "est l'infrastructure du lâcher-prise."
], GOLD, NAVY, accent=NAVY))

story.append(P("Les ancres corporelles utilisables en 30 secondes", h_sub))
story.append(styled_table([
    [C("Ancre", cell_g), C("Comment", cell_g), C("Effet", cell_g)],
    [C("Souffle"), C("3 cycles 4-6"), C("Active vagal ventral")],
    [C("Pieds au sol"), C("Sentir contact, pression"), C("Ancrage spatial")],
    [C("Mains chaudes/froides"), C("Eau froide ou frottement"), C("Active interoception")],
    [C("Vue 5 choses"), C("Nommer 5 objets visibles"), C("Sort de la rumination")],
    [C("Ouïe — 4 sons"), C("Identifier 4 sons distincts"), C("Présence sensorielle")],
    [C("Goûter / sentir"), C("Aliment fort, huile essentielle"), C("Reset olfacto-gustatif")],
], [3.5*cm, 5*cm, 7.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> quand tu sens le mental déraper en trade (rumination, panique, compulsion), 30 secondes "
    "d'ancre corporelle AVANT toute autre action. Pieds au sol + 3 respirations + nommer 3 objets visibles. "
    "Tu te ramènes. Tu décides ensuite."
]))

story.extend(exercice([
    "<b>Routine du retour au corps.</b> 5 fois par jour, à des moments aléatoires (alarme téléphone), tu "
    "fais 30 sec d'ancre corporelle. Pas en réaction à un problème — en pratique régulière. À force, "
    "l'ancre devient disponible automatiquement en cas de besoin.",
    "<b>Trousse d'ancres physiques.</b> Garde près de toi (sur ton bureau) 3 objets : pierre froide, "
    "bracelet en bois texturé, petite bouteille d'huile essentielle. Quand tu sens dériver, tu actives "
    "une ancre concrète. Sensoriel toujours plus puissant que mental."
]))
story.extend(phrase_ancre(
    "« Quand le mental dérape, le corps reste. Je reviens au corps pour revenir à moi. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 8 ---
story.append(P("Carte mentale — Partie 8", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Lâcher prise",
    [
        {"label": "PRINCIPES", "leaves": ["résistance amplifie", "60-90 sec suffisent", "linéaire ≠ stochastique"], "color": NAVY},
        {"label": "TECHNIQUE", "leaves": ["6 étapes", "nommer / accepter / respirer", "pratique quotidienne"], "color": ACCENT},
        {"label": "APPLICATION", "leaves": ["7 moments-clés", "TP / SL / post-série", "compétence sur 6-12 mois"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Reconnaître la résistance → appliquer le protocole → installer la compétence.", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 8", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  LÂCHER PRISE — FICHE D'ANCRAGE                           ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Contrôler ce qui n'est pas contrôlable.                 ║
║    Combattre des émotions au lieu de les laisser passer.   ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Mâchoire serrée pendant un trade                      ║
║    - « Je dois absolument... »                             ║
║    - Émotion qui dure plus de 5 minutes                    ║
║    - Refus mental d'une réalité                            ║
║                                                            ║
║  ACTION IMMÉDIATE — PROTOCOLE 6 ÉTAPES                     ║
║    1. NOMMER l'émotion exactement                          ║
║    2. LOCALISER dans le corps                              ║
║    3. ACCEPTER (autoriser la présence)                     ║
║    4. RESPIRER vers la sensation                           ║
║    5. ATTENDRE 60-90 sec                                   ║
║    6. CONSTATER la dissolution                             ║
║                                                            ║
║  RÈGLE                                                     ║
║    1 pratique du protocole par jour pendant 30 jours.      ║
║    Au TP atteint : protocole 90s, puis couper.             ║
║    Au SL approché : close the platform.                    ║
║    Après série : 24h de pause, lâcher la revanche.         ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Je contrôle mes gestes. Je lâche les résultats. »     ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


# ============================================================
# PARTIE 9 — DÉVELOPPER UNE PATIENCE FINANCIÈRE
# ============================================================
_part_color[0] = PART_COLORS[8]
_part_num[0] = 9
_part_name[0] = "Patience financière"
ACCENT = PART_COLORS[8]

story.extend(part_separator(9, "Développer une", "patience financière", ACCENT))
story.extend(part_intro_header(9, "Développer une patience financière",
    "Du coup ponctuel à la construction de 30 ans", ACCENT))

story.append(P("1.  Pourquoi cette partie est cruciale pour toi", h_section))
story.append(P(
    "Tu n'as pas un problème d'argent. Tu as un problème de RAPPORT à l'argent. Tu cherches le coup, pas la "
    "durée. Tu n'as jamais défini ton « assez ». Tu vis le trading comme une course d'amplitude alors que les "
    "fortunes durables se construisent par composition lente. Cette partie reformule la question fondamentale : "
    "quel rapport veux-tu construire avec l'argent pour les 30 prochaines années ?"
))


# --- CONCEPT 1 ---
story.extend(concept_header(1, "Le rôle massif de la chance et du risque", ACCENT))
story.extend(retenir(
    "La chance et le risque sont les forces les plus sous-estimées dans les résultats financiers. Quand "
    "quelqu'un réussit, on attribue à sa compétence. Quand il échoue, à ses erreurs. La réalité : la chance "
    "et le risque jouent un rôle BEAUCOUP plus grand qu'on pense — dans les deux directions."
))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu fais 3 trades gagnants. Tu te dis « j'ai trouvé la formule ». Tu passes en taille x2. Le 4e est perdant. "
    "Tu te dis « j'ai perdu la main ». Sur 5 trades, tu as confondu chance et compétence dans les deux sens.",
    "<b>Cible :</b> bonne série de 3. « C'est dans la distribution. Je maintiens ma taille. La prochaine peut "
    "être perdante. » Tu joues la durée, pas l'amplitude."
], GOLD, NAVY, accent=NAVY))

story.extend(exercice([
    "<b>Audit honnête.</b> Sur tes 10 derniers gros gains et 10 dernières grosses pertes, estime le % de "
    "compétence vs % de chance/risque externe. Tu vas être surpris.",
    "<b>Règle d'humilité.</b> Après chaque grosse série gagnante (3-5 trades), tu ne changes pas ta taille "
    "pendant 7 jours. Tu laisses la chance s'estomper pour voir ta compétence vraie."
]))
story.extend(phrase_ancre(
    "« Mes résultats sont moi + chance + risque. Je suis humble dans les deux directions. »"
))
story.append(PageBreak())


# --- CONCEPT 2 ---
story.extend(concept_header(2, "La composition long terme — durée > amplitude", ACCENT))
story.extend(retenir(
    "La composition (intérêts composés sur le long terme) est la force la plus puissante en finance. Quelqu'un "
    "qui gagne 10%/an pendant 30 ans devient riche. Quelqu'un qui essaie 30%/an pendant 5 ans, en prenant les "
    "risques associés, finit le plus souvent ruiné. Le secret : la DURÉE."
))
story.extend(explication([
    "<b>Mathématiquement.</b> 100€ à 10%/an pendant 30 ans = 1745€. 100€ à 10% pendant 5 ans = 161€. Le facteur "
    "durée est >10x plus puissant que l'amplitude pour un effort équivalent. Contre-intuitif parce que l'humain "
    "pense linéairement. Mais c'est ce qui sépare les vrais riches durables des « riches éphémères »."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Si tu maîtrises ton edge et tu produis 1% par mois moyen sur 30 ans, tu construis une fortune énorme. "
    "10 000€ deviennent ~350 000€. 30 000€ deviennent 1 050 000€. C'est lent, ennuyeux — c'est ce qui marche. "
    "1% par mois est ATTEIGNABLE par un trader rigoureux. 30% par mois est INSOUTENABLE sur la durée. Viser "
    "30% te fait souvent finir avec moins que ce que 1% aurait produit."
], GOLD, NAVY, accent=NAVY))

story.extend(application([
    "<b>Re-paramétrage des objectifs.</b> « Faire 0,5% à 1% par semaine, en moyenne, sur 12 mois consécutifs. » "
    "Cet objectif te protège des comportements destructeurs.",
    "<b>L'engagement de durée.</b> Décide aujourd'hui que tu trades comme métier sérieux pendant AU MOINS 10 ans. "
    "Pas 2 ans pour faire fortune. 10 ans min. Cet horizon change tout."
]))

story.extend(exercice([
    "<b>Calculer ton chemin de composition.</b> Avec ton capital actuel, fais le calcul : si je fais 1% par "
    "semaine en moyenne pendant 10 ans, je termine à combien ? Le résultat va te ramener à la modestie des "
    "bons rendements."
]))
story.extend(phrase_ancre(
    "« La durée bat l'amplitude. Je joue 30 ans, pas 30 jours. »"
))
story.append(PageBreak())


# --- CONCEPT 3 ---
story.extend(concept_header(3, "Faire de l'argent ≠ en garder", ACCENT))
story.extend(retenir(
    "Faire de l'argent demande optimisme, prise de risque, conviction, ambition. En garder demande l'inverse : "
    "humilité, peur, conservation, paranoïa adaptative. Très peu de gens cumulent les deux. La plupart des "
    "fortunes faites sont reperdues parce que les détenteurs n'ont jamais développé la deuxième compétence."
))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu es très optimiste dans ta personnalité de trader. Tu prends des risques. Tu pousses. Cette compétence "
    "est utile — elle te permet d'entrer dans le jeu. Mais tu n'as PRESQUE AUCUNE compétence de paranoïa "
    "adaptative — tu ne sais pas protéger ce que tu as. Même si tu fais 100 000€ en 6 mois, sans la compétence "
    "de garder, tu en auras perdu 90 000 dans les 6 mois suivants."
], GOLD, NAVY, accent=NAVY))

story.append(P("Comportements de GARDER (à installer)", h_sub))
story.append(styled_table([
    [C("Comportement", cell_g), C("Description", cell_g)],
    [C("Sortir une partie des gains"),
     C("Chaque semaine/mois, retirer X% du compte trading vers un compte sécurisé.")],
    [C("Définir un seuil de réussite"),
     C("« Au-dessus de X, je sors le surplus. » Plafonner l'exposition au risque.")],
    [C("Coussin de sécurité"),
     C("3-6 mois de dépenses sur compte épargne, indépendant du trading.")],
    [C("Diversifier ailleurs"),
     C("ATHÉNA, immobilier, fonds indiciels — pas tout dans le trading.")],
    [C("Ne pas augmenter le mode de vie"),
     C("Quand tu gagnes plus, tu n'augmentes PAS proportionnellement. La différence va à l'épargne.")],
], [4.5*cm, 11.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Compte épargne dédié.</b> Cette semaine : ouverture d'un compte épargne DÉDIÉ au surplus du trading. "
    "Aucun virement sortant possible pendant 12 mois (mentalement).",
    "<b>Règle 50/30/20.</b> Sur tout gain mensuel net en trading : 50% reste en compte trading (capitalisation), "
    "30% va à l'épargne dédiée, 20% au plaisir/qualité de vie. Pourcentages fixes, non négociables."
]))
story.extend(phrase_ancre(
    "« Faire de l'argent et le garder sont deux compétences. Je les développe en parallèle. »"
))
story.append(PageBreak())


# --- CONCEPT 4 ---
story.extend(concept_header(4, "Définir « assez »", ACCENT))
story.extend(retenir(
    "Sans définition explicite de ce qui constitue « assez » pour toi, tu cours après l'infini. Et l'infini "
    "ne s'attrape jamais. Tu peux multiplier ton capital par 10, par 100, par 1000 — sans définition, tu "
    "ressentiras toujours un manque."
))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu n'as probablement AUCUNE définition claire de « assez ». Si on te demande « quel niveau de "
    "compte/patrimoine/revenu serait suffisant pour que tu ressentes que tu as gagné », ta réponse est "
    "probablement vague. Cette absence garantit que tu ne ressentiras jamais d'avoir gagné — quel que soit "
    "le montant atteint."
], GOLD, NAVY, accent=NAVY))

story.append(P("Le calcul de ton « assez »", h_sub))
story.append(styled_table([
    [C("Question", cell_g), C("À te poser honnêtement", cell_g)],
    [C("Dépenses mensuelles"),
     C("Combien je dépense par mois pour vivre comme je veux ? (loyer + chevaux + ATHÉNA + plaisirs)")],
    [C("Multiplicateur"),
     C("Règle standard : 25-30x les dépenses annuelles. Permet un retrait de 3-4% par an sans toucher au capital.")],
    [C("Capital cible"),
     C("Dépenses annuelles × 25-30. C'est ton « assez ».")],
    [C("Délai réaliste"),
     C("À quel horizon je peux y arriver ? 10 ans ? 15 ans ?")],
    [C("Plan"),
     C("Combien épargner/investir par mois pour y arriver dans ce délai ?")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 10))

story.extend(exercice([
    "<b>Le calcul de ton « assez ».</b> Cette semaine, prends 1 heure pour faire le calcul complet. Écris-le. "
    "C'est ton point d'ancrage à vie.",
    "<b>Le test de la liberté.</b> Demande-toi : « si j'avais atteint mon "
    "&laquo;assez&raquo; demain, qu'est-ce que je ferais de ma vie ? » Si la réponse est « la même chose » ou "
    "« je sais pas », tu es en train de fuir une vie que tu n'as pas conçue."
]))
story.extend(phrase_ancre(
    "« Sans 'assez' défini, je cours après l'infini. Je définis. Je sais où je vais. »"
))
story.append(PageBreak())


# --- CONCEPT 5 ---
story.extend(concept_header(5, "Acheter du temps, pas des choses", ACCENT))
story.extend(retenir(
    "La vraie utilité de l'argent qui dépasse les biens : la LIBERTÉ de choisir comment tu utilises ton temps. "
    "Pouvoir dire non à un travail qui ne te plaît plus. Pouvoir consacrer 3 mois à un projet sans pression. "
    "Cette liberté distingue richesse vécue et richesse comptable."
))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as 25 ans. Si tu construis une fortune à 40 en sacrifiant 15 ans de temps libre, sans aller en "
    "compétition, sans ATHÉNA pour ses qualités propres, sans investir dans ta relation à ta filly — ces 15 ans "
    "ne reviendront pas. L'argent gagné ne pourra pas les racheter. À l'inverse, si tu choisis dès maintenant "
    "une vie mêlant progression financière raisonnable ET temps de qualité, tu cumules les deux."
], GOLD, NAVY, accent=NAVY))

story.append(P("Rendement bonheur des dépenses", h_sub))
story.append(styled_table([
    [C("Type de dépense", cell_g), C("Rendement bonheur", cell_g)],
    [C("Voiture premium"), C("Faible. Adaptation 3-6 mois.")],
    [C("Maison plus grande"), C("Faible. Adaptation 6-12 mois.")],
    [C("Statut social"), C("Très faible. Adaptation en jours.")],
    [C("Temps libre supplémentaire"), C("Très fort. Pas d'adaptation.")],
    [C("Expériences avec proches"), C("Très fort. Renforcé par la mémoire.")],
    [C("Liberté de choix professionnel"), C("Très fort. Permanent.")],
    [C("Santé (sport, qualité de vie)"), C("Très fort. Cumulé.")],
    [C("Apprentissage / développement"), C("Fort. Cumulé.")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu gagnes 6000€. Tu retires 50% (3000€) vers ton compte épargne stratégique. Tu utilises "
    "1500€ pour une expérience qui compte : 4 jours en montagne avec un proche, un stage intensif d'équitation "
    "avec un grand maître. Tu gagnes du patrimoine ET de la mémoire/compétence. Les deux capitalisent."
]))

story.extend(exercice([
    "<b>Audit des dépenses de l'année.</b> Liste tes 10 plus grosses dépenses (hors charges fixes). Pour chaque, "
    "évalue 1-10 ton rendement bonheur 6 mois après. Tu vas voir : majorité = mauvais investissement de bonheur.",
    "<b>La règle « temps avant chose ».</b> Pendant 12 mois, priorise toute dépense discrétionnaire vers les "
    "catégories à fort rendement (temps libre, expériences, santé, relations, apprentissage)."
]))
story.extend(phrase_ancre(
    "« L'argent gagne sa valeur quand il achète du temps, du sens, de la liberté. Pas des choses. »"
))
story.append(PageBreak())


# --- CONCEPT 6 ---
story.extend(concept_header(6, "Le risque de ruine — la math que tu ignores", ACCENT))
story.extend(retenir(
    "Le risque de ruine est la probabilité MATHÉMATIQUE que ta série de trades te ruine à long terme. Cette "
    "probabilité dépend de trois variables : ton win rate, ton ratio gain/perte, et ton risque par trade. "
    "Tu peux la calculer. Si elle est > 1%, ton compte va exploser tôt ou tard — mathématiquement."
))
story.extend(explication([
    "<b>La formule simplifiée.</b> Si tu risques 5% par trade avec un edge de 55% et un RR 1:1, ton risque "
    "de perdre 50% du compte sur une série est massif. Si tu risques 0,5% avec le même edge, ton risque "
    "tombe à quelques pourcents. La taille de risque par trade est la variable la plus puissante de toutes — "
    "plus que ton edge.",
    "<b>Le paradoxe contre-intuitif.</b> Réduire ton risque par trade de moitié ne divise pas tes gains "
    "par deux — il les divise par environ 1,3 à 1,5 sur le long terme, parce que tu cessés de subir les "
    "drawdowns destructeurs. Plus tu réduis le risque par trade, plus ta courbe de capital devient lisse, "
    "plus tu peux composer durablement."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu risques probablement 1-3% par trade (peut-être plus quand tu pousses). Avec ton win rate réel "
    "(probablement 40-55%) et ton RR réel (probablement perturbé par les décalages et pushs), ton risque "
    "de ruine est très probablement > 30%. Mathématiquement, sans changer ces variables, tu vas continuer "
    "à cramer des comptes. Ce n'est pas la discipline qui manque — c'est l'arithmétique."
], GOLD, NAVY, accent=NAVY))

story.append(P("Effet du risque par trade sur la stabilité du capital", h_sub))
story.append(styled_table([
    [C("Risque/trade", cell_g), C("Edge 55% RR 1:2", cell_g), C("Effet long terme", cell_g)],
    [C("3%"), C("Drawdowns -40% fréquents"), C("Risque de ruine élevé")],
    [C("2%"), C("Drawdowns -25% possibles"), C("Risque modéré")],
    [C("1%"), C("Drawdowns -15% rares"), C("Risque faible")],
    [C("0,5%"), C("Drawdowns -8% rares"), C("Risque quasi nul, croissance lente mais sûre")],
    [C("0,25%"), C("Drawdowns -5% très rares"), C("Quasi indestructible. Croissance très lente.")],
], [3.5*cm, 6*cm, 6.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu fixes ton risque par trade à 0,5% MAXIMUM. Pour un compte de 50K, ça représente 250$ "
    "par trade. Tu trouves ça « trop peu » ? C'est précisément le problème. Tu confonds amplitude et "
    "compétence. À 0,5%, sur 1000 trades à edge positif, ton capital grandit MASSIVEMENT par composition. "
    "Tu lis Partie 9 concept 2 pour t'en rappeler."
]))

story.extend(exercice([
    "<b>Calcul de ton risque de ruine actuel.</b> Outils gratuits en ligne (chercher « risk of ruin calculator »). "
    "Entre ton win rate réel, ton RR réel, ton risque par trade actuel. Tu vas voir le chiffre.",
    "<b>Re-paramétrage strict.</b> Risk par trade fixé à 0,5%. Pas modifiable. Pas négociable. Pendant 100 "
    "trades. Tu vas voir : tes pertes sont gérables, tes gains sont consistants, ta courbe se lisse."
]))
story.extend(phrase_ancre(
    "« Mon risque par trade est la variable la plus puissante. Je la fixe bas, je laisse la composition agir. »"
))
story.append(PageBreak())


# --- CONCEPT 7 ---
story.extend(concept_header(7, "Prop firms et patience structurelle", ACCENT))
story.extend(retenir(
    "Les prop firms sont conçues pour récompenser la patience structurelle et punir l'impatience. Leurs "
    "règles favorisent statistiquement les traders qui prennent peu de risque, exécutent constamment, "
    "encaissent les gains progressivement. Si tu te plies à cette logique au lieu de la combattre, tu "
    "passes du côté des 5-10% qui réussissent."
))
story.extend(explication([
    "<b>La logique du business model.</b> Les prop firms gagnent quand les traders échouent (commissions "
    "d'évaluation, comptes cramés). Elles perdent quand un trader devient consistent et empoche des payouts "
    "réguliers. Donc structurellement, leurs règles SONT le filtre qui sépare l'impatient (qui paye des "
    "frais) du patient (qui touche des payouts). La règle est l'opposante du saboteur, pas la tienne.",
    "<b>Le pattern du trader patient en prop firm.</b> Petits gains réguliers. Respect strict du drawdown. "
    "Sessions courtes (1-3 trades par jour max). Payouts réguliers sortis et sécurisés en compte personnel. "
    "Ce trader est INVISIBLE sur les réseaux sociaux. Il ne fait pas le buzz. Il fait de l'argent."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu as vu probablement les comptes Twitter/Instagram avec « +$15 000 today on $50K Apex ». Tu as cru que "
    "c'était le modèle à reproduire. C'est en réalité l'EXCEPTION dopaminergique mise en avant — la majorité "
    "des grosses journées finit en compte cramé la semaine suivante. Les traders prop firm qui durent font "
    "$300-500 par jour, sortent en payout dès qu'ils peuvent, et restent. Tu veux être visible — ou tu veux être riche ?"
], GOLD, NAVY, accent=NAVY))

story.append(P("Patience structurelle en prop firm", h_sub))
story.append(styled_table([
    [C("Comportement saboteur", cell_g), C("Comportement patient", cell_g)],
    [C("Viser le grand payout en 1-2 mois"), C("Viser le 1er payout dès qu'autorisé")],
    [C("Pousser le compte au max permis"), C("Garder 50% de marge sur drawdown")],
    [C("Trader chaque jour pour « profiter »"), C("Trader 2-3 fois/semaine, A+ uniquement")],
    [C("Réinvestir 100% des gains"), C("Sortir 70% des payouts vers personnel")],
    [C("Acheter un nouveau compte après crash"), C("Pause 4 semaines, analyse, reprise lente")],
], [7.5*cm, 8.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu trades comme si le compte était PRÉCIEUX (parce qu'il l'est : il a coûté en frais "
    "d'inscription + temps + énergie). Tu ne le risques pas pour un « gros coup ». Tu vises la durée. "
    "Plus le compte vit, plus tu peux composer ses gains."
]))

story.extend(exercice([
    "<b>Re-calibration des objectifs.</b> Au lieu de « je veux faire +$5000 ce mois », vise « je veux que "
    "mon compte ait survécu intact dans 6 mois, avec un payout mensuel régulier de $500-800 ». Objectif "
    "qui change tout.",
    "<b>Audit des derniers comptes cramés.</b> Combien aurais-tu gagné en restant patient ? Si tu avais "
    "fait $500/mois pendant 12 mois sur chaque compte = $6000 par compte × N comptes. La patience aurait "
    "rapporté MASSIVEMENT plus que tes coups."
]))
story.extend(phrase_ancre(
    "« Les prop firms récompensent la patience structurelle. Je joue leur jeu, pas contre. »"
))
story.append(PageBreak())


# --- CONCEPT 8 ---
story.extend(concept_header(8, "L'obsession du gros payout vs les micro-victoires", ACCENT))
story.extend(retenir(
    "Tu cherches le gros payout qui change tout. C'est ton fantasme — payer une voiture, partir en voyage, "
    "prouver à tout le monde. Cette obsession est la matrice de ton problème. La richesse réelle se "
    "construit en MICRO-VICTOIRES répétées des milliers de fois — pas en gros coups."
))
story.extend(explication([
    "<b>Le mythe du gros coup.</b> Les médias trading et les réseaux sociaux glorifient le gros coup ("
    "« +$50K en une session »). C'est ce qui fait l'audience. Statistiquement, la grosse majorité de ces "
    "gros coups est : (a) suivi de pertes massives qui annulent tout, (b) attribuable à de la chance non "
    "reproductible, ou (c) carrément faux/exagéré. Les vrais riches du trading construisent par milliers "
    "de petits gains.",
    "<b>La réalité de la construction.</b> Un trader qui fait $500 par jour, 200 jours par an, fait $100K "
    "par an. Sur 10 ans, en composant intelligemment, il peut devenir multi-millionnaire. Sans drama. "
    "Sans Twitter. Avec une vie équilibrée. C'est ennuyeux à raconter. C'est ce qui marche."
]))
story.extend(make_callout("◈  CHEZ TOI", [
    "Tu portes probablement le fantasme du gros payout qui efface tes échecs. Si tu fais +$30K en une "
    "session, tu effaces 6 mois de pertes, tu prouves à tout le monde, tu reconstruis ton estime. C'est "
    "compréhensible — mais c'est précisément le piège. Ce fantasme te pousse à prendre les risques qui te "
    "détruisent. La sortie n'est pas dans le gros payout — elle est dans l'abandon de ce fantasme."
], GOLD, NAVY, accent=NAVY))

story.append(P("Reprogrammation : du gros payout aux micro-victoires", h_sub))
story.append(styled_table([
    [C("Ancien objectif", cell_g), C("Nouvel objectif", cell_g)],
    [C("Faire $10K en une session"), C("Faire $500 avec exécution propre")],
    [C("Doubler le compte en 2 mois"), C("Composer 1-2% par mois sur 5 ans")],
    [C("Tweeter mes gros gains"), C("Remplir mon journal de mes 100 trades")],
    [C("Acheter une voiture symbolique"), C("Augmenter mon compte épargne de $X")],
    [C("Devenir visible"), C("Devenir libre")],
], [7.5*cm, 8.5*cm]))
story.append(Spacer(1, 10))

story.extend(application([
    "<b>Cible :</b> tu te récompenses non pas pour le gros payout, mais pour les MICRO-VICTOIRES quotidiennes. "
    "« Aujourd'hui j'ai respecté mon SL. C'est une victoire. » « J'ai pris mon payout mensuel modeste mais "
    "régulier. C'est une victoire. » « J'ai fait 1% sur la semaine sans crisper. C'est une victoire. »"
]))

story.extend(exercice([
    "<b>Le journal des micro-victoires.</b> Une page dédiée. Chaque jour, 1 micro-victoire de trader notée. "
    "Petite, mais réelle. Sur 100 jours, tu auras 100 micro-victoires écrites. C'est ta richesse réelle.",
    "<b>Désintoxication des réseaux sociaux trading.</b> Pendant 90 jours, tu ne suis aucun trader « gros payout » "
    "sur Twitter/Instagram/YouTube. Tu te déprogrammes de l'image du gros coup. Tu te reprogrammes vers "
    "la patience."
]))
story.extend(phrase_ancre(
    "« La richesse se construit par milliers de micro-victoires. Pas en un gros payout. »"
))
story.append(PageBreak())


# --- SYNTHÈSE PARTIE 9 ---
story.append(P("Carte mentale — Partie 9", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Patience financière",
    [
        {"label": "PRINCIPES", "leaves": ["chance + risque massifs", "composition long terme", "durée > amplitude"], "color": NAVY},
        {"label": "DEUX COMPÉTENCES", "leaves": ["faire de l'argent (optimisme)", "garder (paranoïa adaptative)"], "color": ACCENT},
        {"label": "BOUSSOLE", "leaves": ["définir 'assez'", "marge de sécurité", "acheter du temps"], "color": GREEN},
    ], accent=ACCENT
)))
story.append(P("Joue la durée → cumule les compétences → définis ton « assez ».", caption))
story.append(Spacer(1, 10))

story.append(P("Fiche finale à imprimer — Partie 9", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║  PATIENCE FINANCIÈRE — FICHE D'ANCRAGE                    ║
║                                                            ║
║  DANGER PRINCIPAL                                          ║
║    Course à l'infini sans cible.                           ║
║    Vivre au niveau des gains.                              ║
║    Confondre série de chance et compétence.               ║
║                                                            ║
║  SIGNAL D'ALERTE                                           ║
║    - Aucun montant ne te semble « assez »                  ║
║    - Tu réinvestis 100% des gains en trading               ║
║    - Tes dépenses suivent tes revenus exactement           ║
║    - Pas de coussin de sécurité                            ║
║                                                            ║
║  ACTION IMMÉDIATE                                          ║
║    1. Calculer « assez » : dépenses annuelles × 25-30      ║
║    2. Sortir 30-50% des gains mensuels                     ║
║    3. Maintenir 6-12 mois de dépenses en coussin           ║
║    4. Diversifier (trading + ATHÉNA + LT)                  ║
║    5. Privilégier temps et expériences sur biens           ║
║                                                            ║
║  RÈGLE                                                     ║
║    Objectif : 0,5-1% par semaine moyenne sur 12 mois.      ║
║    Pas 30% par mois ambitieux mais insoutenable.           ║
║    Retrait automatique mensuel vers épargne.               ║
║                                                            ║
║  PHRASE D'ANCRAGE                                          ║
║    « Je joue 30 ans, pas 30 jours. »                       ║
╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))
story.append(PageBreak())


# ============================================================
# CONCLUSION GÉNÉRALE
# ============================================================
_part_color[0] = GOLD
_part_num[0] = None
_part_name[0] = ""

story.append(P("CONCLUSION GÉNÉRALE", h_part))
story.append(P("Intégrer les 9 parties dans une vie", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Si tu as lu jusqu'ici, tu portes maintenant un système complet de transformation. 9 dimensions du même "
    "problème : psychologie de la perte, dopamine, trauma, décharge somatique, pensée probabiliste, limites "
    "du corps, habitudes, lâcher-prise, rapport à l'argent. Aucune partie seule ne te transforme. C'est "
    "l'INTÉGRATION des 9 qui produit le changement."
))
story.append(P(
    "L'intégration ne se fait pas en lisant. Elle se fait en VIVANT les 9 parties au quotidien, sur des années. "
    "Le manuel est une carte. Le territoire, c'est ta vie."
))

story.append(P("Les 9 phrases d'ancrage à imprimer ensemble", h_section))
story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║              LES 9 PHRASES D'ANCRAGE                      ║
║                                                            ║
║  P1.  "Je joue ma série de 100. Pas ce trade-ci.          ║
║        Couper au SL est une victoire."                     ║
║                                                            ║
║  P2.  "Chaque pic produit un creux.                        ║
║        Je n'alimente pas le creux par un autre pic."       ║
║                                                            ║
║  P3.  "Je soigne par le corps.                             ║
║        C'est là que mon trauma est stocké."                ║
║                                                            ║
║  P4.  "Goutte par goutte.                                  ║
║        Mon corps se libère à son rythme."                  ║
║                                                            ║
║  P5.  "Je joue 100. Celui-ci ne dit rien sur mon edge."    ║
║                                                            ║
║  P6.  "Je vaux. Indépendamment de ce que je produis."      ║
║                                                            ║
║  P7.  "1% par jour. Pendant 365 jours."                    ║
║                                                            ║
║  P8.  "Je contrôle mes gestes. Je lâche les résultats."    ║
║                                                            ║
║  P9.  "Je joue 30 ans, pas 30 jours."                      ║
║                                                            ║
║  RECETTE                                                   ║
║    1 phrase / jour, le matin.                              ║
║    Tu tournes sur les 9 toutes les 9 jours.                ║
║    Sur 12 mois, chaque phrase est intégrée ~40 fois.       ║
╚══════════════════════════════════════════════════════════╝
""", accent=GOLD))
story.append(PageBreak())


# ============================================================
# PLAN D'APPLICATION 30 JOURS
# ============================================================
story.append(P("PLAN D'APPLICATION 30 JOURS", h_part))
story.append(P("Le démarrage concret — semaine par semaine", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce plan installe les fondations en 30 jours. Pas plus, pas moins. À la fin, tu auras les routines en "
    "place pour le plan 12 mois qui suit."
))

story.append(P("Semaine 1 — Sevrage et fondations", h_section))
story.append(styled_table([
    [C("Domaine", cell_g), C("Action", cell_g)],
    [C("Trading"), C("ARRÊT TOTAL. Aucun trade. Aucun chart. Apps désinstallées du téléphone.")],
    [C("Lecture"), C("Lire Partie 1 + 2. Faire les exercices.")],
    [C("Cahier"), C("Acheter un cahier. Page 1 manuscrite : « Cahier de Marien, trader chirurgical en formation. »")],
    [C("Corps"), C("Cold shower 2 min chaque matin. Pas négociable.")],
    [C("Sport"), C("3 séances intenses (box, équitation, course).")],
    [C("Méditation"), C("10 min/jour minimum.")],
    [C("Praticien somatique"), C("Recherche + 1 RDV pris dans la semaine.")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 10))

story.append(P("Semaine 2 — Conscience corporelle", h_section))
story.append(styled_table([
    [C("Domaine", cell_g), C("Action", cell_g)],
    [C("Trading"), C("Toujours zéro. Sevrage strict.")],
    [C("Lecture"), C("Lire Partie 3 + 4. Faire les exercices.")],
    [C("Cahier"), C("Scan corporel matin + soir, noter dans le cahier.")],
    [C("Corps"), C("Pansage conscient avec ta filly 1 fois cette semaine, 30 min min.")],
    [C("Sport"), C("3 séances + 1 séance somatique exploratoire.")],
    [C("Émotionnel"), C("15 min/jour expression émotionnelle (à voix ou par écrit).")],
    [C("Praticien"), C("1ère séance SE/EMDR effectuée si possible.")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 10))

story.append(P("Semaine 3 — Reprise contrôlée et probabiliste", h_section))
story.append(styled_table([
    [C("Domaine", cell_g), C("Action", cell_g)],
    [C("Trading"), C("Reprise DÉMO uniquement. 1-2 setups A+ par jour MAX. Protocole strict.")],
    [C("Lecture"), C("Lire Partie 5 + 6. Faire les exercices.")],
    [C("Pré-trade"), C("Visualisation 90s OBLIGATOIRE avant chaque trade démo.")],
    [C("Journal"), C("Double notation pour chaque trade : PnL + Discipline OUI/NON.")],
    [C("5 vérités"), C("Récitation matinale obligatoire.")],
    [C("« Non »"), C("5 non par semaine en pratique sociale.")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 10))

story.append(P("Semaine 4 — Habitudes et lâcher", h_section))
story.append(styled_table([
    [C("Domaine", cell_g), C("Action", cell_g)],
    [C("Trading"), C("Démo + bilan complet de la semaine 3. Aucune modification de méthode.")],
    [C("Lecture"), C("Lire Partie 7 + 8 + 9. Faire les exercices.")],
    [C("Habitude"), C("Choisir UNE habitude version 2 min. L'empiler sur une habitude existante.")],
    [C("Lâcher"), C("Pratique du protocole 6 étapes 1 fois/jour.")],
    [C("Argent"), C("Calculer ton « assez ». Ouvrir compte épargne dédié.")],
    [C("Bilan"), C("À J+30, bilan complet : qu'est-ce qui s'est installé ? qu'est-ce qui résiste ?")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 10))

story.extend(retenir(
    "À la fin des 30 jours, tu as posé les fondations. Tu n'es pas encore rentable — tu es PRÊT à l'être. "
    "C'est différent. Tu passes maintenant au plan 12 mois pour ancrer durablement."
))
story.append(PageBreak())


# ============================================================
# PLAN D'APPLICATION 12 MOIS
# ============================================================
story.append(P("PLAN D'APPLICATION 12 MOIS", h_part))
story.append(P("L'ancrage durable — mois par mois", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Après les 30 jours de fondations, tu entres dans le cycle long. Une thématique par mois. À la fin de "
    "12 mois, tu es transformé."
))

story.append(P(
    "Chaque mois a sa thématique, ses objectifs précis, ses métriques de validation, ses signaux d'alerte et "
    "ses critères de passage. Tu ne progresses au mois suivant que si les critères du mois en cours sont "
    "remplis. Si non, tu refais le mois. Ce n'est pas une punition — c'est de l'ingénierie."
))
story.append(PageBreak())


def mois_block(num, theme, objectifs, metriques, alertes, passage):
    out = []
    out.append(P(f"MOIS {num}", small_label))
    out.append(P(theme, h_concept))
    out.append(GoldRule(thickness=0.8))
    out.append(Spacer(1, 6))
    out.append(P("Objectifs concrets", h_sub))
    for o in objectifs:
        out.append(P("•  " + o, body))
    out.append(P("Métriques de validation", h_sub))
    for m in metriques:
        out.append(P("•  " + m, body))
    out.append(P("Signaux d'alerte (à corriger immédiatement)", h_sub))
    for a in alertes:
        out.append(P("•  " + a, body))
    out.append(P("Critères de passage au mois suivant", h_sub))
    for p in passage:
        out.append(P("✓  " + p, body))
    out.append(PageBreak())
    return out


story.extend(mois_block(1, "Sevrage et fondations",
    objectifs=[
        "Arrêt total du trading pendant 30 jours (aucun trade, démo ou réel).",
        "Désinstallation des apps de trading du téléphone. Mot de passe TradingView donné à un proche.",
        "Mise en place des routines de base : cold shower quotidien, méditation 20 min/jour, sport 3x/sem.",
        "Achat du cahier sérieux et première page manuscrite.",
        "Premier contact avec un praticien somatique (SE / EMDR) — RDV pris.",
    ],
    metriques=[
        "30 jours consécutifs sans aucun trade.",
        "Cold shower ≥ 25/30 jours.",
        "Méditation ≥ 25/30 jours.",
        "Journal manuscrit rempli ≥ 25/30 jours.",
        "1 RDV pris (et idéalement honoré) avec praticien somatique.",
    ],
    alertes=[
        "Tu ouvres une plateforme « juste pour voir » → reset du compteur de jours.",
        "Tu compenses par alcool/sucre/écrans excessifs → ce n'est pas un sevrage, c'est un déplacement.",
        "Tu reproches au temps qui passe d'être lent → résistance, pas progrès.",
    ],
    passage=[
        "30 jours sans trade complets.",
        "Au moins 4 pratiques quotidiennes installées comme automatismes (sans effort de volonté).",
        "Praticien somatique au moins contacté.",
    ],
))

story.extend(mois_block(2, "Reconstruction du baseline dopaminergique",
    objectifs=[
        "Maintien strict du sevrage trading.",
        "Inconfort volontaire intensifié : douche froide quotidienne (étendue à 5 min), 2 séances HIIT/sem.",
        "Substitution active des comportements compensatoires (alcool, scroll, sucre, écrans excessifs).",
        "Pratique 5×/jour de respiration 4-6 — installation comme automatisme.",
        "Pansage conscient avec ta filly : 1 fois/sem minimum, 45 min, sans téléphone.",
    ],
    metriques=[
        "Baseline énergétique évalué quotidiennement 1-10. Moyenne sur 30 jours ≥ 7/10.",
        "Substituts toxiques (alcool/scroll/sucre) réduits de 70%+ vs mois 1.",
        "Pansage conscient ≥ 4 fois dans le mois.",
        "Test du baseline : plaisirs simples reviennent (repas, lecture, marche).",
    ],
    alertes=[
        "Tu te dis « le calme est encore vide » → SN encore en tolérance. Ne reviens pas au trading.",
        "Tu commences à scroller du contenu trading « pour rester à jour » → fuite déguisée.",
        "Tu te sens vidé/déprimé chronique → consulte. Possible décompensation post-sevrage.",
    ],
    passage=[
        "Plaisirs simples (marche, repas calme) procurent ≥ 6/10 de satisfaction.",
        "Sevrage maintenu intact sur 60 jours cumulés (mois 1 + mois 2).",
        "Au moins 1 séance avec praticien somatique effectuée.",
    ],
))

story.extend(mois_block(3, "Travail somatique et SN",
    objectifs=[
        "Toujours pas de trading. Sevrage prolongé à 90 jours total.",
        "Praticien somatique : 1 séance toutes les 2 semaines (2 séances ce mois).",
        "Scan corporel matin et soir installé comme automatisme (sans rappel nécessaire).",
        "Cartographie quotidienne SN (V/S/D à 8h, 12h, 16h, 20h) pendant tout le mois.",
        "Bilan neuropsychologique post-TBI prescrit (idéalement passé dans le mois).",
    ],
    metriques=[
        "Sevrage trading total ≥ 90 jours.",
        "2 séances somatiques effectuées.",
        "Score moyen sympathique sur la journée (sur 0-10) en baisse mesurable vs mois 1-2.",
        "Sommeil ≥ 7h en moyenne, sentiment de récupération amélioré.",
    ],
    alertes=[
        "Le travail somatique réveille des émotions fortes → c'est attendu. Pas raison d'arrêter.",
        "Tu sens « ça ne sert à rien » → résistance classique au travail corporel. Continuer.",
        "Insomnies aggravées sur > 7 jours → en parler au praticien.",
    ],
    passage=[
        "État SN baseline majoritairement V ou S calme (pas S élevé).",
        "Reconnaissance fluide des signaux corporels précoces.",
        "Engagement de continuer le travail somatique sur les 9 mois suivants.",
    ],
))

story.extend(mois_block(4, "Décharge somatique et intégration",
    objectifs=[
        "Reprise possible du trading en DÉMO uniquement à partir de la 3e semaine du mois.",
        "Pratique active de la pendulation (1 fois/jour minimum).",
        "Exploration hebdomadaire d'un mouvement inachevé (push/pull/reach/run/voice).",
        "Sortie nature 1 fois/sem (90 min sans téléphone).",
        "Lecture du manuel — parties 1 et 2 — relue et annotée.",
    ],
    metriques=[
        "Démo : minimum 20 trades exécutés selon protocole strict (SL/TP préfixés, BE+1R, plateforme fermée).",
        "Zéro décalage de SL en démo.",
        "Pendulation pratiquée ≥ 25 jours sur 30.",
        "Capacité à sentir une émotion 90 sec sans agir sur elle (testée plusieurs fois).",
    ],
    alertes=[
        "Tu sautes la démo et veux passer en réel → c'est de l'impatience, signal rouge.",
        "Tu modifies ton protocole en démo → reset l'engagement.",
        "Tu te dis « la démo c'est pas pareil que le réel » → vrai, mais c'est exprès. Tiens.",
    ],
    passage=[
        "20+ trades démo exécutés selon protocole exact, sans aucune dérogation.",
        "Sensation de fluidité corporelle vs début du mois.",
        "Carnet du lâcher actif (1 entrée/jour minimum).",
    ],
))

story.extend(mois_block(5, "Pensée probabiliste et exécution",
    objectifs=[
        "Trading réel autorisé : UN seul compte prop firm, le plus petit possible (ex : Apex 25K).",
        "Risque par trade : 0,5% MAXIMUM. Non négociable.",
        "Méthode de trading entièrement écrite sur A4 (mode systématique).",
        "Récitation matinale des 5 vérités, installée comme automatisme.",
        "Premier groupe de 100 trades commencé — grille de suivi visuel au mur.",
    ],
    metriques=[
        "Réel : minimum 30 trades exécutés selon protocole.",
        "Zéro décalage de SL. Zéro modification de méthode.",
        "Journal pré + post session rempli 100% des sessions de trading.",
        "Score quotidien d'exécution (OUI/NON) — minimum 90% OUI.",
    ],
    alertes=[
        "Tu rates UN scan corporel pré-session → laisse-toi un strike. Deux strikes consécutifs → pause 48h.",
        "Tu prends un trade en colère / fatigué / euphorique → reset compteur série.",
        "Tu te compares à des comptes Twitter qui font « +$10K » → désintoxication immédiate des réseaux.",
    ],
    passage=[
        "30+ trades réels selon protocole strict.",
        "Compteur d'extinction « sans décalage SL » à 30 sessions consécutives.",
        "Vivre un trade perdant sans drama émotionnel notable.",
    ],
))

story.extend(mois_block(6, "Limites du corps et modulation",
    objectifs=[
        "Continuation trading réel sur le même compte. Aucune augmentation de risque.",
        "Audit complet de ta charge totale (trading + ATHÉNA + équitation + relations). Identification des excès.",
        "Pratique du « non » : 5 « non » concrets par semaine, dont au moins 1 « non à toi-même ».",
        "Jour OFF hebdomadaire complet — non négociable. Pas un demi-jour. Une journée entière.",
        "Une vraie pause de 3-5 jours sur le mois (vacances OFF totales).",
    ],
    metriques=[
        "5 non par semaine sur 4 semaines = 20 non documentés.",
        "1 jour OFF par semaine respecté ≥ 4 fois.",
        "1 pause longue 3-5 jours effectuée.",
        "Score moyen de récupération (sommeil, énergie, irritabilité) en amélioration.",
    ],
    alertes=[
        "Tu te dis « j'ai pas le temps de prendre une journée OFF » → c'est exactement le pattern à casser.",
        "Tu utilises le jour OFF pour bosser ATHÉNA en cachette → c'est pas un jour OFF.",
        "Tensions corporelles chroniques (mâchoire, épaules) persistent → continuer travail somatique.",
    ],
    passage=[
        "Capacité à dire 5 non/sem sans culpabilité massive.",
        "Jour OFF intégré dans la semaine comme évident.",
        "Sentiment de récupération mesurable post-pause longue.",
    ],
))

story.extend(mois_block(7, "Habitudes et automatisation",
    objectifs=[
        "Audit complet des 8 habitudes-clés (cf. master index). Lesquelles sont automatisées ? Lesquelles demandent encore de la volonté ?",
        "Choix d'UNE habitude prioritaire à automatiser sur le mois — empilement sur déclencheur existant.",
        "Première lecture (à partir d'un livre de la bibliographie) — 1 livre dans le mois.",
        "Continuation du compte prop firm. Premier payout sollicité si atteignable selon règles.",
        "Mise en place du système anti-rechute personnel (plan 6 étapes écrit, en portefeuille).",
    ],
    metriques=[
        "Premier livre de la bibliographie lu et annoté avec tes propres notes.",
        "Une habitude nouvelle installée comme automatisme (30 jours consécutifs).",
        "Plan anti-rechute écrit, signé, présent physiquement sur toi.",
        "Si éligible : premier payout reçu sur compte prop firm.",
    ],
    alertes=[
        "Tu lis 3 livres en parallèle → c'est de la fuite dans la consommation. Un seul à la fois.",
        "Tu veux installer 3 habitudes en même temps → 2 vont échouer. Une seule.",
        "Tu veux ton payout entier transféré vers ton compte trading → règle 50/30/20.",
    ],
    passage=[
        "1 livre lu, 1 habitude automatisée, plan anti-rechute en place.",
        "Si applicable : 1 payout pris et SORTI vers compte personnel (pas tout réinvesti).",
        "Sens d'avoir installé du DURABLE, pas du temporaire.",
    ],
))

story.extend(mois_block(8, "Lâcher prise opérationnel",
    objectifs=[
        "Pratique quotidienne du protocole 6 étapes de lâcher prise.",
        "Identification de TES 2-3 moments-clés où tu n'arrives pas à lâcher (parmi les 7 moments du Concept 4 P8).",
        "Travail spécifique sur ces moments — pratique délibérée en démo si nécessaire.",
        "Continuation trading réel. Évaluation : suis-je passé en mode systématique stable ?",
        "Lecture du 2e livre de la bibliographie.",
    ],
    metriques=[
        "Protocole 6 étapes pratiqué quotidiennement ≥ 25/30 jours.",
        "Tes 2-3 moments-clés améliorés vs début du mois (autoévaluation honnête).",
        "Compteur d'extinction « sans décalage SL » à 60 sessions consécutives.",
        "Vivre un gros gain sans euphorie déstabilisante (testé au moins une fois).",
    ],
    alertes=[
        "Le lâcher reste un mot, pas une pratique → reviens au protocole 6 étapes par écrit.",
        "Tu reviens systématiquement aux mêmes 2-3 moments-clés sans progrès → besoin d'aide externe (coach, psy, praticien).",
        "Excitation post-gain qui reste 12h+ → SN encore peu modulé.",
    ],
    passage=[
        "Protocole 6 étapes intégré comme automatisme.",
        "Au moins UN des 2-3 moments-clés clairement amélioré.",
        "Une grosse journée gagnante traversée sans crash le lendemain.",
    ],
))

story.extend(mois_block(9, "Patience financière et structure",
    objectifs=[
        "Calcul officiel de ton « assez » (capital cible + délai + plan mensuel).",
        "Compte épargne dédié pleinement actif. Règle 50/30/20 appliquée à chaque payout.",
        "Audit du risque de ruine avec un calculateur en ligne — résultats inscrits.",
        "Calibrage : ton risque par trade reste à 0,5% MAX. Aucune augmentation.",
        "Lecture du 3e livre de la bibliographie.",
    ],
    metriques=[
        "« Assez » calculé et écrit dans le journal (nombre précis, délai précis).",
        "Compte épargne dédié contient au moins 1 versement provenant des payouts.",
        "Risque de ruine évalué et sous 5%.",
        "Sentiment de cohérence : « je sais où je vais ».",
    ],
    alertes=[
        "Tu repoussés le calcul de « assez » → c'est précisément la résistance à dissoudre.",
        "Tu te dis « 0,5% c'est trop peu » → re-lecture P9 concept 6 (risque de ruine).",
        "Tu compares ton compte épargne à des Twitter trader avec « 7 figures » → désintoxication.",
    ],
    passage=[
        "« Assez » défini, écrit, accepté.",
        "Premier versement vers épargne effectué.",
        "Calcul du risque de ruine documenté.",
    ],
))

story.extend(mois_block(10, "Consolidation et stabilité",
    objectifs=[
        "Trois mois d'application réelle continue (mois 5, 6, 7-8 ou équivalent). Bilan honnête.",
        "Audit complet des 9 parties — où en suis-je dans chacune ?",
        "Maintien strict de toutes les pratiques acquises.",
        "Lecture du 4e livre de la bibliographie.",
        "Test calibration scalping vs swing — si pas encore fait — appliqué cette semaine.",
    ],
    metriques=[
        "Tableau d'auto-évaluation 9 parties — score 1-10 par partie.",
        "Parties ≥ 7/10 : 6 sur 9 minimum.",
        "Aucune pratique fondamentale abandonnée.",
        "Compteur d'extinction « sans décalage SL » à 90 sessions consécutives.",
    ],
    alertes=[
        "Une pratique a été abandonnée sans que tu t'en rendes compte → revenir dessus.",
        "Tu commences à « connaître » le manuel par cœur et à zapper les exercices → relire le concept 1 de la P1.",
    ],
    passage=[
        "Auto-évaluation honnête : 6/9 parties à 7+/10.",
        "Stabilité globale notable vs il y a 6 mois.",
        "Sens d'identité différente — Marien-d'après commence à émerger.",
    ],
))

story.extend(mois_block(11, "Préparation au scaling — ou maintien",
    objectifs=[
        "Si stabilité confirmée sur les 6 derniers mois : possibilité d'AUGMENTER LÉGÈREMENT la taille (risque/trade de 0,5% → 0,75%, pas plus).",
        "Si instabilité ou rechutes : prolongation du mode actuel, pas de scaling.",
        "Décision honnête sur la base des METRIQUES, pas du désir.",
        "Renforcement des pratiques somatiques en parallèle du scaling.",
        "Lecture du 5e livre.",
    ],
    metriques=[
        "PnL sur 6 derniers mois en positif (modeste mais positif).",
        "Zéro crash de compte sur 6 mois.",
        "Compteur d'extinction « sans décalage SL » à 120+ sessions consécutives.",
        "Sentiment d'opérateur stable.",
    ],
    alertes=[
        "Tu scales par excitation, pas par évidence chiffrée → DANGER. Revenir en arrière.",
        "Tu sautes les pratiques somatiques parce que « ça va » → c'est exactement ce qui les fait revenir.",
    ],
    passage=[
        "Décision documentée : scaling ou maintien. Sans drame.",
        "Plan précis pour le mois 12.",
    ],
))

story.extend(mois_block(12, "Bilan, intégration, décision année 2",
    objectifs=[
        "Bilan complet sur 12 mois. Mesures chiffrées (PnL, drawdowns max, jours OFF respectés, séances somatiques, etc.).",
        "Relecture du manuel — sections les plus utilisées vs les moins utilisées.",
        "Décision année 2 : continuer le manuel comme référence ? Approfondir un thème ? Changer de style de trading ?",
        "Bilan identitaire : où en es-tu sur Marien-d'après ?",
        "Engagement année 2 écrit dans le journal.",
    ],
    metriques=[
        "Bilan financier précis (% de progression du capital, drawdowns, payouts).",
        "Bilan psychologique honnête (qualité du sommeil, état SN, vie hors écran).",
        "Bilan identitaire (sentiment de Marien-d'après vs Marien-en-reconstruction).",
        "Bilan relationnel (rapports proches, ouverture, vulnérabilité).",
    ],
    alertes=[
        "Tu juges l'année uniquement sur le PnL → la mesure est partielle.",
        "Tu veux « tout finir » en mois 12 → le travail continue. Le manuel reste un compagnon.",
    ],
    passage=[
        "Bilan complet écrit dans le journal — plusieurs pages.",
        "Engagement année 2 clair et réaliste.",
        "Sens d'avoir avancé — quel que soit le PnL.",
    ],
))


# ============================================================
# CHECKLIST FINALE AVANT TRADING
# ============================================================
story.append(P("CHECKLIST FINALE", h_part))
story.append(P("Avant chaque session de trading", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Cette checklist te garantit que tu n'ouvres une session que dans un état d'opérateur stable. À imprimer, "
    "afficher au mur, parcourir mentalement avant chaque session. Si une seule case ne peut pas être cochée, "
    "tu ne trades pas aujourd'hui."
))

story.extend(ascii_box("""
╔══════════════════════════════════════════════════════════╗
║         CHECKLIST PRÉ-TRADING — À COCHER MENTALEMENT     ║
║                                                            ║
║  CORPS                                                     ║
║    □  J'ai dormi 7-9h cette nuit                           ║
║    □  Mon état SN est V (calme) ou S (mobilisé propre)     ║
║    □  Je n'ai PAS bu d'alcool hier soir en excès           ║
║    □  J'ai fait du sport dans les 48 dernières heures      ║
║    □  Mâchoire, épaules, ventre : pas de tension forte     ║
║                                                            ║
║  MENTAL                                                    ║
║    □  J'ai médité 10-20 min ce matin                       ║
║    □  J'ai relu les 5 vérités                              ║
║    □  Je connais le setup A+ que je guette                 ║
║    □  Je sais quelle taille max je m'autorise              ║
║    □  Je suis prêt à perdre la somme prévue calmement      ║
║                                                            ║
║  PROTOCOLE                                                 ║
║    □  Mon protocole personnel est affiché au mur           ║
║    □  Si pas A+ aujourd'hui : je peux ne pas trader        ║
║    □  Plateforme fermée APRÈS ordres placés (engagement)   ║
║    □  Téléphone dans une autre pièce                       ║
║    □  Cahier ouvert, prêt à remplir                        ║
║                                                            ║
║  CONTEXTE                                                  ║
║    □  Pas de session après une grosse journée (gain/perte) ║
║    □  Pas de revanche d'une perte récente                  ║
║    □  Pas de désir de me prouver quelque chose             ║
║    □  Je vais traiter chaque trade comme une instance      ║
║       d'une distribution sur 100                           ║
║                                                            ║
║  IDENTITÉ                                                  ║
║    □  Je SUIS un trader chirurgical aujourd'hui            ║
║    □  Mon identité ne dépend pas du PnL d'aujourd'hui      ║
║    □  Couper au SL sera une victoire de discipline         ║
║    □  Couper au TP sera une victoire de discipline         ║
║                                                            ║
║  → Si une case ne peut pas être cochée : PAS DE TRADE.     ║
║    Pas par discipline rigide. Par lucidité.                ║
╚══════════════════════════════════════════════════════════╝
""", accent=GOLD))
story.append(PageBreak())


# ============================================================
# POUR ALLER PLUS LOIN — BIBLIOGRAPHIE RECOMMANDÉE
# ============================================================
_part_color[0] = GOLD
story.append(P("POUR ALLER PLUS LOIN", h_part))
story.append(P("Lectures recommandées sur les thèmes du manuel", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce manuel est un cours personnalisé original sur des concepts généraux de psychologie, neurosciences, "
    "psychologie du trauma, sciences comportementales et finance comportementale. <b>Il n'est pas un résumé, "
    "un dérivé ou un substitut des livres ci-dessous.</b> Les neuf ouvrages listés sont des références "
    "indépendantes que tu peux lire pour approfondir les thèmes que ce manuel aborde — chacune avec la voix "
    "propre de son auteur, ses anecdotes, sa structure argumentative."
))
story.append(P(
    "Ne t'attends pas à retrouver le contenu de mon manuel dans ces livres. Ne t'attends pas non plus à "
    "retrouver le contenu de ces livres dans mon manuel. Ce sont des chemins parallèles vers les mêmes "
    "territoires."
))
story.append(Spacer(1, 10))

bib_data = [
    [C("#", cell_g), C("Titre — Auteur", cell_g), C("Thème principal", cell_g)],
    [C("1"), C("Best Loser Wins — Tom Hougaard", cell_b),
     C("Psychologie du trader perdant et de la gestion de la perte.")],
    [C("2"), C("Un monde sous dopamine (Dopamine Nation) — Anna Lembke", cell_b),
     C("Neurochimie de l'addiction et de l'équilibre plaisir-douleur.")],
    [C("3"), C("Le corps n'oublie rien (The Body Keeps the Score) — Bessel van der Kolk", cell_b),
     C("Trauma, cerveau, corps. Référence en psycho-traumatologie.")],
    [C("4"), C("Réveiller le tigre (Waking the Tiger) — Peter Levine", cell_b),
     C("Somatic Experiencing — méthode de libération du trauma corporel.")],
    [C("5"), C("Trader dans la zone (Trading in the Zone) — Mark Douglas", cell_b),
     C("Psychologie du trader rentable et pensée probabiliste.")],
    [C("6"), C("Quand le corps dit non (When the Body Says No) — Gabor Maté", cell_b),
     C("Stress chronique, émotions refoulées, médecine psychosomatique.")],
    [C("7"), C("Un rien peut tout changer (Atomic Habits) — James Clear", cell_b),
     C("Architecture des habitudes et changement comportemental.")],
    [C("8"), C("Lâcher prise (Letting Go) — David R. Hawkins", cell_b),
     C("Régulation émotionnelle, acceptation, mécanisme du lâcher.")],
    [C("9"), C("La psychologie de l'argent (The Psychology of Money) — Morgan Housel", cell_b),
     C("Comportements financiers durables et patience patrimoniale.")],
]
story.append(styled_table(bib_data, [0.7*cm, 7.3*cm, 8*cm]))
story.append(Spacer(1, 12))

story.append(P("Comment intégrer ces lectures dans ton plan 12 mois", h_section))
story.append(P(
    "Tu peux intégrer ces lectures à raison d'<b>un livre par mois</b> pendant la deuxième moitié de ton plan "
    "12 mois (à partir du Mois 7, quand les fondations somatiques et identitaires sont posées). Avant le Mois 7, "
    "concentre-toi sur l'application des modules de ce manuel — pas sur l'ajout d'autres lectures. Tu serais en "
    "fuite dans la consommation de contenu (cf. Concept 1 de la Partie 1)."
))
story.append(P(
    "À partir du Mois 7 : tu choisis un livre par mois selon ton besoin du moment. Tu lis lentement. Tu prends "
    "tes propres notes manuscrites (cf. Concept 6 de la Partie 7). Tu confrontes tes notes à ce que tu as appris "
    "dans ce manuel. Tu enrichis. Tu ne remplaces pas."
))
story.append(P(
    "<b>Avertissement honnête :</b> ces 9 livres ne couvrent qu'une fraction de la littérature scientifique sur "
    "ces thèmes. Pour chacun, il existe des dizaines d'autres ouvrages également pertinents (Kahneman, Steenbarger, "
    "Porges, Brewer, Schultz, Duhigg, Bogle, etc.). Cette liste est un point de départ, pas une liste exhaustive.",
    body_i
))
story.append(PageBreak())


# ============================================================
# CARTE D'URGENCE — APRÈS UN CRASH DE COMPTE
# ============================================================
_part_color[0] = HexColor("#B33A3A")
_part_num[0] = None
_part_name[0] = "Carte d'urgence"

story.append(P("CARTE D'URGENCE", h_part))
story.append(P("Protocole post-crash — à imprimer et garder à portée", h_part_sub))
story.append(GoldRule(color=HexColor("#B33A3A")))
story.append(Spacer(1, 12))

story.append(P(
    "Tu vas cramer un compte. Pas peut-être — sur 12-24 mois, certainement, au moins une fois. C'est dans la "
    "distribution. Ce protocole te donne la séquence précise des 7 jours suivants. Imprime-le. Garde-le dans "
    "ton portefeuille ou collé au mur. Quand le moment arrive (et il arrivera), tu ne réfléchis pas — tu suis."
))
story.append(Spacer(1, 8))

story.append(P("60 PREMIÈRES MINUTES — Stabilisation immédiate", h_section))
story.append(styled_table([
    [C("Temps", cell_g), C("Action obligatoire", cell_g)],
    [C("0-5 min", cell_b),
     C("FERMER LA PLATEFORME. Téléphone autre pièce. AUCUNE tentative de se refaire. AUCUN message envoyé.")],
    [C("5-15 min", cell_b),
     C("SORTIR PHYSIQUEMENT. Marcher dehors. Pas écouter de musique. Juste marcher. Respiration ample.")],
    [C("15-30 min", cell_b),
     C("Eau froide visage / cold shower / contact eau froide. Activation parasympathique forcée.")],
    [C("30-45 min", cell_b),
     C("Manger quelque chose de simple (banane, fruits, eau). Stabiliser la glycémie.")],
    [C("45-60 min", cell_b),
     C("Allonger 5 min. Scan corporel. NOMMER l'émotion (honte/colère/tristesse/dégoût). Ne pas combattre.")],
], [1.8*cm, 14.2*cm]))
story.append(Spacer(1, 10))

story.extend(make_callout("⚠  INTERDICTIONS ABSOLUES — 24 PREMIÈRES HEURES",
    "Aucun trade. Aucun nouveau compte acheté. Aucune décision financière. Aucun message envoyé à un autre "
    "trader. Aucune analyse rétrospective. Aucun engagement de « plus jamais ». Aucun alcool en excès. "
    "Aucun ordre Amazon impulsif. RIEN d'irréversible.",
    HexColor("#B33A3A"), white, accent=GOLD))

story.append(P("JOUR 1 — Soir du crash", h_section))
story.append(styled_table([
    [C("Action", cell_g), C("Pourquoi", cell_g)],
    [C("Dire à au moins UNE personne de confiance"), C("La honte cachée grandit. La honte dite décroît.")],
    [C("Repas simple, hydraté, pas d'alcool"), C("Système nerveux déjà saturé, pas de toxique en plus.")],
    [C("Sport doux ou marche longue"), C("Décharge somatique. Pas sport intense — déjà fatigué.")],
    [C("Coucher tôt (avant 23h)"), C("Le sommeil consolide. Tu en as besoin.")],
    [C("Si insomnie : lecture papier"), C("Pas d'écran. Pas de re-rumination.")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 10))

story.append(P("JOURS 2-3 — Phase de descente", h_section))
story.append(P(
    "Ton SN va probablement basculer en vagal dorsal (vide, dissociation, fatigue lourde). C'est la "
    "conséquence de l'activation extrême précédente. <b>Ne combats pas cet état</b> — accompagne-le. C'est "
    "biologique, ça passera."
))
story.append(styled_table([
    [C("Action", cell_g), C("À faire / À éviter", cell_g)],
    [C("Maintenir routines de base", cell_b), C("Sommeil 8h+. Repas réguliers. Hydratation. Pas plus.")],
    [C("Sortie nature 1h/jour", cell_b), C("Forêt, parc, eau. Sans téléphone. Marche lente.")],
    [C("Présence animale", cell_b), C("Pansage filly, contact lent. Co-régulation passive.")],
    [C("NE PAS retourner à la plateforme", cell_b), C("Même pour « voir ». L'envie va revenir. Ne cède pas.")],
    [C("NE PAS lire de contenu trading", cell_b), C("Pas YouTube, pas Twitter, pas livre. Purge sensorielle.")],
    [C("Journal court le soir", cell_b), C("3-5 phrases. Pas plus. Pas d'analyse profonde encore.")],
], [4.5*cm, 11.5*cm]))
story.append(Spacer(1, 10))

story.append(P("JOURS 4-7 — Émergence et analyse", h_section))
story.append(styled_table([
    [C("Action", cell_g), C("Détail", cell_g)],
    [C("Reprise progressive de l'activité", cell_b),
     C("Sport, équitation, ATHÉNA. Pas trading.")],
    [C("Premier journal d'analyse (J5-J6)", cell_b),
     C("30 min max. Identifier : déclencheur, pattern, état corporel. Pas de flagellation.")],
    [C("Identifier UN ajustement", cell_b),
     C("Pas tout repenser. UN ajustement précis (taille, règle, seuil).")],
    [C("Engagement de reprise (J7)", cell_b),
     C("Date précise. Conditions précises. SI fatigué/instable → reporter d'une semaine.")],
], [5*cm, 11*cm]))
story.append(Spacer(1, 10))

story.extend(retenir(
    "Tu n'as pas à reprendre vite. Tu as à reprendre PROPRE. Une semaine de pause est moins coûteuse qu'une "
    "rechute mal préparée. Pas de héroïsme. Suis le protocole.",
    HexColor("#B33A3A")
))
story.append(PageBreak())


# ============================================================
# STYLE DE TRADING ET PHYSIOLOGIE
# ============================================================
_part_color[0] = GOLD
_part_name[0] = "Style de trading"

story.append(P("STYLE DE TRADING ET PHYSIOLOGIE", h_part))
story.append(P("Une question que tu n'as peut-être jamais posée", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Tu fais du scalping XAUUSD en killzones London et NY. C'est un style de trading qui te demande : "
    "(1) attention soutenue sur 1-3 heures, (2) prise de décision rapide, (3) tolérance à des micro-mouvements "
    "intenses, (4) gestion d'une charge dopaminergique très haute (chaque clic est un shoot d'anticipation). "
    "Question honnête : <b>est-ce que ce style est aligné avec ta physiologie post-TBI ?</b>"
))

story.append(P("Spectre des styles de trading", h_section))
story.append(styled_table([
    [C("Style", cell_g), C("Charge SN", cell_g), C("Aligné avec post-TBI ?", cell_g)],
    [C("Scalping (sec-min)"), C("TRÈS HAUTE"),
     C("Difficile. Hyper-stimulation. Risque de dérégulation amplifié.")],
    [C("Intraday (heures)"), C("HAUTE"),
     C("Possible mais demande une régulation SN solide.")],
    [C("Swing (jours)"), C("MOYENNE"),
     C("Plus adapté. Décisions plus lentes, moins d'adrénaline.")],
    [C("Position (semaines-mois)"), C("BASSE"),
     C("Très adapté. Décisions rares, basées sur analyse longue.")],
], [4*cm, 3*cm, 9*cm]))
story.append(Spacer(1, 10))

story.append(P("Ce que ça implique pour toi", h_section))
story.append(P(
    "Je ne te dis pas d'arrêter le scalping. Je te dis de te poser la question. Le scalping demande un SN "
    "<b>très bien régulé</b> — capacité à rester en sympathique productif sans déraper en hyper-activation, "
    "capacité à revenir vite au calme entre les trades. Ton SN post-TBI a probablement encore du mal avec cette "
    "modulation fine. Tu peux passer du calme au pic en 30 secondes — pas l'inverse aussi rapidement."
))
story.append(P(
    "Trois pistes à considérer honnêtement :"
))
story.append(styled_table([
    [C("Option", cell_g), C("Logique", cell_g)],
    [C("Maintenir le scalping", cell_b),
     C("Si tu travailles solidement la régulation SN (Parties 3-4) pendant 6-12 mois et que les patterns destructeurs s'éteignent, le style peut rester. Mais ça demande un travail somatique sérieux en parallèle.")],
    [C("Passer en intraday plus lent", cell_b),
     C("1-2 trades/jour sur timeframes plus larges (H1, H4). Moins de décisions, moins de stimulation, plus de temps entre les trades pour réguler. Probablement le meilleur compromis pour ton profil actuel.")],
    [C("Passer en swing trading", cell_b),
     C("1-3 trades/semaine sur D1. Décisions calmes, analyses profondes. Charge SN très basse. Compatible avec ATHÉNA, équitation, vie équilibrée. À considérer sérieusement.")],
], [4.5*cm, 11.5*cm]))
story.append(Spacer(1, 10))

story.extend(retenir(
    "Le « bon style de trading » n'est pas un absolu. C'est celui qui s'aligne avec ta physiologie ET ton edge "
    "technique. Pour quelqu'un avec un SN post-TBI cherchant à se réguler, un style plus lent peut être un "
    "ACCÉLÉRATEUR de progrès — pas un compromis."
))
story.append(Spacer(1, 8))

story.extend(exercice([
    "<b>Test de calibration honnête.</b> Pendant 4 semaines, fais une session de scalping ET une session de swing "
    "sur la même semaine. Pour chaque session : score d'état SN avant/après, qualité d'exécution, PnL. À la fin "
    "des 4 semaines, compare. Laquelle correspond mieux à ta physiologie ACTUELLE ? Tu pourras toujours revenir "
    "au scalping plus tard si tu veux. Mais teste."
]))
story.append(PageBreak())


# ============================================================
# RESSOURCES CONCRÈTES — FRANCE
# ============================================================
_part_color[0] = GOLD
_part_name[0] = "Ressources"

story.append(P("RESSOURCES CONCRÈTES", h_part))
story.append(P("Trouver les bons praticiens en France", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce manuel te recommande à plusieurs reprises de consulter un praticien somatique (SE, EMDR), un "
    "neuropsychologue, éventuellement un thérapeute spécialisé trauma. Voici les ressources concrètes pour "
    "passer de l'intention à l'action — parce que sans points de contact précis, tu vas remettre à plus tard."
))

story.append(P("Somatic Experiencing (SE) — pour ton TBI 2022", h_section))
story.append(styled_table([
    [C("Item", cell_g), C("Détail", cell_g)],
    [C("Annuaire officiel", cell_b),
     C("Association France SE / EASE (European Association for Somatic Experiencing). Recherche : « somatic experiencing france annuaire » sur moteur de recherche.")],
    [C("Praticien certifié", cell_b),
     C("Cherche un praticien ayant fait l'intégralité du cursus SE (3 ans). Pas un praticien qui a juste fait une formation de week-end.")],
    [C("Prix indicatif", cell_b),
     C("70-110€ la séance d'1h en province. 100-150€ en région parisienne.")],
    [C("Rythme typique", cell_b),
     C("1 séance par 2-3 semaines. Travail sur 12-24 mois pour un trauma majeur.")],
    [C("Couverture mutuelle", cell_b),
     C("La SE n'est généralement pas remboursée par la Sécu. Certaines mutuelles remboursent partiellement (vérifie ton contrat — rubrique « médecines douces » ou « ostéopathie »).")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.append(P("EMDR — alternative ou complément", h_section))
story.append(styled_table([
    [C("Item", cell_g), C("Détail", cell_g)],
    [C("Annuaire officiel", cell_b),
     C("Association EMDR France — site officiel avec annuaire géographique des praticiens certifiés.")],
    [C("Praticien certifié", cell_b),
     C("Certification Niveau 1 ou Niveau 2. Beaucoup de psychologues/psychiatres se sont formés. Vérifie la certification.")],
    [C("Prix indicatif", cell_b),
     C("60-100€ la séance. Si fait par psychiatre conventionné, partiellement remboursé Sécu.")],
    [C("Rythme typique", cell_b),
     C("1 séance par semaine au début, puis tous les 15 jours. 10-25 séances pour un trauma défini.")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.append(P("Bilan neuropsychologique post-TBI", h_section))
story.append(styled_table([
    [C("Item", cell_g), C("Détail", cell_g)],
    [C("Pour quoi", cell_b),
     C("Évaluer précisément tes séquelles cognitives 3+ ans après ton TBI. Si jamais fait, à faire absolument.")],
    [C("Praticien", cell_b),
     C("Neuropsychologue. Peut être trouvé via CHU, centre de rééducation post-AVC/TBI, ou en libéral.")],
    [C("Prix indicatif", cell_b),
     C("Hôpital public : remboursé par Sécu sur prescription. Libéral : 150-300€ le bilan complet.")],
    [C("Démarche", cell_b),
     C("Demande à ton médecin traitant une orientation. Mention « bilan neuropsychologique post-TBI ».")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.append(P("TRE (Tension & Trauma Releasing Exercises)", h_section))
story.append(styled_table([
    [C("Item", cell_g), C("Détail", cell_g)],
    [C("Annuaire", cell_b),
     C("Site officiel TRE for All — annuaire international avec filtre France.")],
    [C("Format", cell_b),
     C("3-5 séances pour apprendre la technique, puis pratique autonome possible.")],
    [C("Prix indicatif", cell_b),
     C("60-90€ la séance individuelle. Existe aussi en groupe (moins cher).")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 10))

story.extend(retenir(
    "Investissement total estimé sur 12 mois : 1500-3000€ (1 praticien SE/EMDR régulier + 1 bilan neuropsy). "
    "Comparé au coût total de tes comptes prop firm cramés, c'est dérisoire. À la différence des comptes "
    "cramés, c'est un investissement qui produit un retour cumulé sur 20+ ans."
))
story.append(Spacer(1, 8))

story.extend(exercice([
    "<b>Action concrète cette semaine.</b> 30 minutes de recherche en ligne. Annuaire SE France + EMDR France. "
    "Identifie 3 praticiens dans ton département. Contacte 1 d'entre eux. Premier RDV pris dans les 15 jours.",
    "<b>Action concrète ce mois.</b> Demande à ton médecin traitant une prescription pour un bilan "
    "neuropsychologique post-TBI. Si jamais fait, c'est ton premier diagnostic objectif."
]))
story.append(PageBreak())


# ============================================================
# MOT DE LA FIN
# ============================================================
story.append(P("MOT DE LA FIN", h_part))
story.append(P("Pour Marien", h_part_sub))
story.append(GoldRule())
story.append(Spacer(1, 16))

story.append(P(
    "Tu as 25 ans. Tu as un coma derrière toi, un système nerveux qui se reconstruit, une intelligence rare, "
    "une ambition intacte, et maintenant un système structuré de 9 parties qui couvre toutes les dimensions "
    "de ton problème de trading."
))
story.append(Spacer(1, 4))
story.append(P(
    "Si à la fin de 2027, tu as travaillé ce manuel jour après jour, lentement, sans drame, tu seras un autre. "
    "Pas un trader plus performant — un Marien plus complet, plus calme, plus puissant, plus libre. Le trading "
    "suivra. Le reste suivra. Mais l'ordre compte : c'est toi qui changes, et tout le reste découle de ce changement."
))
story.append(Spacer(1, 4))
story.append(P(
    "Tu vas peut-être te dire que tu es en retard, qu'à 25 ans tu devrais déjà avoir réussi. C'est faux. "
    "Tu n'es pas en retard. Tu es <b>à l'heure</b>. Ton calendrier n'est pas celui de Twitter trading. Tu as "
    "ce qu'il faut pour les vingt prochaines années."
))
story.append(Spacer(1, 8))
story.append(P(
    "Va, applique, échoue parfois, reprends, écris dans ton cahier, ferme la plateforme, rentre chez toi, "
    "monte à cheval, dors sept heures, et reviens demain avec la même intention. C'est tout. C'est tout ce "
    "qu'il y a à faire.",
    body_i
))
story.append(Spacer(1, 20))
story.append(P("— Fin du manuel —",
    ParagraphStyle("end", fontName="DV-Italic", fontSize=11,
        textColor=MID_GREY, alignment=TA_CENTER)))


# ============================================================
# BUILD
# ============================================================
def on_first_page(canv, doc): cover_page(canv, doc)
def on_later_pages(canv, doc): standard_page(canv, doc)

doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
print(f"✓ PDF généré : {OUTPUT}")




