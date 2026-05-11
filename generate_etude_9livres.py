# -*- coding: utf-8 -*-
"""
Étude complète des 9 livres pour Marien — un seul PDF.
Toutes les analyses sont des paraphrases pédagogiques originales,
heavily personnalisées au profil de Marien. Aucune reproduction verbatim
des livres sources.
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
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Italic", "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Serif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Serif-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Mono", "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"))
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
PURPLE_SOFT = HexColor("#C5B5D8")
CREAM      = HexColor("#F8F4EC")
BLUE_DEEP  = HexColor("#1F3A52")
BLUE_SOFT  = HexColor("#A8C5D8")

# Couleurs par livre (chacun a sa teinte d'accent)
BOOK_COLORS = [
    GOLD,                # 1 Best Loser Wins
    HexColor("#C56E2E"),  # 2 Un monde sous dopamine
    HexColor("#7B3E5C"),  # 3 Le corps n'oublie rien
    HexColor("#A04A2C"),  # 4 Réveiller le tigre
    HexColor("#2D6A8E"),  # 5 Trader dans la zone
    HexColor("#5C7A3E"),  # 6 Quand le corps dit non
    HexColor("#8A5F2E"),  # 7 Un rien peut tout changer
    HexColor("#4A3E6E"),  # 8 Lâcher prise
    HexColor("#2E6A5C"),  # 9 La psychologie de l'argent
]

# ---------- STYLES ----------
body = ParagraphStyle("body", fontName="DejaVu", fontSize=10.3, leading=14.5,
    textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=7)
body_center = ParagraphStyle("body_c", parent=body, alignment=TA_CENTER)
body_white = ParagraphStyle("body_w", parent=body, textColor=white)
body_dark = ParagraphStyle("body_d", parent=body, textColor=DARK_BG)
body_italic = ParagraphStyle("body_i", parent=body, fontName="DejaVu-Italic")

cell_st = ParagraphStyle("cell", fontName="DejaVu", fontSize=9.2, leading=12.2,
    textColor=TEXT, alignment=TA_LEFT, spaceAfter=0)
cell_bold = ParagraphStyle("cell_b", parent=cell_st, fontName="DejaVu-Bold")
cell_gold = ParagraphStyle("cell_g", parent=cell_st, fontName="DejaVu-Bold", textColor=GOLD)
cell_white = ParagraphStyle("cell_w", parent=cell_st, textColor=white)
cell_white_bold = ParagraphStyle("cell_wb", parent=cell_white, fontName="DejaVu-Bold")

h_book = ParagraphStyle("h_book", fontName="DejaVu-Serif-Bold", fontSize=30, leading=34,
    textColor=GOLD, alignment=TA_LEFT, spaceAfter=4)
h_book_sub = ParagraphStyle("h_book_sub", fontName="DejaVu-Italic", fontSize=14, leading=18,
    textColor=MID_GREY, alignment=TA_LEFT, spaceAfter=20)
h_module = ParagraphStyle("h_module", fontName="DejaVu-Serif-Bold", fontSize=18, leading=22,
    textColor=GOLD, alignment=TA_LEFT, spaceBefore=8, spaceAfter=4)
h_module_sub = ParagraphStyle("h_module_sub", fontName="DejaVu-Italic", fontSize=11, leading=14,
    textColor=MID_GREY, alignment=TA_LEFT, spaceAfter=12)
h_section = ParagraphStyle("h_section", fontName="DejaVu-Bold", fontSize=12, leading=15,
    textColor=GOLD_SOFT, alignment=TA_LEFT, spaceBefore=10, spaceAfter=6)
h_subsection = ParagraphStyle("h_subsec", fontName="DejaVu-Bold", fontSize=10.5, leading=13,
    textColor=DARK_GREY, alignment=TA_LEFT, spaceBefore=6, spaceAfter=3)
cover_title = ParagraphStyle("cover_t", fontName="DejaVu-Serif-Bold", fontSize=38, leading=42,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10)
cover_sub = ParagraphStyle("cover_s", fontName="DejaVu-Italic", fontSize=16, leading=20,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=40)
cover_for = ParagraphStyle("cover_f", fontName="DejaVu", fontSize=13, leading=17,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=4)
cover_name = ParagraphStyle("cover_n", fontName="DejaVu-Serif-Bold", fontSize=30, leading=36,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=40)
cover_quote = ParagraphStyle("cover_q", fontName="DejaVu-Italic", fontSize=13, leading=18,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10)
callout_label = ParagraphStyle("c_label", fontName="DejaVu-Bold", fontSize=10, leading=12,
    textColor=white, alignment=TA_LEFT, spaceAfter=5)
callout_label_dark = ParagraphStyle("c_label_d", parent=callout_label, textColor=DARK_BG)
callout_body = ParagraphStyle("c_body", fontName="DejaVu", fontSize=10, leading=14,
    textColor=white, alignment=TA_JUSTIFY, spaceAfter=5)
callout_body_dark = ParagraphStyle("c_body_d", parent=callout_body, textColor=DARK_BG)
pull_quote = ParagraphStyle("pull_q", fontName="DejaVu-Italic", fontSize=12.5, leading=17,
    textColor=GOLD_SOFT, alignment=TA_CENTER, spaceBefore=8, spaceAfter=12,
    leftIndent=30, rightIndent=30)
mono = ParagraphStyle("mono", fontName="DejaVu-Mono", fontSize=8.5, leading=11,
    textColor=DARK_BG, alignment=TA_LEFT, spaceAfter=4)
small_label = ParagraphStyle("small_lab", fontName="DejaVu-Bold", fontSize=9, leading=11,
    textColor=GOLD_SOFT, alignment=TA_LEFT, spaceAfter=2)
diagram_caption = ParagraphStyle("dia_cap", fontName="DejaVu-Italic", fontSize=8.5, leading=11,
    textColor=MID_GREY, alignment=TA_CENTER, spaceBefore=2, spaceAfter=10)

# ---------- HELPERS ----------
def P(text, style=None):
    return Paragraph(text, style or body)

def C(text, style=None):
    return Paragraph(text, style or cell_st)


# ---------- CALLOUTS ----------
def make_callout(label, text, bg, fg, accent=GOLD):
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
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 3, accent),
    ]))
    return [Spacer(1, 4), t, Spacer(1, 8)]

def idee(text):    return make_callout("◆  IDÉE PRINCIPALE", text, DARK_GREY, white)
def mecan(text):   return make_callout("⚙  MÉCANISME", text, BLUE_DEEP, white, accent=GOLD)
def lien(text):    return make_callout("◈  CHEZ TOI, MARIEN", text, GOLD, DARK_BG)
def exemple(text): return make_callout("▣  EXEMPLE TRADING", text, DARK_BG, white, accent=GOLD)
def exo(text):     return make_callout("▶  EXERCICE", text, GREEN, white)
def phrase(text):  return make_callout("◇  PHRASE CLÉ", text, PURPLE, white)
def alerte(text):  return make_callout("!  ALERTE / VÉRITÉ BRUTALE", text, RED_ACC, white)

def section_callout(label, text):
    """Section générique avec label personnalisé (couleur crème)."""
    inner = [Paragraph(label, small_label)]
    if isinstance(text, list):
        for t in text:
            inner.append(Paragraph(t, body))
    else:
        inner.append(Paragraph(text, body))
    t = Table([[inner]], colWidths=[16 * cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), CREAM),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 10),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBEFORE", (0, 0), (0, -1), 2, GOLD_SOFT),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 8)]


# ---------- SCHEMAS / DIAGRAMS ----------
class Schema(Flowable):
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
    def __init__(self, width=16*cm, thickness=1.2, color=GOLD):
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


# ============================================================
# RENDERERS VISUELS — schémas de manuel d'étude
# ============================================================

def _arrow_full(c, x1, y1, x2, y2, color=GOLD, lw=1.4, head=6):
    """Flèche complète avec tête remplie."""
    c.setStrokeColor(color); c.setFillColor(color); c.setLineWidth(lw)
    c.line(x1, y1, x2, y2)
    dx, dy = x2 - x1, y2 - y1
    d = math.sqrt(dx*dx + dy*dy) or 1
    ux, uy = dx/d, dy/d
    px, py = -uy, ux
    p1 = (x2 - head*ux + head*0.45*px, y2 - head*uy + head*0.45*py)
    p2 = (x2 - head*ux - head*0.45*px, y2 - head*uy - head*0.45*py)
    path = c.beginPath()
    path.moveTo(x2, y2); path.lineTo(*p1); path.lineTo(*p2); path.close()
    c.drawPath(path, fill=1, stroke=1)


def _rounded_box(c, x, y, w, h, title=None, body=None, bg=DARK_GREY, fg=GOLD,
                 body_color=white, radius=5, title_size=9.5, body_size=8,
                 accent=None, center=False):
    """Boîte arrondie avec titre + corps optionnel."""
    c.setFillColor(bg)
    c.setStrokeColor(accent or bg)
    c.setLineWidth(0.8 if accent else 0)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1 if accent else 0)
    if title:
        c.setFillColor(fg)
        c.setFont("DejaVu-Bold", title_size)
        if center:
            c.drawCentredString(x + w/2, y + h - title_size - 4, title)
        else:
            c.drawString(x + 8, y + h - title_size - 4, title)
    if body:
        c.setFillColor(body_color)
        c.setFont("DejaVu", body_size)
        lines = body.split("\n") if isinstance(body, str) else body
        ly = y + h - title_size - 16 if title else y + h - body_size - 4
        for line in lines:
            if center:
                c.drawCentredString(x + w/2, ly, line)
            else:
                c.drawString(x + 8, ly, line)
            ly -= body_size + 2


# ---------- MINDMAP (Carte mentale) ----------
def draw_mindmap(c, w, h, title, branches, accent=GOLD):
    """
    title : str (texte du nœud central)
    branches : list of dicts {label, leaves: [list of str], color}
    """
    cx, cy = w/2, h/2
    # central node — adaptive radius based on title length
    longest_word = max((len(w_) for w_ in title.upper().split()), default=0)
    central_r = max(1.5*cm, longest_word * 0.13*cm)
    c.setFillColor(DARK_BG)
    c.circle(cx, cy, central_r, fill=1, stroke=0)
    c.setStrokeColor(accent); c.setLineWidth(1.8)
    c.circle(cx, cy, central_r, fill=0, stroke=1)
    # title — wrap to multiple lines if needed
    c.setFillColor(accent)
    c.setFont("DejaVu-Bold", 10)
    words = title.upper().split()
    lines_t = []
    cur = []
    max_w = central_r * 1.6
    for word in words:
        test_line = (" ".join(cur + [word])) if cur else word
        if c.stringWidth(test_line, "DejaVu-Bold", 10) > max_w and cur:
            lines_t.append(" ".join(cur)); cur = [word]
        else:
            cur.append(word)
    if cur: lines_t.append(" ".join(cur))
    total_h = len(lines_t) * 11
    for i, line in enumerate(lines_t):
        c.drawCentredString(cx, cy + total_h/2 - 11 - i*11 + 3, line)

    n = len(branches)
    # 3 branches : haut-gauche, droite, bas-gauche (mieux espacé visuellement)
    if n == 3:
        positions = [
            ("left", "top"),
            ("right", "middle"),
            ("left", "bottom"),
        ]
    elif n == 4:
        positions = [
            ("left", "top"),
            ("right", "top"),
            ("left", "bottom"),
            ("right", "bottom"),
        ]
    else:
        positions = []
        for i in range(n):
            side = "left" if i % 2 == 0 else "right"
            row = ["top", "middle", "bottom"][i // 2 % 3]
            positions.append((side, row))

    bw, bh = 3.4*cm, 1*cm

    for i, (br, (side, row)) in enumerate(zip(branches, positions)):
        # position
        if side == "left":
            bx = 0.5*cm
        else:
            bx = w - bw - 0.5*cm
        if row == "top":
            by = h - bh - 0.6*cm
        elif row == "bottom":
            by = 0.6*cm
        else:
            by = (h - bh) / 2

        # rectangle
        col = br.get("color", accent)
        c.setFillColor(col)
        c.roundRect(bx, by, bw, bh, 5, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("DejaVu-Bold", 9.5)
        c.drawCentredString(bx + bw/2, by + bh/2 - 3, br["label"])

        # connecting line from central node edge to branch box edge
        # branch attachment point: middle of the side closer to center
        if side == "left":
            attach_x = bx + bw
            attach_y = by + bh/2
        else:
            attach_x = bx
            attach_y = by + bh/2
        # direction
        dx, dy = attach_x - cx, attach_y - cy
        d = math.sqrt(dx*dx + dy*dy) or 1
        ux, uy = dx/d, dy/d
        start_x = cx + ux * central_r
        start_y = cy + uy * central_r
        c.setStrokeColor(accent); c.setLineWidth(1.3)
        c.line(start_x, start_y, attach_x, attach_y)

        # leaves listed BELOW the branch box (or above if at bottom row)
        leaves = br.get("leaves", [])
        if leaves:
            c.setFillColor(MID_GREY); c.setFont("DejaVu", 7.8)
            if row == "bottom":
                leaf_y = by + bh + 4
                step = 10
            else:
                leaf_y = by - 8
                step = -10
            for leaf in leaves:
                if side == "left":
                    c.drawString(bx + 4, leaf_y, "• " + leaf)
                else:
                    c.drawRightString(bx + bw - 4, leaf_y, leaf + " •")
                leaf_y += step


# ---------- CYCLE (boucle circulaire) ----------
def draw_cycle(c, w, h, nodes, title=None, accent=GOLD, node_color=DARK_BG):
    """nodes : list of (label, sublabel)."""
    cx, cy = w/2, h/2
    R = min(w, h) * 0.32
    node_r = 0.42 * cm
    n = len(nodes)
    pts = []
    for i, (label, sub) in enumerate(nodes):
        deg = 90 - i * 360 / n
        rad = math.radians(deg)
        x = cx + R * math.cos(rad)
        y = cy + R * math.sin(rad)
        pts.append((x, y, label, sub, rad))
    # arrows between consecutive
    for i in range(n):
        x1, y1, _, _, r1 = pts[i]
        x2, y2, _, _, r2 = pts[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        d = math.sqrt(dx*dx + dy*dy) or 1
        ux, uy = dx/d, dy/d
        _arrow_full(c, x1 + ux*node_r*1.3, y1 + uy*node_r*1.3,
                    x2 - ux*node_r*1.3, y2 - uy*node_r*1.3,
                    color=accent, lw=1.1, head=5)
    # nodes + labels
    for x, y, label, sub, rad in pts:
        # numbered node
        c.setFillColor(node_color)
        c.circle(x, y, node_r, fill=1, stroke=0)
        c.setStrokeColor(accent); c.setLineWidth(1.2)
        c.circle(x, y, node_r, fill=0, stroke=1)
        # label positioned outside
        ux, uy = math.cos(rad), math.sin(rad)
        lx = x + ux * 1.5*cm
        ly = y + uy * 0.7*cm
        c.setFillColor(DARK_BG)
        c.setFont("DejaVu-Bold", 8.2)
        if abs(ux) < 0.3:  # cardinal top/bottom
            c.drawCentredString(lx, ly + 3, label)
            c.setFont("DejaVu-Italic", 7)
            c.setFillColor(MID_GREY)
            c.drawCentredString(lx, ly - 8, sub)
        elif ux >= 0:
            c.drawString(lx, ly + 3, label)
            c.setFont("DejaVu-Italic", 7)
            c.setFillColor(MID_GREY)
            c.drawString(lx, ly - 8, sub)
        else:
            c.drawRightString(lx, ly + 3, label)
            c.setFont("DejaVu-Italic", 7)
            c.setFillColor(MID_GREY)
            c.drawRightString(lx, ly - 8, sub)
    # center text
    if title:
        c.setFillColor(accent)
        c.setFont("DejaVu-Serif-Bold", 11)
        lines = title.split("\n")
        for i, line in enumerate(lines):
            c.drawCentredString(cx, cy + 5 - i*12, line)


# ---------- COMPARISON (Saboteur vs Cible) ----------
def draw_comparison(c, w, h, left_title, left_items, right_title, right_items,
                    left_color=RED_ACC, right_color=GREEN, arrows_between=True,
                    left_sub=None, right_sub=None):
    """Deux colonnes opposées avec items."""
    gap = 0.4*cm
    box_w = (w - 2*gap) / 2
    bh = h - 0.4*cm
    # left box
    c.setFillColor(HexColor("#F8E5E5") if left_color == RED_ACC else left_color)
    c.roundRect(0, 0.2*cm, box_w, bh, 8, fill=1, stroke=0)
    c.setFillColor(left_color)
    c.setFont("DejaVu-Bold", 12)
    c.drawCentredString(box_w/2, bh - 14, left_title)
    if left_sub:
        c.setFont("DejaVu-Italic", 9)
        c.drawCentredString(box_w/2, bh - 28, left_sub)
    # right box
    rx = box_w + 2*gap
    c.setFillColor(HexColor("#E5F0E0") if right_color == GREEN else right_color)
    c.roundRect(rx, 0.2*cm, box_w, bh, 8, fill=1, stroke=0)
    c.setFillColor(right_color)
    c.setFont("DejaVu-Bold", 12)
    c.drawCentredString(rx + box_w/2, bh - 14, right_title)
    if right_sub:
        c.setFont("DejaVu-Italic", 9)
        c.drawCentredString(rx + box_w/2, bh - 28, right_sub)
    # items
    item_count = max(len(left_items), len(right_items))
    start_y = bh - 50
    step = (bh - 60) / max(item_count, 1) if item_count > 0 else 0
    for i in range(item_count):
        y_ = start_y - i * step
        if i < len(left_items):
            c.setFillColor(DARK_BG)
            c.setFont("DejaVu", 9)
            c.drawCentredString(box_w/2, y_, "•  " + left_items[i])
        if i < len(right_items):
            c.setFillColor(DARK_BG)
            c.setFont("DejaVu", 9)
            c.drawCentredString(rx + box_w/2, y_, "•  " + right_items[i])
        if arrows_between and i < min(len(left_items), len(right_items)):
            _arrow_full(c, box_w + 4, y_ + 3, rx - 4, y_ + 3, color=DARK_GREY, lw=0.7, head=4)


# ---------- PYRAMID 3-couches ----------
def draw_pyramid_3(c, w, h, levels, accent=GOLD):
    """levels: list of (title, example, sub, bg, txt) du BAS vers le HAUT."""
    cx = w/2
    top_y = h - 0.4*cm
    bot_y = 0.8*cm
    pyramid_h = top_y - bot_y
    half_base = 4.5*cm
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
        c.setStrokeColor(DARK_BG); c.setLineWidth(0.6)
        c.drawPath(p, fill=1, stroke=1)
        c.setFillColor(txt)
        c.setFont("DejaVu-Bold", 10 if i < 2 else 11)
        c.drawCentredString(cx, (y_lo + y_hi)/2 + 2, title)
        c.setFont("DejaVu-Italic", 7.5)
        c.drawCentredString(cx, (y_lo + y_hi)/2 - 8, ex)
        # right-side annotation
        c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 7.5)
        c.drawString(cx + half_base + 0.4*cm, (y_lo + y_hi)/2, sub)
    # left arrow
    c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 8)
    c.saveState()
    c.translate(cx - half_base - 0.8*cm, bot_y + pyramid_h/2)
    c.rotate(90)
    c.drawCentredString(0, 0, "↑ profondeur du changement ↑")
    c.restoreState()


# ---------- SEESAW (Bascule plaisir-douleur) ----------
def draw_seesaw(c, w, h, state="balanced", accent=GOLD):
    """state in {'balanced', 'pleasure', 'pain'}"""
    cx, cy = w/2, h/2
    beam_w = 10*cm
    beam_h = 0.4*cm
    # pivot triangle
    pivot_h = 1.4*cm
    pivot_w = 1.8*cm
    c.setFillColor(DARK_BG)
    p = c.beginPath()
    p.moveTo(cx, cy - 0.3*cm)
    p.lineTo(cx - pivot_w/2, cy - pivot_h)
    p.lineTo(cx + pivot_w/2, cy - pivot_h)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # beam tilt according to state
    tilt = 0
    if state == "pleasure":
        tilt = -10  # plaisir down on right
    elif state == "pain":
        tilt = 10
    c.saveState()
    c.translate(cx, cy)
    c.rotate(tilt)
    # beam
    c.setFillColor(accent)
    c.roundRect(-beam_w/2, -beam_h/2, beam_w, beam_h, 0.1*cm, fill=1, stroke=0)
    # weight on left (douleur)
    lw_size = 1.2*cm
    c.setFillColor(RED_ACC)
    c.roundRect(-beam_w/2 + 0.2*cm, beam_h/2, lw_size, lw_size, 4, fill=1, stroke=0)
    c.setFillColor(white); c.setFont("DejaVu-Bold", 8)
    c.drawCentredString(-beam_w/2 + 0.2*cm + lw_size/2, beam_h/2 + lw_size/2 - 3, "DOULEUR")
    # weight on right (plaisir)
    c.setFillColor(GOLD_SOFT)
    c.roundRect(beam_w/2 - 0.2*cm - lw_size, beam_h/2, lw_size, lw_size, 4, fill=1, stroke=0)
    c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 8)
    c.drawCentredString(beam_w/2 - 0.2*cm - lw_size/2, beam_h/2 + lw_size/2 - 3, "PLAISIR")
    c.restoreState()


# ---------- TIMELINE / PHASES horizontale ----------
def draw_phases_timeline(c, w, h, phases, ticks=None):
    """phases: list of (label, days, desc, bg, fg)"""
    margin = 0.4*cm
    seg_w = (w - 2*margin) / len(phases)
    bar_h = 2.2*cm
    bar_y = h - 4*cm if ticks else h/2 - bar_h/2
    if ticks:
        c.setStrokeColor(DARK_BG); c.setLineWidth(0.6); c.setFillColor(DARK_BG)
        c.setFont("DejaVu-Bold", 9)
        for k, t in enumerate(ticks):
            tx = margin + k * seg_w
            c.line(tx, bar_y + bar_h, tx, bar_y + bar_h + 8)
            c.drawCentredString(tx, bar_y + bar_h + 14, t)
    for i, (lbl, days, desc, bg, fg) in enumerate(phases):
        x = margin + i * seg_w
        c.setFillColor(bg); c.setStrokeColor(fg); c.setLineWidth(0.8)
        c.rect(x + 4, bar_y, seg_w - 8, bar_h, fill=1, stroke=1)
        c.setFillColor(fg); c.setFont("DejaVu-Bold", 12)
        c.drawCentredString(x + seg_w/2, bar_y + bar_h - 20, lbl)
        c.setFillColor(DARK_BG); c.setFont("DejaVu", 9)
        c.drawCentredString(x + seg_w/2, bar_y + bar_h - 38, days)
        c.setFont("DejaVu-Italic", 9); c.setFillColor(MID_GREY)
        c.drawCentredString(x + seg_w/2, bar_y + 14, desc)
    _arrow_full(c, margin, bar_y - 0.7*cm, w - margin, bar_y - 0.7*cm, color=GOLD, lw=1.2, head=6)


# ---------- VERTICAL FLOW (Boucle linéaire) ----------
def draw_flow_vertical(c, w, h, steps, title=None, accent=GOLD, color_each=None):
    """steps: list of strings (each becomes a box). Arrows connect them top-down."""
    n = len(steps)
    if title:
        c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 11)
        c.drawCentredString(w/2, h - 14, title)
        top_offset = 0.7*cm
    else:
        top_offset = 0.2*cm
    available = h - top_offset - 0.3*cm
    box_h = 0.85*cm
    spacing = (available - n*box_h) / max(n-1, 1) if n > 1 else 0
    box_w = w * 0.55
    bx = (w - box_w) / 2
    for i, step in enumerate(steps):
        by = h - top_offset - (i+1)*box_h - i*spacing
        col = accent if color_each is None else color_each[i % len(color_each)]
        c.setFillColor(col)
        c.roundRect(bx, by, box_w, box_h, 5, fill=1, stroke=0)
        # white or dark text depending on color
        c.setFillColor(white)
        c.setFont("DejaVu-Bold", 9)
        c.drawCentredString(w/2, by + box_h/2 - 3, step)
        # arrow between
        if i < n - 1:
            ay_start = by
            ay_end = by - spacing + 4
            _arrow_full(c, w/2, ay_start, w/2, ay_end, color=DARK_GREY, lw=1, head=5)


# ---------- HORIZONTAL FLOW ----------
def draw_flow_horizontal(c, w, h, steps, title=None, accent=GOLD):
    """Linear flow left-to-right."""
    n = len(steps)
    if title:
        c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 11)
        c.drawCentredString(w/2, h - 14, title)
        margin_top = 0.7*cm
    else:
        margin_top = 0.2*cm
    avail_w = w - 0.4*cm
    box_w = avail_w / n - 0.3*cm
    box_h = h - margin_top - 0.7*cm
    by = 0.4*cm
    for i, step in enumerate(steps):
        bx = 0.2*cm + i * (avail_w / n) + 0.15*cm
        c.setFillColor(accent)
        c.roundRect(bx, by, box_w, box_h, 5, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("DejaVu-Bold", 9)
        # word wrap
        words = step.split(" ")
        lines = []
        cur = []
        max_chars = int(box_w / 5)
        for word in words:
            if sum(len(w_) for w_ in cur) + len(word) + len(cur) > max_chars:
                lines.append(" ".join(cur)); cur = [word]
            else:
                cur.append(word)
        if cur: lines.append(" ".join(cur))
        for j, line in enumerate(lines):
            c.drawCentredString(bx + box_w/2, by + box_h/2 + 5 - j*11, line)
        if i < n - 1:
            ax = bx + box_w + 1
            ax_end = bx + (avail_w / n) + 0.1*cm
            _arrow_full(c, ax, by + box_h/2, ax_end, by + box_h/2, color=DARK_GREY, lw=1, head=5)


# ---------- HIERARCHY / TREE ----------
def draw_hierarchy(c, w, h, root, children, accent=GOLD):
    """Simple top-down hierarchy."""
    # root at top
    rw, rh = 5*cm, 1*cm
    rx = w/2 - rw/2
    ry = h - rh - 0.3*cm
    c.setFillColor(DARK_BG)
    c.roundRect(rx, ry, rw, rh, 5, fill=1, stroke=0)
    c.setStrokeColor(accent); c.setLineWidth(1)
    c.roundRect(rx, ry, rw, rh, 5, fill=0, stroke=1)
    c.setFillColor(accent); c.setFont("DejaVu-Bold", 11)
    c.drawCentredString(w/2, ry + rh/2 - 3, root)
    # children
    n = len(children)
    cw, ch = (w - 0.4*cm) / n - 0.3*cm, 1.4*cm
    cy_ = 0.4*cm
    for i, (label, sub) in enumerate(children):
        cx_ = 0.2*cm + i * ((w - 0.4*cm) / n) + 0.15*cm
        c.setFillColor(accent)
        c.roundRect(cx_, cy_, cw, ch, 5, fill=1, stroke=0)
        c.setFillColor(white); c.setFont("DejaVu-Bold", 9.5)
        c.drawCentredString(cx_ + cw/2, cy_ + ch - 14, label)
        if sub:
            c.setFont("DejaVu", 8); c.setFillColor(white)
            words = sub.split(" "); lines = []; cur = []
            max_chars = int(cw / 5)
            for word in words:
                if sum(len(w_) for w_ in cur) + len(word) + len(cur) > max_chars:
                    lines.append(" ".join(cur)); cur = [word]
                else:
                    cur.append(word)
            if cur: lines.append(" ".join(cur))
            for j, line in enumerate(lines):
                c.drawCentredString(cx_ + cw/2, cy_ + ch - 26 - j*9, line)
        # connector line from root to child
        c.setStrokeColor(MID_GREY); c.setLineWidth(0.7)
        c.line(w/2, ry, cx_ + cw/2, cy_ + ch + 3)


# ---------- GRAPH (Plateau vs linéaire) ----------
def draw_plateau_graph(c, w, h):
    """Graphique attente vs réalité."""
    margin_l = 1*cm; margin_r = 0.4*cm; margin_b = 1.2*cm; margin_t = 0.6*cm
    pw = w - margin_l - margin_r
    ph = h - margin_b - margin_t
    x0, y0 = margin_l, margin_b

    # axis
    c.setStrokeColor(MID_GREY); c.setLineWidth(0.5)
    c.line(x0, y0, x0 + pw, y0)
    c.line(x0, y0, x0, y0 + ph)
    c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 7.5)
    c.drawString(x0, y0 - 12, "temps →")

    # linear (expected) — gold
    c.setStrokeColor(GOLD_SOFT); c.setLineWidth(1.5)
    path1 = c.beginPath()
    path1.moveTo(x0, y0)
    path1.lineTo(x0 + pw, y0 + ph * 0.9)
    c.drawPath(path1, stroke=1, fill=0)
    c.setFillColor(GOLD_SOFT); c.setFont("DejaVu-Bold", 8)
    c.drawString(x0 + pw - 90, y0 + ph * 0.9 - 4, "Ce que tu attends")

    # real (plateau then breakthrough) — dark
    c.setStrokeColor(DARK_BG); c.setLineWidth(2)
    path2 = c.beginPath()
    path2.moveTo(x0, y0 + 4)
    path2.lineTo(x0 + pw * 0.5, y0 + 8)
    path2.lineTo(x0 + pw * 0.65, y0 + 14)
    path2.lineTo(x0 + pw * 0.75, y0 + ph * 0.3)
    path2.lineTo(x0 + pw * 0.88, y0 + ph * 0.7)
    path2.lineTo(x0 + pw, y0 + ph * 0.92)
    c.drawPath(path2, stroke=1, fill=0)
    c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 8)
    c.drawString(x0 + 10, y0 + 8, "Ce qui se passe vraiment")
    # marker basculement
    bx, by = x0 + pw * 0.7, y0 + ph * 0.2
    c.setFillColor(RED_ACC); c.circle(bx, by, 4, fill=1, stroke=0)
    c.setFillColor(RED_ACC); c.setFont("DejaVu-Bold", 7.5)
    c.drawString(bx + 8, by - 2, "★ basculement")
    c.setFont("DejaVu-Italic", 7); c.setFillColor(MID_GREY)
    c.drawString(bx + 8, by - 12, "  (préparé pendant le plateau)")


# ---------- 80/20 BAR ----------
def draw_8020_bar(c, w, h, perdants=80, gagnants=20):
    """Barre stacked."""
    bar_h = 1.3*cm
    bar_y = h/2 - bar_h/2
    p_w = w * perdants / 100
    g_w = w * gagnants / 100
    c.setFillColor(RED_ACC)
    c.rect(0, bar_y, p_w, bar_h, fill=1, stroke=0)
    c.setFillColor(GREEN)
    c.rect(p_w, bar_y, g_w, bar_h, fill=1, stroke=0)
    c.setFont("DejaVu-Bold", 13); c.setFillColor(white)
    c.drawCentredString(p_w/2, bar_y + bar_h/2 - 4, f"{perdants}%  PERDENT")
    c.drawCentredString(p_w + g_w/2, bar_y + bar_h/2 - 4, f"{gagnants}%")
    c.setFont("DejaVu", 8.5); c.setFillColor(DARK_BG)
    c.drawCentredString(p_w/2, bar_y + bar_h + 8, "Tu es ici — pas par hasard")
    c.drawCentredString(p_w + g_w/2, bar_y + bar_h + 8, "La sortie")


# ---------- ÉTAGES de compétence ----------
def draw_etages(c, w, h, levels, accent=GOLD):
    """3 étages d'une compétence. levels: list (titre, description, %)."""
    n = len(levels)
    margin = 0.4*cm
    avail_h = h - 0.4*cm
    box_h = avail_h / n - 0.2*cm
    for i, (title, desc, perc) in enumerate(reversed(levels)):
        idx = n - 1 - i  # actual index from bottom
        by = margin + i * (box_h + 0.2*cm)
        # color : top brightest
        col_pool = [GREEN_SOFT, GOLD_PALE, RED_SOFT]
        col = col_pool[i] if i < len(col_pool) else GOLD_PALE
        c.setFillColor(col)
        c.setStrokeColor(DARK_BG); c.setLineWidth(0.6)
        c.rect(0.3*cm, by, w - 0.6*cm, box_h, fill=1, stroke=1)
        c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 11)
        c.drawString(0.6*cm, by + box_h - 16, f"ÉTAGE {idx+1} — {title}")
        c.setFont("DejaVu-Italic", 9)
        c.drawString(0.6*cm, by + box_h - 30, desc)
        c.setFillColor(MID_GREY); c.setFont("DejaVu-Bold", 9)
        c.drawRightString(w - 0.5*cm, by + box_h - 16, perc)


# ---------- THERMOSTAT (déjà fait avant, à réutiliser) ----------
def draw_thermostat_v(c, w, h):
    c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 12)
    c.drawCentredString(w/2, h - 16, "TON THERMOSTAT FINANCIER")
    c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 9)
    c.drawCentredString(w/2, h - 32, "le sabotage est mécanique, pas moral")
    tx, ty, tw, th = 4.2*cm, 1.4*cm, 1.4*cm, h - 3.6*cm
    c.setStrokeColor(DARK_GREY); c.setLineWidth(1)
    c.roundRect(tx, ty, tw, th, 8, fill=0, stroke=1)
    bands = [(0.0, 0.30, GREEN_SOFT), (0.30, 0.55, GOLD_PALE),
             (0.55, 0.80, GOLD), (0.80, 1.0, RED_ACC)]
    for lo, hi, col in bands:
        c.setFillColor(col)
        c.rect(tx + 2, ty + 2 + lo*(th-4), tw - 4, (hi - lo)*(th-4), fill=1, stroke=0)
    # zone labels
    c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 8)
    for ratio, lbl in [(0.90, "danger"), (0.65, "inconfort"), (0.42, "tolérable"), (0.15, "confort")]:
        c.drawRightString(tx - 10, ty + ratio * th - 3, lbl)
    # markers
    cy_y = ty + 0.80 * th
    c.setStrokeColor(RED_ACC); c.setLineWidth(1.4)
    c.line(tx + tw, cy_y, tx + tw + 20, cy_y)
    c.setFillColor(RED_ACC); c.setFont("DejaVu-Bold", 10)
    c.drawString(tx + tw + 26, cy_y - 3, "PLAFOND")
    c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 8)
    c.drawString(tx + tw + 26, cy_y - 15, "zone du sabotage (+1500)")
    bs_y = ty + 0.30 * th
    c.setStrokeColor(DARK_BG); c.setLineWidth(1.4)
    c.line(tx + tw, bs_y, tx + tw + 20, bs_y)
    c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 10)
    c.drawString(tx + tw + 26, bs_y - 3, "BASELINE")
    c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 8)
    c.drawString(tx + tw + 26, bs_y - 15, "ton « normal pour moi »")
    _arrow_full(c, tx + tw/2, cy_y - 0.3*cm, tx + tw/2, bs_y + 0.4*cm, color=DARK_BG, lw=1.4, head=6)


# ---------- 4 FORCES PSY ----------
def draw_4_forces_psy(c, w, h):
    cx, cy = w/2, h/2
    r = 1.3*cm
    c.setFillColor(GOLD)
    c.circle(cx, cy, r, fill=1, stroke=0)
    c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 10)
    c.drawCentredString(cx, cy + 4, "TOI")
    c.setFont("DejaVu", 8.5)
    c.drawCentredString(cx, cy - 8, "EN TRADE")
    box_w, box_h = 5*cm, 1.4*cm
    positions = [
        (0.4*cm, cy + 1.2*cm, "BESOIN D'AVOIR RAISON", "Ego refuse d'être contredit"),
        (w - box_w - 0.4*cm, cy + 1.2*cm, "AVERSION À LA PERTE", "Kahneman : 2x plus mal"),
        (0.4*cm, cy - 1.2*cm - box_h, "BESOIN DE CERTITUDE", "Invente du « je suis sûr »"),
        (w - box_w - 0.4*cm, cy - 1.2*cm - box_h, "PROJECTION ÉMOTIONNELLE", "Tu vois ce que tu veux voir"),
    ]
    for bx, by, title, sub in positions:
        c.setFillColor(DARK_GREY)
        c.roundRect(bx, by, box_w, box_h, 4, fill=1, stroke=0)
        c.setFillColor(GOLD); c.setFont("DejaVu-Bold", 8.5)
        c.drawString(bx + 8, by + box_h - 14, title)
        c.setFillColor(white); c.setFont("DejaVu", 7.5)
        c.drawString(bx + 8, by + 8, sub)
        # arrow
        bcx, bcy = bx + box_w/2, by + box_h/2
        dx, dy = cx - bcx, cy - bcy
        d = math.sqrt(dx*dx + dy*dy)
        ux, uy = dx/d, dy/d
        ex, ey = cx - ux*r, cy - uy*r
        _arrow_full(c, bcx + ux*box_w*0.35, bcy + uy*box_h*0.45, ex, ey,
                    color=RED_ACC, lw=1.3, head=5)


# ---------- PATTERN +1500 ----------
def draw_1500_curve(c, w, h):
    margin_l, margin_r = 1*cm, 0.4*cm
    margin_b, margin_t = 1.2*cm, 0.6*cm
    pw = w - margin_l - margin_r
    ph = h - margin_b - margin_t
    x0 = margin_l; y0 = margin_b
    c.setStrokeColor(MID_GREY); c.setLineWidth(0.5)
    c.line(x0, y0, x0 + pw, y0)
    c.line(x0, y0, x0, y0 + ph)
    zero_y = y0 + ph * 0.45
    c.setStrokeColor(LIGHT_GREY)
    c.line(x0, zero_y, x0 + pw, zero_y)
    c.setFont("DejaVu", 7.5); c.setFillColor(MID_GREY)
    c.drawString(x0 - 20, zero_y - 2, "0")
    c.drawString(x0 - 30, y0 + ph - 6, "+1500")
    c.drawString(x0 - 28, y0 + 4, "-800")
    pts = [(0.00, 0.00), (0.18, 0.45), (0.30, 0.95), (0.42, 0.70),
           (0.55, 0.35), (0.68, 0.00), (0.78, -0.35), (0.88, -0.65), (1.00, -0.95)]
    def px(t): return x0 + t * pw
    def py(v): return zero_y + v * (ph * 0.50)
    c.setStrokeColor(GOLD); c.setLineWidth(1.8)
    path = c.beginPath()
    path.moveTo(px(pts[0][0]), py(pts[0][1]))
    for t, v in pts[1:]:
        path.lineTo(px(t), py(v))
    c.drawPath(path, stroke=1, fill=0)
    markers = [
        (pts[0], "Entrée", "calme", GREEN),
        (pts[1], "+800 dopamine ON", "« je tiens »", GOLD_SOFT),
        (pts[2], "+1500 — préfrontal OFF", "tu es passager", RED_ACC),
        (pts[5], "Retour à 0", "« ça va repartir »", RED_ACC),
        (pts[6], "SL touché → décalé", "auto-destruction", RED_ACC),
        (pts[8], "Compte cramé", "game over", DARK_BG),
    ]
    for (t, v), lab, sub, col in markers:
        x, y = px(t), py(v)
        c.setFillColor(col); c.circle(x, y, 3.5, fill=1, stroke=0)
        c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 7.5)
        ly = y + 8 if v > 0 else y - 14
        c.drawCentredString(x, ly, lab)
        c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 7)
        c.drawCentredString(x, ly - 9, sub)


# ---------- BOUCLE D'HABITUDE (4 phases) ----------
def draw_habit_loop(c, w, h):
    """Boucle déclencheur → désir → réponse → récompense."""
    nodes = [
        ("DÉCLENCHEUR", "signal / contexte"),
        ("DÉSIR", "anticipation"),
        ("RÉPONSE", "comportement"),
        ("RÉCOMPENSE", "gratification"),
    ]
    cx, cy = w/2, h/2
    R = min(w, h) * 0.30
    node_r = 0.7*cm
    pts = []
    for i, (label, sub) in enumerate(nodes):
        deg = 90 - i * 90
        rad = math.radians(deg)
        x = cx + R * math.cos(rad)
        y = cy + R * math.sin(rad)
        pts.append((x, y, label, sub, rad))
    for i in range(4):
        x1, y1, _, _, _ = pts[i]
        x2, y2, _, _, _ = pts[(i + 1) % 4]
        dx, dy = x2 - x1, y2 - y1
        d = math.sqrt(dx*dx + dy*dy)
        ux, uy = dx/d, dy/d
        _arrow_full(c, x1 + ux*node_r, y1 + uy*node_r,
                    x2 - ux*node_r, y2 - uy*node_r,
                    color=GOLD_SOFT, lw=1.3, head=6)
    for i, (x, y, label, sub, rad) in enumerate(pts):
        c.setFillColor(DARK_BG); c.circle(x, y, node_r, fill=1, stroke=0)
        c.setStrokeColor(GOLD); c.setLineWidth(1.5)
        c.circle(x, y, node_r, fill=0, stroke=1)
        c.setFillColor(GOLD); c.setFont("DejaVu-Bold", 8)
        c.drawCentredString(x, y + 2, str(i+1))
        c.setFillColor(DARK_BG); c.setFont("DejaVu-Bold", 9)
        ux, uy = math.cos(rad), math.sin(rad)
        lx = x + ux * 1.5*cm
        ly = y + uy * 1*cm
        c.drawCentredString(lx, ly + 4, label)
        c.setFillColor(MID_GREY); c.setFont("DejaVu-Italic", 8)
        c.drawCentredString(lx, ly - 7, sub)
    c.setFillColor(GOLD); c.setFont("DejaVu-Serif-Bold", 11)
    c.drawCentredString(cx, cy + 5, "BOUCLE")
    c.drawCentredString(cx, cy - 8, "D'HABITUDE")


print("✓ Renderers visuels ajoutés")


# ---------- ASCII-style schema rendered as styled box ----------
def ascii_schema(text, accent=GOLD):
    """Render un schéma ASCII / texte structuré dans une boîte sombre."""
    lines = text.strip("\n").split("\n")
    para_lines = []
    for line in lines:
        # garder le formatage avec espaces non sécables
        line_html = line.replace(" ", "&nbsp;")
        para_lines.append(Paragraph(line_html,
            ParagraphStyle("schema_line", fontName="DejaVu-Mono", fontSize=8.2,
                leading=10.5, textColor=DARK_BG, alignment=TA_LEFT)))
    t = Table([[para_lines]], colWidths=[16*cm])
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


def styled_table(data, col_widths, header=True, accent=GOLD):
    t = Table(data, colWidths=col_widths, repeatRows=1 if header else 0)
    style = [
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BOX", (0, 0), (-1, -1), 0.6, accent),
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


# ---------- BOOK COVER (separator page) ----------
def book_separator_page(num, title, author, original_title, year, accent, quote=None, subtitle=None):
    """Page de séparation entre livres : grande page sombre avec numéro."""
    out = []
    out.append(Spacer(1, 5*cm))
    # numéro
    num_style = ParagraphStyle("booknum", fontName="DejaVu-Serif-Bold", fontSize=48, leading=52,
        textColor=accent, alignment=TA_CENTER, spaceAfter=8)
    out.append(P(f"LIVRE {num}", num_style))
    out.append(Spacer(1, 0.8*cm))
    # titre
    out.append(P(title, cover_title))
    if subtitle:
        out.append(P(subtitle, ParagraphStyle("bksub", fontName="DejaVu-Italic", fontSize=13,
            leading=17, textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=10)))
    out.append(P(f"{author}  ·  {year}", cover_sub))
    out.append(Spacer(1, 1*cm))
    if original_title and original_title != title:
        out.append(P(f"<i>Titre original : {original_title}</i>",
            ParagraphStyle("origt", fontName="DejaVu-Italic", fontSize=10,
                textColor=MID_GREY, alignment=TA_CENTER)))
    out.append(Spacer(1, 1.2*cm))
    if quote:
        out.append(P(quote, cover_quote))
    out.append(PageBreak())
    return out


# ---------- PAGE TEMPLATES ----------
_current_book_color = [GOLD]  # mutable holder

def cover_page(canv, doc):
    canv.saveState()
    canv.setFillColor(DARK_BG)
    canv.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    canv.setFillColor(GOLD)
    canv.rect(0, A4[1] - 1.4*cm, A4[0], 1.4*cm, fill=1, stroke=0)
    canv.rect(0, 0, A4[0], 1.4*cm, fill=1, stroke=0)
    canv.setStrokeColor(GOLD); canv.setLineWidth(0.5)
    canv.rect(1.2*cm, 2.2*cm, A4[0] - 2.4*cm, A4[1] - 4.4*cm, fill=0, stroke=1)
    canv.restoreState()

def standard_page(canv, doc):
    canv.saveState()
    color = _current_book_color[0]
    canv.setStrokeColor(color)
    canv.setLineWidth(0.6)
    canv.line(2*cm, A4[1] - 1.4*cm, A4[0] - 2*cm, A4[1] - 1.4*cm)
    canv.setFont("DejaVu-Bold", 8)
    canv.setFillColor(color)
    canv.drawString(2*cm, A4[1] - 1.15*cm, "MANUEL D'ÉTUDE — 9 LIVRES")
    canv.setFont("DejaVu-Italic", 8)
    canv.setFillColor(MID_GREY)
    canv.drawRightString(A4[0] - 2*cm, A4[1] - 1.15*cm, "Marien")
    canv.setFont("DejaVu", 8.5)
    canv.setFillColor(MID_GREY)
    canv.drawCentredString(A4[0]/2.0, 1.2*cm, f"— {doc.page} —")
    canv.setStrokeColor(color)
    canv.setLineWidth(0.3)
    canv.line(2*cm, 1.7*cm, A4[0] - 2*cm, 1.7*cm)
    canv.restoreState()

def book_separator_page_canvas(canv, doc):
    canv.saveState()
    canv.setFillColor(DARK_BG)
    canv.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    color = _current_book_color[0]
    canv.setFillColor(color)
    canv.rect(0, A4[1] - 1.4*cm, A4[0], 1.4*cm, fill=1, stroke=0)
    canv.rect(0, 0, A4[0], 1.4*cm, fill=1, stroke=0)
    canv.setStrokeColor(color); canv.setLineWidth(0.5)
    canv.rect(1.2*cm, 2.2*cm, A4[0] - 2.4*cm, A4[1] - 4.4*cm, fill=0, stroke=1)
    canv.restoreState()


def module_header(num_book, num_module, title, subtitle, accent):
    out = []
    out.append(P(f"MODULE {num_module}", small_label))
    out.append(P(title, h_module))
    out.append(P(subtitle, h_module_sub))
    out.append(GoldRule(color=accent))
    out.append(Spacer(1, 10))
    return out


def book_intro_header(num, title, author, accent):
    out = []
    out.append(P(f"LIVRE {num}", small_label))
    out.append(P(title, h_book))
    out.append(P(f"{author}", h_book_sub))
    out.append(GoldRule(color=accent))
    out.append(Spacer(1, 14))
    return out


print("✓ Infrastructure chargée")


# ============================================================
# DOCUMENT
# ============================================================
OUTPUT = "/home/user/Site-Enzo/etude_9livres_marien.pdf"
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2.5*cm, rightMargin=2.5*cm,
    topMargin=2.2*cm, bottomMargin=2.2*cm,
    title="Manuel d'étude — 9 livres pour Marien",
    author="Étude personnalisée"
)
story = []


# ============================================================
# COVER GÉNÉRALE
# ============================================================
story.append(Spacer(1, 4*cm))
story.append(P("MANUEL D'ÉTUDE", cover_title))
story.append(P("9 livres pour transformer ton trading,<br/>ton corps et ton mental", cover_sub))
story.append(Spacer(1, 0.8*cm))
story.append(P("Pour", cover_for))
story.append(P("MARIEN", cover_name))
story.append(Spacer(1, 1.5*cm))
story.append(P(
    '« On ne change pas en consommant des livres.<br/>'
    'On change en habitant un livre à la fois,<br/>'
    'jusqu\'à ce qu\'il habite en nous. »', cover_quote))
story.append(Spacer(1, 1*cm))
story.append(P("Mai 2026", ParagraphStyle("date", fontName="DejaVu", fontSize=11,
    textColor=LIGHT_GREY, alignment=TA_CENTER)))
story.append(PageBreak())


# ============================================================
# PRÉFACE GÉNÉRALE
# ============================================================
story.append(P("PRÉFACE", h_book))
story.append(P("Comment utiliser ce manuel", h_book_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Ce document n'est pas une bibliothèque de résumés. C'est un <b>manuel d'étude</b>. Neuf livres, choisis "
    "spécifiquement pour ton profil — trader prop firm sur XAUUSD, pattern destructeur signature, post-TBI 2022, "
    "système nerveux dérégulé, lien identité-performance trop chargé, addiction à l'intensité. Chaque livre adresse "
    "une dimension de ton problème. Lus dans l'ordre, ils forment un système."
))
story.append(P("Trois règles d'or pour ne pas perdre ton temps", h_section))
story.append(P(
    "<b>1. Un livre à la fois.</b> Tu lis l'analyse complète du livre dans ce manuel. Tu appliques les exercices "
    "pendant 7 à 14 jours. Tu ne passes pas au suivant tant que tu n'as pas appliqué le précédent. "
    "Si tu sautes les exercices, tu fais de la consommation de contenu — exactement le piège que ces livres "
    "te décrivent."
))
story.append(P(
    "<b>2. La main qui écrit.</b> Chaque exercice dans le manuel est conçu pour être fait <b>à la main</b>, "
    "dans un cahier dédié. Écrire à la main n'est pas un détail esthétique : c'est une voie neuronale différente. "
    "Tape sur un clavier et tu restes en surface. Écris à la main et tu descends en toi."
))
story.append(P(
    "<b>3. Le corps avant le mental.</b> Quatre des neuf livres parlent du corps (Levine, van der Kolk, Maté, Lembke). "
    "Ce n'est pas un hasard. Ton TBI a fait de ton système nerveux ton premier terrain de travail. "
    "Aucun mental ne s'apaise dans un corps en alerte. Lis ces livres comme un physique avant de les lire "
    "comme un mental."
))

story.append(P("La structure de chaque chapitre-livre", h_section))
story.append(P("Pour chaque livre tu trouveras la même architecture en cinq blocs :"))

struct_data = [
    [C("Bloc", cell_gold), C("Contenu", cell_gold)],
    [C("A. Pourquoi ce livre", cell_bold),
     C("Le diagnostic — pourquoi ce livre touche TON problème, pas un problème générique.")],
    [C("B. Résumé global profond", cell_bold),
     C("La thèse, les mécanismes psychologiques, les transformations proposées, les limites du livre.")],
    [C("C. Carte mentale", cell_bold),
     C("Schéma textuel synthétique de l'architecture du livre.")],
    [C("D. Modules thématiques", cell_bold),
     C("8 à 12 modules par livre. Chaque module = idée + mécanisme + lien Marien + exemple trading + schéma + tableau + exercice + phrase clé.")],
    [C("E. Synthèse complète", cell_bold),
     C("10 idées clés, 10 erreurs que le livre t'aide à arrêter, 10 nouvelles règles, protocole 7 jours, fiche visuelle finale.")],
]
story.append(styled_table(struct_data, [4.5*cm, 11.5*cm]))
story.append(Spacer(1, 12))

story.append(P("L'ordre des 9 livres et son intention", h_section))
story.append(P(
    "L'ordre n'est pas aléatoire. Il suit une logique de chantier intérieur, de la surface vers le fond, "
    "puis du fond vers l'intégration :"
))

roadmap = [
    [C("#", cell_gold), C("Livre", cell_gold), C("Auteur", cell_gold), C("Pourquoi à ce moment", cell_gold)],
    [C("1"), C("Best Loser Wins", cell_bold), C("T. Hougaard"),
     C("Le diagnostic frontal de ton pattern de trader. Le miroir le plus direct.")],
    [C("2"), C("Un monde sous dopamine", cell_bold), C("A. Lembke"),
     C("Le mécanisme neurochimique de ton addiction à l'intensité. La chimie expliquée.")],
    [C("3"), C("Le corps n'oublie rien", cell_bold), C("B. van der Kolk"),
     C("Pourquoi ton TBI 2022 pilote encore tes décisions. Le trauma stocké dans le corps.")],
    [C("4"), C("Réveiller le tigre", cell_bold), C("P. Levine"),
     C("Comment décharger concrètement les états d'urgence figés dans ton système nerveux.")],
    [C("5"), C("Trader dans la zone", cell_bold), C("M. Douglas"),
     C("La structure mentale du trader rentable. Le livre fondateur que Hougaard prolonge.")],
    [C("6"), C("Quand le corps dit non", cell_bold), C("G. Maté"),
     C("Le coût somatique des émotions refoulées. Lié à ton lien identité-performance.")],
    [C("7"), C("Un rien peut tout changer", cell_bold), C("J. Clear"),
     C("L'architecture d'habitude. Comment transformer les insights précédents en système quotidien.")],
    [C("8"), C("Lâcher prise", cell_bold), C("D. Hawkins"),
     C("La compétence du surrender. Antidote à ton contrôle pathologique.")],
    [C("9"), C("La psychologie de l'argent", cell_bold), C("M. Housel"),
     C("Le rapport à l'argent comme rapport à soi. Boucle finale de la transformation.")],
]
story.append(styled_table(roadmap, [0.7*cm, 4.6*cm, 2.7*cm, 8*cm]))
story.append(Spacer(1, 14))

story.append(P("Avertissement honnête", h_section))
story.append(P(
    "Ce manuel n'est pas un substitut aux livres originaux. C'est un guide d'étude qui paraphrase, structure "
    "et personnalise. Si une idée te touche, achète le livre, lis-le entier. Le manuel sert à <b>orienter "
    "ta lecture et à la rendre opérationnelle</b> dans ton cas spécifique. Lis-le comme une carte qui "
    "accompagne le territoire, pas comme le territoire lui-même."
))
story.append(P(
    "Aucune citation longue des auteurs originaux n'a été reproduite. Toutes les analyses sont des paraphrases "
    "originales, écrites avec mes mots, structurées pour ton apprentissage visuel et appliquées à ton cas. "
    "L'objectif est transformatif, pas copiste."
))
story.append(PageBreak())


# ============================================================
# LIVRE 1 — BEST LOSER WINS
# ============================================================
_current_book_color[0] = BOOK_COLORS[0]
ACCENT = BOOK_COLORS[0]

# --- Page séparateur ---
story.extend(book_separator_page(
    1, "Best Loser Wins", "Tom Hougaard", "Best Loser Wins", 2022, ACCENT,
    quote='« Les meilleurs traders ne gagnent pas mieux.<br/>Ils perdent mieux. »',
    subtitle="Pourquoi la pensée normale ne gagne jamais"
))

# --- Bloc A : Pourquoi ce livre ---
story.extend(book_intro_header(1, "Best Loser Wins", "Tom Hougaard — 2022", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "Hougaard a passé plus de vingt ans dans les salles de marché de la City de Londres. Il a vu défiler "
    "des centaines de traders. Il a écrit ce livre pour expliquer pourquoi des traders intelligents, techniquement "
    "compétents, lecteurs assidus, perdent quand même. <b>Tu rentres dans cette catégorie avec une précision chirurgicale.</b>"
))
story.append(P(
    "Tu maîtrises SMC, killzones, FVG, OB, CHoCH. Tu peux justifier chaque entrée. Si on prenait tes dix derniers "
    "setups en isolation, ils seraient probablement bons. Et tu crames quand même tes comptes Apex, Topstep, "
    "Alpha Futures. Le décalage entre <b>ce que tu sais</b> et <b>ce que tu fais</b> est précisément le sujet "
    "du livre. Hougaard ne te parle pas de setups. Il te parle de toi."
))
story.append(P(
    "Ton pattern signature — +1500 PnL, refus de couper, reverse, SL décalé, compte cramé — est un cas d'école "
    "que ce livre décrit sous différentes formes. Il te donne le <b>vocabulaire</b> et la <b>carte</b> pour nommer "
    "ce que tu fais. Et nommer une mécanique, c'est la première étape pour la contrer."
))
story.append(P(
    "C'est le livre <b>numéro 1</b> de ton chantier car c'est le plus frontal. Les huit suivants creusent "
    "les dimensions que celui-ci pose sans les développer entièrement."
))

# --- Bloc B : Résumé global ---
story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse en une phrase", h_subsection))
story.append(P('<b>Le trader rentable n\'est pas celui qui gagne mieux. C\'est celui qui perd mieux.</b>', pull_quote))
story.append(P(
    "Hougaard inverse l'intuition naïve. Le débutant croit que devenir rentable signifie augmenter son taux "
    "de réussite. Hougaard démontre que l'écart de performance entre rentables et perdants ne se joue presque "
    "jamais sur le taux de réussite — il se joue sur la <b>façon de gérer pertes et gains</b>."
))
story.append(P("Les six mécanismes psychologiques exposés", h_subsection))
story.append(P(
    "<b>1. Aversion à la perte (Kahneman) :</b> perdre fait 2 à 2,5 fois plus mal que gagner ne fait plaisir. "
    "Tu coupes tes gains tôt et tu tiens tes pertes long. <b>2. Besoin d'avoir raison :</b> l'ego s'attache à "
    "la justesse de ses prédictions. Acter un SL c'est admettre qu'on a eu tort. <b>3. Besoin de certitude :</b> "
    "le cerveau invente de la certitude là où il n'y en a pas. <b>4. Projection émotionnelle :</b> biais de "
    "confirmation appliqué au chart. <b>5. Dopamine d'anticipation :</b> c'est l'attente du résultat qui addictive. "
    "<b>6. Identité-performance :</b> tant que ton identité dépend de ton dernier trade, tu es ingouvernable."
))
story.append(P("Les trois transformations proposées", h_subsection))
story.append(P(
    "<b>T1 — De l'analyse à l'exécution.</b> Arrêter de chercher la méthode parfaite. Travailler le geste. "
    "<b>T2 — Du joueur au statisticien.</b> Juger la distribution sur 100 trades, pas chaque trade. "
    "<b>T3 — Du performeur à l'identité.</b> Devenir « le trader qui exécute ». Le gain suit l'identité."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Très anglo-saxon, storytelling parfois envahissant. Peu de neurosciences précises (à compléter avec Lembke "
    "et van der Kolk). Pas un mot sur le trauma corporel (à compléter avec Levine — crucial pour ton TBI). "
    "Pas de protocole jour-par-jour. C'est un livre d'insight, pas un manuel d'application — c'est pourquoi "
    "ce manuel d'étude existe."
))

# --- Bloc C : Carte mentale ---
story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Best Loser Wins",
    [
        {"label": "THÈSE", "leaves": ["« best loser wins »", "perte gérée = edge"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["aversion perte", "besoin certitude", "dopamine", "identité-perf"], "color": ACCENT},
        {"label": "APPLICATION", "leaves": ["pattern +1500", "décalage SL", "FOMO", "sur-trading"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Vue d'ensemble du livre — concepts et application personnelle.", diagram_caption))
story.append(PageBreak())


# ============================================================
# LIVRE 1 — Modules
# ============================================================

# --- MODULE 1 ---
story.extend(module_header(1, 1, "Le parcours initiatique",
    "Pourquoi la compétence technique ne sauve pas", ACCENT))
story.extend(idee(
    "L'auteur a passé ses premières années obsédé par l'analyse technique. Il perdait quand même. "
    "Le décalage entre <b>savoir</b> et <b>faire</b> est devenu sa thèse fondatrice : le trading n'est "
    "pas un problème intellectuel, c'est un problème comportemental."
))
story.append(P("Ce que l'auteur veut vraiment te faire comprendre", h_subsection))
story.append(P(
    "Tu n'as pas un problème de connaissance. Tu sais déjà. L'edge n'est pas dans la méthode (qui est le ticket "
    "d'entrée) — il est dans ta capacité à exécuter cette méthode quand ton corps te pousse à autre chose. "
    "Le vrai jeu commence quand tu sais lire le marché correctement et que tu continues à perdre quand même."
))
story.extend(mecan([
    "Trois étages dans toute compétence humaine : <b>1) Savoir</b> (cognitif — tu peux expliquer). "
    "<b>2) Savoir-faire</b> (procédural — tu peux faire en démo, au calme). <b>3) Être</b> "
    "(identitaire — tu fais sous pression nerveuse).",
    "L'erreur fatale : croire qu'ajouter du savoir (étage 1) débloque l'être (étage 3). Faux. "
    "Le passage 1 → 3 demande un travail vertical — descente dans le corps, le SN, l'identité — pas horizontal."
]))
story.extend(lien([
    "Combien de méthodes différentes as-tu testées depuis 18 mois ? Combien de mentors, formations, Discords ? "
    "Quand tu galères, ton premier réflexe est-il d'observer ou de chercher un nouvel outil ?",
    "Si ton ratio « apprendre/observer » est >> 5:1, tu es bloqué à l'étage 1. Signal d'alerte : "
    "quand tu penses « il me manque encore un truc », c'est ton cerveau qui fuit l'étage 3."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu cramés un compte 50K. Tu te dis « ma méthode ne marche pas en NY killzone, "
    "je vais rajouter un confluence delta volume ». À 3h du matin tu regardes une vidéo de 47 minutes "
    "sur un nouvel indicateur. Tu te sens productif. Tu n'as rien réglé.",
    "<b>Cible :</b> tu cramés. Tu écris dans ton journal : « mon edge n'a pas changé. À +1700 j'ai senti "
    "une chaleur dans la poitrine, j'ai vu mon préfrontal partir, j'ai joué. Je n'ai pas un problème de signal, "
    "j'ai un problème de système nerveux à +1700. Demain je m'attaque à ça. » Tu coupes Internet. Tu te couches."
]))
story.append(P("Schéma — La boucle du saboteur vs corrigée", h_subsection))
story.extend(ascii_schema("""
   BOUCLE DU SABOTEUR                      BOUCLE CORRIGÉE
   ─────────────────                       ────────────────
       PERTE                                   PERTE
         ▼                                       ▼
   "il manque un truc                    PAUSE 24h obligatoire
    technique"                                   ▼
         ▼                                OBSERVATION CORPORELLE
   Consommation contenu                "qu'a fait MON CORPS ?"
         ▼                                       ▼
   Fausse sensation                      Identification du
   de progrès                            déclencheur précis
         ▼                                       ▼
   Retour écran sans                     Protocole correctif
   rien avoir changé                     écrit dans le journal
         ▼                                       ▼
   MÊME PATTERN                          Nouvelle exécution
         ▼                                       ▼
       PERTE  ◄──── boucle                CONFIANCE BÂTIE
""", accent=ACCENT))
story.append(P("Tableau de compréhension", h_subsection))
story.append(styled_table([
    [C("Concept", cell_gold), C("Chez moi", cell_gold), C("Correction", cell_gold)],
    [C("Étage 1 — savoir"), C("Je connais SMC parfaitement"), C("Stop d'ajouter. Purge 6 semaines.")],
    [C("Étage 2 — savoir-faire"), C("Je gère bien en démo"), C("Identifier ce qui change en réel")],
    [C("Étage 3 — être"), C("Je craque à +1700"), C("Travail somatique + visualisation")],
    [C("Fuite dans le savoir"), C("Vidéo YouTube après chaque crash"), C("Zéro contenu nouveau 6 semaines")],
], [3.3*cm, 6*cm, 6.7*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Exercice 1.A — Inventaire de l'étage 1.</b> Deux colonnes. Gauche : toutes les méthodes/mentors/formations "
    "consommés depuis 18 mois. Droite : ce que chacun a réellement changé dans ton COMPORTEMENT (pas dans ta "
    "connaissance). La droite sera quasi vide. C'est le signal.",
    "<b>Exercice 1.B — Détecteur de fuite.</b> 7 jours. Chaque fois que tu vas chercher un contenu trading : "
    "heure, ce que tu cherchais, ce qui s'est passé juste avant, l'émotion réelle. Tu vas voir : tu consommes "
    "pour fuir une émotion, pas pour apprendre.",
    "<b>Exercice 1.C — Phrase d'ancrage.</b> À la main, majuscules, page 1 de ton cahier : "
    "« MA MÉTHODE EST SUFFISANTE. CE QUI N'EST PAS SUFFISANT, C'EST L'OPÉRATEUR. JE TRAVAILLE L'OPÉRATEUR. » "
    "Relue 30 jours."
]))
story.extend(phrase("On ne perd pas par manque de savoir. On perd parce qu'on n'exécute pas le savoir qu'on a déjà."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(1, 2, "Anatomie du trader perdant",
    "Les cinq patterns destructeurs universels", ACCENT))
story.extend(idee(
    "L'auteur identifie cinq patterns comportementaux que rejouent <b>tous</b> les traders perdants, quel que soit "
    "leur niveau technique. Ces patterns ne sont pas dûs à une mauvaise méthode — ils sont dûs au câblage humain "
    "face à l'incertitude monétaire."
))
story.append(P("Les cinq patterns en détail", h_subsection))
story.append(styled_table([
    [C("#", cell_gold), C("Pattern", cell_gold), C("Mécanique précise", cell_gold)],
    [C("P1"), C("Doubler sur la perte", cell_bold),
     C("Le trade va contre toi. Tu rajoutes pour « baisser le prix moyen ». Espoir déguisé en stratégie. Sur 10 occurrences, 1 te sauve — et te conditionne pour les 9 suivantes.")],
    [C("P2"), C("Couper le gain trop tôt", cell_bold),
     C("Tu coupes à +200 alors que le plan disait +800. Peur de voir le gain disparaître. Tu tronques systématiquement la queue gauche de ta distribution gagnante.")],
    [C("P3"), C("Peur post-perte", cell_bold),
     C("Setup valide après une perte, mais tu n'oses plus. Tu rates le trade compensatoire. Aversion à la perte amplifiée par l'expérience récente.")],
    [C("P4"), C("FOMO compensatoire", cell_bold),
     C("Après une perte, tu prends n'importe quoi pour récupérer. Setup B-grade, taille augmentée, killzone passée. Deuxième perte garantie.")],
    [C("P5"), C("Décaler le SL", cell_bold),
     C("Le marché va contre toi vers ton stop. Tu te dis « il va revenir ». Tu décales « juste un peu ». Et encore. Et c'est trop tard. C'est statistiquement le geste qui détruit le plus de comptes.")],
], [0.8*cm, 4.2*cm, 11*cm]))
story.append(Spacer(1, 8))
story.extend(mecan(
    "Ces patterns ne sont pas des choix. Ce sont des réflexes neurologiques. Le système limbique prend le "
    "contrôle quand l'incertitude monétaire active la menace. Le préfrontal (rationnel, planificateur) est "
    "désactivé. Tu n'es plus le décideur. Tu es le passager. Le seul moyen d'intercepter est de "
    "<b>pré-décider</b> au calme ce que tu feras quand le déclencheur arrive."
))
story.extend(lien([
    "Ton pattern signature combine P2 + P5 + P4. Tu ne coupes pas ton gain à +800 (P2 inversé : tu veux plus). "
    "Tu atteins +1500. Le marché reverse. Tu refuses de couper. Le SL est touché — tu le décales (P5). "
    "Compte stressé. Pour te refaire, tu prends un autre trade B-grade (P4). Compte cramé.",
    "Ce n'est pas une bizarrerie. C'est la séquence la plus documentée du trading. La seule différence entre "
    "toi et un rentable, c'est qu'il a appris à interrompre la séquence là où tu la nourris."
]))
story.extend(exemple([
    "<b>Saboteur (ce que tu fais) :</b> XAUUSD, NY killzone. Tu entres long à 2400, SL à 2397, TP à 2406. "
    "Atteint TP. Tu coupes pas, tu décides de laisser courir. +1500 PnL. Le marché reverse à +1000. "
    "« ça va repartir ». +500. « j'attends que ça revienne à +1200 ». Casse l'entrée. Tu décales le SL "
    "à 2393. Touche 2393. Tu décales à 2390. Compte -800. Drawdown trailing cassé. Compte mort.",
    "<b>Cible (protocole) :</b> TP atteint à 2406, tu coupes. PnL +600. Tu fermes la plateforme. "
    "Tu te lèves. Tu vas pansera ta filly. Si plus tard tu vois que le marché serait monté à +3000, "
    "tu ne regrettes pas — tu as exécuté ton plan. Ce qui suit ton plan ne t'appartient pas."
]))
story.append(P("Schéma — Ton pattern signature en 6 étapes", h_subsection))
story.extend(ascii_schema("""
   1. Entry XAUUSD long          ──►  calme, plan clair
              │
   2. Prix monte vers TP         ──►  léger plaisir, dopamine légère
              │
   3. TP atteint                 ──►  ★ DÉCISION CRUCIALE ★
              │
              ▼
        couper ?  OU  laisser courir ?
              │
   4. Laisser courir →  +1500    ──►  DOPAMINE PIC, préfrontal OFF
              │
   5. Reverse vers 0             ──►  refus de couper (sunk cost)
              │
   6. SL touché → décalage       ──►  ★ ACTE AUTODESTRUCTEUR ★
              │
   ▼ Compte cramé. Pattern bouclé. Pas P2. Pas P5. P2+P5.
""", accent=ACCENT))
story.append(P("Tableau de pré-décision (à imprimer)", h_subsection))
story.append(styled_table([
    [C("Si...", cell_gold), C("Je fais...", cell_gold)],
    [C("TP atteint", cell_bold), C("Je coupe. Sans négocier. Je ferme la plateforme.")],
    [C("Prix touche +1R", cell_bold), C("Je remonte le SL au break-even. Immédiat.")],
    [C("Prix s'approche du SL", cell_bold), C("Je ne décale pas. Je ferme la plateforme. Le SL fait son boulot.")],
    [C("J'ai perdu 2 trades d'affilée", cell_bold), C("Pause 24h. Pas de revanche. Pas de récupération.")],
    [C("Je ressens chaleur/excitation", cell_bold), C("Je quitte la pièce 5 min. Respiration 5-5. Pas de clic.")],
], [5.5*cm, 10.5*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Imprime ce tableau de pré-décision.</b> Affiche-le à côté de l'écran. Plastifie si tu veux. "
    "C'est ton protocole d'urgence pour quand ton préfrontal est OFF.",
    "<b>Logge chaque session :</b> à la fin de chaque jour, sur ton journal, P1 P2 P3 P4 P5 en cinq colonnes. "
    "Tu coches le ou les patterns que tu as déclenchés. Sur 30 jours, tu vois tes 2-3 patterns dominants."
]))
story.extend(alerte(
    "Tu vas être tenté de dire « ouais mais hier c'était différent ». Non. Le contexte change, les patterns "
    "sont identiques. Tant que tu n'auras pas accepté que tu n'as pas un problème unique mais le problème "
    "universel des traders, tu chercheras une solution unique. Tu ne la trouveras pas."
))
story.extend(phrase("Mes patterns ne sont pas miens. Ils sont humains. Je les nomme. Donc je les contre."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(1, 3, "Les quatre forces psychologiques",
    "Kahneman, l'ego, la certitude, la projection", ACCENT))
story.extend(idee(
    "Quatre forces psychologiques se combinent pour rendre chaque trade un piège émotionnel. Tu ne perds pas "
    "parce que tu es stupide. Tu perds parce que tu es <b>humain</b>. Les contrer demande de l'entraînement, "
    "pas de l'intelligence."
))
story.extend(mecan([
    "<b>F1 — Besoin d'avoir raison :</b> l'ego est construit autour de la certitude. Être contredit "
    "(SL touché) est ressenti comme attaque identitaire. Tu décales pour ne pas acter.",
    "<b>F2 — Aversion à la perte (Kahneman) :</b> perdre 100€ fait 2 à 2,5 fois plus mal que gagner 100€ "
    "ne fait plaisir. Asymétrie neurologique documentée. Tu coupes les gains tôt, tu tiens les pertes long.",
    "<b>F3 — Besoin de certitude :</b> le cerveau humain déteste l'aléa. Il invente du « je suis sûr » "
    "là où il n'y a que probabilité. Le marché ne t'a rien promis — c'est ton inconfort qui parle.",
    "<b>F4 — Projection émotionnelle :</b> biais de confirmation. Tu vois sur le chart les indices qui "
    "confirment ton désir et tu ignores ceux qui le contredisent. Un pullback peut être lu comme "
    "« respiration » ou « reversal » — selon ce que tu veux croire."
]))
story.extend(lien([
    "Reprends ton pattern +1500. Décompose avec les 4 forces. <b>F1 :</b> tu as prédit que XAUUSD monterait. "
    "Couper à +1000 = raison <i>partielle</i>. Pas assez pour ton ego. <b>F2 :</b> quand ça reverse de +1500 à "
    "+1000, tu ressens cette baisse comme <b>perte de 500</b>, pas comme gain réduit. Tu refuses d'acter.",
    "<b>F3 :</b> ton cerveau te dit « ça va remonter, je le sens ». Pure invention. <b>F4 :</b> tu lis le "
    "pullback comme respiration normale, alors qu'objectivement le signal est identique à celui d'un reversal.",
    "Ton TBI 2022 amplifie ces réactions. SN dérégulé = ressentis plus forts, plus vites, avec moins de "
    "modulation possible. C'est ton handicap. C'est aussi ta carte : si tu apprends à réguler dans ces "
    "conditions, tu deviendras meilleur qu'un trader neurotypique."
]))
story.append(P("Schéma — Les 4 forces appuient sur toi pendant chaque trade", h_subsection))
story.extend(ascii_schema("""
   F1 — BESOIN D'AVOIR RAISON          F2 — AVERSION À LA PERTE
   "j'ai dit que ça monterait,         "perdre fait 2x plus mal
    si je coupe j'avais à moitié        que gagner — je refuse
    tort"                                d'acter cette perte"
              \\                          /
               \\                        /
                \\                      /
                 \\        TOI         /
                  ►   en trade   ◄
                 /                    \\
                /                      \\
               /                        \\
              /                          \\
   F4 — PROJECTION ÉMOTIONNELLE         F3 — BESOIN DE CERTITUDE
   "ce pullback c'est juste              "ça va repartir,
    une respiration, le bias               je le sens"
    haussier est intact"
""", accent=ACCENT))
story.append(P("Tableau d'identification temps réel", h_subsection))
story.append(styled_table([
    [C("Force", cell_gold), C("Signal interne", cell_gold), C("Antidote immédiat", cell_gold)],
    [C("F1 raison"), C("« si je coupe j'avoue avoir eu tort »"), C("« couper c'est exécuter mon plan, pas avouer »")],
    [C("F2 perte"), C("Refus émotionnel d'acter une perte"), C("« la perte est déjà faite — je l'enregistre »")],
    [C("F3 certitude"), C("« je suis SÛR que... »"), C("« je ne sais pas. Personne ne sait. »")],
    [C("F4 projection"), C("Lecture qui arrange mon désir"), C("Demander : si je n'avais pas de position, je verrais quoi ?")],
], [2.5*cm, 6.5*cm, 7*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Méthode des 4 lettres.</b> Sur ta feuille de session, écris en haut : <b>R / P / C / E</b>. "
    "Pendant le trade, si tu sens un déclencheur lié à une force, tu coches la lettre. C'est de la méta-conscience : "
    "tu ne combats pas la force, tu la nommes. Nommer = rendre opérable.",
    "<b>Question miroir.</b> Quand tu hésites à couper, pose-toi : « si je n'avais aucune position ouverte "
    "actuellement, est-ce que je rentrerais maintenant sur ce setup ? » Si non → tu sors. Cette question "
    "neutralise instantanément F4 et F1."
]))
story.extend(phrase("Je suis humain. Les quatre forces appuient sur tout humain. Je les nomme, je les opère."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(1, 4, "La statistique brutale",
    "80% perdent — par design, pas par accident", ACCENT))
story.extend(idee(
    "70 à 90% des traders particuliers perdent de l'argent. Ce chiffre est cohérent depuis 30 ans, sur tous "
    "marchés, toutes méthodes. Ce n'est pas un problème de marché — c'est un problème humain. "
    "Le marché est une machine à transférer l'argent des impatients aux patients."
))
story.append(P("Pourquoi le chiffre est cohérent", h_subsection))
story.append(P(
    "Les rapports publics des brokers européens (régulation ESMA) montrent 70-90% de comptes retail en perte. "
    "Aux US, mêmes chiffres. En crypto, idem. Forex, futures, actions : idem. Si le problème était la méthode "
    "ou le marché, on verrait des variations. On ne voit aucune variation significative. La constante n'est "
    "donc pas le marché. La constante, c'est l'humain qui trade."
))
story.extend(mecan(
    "Le marché efficient transfère l'argent du côté qui décide mal vers le côté qui décide bien. Les humains, "
    "câblés pour la fuite/agression face à l'incertitude monétaire, décident systématiquement mal. C'est "
    "mécanique. Le marché n'a aucune intention contre toi — il exécute la statistique du comportement humain."
))
story.extend(lien([
    "Tu fais partie des 80%. Pas par accident. Pas par malchance. Pas parce que les prop firms sont conçues "
    "pour te faire échouer (elles ne le sont pas — elles sont des miroirs efficaces). Tu y es parce que tu "
    "trades comme un humain est câblé pour trader.",
    "Tu as une caractéristique aggravante : ton lien identité-performance est très chargé. Quand tu gagnes, "
    "tu existes ; quand tu perds, tu doutes de ta valeur entière. Cette équation rend chaque trade insupportablement "
    "chargé. Le post-coma joue ici. À 22 ans tu as failli mourir. Tu as dû prouver que ton cerveau marchait, "
    "que ton corps marchait. Cette pulsion de preuve t'a sauvé. En trading, elle devient ton ennemi.",
    "La sortie : trader cesse d'être un test identitaire et devient un métier exécuté avec détachement. "
    "Une compétence professionnelle, pas une réhabilitation personnelle."
]))
story.append(P("Schéma — La distribution réelle", h_subsection))
story.extend(ascii_schema("""
   100 traders retail aujourd'hui
   ──────────────────────────────────────────────────────────

   ████████████████████████████████████████  80 = en perte
   ████████████████████████████████████████  (toi inclus)
   ████████████████████████████████████████
   ████████████████████████████████████████

   ████████████  12 = à l'équilibre

   █████ 5 = légèrement rentables

   ███ 3 = vraiment rentables

   ──────────────────────────────────────────────────────────
   La sortie passe par l'admission. Tu ne peux pas devenir
   un des 3 derniers tant que tu n'as pas acté que tu es
   AUJOURD'HUI dans les 80 premiers.
""", accent=ACCENT))
story.append(P("La fuite dans la technique", h_subsection))
story.append(P(
    "Les traders perdants attribuent leur échec à ce qu'ils peuvent <b>changer techniquement</b> : la méthode, "
    "l'indicateur, le timing. C'est confortable. Changer un outil ne te confronte pas à toi-même. Apprendre un "
    "nouveau setup nourrit l'illusion du progrès. Pendant ce temps, le vrai travail — regarder en face tes "
    "mécaniques de saboteur — reste à faire."
))
story.append(styled_table([
    [C("Action confortable", cell_gold), C("Action inconfortable mais nécessaire", cell_gold)],
    [C("Acheter une nouvelle formation"), C("Relire son journal honnêtement")],
    [C("Suivre un mentor sur Twitter"), C("Écrire ses émotions à la main")],
    [C("Tester un nouvel indicateur"), C("Visualiser ses pertes avant de cliquer")],
    [C("Optimiser ses entrées"), C("Pré-décider ses sorties")],
    [C("Lire un livre de plus"), C("Méditer 20 minutes par jour")],
], [8*cm, 8*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Audit honnête.</b> Liste tes cinq derniers contenus de trading consommés ce mois. Pour chacun : "
    "« est-ce que je l'ai consommé pour apprendre quelque chose de précis, ou pour fuir un travail psychologique ? » "
    "Sois honnête. Compte combien étaient de la fuite.",
    "<b>Purge.</b> Pendant 6 semaines : aucun contenu trading purement technique. Pas de nouvelle vidéo, pas de "
    "thread X, pas de Discord. Tu appliques ce que tu sais. Tu n'apprends plus rien de nouveau."
]))
story.extend(alerte(
    "Tu vas vouloir dire « je suis dans les 20% qui vont y arriver ». Possible. Mais tu seras dans les 20% "
    "exactement parce que tu auras arrêté de te raconter ça et commencé à acter que tu es dans les 80% "
    "AUJOURD'HUI. La sortie commence par l'admission."
))
story.extend(phrase("La sortie commence par l'admission. Je suis dans les 80%. Aujourd'hui. Je travaille à en sortir."))
story.append(PageBreak())


print("✓ Livre 1 partie A (modules 1-4) écrits")


# --- MODULE 5 — Pensée probabiliste ---
story.extend(module_header(1, 5, "La pensée probabiliste",
    "Cesser de juger un trade. Juger la distribution.", ACCENT))
story.extend(idee(
    "Le trader rentable joue une distribution sur 100 trades. Le trader perdant juge chaque trade individuellement. "
    "C'est le décalage fondamental. Tu n'es pas un devin — tu es un opérateur de probabilités."
))
story.extend(mecan(
    "Cinq vérités à imprimer dans ton SN : <b>1)</b> tout peut arriver, <b>2)</b> tu n'as pas besoin de savoir ce qui "
    "va se passer pour gagner de l'argent, <b>3)</b> distribution aléatoire entre gagnants et perdants à l'intérieur "
    "d'un edge valide, <b>4)</b> un edge est juste une probabilité plus haute, <b>5)</b> chaque instant du marché "
    "est unique. Tant que ces cinq lignes ne sont pas intégrées corporellement, tu joues émotionnellement."
))
story.extend(lien([
    "Toi tu traites chaque trade XAUUSD comme une mission individuelle, un test. Quand tu cliques, ton cerveau "
    "dit « celui-là il faut qu'il marche ». Cette phrase EST le problème.",
    "Après trois pertes d'affilée, tu changes de timeframe, tu doutes, tu rajoutes un filtre. Tu casses ta propre "
    "série de 100. Tu n'es jamais le casino — tu es toujours le joueur émotionnel. La méditation Dispenza est ton "
    "atout caché ici : tu entraînes l'état de calme non-réactif. C'est exactement l'état du casino. Ne gaspille pas."
]))
story.extend(exemple([
    "<b>Saboteur :</b> 3 pertes XAUUSD ce matin. Tu te dis « ma méthode ne marche plus aujourd'hui ». Tu passes "
    "en H1, tu ajoutes le RSI, tu sors de ta zone. Quatrième trade = catastrophe.",
    "<b>Cible :</b> 3 pertes. Tu coches dans ton journal. Tu reprends ton 4e setup A+ comme si rien ne s'était passé. "
    "Si pas de A+ aujourd'hui : pas de trade. Le PnL d'aujourd'hui ne dit rien sur ton edge. Seuls 100 trades parlent."
]))
story.extend(ascii_schema("""
   GRILLE 100 TRADES — tu joues la distribution, pas l'instance
   ────────────────────────────────────────────────────────────
   1   2   3   4   5   6   7   8   9   10
   ░   █   ░   █   █   ░   █   █   ░   █   ← 6 gagnants / 4 perdants
   ░   ░   █   █   ░   █   █   ░   █   █
   █   █   ░   █   ░   ░   █   █   █   ░
   █   ░   █   ░   █   █   ░   █   █   ░
   ░   █   █   █   ░   █   █   ░   ░   █
   █   ░   ░   █   █   █   ░   █   █   ░
   ░   █   █   ░   █   █   █   ░   █   █
   █   █   ░   █   █   ░   █   █   ░   █
   ░   ░   █   █   █   █   ░   █   █   █
   █   █   █   ░   █   █   █   █   ░   █

   ░ = perte    █ = gain    Distribution émerge sur la longueur.
""", accent=ACCENT))
story.extend(exo([
    "<b>Grille 100 trades.</b> Dessine cette grille dans ton cahier. À chaque trade exécuté selon protocole : "
    "coche en rouge (perte) ou vert (gain). Vise les 100. Tu ne juges rien avant 100. Tu apprends à voir une "
    "distribution, pas 100 jugements individuels.",
    "<b>Question casino.</b> Avant chaque trade : « est-ce que le casino prendrait ce setup ? » Si oui, "
    "tu cliques sans drame. Si non, tu attends."
]))
story.extend(phrase("Je joue 100 trades. Pas celui-ci. Je suis le casino, pas le joueur."))
story.append(PageBreak())


# --- MODULE 6 — Dopamine ---
story.extend(module_header(1, 6, "Le système dopaminergique du trader",
    "Le trader comme junkie — chimie, pas faiblesse", ACCENT))
story.extend(idee(
    "Le trading active les mêmes circuits cérébraux que les machines à sous. C'est l'<b>anticipation</b> du résultat "
    "qui est addictive, pas le résultat lui-même. C'est pour ça que les pertes n'arrêtent pas l'addiction : "
    "le cerveau veut le shoot d'attente suivant."
))
story.extend(mecan([
    "Le décalage de SL est neurochimiquement renforcé. Quand tu décales et que le marché revient, tu reçois "
    "une décharge de soulagement (chute de cortisol) qui agit comme une <b>récompense intermittente</b>. "
    "La psychologie expérimentale a démontré que le renforcement intermittent est la forme de conditionnement "
    "la plus puissante connue. Le décalage qui paye 1 fois sur 10 te conditionne plus solidement que celui "
    "qui paye à chaque fois.",
    "À +1500 PnL, ton préfrontal est désactivé. Tu n'es plus le décideur — tu es le passager du système limbique. "
    "Aucune volonté ne va te sauver à ce moment-là. La discipline ne se gagne pas dans le trade — elle se gagne "
    "AVANT le trade, par pré-décision et par visualisation."
]))
story.extend(lien([
    "Tu es addict à l'intensité depuis ton coma. Tu l'as dit toi-même : le calme te semble vide. Quand un système "
    "nerveux a été soufflé par un TBI et reconstruit en survie/réhabilitation, il calibre son baseline plus haut. "
    "L'intensité = normal. Le calme = anomalie. C'est ton câblage actuel.",
    "Cette caractéristique te dessert en trading. Le trading rentable est lent, ennuyeux, répétitif. Si ton SN "
    "ne tolère pas l'ennui, tu vas le saboter pour récupérer de l'intensité. C'est exactement ce que tu fais "
    "quand tu pousses un winner au-delà du TP ou que tu décales un SL : tu fabriques artificiellement de "
    "l'intensité dans une activité qui devrait être plate."
]))
story.extend(exemple([
    "<b>Saboteur :</b> matin calme, peu de mouvement XAUUSD. Tu ressens un vide. Tu prends un trade sur un setup "
    "B-grade « juste pour voir ». Tu cherches l'intensité, pas le profit. Tu perds. Tu prends un autre. Tu cherches "
    "encore l'intensité. Triple perte avant 11h.",
    "<b>Cible :</b> matin calme. Tu reconnais le vide. Tu te lèves. 20 min de méditation, 15 min de pansage avec "
    "ta filly. Tu reviens. Pas de A+ ce matin → pas de trade. Tu lis. Tu vas à la salle. L'intensité est sortie "
    "ailleurs, pas à l'écran."
]))
story.extend(ascii_schema("""
   BOUCLE DOPAMINE — pourquoi tu reboucles
   ───────────────────────────────────────

      1. ANTICIPATION  ──►  "et si je trade ?"
              │
              ▼
      2. CLIC          ──►  ouverture position
              │
              ▼                                          ★ Le shoot
      3. PIC DOPAMINE  ──►  PnL bouge en ma faveur       n'est pas
              │                                          dans le gain.
              ▼                                          Il est dans
      4. CRASH         ──►  PnL reverse ou SL touché     l'ATTENTE
              │                                          du résultat.
              ▼                                          C'est ça
      5. BESOIN +      ──►  "je me refais"               qui addicte.
              │
              ▼
      6. RECHERCHE     ──►  scan compulsif chart
              │                                          ────────────
              ▼
      RETOUR à 1 (boucle infinie)
""", accent=ACCENT))
story.extend(exo([
    "<b>Plate-life — 20 min/jour.</b> Méditation Dispenza, respiration cohérente (5s in / 5s out), ou marche "
    "sans téléphone. Non négociable. Tu entraînes ton SN à tolérer le calme. C'est de l'augmentation de "
    "capacité de réception du calme.",
    "<b>Intensité OFF-screen — 3x/semaine.</b> Box, équitation cross, sport explosif. Tu décharges l'intensité "
    "hors de l'écran avant qu'elle aille la chercher dedans.",
    "<b>Pré-décision +1500.</b> AVANT de cliquer (donc à PnL=0, préfrontal en ligne), écris : « si j'atteins +1500, "
    "je coupe. Pas de discussion. » Signe la feuille. Affiche-la."
]))
story.extend(alerte(
    "Tu ne vaincras pas ton pattern +1500 par la volonté. C'est de la chimie. À +1500 ton préfrontal est OFF. "
    "Si tu n'as pas pré-décidé au calme, tu fais ce que ta chimie dicte. La discipline ne se gagne pas dans "
    "le trade. Elle se gagne avant."
))
story.extend(phrase("La discipline ne se gagne pas dans le trade. Elle se gagne au calme, avant."))
story.append(PageBreak())


# --- MODULE 7 — Couper les perdants ---
story.extend(module_header(1, 7, "Couper les perdants vite",
    "La compétence numéro un — pas une option", ACCENT))
story.extend(idee(
    "Si on ne devait retenir qu'une seule compétence du trading, ce serait celle-ci. Couper vite ses pertes "
    "est l'écart le plus net entre rentables et perdants. Avant la lecture du marché. Avant le money management. "
    "Le décalage de SL est statistiquement le geste qui détruit le plus de comptes."
))
story.append(P("Pourquoi une perte non-coupée n'est pas linéaire", h_subsection))
story.append(P(
    "Quatre effets cumulés. <b>1)</b> Elle prend du capital. <b>2)</b> Elle prend du temps mental — tu "
    "rumines pendant des heures. <b>3)</b> Elle prend de l'attention sur les setups suivants — tu rates des A+. "
    "<b>4)</b> Elle conditionne ton cerveau à accepter des pertes plus grandes au prochain tour. C'est cette "
    "quatrième qui te tue à long terme."
))
story.extend(lien([
    "Ton pattern de décalage est documenté. Tu te dis « il va revenir », tu décales « juste un peu ». Cette phrase "
    "est ton mensonge personnel. Le marché n'a pas besoin de temps. Il a besoin que tu te trompes pour empocher "
    "ton SL. C'est neutre. Tu personnalises ce qui n'est pas personnel.",
    "Facteur aggravant : les prop firms. Apex, Topstep, Alpha ont des règles de trailing drawdown. Tu décales un SL, "
    "le marché te tape -300, tu décales encore, -600. À -800 tu casses la règle. Compte mort. Avec les frais "
    "d'inscription, tu es à -1000 à -1500 réels. La prop firm parie sur ce mécanisme — c'est son business model. "
    "<b>Tu peux refuser d'être le carburant.</b>"
]))
story.append(P("Protocole anti-décalage en 4 niveaux", h_subsection))
story.extend(ascii_schema("""
   Niveau 1 : SL placé AVEC l'ordre. Non négociable.

   Niveau 2 : Alerte sonore TradingView placée 5 pips avant le SL.
              Quand ça sonne, tu sais que ça va se passer. Tu te prépares.

   Niveau 3 : Engagement signé. Sur ta feuille : "JE NE DÉCALE PAS DE SL
              AUJOURD'HUI. — signé Marien, [date]." Affichée au mur.

   Niveau 4 : Close the platform. Tu fermes l'app. Tu sors physiquement
              de la pièce. Le SL fait son boulot sans toi. Tu reviens
              30 min plus tard. Tu vois le résultat. C'est fini.
""", accent=ACCENT))
story.extend(exo([
    "<b>Les 4 niveaux dès demain.</b> Tu commences au niveau 1. Si tu sens que tu vas décaler, tu passes au 2. "
    "Si insuffisant, au 3. Si encore insuffisant, au 4. Tu n'as pas le droit de décaler.",
    "<b>Log par session.</b> Bas de chaque page de journal : croix verte (pas décalé) ou rouge (décalé). "
    "Vise <b>zéro rouge sur 20 sessions consécutives</b>. Si tu casses une fois, tu repars à zéro. Sans drame."
]))
story.extend(alerte(
    "Le décalage qui paye 1 fois sur 10 te conditionne PLUS solidement que celui qui paye à chaque fois. "
    "C'est le renforcement intermittent — le mode de conditionnement le plus puissant connu. La règle est : "
    "zéro décalage. Pas même un."
))
story.extend(phrase("Mon SL ne bouge que vers le profit. Jamais vers la perte. Jamais. Une seule règle, zéro exception."))
story.append(PageBreak())


# --- MODULE 8 — Journal ---
story.extend(module_header(1, 8, "Le journal manuscrit",
    "L'outil de transformation numéro un", ACCENT))
story.extend(idee(
    "Le journal de trading est l'outil de transformation le plus puissant à ta disposition. Pas un journal de PnL "
    "(n'importe quel logiciel fait ça). Un journal <b>introspectif manuscrit</b>, où tu écris ton état émotionnel "
    "avant, pendant et après chaque trade et chaque session."
))
story.append(P("Pourquoi manuscrit, pas tablette ni Notion", h_subsection))
story.append(P(
    "Écrire à la main mobilise différemment le cerveau. Plus lent → réflexion plus profonde. Plus engageant → "
    "tu peux moins fuir. Trois fonctions : <b>1)</b> acter ce qui s'est passé (mémoire externe), "
    "<b>2)</b> repérer tes patterns à travers le temps (l'analyse rétrospective est l'endroit où la transformation "
    "se produit), <b>3)</b> construire l'identité du trader que tu deviens (en t'observant écrire, tu deviens "
    "cette personne)."
))
story.extend(lien([
    "Toi tu prends des notes sur ton téléphone, parfois. Ou rien. Tu te promets de tenir un journal et tu craques "
    "après trois jours. C'est l'erreur classique. Tu rates l'outil dont tu as précisément besoin.",
    "Pour quelqu'un qui pratique Dispenza, le journal est la version écrite de ta méditation. Observation consciente "
    "de tes patterns en mode écrit. Tu installes la position d'observateur. À force, tu deviens cet observateur "
    "même pendant le trade — c'est là que tu reprends le contrôle des décisions."
]))
story.append(P("Template à recopier à la main (4 sections)", h_subsection))
story.append(styled_table([
    [C("Moment", cell_gold), C("Durée", cell_gold), C("Contenu clé", cell_gold)],
    [C("Avant session", cell_bold), C("5 min"),
     C("État émotionnel 1-10, sommeil, énergie, killzone visée, bias macro, taille max, phrase d'ancrage.")],
    [C("Pour chaque trade", cell_bold), C("2 min"),
     C("Heure, direction, entrée/SL/TP, justification SMC (1 phrase), visu 90s OUI/NON, état corps, BE déplacé OUI/NON, résultat, décalage SL OUI/NON, plateforme fermée OUI/NON.")],
    [C("Après session", cell_bold), C("10 min"),
     C("Nombre trades, gagnants/perdants, PnL, protocole respecté OUI/NON, pattern déclenché (P1-P5), voix dominante, émotion principale, vote du jour.")],
    [C("Revue hebdo", cell_bold), C("30 min"),
     C("Sessions, win rate, PnL, pattern le plus fréquent, vote semaine (chirurgical / contre), 3 leçons, engagement semaine suivante.")],
], [3*cm, 1.5*cm, 11.5*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Cette semaine — achète le cahier.</b> Pas un carnet bas de gamme. Un VRAI cahier. Cuir, papier épais, "
    "ce que tu veux mais que tu RESPECTES. Page 1 (à la main) : « Cahier de Marien, trader chirurgical en formation. "
    "Ouvert le [date]. »",
    "<b>Règle absolue.</b> Pas de journal du soir = pas de session le lendemain. Le journal est la condition "
    "d'accès à l'écran. Pas négociable."
]))
story.extend(phrase("Le journal n'est pas joli. Il n'a pas besoin de l'être. Il a besoin d'être FAIT."))
story.append(PageBreak())


# --- MODULE 9 — Inner game ---
story.extend(module_header(1, 9, "L'inner game",
    "Le vrai adversaire est intérieur — pas le marché", ACCENT))
story.extend(idee(
    "L'adversaire que tu affrontes n'est pas l'extérieur (le marché, les market makers, les prop firms). "
    "C'est une voix intérieure qui commente, juge, déstabilise. Cette voix est constamment active. "
    "Le but n'est pas de la faire taire (impossible) — c'est de l'<b>observer sans lui obéir</b>."
))
story.extend(mecan(
    "La conscience qui observe la voix est différente de la voix. Quand tu identifies cette différence, "
    "tu déposes une distance. Cette distance est le siège de la liberté. Sans cette distance, tu ES la voix — "
    "tu obéis sans même réaliser que tu obéis. C'est exactement la posture que la méditation Dispenza t'entraîne "
    "à installer le matin."
))
story.extend(lien([
    "Ta voix typique en trade ressemble à ça : « OK setup propre, je rentre. Allez ça doit marcher celui-là. "
    "Ah ça monte, peut-être augmenter la taille... non reste calme. +400, +600, +800. C'est mon TP. Mais regarde "
    "la momentum, si je coupe je vais regretter. +1500. Ouais voilà. Oh ça ralentit. Bon respiration. +1200. "
    "Ouais temporaire. +400. Putain. Non ça va repartir. -200. Je décale le SL, juste un retest. -800. Compte mort. »",
    "Cette voix te ment à chaque phrase, mais sur le ton de l'évidence. Elle est crédible parce qu'elle EST toi — "
    "une partie de toi. Le travail : l'entendre comme une radio en arrière-plan, pas comme la commande de l'avion. "
    "Pendant le trade, dis à voix basse : « j'entends la voix, je continue le plan ». Tu casses l'identification."
]))
story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════╗
   ║                  L'OBSERVATEUR                    ║
   ║              (celui qui ENTEND la voix)           ║
   ║                                                   ║
   ║      ┌─────────┐    ┌─────────┐    ┌─────────┐  ║
   ║      │ "il va  │    │ "tu vas │    │ "encore │  ║
   ║      │remonter"│    │ rater"  │    │ +100"   │  ║
   ║      └─────────┘    └─────────┘    └─────────┘  ║
   ║                                                   ║
   ║   Tu n'es PAS les bulles. Tu es CELUI QUI VOIT  ║
   ║   les bulles. Cette distinction est ta liberté.  ║
   ╚══════════════════════════════════════════════════╝
""", accent=ACCENT))
story.extend(exo([
    "<b>Nommer la voix.</b> Donne un prénom à ta voix de saboteur. Quand tu l'entends : « tiens, voilà [prénom] qui "
    "essaye de me faire décaler ». Le prénom externalise la voix. Tu n'es plus elle, tu es face à elle.",
    "<b>Phrase de rupture.</b> Pendant chaque trade, à voix basse : « voix notée, je continue le plan ». "
    "Cette phrase casse l'identification. À répéter 50 fois par session si nécessaire.",
    "<b>Méditation 20 min/matin.</b> Tu observes tes pensées sans les suivre. Tu entraînes le muscle. "
    "Sans cette pratique matinale, tu n'auras pas le muscle l'après-midi devant l'écran."
]))
story.extend(phrase("Je ne suis pas la voix. Je suis celui qui entend la voix. C'est ma liberté."))
story.append(PageBreak())


# --- MODULE 10 — Identité ---
story.extend(module_header(1, 10, "Le changement identitaire en 3 niveaux",
    "Devenir le trader — pas l'imiter", ACCENT))
story.extend(idee(
    "Trois niveaux de changement, du plus instable au plus stable : <b>Résultat</b> (« je veux gagner 10 000€ ») → "
    "<b>Processus</b> (« j'exécute mon protocole 100 trades ») → <b>Identité</b> (« je SUIS un trader chirurgical »). "
    "Seul le niveau identité produit un changement durable."
))
story.extend(mecan(
    "Au niveau résultat, tu dépends de variables hors de ton contrôle. Au niveau processus, tu contrôles, "
    "mais ça demande de la discipline constante. Au niveau identité, le comportement <b>découle naturellement</b> "
    "de qui tu es. Tu n'as plus à te forcer. La cohérence avec ton identité fait le travail. Chaque action "
    "alignée est un vote pour cette identité ; chaque action désalignée est un vote contre. À force de votes, "
    "l'identité devient majoritaire dans ta perception de toi."
))
story.extend(lien([
    "Ton identité de trader est instable aujourd'hui. Quand tu gagnes, tu es « un trader qui réussit ». Quand "
    "tu perds, tu es « un trader qui galère ». Ton identité fluctue avec ton PnL. L'opérateur change selon le "
    "résultat de l'opération précédente — ingouvernable.",
    "Identité cible proposée : <b>« Je suis un trader chirurgical. »</b> Chirurgical = précis, calme, ennuyeux "
    "de l'extérieur, geste propre. Un chirurgien ne « croit » pas qu'une opération va marcher. Il ouvre, fait "
    "le geste, referme. Il ne double pas sur une perte. Il ne décale pas son SL. Ces gestes n'ont aucun sens "
    "pour qui il est. Tu vois comment l'identité résout le problème de discipline ? Tu n'as pas à te forcer — "
    "c'est juste qui tu es.",
    "Tu l'as déjà fait pour l'équitation. Tu ne t'es pas réveillé un matin cavalier compétitif. Tu as fait des "
    "milliers d'heures de selle. À un moment, l'identité « cavalier » est devenue ta vérité, pas un projet. "
    "Le trading suit la même loi."
]))
story.extend(ascii_schema("""
                    PYRAMIDE DU CHANGEMENT
                    ───────────────────────

                            ▲ IDENTITÉ ▲
                          "Je suis trader
                           chirurgical"
                         ◄─ le seul niveau
                           durable. Ici le
                           comportement coule
                           tout seul. ─►

                        ─────────────────
                            PROCESSUS
                       "J'exécute mon plan"
                         ◄─ stable tant que
                           motivation tient ─►

                    ──────────────────────────
                            RÉSULTAT
                      "Je veux gagner 10000€"
                       ◄─ instable, hors de
                          ton contrôle ─►
                    ──────────────────────────

   ↑ Plus tu MONTES dans la pyramide,
     plus le changement est PROFOND et DURABLE.
""", accent=ACCENT))
story.extend(exo([
    "<b>Page identité.</b> Ouvre une page dédiée dans ton journal. En majuscules : « JE SUIS UN TRADER CHIRURGICAL. » "
    "Avant chaque session, tu relis. Avant chaque trade : « est-ce qu'un trader chirurgical ferait ce clic ? ». "
    "Si non, tu ne cliques pas.",
    "<b>Comptage des votes.</b> En fin de journée, dans ton journal : « Aujourd'hui combien de votes "
    "CHIRURGICAL j'ai déposés ? Combien de votes CONTRE ? » Tu fais le ratio sur la semaine. Tu vois "
    "l'identité s'installer ou pas."
]))
story.extend(phrase("Je ne gagne pas pour devenir rentable. Je SUIS rentable, donc je gagne. L'ordre compte."))
story.append(PageBreak())


# ============================================================
# LIVRE 1 — SYNTHÈSE COMPLÈTE (Bloc E)
# ============================================================
story.append(P("E.  Synthèse complète — Livre 1", h_section))

story.append(P("1. Les 10 idées les plus importantes", h_subsection))
ideas_10 = [
    "L'edge n'est pas dans la méthode. Il est dans l'exécution de la méthode sous pression nerveuse.",
    "Le meilleur trader n'est pas celui qui gagne mieux. C'est celui qui perd mieux.",
    "Tu joues une distribution sur 100 trades. Jamais un trade individuel.",
    "Les patterns destructeurs (P1-P5) sont humains, pas personnels. Tu les nommes pour les contrer.",
    "Quatre forces psychologiques (raison, perte, certitude, projection) appuient sur tout humain qui trade.",
    "La discipline ne se gagne pas dans le trade. Elle se gagne au calme avant le trade.",
    "Le SL est sacré. Il ne bouge que vers le profit, jamais vers la perte.",
    "Couper vite ses pertes est la compétence n°1. Avant tout le reste.",
    "Le journal manuscrit est l'outil de transformation. Pas un logiciel — un cahier.",
    "L'identité change le comportement. Pas l'inverse. Tu deviens, tu ne forces pas.",
]
for i, idea in enumerate(ideas_10, 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("2. Les 10 erreurs que ce livre t'aide à arrêter", h_subsection))
errors_10 = [
    "Croire qu'un nouveau setup va régler ton problème comportemental.",
    "Juger ton edge sur 3-5 trades au lieu de 100.",
    "Décaler un SL parce que « ça va revenir ».",
    "Pousser un winner au-delà du TP par avidité.",
    "Prendre un trade B-grade pour récupérer une perte.",
    "Consommer du contenu trading pour fuir une émotion.",
    "Confondre confiance et euphorie après une bonne journée.",
    "Trader pour ressentir au lieu d'exécuter.",
    "Faire dépendre ton identité du PnL de la journée.",
    "Tenir un journal numérique au lieu d'un cahier manuscrit.",
]
for i, err in enumerate(errors_10, 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("3. Les 10 nouvelles règles de vie / trading", h_subsection))
rules_10 = [
    "Je joue une série de 100, pas un trade.",
    "Mon SL est sacré. Il ne bouge que vers le profit.",
    "Je coupe à mon TP. Sans négocier. Sans regret.",
    "Je pré-vis chaque trade 90 secondes avant de cliquer.",
    "Je ferme la plateforme dès que les ordres sont placés.",
    "Je tiens un journal manuscrit. Pas de journal = pas de session.",
    "Je ne consomme aucun contenu trading nouveau pendant 6 semaines.",
    "Je nourris ma vie hors écran chaque jour (ATHÉNA, chevaux, box).",
    "Je médite 20 min chaque matin. Sans exception.",
    "Je SUIS un trader chirurgical. Chaque clic est un vote pour cette identité.",
]
for i, rule in enumerate(rules_10, 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 10))

story.append(P("4. Protocole d'application — 7 jours", h_subsection))
story.append(styled_table([
    [C("Jour", cell_gold), C("Objectif", cell_gold), C("Exercice", cell_gold), C("Application", cell_gold), C("Question du soir", cell_gold)],
    [C("J1", cell_bold), C("Diagnostic"),
     C("Inventaire étage 1"), C("Lire modules 1-2"),
     C("Combien de méthodes j'ai testées ?")],
    [C("J2", cell_bold), C("Achat cahier"),
     C("Page 1 manuscrite"), C("Aucun trade"),
     C("Pourquoi je résiste à écrire à la main ?")],
    [C("J3", cell_bold), C("Pré-décisions"),
     C("Tableau « si... je fais »"), C("Affichage mur"),
     C("Quelle pré-décision je vais oublier ?")],
    [C("J4", cell_bold), C("4 forces"),
     C("R/P/C/E sur feuille"), C("Démo + log"),
     C("Quelle force domine chez moi ?")],
    [C("J5", cell_bold), C("Grille 100"),
     C("Dessiner grille 100"), C("Démo, cocher"),
     C("Je vois la distribution ou je juge l'instance ?")],
    [C("J6", cell_bold), C("Plate-life"),
     C("20 min méditation + sport"), C("Pas de trade"),
     C("Est-ce que le calme m'a paru vide ?")],
    [C("J7", cell_bold), C("Identité"),
     C("Page « JE SUIS chirurgical »"), C("Revue J1-J6"),
     C("Combien de votes chirurgical j'ai déposés ?")],
], [0.8*cm, 2.4*cm, 3.5*cm, 3.5*cm, 5.8*cm]))
story.append(PageBreak())

story.append(P("5. Fiche visuelle finale — à imprimer", h_subsection))
story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║          BEST LOSER WINS  —  FICHE D'ANCRAGE             ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Je perds mieux pour gagner mieux.                       ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Décaler le SL. Pousser au-delà du TP. Trader            ║
   ║    pour ressentir.                                         ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE CHEZ MOI                                  ║
   ║    - Chaleur dans la poitrine                              ║
   ║    - Souffle court                                         ║
   ║    - Phrase « ça va remonter »                             ║
   ║    - Envie de prendre un autre trade pour me refaire       ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Je nomme l'état (R / P / C / E)                      ║
   ║    2. Je respire 5-5 pendant 30s                           ║
   ║    3. Je vérifie mon pré-engagement écrit                  ║
   ║    4. Si je sens que je vais tricher : close the platform  ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je SUIS un trader chirurgical."                        ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Pré-décider à PnL=0 ce que je fais à PnL=+1500.         ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Une série de 100 trades. Pas un trade.                  ║
   ║    Le SL ne bouge que vers le profit.                      ║
   ║    Je ferme la plateforme dès que les ordres sont placés.  ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

# Checklist Livre 1
story.append(P("Checklist finale — Livre 1", h_subsection))
story.append(styled_table([
    [C("Module", cell_gold), C("Idée clé", cell_gold), C("Exo donné", cell_gold)],
    [C("1 Parcours initiatique"), C("Edge = exécution, pas méthode"), C("✓")],
    [C("2 Anatomie perdant"), C("5 patterns destructeurs universels"), C("✓")],
    [C("3 4 forces psy"), C("Raison/Perte/Certitude/Projection"), C("✓")],
    [C("4 Statistique brutale"), C("80% perdent par design"), C("✓")],
    [C("5 Pensée probabiliste"), C("100 trades, pas 1 trade"), C("✓")],
    [C("6 Dopamine"), C("Discipline avant trade, pas pendant"), C("✓")],
    [C("7 Couper vite"), C("SL sacré, jamais vers la perte"), C("✓")],
    [C("8 Journal"), C("Manuscrit = transformation"), C("✓")],
    [C("9 Inner game"), C("Observer la voix, ne pas obéir"), C("✓")],
    [C("10 Identité"), C("Je suis, donc je fais"), C("✓")],
], [4.5*cm, 8.5*cm, 3*cm]))

story.append(PageBreak())

print("✓ Livre 1 complet (10 modules + synthèse)")


# ============================================================
# LIVRE 2 — UN MONDE SOUS DOPAMINE (Anna Lembke)
# ============================================================
_current_book_color[0] = BOOK_COLORS[1]
ACCENT = BOOK_COLORS[1]

story.extend(book_separator_page(
    2, "Un monde sous dopamine", "Anna Lembke", "Dopamine Nation", 2021, ACCENT,
    quote='« Le plaisir et la douleur sont sur la même bascule.<br/>Plus tu pousses d\'un côté, plus tu seras tiré de l\'autre. »',
    subtitle="Comment trouver l'équilibre dans une époque d'excès"
))

story.extend(book_intro_header(2, "Un monde sous dopamine", "Anna Lembke — 2021", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "Anna Lembke est psychiatre spécialisée en addiction à Stanford. Ce livre vulgarise ce que la science "
    "de l'addiction comprend en 2020. Le concept central — le mécanisme dopaminergique du plaisir et de la "
    "douleur — est <b>exactement ton problème principal</b>."
))
story.append(P(
    "Tu n'as pas de problème d'argent. Tu n'as pas de problème de marché. Tu as un problème de <b>chimie</b>. "
    "Ton pattern +1500 PnL n'est pas une faiblesse mentale, c'est une boucle dopaminergique. Le décalage de SL "
    "n'est pas une décision rationnelle, c'est un renforcement intermittent. Lembke te donne la carte neurochimique "
    "de ce qui se passe dans ton cerveau quand tu trades."
))
story.append(P(
    "Tu cumules en plus deux facteurs aggravants : <b>1)</b> un TBI 2022 qui a probablement modifié ta sensibilité "
    "dopaminergique baseline, <b>2)</b> une attirance documentée pour l'intensité (le calme te semble vide). "
    "Ce livre est ton manuel de réparation neurochimique."
))
story.append(P(
    "Lis-le après Hougaard car il te donne le <b>pourquoi</b> de ce que Hougaard décrit. Hougaard te dit "
    "<i>quoi</i> ; Lembke te dit <i>comment ça marche dans le cerveau</i>."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Le plaisir et la douleur partagent le même circuit cérébral, qui fonctionne comme une bascule.</b>', pull_quote))
story.append(P(
    "Quand tu actives le circuit de plaisir (dopamine), ton cerveau active <b>en compensation</b> un retour vers la "
    "douleur pour rétablir l'équilibre. C'est ce qu'on appelle l'homéostasie. Conséquence : plus tu cherches "
    "intensément le plaisir, plus tu seras profondément en douleur après. Et plus tu vas chercher à nouveau du "
    "plaisir pour fuir cette douleur. La boucle de l'addiction est entièrement dans ce mécanisme."
))
story.append(P("Les mécanismes neurochimiques exposés", h_subsection))
story.append(P(
    "<b>1. Bascule plaisir-douleur :</b> mécanisme cérébral d'homéostasie. Chaque pic dopaminergique est suivi "
    "d'un déficit dopaminergique équivalent. <b>2. Tolérance :</b> à force de stimulation, le baseline "
    "dopaminergique baisse. Il faut plus pour ressentir pareil. <b>3. Anhédonie :</b> au stade avancé, "
    "le baseline est si bas que rien ne procure plus de plaisir naturel. <b>4. Renforcement intermittent :</b> "
    "les récompenses imprévisibles addictent plus que les récompenses régulières. <b>5. Honte productive vs honte "
    "destructive :</b> l'admission consciente d'une addiction est libératrice ; la honte cachée est aggravante."
))
story.append(P("Les solutions proposées", h_subsection))
story.append(P(
    "<b>Le jeûne dopaminergique</b> (4 semaines minimum sans la substance/comportement addictif) pour laisser "
    "le baseline remonter. <b>L'inconfort volontaire</b> (cold exposure, sport intense, restriction délibérée) "
    "pour entraîner la voie dopaminergique opposée — celle qui produit du plaisir <i>après</i> la douleur "
    "endurée. <b>L'honnêteté radicale</b> (auprès d'un thérapeute, d'un coach, d'un proche) qui désactive "
    "le système de honte cachée. <b>Le compteur de pleine présence</b> (mindfulness) qui re-sensibilise au "
    "plaisir naturel ordinaire."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Très anecdotique (cas cliniques répétés). Tu peux trouver les chapitres de cas un peu longs. La science "
    "y est vulgarisée — pour creuser plus, il faut lire Robert Sapolsky ou Carl Hart. Pas spécifique au trading, "
    "donc tu fais le pont toi-même (c'est ce que ce manuel fait pour toi). Le concept de « jeûne dopaminergique » "
    "est parfois critiqué scientifiquement comme simplification — mais le mécanisme général de remontée du baseline "
    "lors d'une abstention prolongée est solide."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Un monde sous dopamine",
    [
        {"label": "BASCULE", "leaves": ["plaisir/douleur", "compensation auto"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["tolérance", "anhédonie", "renforcement intermittent"], "color": ACCENT},
        {"label": "SOLUTIONS", "leaves": ["jeûne 4 sem", "inconfort volontaire", "honnêteté radicale"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Le mécanisme neurochimique et ses solutions structurées.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(2, 1, "La bascule plaisir-douleur",
    "Le mécanisme central — homéostasie neurochimique", ACCENT))
story.extend(idee(
    "Le plaisir et la douleur occupent le même réseau cérébral. Chaque fois que tu actives le plaisir, "
    "ton cerveau active automatiquement la douleur en compensation, pour rétablir l'équilibre. "
    "C'est mécanique. Ce n'est pas une question de morale ou de discipline."
))
story.extend(mecan(
    "Imagine une balance. D'un côté, le plaisir. De l'autre, la douleur. Quand tu fais un pic dopaminergique "
    "(gain XAUUSD, pornographie, alcool, sucre, validation sociale), le côté plaisir s'enfonce. Le cerveau, "
    "obsédé par l'équilibre, pousse alors mécaniquement le côté douleur. Conclusion : <b>chaque grand plaisir "
    "produit une grande douleur compensatoire</b>. C'est ce qu'on appelle l'after-shock dopaminergique. "
    "Plus tu pousses fort d'un côté, plus tu seras tiré fort de l'autre."
))
story.extend(lien([
    "Reprends ton pattern. +1500 PnL → pic dopaminergique massif. Ton cerveau enregistre. Trois heures plus tard, "
    "tu ressens un vide. Tu ne comprends pas pourquoi — tu as gagné. Tu cherches à compenser le vide en reprenant "
    "un trade « pour le plaisir ». Tu reprends un B-grade. Tu perds. Le vide devient creux. Tu reprends. "
    "Tu crames le compte. <b>Ce n'est pas le trade qui te détruit. C'est le rebond après le pic.</b>",
    "Cette logique explique aussi tes lendemains. Une journée de +3000 est souvent suivie d'une journée de -3500. "
    "Ce n'est pas de la malchance — c'est le rebond. Ton baseline dopaminergique est en dette après le pic, "
    "ton cerveau cherche à payer cette dette par n'importe quel moyen."
]))
story.extend(exemple([
    "<b>Saboteur :</b> Lundi tu fais +2000. Tu fermes la plateforme euphorique. Tu te sens roi. Tu pars en "
    "soirée. Tu rentres tard. Mardi tu te lèves vaseux, vide. Tu ouvres la plateforme. Le vide te dégoûte. "
    "Tu veux un autre pic. Tu prends un trade B-grade en H1. Tu te crashes à -1500. La bascule a fait son boulot.",
    "<b>Cible :</b> Lundi +2000. Tu reconnais le pic. Tu sais que le rebond arrive. Mardi tu PRÉ-DÉCIDES, "
    "le matin, que tu ne tradera PAS. Tu vas à la salle. Tu pansa ta filly. Tu lis. Tu acceptes le creux. "
    "Le creux passe. Mercredi tu reprends, en calme, avec un nouveau setup A+. Tu n'as pas alimenté la bascule."
]))
story.extend(ascii_schema("""
   LA BASCULE PLAISIR ↔ DOULEUR
   ────────────────────────────

   État neutre (baseline) — la bascule est horizontale

        DOULEUR  ◄════════════════════════════►  PLAISIR
                          │ balance

   Tu cherches du plaisir (gain trade, dopamine)

        DOULEUR  ◄════════                      ★ PLAISIR
                            ───────────────────►
   Le cerveau compense automatiquement

        ★ DOULEUR                       ◄════ PLAISIR
                      ◄─────────────────
   Tu ressens le rebond, tu cherches encore du plaisir...

        DOULEUR  ◄════════                      ★ PLAISIR
                            ───────────────────►
   ...le rebond suivant sera plus fort.
""", accent=ACCENT))
story.extend(exo([
    "<b>Cartographie 7 jours.</b> Pour chaque jour : note ton pic dopaminergique principal (trade gagnant, "
    "alcool, sucre, validation, etc.) ET le rebond qui a suivi 2-12h plus tard. Tu vas voir le pattern.",
    "<b>Règle anti-rebond.</b> Après chaque journée à +X PnL au-dessus de ta moyenne : pause obligatoire le "
    "lendemain. Pas de trade. Tu attends que le baseline remonte tout seul."
]))
story.extend(phrase("Chaque pic produit un creux équivalent. Le creux n'est pas hostile — il est mécanique."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(2, 2, "Tolérance et anhédonie",
    "Pourquoi tu en as besoin de toujours plus", ACCENT))
story.extend(idee(
    "À force de stimulation dopaminergique répétée, ton cerveau diminue le nombre de récepteurs dopaminergiques "
    "actifs (down-regulation). Conséquence : il te faut une stimulation plus forte pour ressentir pareil. "
    "C'est la tolérance. Au stade avancé, le baseline est si bas que les plaisirs naturels ordinaires "
    "(une marche, un repas, une discussion) ne produisent plus rien : c'est l'anhédonie."
))
story.extend(mecan(
    "Mécaniquement : le cerveau perçoit l'excès de dopamine comme un déséquilibre. Pour se protéger, il "
    "diminue sa propre capacité à recevoir la dopamine (réduction des récepteurs D2). Tu as donc besoin "
    "d'envoyer plus de dopamine pour produire le même signal. Cycle : tu pousses plus → baseline baisse → "
    "tu pousses encore plus → baseline encore plus bas. Au bout : rien ne te fait rien. Seul ce qui est "
    "extrême produit encore une sensation."
))
story.extend(lien([
    "Ton signal d'anhédonie : « le calme me semble vide ». Cette phrase n'est pas un trait de caractère. "
    "C'est un diagnostic neurochimique. Ton baseline dopaminergique est bas — sans doute en partie depuis "
    "ton TBI (les traumas crâniens affectent fréquemment les systèmes dopaminergiques), et amplifié par "
    "tes stimulations actuelles (trading, écrans, intensité recherchée).",
    "Concrètement pour toi : tu ne peux plus tolérer un setup XAUUSD qui rapporte tranquillement +600 sans "
    "vouloir le pousser à +1500. +600 ne suffit pas à ton cerveau pour produire un signal de plaisir suffisant. "
    "Il en faut plus. C'est de la tolérance pure. Tu ne décides pas ça — ton cerveau le réclame."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu prends un setup XAUUSD A+, TP à +600. Atteint. Tu coupes pas — « ça ne vaut pas le coup ». "
    "Tu laisses courir. Le pic à +1500 produit enfin une sensation. Mais le rebond te détruit.",
    "<b>Cible :</b> tu coupes à +600. Tu reconnais que ton cerveau réclame plus. Tu nommes : « tolérance — "
    "je n'ai pas BESOIN de plus, mon cerveau réclame plus ». Tu fermes la plateforme. Tu laisses ton baseline "
    "remonter. Dans 4 semaines, +600 te procurera de nouveau une vraie satisfaction."
]))
story.extend(ascii_schema("""
   TOLÉRANCE DOPAMINERGIQUE — la dette qui s'accumule
   ──────────────────────────────────────────────────

   Mois 0 (baseline sain)
   ░░░░░░░░░░░░░░░░░░░░  +600 PnL produit un VRAI plaisir.

   Mois 6 (stimulations répétées)
   ░░░░░░░░░░░░          +600 ne fait plus rien. Il faut +1500.

   Mois 12 (sans pause)
   ░░░░░░                +1500 ne fait plus rien. Il faut +3000.

   Mois 18 (cycle infernal)
   ░░                    Plus rien ne fait rien. Anhédonie installée.

   Mois 0 + 12 semaines de jeûne dopaminergique
   ░░░░░░░░░░░░░░░░░░░░  Baseline restauré. +600 redevient plaisir.
""", accent=ACCENT))
story.extend(exo([
    "<b>Test de tolérance.</b> Demande-toi : qu'est-ce qui me procurait du plaisir avant 2022, qui ne m'en "
    "procure plus aujourd'hui ? Liste 5 choses. Ces 5 choses sont ta mesure de baseline. Si tu ne ressens "
    "plus rien sur elles, tu es en tolérance avancée.",
    "<b>Restauration de plaisirs simples.</b> 14 jours d'expérimentation : chaque jour, faire UNE chose simple "
    "et lente (pansage 30 min, marche sans téléphone 45 min, repas sans écran). Évalue 1-10 le plaisir ressenti. "
    "Tu vas voir : ça remonte progressivement."
]))
story.extend(phrase("Mon cerveau réclame plus. Je n'ai pas besoin de plus. Je laisse remonter mon baseline."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(2, 3, "Le jeûne dopaminergique",
    "Le protocole de réparation neurochimique", ACCENT))
story.extend(idee(
    "Pour restaurer ton baseline dopaminergique, il faut t'abstenir totalement de la substance ou du "
    "comportement addictif pendant <b>au minimum 4 semaines</b> (idéalement 12 semaines). Pendant cette "
    "période, le cerveau remonte progressivement le nombre de récepteurs D2. Le baseline redevient sensible. "
    "C'est de la biologie, pas du mental."
))
story.extend(mecan(
    "Les 14 premiers jours sont les plus durs. Le cerveau, sevré de sa stimulation habituelle, produit un état "
    "de manque caractérisé : irritabilité, ennui intense, anxiété diffuse, troubles du sommeil, parfois "
    "symptômes physiques. Ce n'est pas une preuve que le sevrage est mauvais — c'est la signature même du "
    "sevrage. Les jours 14-28 sont une phase de stabilisation. À partir du jour 28, le baseline commence "
    "à remonter visiblement."
))
story.extend(lien([
    "Pour ton cas, le « jeûne » signifie : <b>arrêt total du trading pendant 4 semaines minimum</b>. Pas démo, "
    "pas backtest, pas analyse, pas Twitter trading, pas YouTube SMC. Coupure totale. Si tu te dis « impossible », "
    "c'est exactement la preuve qu'il faut le faire. Une chose dont tu ne peux pas t'abstenir 4 semaines te "
    "domine.",
    "C'est aussi exactement ce que ta phase 1 du plan 90 jours te demande (PDF principal). Ce livre te donne "
    "la justification neurochimique de cette phase. Si tu comprends que c'est de la <b>chimie</b>, pas de "
    "la discipline morale, tu vas accepter de le faire."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu te dis « je vais réduire à 2 trades par semaine ». Ça ne marchera pas. La réduction "
    "n'autorise pas le baseline à remonter — chaque trade re-stimule le système.",
    "<b>Cible :</b> tu te dis « 4 semaines zéro trade. Y compris démo. Y compris regarder un chart. Y compris "
    "un thread X de SMC ». Tu désinstalles les apps. Tu donnes ton mot de passe TradingView à quelqu'un de "
    "confiance pour 4 semaines. Tu coupes la stimulation à la racine."
]))
story.append(P("Protocole 4 semaines", h_subsection))
story.append(styled_table([
    [C("Phase", cell_gold), C("Jours", cell_gold), C("Ce qui se passe", cell_gold), C("Ce que tu fais", cell_gold)],
    [C("Sevrage aigu", cell_bold), C("1-7"),
     C("Manque intense, irritabilité, ennui"),
     C("Pansage, marche, sport, sommeil, méditation. Pas de chart.")],
    [C("Sevrage moyen", cell_bold), C("8-14"),
     C("Anxiété diffuse, désir de check, vide"),
     C("Tu tiens. Ce n'est pas grave. Tu nommes le manque.")],
    [C("Stabilisation", cell_bold), C("15-21"),
     C("Désir baisse, énergie revient"),
     C("Tu poses des bases : lectures, projets ATHÉNA, relations.")],
    [C("Restauration", cell_bold), C("22-28"),
     C("Baseline qui remonte. Plaisirs simples reviennent."),
     C("Tu valides : test sur plaisirs ordinaires (repas, marche).")],
], [2.2*cm, 1.2*cm, 5.8*cm, 6.8*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Engagement écrit signé.</b> Sur ton journal : « Du [date] au [date+28], je m'abstiens totalement de "
    "tout trading et de tout contenu trading. Je signe pour Marien-du-futur. — [signature] » Affiche au mur.",
    "<b>Désinstallation physique.</b> Apps de trading désinstallées du téléphone. TradingView mot de passe "
    "changé et donné à quelqu'un de confiance. Discord trading désactivés. Tu rends impossible la rechute "
    "impulsive."
]))
story.extend(alerte(
    "Si tu réduis au lieu d'arrêter complètement, le baseline ne remonte PAS. C'est un fait neurochimique, "
    "pas une opinion. 4 semaines zéro, pas 4 semaines réduit. Sans cela, tu fais semblant de te soigner."
))
story.extend(phrase("Le sevrage n'est pas un test mental. C'est un protocole biologique. Je suis le protocole."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(2, 4, "L'inconfort volontaire",
    "Pousser la balance du côté de la douleur", ACCENT))
story.extend(idee(
    "Logique de bascule inversée : si chaque plaisir produit une douleur compensatoire, alors chaque douleur "
    "volontairement endurée produit un plaisir compensatoire. C'est le principe de l'inconfort volontaire. "
    "Cold exposure, jeûne, sport intense, restriction délibérée : tu pousses la balance vers la douleur — "
    "le cerveau te récompense en plaisir naturel <i>après</i>."
))
story.extend(mecan(
    "Mécanisme : la douleur volontaire et brève active la libération naturelle de dopamine et d'endorphines "
    "en compensation. Mais cette dopamine-là est <b>endogène</b>, elle ne crée pas de tolérance — au contraire, "
    "elle re-sensibilise le système. Bain froid 2 min produit un afflux dopaminergique soutenu sur 4-6 heures. "
    "Sport intense produit un effet équivalent. Jeûne 16h améliore la sensibilité dopaminergique. "
    "Tu hacks le système dans le bon sens."
))
story.extend(lien([
    "Tu es <b>déjà</b> très bien équipé pour ça. Cavalier saut d'obstacles compétitif → inconfort physique régulier. "
    "Box → décharge intense. Ta rééducation post-TBI t'a entraîné à tolérer l'inconfort prolongé. "
    "Tu as cette compétence. Tu ne l'utilises pas systématiquement.",
    "Pour ton sevrage trading, l'inconfort volontaire est essentiel. Sans lui, tu vas chercher le pic ailleurs "
    "(alcool, food, écran, sexe). Avec lui, tu fournis à ton cerveau la dose de dopamine endogène nécessaire "
    "pour traverser le sevrage."
]))
story.extend(exemple([
    "<b>Saboteur :</b> sevrage trading semaine 2. Vide intense, irritabilité. Tu compenses avec Netflix, sucre, "
    "alcool le soir. Tu satures un autre circuit dopaminergique. Tu ne soignes rien.",
    "<b>Cible :</b> sevrage trading semaine 2. Vide intense. Tu actives le protocole inconfort : 5 min douche "
    "froide le matin, séance box 1h, lecture longue le soir. Le cerveau reçoit sa dopamine endogène. Le creux "
    "passe. Tu rebondis."
]))
story.append(P("Menu d'inconfort volontaire — pioche selon tes goûts", h_subsection))
story.append(styled_table([
    [C("Protocole", cell_gold), C("Durée", cell_gold), C("Effet dopaminergique", cell_gold)],
    [C("Cold shower / bain froid", cell_bold), C("2-5 min"), C("Dopamine soutenue 4-6h. Le plus puissant.")],
    [C("Sport haute intensité", cell_bold), C("30-60 min"), C("Endorphines + dopamine. Effet 2-4h.")],
    [C("Jeûne intermittent 16:8", cell_bold), C("Quotidien"), C("Sensibilité dopaminergique générale.")],
    [C("Marche longue sans téléphone", cell_bold), C("60+ min"), C("Calme + tolérance ennui.")],
    [C("Lecture papier 1h", cell_bold), C("Quotidien"), C("Re-sensibilise aux plaisirs lents.")],
    [C("Méditation Dispenza guidée", cell_bold), C("20-60 min"), C("Réorganise le système de récompense.")],
], [5*cm, 2*cm, 9*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Protocole 14 jours.</b> Engage-toi sur 1 douche froide quotidienne (2-5 min) + 1 séance sport intense "
    "tous les 2 jours. Note ton état émotionnel le soir 1-10. Tu vas voir : le baseline remonte rapidement.",
    "<b>Journal de l'inconfort.</b> Chaque soir : « quel inconfort volontaire j'ai fait aujourd'hui ? » "
    "Si la réponse est « aucun », tu en planifies un pour demain."
]))
story.extend(phrase("Si je veux que mon plaisir naturel revienne, je dois enseigner à mon cerveau à passer par la douleur volontaire."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(2, 5, "Le renforcement intermittent",
    "Pourquoi le décalage de SL est plus addictif que tu ne crois", ACCENT))
story.extend(idee(
    "En psychologie expérimentale, le mode de conditionnement le plus puissant connu n'est pas la récompense "
    "régulière. C'est la récompense <b>imprévisible</b> et <b>intermittente</b>. C'est ce qui rend les machines "
    "à sous addictives. C'est ce qui rend le décalage de SL pratiquement impossible à arrêter par la volonté seule."
))
story.extend(mecan(
    "Skinner a démontré dans les années 50 qu'un pigeon récompensé une fois sur dix appuiera sur le levier "
    "<b>plus intensément et plus longtemps</b> qu'un pigeon récompensé à chaque fois. Le renforcement intermittent "
    "produit un comportement d'<b>extinction lente</b>. Appliqué à toi : chaque décalage de SL qui « marche » "
    "renforce massivement le comportement, même s'il ne marche qu'une fois sur dix. Tu deviens neuro-conditionné."
))
story.extend(lien([
    "Ton expérience récente confirme. Combien de fois as-tu décalé un SL et le marché est revenu, te sauvant "
    "d'une perte ? Probablement 1 fois sur 5, 1 fois sur 10. Cette expérience-là, qui aurait dû être un signal "
    "d'arrêt (« je m'en suis sorti par chance »), te conditionne au contraire à recommencer. <b>C'est la fois "
    "où ça marche qui t'enferme, pas les fois où ça crame.</b>",
    "C'est pour ça qu'aucun raisonnement ne marche contre le décalage. Tu sais rationnellement que c'est "
    "destructeur. Mais ton conditionnement neuronal est plus fort que ta connaissance. Pour le casser, il "
    "faut une <b>règle mécanique externe</b>, pas une décision interne."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu décales un SL XAUUSD. Marché revient. Tu sors à +0. Tu te dis « j'ai bien fait, "
    "j'aurais perdu sinon ». Tu viens de te conditionner pour la prochaine fois. 8 fois sur 10, la prochaine "
    "fois te détruira le compte.",
    "<b>Cible :</b> tu sens l'envie de décaler. Tu fermes la plateforme. Le SL fait son boulot. Tu prends "
    "la perte. Tu notes dans ton journal : « j'ai pris la perte planifiée. Je n'ai pas alimenté mon "
    "conditionnement. » Au bout de 50 fois, le conditionnement s'éteint."
]))
story.extend(ascii_schema("""
   COMPORTEMENT  +  RÉCOMPENSE RÉGULIÈRE        =  Extinction rapide
                                                  Tu arrêtes vite
                                                  si la récompense
                                                  disparaît.

   COMPORTEMENT  +  RÉCOMPENSE INTERMITTENTE    =  Extinction TRÈS LENTE
                    (1 fois sur 5-10)             Tu continues très
                                                  longtemps même si
                                                  la récompense est
                                                  rare. C'est le PIRE
                                                  des conditionnements.

   Décalage SL = jackpot 1 fois sur 10
              = conditionnement le plus puissant connu
""", accent=ACCENT))
story.extend(exo([
    "<b>Règle externe absolue.</b> Tu ne te fais pas confiance pour ne pas décaler. Tu mets une règle "
    "mécanique : SL placé avec l'ordre + plateforme fermée dès l'ordre placé. La plateforme fermée = "
    "impossible de décaler. Mécanique, pas mentale.",
    "<b>Log d'extinction.</b> Compte les sessions consécutives sans décalage. À chaque session sans décalage : "
    "+1. À la première rechute : retour à zéro. Vise 50 consécutives. C'est ton compteur d'extinction."
]))
story.extend(phrase("Mon conditionnement est plus fort que ma volonté. Donc je rends le geste impossible, pas optionnel."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(2, 6, "L'honnêteté radicale",
    "La honte cachée nourrit l'addiction. La honte dite la désactive.", ACCENT))
story.extend(idee(
    "Toute addiction se nourrit du <b>secret</b>. Tant que tu caches ton comportement (à toi-même, à ton "
    "entourage, à un thérapeute), tu maintiens un système de honte qui te pousse à reprendre pour fuir "
    "la honte. Quand tu dis ouvertement ce qui se passe, ce système se désactive."
))
story.extend(mecan(
    "Physiologiquement : la honte cachée produit un stress chronique de bas niveau qui maintient le système "
    "dopaminergique en mode recherche de fuite. La verbalisation à un tiers de confiance interrompt ce stress. "
    "Le cortisol baisse. Le besoin de stimulation diminue. Effet biologique mesurable, pas symbolique."
))
story.extend(lien([
    "Toi tu portes probablement plusieurs hontes silencieuses : nombre de comptes crammés que tu n'as pas "
    "dits à tes proches, sommes dépensées en frais d'inscription prop firms, sentiment d'avoir « gâché » du "
    "temps. Ces hontes alimentent ton besoin de pic — tu veux le gros gain qui annulera la honte. Mais le gain "
    "ne l'annule jamais, il en crée la conditions pour la suivante.",
    "Ta sortie : dire. Pas tout à tout le monde. Mais dire à au moins UNE personne de confiance ce que "
    "tu fais réellement, depuis combien de temps, à quelle hauteur. Cette personne peut être un thérapeute, "
    "un coach, un ami proche. L'acte de dire à voix haute coupe la racine."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu crames un compte. Tu le caches à tes proches. Tu te dis « la prochaine fois je vais "
    "me refaire, alors je leur dirai ». Tu portes la honte tout seul. La honte devient combustible pour le "
    "prochain trade impulsif.",
    "<b>Cible :</b> tu crames un compte. Le soir même tu appelles ton meilleur ami : « j'ai cramé un compte "
    "ce matin. C'est le sixième. Je veux que tu le saches. » Pas pour qu'il t'aide à régler — pour casser "
    "le secret. La honte se désactive en partie. Le besoin de revanche aussi."
]))
story.extend(exo([
    "<b>Liste des hontes cachées.</b> Sur ton journal, en page séparée, liste tout ce qui te concerne en "
    "trading et que tu n'as dit à personne (ou minimisé). Sois honnête. Cette liste n'est pas pour être partagée — "
    "elle est pour TOI.",
    "<b>L'acte de dire.</b> Choisis UNE personne de confiance. Dis-lui clairement, en 5 minutes, ce que tu "
    "vis avec le trading. Pas pour conseil, pas pour aide. Pour que ce ne soit plus seulement dans ta tête.",
    "<b>Thérapeute spécialisé.</b> Envisage un thérapeute spécialisé en addictions comportementales OU en "
    "trauma (idéal vu ton TBI). 1 séance par 2-3 semaines. Coût = un compte prop firm raté. Investissement, "
    "pas dépense."
]))
story.extend(phrase("Ce que je tais grandit. Ce que je dis perd son pouvoir. L'honnêteté est ma médecine."))
story.append(PageBreak())


# --- LIVRE 2 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 2", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Plaisir et douleur partagent le même circuit. Chaque pic produit un creux.",
    "La tolérance fait baisser ton baseline. Tu as besoin de plus pour ressentir pareil.",
    "L'anhédonie : « le calme me semble vide » est un diagnostic neurochimique, pas un trait.",
    "Le jeûne dopaminergique de 4 semaines remonte le baseline. Sevrage zéro, pas réduit.",
    "L'inconfort volontaire (cold, sport, jeûne) produit de la dopamine endogène — sans tolérance.",
    "Le renforcement intermittent (décalage SL qui marche parfois) est le pire conditionnement.",
    "La règle externe mécanique bat toujours la volonté interne contre l'addiction.",
    "La honte cachée nourrit l'addiction. La honte dite la désactive.",
    "Ton TBI 2022 a probablement modifié ta sensibilité dopaminergique baseline.",
    "Le sevrage est biologique. Pas moral. Tu suis le protocole, pas ta motivation.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs que ce livre t'aide à arrêter", h_subsection))
for i, err in enumerate([
    "Croire que c'est mental — c'est neurochimique.",
    "Réduire au lieu de stopper (le baseline ne remonte pas).",
    "Compenser le sevrage trading par alcool / sucre / écran.",
    "Cacher tes crashs à tes proches.",
    "Penser qu'un grand gain va effacer la dette dopaminergique.",
    "Confondre le rebond après pic avec « le marché qui te punit ».",
    "Chercher le pic sans payer la douleur volontaire à côté.",
    "Croire que ta volonté battra le renforcement intermittent.",
    "Refuser un thérapeute parce que « je vais m'en sortir seul ».",
    "Trader le lendemain d'une grosse journée.",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je sevré totalement 4 semaines avant toute reprise.",
    "Je fais une douche froide quotidienne minimum 2 min.",
    "Je fais 3 séances de sport intense par semaine, non négociable.",
    "Je dis à au moins une personne de confiance ce que je vis.",
    "Je consulte un thérapeute spécialisé trauma/addiction.",
    "Je pause obligatoire le lendemain d'une journée à +X au-dessus de ma moyenne.",
    "Je rends impossible le décalage de SL (plateforme fermée).",
    "Je ne compense pas le sevrage trading par d'autres pics.",
    "Je restaure quotidiennement des plaisirs simples et lents.",
    "Le baseline est ma priorité. Tout le reste passe après.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║       UN MONDE SOUS DOPAMINE  —  FICHE D'ANCRAGE         ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Plaisir et douleur sur la même bascule.                 ║
   ║    Pic = creux compensatoire mécanique.                    ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Anhédonie. Tolérance. Conditionnement intermittent.     ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE CHEZ MOI                                  ║
   ║    - "Le calme me semble vide"                             ║
   ║    - Besoin de plus pour ressentir pareil                  ║
   ║    - Compensation post-pic (alcool, sucre, écran)          ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Sevrage 4 semaines zéro trade                        ║
   ║    2. Cold shower quotidien + sport 3x/sem                 ║
   ║    3. Plateforme fermée = impossible de décaler            ║
   ║    4. Dire à un proche / thérapeute                        ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je suis chimique. Je suis le protocole, pas mon envie."║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Liste de mes 5 plaisirs perdus depuis 2022.             ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Pause obligatoire le lendemain de chaque pic.           ║
   ║    Compteur d'extinction : sessions sans décalage SL.      ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 2 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 3 — LE CORPS N'OUBLIE RIEN (Bessel van der Kolk)
# ============================================================
_current_book_color[0] = BOOK_COLORS[2]
ACCENT = BOOK_COLORS[2]

story.extend(book_separator_page(
    3, "Le corps n'oublie rien", "Bessel van der Kolk", "The Body Keeps the Score", 2014, ACCENT,
    quote='« Le trauma ne se loge pas dans la mémoire.<br/>Il se loge dans le corps. »',
    subtitle="Cerveau, esprit et corps dans la guérison du traumatisme"
))

story.extend(book_intro_header(3, "Le corps n'oublie rien", "Bessel van der Kolk — 2014", ACCENT))
story.append(P("A.  Pourquoi ce livre est crucial pour toi", h_section))
story.append(P(
    "Van der Kolk est psychiatre, chercheur à Harvard, pionnier de la recherche sur le trauma depuis les années 1970. "
    "Ce livre est la référence mondiale sur la façon dont le trauma s'inscrit dans le corps et le système nerveux. "
    "Pour quelqu'un qui a vécu ce que tu as vécu en 2022 — coma, opérations multiples, traumatisme crânien, "
    "reconstruction physique sur des mois — ce livre n'est pas optionnel. C'est ta carte d'identité neurologique."
))
story.append(P(
    "Ton TBI est un trauma au sens technique du terme : un événement où ton organisme a été confronté à une menace "
    "vitale qu'il n'a pas pu fuir ni combattre. Le coma, les opérations sous anesthésie, le réveil dans un corps "
    "qui ne répondait plus correctement — tout ça laisse des empreintes neurologiques que ton mental ne perçoit pas, "
    "mais que ton corps actionne quotidiennement. Quand tu cherches l'intensité, quand tu te crispés à +1500 PnL, "
    "quand tu ne supportes pas le calme : ce n'est pas Marien qui choisit. C'est ton système nerveux qui répond "
    "à des signaux que tu n'identifies pas."
))
story.append(P(
    "Hougaard et Lembke t'ont parlé du <b>quoi</b> et du <b>comment chimique</b> de tes patterns. Van der Kolk te "
    "parle du <b>où</b> : où ces patterns sont stockés dans ton corps, pourquoi ils ne se débloquent pas par la "
    "parole ou la volonté, et par quels chemins corporels ils peuvent se libérer."
))
story.append(P(
    "Lis-le lentement. Ce n'est pas un livre de techniques rapides. C'est un livre de compréhension profonde. "
    "Il va te faire reconnaître des choses que tu vis tous les jours sans les nommer."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Le trauma n\'est pas un souvenir. C\'est une empreinte corporelle vivante qui pilote toujours des comportements actuels.</b>', pull_quote))
story.append(P(
    "Quand un événement traumatique se produit, le cerveau ne l'encode pas comme un souvenir narratif normal "
    "(quelque chose qui s'est passé et qui est terminé). Il l'encode comme un <b>signal somatique permanent</b> "
    "logé dans le système nerveux autonome. Conséquence : le corps continue de réagir, des années plus tard, "
    "comme si la menace était présente. Tu peux être totalement réparé physiquement et porter encore "
    "tous les réflexes du danger originel."
))
story.append(P("Les mécanismes neurologiques exposés", h_subsection))
story.append(P(
    "<b>1. La théorie polyvagale (Stephen Porges) :</b> le nerf vague a trois états — calme social (vagal ventral), "
    "mobilisation (sympathique : fight/flight), figement (vagal dorsal : freeze). Le trauma fige souvent dans "
    "l'un des deux derniers. <b>2. La désintégration mémorielle :</b> le trauma fragmente le souvenir en bouts "
    "sensoriels (odeur, son, sensation) sans narration, ce qui explique pourquoi un déclencheur peut "
    "ré-actualiser tout l'état du corps. <b>3. L'imprint corporel :</b> postures, micro-tensions, schémas "
    "respiratoires, hypervigilance — tout reste dans la chair. <b>4. La dérégulation interoceptive :</b> "
    "la perte de la capacité à lire correctement les signaux internes du corps. <b>5. L'altération de "
    "l'auto-représentation :</b> le sentiment de qui tu es se désorganise."
))
story.append(P("Les voies de réparation proposées", h_subsection))
story.append(P(
    "Van der Kolk insiste sur le fait que la <b>parole seule</b> ne suffit pas — beaucoup de traumatisés ont "
    "passé des années en thérapie par la parole sans soulagement. Il faut compléter par des approches corporelles. "
    "Les principales : <b>EMDR</b> (mouvements oculaires), <b>yoga thérapeutique</b> sensible au trauma, "
    "<b>neurofeedback</b>, <b>théâtre</b>, <b>chant</b>, <b>thérapies somatiques</b> (Somatic Experiencing — "
    "c'est le sujet du livre suivant, Levine). Le fil rouge : <b>passer par le corps</b> pour libérer ce qui "
    "est stocké dans le corps."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Très américain, parfois bavard. Certains chapitres cliniques peuvent te paraître hors sujet (cas d'inceste, "
    "guerre du Vietnam). Le concept central — trauma stocké dans le corps — est solide scientifiquement, mais "
    "certaines techniques recommandées (EMDR, neurofeedback) sont efficaces sans qu'on sache totalement pourquoi. "
    "Tu peux lire en survolant les études de cas qui ne te concernent pas directement et te concentrer sur la "
    "physiologie du trauma."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Le corps n'oublie rien",
    [
        {"label": "THÈSE", "leaves": ["trauma = empreinte", "vit dans le corps"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["polyvagal (3 états)", "hypervigilance", "interoception altérée"], "color": ACCENT},
        {"label": "RÉPARATION", "leaves": ["SE / EMDR", "yoga trauma", "neurofeedback", "co-régulation animale"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Le trauma stocké et les voies de réparation corporelle.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(3, 1, "Le trauma comme empreinte vivante",
    "Pourquoi tu portes encore 2022 dans ton corps", ACCENT))
story.extend(idee(
    "Le trauma n'est pas un événement passé. C'est un état présent du système nerveux qui n'a jamais "
    "« digéré » l'événement original. Le corps reproduit en permanence les réflexes de survie de la menace "
    "originelle, même quand la menace est terminée depuis longtemps."
))
story.extend(mecan(
    "Quand une menace vitale survient, le système nerveux active une cascade : adrénaline, cortisol, mobilisation "
    "musculaire, hypervigilance sensorielle. Normalement, après la résolution de la menace, le corps "
    "<b>décharge</b> cette énergie de survie (tremblements, pleurs, mouvements involontaires). Quand cette "
    "décharge ne peut pas avoir lieu (anesthésie, immobilisation, coma, opérations), l'énergie reste figée. "
    "Le système nerveux reste « branché » sur le mode urgence, des années plus tard."
))
story.extend(lien([
    "Toi en 2022 : coma + opérations sous anesthésie + immobilisation prolongée + réveil dans un corps qui ne "
    "répond plus comme avant. Pendant tout cet épisode, ton système nerveux a vécu une menace vitale ET n'a "
    "JAMAIS pu décharger l'énergie de survie correspondante. Anesthésie = pas de tremblement, pas de pleurs, "
    "pas de mouvement involontaire. L'énergie est restée figée.",
    "Trois ans plus tard, ton corps est réparé. Mais ton système nerveux porte encore l'empreinte. "
    "Ce que tu vis aujourd'hui — intolérance au calme, recherche d'intensité, crispation devant l'écran, "
    "sommeil parfois agité, hypervigilance discrète — ce ne sont pas des traits de caractère. Ce sont des "
    "<b>conséquences neurologiques directes</b> de 2022 que ton mental ne reconnaît pas mais que ton corps "
    "actionne tous les jours.",
    "Cette compréhension change tout. Tu n'as pas un problème de motivation. Tu n'es pas un mauvais trader. "
    "Tu as un <b>système nerveux dérégulé par un trauma non décharge</b>, qui pilote silencieusement tes choix. "
    "La voie de réparation passe par le corps, pas par la volonté."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu trades XAUUSD un matin calme. Le marché ne bouge pas. Tu ressens une montée d'irritation, "
    "de l'agitation, l'envie de cliquer quelque chose. Tu cliques un setup B-grade pour « activer quelque chose ». "
    "Tu perds. Tu te dis « j'ai été impulsif ». Faux diagnostic.",
    "<b>Cible :</b> tu trades. Même calme. Tu ressens la même agitation. Tu nommes : « ce n'est pas Marien qui veut "
    "trader. C'est mon SN qui ne tolère pas le calme parce qu'il est figé en hypervigilance depuis 2022. » "
    "Tu fermes la plateforme. Tu fais 10 min de respiration cohérente. L'agitation passe. Tu reprends quand "
    "elle est passée — ou tu ne reprends pas du tout aujourd'hui."
]))
story.append(P("Schéma — Le trauma figé vs le trauma déchargé", h_subsection))
story.extend(ascii_schema("""
   TRAUMA FIGÉ (ton cas)               TRAUMA DÉCHARGÉ
   ────────────────────                ───────────────
   Menace originelle                   Menace originelle
        │                                    │
        ▼                                    ▼
   Mobilisation SN totale              Mobilisation SN totale
   (cortisol, adrénaline, tension)     (cortisol, adrénaline, tension)
        │                                    │
        ▼                                    ▼
   ╔═══════════════════╗                Résolution de la menace
   ║ ANESTHÉSIE / COMA ║                     │
   ║ Pas de décharge   ║                     ▼
   ╚═══════════════════╝                ★ DÉCHARGE ★
        │                              tremblements / pleurs /
        ▼                              mouvements involontaires
   Énergie FIGÉE dans le SN                  │
        │                                    ▼
        ▼                              SN revient au baseline
   3 ans plus tard,                          │
   réflexes toujours actifs.                 ▼
   Hypervigilance silencieuse.        Trauma intégré,
   Intolérance au calme.              pas figé.

   → C'est pourquoi tu portes encore 2022. La décharge n'a pas eu lieu.
""", accent=ACCENT))
story.extend(exo([
    "<b>Reconnaissance.</b> Pendant 7 jours, à chaque moment où tu ressens agitation/irritation/envie de pic, "
    "écris dans ton journal : « SN figé qui parle, pas Marien qui parle ». Cette nomination casse l'identification. "
    "Tu cesses de croire que c'est toi qui réclames — c'est ton SN qui décharge un signal vieux.",
    "<b>Premier contact avec ton corps.</b> Chaque soir, 5 min de scan corporel. Tu fermes les yeux. "
    "Tu balayes mentalement de la tête aux pieds. Où ton corps est tendu ? Où il est en alerte ? Où il est "
    "détendu ? Tu ne corriges rien. Tu OBSERVES. C'est la première étape de toute réparation : redevenir "
    "habitant de ton corps."
]))
story.extend(phrase("Mon TBI 2022 n'est pas dans mon passé. Il est dans mon corps présent. Je travaille là où il est."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(3, 2, "La théorie polyvagale",
    "Les trois états de ton système nerveux", ACCENT))
story.extend(idee(
    "Stephen Porges a démontré que le système nerveux autonome n'a pas deux états (calme / stress) mais "
    "<b>trois</b> : engagement social (vagal ventral), mobilisation (sympathique), figement (vagal dorsal). "
    "Le trauma fige souvent dans les deux derniers — et empêche le retour au premier."
))
story.append(P("Les trois états en détail", h_subsection))
story.append(styled_table([
    [C("État", cell_gold), C("Activation", cell_gold), C("Sensation", cell_gold), C("Chez Marien", cell_gold)],
    [C("VAGAL VENTRAL", cell_bold), C("Calme social, sécurité"),
     C("Présence ouverte, voix calme, respiration ample, lien possible"),
     C("Rare. Atteint en pansage, méditation profonde, certaines présences.")],
    [C("SYMPATHIQUE", cell_bold), C("Mobilisation fight/flight"),
     C("Cœur rapide, souffle court, agitation, tension musculaire, vigilance"),
     C("État baseline actuel. Devant l'écran, en société dense, après caféine.")],
    [C("VAGAL DORSAL", cell_bold), C("Figement, effondrement"),
     C("Engourdissement, dissociation, fatigue extrême, vide, déconnexion"),
     C("Après un crash de compte, certains réveils, journées « vides ».")],
], [3*cm, 2.8*cm, 5.4*cm, 4.8*cm]))
story.append(Spacer(1, 8))
story.extend(mecan(
    "Le système est <b>hiérarchique</b>. Si le vagal ventral (calme social) n'arrive pas à gérer la situation, "
    "le sympathique prend la suite. Si le sympathique ne suffit pas (menace écrasante, impossibilité de fuir), "
    "le vagal dorsal prend le relais en figement. C'est une cascade descendante. Pour remonter, il faut faire "
    "le chemin inverse : du figement → mobilisation → calme. On ne saute pas d'étape."
))
story.extend(lien([
    "Tu fonctionnes la plupart du temps en sympathique. Devant l'écran, tu es en mobilisation. Quand tu trades, "
    "tu accentues encore cette mobilisation. À +1500 PnL, tu es en hyper-sympathique extrême — fight/flight maximal. "
    "Quand le marché reverse et que tu perds, tu peux basculer dans le vagal dorsal (vide, dissociation, "
    "« je ne sens plus rien »).",
    "Ton trading active donc systématiquement les deux états traumatiques. Tu n'y trouves jamais le vagal ventral. "
    "C'est pour ça que le trading t'épuise corporellement : tu fais des allers-retours violents entre les deux "
    "états les plus coûteux pour ton organisme.",
    "Ta cible : retour <b>fréquent</b> au vagal ventral pendant la journée (méditation, pansage, présence à ta "
    "filly, respiration profonde, contact social safe avec proches). Plus tu y reviens, plus ton SN apprend "
    "que cet état est accessible. À force, il devient ton baseline."
]))
story.append(P("Comment activer chaque état (pour info — tu veux le vagal ventral)", h_subsection))
story.append(styled_table([
    [C("Pour activer...", cell_gold), C("Technique", cell_gold)],
    [C("VAGAL VENTRAL (calme)", cell_bold),
     C("Respiration 4-6 (4s in, 6s out), chant/fredonnement, eau froide visage, regard doux fixé loin, "
       "contact lent avec animal ou personne de confiance, voix grave, méditation guidée.")],
    [C("SYMPATHIQUE (mobilisation utile)", cell_bold),
     C("Sport intense, douche froide rapide, café, musique stimulante. Utile pour SORTIR du figement, "
       "puis on enchaîne avec calme vagal ventral.")],
    [C("VAGAL DORSAL (à ÉVITER)", cell_bold),
     C("S'isoler, scroller passivement, alcool, sucre excessif, sommeil de fuite. Si tu y tombes : sortir par "
       "mouvement physique court, puis activation calme ensuite.")],
], [5.5*cm, 10.5*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Cartographie quotidienne 7 jours.</b> À 8h, 12h, 16h, 20h : note tu es dans quel état (V / S / D). "
    "Sur 7 jours tu vas voir ton baseline réel — probablement S 70% du temps.",
    "<b>Protocole de retour au vagal ventral.</b> 5 fois par jour : 2 min de respiration 4-6. Pas plus, "
    "pas moins. Tu installes un point d'ancrage. À force, ton SN sait où retrouver ce calme.",
    "<b>Chant ou fredonnement.</b> 1 min/jour. Le chant active directement le nerf vague ventral via la "
    "stimulation laryngée. C'est physiologique, pas symbolique."
]))
story.extend(phrase("Trois états. Je sais lequel je suis. Je sais comment revenir au calme. C'est physiologique."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(3, 3, "L'hypervigilance silencieuse",
    "Tu es en alerte permanente sans le savoir", ACCENT))
story.extend(idee(
    "L'hypervigilance est l'état où ton SN scanne en permanence l'environnement pour détecter une menace. "
    "C'est épuisant et c'est souvent invisible pour le concerné — il croit que c'est sa façon normale d'être. "
    "Le trauma installe cette hypervigilance comme état permanent."
))
story.extend(mecan(
    "L'amygdale (centre de la peur) reste sur-activée après un trauma. Elle interprète des stimuli ordinaires "
    "comme potentiellement menaçants. Conséquences : sursauts faciles, qualité de sommeil dégradée, fatigue "
    "chronique, irritabilité au bruit, hyper-attention au visage des autres, agitation diffuse, difficulté à "
    "rester immobile longtemps. Le SN se comporte comme un soldat en zone de combat — même dans ton salon."
))
story.extend(lien([
    "Signaux probables chez toi : tu te réveilles parfois sans raison, fatigué. Tu sursautes facilement à un bruit "
    "soudain. Tu as du mal à rester immobile sans rien faire. Tu lis les visages des autres rapidement. Tu sens "
    "tes épaules ou ta mâchoire serrées sans raison. Ton ventre est souvent tendu.",
    "En trading, l'hypervigilance se traduit par : tu ne peux pas <b>vraiment</b> fermer la plateforme et oublier "
    "le trade en cours. Tu y penses. Tu ressens le besoin de vérifier. Cette vigilance perpétuelle te coûte "
    "énormément d'énergie et nourrit le besoin de décharge intense — ton SN ne tient pas longtemps cette "
    "vigilance, il décharge par impulsivité."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu places un trade XAUUSD avec SL et TP. Tu te dis « OK je peux faire autre chose ». "
    "Tu essayes de lire. Toutes les 90 secondes tu vérifies. Tu n'arrives pas à vraiment décrocher. "
    "L'hypervigilance contre-attaque.",
    "<b>Cible :</b> tu places le trade. Tu sais que ton SN va vouloir vérifier. Tu décides à l'avance : "
    "téléphone dans une autre pièce, plateforme fermée. Tu vas faire pansage 30 min, mouvement physique "
    "qui occupe le SN. Quand tu reviens, c'est terminé. Tu n'as pas alimenté l'hypervigilance par micro-checks."
]))
story.extend(ascii_schema("""
   HYPERVIGILANCE — la fatigue silencieuse
   ───────────────────────────────────────

   Niveau de vigilance d'un cerveau non-traumatisé :
   ▁▁▂▁▂▁▁▂▁▁▁▂▁▁▂▁▁▁▁▂  baseline bas, monte sur menace réelle

   Niveau de vigilance de ton cerveau aujourd'hui :
   ▇▇▆▇▆▇▇▆▆▇▇▆▇▆▇▇▆▇▆▇  baseline ÉLEVÉ, pas de retour au repos

   Conséquences accumulées :
   - Fatigue chronique masquée par l'adrénaline
   - Sommeil moins réparateur
   - Besoin d'intensité (le calme dérange le système qui scanne)
   - Décisions impulsives (le SN décharge la pression)
   - Crispations corporelles (mâchoire, épaules, ventre)
""", accent=ACCENT))
story.extend(exo([
    "<b>Le scan des tensions.</b> 3 fois par jour, 1 min : épaules, mâchoire, ventre, front. Sont-ils tendus ? "
    "Tu relâches consciemment. C'est un acte de signal pour ton SN : « la menace est partie ».",
    "<b>Routine de coucher anti-hypervigilance.</b> 30 min avant dormir : lumière baissée, aucun écran, "
    "respiration 4-6 pendant 10 min, lecture papier. Tu indiques à ton SN que la journée est terminée. "
    "Sans ce rituel, l'hypervigilance suit jusque dans le sommeil.",
    "<b>Plateforme physiquement fermée.</b> Pas réduite — fermée. Téléphone dans une autre pièce. Tu coupes "
    "l'objet qui maintient la vigilance."
]))
story.extend(phrase("Mon SN scanne en permanence. Je lui apprends, dose après dose, qu'il peut se reposer."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(3, 4, "L'interoception altérée",
    "Tu ne lis plus correctement les signaux de ton corps", ACCENT))
story.extend(idee(
    "L'interoception est la capacité à percevoir et interpréter les signaux internes du corps : faim, soif, "
    "fatigue, anxiété, joie, tension. Le trauma altère cette capacité. Tu confonds des signaux. Tu n'entends "
    "plus tes besoins. Tu agis à l'aveugle physiologiquement."
))
story.extend(mecan(
    "L'insula (zone cérébrale de l'interoception) est régulièrement perturbée chez les traumatisés. Tu peux "
    "confondre faim et anxiété, fatigue et ennui, tension corporelle et besoin de pic, signal de stop et signal "
    "de continuer. Ton système informatif interne est <b>déréglé</b>. Tu te fies à des sensations qui ne disent "
    "pas ce que tu crois qu'elles disent."
))
story.extend(lien([
    "Pour toi en trade, ça donne des cas précis. <b>1)</b> Tu ressens « ça doit marcher » dans ta poitrine. Tu "
    "crois que c'est de l'intuition de trader. C'est en fait de la mobilisation sympathique liée à l'attente — "
    "rien à voir avec la qualité du setup. <b>2)</b> Tu ressens un creux après une session calme. Tu crois que "
    "c'est de l'ennui qui appelle un trade. C'est en fait une fatigue mentale qui appelle du repos.",
    "Tu prends donc des décisions de trading basées sur des signaux corporels que tu interprètes mal. C'est une "
    "des sources majeures de ton sabotage. La solution est de <b>réapprendre à lire ton corps</b>. C'est lent, "
    "ça demande pratique régulière, mais c'est récupérable."
]))
story.extend(exemple([
    "<b>Saboteur :</b> 14h, session vide. Tu ressens une agitation. Tu interprètes « je dois trader, c'est mon "
    "intuition qui me dit qu'il va y avoir un mouvement ». Tu trades. Tu perds.",
    "<b>Cible :</b> 14h, agitation. Tu fais le check : « qu'est-ce que mon corps me dit vraiment ? » Tu fais 2 min "
    "de scan. Tu identifies : mâchoire serrée, ventre tendu, souffle court. C'est une mobilisation sympathique "
    "déconnectée de toute info de marché. Tu nommes : « agitation sympathique sans signal marché ». Tu n'ouvres "
    "pas. Tu fais 5 min de respiration."
]))
story.extend(exo([
    "<b>Journal interoceptif.</b> 3 fois par jour, 2 min : qu'est-ce que je ressens dans mon corps maintenant ? "
    "(faim, soif, tension, fatigue, calme, agitation, chaleur, froid). Écris-le. Tu réapprends à percevoir.",
    "<b>Test du décodage.</b> Avant chaque trade : qu'est-ce que je ressens corporellement ? Est-ce que c'est "
    "un signal de marché ou un signal interne déconnecté ? Si c'est un signal interne (agitation, désir de pic, "
    "FOMO), tu ne cliques pas.",
    "<b>Yoga ou body scan guidé.</b> 10-20 min, 3x/semaine. Le yoga thérapeutique sensible au trauma "
    "(« trauma-sensitive yoga ») est documenté comme la pratique qui restaure le plus efficacement "
    "l'interoception. Pour ton TBI, c'est presque un soin."
]))
story.extend(phrase("Mes sensations corporelles ne disent pas toujours ce que je crois. J'apprends à les lire."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(3, 5, "Les chemins de réparation corporelle",
    "Pourquoi parler ne suffit pas", ACCENT))
story.extend(idee(
    "Le trauma est stocké dans le corps. La parole accède au cortex (zone du langage). Mais le trauma est "
    "logé dans des zones plus anciennes du cerveau (système limbique, tronc cérébral) auxquelles la parole "
    "n'accède pas directement. Conclusion : pour libérer du trauma, il faut <b>passer par le corps</b>. "
    "Pas exclusivement, mais nécessairement."
))
story.extend(mecan(
    "Les approches corporelles efficaces partagent un principe : elles activent simultanément la sensation "
    "interoceptive (lecture du corps) et une régulation lente du SN. C'est ce double processus qui permet "
    "à l'énergie figée de se libérer en douceur. Sans la régulation, l'activation seule peut retraumatiser. "
    "Sans l'activation, la régulation seule ne libère rien."
))
story.append(P("Les approches documentées efficaces (pour toi à prioriser)", h_subsection))
story.append(styled_table([
    [C("Approche", cell_gold), C("Principe", cell_gold), C("Pertinence pour toi", cell_gold)],
    [C("Somatic Experiencing", cell_bold),
     C("Libération progressive de l'énergie figée via attention au corps."),
     C("Très haute. C'est le sujet du Livre 4 (Levine). Cherche un praticien.")],
    [C("EMDR", cell_bold),
     C("Mouvements oculaires bilatéraux qui aident à recontextualiser le trauma."),
     C("Haute. Une bonne option pour ton TBI. Demande à ton médecin une orientation.")],
    [C("Yoga thérapeutique trauma-sensitive", cell_bold),
     C("Yoga adapté qui priorise l'écoute du corps sur la performance."),
     C("Haute. Compatible avec ta vie équestre. Cherche un instructeur certifié TCTSY.")],
    [C("Neurofeedback", cell_bold),
     C("Entraînement direct des ondes cérébrales via mesure EEG."),
     C("Moyenne. Coûteux, moins accessible. À envisager si autres voies insuffisantes.")],
    [C("Équitation thérapeutique", cell_bold),
     C("La présence du cheval régule directement le SN humain (co-régulation interspécifique)."),
     C("TRÈS haute. Tu fais déjà du cheval — fais-le aussi POUR ça, en conscience.")],
    [C("Travail respiratoire", cell_bold),
     C("Respirations spécifiques qui rééquilibrent le système autonome."),
     C("Haute, gratuit, immédiat. À intégrer quotidiennement.")],
], [4*cm, 5.5*cm, 6.5*cm]))
story.append(Spacer(1, 8))
story.extend(lien([
    "Tu as un atout rare : <b>les chevaux</b>. La recherche montre que la présence rapprochée d'un cheval "
    "régule directement le SN humain — le cœur du cheval (à basse fréquence) entraîne celui de l'humain "
    "(phénomène de co-régulation interspécifique). Ta filly est une thérapeute non diplômée. Si tu fais "
    "ton pansage tranquille en conscience (pas en pensant à autre chose), tu fais une séance de régulation "
    "vagale.",
    "Tu fais aussi de la box. La box est un outil DOUBLE : décharge sympathique (poing) + retour au calme "
    "(récupération entre rounds). Si tu structures bien, c'est de la décharge somatique légitime.",
    "Le travail spécifique sur ton TBI 2022 demanderait idéalement un thérapeute somatique formé. C'est un "
    "investissement de 80-150€ la séance, 1 par 2-3 semaines. À l'échelle de tes pertes prop firm, c'est "
    "rien. Cherche un praticien Somatic Experiencing certifié dans ta région."
]))
story.extend(exo([
    "<b>Pansage conscient.</b> 1 fois par semaine minimum, 30 min : pansage à ta filly en présence totale. "
    "Pas de téléphone. Pas de pensée trading. Tu sens tes mains, son souffle, sa chaleur. C'est de la thérapie.",
    "<b>Recherche thérapeute somatique.</b> Cette semaine : 30 min de recherche en ligne. Annuaire Somatic "
    "Experiencing France. Note 3 praticiens. Contacte 1 pour un premier rendez-vous. C'est ton action concrète.",
    "<b>Respiration cohérence cardiaque.</b> 3 x 5 min/jour, respiration 5-5 (5s in, 5s out). Au matin, "
    "avant trading, avant coucher. Régulation autonome documentée."
]))
story.extend(phrase("Je ne soigne pas mon trauma par la pensée. Je le soigne par le corps, lent, régulier."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(3, 6, "L'altération de l'auto-représentation",
    "Comment ton TBI a modifié ton sens d'être Marien", ACCENT))
story.extend(idee(
    "Le trauma altère la <b>continuité de l'identité</b>. Avant l'événement, il y a un « moi ». Après, il y a "
    "un « moi nouveau » qui ne reconnaît plus complètement l'ancien. Le pont entre les deux est cassé. "
    "Tu peux porter le sentiment confus de ne plus être tout à fait toi-même."
))
story.extend(mecan(
    "Le réseau de connectivité par défaut du cerveau (DMN — qui produit le sentiment de continuité de soi) est "
    "souvent perturbé par le trauma. Conséquences : sentiment d'irréalité de soi (« je joue un rôle de moi-même »), "
    "perte de connexion aux désirs profonds, identification accrue à des rôles externes (« je suis trader », "
    "« je suis cavalier ») au lieu d'un soi unifié. Le moi devient une collection de rôles à performer plutôt "
    "qu'une présence continue."
))
story.extend(lien([
    "Tu portes peut-être ce sentiment. Ton lien identité-performance très chargé pointe dans cette direction : "
    "tu cherches dans la performance (trade, équitation, ATHÉNA) une confirmation de qui tu es. Comme si sans "
    "cette confirmation continue, le sens de soi s'effritait. Ce n'est pas du narcissisme. C'est probablement "
    "une compensation à une auto-représentation altérée par 2022.",
    "Le coma a interrompu la continuité phénoménologique de ta conscience. Tu t'es endormi en étant un certain "
    "Marien et tu t'es réveillé après des heures/jours d'absence — sans souvenir intermédiaire. C'est une "
    "rupture qui laisse une trace. Le « Marien post-2022 » est en partie en train de se reconstruire un sens "
    "de soi cohérent. Le trading est devenu involontairement un de ses terrains de test."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu fais +1000 PnL. Tu te sens « réel », « plein », « validé ». Tu fermes la plateforme. "
    "Une heure après, tu ne sais plus pourquoi tu existes. Tu retournes ouvrir la plateforme pour reproduire "
    "la sensation. Tu trades sans setup A+. Tu perds.",
    "<b>Cible :</b> tu reconnais que le pic de +1000 a temporairement comblé un vide d'auto-représentation. "
    "Tu sais que le vide va revenir. Tu ne le combats pas avec un autre trade. Tu vas vers ce qui te construit "
    "un sens de soi durable : ATHÉNA, ta filly, ton journal, présence avec un proche. Tu nourris le moi profond, "
    "pas le moi-performance."
]))
story.extend(exo([
    "<b>Le journal d'auto-cohérence.</b> Chaque soir, 3 phrases : « Aujourd'hui j'ai été Marien quand... », "
    "« Aujourd'hui je n'ai pas été Marien quand... », « Demain je serai Marien si... ». Tu reconstruis "
    "consciemment ta continuité.",
    "<b>Les ancres identitaires non-trading.</b> Liste 5 activités où tu te sens « toi » indépendamment d'un "
    "résultat. (Probablement : pansage, certaines lectures, certaines présences, dessin, etc.). Programme-les "
    "dans ta semaine. Tu nourris ton sens de soi en dehors de la performance.",
    "<b>Réminiscence longue.</b> Une fois par mois, 30 min : tu te rappelles 3 souvenirs précis d'avant 2022 "
    "où tu étais clairement toi-même. Tu écris dans ton journal. Tu reconstruis activement le pont entre "
    "le Marien d'avant et le Marien d'après."
]))
story.extend(phrase("Je ne suis pas mes trades. Je ne suis pas mes performances. Je suis Marien — avec ou sans résultats."))
story.append(PageBreak())


# --- LIVRE 3 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 3", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Le trauma n'est pas un souvenir. C'est une empreinte corporelle vivante.",
    "Ton TBI 2022 pilote encore tes choix actuels, par le SN, pas par le mental.",
    "Trois états du SN : vagal ventral (calme), sympathique (mobilisation), vagal dorsal (figement).",
    "Tu vis majoritairement en sympathique. Ton baseline est élevé.",
    "L'hypervigilance est silencieuse mais épuisante. Elle nourrit le besoin d'intensité.",
    "L'interoception altérée te fait mal lire tes signaux corporels.",
    "La parole seule ne suffit pas. Le trauma se libère par le corps.",
    "Les chevaux régulent ton SN par co-régulation interspécifique. Atout précieux.",
    "Somatic Experiencing, EMDR, yoga trauma-sensitive : voies documentées de réparation.",
    "Ton auto-représentation est probablement encore en reconstruction. Le trading n'est pas le bon terrain de test.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Croire que ton TBI est « guéri » parce que ton corps est réparé.",
    "Interpréter ton agitation comme intuition de trader.",
    "Chercher l'intensité parce que « le calme te semble vide ».",
    "Confondre tension corporelle et signal de marché.",
    "Vouloir guérir le trauma uniquement par la pensée / la lecture.",
    "Ignorer les chevaux comme ressource thérapeutique.",
    "Refuser un thérapeute somatique « parce que je vais m'en sortir seul ».",
    "Faire confiance à des sensations interoceptives non vérifiées.",
    "Forcer le calme au lieu de le pratiquer en doses progressives.",
    "Chercher ta valeur dans la performance pour combler un vide d'identité.",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je traite mon TBI 2022 comme un trauma actif, pas comme du passé.",
    "Je pratique 5x/jour 2 min de respiration 4-6 (retour vagal ventral).",
    "Je fais un pansage conscient avec ma filly 1x/semaine minimum.",
    "Je consulte un thérapeute somatique (SE ou EMDR) au moins 1x/2-3 semaines.",
    "Je fais un scan corporel le soir 5 min.",
    "Je nomme l'état SN dans lequel je suis avant chaque décision importante.",
    "Je tiens un journal interoceptif (qu'est-ce que mon corps dit vraiment ?).",
    "Je distingue signal de marché et signal de SN figé.",
    "Je nourris une identité non-performance chaque jour.",
    "Je ne soigne pas par la pensée seule. Je passe par le corps.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║       LE CORPS N'OUBLIE RIEN  —  FICHE D'ANCRAGE         ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Mon TBI 2022 vit dans mon corps présent.                ║
   ║    Je travaille là où il vit.                              ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Croire que c'est mental. Ignorer le SN.                 ║
   ║    Vouloir tout résoudre par la lecture.                   ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE                                           ║
   ║    - Mâchoire/épaules tendues sans raison                  ║
   ║    - Intolérance au calme = "le calme me semble vide"      ║
   ║    - Sursaut facile, sommeil interrompu                    ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Nommer l'état SN (V / S / D)                         ║
   ║    2. Activer ce qui ramène au vagal ventral               ║
   ║       (respi 4-6, pansage, chant, eau froide visage)       ║
   ║    3. Consulter thérapeute somatique régulier              ║
   ║    4. Yoga trauma-sensitive 2x/sem                         ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je soigne par le corps. C'est là que c'est stocké."   ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Cette semaine : trouver un praticien Somatic            ║
   ║    Experiencing dans ma région.                            ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Pas de trading en état sympathique élevé.               ║
   ║    Check SN avant chaque session.                          ║
   ║    Sinon : pansage 30 min, puis re-check.                  ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 3 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 4 — RÉVEILLER LE TIGRE (Peter Levine)
# ============================================================
_current_book_color[0] = BOOK_COLORS[3]
ACCENT = BOOK_COLORS[3]

story.extend(book_separator_page(
    4, "Réveiller le tigre", "Peter A. Levine", "Waking the Tiger — Healing Trauma", 1997, ACCENT,
    quote='« Les animaux sauvages se libèrent du trauma.<br/>Nous, humains, l\'enfermons dans nos corps. »',
    subtitle="Guérir le trauma — Le modèle Somatic Experiencing"
))

story.extend(book_intro_header(4, "Réveiller le tigre", "Peter A. Levine — 1997", ACCENT))
story.append(P("A.  Pourquoi ce livre est crucial pour toi", h_section))
story.append(P(
    "Peter Levine est le créateur de la méthode <b>Somatic Experiencing</b> (SE). Pendant 40 ans, il a "
    "observé une chose qui semble triviale mais qui est révolutionnaire : <b>les animaux sauvages ne "
    "développent presque jamais de trauma chronique</b>, alors qu'ils vivent des menaces mortelles fréquentes. "
    "Pourquoi ? Parce qu'après la menace, ils <b>déchargent l'énergie de survie</b> par un mécanisme "
    "automatique : tremblements, sursauts, respirations profondes, secouements. Les humains, eux, "
    "<b>inhibent</b> cette décharge — par éducation, par anesthésie médicale, par incapacité contextuelle. "
    "L'énergie reste figée. C'est ça, le trauma chronique."
))
story.append(P(
    "Ce livre est le compagnon direct de van der Kolk (Livre 3). Van der Kolk t'explique le diagnostic — "
    "que le trauma vit dans le corps. Levine t'explique le <b>traitement</b> — comment libérer ce qui est "
    "figé. Pour ton TBI 2022, où tu as vécu un événement vital menaçant suivi d'anesthésie multiple et "
    "d'immobilisation prolongée, c'est presque un cas d'école : ton corps a vécu une activation maximale "
    "sans aucune possibilité de décharge. L'énergie est restée figée."
))
story.append(P(
    "Le livre est court (200 pages), simple, direct, parsemé d'exercices concrets que tu peux faire seul ou "
    "avec un praticien. C'est probablement le livre le plus <b>opérationnel</b> de cette bibliothèque pour ce "
    "qui concerne ton corps. Lis-le après van der Kolk, et idéalement applique ses techniques en parallèle "
    "d'une thérapie SE en présentiel."
))
story.append(P(
    "Pour toi, ce livre est la clé qui dénoue ce que les autres livres décrivent. Si tu sors de cette bibliothèque "
    "avec une seule pratique corporelle régulière, fais en sorte que ce soit l'une des techniques SE."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Le trauma n\'est pas l\'événement. C\'est l\'énergie figée dans le corps qui n\'a pas pu se décharger après l\'événement.</b>', pull_quote))
story.append(P(
    "Cette distinction est révolutionnaire. Deux personnes peuvent vivre le même accident — l'une développe "
    "un trauma chronique, l'autre non. La différence n'est pas la sévérité de l'événement. C'est ce qui se "
    "passe APRÈS : la décharge a-t-elle pu avoir lieu ? Si oui, le système nerveux retrouve son équilibre. "
    "Si non, l'énergie reste piégée, et le SN reproduit indéfiniment les réflexes de survie."
))
story.append(P("Les mécanismes exposés", h_subsection))
story.append(P(
    "<b>1. La triade fight/flight/freeze :</b> face à une menace mortelle, l'organisme tente d'abord de combattre, "
    "puis de fuir. Si les deux sont impossibles, il fige (« je fais le mort »). Le figement n'est pas "
    "passif — c'est une activation interne énorme avec inhibition motrice externe. "
    "<b>2. Le réflexe d'achèvement :</b> tous les mammifères ont un mécanisme automatique de décharge "
    "post-menace. Animaux : tremblements visibles, secouements, sursauts. Humains : ce réflexe est inhibé "
    "(« calme-toi », anesthésie, contrôle social). "
    "<b>3. L'énergie figée :</b> sans décharge, l'énergie de survie reste dans le système. Elle s'exprime "
    "ensuite en symptômes : hypervigilance, anxiété, douleurs chroniques, problèmes de sommeil, "
    "comportements compulsifs. "
    "<b>4. La sensation ressentie (felt sense) :</b> capacité à percevoir les sensations corporelles subtiles. "
    "C'est l'outil principal du SE. "
    "<b>5. La pendulation :</b> oscillation contrôlée entre activation et calme, qui permet à l'énergie "
    "figée de se libérer en douceur, sans retraumatiser. "
    "<b>6. La titration :</b> doses minuscules de matériel traumatique, plutôt que confrontation massive."
))
story.append(P("Les voies de réparation proposées", h_subsection))
story.append(P(
    "Le protocole SE consiste à <b>réactiver doucement</b> les sensations corporelles liées au trauma, dans "
    "un contexte sécurisé, et à <b>permettre la décharge</b> (tremblements spontanés, mouvements, respirations) "
    "qui n'a pas pu avoir lieu à l'origine. C'est un travail lent (souvent 1-2 ans), patient, qui se fait "
    "idéalement avec un praticien certifié. Mais Levine donne aussi des exercices simples pour pratiquer "
    "seul. La règle d'or : <b>jamais forcer, toujours doser</b>. Si tu sens que ça déborde, tu reviens "
    "au calme. Tu oscilles. Tu ne plonges jamais dans le matériel traumatique."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Le ton du livre est parfois mystique (références à la « sagesse animale », au « tigre intérieur »). "
    "Si ce langage te dérange, ne te bloque pas — la méthode sous-jacente est très solide scientifiquement. "
    "Levine est un PhD en biophysique médicale, pas un chamane. La science derrière SE a été validée par "
    "des études cliniques depuis 2000. Le livre date de 1997, donc certaines références scientifiques sont "
    "datées — mais la méthode reste à la pointe."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Réveiller le tigre",
    [
        {"label": "THÈSE", "leaves": ["énergie figée", "décharge inachevée"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["fight/flight/freeze", "réflexe achèvement", "inhibition humaine"], "color": ACCENT},
        {"label": "MÉTHODE SE", "leaves": ["felt sense", "pendulation", "titration", "SIBAM"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Somatic Experiencing — comment libérer l'énergie figée du trauma.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(4, 1, "L'observation des animaux",
    "Pourquoi les antilopes ne deviennent pas anxieuses chroniques", ACCENT))
story.extend(idee(
    "Une antilope poursuivie par un guépard vit une menace de mort absolue. Si elle survit, dans les minutes "
    "qui suivent, elle <b>tremble, secoue son corps, respire profondément</b>. Quelques heures plus tard, elle "
    "broute calmement. Elle n'a pas de cauchemars. Elle ne développe pas d'anxiété. La menace est intégrée. "
    "Les animaux savent quelque chose que nous avons désappris."
))
story.extend(mecan(
    "Le mécanisme est neurologique. Pendant la menace, le système nerveux active une énergie de survie massive "
    "(sympathique). Pour que cette énergie soit utile, elle doit ensuite être <b>déchargée</b> par le système "
    "moteur (course, combat) ou par des décharges autonomes (tremblements, secouements). Si la décharge a lieu, "
    "le SN revient au baseline. Si elle n'a pas lieu, l'énergie reste dans le système et continue de produire "
    "les effets de la menace, même quand la menace est partie."
))
story.extend(lien([
    "Toi en 2022 : accident de trottinette. Activation sympathique maximale, probablement passée par tous "
    "les stades — surprise, mobilisation, peut-être figement. Puis coma. Puis anesthésie générale (qui "
    "<b>bloque</b> chimiquement toute possibilité de décharge). Puis opérations multiples (autres anesthésies). "
    "Puis immobilisation prolongée pendant la rééducation (le corps ne peut pas trembler ou bouger comme il "
    "voudrait).",
    "C'est presque le scénario parfait pour que l'énergie reste figée. Ton corps a vécu une activation maximale "
    "à laquelle il n'a JAMAIS pu apporter de décharge naturelle. Aujourd'hui, trois ans après, ton SN cherche "
    "à le faire — c'est probablement une des raisons de ton intolérance au calme, de ton besoin d'intensité, "
    "de ton hyperréactivité. <b>Ton corps demande à décharger ce qui n'a jamais été déchargé.</b>",
    "C'est pour ça que les pratiques somatiques (Somatic Experiencing, TRE, yoga trauma-sensitive) sont "
    "indispensables pour toi. Elles permettent — en sécurité, en doses, accompagné — d'<b>achever</b> la "
    "décharge inachevée de 2022."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu sens une agitation montante dans le corps. Tu interprètes « besoin de trader ». Tu cliques. "
    "Tu satisfais temporairement le besoin de décharge en injectant de l'intensité par le trading. "
    "Mais cette décharge n'est pas celle dont ton corps a besoin — c'est une décharge artificielle qui "
    "alimente d'autres patterns destructeurs.",
    "<b>Cible :</b> tu sens l'agitation. Tu reconnais : « c'est de l'énergie de 2022 qui demande à sortir, "
    "pas un signal de marché ». Tu vas au sac de frappe 15 min. Tu cours 20 min. Tu danses 10 min sur "
    "musique intense puis tu te poses. Tu offres à ton corps le mouvement qu'il cherchait, mais dans un "
    "cadre constructif. La décharge se fait à sa juste place."
]))
story.append(P("Schéma — L'antilope vs Marien", h_subsection))
story.extend(ascii_schema("""
   L'ANTILOPE                              MARIEN EN 2022
   ──────────                              ───────────────
   Menace (guépard)                        Menace (accident)
        │                                       │
        ▼                                       ▼
   Mobilisation totale                     Mobilisation totale
   du SN                                   du SN
        │                                       │
        ▼                                       ▼
   Course / fuite / combat                 Coma immédiat
        │                                       │
        ▼                                       ▼
   Si survie : decharge AUTO               Anesthésies multiples
   - tremblements                          (BLOQUENT décharge)
   - secouements                                │
   - respirations profondes                     ▼
        │                                  Immobilisation
        ▼                                  prolongée
   SN revient au baseline                       │
        │                                       ▼
        ▼                                  Énergie figée
   Antilope broute en paix.                pendant 3 ans.
                                                │
                                                ▼
                                          Symptômes actuels
                                          (besoin intensité,
                                          hypervigilance, etc.)

   → Ton corps cherche encore aujourd'hui à terminer la décharge.
""", accent=ACCENT))
story.extend(exo([
    "<b>L'exercice du tigre (Levine).</b> Allongé au sol, yeux fermés. Tu te connectes à ta respiration. Tu "
    "imagines un tigre qui te poursuit (oui, c'est étrange — fais-le quand même). Tu sens dans tes jambes "
    "l'envie de courir, dans tes bras l'envie de combattre. Tu LAISSES tes muscles se contracter doucement, "
    "sans bouger physiquement. Tu remarques où ton corps veut se mobiliser. Après 5-10 min, tu te laisses "
    "trembler / secouer si ça vient. Tu n'inhibes pas. Tu observes.",
    "<b>Décharge sportive structurée.</b> 3x/semaine : 20 min de sport intense (sprint, box, équitation "
    "explosive) suivi obligatoirement de 10 min de retour au calme conscient (respi, allongé, observation). "
    "Tu cycles activation et décharge. C'est le rythme naturel de ton SN."
]))
story.extend(phrase("Mon corps cherche à terminer une décharge inachevée. Je lui donne le cadre pour le faire."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(4, 2, "La sensation ressentie (felt sense)",
    "L'outil principal de la réparation somatique", ACCENT))
story.extend(idee(
    "La <b>sensation ressentie</b> (felt sense, terme emprunté à Eugene Gendlin) est la capacité à percevoir "
    "ton corps de l'intérieur — pas en pensée, en sensation. Sans cette capacité, aucun travail somatique "
    "n'est possible. Pour la plupart des traumatisés, cette capacité est très atrophiée. La restaurer est "
    "le premier travail."
))
story.extend(mecan(
    "Quand tu te demandes « comment je vais ? », tu réponds normalement par un mot (« bien », « fatigué »). "
    "C'est une réponse <b>cognitive</b>. La sensation ressentie, c'est différent : tu fermes les yeux, tu "
    "diriges ton attention dans ton corps, et tu remarques des sensations subtiles — une chaleur dans la "
    "poitrine, une tension dans la nuque, un creux dans le ventre, un picotement dans les mains. Ces "
    "sensations <b>précèdent</b> les mots. Elles sont la voix de ton corps avant traduction mentale."
))
story.extend(lien([
    "Toi tu vis beaucoup en tête. Le trading t'a renforcé dans cette habitude — analyser, prédire, calculer. "
    "Tu as développé une compétence verticale (mentale) au prix de ta compétence horizontale (corporelle). "
    "Ta connexion à ta sensation ressentie est probablement faible aujourd'hui.",
    "C'est précisément pourquoi tu te fais surprendre par tes états. Quand l'agitation monte, tu ne la sens "
    "pas venir — tu te retrouves d'un coup à cliquer sans avoir vu venir l'élan. Si tu restaurais ta sensation "
    "ressentie, tu remarquerais l'agitation au stade 2 sur 10, pas au stade 9 sur 10. Tu aurais le temps "
    "d'intervenir avant le déclic.",
    "Ta filly et les chevaux en général t'aident à restaurer cette capacité. Le contact avec un animal — "
    "particulièrement un cheval, dont le système nerveux est très sensible aux sensations subtiles — réveille "
    "naturellement ta sensation ressentie. Quand tu poses ta main sur son flanc, ton attention plonge dans "
    "ton propre corps. C'est de l'entraînement somatique."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu trades XAUUSD. Le marché stagne. Tu ressens monter — quoi exactement ? Tu ne sais pas. "
    "Tu cliques un setup B-grade. Tu réalises 30 secondes après que tu ne sais même pas pourquoi tu as cliqué.",
    "<b>Cible :</b> tu trades. Le marché stagne. Tu ressens monter <b>quelque chose</b>. Tu PRENDS 30 secondes "
    "pour identifier : « c'est dans ma poitrine, c'est une chaleur, c'est associé à une légère respiration "
    "courte ». Tu nommes : « c'est de l'impatience corporelle ». Tu sais maintenant que cette sensation n'a "
    "rien à voir avec le marché — c'est ton SN qui réclame de la stimulation. Tu ne cliques pas. Tu fermes "
    "la plateforme. Tu fais 5 min de respiration."
]))
story.append(P("Le vocabulaire de la sensation ressentie", h_subsection))
story.append(styled_table([
    [C("Catégorie", cell_gold), C("Exemples de descripteurs", cell_gold)],
    [C("Température", cell_bold),
     C("chaud, brûlant, frais, glacé, tiède, brûle, gèle")],
    [C("Texture / qualité", cell_bold),
     C("dense, fluide, granuleux, lisse, vide, plein, vibrant, immobile")],
    [C("Mouvement", cell_bold),
     C("monte, descend, irradie, palpite, pousse, tire, s'étend, se contracte")],
    [C("Localisation", cell_bold),
     C("poitrine, ventre, gorge, épaules, mâchoire, nuque, bassin, jambes, mains")],
    [C("Intensité (1-10)", cell_bold),
     C("noter sur 10 — permet de mesurer la pendulation au fil du temps")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Scan corporel quotidien.</b> Matin et soir, 5 min, allongé. Tu balaies de la tête aux pieds. À chaque "
    "zone, tu cherches une sensation. Tu décris avec le vocabulaire du tableau. Tu ne corriges rien. Tu observes.",
    "<b>L'entraînement à la sensation au cheval.</b> Pendant le pansage de ta filly, 5 min de présence "
    "totale au contact. Qu'est-ce que tu ressens dans TES mains ? Dans TON ventre ? Dans TES jambes ? "
    "Le cheval est ton coach somatique gratuit.",
    "<b>Stop sensations pré-trade.</b> Avant CHAQUE clic, 30 secondes : qu'est-ce que je ressens dans mon "
    "corps maintenant ? Si la sensation dominante est de l'agitation, du désir, de la précipitation : tu ne "
    "cliques pas. Tu attends que la sensation soit du calme stable."
]))
story.extend(phrase("Mon corps parle avant ma tête. J'apprends à écouter le corps en premier."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(4, 3, "La pendulation",
    "Osciller entre activation et calme — pas plonger", ACCENT))
story.extend(idee(
    "La pendulation est le mouvement naturel du SN entre activation (sympathique) et calme (parasympathique). "
    "Dans un SN sain, cette oscillation se fait fluidement, plusieurs fois par jour. Dans un SN traumatisé, "
    "elle est bloquée — soit en activation chronique, soit en figement. Le travail somatique consiste à "
    "<b>restaurer la pendulation</b> en douceur, par doses, sans jamais forcer."
))
story.extend(mecan(
    "Quand tu touches une sensation corporelle inconfortable (tension, peur, vide), la tendance est de soit "
    "<b>plonger</b> dedans (s'y noyer), soit <b>fuir</b> (changer de sujet). Les deux sont contre-productifs. "
    "La pendulation consiste à : <b>1)</b> toucher brièvement la sensation inconfortable, <b>2)</b> revenir "
    "vers une ressource (sensation agréable, image apaisante, contact d'un proche), <b>3)</b> revenir au "
    "matériel inconfortable plus brièvement, <b>4)</b> revenir à la ressource. À force, tu enseignes à ton "
    "SN qu'il peut traverser l'inconfort et revenir au calme. C'est la base de la réparation."
))
story.extend(lien([
    "Toi tu fonctionnes typiquement par plongée puis fuite. Tu plonges dans le trade — tu y mets toute ton "
    "énergie, ta tension, ton désir. Quand ça crashe, tu fuis (Netflix, alcool, écran, isolement). Tu n'as "
    "jamais d'oscillation contrôlée. Soit tout, soit rien. Ton SN ne sait plus pendulator.",
    "L'apprentissage de la pendulation est donc fondamental pour toi. Concrètement : tu apprends à toucher "
    "une émotion difficile (par exemple, la frustration après un crash) sans t'y noyer, puis à revenir à une "
    "ressource (ta filly, une respiration profonde, un souvenir agréable précis), puis à revenir à la "
    "frustration plus brièvement, puis à la ressource, etc.",
    "C'est cette compétence qui te manque dans le trade. Quand le PnL bascule, tu plonges dans la panique. "
    "Tu n'oscilles pas. La pendulation t'apprendrait à toucher la peur de la perte (5 secondes) puis revenir "
    "au calme (5 secondes), oscillation qui dépressurise progressivement."
]))
story.append(P("Le protocole pendulation — pour une émotion difficile", h_subsection))
story.extend(ascii_schema("""
   1. RESSOURCE        →  Identifie une sensation agréable disponible
                          (chaleur dans le ventre, respiration ample,
                          image de ta filly, contact d'un être aimé).
                          Tu la ressens 30 sec - 1 min. Tu t'ancres.

   2. MATÉRIEL DIFF.   →  Tu touches BRIÈVEMENT (5-10 sec max)
                          la sensation inconfortable.
                          Tu remarques. Tu ne plonges pas.

   3. RETOUR RESSOURCE →  Tu reviens à ta sensation agréable.
                          30 sec - 1 min. Tu te re-régule.

   4. MATÉRIEL DIFF.   →  Tu touches à nouveau, plus brièvement.
                          3-5 sec.

   5. RESSOURCE        →  Retour.

   6. ITÉRATIONS       →  Tu continues 6-10 cycles.

   Effet : le SN apprend que l'inconfort est traversable.
           L'énergie figée se libère par micro-doses.
           Tu ne retraumatises jamais.
""", accent=ACCENT))
story.extend(exemple([
    "<b>Saboteur :</b> tu viens de craquer un compte. Tu plonges dans la honte/colère. Tu y restes 4 heures. "
    "Tu sors par fuite (alcool, écran, isolement). Tu n'as rien traité.",
    "<b>Cible :</b> tu craques un compte. Tu identifies une ressource (image de ta filly broutant calme dans "
    "le pré). Tu touches 5 sec la honte (« j'ai cramé »). Tu reviens 30 sec à la filly. Tu touches 5 sec "
    "la colère envers toi-même. Tu reviens 30 sec. Tu touches 5 sec le sentiment d'échec. Tu reviens. "
    "Tu fais 8 cycles. Au bout, l'émotion est traversée, pas refoulée."
]))
story.extend(exo([
    "<b>Pendulation quotidienne.</b> Une fois par jour, 5 min : tu choisis une petite gêne corporelle "
    "(tension dans la nuque, agitation, malaise vague). Tu fais le protocole 1-2-3-4-5-6. C'est ton "
    "entraînement.",
    "<b>Pendulation post-trade perdant.</b> Après chaque trade perdant (pas chaque crash, chaque trade), "
    "tu fais 3 cycles courts. Tu enseignes à ton SN que la perte est traversable, pas effondrante.",
    "<b>Identification de tes ressources stables.</b> Liste 5 ressources somatiques disponibles 24h/24 : "
    "image, sensation, lieu, personne, son. Ces 5 ressources sont tes points d'ancrage pour toute "
    "pendulation."
]))
story.extend(phrase("J'oscille, je ne plonge pas. Toucher 5 secondes. Revenir 30. C'est la voie."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(4, 4, "La titration",
    "Doses minuscules — jamais affronter frontalement", ACCENT))
story.extend(idee(
    "La titration est un terme de chimie : ajouter une substance goutte par goutte pour ne pas faire "
    "exploser la réaction. Appliqué au trauma : tu n'affrontes JAMAIS le matériel traumatique frontalement. "
    "Tu y vas par gouttes. Toujours. Le système doit pouvoir <b>intégrer</b> chaque dose avant la suivante."
))
story.extend(mecan(
    "Si tu plonges dans le matériel traumatique entier, ton SN se retrouve à nouveau dans l'état originel — "
    "tu retraumatises. C'est pour ça que beaucoup de thérapies par exposition forte échouent ou aggravent. "
    "La titration force la digestion graduelle. Goutte 1 : une sensation corporelle minime liée au trauma. "
    "Tu la traverses. Tu intègres. Goutte 2 : une autre sensation, légèrement plus chargée. Tu intègres. "
    "Etc. Le système digère sans déborder."
))
story.extend(lien([
    "Pour ton TBI 2022, la titration est essentielle. Tu ne dois PAS essayer de « repenser à l'accident » en bloc, "
    "ni « revivre le coma » mentalement. Ça t'épuiserait ou te retraumatiserait. À la place : un thérapeute "
    "SE te ferait travailler par micro-bouts. Une sensation. Un détail périphérique. Une petite tension. "
    "Tu intègres chacun. À force, le tout est digéré.",
    "En trading aussi, la titration s'applique. Après un crash, ne pas vouloir « tout comprendre » en bloc. "
    "Plutôt : un détail à la fois. À 14h32 tu as ressenti quoi ? Tu décris UNE sensation. Tu intègres. Le "
    "lendemain, autre détail. À force, le pattern se révèle sans surcharge."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu viens de craquer un compte. Tu décides « ce soir je vais ENFIN comprendre ce qui m'arrive ». "
    "Tu t'enfermes 3h à ressasser, analyser, écrire. Tu finis épuisé, encore plus confus, parfois "
    "submergé. Tu n'as rien intégré — tu as retraumatisé.",
    "<b>Cible :</b> tu craques. Tu te donnes 15 min pour écrire dans le journal. Pas plus. Tu décris UNE "
    "scène précise : « à 14h32, juste avant de décaler le SL, j'ai ressenti dans la poitrine... ». Tu "
    "explores ce SEUL moment. Tu arrêtes. Tu fais une pendulation. Tu fais autre chose. Le lendemain, autre "
    "moment, 15 min. À force, tu cartographies le pattern sans te surcharger."
]))
story.extend(exo([
    "<b>Règle des 15 minutes.</b> Aucune session d'introspection ne dépasse 15 min consécutives. Au-delà, "
    "tu sors, tu fais autre chose, tu reviens éventuellement plus tard. Le SN ne tolère pas l'introspection "
    "longue après trauma.",
    "<b>Journal en gouttes.</b> Quand tu écris sur un événement difficile : tu te limites à 3-5 phrases par "
    "session. Tu reprends le lendemain, autres 3-5 phrases. À force, tu construis sans accabler.",
    "<b>Thérapie titrée.</b> Avec un praticien SE, le rythme typique est 1 séance par 2-3 semaines. PAS plus. "
    "Le temps entre séances est aussi important que les séances — c'est le temps d'intégration."
]))
story.extend(phrase("Goutte par goutte. Jamais le grand débordement. Mon SN intègre à son rythme."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(4, 5, "Le réflexe d'achèvement",
    "Permettre au mouvement bloqué de se compléter", ACCENT))
story.extend(idee(
    "Chaque trauma laisse dans le corps un <b>mouvement bloqué</b> — une action qui aurait dû se faire et "
    "qui n'a pas pu (fuir, se protéger, repousser, crier). Le réflexe d'achèvement consiste à permettre "
    "à ce mouvement de se compléter dans un cadre sécurisé. Pas mentalement — corporellement. "
    "Une fois le mouvement complet, l'énergie associée se libère."
))
story.extend(mecan(
    "Le SN garde en mémoire les actions <b>inachevées</b>. Si tu allais courir mais que tu as été immobilisé, "
    "tes muscles des jambes gardent l'impulsion de course en attente. Des années plus tard, ces muscles "
    "restent légèrement contractés, en attente. Le travail somatique permet de réveiller ces impulsions, "
    "doucement, et de les laisser s'<b>achever</b> par micro-mouvements consciemment habités."
))
story.extend(lien([
    "Toi en 2022 : les mouvements inachevés sont nombreux. Au moment de l'accident, ton corps a probablement "
    "voulu (instinctivement) : se protéger les mains, tourner la tête, freiner avec les jambes, crier. Aucun "
    "de ces mouvements n'a pu se faire correctement (vitesse + perte de conscience). Pendant le coma, "
    "ton corps a peut-être voulu bouger, tourner, dire quelque chose — anesthésie a tout bloqué. Pendant "
    "les opérations, idem.",
    "Tous ces mouvements sont en attente dans ton corps. Un praticien SE les ferait remonter doucement et "
    "laisserait ton corps les compléter dans le cabinet (souvent sous forme de micro-mouvements, "
    "tremblements, parfois sons). C'est une libération profonde. C'est probablement ce qui te permettrait "
    "de ressentir moins de pression sourde dans ton corps."
]))
story.append(P("Les micro-mouvements à explorer (en solo, doucement)", h_subsection))
story.append(styled_table([
    [C("Mouvement à explorer", cell_gold), C("Quand l'utiliser", cell_gold)],
    [C("Push (mains poussent un mur)", cell_bold),
     C("Quand tu sens de la pression / colère figée. Le geste de repousser une menace.")],
    [C("Pull (tirer une corde imaginée)", cell_bold),
     C("Quand tu sens de la déconnexion / vide. Le geste de ramener.")],
    [C("Reach (tendre les bras loin)", cell_bold),
     C("Quand tu sens un manque de lien / désir refoulé. Le geste de chercher.")],
    [C("Run (courir sur place lentement)", cell_bold),
     C("Quand tu sens de l'agitation figée dans les jambes. Le geste de fuir.")],
    [C("Voice (crier dans l'oreiller)", cell_bold),
     C("Quand tu sens un blocage à la gorge / poitrine. Le geste de protester.")],
], [5.5*cm, 10.5*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Exploration douce des mouvements bloqués.</b> Une fois par semaine, 15 min, en privé. Tu choisis "
    "UN micro-mouvement du tableau. Tu le fais LENTEMENT, avec conscience corporelle complète. Tu remarques "
    "ce qui se passe. Si des tremblements ou émotions montent : tu laisses, sans forcer. Tu reviens à "
    "la respiration calme à la fin.",
    "<b>Box conscient.</b> Tu fais déjà de la box. Fais-en aussi DE LA THÉRAPIE SOMATIQUE. Choisis 2 minutes "
    "par séance où tu frappes avec INTENTION corporelle complète — pas pour la perf, pour la décharge. "
    "Tu sentiras ton corps libérer.",
    "<b>Travail avec praticien.</b> Pour ton TBI, ce module est trop important pour le faire seul. "
    "Cherche cette semaine un praticien SE ou TRE certifié."
]))
story.extend(phrase("Mon corps a des mouvements en attente depuis 2022. Je leur donne le cadre pour s'achever."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(4, 6, "Le modèle SIBAM",
    "Cartographier ce qui se passe en toi", ACCENT))
story.extend(idee(
    "SIBAM est l'acronyme des cinq dimensions de l'expérience humaine : <b>S</b>ensation (corporelle), "
    "<b>I</b>mage (mentale, souvenir visuel), <b>B</b>ehavior (comportement, mouvement), <b>A</b>ffect "
    "(émotion), <b>M</b>eaning (sens, narration). Dans un trauma, ces dimensions sont fragmentées — "
    "tu peux avoir une sensation sans pouvoir nommer l'émotion, une image sans contexte, un comportement "
    "sans connaître son origine."
))
story.extend(mecan(
    "La réparation consiste à <b>recoudre</b> les cinq dimensions. Tu pars d'une dimension accessible "
    "(souvent la sensation), tu vas vers une autre. Tu prends ton temps. Tu intègres. Tu n'imposes pas un "
    "récit cohérent qui n'est pas encore prêt — tu laisses la cohérence émerger de la reconnexion progressive "
    "des dimensions."
))
story.extend(lien([
    "Pour ton TBI 2022, certaines dimensions sont probablement encore fragmentées. Tu as des sensations "
    "récurrentes (intolérance au calme, hypervigilance) sans qu'elles soient bien reliées à des images "
    "précises (le coma est probablement amnésique), à des émotions claires (« je ne sais pas ce que je "
    "ressens »), à des comportements identifiés (« je ne sais pas pourquoi je clique »), à un sens "
    "(« je ne comprends pas pourquoi je sabote »).",
    "Le SIBAM te donne un outil pour cartographier. Tu prends un état que tu vis (par exemple, l'envie "
    "de cliquer à 14h sans setup). Tu listes : <b>S</b> qu'est-ce que je ressens dans le corps ? "
    "<b>I</b> y a-t-il une image associée ? <b>B</b> qu'est-ce que je suis en train de faire ou voudrais "
    "faire ? <b>A</b> quelle émotion ? <b>M</b> quel sens je donne à tout ça ? Tu écris. Tu rends conscient. "
    "Tu reconnectes les fragments."
]))
story.extend(exemple([
    "<b>Saboteur :</b> 14h, envie de cliquer. Tu cliques sans rien analyser. Tu perds. Tu te dis « j'ai été "
    "impulsif ». Trois mots qui n'expliquent rien.",
    "<b>Cible :</b> 14h, envie de cliquer. Tu PAUSES. SIBAM : <b>S</b> chaleur poitrine, mâchoire serrée, "
    "ventre tendu. <b>I</b> image floue d'un compte qui grimpe vite. <b>B</b> ma main veut se diriger vers "
    "la souris. <b>A</b> émotion : un mélange de désir et d'anxiété. <b>M</b> sens : « si je ne trade pas "
    "maintenant je vais rater quelque chose ». Tu vois la mécanique en 5 dimensions. Tu sais que rien n'est "
    "marché — tout est interne. Tu ne cliques pas."
]))
story.extend(exo([
    "<b>Cartographie SIBAM hebdomadaire.</b> Une fois par semaine, prends un état récurrent (envie de cliquer, "
    "agitation, vide) et fais le SIBAM complet par écrit. Tu cartographies. À force, tu auras 10-15 "
    "cartographies qui révéleront tes patterns profonds.",
    "<b>Le SIBAM en temps réel.</b> Avant chaque trade : 30 secondes pour passer les 5 dimensions. Si une "
    "dimension révèle un signal de SN traumatisé (pas de signal de marché), tu ne cliques pas."
]))
story.extend(phrase("Cinq dimensions. Je les nomme. Je les reconnecte. Le trauma se digère par reconnexion."))
story.append(PageBreak())


# --- LIVRE 4 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 4", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Le trauma n'est pas l'événement. C'est l'énergie figée qui n'a pas pu se décharger après.",
    "Les animaux déchargent naturellement (tremblements). Les humains inhibent. D'où le trauma chronique.",
    "Ton 2022 a été une activation max sans aucune possibilité de décharge (anesthésies, immobilisation).",
    "Trois mots-clés SE : Felt Sense, Pendulation, Titration.",
    "La sensation ressentie est l'outil principal. Sans elle, aucun travail somatique possible.",
    "La pendulation oscille entre activation et calme. Jamais plonger.",
    "La titration : doses minuscules. Jamais le grand débordement.",
    "Le réflexe d'achèvement permet aux mouvements bloqués de se compléter.",
    "SIBAM cartographie les 5 dimensions (sensation, image, comportement, affect, sens).",
    "La box et l'équitation sont déjà des outils pour toi. Utilise-les en conscience somatique.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Essayer de tout comprendre mentalement.",
    "Plonger dans le matériel traumatique d'un coup.",
    "Ignorer les sensations corporelles subtiles.",
    "Forcer le calme au lieu de le pratiquer en oscillation.",
    "Faire des sessions d'introspection longues (> 15 min).",
    "Interpréter chaque agitation comme signal de marché.",
    "Refuser un praticien somatique « parce que je me débrouille ».",
    "Faire box ou équitation en mode performance sans conscience corporelle.",
    "Vouloir des résultats rapides (SE prend 6-24 mois).",
    "Confondre amnésie du coma avec « rien à traiter ».",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je consulte un praticien Somatic Experiencing certifié.",
    "Je fais un scan corporel matin et soir.",
    "Je pendule au lieu de plonger (5 sec inconfort / 30 sec ressource).",
    "Je titre toujours : 15 min max d'introspection consécutive.",
    "Je fais SIBAM pour chaque état confus.",
    "Je fais 1 séance de mouvement libre exploratoire par semaine.",
    "Je pratique 5 min de respiration cohérente avant chaque trade.",
    "Je pansa ma filly avec présence totale 1x/semaine min.",
    "Je box pour me décharger, pas seulement pour performer.",
    "Je laisse mon corps trembler ou bouger spontanément quand ça vient.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║          RÉVEILLER LE TIGRE  —  FICHE D'ANCRAGE          ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Le trauma = énergie figée. Je la décharge en doses.     ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Plonger frontalement. Forcer. Vouloir tout en bloc.     ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE                                           ║
   ║    - Pression sourde sans cause                            ║
   ║    - Tension chronique nuque/mâchoire                      ║
   ║    - Énergie qui réclame sans direction                    ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Sensation ressentie : qu'est-ce que je sens ?        ║
   ║    2. Si charge : pendulation (5 sec / 30 sec)             ║
   ║    3. Si mouvement bloqué : micro-geste conscient          ║
   ║    4. Décharge structurée (box, course, danse)             ║
   ║       puis retour au calme 10 min.                         ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Goutte par goutte. Mon corps se libère à son rythme." ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Cette semaine : 1 séance d'exploration de mouvement     ║
   ║    bloqué (push, pull, reach, run, voice).                 ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    SIBAM avant chaque trade (5 dimensions).                ║
   ║    Si dimension révèle SN figé : pas de trade.             ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 4 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 5 — TRADER DANS LA ZONE (Mark Douglas)
# ============================================================
_current_book_color[0] = BOOK_COLORS[4]
ACCENT = BOOK_COLORS[4]

story.extend(book_separator_page(
    5, "Trader dans la zone", "Mark Douglas", "Trading in the Zone", 2000, ACCENT,
    quote='« Tout peut arriver sur le marché.<br/>Tu n\'as pas besoin de le prédire pour gagner. »',
    subtitle="Maîtriser le marché par la confiance, la discipline et le mental"
))

story.extend(book_intro_header(5, "Trader dans la zone", "Mark Douglas — 2000", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "Mark Douglas est le livre fondateur de la psychologie de trading moderne. Hougaard, Steenbarger, "
    "tous les auteurs sérieux qui ont écrit après 2000 sont des héritiers de Douglas. Si Hougaard te dit "
    "« perds mieux », Douglas te dit <b>pourquoi</b> tu ne perds pas mieux — et comment ré-architecturer "
    "ta pensée pour y arriver."
))
story.append(P(
    "Ce livre est plus dense, plus exigeant intellectuellement que Hougaard. C'est un livre où chaque "
    "concept demande à être <i>digéré</i>, pas juste lu. Il te confronte à ce qui est probablement ta "
    "principale faiblesse mentale en trading : <b>tu raisonnes en certitudes alors que le marché est "
    "fondamentalement probabiliste</b>. Cette dissonance est la source de la quasi-totalité de tes "
    "comportements destructeurs."
))
story.append(P(
    "À placer en cinquième position parce qu'il demande que tu aies déjà compris les blocages corporels "
    "(Levine, van der Kolk) et chimiques (Lembke). Sans cette base, le travail mental que propose Douglas "
    "ne s'installe pas — ton SN sabote l'apprentissage mental. Une fois le corps en cours de réparation, "
    "Douglas devient extrêmement opérationnel."
))
story.append(P(
    "Lis-le lentement. Annote. Reviens dessus. C'est un livre à habiter pendant 3-6 mois, pas à expédier "
    "en une semaine."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Le trader rentable a fait la paix avec l\'incertitude. Le trader perdant la combat encore.</b>', pull_quote))
story.append(P(
    "Toute la différence se joue là. Le marché est fondamentalement probabiliste : chaque trade individuel "
    "est imprévisible, mais une distribution de 100 trades exécutés selon un edge valide produit un résultat "
    "statistique stable. Le trader rentable accepte cette nature. Il joue la distribution. Le trader perdant "
    "veut savoir si CE trade va marcher. Il combat l'incertitude au lieu de jouer avec elle. C'est ce combat "
    "qui produit la majorité de ses erreurs."
))
story.append(P("Les mécanismes mentaux exposés", h_subsection))
story.append(P(
    "<b>1. Le piège de l'analyse plus poussée :</b> les traders en difficulté cherchent une certitude "
    "supplémentaire dans plus d'analyse. C'est une fausse piste — la certitude ne viendra jamais. "
    "<b>2. La confusion micro/macro :</b> tu juges ton edge sur quelques trades alors qu'il s'évalue sur "
    "des centaines. <b>3. Les croyances limitantes :</b> tes convictions inconscientes (sur l'argent, "
    "le mérite, le risque) déterminent ton comportement bien plus que ta méthode. <b>4. Les quatre "
    "peurs fondamentales du trader :</b> peur de perdre, peur de rater, peur de se tromper, peur de "
    "laisser de l'argent sur la table. Chacune produit des erreurs spécifiques. <b>5. L'état mental "
    "du gagnant constant :</b> confiance + discipline + perspective probabiliste."
))
story.append(P("Les transformations proposées", h_subsection))
story.append(P(
    "<b>Accepter le risque pour de bon</b> — pas dire qu'on l'accepte, le ressentir corporellement. "
    "<b>Penser en probabilités</b> — réécrire le câblage mental qui veut du « oui/non » et apprendre à "
    "fonctionner en « probabilité de A vs B ». <b>Installer des croyances productives</b> — pas par "
    "affirmation mentale forcée, mais par expérience cumulative. <b>Créer un état de flow trader</b> — "
    "l'état où tu exécutes sans friction, sans questionnement, sans drame."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Douglas est connu pour être <b>répétitif</b> — il revient sur les mêmes idées sous des angles légèrement "
    "différents. Ça peut être agaçant. Mais c'est probablement délibéré : il faut entendre 5-6 fois pour "
    "vraiment intégrer. Le livre est aussi très anglo-saxon des années 2000 — peu de neurosciences, "
    "beaucoup d'introspection. À compléter avec van der Kolk et Lembke pour la dimension corporelle. "
    "Pas de protocole jour-par-jour — c'est un livre de réorientation mentale, pas un manuel d'application."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Trader dans la zone",
    [
        {"label": "THÈSE", "leaves": ["paix avec incertitude", "probabilités > certitudes"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["piège analyse", "4 peurs trader", "croyances limitantes"], "color": ACCENT},
        {"label": "ÉTAT CIBLE", "leaves": ["confiance", "discipline", "perspective probabiliste"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("La structure mentale du trader rentable — état de zone.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(5, 1, "Le piège de l'analyse plus poussée",
    "Pourquoi plus d'analyse ne te sauvera pas", ACCENT))
story.extend(idee(
    "Le trader en difficulté pense qu'une analyse plus précise va lui apporter la certitude qui lui manque. "
    "C'est la fausse piste numéro un. La certitude qu'il cherche n'existe pas, ne peut pas exister. "
    "Continuer à chercher est une fuite, pas une solution."
))
story.extend(mecan(
    "La nature du marché est statistique. Chaque trade individuel a un résultat probabiliste. Aucune analyse, "
    "même parfaite, ne peut transformer une probabilité en certitude. Quand tu cherches plus d'analyse, "
    "tu cherches à apaiser une anxiété (« et si je me trompais ? ») par un moyen qui ne peut pas marcher. "
    "C'est comme essayer d'éteindre un feu en y jetant de l'huile : tu accumules de la connaissance qui "
    "produit l'illusion d'un contrôle, et tu te crispes davantage quand le marché te dément."
))
story.extend(lien([
    "Tu as exactement ce pattern. Quand tu galères, ton premier réflexe est d'apprendre encore. Un nouveau "
    "confluence, un nouveau timeframe, un nouveau mentor SMC. Tu cherches LA pièce manquante qui va te "
    "donner la certitude. Cette pièce n'existe pas. Plus tu la cherches, plus tu construis un système "
    "complexe qui aggrave ta rigidité mentale.",
    "Tu as déjà SMC, killzones, FVG, OB, CHoCH, bias macro. C'est largement plus de signal que la plupart "
    "des traders rentables n'utilisent. Le problème n'est pas que tu manques d'information. Le problème est "
    "que tu attends de l'information qu'elle te donne ce qu'elle ne peut pas donner : la certitude.",
    "Ta sortie : <b>arrêter d'ajouter</b>. Pendant 6 semaines minimum, aucun nouvel outil, aucune nouvelle "
    "vidéo, aucun nouveau mentor. Tu utilises STRICTEMENT ce que tu as. Tu observes ce qui se passe. "
    "Tu vas découvrir que ce qui manque n'est pas dans l'info — c'est dans l'exécution."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu prends 3 trades XAUUSD perdants en deux jours. Tu te dis « j'ai loupé quelque chose, "
    "il me manque un confirm de plus ». Tu passes ta soirée à étudier le delta volume. Le lendemain tu "
    "ajoutes ce filtre. Cinquième trade, le delta volume confirme. Tu rentres. Tu perds quand même.",
    "<b>Cible :</b> 3 trades perdants. Tu reconnais : « 3 trades ne disent rien sur mon edge. Je joue 100. » "
    "Tu n'ajoutes RIEN à ta méthode. Tu maintiens. Le 4e trade : setup A+ comme tu sais le voir. Tu le prends. "
    "Tu acceptes que le résultat ne sera connu que sur 100 occurrences. Pas sur celui-ci."
]))
story.append(P("Schéma — La spirale de l'analyse plus poussée", h_subsection))
story.extend(ascii_schema("""
   Trade perdant                              Acceptation
        │                                          │
        ▼                                          ▼
   Anxiété d'avoir tort                       "Je joue 100 trades."
        │                                          │
        ▼                                          ▼
   Recherche de certitude                     Pas de modification.
        │                                          │
        ▼                                          ▼
   Ajout d'un outil                           Trade suivant exécuté
        │                                     comme prévu.
        ▼                                          │
   Système plus complexe                          ▼
        │                                     Distribution se révèle
        ▼                                     sur la longueur.
   Plus de paramètres = plus
   d'occasions de paralyser
        │
        ▼
   Hésitation + retard d'entrée
        │
        ▼
   Perte aggravée
        │
        ▼ (boucle)
   Nouvelle anxiété
""", accent=ACCENT))
story.extend(exo([
    "<b>Audit des sur-additions.</b> Liste tous les outils, filtres, confluences que tu utilises actuellement "
    "en trading. Probablement 8-15 paramètres. Identifie les 3-5 qui sont essentiels. Les autres sont "
    "probablement des additions anxieuses. Tu peux en enlever sans dégrader ton edge.",
    "<b>Règle du minimum viable.</b> Pendant 4 semaines : aucune nouvelle source d'info. Aucun nouveau "
    "paramètre. Tu travailles avec exactement ce que tu as aujourd'hui. Tu observes ce qui se passe."
]))
story.extend(phrase("La certitude n'existe pas. Plus d'analyse ne la crée pas. J'arrête d'ajouter."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(5, 2, "Penser en probabilités",
    "Réécrire le câblage qui veut du oui/non", ACCENT))
story.extend(idee(
    "Le cerveau humain est câblé pour la pensée binaire — oui/non, sécurité/danger, bon/mauvais. Cette pensée "
    "a été utile dans la savane. Elle est désastreuse pour le trading. Penser en probabilités est un mode "
    "mental qui demande à être <b>activement entraîné</b>. Ça ne vient pas tout seul, même si tu sais "
    "intellectuellement que c'est utile."
))
story.extend(mecan(
    "La pensée probabiliste consiste à internaliser que <b>chaque événement a une probabilité, pas une "
    "certitude</b>. Un setup A+ XAUUSD en NY killzone n'est pas « ça va marcher ». C'est « ça a, disons, 58% "
    "de chances de marcher selon ma série historique ». Cette transformation grammaticale change tout : "
    "tu ne cherches plus à avoir raison, tu joues une probabilité. Le résultat individuel ne porte plus la "
    "charge identitaire."
))
story.extend(lien([
    "Toi tu fonctionnes encore en binaire. Quand tu prends un trade, tu te dis « ce trade VA marcher ». Cette "
    "phrase est l'origine de ton problème +1500. Si tu te dis qu'il VA marcher, alors quand le marché te "
    "donne raison, tu veux encore plus de validation (donc tu pousses). Et quand le marché te contredit, "
    "tu refuses parce que ça remet en cause ta conviction (donc tu décales).",
    "Si tu te disais « ce trade a 55-60% de chances de gagner, je joue ma série » : quand le marché te donne "
    "raison, tu coupes au TP parce que c'est ce que ta probabilité prévoyait. Quand le marché te contredit, "
    "tu coupes au SL parce que c'est dans la distribution attendue. Aucune charge émotionnelle parce qu'aucun "
    "trade individuel ne dit rien sur toi."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu rentres long XAUUSD. Tu te dis « ça va monter, le bias est haussier, mon setup est "
    "propre ». Marché atteint TP. Tu te dis « j'avais raison, donc ça va monter encore ». Tu pousses. "
    "Tu cramés.",
    "<b>Cible :</b> tu rentres long XAUUSD. Tu te dis « ce setup A+ donne historiquement 55% gagnants avec "
    "RR 1:2. Je joue ma série de 100. Celui-ci peut être un perdant ou un gagnant — le résultat ne dit rien "
    "sur la qualité du setup. » Marché atteint TP. Tu coupes. C'est ce que ton plan probabiliste prévoyait. "
    "Tu ne pousses pas — pousser, ce serait sortir de la statistique connue et entrer dans l'inconnu "
    "non testé."
]))
story.append(P("Le langage binaire vs probabiliste", h_subsection))
story.append(styled_table([
    [C("Pensée binaire (à éviter)", cell_gold), C("Pensée probabiliste (cible)", cell_gold)],
    [C("« Ça va monter »"), C("« 55% de chances que ça monte selon mon setup »")],
    [C("« J'ai raison »"), C("« Mon hypothèse a une probabilité plus haute que sa contraire »")],
    [C("« Ce trade doit marcher »"), C("« Ce trade est une instance de ma série »")],
    [C("« Je me suis trompé »"), C("« Ce trade est dans les 45% qui perdent normalement »")],
    [C("« Mon edge ne marche plus »"), C("« Sur 5 trades, je n'ai pas assez de données »")],
    [C("« Le marché est imprévisible »"), C("« Chaque trade est imprévisible, la série est prévisible »")],
], [7.5*cm, 8.5*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Le journal probabiliste.</b> Pour chaque trade que tu prends, écris la phrase : « Ce setup donne X% "
    "de gagnants historiquement avec RR Y:Z. Je joue ma série. » Si tu ne peux pas remplir cette phrase, "
    "tu ne dois pas prendre le trade (ça veut dire que tu n'as pas backtesté ta méthode).",
    "<b>Substitution grammaticale.</b> Pendant 30 jours, chaque fois que tu te surprends à dire mentalement "
    "« ça va », « ça doit », « j'ai raison » : tu reformules en probabilité. Le langage modifie la pensée."
]))
story.extend(phrase("Je ne dis plus « ça va marcher ». Je dis « ce setup a X% selon ma série »."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(5, 3, "Les 5 vérités fondamentales",
    "Les axiomes à graver dans le système nerveux", ACCENT))
story.extend(idee(
    "Douglas formule cinq vérités axiomatiques que le trader rentable a intégrées au niveau réflexe. "
    "Ce ne sont pas des concepts à savoir — ce sont des automatismes mentaux qui doivent fonctionner "
    "sans effort. Tant qu'elles sont au niveau intellectuel uniquement, elles ne protègent pas. Tant "
    "qu'elles sont au niveau réflexe, elles deviennent ton armure."
))
story.append(P("Les cinq vérités, formulées simplement", h_subsection))
story.append(styled_table([
    [C("Vérité", cell_gold), C("Formulation", cell_gold), C("Conséquence pratique", cell_gold)],
    [C("V1", cell_bold), C("Tout peut arriver sur le marché.",
                            cell_bold),
     C("Aucun setup n'a 100%. Le SL est sacré.")],
    [C("V2", cell_bold), C("Tu n'as pas besoin de savoir ce qui va arriver pour gagner.",
                            cell_bold),
     C("La prédiction n'est pas l'objectif. Le plan oui.")],
    [C("V3", cell_bold), C("Il y a une distribution aléatoire des gagnants et perdants à l'intérieur d'un edge valide.",
                            cell_bold),
     C("3 pertes consécutives ne disent rien sur l'edge.")],
    [C("V4", cell_bold), C("Un edge est juste une probabilité plus haute d'un mouvement plutôt qu'un autre.",
                            cell_bold),
     C("Un edge à 55% n'est pas une certitude. C'est un edge.")],
    [C("V5", cell_bold), C("Chaque instant du marché est unique.",
                            cell_bold),
     C("Le passé informe, ne détermine pas. Pas de revanche.")],
], [1*cm, 7*cm, 8*cm]))
story.append(Spacer(1, 8))
story.extend(mecan(
    "Le problème de ces 5 vérités, c'est qu'elles s'opposent directement à des réflexes profonds du cerveau "
    "humain. <b>V1</b> contredit le besoin de prédiction. <b>V2</b> contredit le besoin de contrôle. "
    "<b>V3</b> contredit le pattern recognition à court terme. <b>V4</b> contredit le besoin de certitude. "
    "<b>V5</b> contredit la mémoire affective (« la dernière fois ça a marché donc cette fois aussi »). "
    "Intégrer ces vérités au niveau réflexe demande de la <b>répétition consciente</b>, comme on installe "
    "n'importe quel automatisme : par exposition fréquente sur une période longue (6-12 mois)."
))
story.extend(lien([
    "Pour toi en pratique : tu connais probablement déjà ces 5 vérités intellectuellement. Si on te les "
    "lit, tu hoches la tête. Mais en trade, à 14h30, +1500 sur la table, tu ne les actionnes pas. C'est "
    "exactement la marque du « savoir non incarné ».",
    "Ton travail : passer les 5 vérités du niveau intellectuel au niveau réflexe. Méthode : tu les écris à "
    "la main chaque matin. Tu les répètes à voix basse avant chaque session. Tu les colles au mur. À force "
    "de répétition consciente, elles s'installent dans le système 1 (réflexe) et ne sont plus dans le "
    "système 2 (réflexion). À ce moment-là, elles te protègent automatiquement."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu prends 4 pertes XAUUSD d'affilée. Tu te dis « mon setup ne marche plus, le marché a "
    "changé ». Tu changes ta méthode. Tu casses ta série.",
    "<b>Cible :</b> tu prends 4 pertes. Tu sens monter le doute. Tu te récites <b>V3</b> : « il y a une "
    "distribution aléatoire des gagnants et perdants à l'intérieur d'un edge valide. 4 pertes consécutives "
    "ne disent rien sur la validité de mon edge. » Tu continues ta série. Le 5e trade est gagnant. Le 6e aussi. "
    "La distribution se révèle."
]))
story.extend(exo([
    "<b>Récitation matinale.</b> Chaque matin, avant ouverture des marchés, tu lis à voix basse les 5 vérités. "
    "Pas en les lisant — en les <b>habitant</b>. Pause après chaque pour ressentir si elle est vraie pour toi.",
    "<b>Mémorisation.</b> En 30 jours, tu dois pouvoir réciter les 5 vérités de mémoire, dans l'ordre, sans "
    "regarder. Pas par discipline scolaire — parce que tu auras besoin de les actionner en situation de "
    "stress, où la lecture ne sera pas possible.",
    "<b>Application pré-trade.</b> Avant chaque trade, identifie laquelle des 5 vérités est la plus "
    "pertinente pour ce moment-là. Tu l'évoques. Tu cliques."
]))
story.extend(phrase("Les 5 vérités ne sont pas des slogans. Ce sont les axiomes de mon nouveau système d'exploitation."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(5, 4, "Les quatre peurs fondamentales",
    "Ce qui te pousse à saboter — peur par peur", ACCENT))
story.extend(idee(
    "Le trader perdant agit sous l'influence de quatre peurs fondamentales : peur de perdre, peur de "
    "rater, peur de se tromper, peur de laisser de l'argent sur la table. Chaque peur produit des "
    "comportements spécifiques. Le trader rentable les a identifiées et les a désactivées une par une — "
    "pas en les niant, en les digérant."
))
story.append(P("Les quatre peurs, leurs symptômes, leurs antidotes", h_subsection))
story.append(styled_table([
    [C("Peur", cell_gold), C("Symptôme typique", cell_gold), C("Antidote", cell_gold)],
    [C("Peur de perdre", cell_bold),
     C("Couper les gains tôt. Refuser de prendre certains setups valides. Hésitation à l'entrée."),
     C("Accepter le risque CORPORELLEMENT, pas mentalement. Méditation pré-trade.")],
    [C("Peur de rater (FOMO)", cell_bold),
     C("Entrer en retard. Prendre des setups B-grade. Sur-trader les killzones."),
     C("Pré-décision écrite : si pas de A+, pas de trade. Aucune exception.")],
    [C("Peur de se tromper", cell_bold),
     C("Décaler le SL. Refuser d'acter une perte. Doubler sur la perte."),
     C("V1 + V3 : se tromper est dans la distribution attendue. Pas honteux.")],
    [C("Peur de laisser de l'argent", cell_bold),
     C("Pousser au-delà du TP. Pattern +1500. Refus de couper en profit."),
     C("Pré-décider à PnL=0 ce que tu fais à TP. Plateforme fermée après ordre.")],
], [3.5*cm, 6.5*cm, 6*cm]))
story.append(Spacer(1, 8))
story.extend(lien([
    "Tes deux peurs dominantes sont probablement <b>peur de se tromper</b> (donc tu décales les SL) et "
    "<b>peur de laisser de l'argent sur la table</b> (donc tu pousses au-delà du TP — pattern +1500). "
    "Les deux travaillent en tandem : tu pousses parce que tu ne veux pas rater plus, et quand ça reverse, "
    "tu refuses parce que tu ne veux pas avoir eu tort.",
    "Ces deux peurs sont fondamentalement liées à ton lien identité-performance. Se tromper = identité "
    "menacée. Rater = identité non confirmée. Tant que ton identité dépend de chaque trade, ces peurs "
    "auront une force démesurée."
]))
story.extend(exemple([
    "<b>Saboteur (peur de laisser de l'argent) :</b> XAUUSD +800. TP à +1000. Tu te dis « si je coupe et que "
    "ça monte à +2000, je vais m'en vouloir ». Tu laisses courir. +1500. Reverse. Perte.",
    "<b>Cible (antidote) :</b> XAUUSD +800. TP à +1000. Tu te récites : « si ça continue à monter sans moi "
    "après mon TP, c'est dans la distribution. Je ne suis pas censé capturer chaque mouvement. Mon edge se "
    "joue sur 100 trades, pas sur l'optimisation de celui-ci. » Tu coupes au TP. Tu fermes la plateforme. "
    "Si plus tard tu vois que ça a monté à +3000, tu ne ressens AUCUN regret — c'était au-delà de ton plan."
]))
story.extend(exo([
    "<b>Diagnostic des 4 peurs.</b> Sur tes 10 derniers crashs/erreurs, identifie laquelle des 4 peurs était "
    "à l'œuvre. Probablement les peurs 3 et 4 dominent. C'est ta cible prioritaire.",
    "<b>Pré-décisions écrites.</b> Pour chaque peur, écris UNE phrase de pré-décision que tu te récites avant "
    "chaque trade. Exemple peur 4 : « Je coupe au TP. Si le marché monte sans moi, c'est OK. C'est dans le "
    "plan. »",
    "<b>Méditation d'acceptation du risque.</b> Avant chaque session, 3 min : tu visualises chaque trade "
    "potentiel comme une instance d'une distribution. Tu acceptes émotionnellement (pas mentalement) que "
    "celui-ci peut perdre. Sans cette acceptation corporelle, les peurs continueront à piloter."
]))
story.extend(phrase("Les 4 peurs ne sont pas miennes. Elles sont humaines. Je les nomme, je les désamorce."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(5, 5, "Les croyances limitantes",
    "Ce que tu crois inconsciemment sur l'argent et le risque", ACCENT))
story.extend(idee(
    "Tes comportements de trading ne sont pas pilotés par tes décisions conscientes. Ils sont pilotés "
    "par tes <b>croyances inconscientes</b> — sur l'argent, le mérite, le risque, la valeur, la sécurité. "
    "Ces croyances ont été installées dans l'enfance et l'adolescence. Tu ne les vois pas. Mais elles "
    "décident à ta place."
))
story.extend(mecan(
    "Une croyance fonctionne comme un filtre perceptuel. Si tu crois inconsciemment que « l'argent facile "
    "est suspect », chaque gain rapide active une dissonance silencieuse — tu vas inconsciemment chercher "
    "à le justifier (par de l'effort supplémentaire, donc trop de trades) ou à le détruire (par sabotage). "
    "Si tu crois que « je ne mérite pas de garder beaucoup d'argent », tout profit qui dépasse ton seuil de "
    "« mérite » sera mécaniquement repris."
))
story.extend(lien([
    "Tu portes probablement plusieurs croyances limitantes installées avant et après 2022. "
    "<b>« L'argent doit être mérité par l'effort visible »</b> — un edge qui paye 5 secondes de clic active "
    "alors une dissonance. <b>« Je dois prouver que mon cerveau marche encore »</b> — installée post-coma, "
    "elle fait du trade un test identitaire. <b>« Si je gagne trop, je le payerai ailleurs »</b> — loi du "
    "retour, garantit le crash après un pic. <b>« Je suis chanceux de m'en être sorti, je ne dois pas pousser "
    "ma chance »</b> — autre installation post-TBI, sabote le scaling.",
    "Tant que ces croyances opèrent en arrière-plan, tu peux apprendre tous les outils mentaux du monde — "
    "elles te ramèneront à leur logique. La transformation passe par <b>identifier</b> les croyances "
    "limitantes (les rendre conscientes) et <b>installer</b> des croyances de remplacement par expérience "
    "répétée."
]))
story.append(P("Le processus de transformation d'une croyance", h_subsection))
story.extend(ascii_schema("""
   1. IDENTIFICATION
      Quelle phrase silencieuse je porte sur l'argent / le mérite / le risque ?
      → Souvent installée 0-18 ans. Souvent héritée d'un parent.
      → Souvent reformulée post-trauma.

   2. NOMMER
      Écrire la phrase EXACTE à la main dans le journal.
      "Je crois que..."

   3. EXPLORER
      D'où vient cette croyance ? Quel événement / phrase / contexte ?

   4. CONTRE-PROPOSER
      Quelle phrase je CHOISIS de croire à la place ?
      → Pas un slogan magique. Une phrase plausible et utile.

   5. EXPÉRIENCE
      Comment je peux PROUVER à mon SN que la nouvelle phrase est vraie ?
      → Par expérience cumulative — pas par affirmation.

   6. RÉPÉTITION (3-6 mois)
      Chaque expérience qui confirme la nouvelle croyance affaiblit l'ancienne.
""", accent=ACCENT))
story.extend(exemple([
    "<b>Saboteur :</b> tu fais 5000€ de profit en deux jours XAUUSD. Le 3e jour tu te crashes -4500€. Tu te "
    "dis « j'ai été imprudent ». Faux diagnostic. La vraie cause : ta croyance « je ne mérite pas 5000€ "
    "facilement » a activé le sabotage automatique.",
    "<b>Cible :</b> tu fais 5000€. Tu reconnais immédiatement le seuil. Tu écris dans le journal : « je viens "
    "de dépasser ce que je croyais mériter. Ma croyance va activer un sabotage. Je le sais. Donc je ferme "
    "la plateforme pendant 48h. Je ne donne pas l'occasion au sabotage de s'exprimer. » Tu protèges "
    "physiquement le profit pendant que tu reconfigures la croyance."
]))
story.extend(exo([
    "<b>Inventaire des croyances.</b> Sur 2 pages dans ton journal, liste tout ce que tu as entendu sur "
    "l'argent dans ton enfance, ta famille, ton entourage. « Les gens riches sont... », « gagner de "
    "l'argent ça demande... », « si on a beaucoup d'argent on... ». Ne minimise pas. Tu vas découvrir "
    "10-15 phrases qui pilotent ton inconscient.",
    "<b>Contre-proposition.</b> Pour les 3 croyances qui te touchent le plus, écris une contre-phrase. "
    "Pas un slogan creux — une phrase plausible et utile. Tu n'effaces pas l'ancienne, tu plantes la "
    "nouvelle à côté.",
    "<b>Travail thérapeutique sur les croyances post-TBI.</b> Les croyances installées post-trauma sont "
    "plus difficiles à reconfigurer seul. Un thérapeute (cognitif-comportemental ou somatique) peut "
    "accélérer significativement ce travail."
]))
story.extend(phrase("Ce que je crois inconsciemment pilote mes choix. Je rends conscient ce qui pilote dans l'ombre."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(5, 6, "La zone",
    "L'état mental du trader qui exécute sans friction", ACCENT))
story.extend(idee(
    "La « zone » est l'état mental où tu exécutes ton plan sans friction interne. Pas de questionnement, "
    "pas de drame émotionnel, pas d'hésitation. Le trade est exécuté comme un chirurgien ferme une plaie : "
    "geste calme, précis, sans charge identitaire. Cet état n'est pas un don. C'est le résultat d'une "
    "préparation."
))
story.extend(mecan(
    "Trois composants assemblés produisent l'état de zone : <b>1) Confiance</b> dans la méthode (validée "
    "statistiquement par une série antérieure). <b>2) Discipline</b> (capacité réflexe à exécuter le plan "
    "même sous pression). <b>3) Perspective probabiliste</b> (chaque trade est une instance d'une série, "
    "pas un événement isolé). Quand les trois sont présents, la zone émerge naturellement. Quand l'un "
    "manque, l'état est instable."
))
story.extend(lien([
    "Tu n'as <b>jamais</b> été dans la zone, probablement. Tu as eu des sessions où tu te sentais en flow — "
    "mais c'était un flow émotionnel (l'euphorie d'une bonne séance), pas la zone (le calme exécutif). "
    "La différence est cruciale : le flow émotionnel est instable et se retourne en crash. La zone est "
    "stable et reproductible.",
    "Pour entrer dans la zone, tu dois d'abord avoir <b>une série de 100 trades exécutés selon ton protocole "
    "exact</b>. Sans cette série, la confiance manque. Tant que tu changes ta méthode tous les 5 trades, "
    "tu ne peux pas construire la confiance qui permet la zone. C'est un travail de plusieurs mois.",
    "Tu dois aussi avoir intégré les 5 vérités au niveau réflexe (Module 3), désamorcé les 4 peurs "
    "(Module 4), reconfiguré les croyances limitantes (Module 5). La zone n'est pas un état mental "
    "isolé — c'est l'aboutissement de tout le travail."
]))
story.append(P("Schéma — Les ingrédients de la zone", h_subsection))
story.extend(ascii_schema("""
                            LA ZONE
                              ★
                              │
              ┌───────────────┼───────────────┐
              │               │               │
        CONFIANCE        DISCIPLINE     PERSPECTIVE
        dans ma          d'exécution    PROBABILISTE
        méthode          réflexe        (5 vérités
              │               │         intégrées)
              │               │               │
         construite       construite      construite
         par 100         par répétition   par travail
         trades selon    consciente sur   conscient sur
         protocole       6-12 mois        12 mois
              │               │               │
              ▼               ▼               ▼
        Tu sais que ta    Tu n'as plus à  Le résultat
        méthode marche    te forcer       individuel
        sur 100 trades    à exécuter      ne te touche
                                          plus

   ─────────────────────────────────────────────────────────
   La zone n'est pas un cadeau. C'est le résultat d'un
   travail intégré sur tous les axes de cette bibliothèque.
""", accent=ACCENT))
story.extend(exemple([
    "<b>Saboteur (faux flow) :</b> tu enchaînes 5 trades gagnants. Tu te sens invincible. Tu augmentes la "
    "taille. Tu prends un B-grade. Tu cramés. C'était de l'euphorie déguisée en zone.",
    "<b>Cible (zone réelle) :</b> tu enchaînes 5 trades gagnants. Tu ne ressens rien de particulier. C'est "
    "ce que ta distribution prévoyait. Tu prends le 6e setup A+ avec exactement la même taille, la même "
    "rigueur, le même calme. Tu n'augmentes rien. Tu n'es ni euphorique ni anxieux. Tu exécutes."
]))
story.extend(exo([
    "<b>Le test de la zone.</b> Pendant une session, observe ton état corporel après chaque trade. Si tu "
    "ressens de l'euphorie, de l'excitation, du soulagement intense, de l'angoisse : tu n'es pas dans la "
    "zone. Tu es en émotion. La zone se sent comme... rien. Comme respirer. C'est le signe.",
    "<b>Le carnet de zone.</b> Chaque session, note 1-10 ton niveau de zone (1 = drame émotionnel, "
    "10 = neutralité chirurgicale). Sur 90 jours, tu vas voir l'évolution.",
    "<b>Construire la zone sur 6 mois.</b> Plan : 30 jours sevrage + 30 jours démo strict + 30 jours réel "
    "avec un seul compte + 90 jours d'application répétée. À la fin, la zone est accessible. Pas avant."
]))
story.extend(phrase("La zone n'est pas un état magique. C'est le résultat naturel d'un travail intégré."))
story.append(PageBreak())


# --- LIVRE 5 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 5", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Le trader rentable a fait la paix avec l'incertitude. Le perdant la combat encore.",
    "Plus d'analyse ne te donnera pas la certitude. Elle n'existe pas.",
    "Penser en probabilités est un mode mental à entraîner activement.",
    "Les 5 vérités doivent passer du niveau intellectuel au niveau réflexe.",
    "Les 4 peurs (perdre, rater, se tromper, laisser de l'argent) produisent les 5 patterns.",
    "Tes croyances inconscientes sur l'argent pilotent ton comportement.",
    "La zone n'est pas un état magique — c'est l'aboutissement d'un travail intégré.",
    "Confiance + Discipline + Perspective probabiliste = la zone.",
    "Une série de 100 trades exécutés selon protocole est le minimum pour construire la confiance.",
    "Le résultat individuel d'un trade ne dit rien sur la qualité de ton edge.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Chercher plus d'analyse comme antidote à l'anxiété.",
    "Penser en oui/non au lieu de probabilités.",
    "Changer de méthode après 3-5 trades perdants.",
    "Croire que les 5 vérités t'ont protégé parce que tu les connais.",
    "Nier tes croyances limitantes (« je n'en ai pas »).",
    "Confondre flow émotionnel et zone.",
    "Vouloir « être dans la zone » sans avoir fait le travail préalable.",
    "Pousser au-delà du TP par peur de laisser de l'argent.",
    "Décaler le SL par peur de se tromper.",
    "Sous-estimer le rôle des croyances installées avant 2022 ou par 2022.",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je joue 100 trades. Pas celui-ci.",
    "Avant chaque trade : « ce setup a X% selon ma série ».",
    "Je récite les 5 vérités chaque matin.",
    "Je connais mes 2 peurs dominantes et leurs antidotes pré-écrits.",
    "Je tiens un inventaire de mes croyances limitantes sur l'argent.",
    "Je ne change ma méthode qu'après 100 trades exécutés, jamais avant.",
    "Je distingue flow émotionnel et zone réelle.",
    "Je note mon niveau de zone (1-10) chaque session.",
    "Je n'ajoute aucun nouvel outil pendant 6 semaines minimum.",
    "Je construis la confiance par expérience, pas par affirmation.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║        TRADER DANS LA ZONE  —  FICHE D'ANCRAGE           ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Je joue une distribution, pas un trade.                 ║
   ║    Je pense en probabilités, pas en certitudes.            ║
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
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Reformuler en probabilité ("X% selon ma série")      ║
   ║    2. Réciter la vérité pertinente (V1 à V5)               ║
   ║    3. Identifier la peur active (P1-P4) et antidote        ║
   ║    4. Exécuter sans charge identitaire                     ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je joue 100. Celui-ci ne dit rien sur mon edge."       ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Imprimer les 5 vérités. Récitation matinale 30 jours.   ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Avant chaque trade : reformulation probabiliste.        ║
   ║    Journal probabiliste : "X% gagnants, RR Y:Z".           ║
   ║    Stricte intangibilité de la méthode pendant 100 trades. ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 5 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 6 — QUAND LE CORPS DIT NON (Gabor Maté)
# ============================================================
_current_book_color[0] = BOOK_COLORS[5]
ACCENT = BOOK_COLORS[5]

story.extend(book_separator_page(
    6, "Quand le corps dit non", "Gabor Maté", "When the Body Says No", 2003, ACCENT,
    quote='« Ce que nous refoulons par la volonté,<br/>le corps finit par l\'exprimer par la maladie. »',
    subtitle="Le coût caché du stress chronique et des émotions refoulées"
))

story.extend(book_intro_header(6, "Quand le corps dit non", "Gabor Maté — 2003", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "Gabor Maté est médecin canadien, spécialiste du stress, du trauma et de l'addiction. Ce livre établit "
    "une chose qui devrait bouleverser ta façon de te traiter : <b>les émotions refoulées finissent par "
    "s'exprimer dans le corps, sous forme de maladies, de douleurs chroniques, de dérèglements physiologiques</b>. "
    "Ce n'est pas une métaphore. C'est documenté cliniquement depuis des décennies."
))
story.append(P(
    "Pour toi, ce livre touche un point précis : ta tendance à <b>tout absorber</b>, à <b>tout porter</b>, "
    "à ne <b>jamais te plaindre</b>, à toujours « tenir bon ». Cette qualité — qui t'a sauvé après 2022, qui "
    "te permet de pousser ATHÉNA, qui te permet de continuer après chaque crash de compte — a un coût. Maté "
    "te montre lequel."
))
story.append(P(
    "Le livre identifie un profil caractéristique chez les personnes qui développent certaines maladies "
    "chroniques : un profil de gens « gentils », performants, exigeants envers eux-mêmes, peu enclins à dire "
    "non, qui absorbent tout. Ils ne sont pas faibles. Ils sont au contraire forts — mais cette force "
    "se retourne contre leur corps quand elle est dirigée contre leurs propres signaux internes."
))
story.append(P(
    "Lis-le pour comprendre que ton intensité, ton ambition, ta capacité à pousser ne sont pas des qualités "
    "sans contrepartie. Elles ont un prix corporel. À 25 ans tu ne le sens pas trop. À 35-45, si tu maintiens "
    "ce rythme sans intégration, tu vas le sentir."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Le corps tient un compte. Ce que la conscience refuse de dire, le corps finira par l\'exprimer en symptômes.</b>', pull_quote))
story.append(P(
    "Maté soutient — preuves cliniques à l'appui — que les maladies chroniques (cancers, maladies auto-immunes, "
    "SLA, sclérose en plaques, syndrome du côlon irritable, fibromyalgie) ont une corrélation forte avec "
    "des patterns émotionnels précis : suppression chronique de la colère, incapacité à dire non, "
    "hyper-responsabilité, identité construite sur l'utilité pour les autres, peur du conflit. Ces patterns "
    "produisent un stress chronique de bas niveau qui dérègle le système immunitaire et l'équilibre "
    "physiologique sur des années."
))
story.append(P("Les mécanismes exposés", h_subsection))
story.append(P(
    "<b>1. Le stress chronique de bas niveau</b> est plus toxique que le stress aigu intense. Il maintient "
    "le cortisol élevé en permanence, ce qui affaiblit l'immunité et accélère le vieillissement cellulaire. "
    "<b>2. La suppression émotionnelle</b> a un coût physiologique. Refouler la colère n'éteint pas la "
    "réaction physiologique de colère — elle continue, mais sans expression. <b>3. La personnalité « type C »</b> "
    "(par opposition au type A agressif et au type B détendu) : personnes apparemment calmes et coopératives "
    "qui suppriment massivement leur agressivité. Documentation clinique d'un lien statistique avec certains "
    "cancers. <b>4. Le mécanisme mère-enfant</b> : les patterns d'auto-suppression s'installent souvent dans "
    "l'enfance pour maintenir l'attachement parental. <b>5. L'identité construite sur l'utilité</b> : "
    "« j'existe par ce que je donne / réussis / produis » — épuisement programmé."
))
story.extend(lien([
    "Plusieurs aspects te concernent directement. <b>L'identité construite sur la performance</b> : tu trades "
    "pour <b>te prouver</b>, tu pousses ATHÉNA pour <b>construire</b>, tu sautes des obstacles pour <b>te dépasser</b>. "
    "Tu existes par ce que tu produis. Ce mode te coûtera physiologiquement à long terme.",
    "<b>La suppression possible de la colère</b> : depuis ton accident 2022, tu portes peut-être une colère "
    "ou une frustration que tu ne nommes pas — colère contre l'injustice de l'accident, frustration contre "
    "la lenteur de la reconstruction, ressentiment envers certaines personnes qui n'ont pas été à la hauteur. "
    "Si tu ne libères pas ces émotions explicitement, ton corps les portera.",
    "<b>L'hyper-responsabilité</b> : tendance à tout assumer, à ne pas demander d'aide, à porter seul. "
    "C'est aussi un facteur Maté."
]))
story.append(P("Les voies de réparation proposées", h_subsection))
story.append(P(
    "<b>Apprendre à dire non</b> : protection de tes ressources énergétiques. <b>Authenticité émotionnelle</b> : "
    "exprimer ce que tu ressens (colère, tristesse, lassitude) au lieu de le contenir. <b>Réorientation "
    "identitaire</b> : ton identité ne doit pas dépendre uniquement de ta production. <b>Travail thérapeutique</b> "
    "sur les patterns de suppression. <b>Repos non négocié</b> : récupération non comme une faiblesse mais "
    "comme une nécessité physiologique."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Maté a été critiqué pour parfois sur-attribuer les maladies à des facteurs psychologiques (corrélation "
    "vs causalité). À lire avec ce filtre — les mécanismes qu'il décrit sont solides, mais ne signifient pas "
    "que toute maladie chronique a une cause psychologique. Le livre est aussi très anecdotique (beaucoup "
    "de cas cliniques) ce qui peut alourdir la lecture. Va à l'essentiel."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Quand le corps dit non",
    [
        {"label": "THÈSE", "leaves": ["émotions refoulées", "expression somatique"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["stress chronique", "personnalité type C", "identité d'utilité"], "color": ACCENT},
        {"label": "RÉPARATION", "leaves": ["dire non", "authenticité émotion.", "repos non négocié"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Le coût somatique de la suppression émotionnelle et ses antidotes.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(6, 1, "Le stress chronique vs aigu",
    "Pourquoi le sourd dépasse l'intense", ACCENT))
story.extend(idee(
    "Le stress aigu intense (une menace ponctuelle, un événement choquant) est métabolisé par l'organisme. "
    "Le stress chronique de bas niveau (la pression sourde permanente) ne l'est pas. C'est lui qui dérègle "
    "l'immunité, accélère le vieillissement cellulaire, prépare les maladies chroniques. Le coût n'est pas "
    "dans l'intensité — il est dans la <b>durée</b>."
))
story.extend(mecan(
    "Physiologiquement : un stress aigu déclenche cortisol + adrénaline, puis retour à la normale. Cycle court, "
    "métabolisé. Un stress chronique maintient le cortisol élevé en permanence — inflammation systémique, "
    "résistance à l'insuline, suppression immunitaire, érosion des télomères (vieillissement cellulaire). "
    "Sur 5-10 ans, ce système cuit lentement. Tu ne le sens pas — jusqu'au jour où tu le sens."
))
story.extend(lien([
    "Toi tu portes plusieurs stress chroniques superposés. <b>Le trading</b> — pression financière, anxiété "
    "des comptes prop firm, peur du drawdown. <b>ATHÉNA</b> — construction d'entreprise, charge mentale. "
    "<b>Le post-TBI</b> — pression discrète de prouver, de récupérer. <b>Le saut d'obstacles compétitif</b> — "
    "pression de performance. Tu ne ressens probablement aucun de ces stress comme « écrasant ». Mais cumulés "
    "et permanents, ils maintiennent ton cortisol à un niveau élevé en continu.",
    "Indicateurs probables : sommeil qui n'est pas complètement réparateur (tu te lèves fatigué parfois sans "
    "raison), tensions chroniques (mâchoire, nuque, épaules), digestion irrégulière, libido fluctuante, "
    "humeur en yo-yo. Ce ne sont pas des problèmes graves. Ce sont des signaux que ton système est en "
    "régime de stress constant.",
    "Sans intervention, ce régime te coûtera dans 10-20 ans. Mais aussi <b>maintenant</b> — il alimente ton "
    "intolérance au calme, ta recherche d'intensité (tu compenses le stress par plus de stimulation, dans "
    "un cercle vicieux)."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu enchaînes 14 jours sans pause — trading le matin, ATHÉNA l'après-midi, équitation "
    "le soir, week-ends compétitions. Tu te sens « productif ». Tu te dis « je suis dans le flow ». "
    "Tu ne reconnais aucun symptôme. Mais ton cortisol est haut depuis 2 semaines, ton immunité est "
    "compromise, ta digestion ralentit, tu accumules du tissu inflammatoire silencieusement.",
    "<b>Cible :</b> tu reconnais le pattern. Tu instaures une <b>journée OFF complète par semaine</b> — "
    "pas de trade, pas d'ATHÉNA, pas d'écran professionnel. Tu fais une marche longue, tu lis, tu cuisines, "
    "tu dors. Tu donnes à ton système le temps de redescendre. Sur l'année, ça change ta physiologie."
]))
story.extend(exo([
    "<b>Audit du stress chronique.</b> Liste tes 5 principales sources de stress chronique de bas niveau. "
    "Note pour chacune si elle est négociable (tu peux la réduire) ou non. Tu vas voir qu'une partie au "
    "moins est négociable et que tu la maintiens par habitude.",
    "<b>Sabbat hebdomadaire.</b> Choisis un jour fixe par semaine où tu décroches complètement de tout "
    "ce qui est performance/production. Vraiment. C'est un investissement de santé.",
    "<b>Mesure de récupération.</b> Si tu as une montre connectée : observe ta variabilité cardiaque (HRV). "
    "C'est le meilleur indicateur de récupération autonome. Une HRV basse en continu = stress chronique. "
    "Sans montre : note ton sommeil 1-10 chaque matin sur 30 jours."
]))
story.extend(phrase("Le coût n'est pas dans l'intensité d'un événement. Il est dans la permanence d'un régime."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(6, 2, "La suppression émotionnelle",
    "Ce que tu ne dis pas, ton corps le porte", ACCENT))
story.extend(idee(
    "Quand une émotion est activée mais que son expression est bloquée, la réaction physiologique ne "
    "disparaît pas — elle se prolonge sous forme de tension corporelle, d'activation hormonale, "
    "d'inflammation. Sur le long terme, ce mécanisme contribue aux maladies chroniques. C'est documenté."
))
story.extend(mecan(
    "Une émotion est avant tout un état corporel (battements de cœur, tension musculaire, respiration). "
    "L'expression de l'émotion (parole, mouvement, larmes) <b>complète</b> le cycle physiologique et permet "
    "le retour au baseline. Sans expression, le corps reste en activation. Répétée des milliers de fois, "
    "cette activation non résolue devient un état chronique. C'est ce que Maté observe chez les patients "
    "atteints de maladies auto-immunes — un pattern fréquent de suppression émotionnelle de longue date."
))
story.extend(lien([
    "Pour toi en particulier, deux émotions sont probablement souvent supprimées. <b>La colère</b> : "
    "à propos de l'accident 2022, à propos des conséquences sur ton corps et ton temps, à propos de "
    "certains événements de ta jeunesse, à propos de tes propres limites. La colère est socialement mal vue "
    "donc beaucoup la suppriment systématiquement. <b>La lassitude</b> : tu pousses tellement que tu ne "
    "t'autorises pas à être fatigué. Tu refoules « j'en peux plus » sous le tapis de « il faut tenir ».",
    "Cette suppression a probablement été nécessaire dans la phase aigüe post-2022. Tenir, pousser, avancer. "
    "Mais ce qui était une stratégie de survie est devenu un automatisme. Trois ans après, tu continues à "
    "supprimer alors que tu pourrais commencer à exprimer. Le travail est de retrouver l'accès aux émotions "
    "qui sont là sans être dites."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu cramés un compte. Tu ressens de la colère contre toi-même, de la frustration, "
    "peut-être de la tristesse. Tu suppresses immédiatement (« il faut avancer », « je vais me refaire »). "
    "Tu repars travailler. L'émotion reste dans le corps. Le soir tu as mal au ventre. Tu ne fais pas le "
    "lien.",
    "<b>Cible :</b> tu cramés. Tu reconnais : « émotion en cours, à traiter ». Tu prends 15 min seul. "
    "Tu nommes : « je suis en colère contre moi-même. Je suis frustré. Je suis triste de revoir ce pattern. » "
    "Tu écris ces phrases. Tu pleures si ça vient. Tu marches 20 min en silence. Tu reviens. L'émotion a "
    "été traversée. Le corps ne la porte pas."
]))
story.append(P("Le protocole d'expression émotionnelle simple", h_subsection))
story.extend(ascii_schema("""
   1. RECONNAÎTRE
      "Là, là maintenant, je ressens quoi ?"
      Tu nommes : colère, tristesse, peur, frustration, honte, lassitude.

   2. AUTORISER
      Tu te dis intérieurement : "j'ai le droit de ressentir ça."
      Pas de jugement. Pas de "je devrais pas".

   3. LOCALISER
      Où dans le corps ? Quelle qualité ?

   4. EXPRIMER (au choix selon l'émotion et le contexte)
      - À voix haute, seul : "je suis en colère parce que..."
      - Par écrit : 3 pages sans censure
      - Par mouvement : marche rapide, sac de frappe, danse
      - À une personne de confiance : verbalisation orale
      - Par les larmes : si elles viennent, tu les laisses

   5. RETOUR AU CALME
      Une fois l'émotion exprimée, retour au baseline par
      respiration ou présence corporelle.
""", accent=ACCENT))
story.extend(exo([
    "<b>Le quart d'heure émotionnel quotidien.</b> Chaque soir, 15 min, seul, dans le silence : tu identifies "
    "et exprimes (à voix, par écriture, par mouvement) ce qui n'a pas été exprimé dans la journée. C'est "
    "préventif. Tu vides régulièrement.",
    "<b>L'inventaire des « tu aurais dû dire ».</b> Sur ton journal, liste les 10 dernières situations où tu "
    "aurais voulu dire quelque chose et tu ne l'as pas dit. Cette liste révèle ton pattern de suppression. "
    "Tu n'as pas besoin d'aller dire ces choses rétroactivement — la prise de conscience suffit déjà.",
    "<b>Travail de la colère 2022.</b> Une séance dédiée par mois minimum : tu écris une lettre à... ton accident, "
    "à ton corps, à ce qui s'est passé, à quelqu'un qui n'a pas été à la hauteur. Tu n'envoies pas. Tu "
    "exprimes ce qui n'a pas pu être exprimé à l'époque. C'est de la libération."
]))
story.extend(phrase("Ce que je ne dis pas, mon corps le portera. J'exprime régulièrement pour ne pas accumuler."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(6, 3, "La personnalité du « gentil performant »",
    "Reconnaître le pattern type C", ACCENT))
story.extend(idee(
    "Maté décrit un profil récurrent chez les patients développant certaines maladies chroniques : "
    "personnes apparemment calmes, coopératives, peu plaintives, qui suppriment leur agressivité et "
    "leurs besoins propres pour maintenir l'harmonie. Ce profil est socialement valorisé — il produit "
    "des « bonnes personnes » qui réussissent. Et qui paient le prix dans leur corps."
))
story.append(P("Le profil type C en détail", h_subsection))
story.append(styled_table([
    [C("Trait", cell_gold), C("Description", cell_gold), C("Coût caché", cell_gold)],
    [C("Difficulté à dire non", cell_bold),
     C("Tendance à accepter les demandes même quand on n'a plus de ressource."),
     C("Surcharge chronique. Stress permanent.")],
    [C("Hyper-responsabilité", cell_bold),
     C("Sentiment d'être responsable du bien-être des autres."),
     C("Épuisement par charge cognitive.")],
    [C("Suppression de la colère", cell_bold),
     C("La colère est jugée inacceptable, elle est donc inhibée."),
     C("Activation physiologique non résolue, chronique.")],
    [C("Identité d'utilité", cell_bold),
     C("« J'existe par ce que je donne / produis / réussis. »"),
     C("Anxiété quand on ne produit pas. Burn-out programmé.")],
    [C("Peur du conflit", cell_bold),
     C("Évitement de la confrontation directe."),
     C("Ressentiments cachés, communications biaisées.")],
    [C("Excellent self-control", cell_bold),
     C("Discipline visible, maîtrise de soi forte."),
     C("Inflexibilité, incapacité à lâcher.")],
], [4*cm, 6*cm, 6*cm]))
story.append(Spacer(1, 8))
story.extend(lien([
    "Plusieurs de ces traits te concernent. <b>Identité d'utilité</b> : tu te juges par ta production. "
    "<b>Excellent self-control</b> : ta capacité à pousser, à tenir, à reconstruire post-2022 montre une "
    "discipline rare — mais qui peut devenir une prison. <b>Hyper-responsabilité</b> : tu portes ATHÉNA "
    "seul, tu portes ton recovery seul, tu portes tes erreurs seul.",
    "Ce n'est pas que ces traits soient mauvais. Ils t'ont sauvé. Mais ils ont aussi un coût que tu vas "
    "commencer à sentir. La voie n'est pas de devenir l'inverse (un irresponsable lâche). La voie est de "
    "<b>moduler</b> — d'apprendre à parfois dire non, parfois demander de l'aide, parfois exprimer la "
    "colère, parfois ne pas être utile."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu reçois un message d'un ami qui veut ton aide pour son business. Tu es déjà "
    "surchargé. Tu réponds « oui pas de souci, je t'aide ce week-end ». Tu te dis « je m'arrangerai ». "
    "Tu ajoutes 4h de charge sur un week-end déjà tendu.",
    "<b>Cible :</b> tu reçois le message. Tu reconnais le réflexe « oui ». Tu attends 1 heure avant de "
    "répondre. Tu te demandes honnêtement : « est-ce que j'ai la ressource ? ». Si non, tu réponds : "
    "« Salut, je vois ta demande. Je suis pas dispo ce week-end. Si tu peux attendre 2 semaines, "
    "je serai content de t'aider. Sinon je comprends si tu trouves quelqu'un d'autre. » Tu protèges ta "
    "ressource."
]))
story.extend(exo([
    "<b>Audit type C.</b> Sur les 6 traits du tableau, note-toi 1-10. Tu vas identifier tes 2-3 traits "
    "les plus chargés. Ce sont tes cibles de transformation.",
    "<b>La liste des « non » à dire.</b> Pour la semaine à venir, identifie 3 situations où tu vas dire "
    "non. Pas dramatiquement — proprement. C'est de l'entraînement.",
    "<b>Demande d'aide explicite.</b> Identifie une chose pour laquelle tu pourrais demander de l'aide cette "
    "semaine et que tu fais habituellement seul. Demande. Observe ce que ça active en toi."
]))
story.extend(phrase("Mes qualités m'ont sauvé. Si je ne les module pas, elles me coûteront. Je commence à dire non."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(6, 4, "L'identité construite sur l'utilité",
    "Quand tu existes par ce que tu produis", ACCENT))
story.extend(idee(
    "Beaucoup de personnes construisent leur identité sur leur utilité — pour autrui, pour leur famille, "
    "pour la société, pour leur propre estime. C'est une identité fragile : elle dépend de la production "
    "continue. Le jour où tu ne produis pas (maladie, fatigue, choix), tu ne sais plus qui tu es. "
    "Cette fragilité génère une anxiété de fond permanente."
))
story.extend(mecan(
    "L'identité d'utilité est typiquement installée dans l'enfance : l'enfant comprend qu'il est aimé/valorisé "
    "quand il produit (bonnes notes, bons comportements, succès visibles). Il intériorise : « je vaux par ce "
    "que je donne ». Adulte, il ne sait plus se reposer sans culpabilité, ne sait plus s'aimer sans accomplir, "
    "vit dans une anxiété permanente de ne pas être « assez ». La performance devient une thérapie qui ne "
    "soigne jamais — chaque succès est suivi du besoin du suivant."
))
story.extend(lien([
    "Toi tu as installé en plus, après 2022, une couche supplémentaire : « je dois prouver que mon cerveau "
    "marche, que mon corps marche, que je suis capable, que ce qui m'est arrivé ne m'a pas réduit. » Cette "
    "preuve permanente que tu te dois te pousse à la performance constante. Trading, ATHÉNA, équitation, box "
    "— autant de terrains de preuve.",
    "Le problème : tu n'arriveras jamais à « la » preuve qui te libère. Parce que la preuve dont tu as besoin "
    "n'est pas dans la performance — elle est dans l'<b>acceptation profonde</b> que tu vaux indépendamment "
    "de ce que tu produis. Cette acceptation ne se construit pas en gagnant plus. Elle se construit en "
    "<b>te valorisant en l'absence de production</b>.",
    "Concrètement : il faut que tu trouves des moments réguliers où tu existes sans produire — et que tu "
    "te sentes <b>OK</b> dans ces moments. Si tu te sens en culpabilité, en agitation, en vide — c'est "
    "le diagnostic que ton identité dépend encore de la production. Le repos devient alors un exercice "
    "identitaire."
]))
story.extend(exemple([
    "<b>Saboteur :</b> dimanche après-midi, rien à faire. Pas de marchés. ATHÉNA en pause. Pas de séance "
    "équestre. Tu ressens un vide, une agitation, une vague culpabilité. Tu ouvres ton ordinateur, tu commences "
    "à analyser des charts, tu regardes des vidéos « pour avancer ». Tu ne te reposes pas — tu compenses le "
    "vide identitaire par de la pseudo-production.",
    "<b>Cible :</b> dimanche après-midi, rien à faire. Tu ressens le vide. Tu nommes : « identité d'utilité "
    "qui s'angoisse — c'est normal, je laisse passer ». Tu prends un bon livre. Tu fais une longue marche "
    "sans téléphone. Tu cuisines lentement. Tu existes sans produire. Au début c'est inconfortable. À "
    "force, ça devient possible. Puis agréable. Puis nécessaire."
]))
story.extend(exo([
    "<b>L'audit identitaire.</b> Réponds par écrit : « si je ne produisais rien pendant un mois (pas de "
    "trading, pas d'ATHÉNA, pas de compétition, juste de l'existence), qui serais-je ? » La difficulté de "
    "cette réponse mesure ton degré d'identité d'utilité.",
    "<b>L'heure d'inutilité.</b> Chaque jour, 1 heure de présence sans production. Marche, lecture, présence "
    "à la nature, contemplation, conversation gratuite. C'est ton entraînement.",
    "<b>La liste des « je suis » non-performance.</b> Identifie 10 attributs de toi qui n'ont rien à voir "
    "avec la performance. Pas « je suis trader », « je suis cavalier » — plutôt « je suis curieux », "
    "« je suis sensible aux animaux », « je suis loyal ». Cette liste te rappelle qui tu es sans production."
]))
story.extend(phrase("Je ne vaux pas par ce que je produis. Je vaux. Point. La production vient ensuite."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(6, 5, "Apprendre à dire non",
    "La compétence qui protège tes ressources", ACCENT))
story.extend(idee(
    "Dire non n'est pas une mauvaise éducation, ni un manque de générosité. C'est une compétence de "
    "<b>protection des ressources</b>. Tes ressources énergétiques sont finies. Chaque oui consomme. "
    "Si tu dis oui à tout, tu finis sans rien pour ce qui compte vraiment. La capacité à dire non est "
    "indispensable à toute vie soutenable."
))
story.extend(mecan(
    "Le réflexe de dire oui est souvent installé en enfance : l'enfant comprend que dire non = retrait de "
    "l'amour parental. Il intériorise que pour rester en lien, il faut accommoder. Adulte, ce réflexe est "
    "automatique — il dit oui avant même d'évaluer s'il a la ressource. Le coût n'est pas immédiat — mais il "
    "s'accumule. Surchage, ressentiment, épuisement progressif."
))
story.extend(lien([
    "Pour toi qui es probablement habitué à dire oui, le « non » est un muscle atrophié. Pas par lâcheté — "
    "par habitude. Et avec ta charge actuelle (trading, ATHÉNA, équitation, post-recovery), apprendre à "
    "dire non est presque vital pour ta santé physique.",
    "Le « non » à pratiquer touche plusieurs domaines : <b>1)</b> sociale (demandes d'amis, invitations, "
    "obligations familiales). <b>2)</b> professionnelle (engagements ATHÉNA qui dépassent ta capacité). "
    "<b>3)</b> envers toi-même (le « non » à un trade B-grade, le « non » à une journée de plus sans repos, "
    "le « non » à un nouveau projet). Cette dernière catégorie est la plus difficile."
]))
story.append(P("Les 4 niveaux du non", h_subsection))
story.append(styled_table([
    [C("Niveau", cell_gold), C("Formulation type", cell_gold), C("Quand l'utiliser", cell_gold)],
    [C("1 — Non poli avec contexte", cell_bold),
     C("« Merci de penser à moi. Je ne peux pas cette fois — je suis chargé. »"),
     C("Refus standard. Pas besoin de justifier en détail.")],
    [C("2 — Non avec proposition", cell_bold),
     C("« Pas maintenant, mais je peux dans X semaines si tu veux. »"),
     C("Quand tu veux maintenir le lien mais protéger la ressource.")],
    [C("3 — Non ferme", cell_bold),
     C("« Non, ce ne sera pas possible. »"),
     C("Quand la situation ne tolère pas d'aménagement. Pas d'explication.")],
    [C("4 — Non avec limite explicite", cell_bold),
     C("« Je ne peux plus accepter ce type de demande. »"),
     C("Quand un pattern de sollicitations devient problématique.")],
], [4*cm, 7*cm, 5*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu reçois une invitation à un mariage le week-end où tu as 3 chevaux à entraîner pour "
    "une compétition importante. Tu dis « oui je viens ». Tu te dis « je trouverai bien ». Tu arrives à la "
    "compétition non préparé, fatigué, frustré.",
    "<b>Cible :</b> tu reçois l'invitation. Tu reconnais le réflexe « oui ». Tu attends 24h. Tu réponds : "
    "« Je suis touché de l'invitation. Malheureusement j'ai une compétition équestre importante ce week-end "
    "que je ne peux pas décaler. Je serai avec vous en pensée. On fait quelque chose à mon retour ? » Tu "
    "protèges ta ressource sans casser la relation."
]))
story.extend(exo([
    "<b>Les 5 non de la semaine.</b> Cette semaine, identifie 5 occasions de dire non. Petits ou grands. "
    "Dis-les. Observe ce qui se passe en toi (culpabilité ? soulagement ?). Observe ce qui se passe avec "
    "l'autre (souvent rien — la peur est plus grande que la conséquence réelle).",
    "<b>Le délai de 24h.</b> Pour toute demande qui peut attendre, instaure une règle : tu ne réponds "
    "jamais immédiatement. Tu prends 24h pour évaluer si tu as la ressource. La majorité de tes oui "
    "regrettés sont des oui immédiats.",
    "<b>Le non à toi-même.</b> 1 fois par jour, dis non à toi-même sur quelque chose que tu fais par habitude "
    "et qui te coûte (un trade B-grade, une session d'écran prolongée, une suralimentation). Le non à toi-même "
    "est le plus exigeant et le plus libérateur."
]))
story.extend(phrase("Dire non n'est pas un refus de l'autre. C'est un oui à ce qui compte vraiment pour moi."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(6, 6, "Le repos comme nécessité physiologique",
    "Pas comme faiblesse — comme physiologie", ACCENT))
story.extend(idee(
    "Le repos n'est pas l'inverse de la productivité. C'est sa <b>condition</b>. Un système qui ne récupère "
    "pas se dégrade — c'est la même loi pour un muscle, un système immunitaire, un cerveau. Tant que tu vis "
    "le repos comme une faiblesse à combattre, ton corps paye un prix qui finira par devenir visible. Le "
    "repos est une compétence à entraîner, pas un cadeau qu'on s'accorde."
))
story.extend(mecan(
    "Le système nerveux humain fonctionne par <b>cycles d'activation-récupération</b> (rythmes ultradiens "
    "de ~90 min, cycle circadien de 24h, cycle hebdomadaire, cycle saisonnier). Chaque cycle a une phase "
    "d'activation et une phase de récupération. Si tu force l'activation permanente, tu compromis la "
    "récupération. Sur le long terme : dégradation immunitaire, déclin cognitif, fragilité émotionnelle, "
    "vieillissement cellulaire accéléré. C'est mécanique, pas moral."
))
story.extend(lien([
    "Tu vis probablement en sur-activation chronique. Sommeil pas toujours réparateur, peu de pauses dans "
    "la journée, semaines remplies, sport intense plus que repos. Tu compenses la fatigue par la stimulation "
    "(café, intensité, écrans). Cycle classique : plus tu es fatigué, plus tu stimules pour ne pas le "
    "ressentir, plus tu dégrades ton baseline.",
    "Pour ton cas post-TBI, c'est particulièrement coûteux. Les traumas crâniens demandent plus de récupération "
    "que la moyenne — ton cerveau a besoin de sommeil de qualité pour ses processus de réparation continus. "
    "Si tu dors mal ou peu, tu compromis directement ta reconstruction neurologique."
]))
story.append(P("Les 4 cycles de récupération à respecter", h_subsection))
story.append(styled_table([
    [C("Cycle", cell_gold), C("Durée", cell_gold), C("Récupération", cell_gold)],
    [C("Ultradien", cell_bold), C("~90 min"),
     C("Toutes les 90 min : pause de 5-15 min. Pas d'écran. Marche, eau, respiration.")],
    [C("Circadien", cell_bold), C("24h"),
     C("Sommeil 7-9h. Couché avant 23h. Routine de coucher stable. Pas de café après 14h.")],
    [C("Hebdomadaire", cell_bold), C("7 jours"),
     C("1 jour OFF complet. Pas de production. Pas d'écran de travail. Repos réel.")],
    [C("Saisonnier", cell_bold), C("3 mois"),
     C("Une vraie pause longue par saison : 5-10 jours sans aucune obligation pro.")],
], [3*cm, 2.5*cm, 10.5*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu trades 4h le matin, ATHÉNA 4h l'après-midi, équitation 2h le soir, vidéos "
    "trading avant de dormir. Aucune pause structurée dans la journée. Tu dors 6h. Tu te lèves avec un "
    "café. Tu recommences. Sur 3 mois : épuisement masqué par la dopamine quotidienne.",
    "<b>Cible :</b> tu structures la journée avec micro-pauses (5 min toutes les 90 min). Tu coupes les "
    "écrans 1h avant de dormir. Tu dors 8h. Tu respectes 1 jour OFF par semaine. Tu prends 5 jours OFF "
    "tous les 3 mois. Sur 3 mois : ton énergie est plus stable, ta capacité décisionnelle s'améliore "
    "visiblement, ton trading aussi."
]))
story.extend(exo([
    "<b>Audit de récupération.</b> Sur les 4 cycles, note 1-10 ton respect actuel. Tu vas voir lequel "
    "est le plus négligé. C'est ta cible prioritaire pour 30 jours.",
    "<b>Implémentation du jour OFF.</b> Choisis un jour fixe par semaine. Bloque-le dans ton calendrier. "
    "Aucune obligation pro ce jour. Aucun écran de travail. Marche, lecture, présence, cuisine, social "
    "gratuit. Non négociable.",
    "<b>Routine de coucher.</b> Définis une séquence de 30-60 min avant le sommeil : pas d'écran, lumière "
    "basse, lecture ou méditation, respiration. À force, cette séquence devient un déclencheur biologique "
    "de sommeil."
]))
story.extend(phrase("Le repos n'est pas le contraire du travail. C'est sa condition. Je récupère pour pouvoir agir."))
story.append(PageBreak())


# --- LIVRE 6 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 6", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Les émotions refoulées finissent par s'exprimer dans le corps.",
    "Le stress chronique de bas niveau est plus toxique que le stress aigu.",
    "La suppression de la colère a un coût physiologique mesurable.",
    "Le profil type C (gentil performant qui supprime) est lié à plusieurs maladies chroniques.",
    "L'identité construite sur l'utilité produit une anxiété permanente.",
    "Le repos n'est pas l'inverse de la productivité — c'est sa condition.",
    "Dire non est une compétence de protection des ressources.",
    "Apprendre à exprimer la colère est protection somatique.",
    "Tes qualités te sauvent à court terme et te coûtent à long terme si non modulées.",
    "Le corps tient un compte. Il finira par présenter l'addition.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Croire que tu peux supprimer tes émotions sans coût.",
    "Te valoriser uniquement par ta production.",
    "Dire oui automatiquement, sans évaluer la ressource.",
    "Vivre le repos comme une faiblesse à combattre.",
    "Compenser la fatigue par plus de stimulation.",
    "Tout porter seul, ne pas demander d'aide.",
    "Éviter le conflit pour préserver l'harmonie de surface.",
    "Confondre intensité chronique et vie réussie.",
    "Ignorer les signaux corporels (tensions, digestion, sommeil).",
    "Penser que la colère est une mauvaise émotion à inhiber.",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "J'exprime mes émotions régulièrement (quart d'heure quotidien).",
    "Je dis 5 non par semaine minimum.",
    "Je délai de 24h pour toute demande qui peut attendre.",
    "Je prends 1 jour OFF complet par semaine, non négociable.",
    "Je dors 7-9h par nuit, couché avant 23h.",
    "Je respecte les micro-pauses toutes les 90 minutes.",
    "Je demande de l'aide 1 fois par semaine sur quelque chose.",
    "Je cultive une identité non-performance.",
    "Je nomme et exprime ma colère quand elle vient.",
    "Je consulte annuellement un médecin pour un bilan physique.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║       QUAND LE CORPS DIT NON  —  FICHE D'ANCRAGE         ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Mon corps tient un compte. J'exprime régulièrement      ║
   ║    pour ne pas accumuler.                                  ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Supprimer émotions + identité d'utilité + sur-activation║
   ║    chronique = dégradation programmée à 35-45 ans.         ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE                                           ║
   ║    - Dire oui automatiquement à tout                       ║
   ║    - Sentir une fatigue qu'on masque par stimulation       ║
   ║    - Repos qui génère culpabilité                          ║
   ║    - Tensions chroniques (nuque, mâchoire, ventre)         ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Délai 24h avant toute réponse à demande              ║
   ║    2. Audit ressource avant d'accepter                     ║
   ║    3. Si non, dire non sans culpabilité                    ║
   ║    4. 15 min d'expression émotionnelle quotidienne         ║
   ║    5. 1 jour OFF/sem + 5 jours OFF/trimestre               ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je vaux. Indépendamment de ce que je produis."         ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Cette semaine : 5 non + 1 jour OFF complet.             ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Dire non aux trades B-grade systématiquement.           ║
   ║    Aucun trade le jour OFF hebdo.                          ║
   ║    Pause obligatoire après chaque journée intense.         ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 6 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 7 — UN RIEN PEUT TOUT CHANGER (James Clear)
# ============================================================
_current_book_color[0] = BOOK_COLORS[6]
ACCENT = BOOK_COLORS[6]

story.extend(book_separator_page(
    7, "Un rien peut tout changer", "James Clear", "Atomic Habits", 2018, ACCENT,
    quote='« Tu ne montes pas au niveau de tes objectifs.<br/>Tu redescends au niveau de tes systèmes. »',
    subtitle="L'architecture des petites habitudes"
))

story.extend(book_intro_header(7, "Un rien peut tout changer", "James Clear — 2018", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "James Clear synthétise dans ce livre vingt ans de recherche sur la psychologie de l'habitude. C'est "
    "probablement le livre le plus <b>opérationnel</b> de toute cette bibliothèque pour ce qui concerne "
    "le passage de l'insight à la pratique quotidienne. Tous les concepts précédents (Hougaard, Lembke, "
    "van der Kolk, Levine, Douglas, Maté) doivent être transformés en habitudes pour avoir un effet. "
    "Sans architecture d'habitude, ils restent de la connaissance intellectuelle."
))
story.append(P(
    "Tu as un problème spécifique en lien avec ce livre : tu opères en <b>cycles de motivation</b> plutôt qu'en "
    "systèmes d'habitude. Tu te dis « cette semaine je vais m'y mettre vraiment », tu fais 5 jours intensément, "
    "puis tu retombes. Tu confonds intensité ponctuelle et changement durable. Clear t'apprend que la "
    "transformation se joue dans l'inverse : <b>petits gestes consistants sur la durée</b> battent toujours "
    "grands gestes ponctuels."
))
story.append(P(
    "Pour ton cas, ce livre est l'outil de conversion. Tout ce que tu auras compris dans les 6 livres "
    "précédents devra être traduit ici en : routines quotidiennes, déclencheurs, environnements modifiés, "
    "récompenses immédiates. C'est ce qui transforme l'insight en transformation."
))
story.append(P(
    "Lis-le après avoir intégré les concepts somatiques (Levine) et mentaux (Douglas). Sans ces fondations, "
    "tu vas essayer d'installer des habitudes par volonté pure — ce qui ne marche pas longtemps. Avec "
    "les fondations, les habitudes s'enracinent."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Tu ne te transformes pas par des objectifs. Tu te transformes par des systèmes répétés des centaines de fois.</b>', pull_quote))
story.append(P(
    "Clear inverse le rapport habituel objectif/processus. La culture populaire valorise les objectifs "
    "ambitieux. Clear démontre que les objectifs sont en réalité <b>secondaires</b>. Ce qui compte, c'est "
    "le système d'habitude qui t'amène à les atteindre — et qui te maintient au-delà. Tu n'atteins pas un "
    "poids cible : tu deviens une personne qui mange et bouge de telle façon. Tu n'atteins pas un PnL cible : "
    "tu deviens un trader qui exécute de telle façon. L'identité précède le résultat."
))
story.append(P("Les mécanismes exposés", h_subsection))
story.append(P(
    "<b>1. L'agrégation de gains marginaux</b> : 1% d'amélioration par jour produit 37 fois mieux en un an "
    "(par effet composé). Inversement, 1% de dégradation produit l'effondrement. Les petits gestes comptent "
    "énormément à long terme. <b>2. Le plateau du potentiel latent</b> : le changement n'est pas linéaire. "
    "Tu pratiques pendant des mois sans résultats visibles, puis tout bascule. La majorité abandonne avant "
    "le bascule. <b>3. La hiérarchie en 3 couches</b> : résultats → processus → identité. Pour des changements "
    "durables, il faut viser l'identité, pas les résultats. <b>4. La boucle d'habitude</b> : signal → désir → "
    "réponse → récompense. Toute habitude se construit sur ces 4 éléments. Tu peux les modifier "
    "consciemment. <b>5. La règle des 2 minutes</b> : pour installer une habitude, commencer par une version "
    "qui prend moins de 2 minutes. La consistance compte plus que l'intensité au début."
))
story.append(P("Les transformations proposées", h_subsection))
story.append(P(
    "<b>Viser l'identité, pas le résultat</b> : « je deviens un trader chirurgical » plutôt que « je veux gagner "
    "10 000€ ». <b>Manipuler l'environnement</b> : rendre les bonnes habitudes faciles et les mauvaises difficiles. "
    "<b>Empiler les habitudes</b> : ajouter une nouvelle habitude juste après une existante (« après mon café, "
    "je médite 5 min »). <b>Suivre le progrès visuellement</b> : grille de cochages, calendrier visible. "
    "<b>Ne jamais manquer deux fois de suite</b> : un raté est normal, deux de suite est le début de "
    "l'arrêt."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Le livre est très anglo-saxon, parfois excessivement positif (« tout le monde peut transformer sa vie "
    "avec des petites habitudes »). Cette posture sous-estime les obstacles structurels — pour quelqu'un "
    "avec un trauma comme ton TBI, certaines habitudes demandent plus que de la mécanique : elles demandent "
    "un travail somatique préalable. Si tu prends Clear comme manuel exclusif sans avoir traité ton SN, "
    "tu vas reproduire des échecs. Avec les autres livres comme fondations, Clear devient extrêmement "
    "puissant."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Un rien peut tout changer",
    [
        {"label": "THÈSE", "leaves": ["systèmes > objectifs", "identité > résultat"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["agrégation 1%", "plateau latent", "boucle d'habitude"], "color": ACCENT},
        {"label": "MÉTHODE", "leaves": ["empilement", "règle 2 min", "environnement modifié"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("L'architecture des habitudes — du résultat à l'identité.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(7, 1, "L'agrégation des gains marginaux",
    "Pourquoi 1% par jour change tout", ACCENT))
story.extend(idee(
    "Une amélioration de 1% par jour produit, par effet composé, environ 37 fois mieux au bout d'un an. "
    "Une dégradation de 1% par jour produit l'inverse — proche de zéro. La différence entre une "
    "trajectoire ascendante et descendante se joue dans des écarts quotidiens qui semblent négligeables "
    "isolés. C'est l'<b>arithmétique du temps long</b>."
))
story.extend(mecan(
    "Tu sous-estimes radicalement ce qu'un geste répété peut produire sur 1 an, 5 ans, 10 ans. C'est un biais "
    "cognitif documenté — les humains pensent linéairement et la composition est exponentielle. Quand tu vois "
    "« 1% par jour », tu te dis « c'est rien ». Mathématiquement : 1.01^365 = 37.8. Sur 5 ans : 1.01^1825 ≈ "
    "98 milliards de fois mieux (théoriquement). La réalité matérielle limite, mais l'effet reste massif."
))
story.extend(lien([
    "Toi tu vis l'inverse de cette logique. Tu cherches le coup ponctuel qui change tout — le compte funded "
    "qui débloque, la session +5000 qui transforme. Tu mises sur l'amplitude instantanée plutôt que sur la "
    "consistance fine. C'est pour ça que tu peux faire 2 ans de trading sans avoir progressé "
    "significativement : tu n'as pas accumulé de 1% par jour.",
    "Pour toi en pratique, l'agrégation des gains marginaux signifie : <b>1% de meilleure exécution par jour</b>. "
    "Pas une session miracle. Un protocole un peu mieux respecté. Une décision marginalement plus calme. "
    "Un journal rempli un jour de plus. À l'échelle de 6-12 mois, ces 1% s'accumulent en transformation "
    "radicale. Tu deviens littéralement quelqu'un d'autre."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu te dis « ce mois je vais doubler mon win rate par une nouvelle approche révolutionnaire ». "
    "Tu changes ta méthode complètement. 3 semaines plus tard, tu reviens à la précédente. Tu n'as pas "
    "accumulé.",
    "<b>Cible :</b> tu te dis « ce mois je vais simplement améliorer 1% mon exécution. Cette semaine je travaille "
    "le respect du SL. La semaine prochaine je travaille la qualité de mes pré-décisions. Et ainsi de suite. » "
    "Sur 12 mois, tu as travaillé 50 micro-aspects. Tu n'es plus la même opératrice."
]))
story.append(P("Schéma — La trajectoire des 1%", h_subsection))
story.extend(ascii_schema("""
   1% MIEUX PAR JOUR vs 1% MOINS BIEN PAR JOUR — 365 jours

   1% MIEUX
                                                              ▄▆█
                                                          ▁▃▅
                                                    ▁▂▄
                                            ▁▂▃
                                    ▁▂
                              ▁▂
                       ▁▁
                  ▁▁
            ▁▁
   ─▁▁▁▁▁▁
        Mois 0          3              6              9             12

   1% MOINS BIEN
   █▇▆▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
        Mois 0          3              6              9             12

   → Les deux trajectoires partent du même point.
   → À 6 mois, elles ne sont presque pas comparables.
   → À 12 mois, c'est une différence d'identité.
""", accent=ACCENT))
story.extend(exo([
    "<b>Le carnet des 1%.</b> Chaque soir, écris une ligne : « aujourd'hui qu'est-ce que j'ai fait à 1% mieux ? » "
    "Tu cherches une chose, même minuscule. Cette pratique installe le mindset des micro-gains.",
    "<b>L'audit du temps long.</b> Réponds par écrit : « si je faisais 1% mieux par jour pendant 12 mois "
    "sur le respect de mon SL, où je serais ? » Visualise concrètement. Cette projection change ta "
    "relation au présent.",
    "<b>Sortie des cycles motivation.</b> Identifie ton dernier cycle « cette semaine je vais m'y mettre "
    "vraiment » qui a échoué. Pourquoi ? Probablement parce que tu as visé trop haut. Refais avec 1% — "
    "et observe la différence sur 30 jours."
]))
story.extend(phrase("Je ne mise pas sur le coup miracle. Je mise sur 1% par jour pendant 365 jours."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(7, 2, "Le plateau du potentiel latent",
    "Pourquoi tu vois aucun progrès — jusqu'au jour où tout bascule", ACCENT))
story.extend(idee(
    "Le changement n'est presque jamais linéaire. Tu pratiques pendant des semaines, des mois, et tu ne "
    "vois aucun résultat visible. C'est la phase du plateau. La majorité abandonne ici. Ceux qui tiennent "
    "voient soudain un basculement, parfois spectaculaire, quand le système atteint un seuil critique. "
    "Comprendre cette dynamique te permet de ne pas abandonner avant le basculement."
))
story.extend(mecan(
    "Métaphore classique : un glaçon dans une pièce à -10°. Tu chauffes la pièce. À -8°, rien. À -6°, rien. "
    "À -4°, rien. À -2°, rien. À 0°, le glaçon fond brutalement. Tous les degrés précédents étaient "
    "nécessaires — mais invisibles. Le changement humain fonctionne pareil. Le travail accumulé est réel "
    "mais sous le seuil de visibilité, jusqu'au moment où il dépasse le seuil et devient brusquement visible."
))
story.extend(lien([
    "Toi tu as probablement un long historique de plateaux abandonnés. Tu commences une discipline (méditation, "
    "sport régulier, journal trading). Au bout de 3-4 semaines tu ne vois aucun résultat évident. Tu arrêtes. "
    "Tu repars sur autre chose. Tu refais ça 5 fois en 2 ans. Conclusion : tu n'as <b>jamais</b> dépassé "
    "le plateau d'aucune discipline. Tu as accumulé des départs sans aucun basculement.",
    "Pour toi, l'apprentissage clé est : <b>la disparition du résultat visible ne signifie pas la disparition "
    "du progrès</b>. Le progrès se fait sous la surface. Si tu maintiens le système, le basculement viendra. "
    "Si tu arrêtes au plateau, tu n'auras jamais le basculement. C'est pour ça que la majorité des gens "
    "n'atteignent jamais leurs transformations promises.",
    "Pour ton trading, le plateau dure souvent 6-12 mois. Tu maintiens ton protocole, tu travailles ton "
    "exécution, tu remplis ton journal — et le PnL n'évolue pas spectaculairement. Si tu tiens, à un moment "
    "(souvent inattendu), tout bascule : tu réalises que tu exécutes proprement depuis 3 semaines, que ton "
    "drawdown est sous contrôle, que ton win rate s'est stabilisé. Le basculement a eu lieu — mais il était "
    "préparé par des mois de plateau invisible."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu commences un journal manuscrit. Tu tiens 3 semaines. Tu ne vois rien changer dans ton "
    "trading. Tu te dis « ça ne sert à rien ». Tu arrêtes. Tu n'as jamais atteint le moment où l'observation "
    "écrite commence à modifier le comportement (typiquement vers la 6e-8e semaine).",
    "<b>Cible :</b> tu commences le journal. Tu décides à l'avance que tu le tiens 12 semaines, peu importe "
    "le résultat visible. Tu enregistres comme une condition non négociable. À la 7e semaine, sans que tu le "
    "réalises explicitement, tu commences à hésiter avant un décalage de SL — parce que ton observation "
    "écrite cumulée a réorganisé ton rapport au geste. Le basculement a eu lieu silencieusement."
]))
story.append(P("Schéma — La courbe du plateau", h_subsection))
story.extend(ascii_schema("""
   Ce que tu ATTENDS (progression linéaire)
                                                ▄▆█
                                            ▂▄▅
                                        ▁▂
                                  ▁▁
                            ▁▁
                       ▁▁
                  ▁▁
            ▁▁
   ─▁▁▁▁
   J1            J90       J180       J270       J365

   Ce qui SE PASSE en réalité (plateau + basculement)
                                                ▄▆█
                                            ▂▄
                                        ▁▂  ★ ← basculement
   ─▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▂   (préparé pendant
   J1            J90       J180       J270       le plateau)

   → Si tu arrêtes pendant le plateau, tu rates le basculement.
   → Le travail invisible est le travail réel.
""", accent=ACCENT))
story.extend(exo([
    "<b>L'engagement temporel.</b> Pour chaque nouvelle habitude/discipline, décide à l'avance la durée "
    "minimale avant de pouvoir juger. Recommandation : 90 jours minimum pour toute habitude psychologique. "
    "12 semaines pour le journal. 6 semaines pour la respiration quotidienne. Tu n'évalues pas avant.",
    "<b>L'observation des micro-signaux.</b> Pendant le plateau, ne cherche pas les gros résultats. Cherche "
    "les micro-changements : « j'ai hésité 2 secondes de plus avant de cliquer », « je me suis surpris à "
    "respirer plus calmement », « j'ai dit non plus facilement ». Ces micro-signaux sont la preuve que le "
    "travail souterrain se fait.",
    "<b>L'inventaire des plateaux abandonnés.</b> Liste 5 disciplines que tu as commencées et abandonnées avant "
    "12 semaines. Si tu reprends UNE et la tiens cette fois jusqu'au basculement, ton année 2026 change."
]))
story.extend(phrase("Le plateau n'est pas l'absence de progrès. C'est la phase invisible du progrès."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(7, 3, "La hiérarchie en 3 couches",
    "Identité avant comportement avant résultat", ACCENT))
story.extend(idee(
    "Trois niveaux de changement, du plus superficiel au plus profond : résultats (ce que tu obtiens), "
    "processus (ce que tu fais), identité (ce que tu crois être). La plupart des gens se concentrent sur "
    "les résultats. Quelques-uns travaillent les processus. Très peu vont à l'identité. Or c'est l'identité "
    "qui pilote durablement les deux autres."
))
story.extend(mecan(
    "Quand tu veux changer, deux directions sont possibles. <b>De l'extérieur vers l'intérieur</b> : viser un "
    "résultat → forcer des processus → espérer un changement d'identité. Cette direction est instable — le "
    "changement dépend du résultat, qui dépend de variables hors contrôle. <b>De l'intérieur vers l'extérieur</b> : "
    "viser une identité → installer les processus cohérents → obtenir les résultats naturellement. Cette "
    "direction est stable — l'identité te pilote, les processus en découlent, les résultats émergent. "
    "Clear, Hougaard, Douglas pointent tous vers la même conclusion : <b>identité d'abord</b>."
))
story.extend(lien([
    "Pour toi, l'identité cible (déjà nommée avec Hougaard) : <b>« Je suis un trader chirurgical. »</b> "
    "Cette phrase n'est pas un slogan. C'est une affirmation identitaire qui doit devenir <b>ce que tu crois "
    "être</b>, pas ce que tu vises. La différence est tout.",
    "Tu installes une identité par <b>preuves cumulées</b>. Chaque fois que tu coupes un SL sans le décaler, "
    "tu déposes une preuve. Chaque fois que tu remplis ton journal, tu déposes une preuve. Chaque fois que "
    "tu respectes le BE+1R, tu déposes une preuve. Au début, les preuves sont peu nombreuses, tu ne te "
    "<b>crois</b> pas encore chirurgical — tu te <b>force</b>. À force de preuves, ta perception de toi-même "
    "bascule. Tu te <b>crois</b> chirurgical. À ce stade, les comportements deviennent automatiques.",
    "Tu peux installer plusieurs identités en parallèle : trader chirurgical (pour le marché), cavalier "
    "patient (pour l'équitation), entrepreneur méthodique (pour ATHÉNA), reconvalescent attentionné (pour "
    "ton corps post-TBI). Chacune cohérente avec son domaine."
]))
story.extend(exemple([
    "<b>Saboteur (couche résultat) :</b> « Je veux faire 30 000€ ce mois. » Tu cherches les setups qui te "
    "donneront ce résultat. Tu prends des risques pour l'obtenir. Tu sors de ton edge.",
    "<b>Couche processus :</b> « Je vais exécuter mon protocole 100 fois ce mois. » Mieux. Plus contrôlable. "
    "Mais ça reste de l'effort de volonté.",
    "<b>Cible (couche identité) :</b> « Je suis un trader chirurgical. Que fait un trader chirurgical "
    "aujourd'hui ? » À cette question, la réponse vient naturellement : il exécute son protocole sans "
    "drame, il ne pousse pas au-delà du TP, il ferme la plateforme après les ordres. Tu n'as pas à te "
    "forcer — c'est qui tu es. Le résultat (PnL) suit, ou pas — peu importe pour qui tu deviens."
]))
story.append(P("Schéma — Les 3 couches", h_subsection))
story.extend(ascii_schema("""
                    CHANGEMENT EXTÉRIEUR VERS INTÉRIEUR (échec garanti)
                    ─────────────────────────────────────────────
                    RÉSULTATS  ──►  Processus  ──►  Identité
                    (visible)        (forcés)       (espérée)

                    Si résultat manque, processus s'effondrent,
                    identité ne change pas.


                    CHANGEMENT INTÉRIEUR VERS EXTÉRIEUR (durable)
                    ──────────────────────────────────────────────
                    IDENTITÉ  ──►  Processus  ──►  Résultats
                    (choisie)      (naturels)     (qui suivent)

                    Identité est stable. Processus en découlent.
                    Résultats émergent. C'est la voie de Clear.

   Pour Marien :
   COUCHE 1 (résultat)  : "je veux gagner X€"
   COUCHE 2 (processus) : "je vais respecter mon protocole"
   COUCHE 3 (identité)  : "JE SUIS UN TRADER CHIRURGICAL"
                          → la seule qui produit du durable.
""", accent=ACCENT))
story.extend(exo([
    "<b>L'audit des couches.</b> Pour tes 3 grands domaines (trading, équitation, ATHÉNA), demande-toi : "
    "actuellement, je travaille à quelle couche ? Probablement résultat. Cible : déplacer vers identité.",
    "<b>La page identité.</b> Une page de ton journal dédiée. En majuscules, l'identité cible. En dessous, "
    "chaque jour, 1 ligne : « aujourd'hui qu'est-ce qu'un trader chirurgical a fait que j'ai fait aussi ? » "
    "Tu cumules les preuves.",
    "<b>La question identitaire pré-trade.</b> Avant CHAQUE clic, 5 secondes : « est-ce qu'un trader "
    "chirurgical ferait ce trade ? » Si non, tu ne cliques pas. À force, le filtre devient automatique."
]))
story.extend(phrase("Je ne vise pas un résultat. Je deviens une personne dont le résultat découle."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(7, 4, "La boucle d'habitude",
    "Démonter et reconstruire les automatismes", ACCENT))
story.extend(idee(
    "Toute habitude — bonne ou mauvaise — fonctionne sur la même mécanique : un <b>déclencheur</b> "
    "(signal, contexte) → un <b>désir</b> (motivation interne) → une <b>réponse</b> (comportement) → "
    "une <b>récompense</b> (gratification qui clôt la boucle). Comprendre cette structure te permet "
    "de démonter une mauvaise habitude et d'en installer une bonne en jouant sur les 4 leviers."
))
story.append(P("Les 4 éléments en détail", h_subsection))
story.append(styled_table([
    [C("Élément", cell_gold), C("Définition", cell_gold), C("Exemple chez toi", cell_gold)],
    [C("1. DÉCLENCHEUR", cell_bold),
     C("Signal qui active l'habitude (heure, lieu, état, événement précédent)"),
     C("14h, killzone NY ouverte, écran allumé, café terminé")],
    [C("2. DÉSIR", cell_bold),
     C("Motivation interne, anticipation de récompense"),
     C("« Je sens que ça va bouger, je veux saisir »")],
    [C("3. RÉPONSE", cell_bold),
     C("Le comportement effectif"),
     C("Cliquer Buy XAUUSD sans setup A+")],
    [C("4. RÉCOMPENSE", cell_bold),
     C("La gratification (souvent dopaminergique)"),
     C("Pic d'attente + soulagement temporaire")],
], [3*cm, 6*cm, 7*cm]))
story.append(Spacer(1, 8))
story.extend(mecan(
    "Pour <b>installer</b> une bonne habitude, tu rends les 4 éléments faciles. Pour <b>désinstaller</b> une "
    "mauvaise, tu rends au moins un des 4 éléments difficile (idéalement le déclencheur). C'est l'application "
    "pratique principale du livre."
))
story.append(P("Désinstaller le décalage de SL", h_subsection))
story.append(styled_table([
    [C("Élément", cell_gold), C("Actuellement", cell_gold), C("Modification", cell_gold)],
    [C("Déclencheur", cell_bold),
     C("Voir le prix s'approcher du SL, plateforme ouverte"),
     C("Fermer la plateforme dès l'ordre placé. Plus de vision = plus de déclencheur.")],
    [C("Désir", cell_bold),
     C("Éviter la perte ressentie comme injuste"),
     C("Visualisation pré-trade de la perte. SN pré-désensibilisé.")],
    [C("Réponse", cell_bold),
     C("Modifier le SL"),
     C("Si je vois encore : règle absolue de close the platform.")],
    [C("Récompense", cell_bold),
     C("Soulagement temporaire si le marché revient"),
     C("Reframe : la récompense est de ne pas avoir trahi mon plan. Note dans le journal.")],
], [3*cm, 6.5*cm, 6.5*cm]))
story.append(Spacer(1, 8))
story.append(P("Installer la respiration cohérente quotidienne", h_subsection))
story.append(styled_table([
    [C("Élément", cell_gold), C("Solution", cell_gold)],
    [C("Déclencheur", cell_bold),
     C("Empilement : juste après mon café du matin. La tasse vide = signal.")],
    [C("Désir", cell_bold),
     C("Rendre attirant : associer à un moment plaisant (vue, musique douce, fauteuil).")],
    [C("Réponse", cell_bold),
     C("Rendre facile : 2 minutes suffisent au début. Pas 10.")],
    [C("Récompense", cell_bold),
     C("Immédiate : noter avec satisfaction la croix verte sur le tableau de suivi.")],
], [3*cm, 13*cm]))
story.append(Spacer(1, 8))
story.extend(exo([
    "<b>Cartographier tes habitudes destructrices.</b> Pour chacune des 3 habitudes destructrices que tu "
    "veux désinstaller (décalage SL, sur-trading après perte, consommation contenu post-crash), remplis le "
    "tableau des 4 éléments. Identifie l'élément le plus facile à modifier (souvent le déclencheur).",
    "<b>Cartographier les habitudes constructives.</b> Pour les 3 habitudes que tu veux installer (méditation "
    "matinale, journal du soir, scan corporel pré-trade), remplis aussi les 4 éléments en mode installation.",
    "<b>Implémenter une seule à la fois.</b> Ne change pas 6 habitudes simultanément. Choisis une, "
    "tu l'installes proprement sur 6-8 semaines, puis tu passes à la suivante. La consistance bat l'ambition."
]))
story.extend(phrase("Mes habitudes se construisent en 4 éléments. Je modifie un élément, le tout bascule."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(7, 5, "L'environnement, ton allié silencieux",
    "Modifier l'environnement bat la discipline pure", ACCENT))
story.extend(idee(
    "La discipline est une ressource finie qui s'épuise. L'environnement, lui, est constant — il agit 24h/24 "
    "sans que tu aies à y penser. Si tu modifies ton environnement pour qu'il pousse vers les bonnes "
    "habitudes et rende les mauvaises difficiles, tu n'as plus besoin de discipline. Le système fait le "
    "travail à ta place."
))
story.extend(mecan(
    "Le cerveau humain suit le chemin de moindre résistance. Si une bonne habitude demande 5 actions pour "
    "se faire, tu vas la rater souvent. Si elle demande 0 action (elle est juste là, accessible), tu vas "
    "la faire. Inversement, si une mauvaise habitude demande 0 action (elle est facilement disponible), "
    "tu vas la faire. Si elle demande 5 actions, tu vas y renoncer souvent. La <b>friction</b> est la "
    "variable principale."
))
story.extend(lien([
    "Pour toi, l'environnement actuel pousse aux comportements destructeurs : apps de trading sur le téléphone "
    "(friction 0 pour cliquer), notifications activées (déclencheurs constants), Discord trading ouverts "
    "(stimulation continue), espace de travail confondu avec espace de vie (pas de sas mental). Modifier "
    "l'environnement réduit drastiquement le besoin de discipline.",
    "Inversement, pour installer les bonnes habitudes : avoir le cahier journal toujours visible et ouvert "
    "à la bonne page (friction 0 pour écrire), avoir la chaise de méditation toujours prête (friction 0 "
    "pour s'asseoir), avoir la tenue de sport préparée la veille (friction 0 pour s'entraîner)."
]))
story.append(P("L'audit d'environnement", h_subsection))
story.append(styled_table([
    [C("Domaine", cell_gold), C("Modification anti-mauvaise habitude", cell_gold), C("Modification pro-bonne habitude", cell_gold)],
    [C("Téléphone", cell_bold),
     C("Apps de trading désinstallées. Notifications désactivées. Mode focus pendant la nuit."),
     C("App de méditation visible sur écran d'accueil. Timer respiration en raccourci.")],
    [C("Bureau", cell_bold),
     C("Écran fermé en dehors des sessions. Plateforme déconnectée hors heures."),
     C("Cahier journal toujours visible. Affichage des 10 commandements et des 5 vérités.")],
    [C("Chambre", cell_bold),
     C("Aucun écran après 22h. Pas de téléphone dans la chambre."),
     C("Livre papier sur table de chevet. Lumière chaude. Routine coucher.")],
    [C("Salon / espace social", cell_bold),
     C("Pas d'écran trading en arrière-plan. Pas de Discord pendant les repas."),
     C("Espace de lecture confortable. Plante, ordre visuel.")],
    [C("Garde-robe", cell_bold),
     C("(N/A)"),
     C("Tenue de sport prête la veille pour le matin.")],
    [C("Cuisine", cell_bold),
     C("Pas de sucres rapides à portée de main. Pas d'alcool si tu veux éviter."),
     C("Eau visible. Café/thé préparé. Nourriture saine accessible.")],
], [2.5*cm, 6.5*cm, 7*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu te dis « je vais arrêter de check ma plateforme entre les trades ». Tu essayes par "
    "discipline. App toujours sur le téléphone, notifications actives. Tu craques 20 fois dans la journée. "
    "Tu te dis « je manque de volonté ».",
    "<b>Cible :</b> tu désinstalles l'app du téléphone. Tu mets ton téléphone en mode avion. Tu places le "
    "téléphone dans une autre pièce. Soudain, tu ne peux plus check. La friction est devenue insurmontable "
    "pour un geste impulsif. Tu te concentres sur ton journal. Pas de volonté en jeu — environnement modifié."
]))
story.extend(exo([
    "<b>L'audit environnement.</b> Sur chacun des 6 domaines du tableau, identifie 1 modification anti-mauvaise "
    "habitude et 1 modification pro-bonne habitude que tu peux faire CETTE SEMAINE.",
    "<b>La règle des 5 secondes / 20 secondes.</b> Bonne habitude : doit être accessible en moins de 5 secondes. "
    "Mauvaise habitude : doit demander plus de 20 secondes de friction. Tu calibres ton environnement sur "
    "ces règles.",
    "<b>Le nettoyage radical.</b> Une fois par mois, tu fais un grand nettoyage : suppression des comptes "
    "Discord inutiles, désabonnement de newsletters trading, suppression des followings inutiles sur X. "
    "Tu épures ton environnement informationnel."
]))
story.extend(phrase("Mon environnement est plus puissant que ma volonté. Je modélise l'environnement, je n'utilise plus la volonté."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(7, 6, "L'empilement d'habitudes et la règle des 2 minutes",
    "Démarrer petit, ancrer sur l'existant", ACCENT))
story.extend(idee(
    "Deux techniques d'installation puissantes. <b>L'empilement</b> : tu rattaches une nouvelle habitude à "
    "une habitude existante qui fonctionne déjà (« après X, je fais Y »). La nouvelle bénéficie de la "
    "régularité de l'ancienne. <b>La règle des 2 minutes</b> : tu commences toute nouvelle habitude par "
    "une version qui prend moins de 2 minutes. La consistance compte plus que l'intensité au début."
))
story.append(P("L'empilement d'habitudes — exemples pour toi", h_subsection))
story.append(styled_table([
    [C("Habitude existante", cell_gold), C("Nouvelle habitude empilée", cell_gold)],
    [C("Après mon café du matin", cell_bold),
     C("je fais 2 min de respiration cohérente.")],
    [C("Après ma respiration", cell_bold),
     C("je relis les 5 vérités à voix basse.")],
    [C("Après la lecture des vérités", cell_bold),
     C("j'ouvre mon journal et j'écris la section AVANT SESSION.")],
    [C("Après ma session de trading", cell_bold),
     C("je remplis la section APRÈS SESSION du journal.")],
    [C("Après ma douche du soir", cell_bold),
     C("je fais 5 min de scan corporel.")],
    [C("Après le scan corporel", cell_bold),
     C("j'écris 3 phrases dans le journal émotionnel.")],
    [C("Après mon pansage avec la filly", cell_bold),
     C("je note 1 chose que j'ai ressentie dans mon corps.")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 8))
story.append(P("La règle des 2 minutes — versions ridiculement petites", h_subsection))
story.append(styled_table([
    [C("Habitude ambitieuse", cell_gold), C("Version 2 minutes pour démarrer", cell_gold)],
    [C("Méditer 30 min/jour", cell_bold),
     C("Méditer 2 min/jour. C'est tout. Pas plus au début.")],
    [C("Faire 1h de sport/jour", cell_bold),
     C("Mettre la tenue de sport. C'est tout. Le reste vient ensuite.")],
    [C("Tenir un journal complet quotidien", cell_bold),
     C("Écrire 1 phrase par jour. C'est tout. La page complète vient.")],
    [C("Lire 1 livre/mois", cell_bold),
     C("Lire 1 page/jour. C'est tout.")],
    [C("Étudier 1 livre de cette bibliothèque/mois", cell_bold),
     C("Lire 1 module/semaine. C'est tout.")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 8))
story.extend(mecan(
    "Pourquoi 2 minutes ? Parce que l'enjeu est d'installer le <b>geste</b>, pas son ampleur. Une fois que "
    "le geste est installé (tu t'assieds pour méditer chaque matin), l'ampleur s'augmente naturellement. "
    "Mais si tu vises l'ampleur d'emblée, tu rates le geste — donc tu n'installes rien. C'est "
    "contre-intuitif mais c'est documenté : <b>petit et consistant battra toujours grand et sporadique</b>."
))
story.extend(lien([
    "Pour toi avec ton historique de cycles motivation, c'est la voie royale. Au lieu de te dire « je vais "
    "tout transformer ce mois », tu te dis « cette semaine je m'assieds pour méditer 2 min après mon café. "
    "Tous les jours. C'est tout. » Tu fais ça 4 semaines. Puis tu augmentes à 5 min. Puis 10. Puis 20. "
    "Sur 6 mois tu as une vraie pratique. Si tu visais 30 min directement, tu aurais abandonné après 10 jours.",
    "Cette logique s'applique à tout. Journal manuscrit : commence par 1 phrase par jour. Box : commence par "
    "5 min/séance. Lecture des modules de cette bibliothèque : 1 module par semaine, pas tout le livre en "
    "3 jours. Tu installes des gestes. L'ampleur viendra."
]))
story.extend(exemple([
    "<b>Saboteur :</b> dimanche soir, tu décides « lundi je commence : 30 min méditation, 1h sport, 30 min "
    "journal, 1 chapitre lecture ». Lundi tu tiens. Mardi aussi. Mercredi tu sautes la méditation parce que tu "
    "es fatigué. Jeudi tu ne fais rien. Vendredi tu te dis « j'ai foiré, je recommencerai lundi ». Cycle "
    "classique abandonné.",
    "<b>Cible :</b> dimanche soir, tu décides : « cette semaine, après mon café, 2 min de respiration. C'est tout. » "
    "Lundi : 2 min. Mardi : 2 min. Mercredi tu es fatigué : 2 min quand même, c'est tellement court qu'il n'y "
    "a pas d'excuse. Jeudi : 2 min. Sur 12 semaines, tu as 84 séances. À ce stade, le geste est installé. Tu "
    "peux passer à 5 min, sans drame."
]))
story.extend(exo([
    "<b>Identifier tes 3 habitudes existantes solides.</b> Quelles habitudes fais-tu tous les jours sans "
    "y penser ? (Café matin, douche, brossage de dents). Ces 3 sont tes points d'ancrage pour empiler.",
    "<b>Empiler 3 nouvelles habitudes ce mois.</b> Choisis 3 nouvelles habitudes à installer (version 2 min). "
    "Empile chacune sur une habitude existante. Suivi quotidien sur 30 jours.",
    "<b>L'engagement « 2 min ou rien ».</b> Pour chaque nouvelle habitude, commence par une version 2 min. "
    "Pendant 4 semaines minimum, tu ne fais que 2 min même si tu pourrais plus. Tu installes le geste avant "
    "d'agrandir l'ampleur."
]))
story.extend(phrase("Je commence ridiculement petit. La consistance bat l'ambition à chaque fois."))
story.append(PageBreak())


# --- LIVRE 7 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 7", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Les systèmes battent les objectifs. Tu redescends au niveau de tes systèmes.",
    "1% par jour pendant 365 jours = 37x mieux. L'arithmétique du temps long.",
    "Le plateau du potentiel latent : le progrès est invisible jusqu'au basculement.",
    "3 couches : résultats → processus → identité. Vise l'identité pour durable.",
    "La boucle d'habitude : déclencheur → désir → réponse → récompense.",
    "Modifier l'environnement bat la discipline pure.",
    "L'empilement : nouvelle habitude rattachée à habitude existante.",
    "Règle des 2 minutes : démarrer ridiculement petit pour installer le geste.",
    "Ne jamais manquer deux fois de suite. Un raté ≠ rechute. Deux ratés = début d'arrêt.",
    "Petit et consistant > grand et sporadique. Toujours.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Viser un résultat sans installer le système qui y mène.",
    "Vouloir tout changer en même temps.",
    "Démarrer fort, ambitieusement, et abandonner après 2 semaines.",
    "Croire que la discipline pure va suffire.",
    "Ignorer l'environnement comme levier.",
    "Mesurer le progrès uniquement par les résultats visibles.",
    "Abandonner pendant un plateau apparent.",
    "Vouloir installer une habitude à son ampleur finale dès le départ.",
    "Confondre intensité ponctuelle et changement durable.",
    "Ne pas relier nouvelle habitude à un déclencheur existant.",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je vise l'identité, pas le résultat.",
    "Je commence chaque nouvelle habitude en version 2 minutes.",
    "Je rattache chaque nouvelle habitude à un déclencheur existant.",
    "Je modifie mon environnement pour faciliter le bon et compliquer le mauvais.",
    "Je tiens 12 semaines minimum avant d'évaluer une discipline.",
    "Je ne change pas plus d'une habitude par mois.",
    "Je suis ma progression visuellement (calendrier ou grille).",
    "Je ne manque jamais deux fois de suite. Un raté, je reprends.",
    "Je note chaque jour 1 chose qui prouve mon identité cible.",
    "Je cherche les micro-changements pendant les plateaux, pas les grands résultats.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║      UN RIEN PEUT TOUT CHANGER  —  FICHE D'ANCRAGE       ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Identité d'abord. Système ensuite. Résultat suit.       ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Cycles de motivation au lieu de systèmes.               ║
   ║    Vouloir tout changer en même temps.                     ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE                                           ║
   ║    - "Lundi je m'y mets vraiment"                          ║
   ║    - Ambition trop grande pour le départ                   ║
   ║    - Abandon pendant le plateau (~semaine 4-8)             ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Identifier l'identité cible                          ║
   ║    2. Choisir UNE habitude version 2 min                   ║
   ║    3. L'empiler sur une habitude existante                 ║
   ║    4. Modifier l'environnement pour faciliter              ║
   ║    5. Suivre 12 semaines minimum avant évaluation          ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "1% par jour. Pendant 365 jours."                       ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Choisir 1 habitude + 1 empilement + 1 modif environnement║
   ║    pour les 4 prochaines semaines. Une seule.              ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Boucle décalage SL : modifier déclencheur (fermer plateforme).║
   ║    Empilement journal : après chaque session, journal.     ║
   ║    Identité : "je suis trader chirurgical".                ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 7 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 8 — LÂCHER PRISE (David Hawkins)
# ============================================================
_current_book_color[0] = BOOK_COLORS[7]
ACCENT = BOOK_COLORS[7]

story.extend(book_separator_page(
    8, "Lâcher prise", "David R. Hawkins", "Letting Go: The Pathway of Surrender", 2012, ACCENT,
    quote='« Ce que tu retiens te retient.<br/>Ce que tu lâches te libère. »',
    subtitle="La voie de la reddition consciente"
))

story.extend(book_intro_header(8, "Lâcher prise", "David R. Hawkins — 2012", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "Hawkins est psychiatre et auteur, connu pour son travail sur la conscience et la régulation émotionnelle. "
    "Ce livre adresse une compétence qui te manque cruellement et qui est l'antidote direct à ton "
    "fonctionnement actuel : la capacité à <b>lâcher prise</b>. Pas comme un slogan New Age, mais comme "
    "une compétence opérationnelle qui s'entraîne, se mesure, se développe."
))
story.append(P(
    "Tu es un contrôleur. C'est documenté dans ton parcours. Le contrôle t'a sauvé après 2022 — il a fallu "
    "reconstruire un corps qui ne répondait plus, une mémoire fragmentée, un avenir à redéfinir. Cette "
    "compétence de contrôle est une des forces de ton identité. Mais elle a un coût gigantesque : tu ne sais "
    "plus lâcher quand il faudrait lâcher. Tu serres dans des contextes où serrer aggrave (un trade qui "
    "tourne mal, une émotion qui veut s'exprimer, une journée qui demande du repos)."
))
story.append(P(
    "Hawkins t'apprend que le lâcher-prise n'est pas une faiblesse opposée au contrôle. C'est une "
    "<b>compétence complémentaire</b>. Le maître n'est pas celui qui contrôle tout, ni celui qui ne "
    "contrôle rien — c'est celui qui sait <b>quand contrôler et quand lâcher</b>, et qui peut faire les "
    "deux à volonté. Pour toi qui as développé un côté de cette balance à 100%, ce livre travaille l'autre."
))
story.append(P(
    "Lis-le après avoir intégré les concepts somatiques (van der Kolk, Levine) et identitaires (Clear). "
    "Sans ces fondations, le lâcher-prise reste un concept mental que tu ne sais pas incarner. Avec ces "
    "fondations, il devient une pratique réelle."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>Toute émotion non lâchée se transforme en charge accumulée. Lâcher est une compétence, pas une mollesse.</b>', pull_quote))
story.append(P(
    "Hawkins défend une idée simple et puissante : les émotions humaines fonctionnent comme des charges "
    "électriques. Tant qu'elles ne sont pas <b>déchargées consciemment</b>, elles continuent de "
    "circuler dans ton système. Tu peux croire qu'elles sont passées — elles sont juste enfouies. À force "
    "d'accumulation, elles produisent des états chroniques (anxiété de fond, irritabilité, lassitude, "
    "tristesse vague) que tu finis par prendre pour des traits de caractère."
))
story.append(P("Les mécanismes exposés", h_subsection))
story.append(P(
    "<b>1. La résistance amplifie ce qu'elle combat.</b> Quand tu résistes à une émotion, elle gagne en "
    "intensité. Quand tu l'accueilles sans la combattre, elle perd sa charge. C'est le paradoxe central. "
    "<b>2. Les trois options face à une émotion :</b> la supprimer (elle reste, s'accumule), l'exprimer "
    "(elle peut se libérer mais peut aussi renforcer le pattern qui la produit), la <b>lâcher</b> (méthode "
    "spécifique : la sentir pleinement sans réagir, sans la suivre, jusqu'à ce qu'elle se dissipe). "
    "<b>3. Le mécanisme physiologique du lâcher-prise :</b> attention soutenue + non-réactivité + respiration "
    "= dissolution de la charge. Documenté en neurosciences contemplatives. "
    "<b>4. La hiérarchie des états émotionnels :</b> certains états (honte, culpabilité, peur, colère) sont "
    "plus contractants ; d'autres (acceptation, paix, joie) sont plus expansifs. Le travail consiste à "
    "monter progressivement dans cette hiérarchie. <b>5. Le piège du contrôle :</b> plus tu contrôles "
    "l'émotion, plus elle te contrôle en retour. Le lâcher est le seul vrai pouvoir."
))
story.append(P("Les transformations proposées", h_subsection))
story.append(P(
    "<b>Apprendre la technique du lâcher-prise</b> : observer la sensation corporelle d'une émotion sans "
    "vouloir la modifier, jusqu'à sa dissipation naturelle. <b>Identifier ses émotions chroniques cachées</b> : "
    "celles qui sont devenues le baseline et qu'on ne reconnaît plus. <b>Pratiquer la non-réactivité</b> : "
    "ressentir sans agir immédiatement. <b>Cultiver l'acceptation</b> : pas la résignation passive, mais "
    "l'arrêt du combat intérieur contre ce qui est."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Le ton du livre peut paraître mystique ou ésotérique par moments. Certaines affirmations de Hawkins "
    "(notamment sur les « niveaux de conscience ») relèvent de sa philosophie personnelle plus que de "
    "données scientifiques. À lire avec ce filtre : la <b>technique</b> du lâcher-prise est solide et "
    "documentée par d'autres traditions (méditation Vipassana, ACT en thérapie cognitive moderne, "
    "psychologie bouddhiste contemporaine). Tu peux prendre la technique en laissant la cosmologie."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Lâcher prise",
    [
        {"label": "THÈSE", "leaves": ["résistance amplifie", "lâcher dissout"], "color": DARK_GREY},
        {"label": "MÉCANISMES", "leaves": ["3 options émotion", "piège du contrôle", "linéaire / stochastique"], "color": ACCENT},
        {"label": "MÉTHODE", "leaves": ["6 étapes", "90 sec", "non-réactivité"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Le lâcher comme compétence opérationnelle — pas attitude mystique.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(8, 1, "La résistance amplifie",
    "Le paradoxe central — combattre une émotion la renforce", ACCENT))
story.extend(idee(
    "Quand tu résistes à une émotion (peur, colère, tristesse, anxiété), tu lui donnes de l'énergie. "
    "La résistance la renforce. Quand tu cesses de résister — quand tu l'accueilles sans vouloir la "
    "modifier — elle perd progressivement sa charge. C'est contre-intuitif mais documenté. "
    "<b>Ce à quoi tu résistes persiste. Ce que tu acceptes traverse.</b>"
))
story.extend(mecan(
    "Physiologiquement : une émotion est une activation neurochimique transitoire. Si tu la laisses traverser, "
    "elle dure typiquement 60 à 90 secondes (les neurosciences ont mesuré ça). Si tu lui résistes "
    "(jugement, suppression, agitation mentale), tu réactives le circuit. L'émotion qui aurait duré 90 "
    "secondes peut alors durer des heures, des jours, des années. La résistance est le carburant qui "
    "maintient l'émotion en place."
))
story.extend(lien([
    "Toi tu résistes presque tout le temps. Quand une perte arrive, tu résistes à la tristesse / colère / "
    "honte qui montent — tu te dis « faut pas, faut tenir, faut avancer ». Tu repousses. L'émotion ne "
    "passe pas — elle se loge dans le corps. Tu finis par porter en permanence un mélange de tristesse, "
    "colère et honte non traitées qui forme un baseline émotionnel difficile.",
    "Pour ton pattern +1500 spécifiquement : tu résistes à la sensation de « laisser de l'argent sur la table ». "
    "Cette sensation est une peur (peur de manquer). Tu n'acceptes pas cette peur — tu agis contre elle "
    "en poussant. Ce que tu pourrais faire à la place : accueillir la peur de manquer pendant 90 secondes "
    "à voix basse (« ok, j'ai peur de laisser de l'argent — je sens cette peur, je ne la combats pas »). "
    "Tu serais surpris : la peur passe, et l'envie de pousser passe avec elle."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu cramés un compte. Tu ressens monter une vague de honte. Tu résistes immédiatement : "
    "« non, faut pas, il faut avancer, j'ai pas le temps pour ça ». Tu suppresses. La honte ne passe pas. "
    "Tu la portes pendant des semaines en arrière-plan. Elle nourrit ton prochain trade impulsif.",
    "<b>Cible :</b> tu cramés. Tu sens la honte monter. Tu te poses (3 min suffisent). Tu te dis intérieurement : "
    "« voilà la honte. Je la sens. Je ne la combats pas. Je ne la justifie pas. Je l'observe. » Tu la sens "
    "dans le ventre, la poitrine, la gorge. Tu respires lentement. Tu ne fais rien d'autre que sentir. "
    "Après 60-90 secondes, la vague passe. Tu reprends ta journée — sans cette honte accumulée."
]))
story.append(P("Schéma — Le paradoxe de la résistance", h_subsection))
story.extend(ascii_schema("""
   RÉSISTER À UNE ÉMOTION (ce que tu fais)
   ───────────────────────────────────────
                Émotion monte
                      │
                      ▼
                Tu juges, suppresses, fuis
                      │
                      ▼
                L'émotion est interprétée comme menace
                      │
                      ▼
                Circuit neuronal RÉACTIVÉ
                      │
                      ▼
                Émotion reste, voire amplifie
                      │
                      ▼
                Accumulation chronique


   ACCUEILLIR UNE ÉMOTION (la voie du lâcher-prise)
   ────────────────────────────────────────────────
                Émotion monte
                      │
                      ▼
                Tu observes sans juger
                      │
                      ▼
                Pas de réaction de menace
                      │
                      ▼
                Cycle physiologique COMPLET (60-90 sec)
                      │
                      ▼
                Émotion se dissipe naturellement
                      │
                      ▼
                Système nerveux retourne au baseline
""", accent=ACCENT))
story.extend(exo([
    "<b>Pratique des 90 secondes.</b> La prochaine fois que tu sens une émotion désagréable monter, "
    "pose-toi 90 secondes. Pas plus. Tu fais juste sentir, sans rien faire d'autre. Tu vas être étonné : "
    "la plupart des émotions ne durent vraiment que ça quand on ne leur résiste pas.",
    "<b>Inventaire des résistances chroniques.</b> Quelles émotions tu n'acceptes pas chez toi ? Probablement "
    "tristesse, vulnérabilité, échec, peur. Liste-les. Chacune est une porte fermée derrière laquelle "
    "s'accumule une charge.",
    "<b>Phrase de désamorçage.</b> Quand tu sens monter une émotion, dis intérieurement (ou à voix basse) : "
    "« Je laisse cette émotion être là. Je n'ai pas à la résoudre maintenant. Je la sens. C'est tout. » "
    "Cette phrase coupe court à la résistance automatique."
]))
story.extend(phrase("Ce à quoi je résiste persiste. Ce que je laisse être traverse."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(8, 2, "Les trois options face à une émotion",
    "Supprimer, exprimer, lâcher — choisir consciemment", ACCENT))
story.extend(idee(
    "Face à une émotion, tu as trois options. <b>La supprimer</b> (la pousser hors de conscience — elle "
    "s'accumule). <b>L'exprimer</b> (la décharger en action — soulage parfois, peut renforcer le pattern "
    "qui la produit). <b>La lâcher</b> (la sentir pleinement sans réagir, jusqu'à dissolution — la seule "
    "qui résout vraiment). La majorité oscille entre les deux premières sans jamais utiliser la troisième."
))
story.append(P("Les trois options en détail", h_subsection))
story.append(styled_table([
    [C("Option", cell_gold), C("Description", cell_gold), C("Effet long terme", cell_gold)],
    [C("1. SUPPRIMER", cell_bold),
     C("Tu pousses l'émotion hors de conscience. Tu te distrais. Tu refuses de ressentir."),
     C("Émotion reste dans le corps. Accumulation. Symptômes somatiques.")],
    [C("2. EXPRIMER", cell_bold),
     C("Tu agis sous l'effet de l'émotion. Tu cries, tu pleures, tu trades impulsivement, etc."),
     C("Décharge immédiate. Mais peut renforcer le pattern et créer des conséquences relationnelles ou matérielles.")],
    [C("3. LÂCHER", cell_bold),
     C("Tu ressens pleinement sans réagir. Tu observes sans bouger. Tu respires. Tu attends que ça passe naturellement."),
     C("Dissolution réelle de la charge. Pas de conséquence externe. Renforcement de la capacité.")],
], [2.5*cm, 7*cm, 6.5*cm]))
story.append(Spacer(1, 8))
story.extend(mecan(
    "Les deux premières options sont presque automatiques chez la plupart des humains. Suppression : "
    "« je ne dois pas ressentir ça ». Expression : « il faut que ça sorte ». Le lâcher est une compétence "
    "qui ne s'installe pas par accident — elle demande une <b>pratique délibérée</b>. C'est exactement comme "
    "apprendre un nouveau geste sportif : au début, c'est conscient et difficile ; à force de pratique, "
    "ça devient un réflexe disponible."
))
story.extend(lien([
    "Pour toi : <b>quand tu es seul</b>, tu suppresses massivement (« il faut tenir »). <b>Quand tu es en "
    "trade</b>, tu exprimes massivement (le décalage de SL est une expression de peur, le push à +1500 est "
    "une expression de désir, le revenge trade est une expression de colère). Ces deux modes ne te "
    "résolvent rien. Le travail est d'installer la troisième option — le lâcher.",
    "Concrètement pendant un trade : quand tu sens monter le désir de pousser au-delà du TP, tu ne suppresses "
    "pas (« je ne dois pas ressentir ça »), tu n'exprimes pas (« je pousse »). Tu LÂCHES : tu sens le "
    "désir dans ton corps, tu respires, tu attends que la vague passe. Pendant ce temps, ton plan exécute "
    "ce qu'il devait exécuter (couper au TP). Tu coexistes avec le désir sans lui obéir."
]))
story.extend(exemple([
    "<b>Saboteur (suppression) :</b> tu perds 3 trades. Tu ressens monter une frustration sourde. Tu te dis "
    "« je dois pas y penser ». Tu repasses devant la plateforme. Tu reprends sans avoir traité. Tu re-perds.",
    "<b>Saboteur (expression) :</b> tu perds 3 trades. Tu ressens la colère monter. Tu prends un autre trade "
    "B-grade pour « me refaire ». Tu exprimes la colère en action. Tu cramés.",
    "<b>Cible (lâcher) :</b> tu perds 3 trades. Tu sens la frustration / colère monter. Tu fermes la "
    "plateforme. Tu t'assieds 5 minutes en silence. Tu sens. Tu respires. Tu laisses la vague passer. "
    "À la fin des 5 minutes, l'émotion a perdu sa charge. Tu décides en lucidité si tu reprends ou pas — "
    "probablement pas, mais cette décision n'est plus chargée."
]))
story.extend(exo([
    "<b>Cartographier tes 3 options préférées par situation.</b> Pour 5 situations émotionnelles fréquentes "
    "chez toi (perte de trade, conflit, fatigue, demande sociale, FOMO), identifie laquelle des 3 options "
    "tu utilises spontanément. Tu vas voir un pattern net.",
    "<b>Tester le lâcher sur une émotion mineure aujourd'hui.</b> Aujourd'hui, dès qu'une petite émotion "
    "désagréable monte (impatience dans un bouchon, agacement face à un message), tu pratiques le lâcher : "
    "tu observes, tu respires, tu attends 90 secondes. C'est ton entraînement.",
    "<b>Le journal des 3 options.</b> Chaque soir, repère 3 émotions vécues dans la journée. Pour chacune, "
    "note laquelle des 3 options tu as utilisée. Sur 30 jours, ratio chiffré de tes patterns."
]))
story.extend(phrase("Suppression, expression, lâcher. Je connais les trois. Je choisis le lâcher consciemment."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(8, 3, "La technique du lâcher-prise",
    "Le protocole étape par étape", ACCENT))
story.extend(idee(
    "Le lâcher-prise n'est pas une attitude mystique. C'est une <b>technique précise</b> avec des étapes "
    "concrètes. Comme toute technique, elle s'apprend, elle se rate au début, elle s'améliore avec la "
    "pratique. Voici la version opérationnelle, sans jargon."
))
story.append(P("Le protocole en 6 étapes", h_subsection))
story.extend(ascii_schema("""
   1. NOMMER
      Tu identifies l'émotion qui monte. "C'est de la peur. C'est de la
      colère. C'est de la honte." Le mot exact. Pas un terme vague.

   2. LOCALISER
      Où dans le corps ? "Ma poitrine. Ma gorge. Mon ventre."
      Tu poses ton attention dessus, comme un projecteur.

   3. ACCEPTER
      Tu te dis intérieurement : "j'autorise cette émotion à être ici
      maintenant. Je n'ai pas à la résoudre. Elle peut être là."
      C'est l'antidote à la résistance.

   4. RESPIRER VERS LA SENSATION
      Tu inspires doucement, comme si tu dirigeais l'air vers la zone
      où tu sens l'émotion. Tu expires lentement. 4-6 cycles.

   5. ATTENDRE
      Tu attends. 60 à 90 secondes minimum. Tu ne fais rien d'autre.
      Tu observes ce qui se passe dans la sensation.
      Elle va changer — devenir plus forte un instant, puis se diluer.

   6. CONSTATER
      Tu remarques que la charge a diminué. Pas forcément disparu —
      diminuée. Tu continues si tu veux, ou tu reprends ta journée.
""", accent=ACCENT))
story.extend(mecan(
    "Ce qui se passe physiologiquement : en nommant, tu actives ton cortex préfrontal (réducteur d'amygdale "
    "documenté). En respirant lentement vers la sensation, tu actives le vagal ventral (apaisement "
    "parasympathique). En acceptant, tu coupes la boucle de résistance qui maintenait l'activation. "
    "En 60-90 secondes, le cycle physiologique de l'émotion se complète. La charge se dissout."
))
story.extend(lien([
    "Pour toi en particulier, l'étape 3 (accepter) est la plus difficile. Tu es entraîné à ne pas accepter "
    "ce qui te ralentit. Pour toi, accepter une émotion = « valider une faiblesse ». C'est une croyance "
    "erronée. Accepter ≠ se résigner. Accepter signifie : reconnaître ce qui EST déjà là. Ce qui est déjà "
    "là EST déjà là — que tu l'acceptes ou non. La seule différence : si tu l'acceptes, elle peut traverser. "
    "Si tu refuses, elle reste.",
    "Pour ton trading, cette technique est applicable en temps réel pendant les sessions. Quand tu sens "
    "monter un désir (de pousser, de décaler, de prendre un trade hors plan), tu pratiques les 6 étapes "
    "en 90 secondes. Tu sors de la session si nécessaire. Tu reviens après la dissolution. Ton plan "
    "reste intact."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu es à +1200 PnL XAUUSD. Le marché continue de monter. Tu sens un désir intense de "
    "pousser au-delà du TP. Tu te dis « allez, momentum solide ». Tu pousses. Tu vois.",
    "<b>Cible :</b> +1200 PnL. Désir intense de pousser. Tu pratiques. <b>1) Nommer :</b> « c'est du désir, de "
    "l'avidité ». <b>2) Localiser :</b> « ça monte dans ma poitrine, dans ma gorge ». <b>3) Accepter :</b> "
    "« je peux ressentir cet élan. C'est OK. Je n'ai pas à agir dessus. » <b>4) Respirer :</b> 4 cycles "
    "lents vers la poitrine. <b>5) Attendre :</b> 60 secondes. La vague monte, puis redescend. <b>6) "
    "Constater :</b> la charge a baissé de 8/10 à 4/10. Tu peux maintenant exécuter ton plan : couper au TP."
]))
story.extend(exo([
    "<b>Pratique quotidienne du protocole.</b> 1 fois par jour, sur une émotion mineure : tu fais les 6 "
    "étapes complètes. Tu écris une ligne dans ton journal pour valider que tu l'as fait. À force de "
    "répétition, le protocole devient disponible automatiquement.",
    "<b>Pratique pré-trade.</b> Avant chaque session, 5 minutes : tu te connectes à ton corps. Y a-t-il "
    "une charge émotionnelle déjà présente (anxiété, désir, frustration restante d'hier) ? Si oui, "
    "protocole de lâcher avant d'ouvrir la plateforme.",
    "<b>Pratique en situation aiguë.</b> Quand tu sens une émotion forte en plein trade (désir de pousser, "
    "peur de couper), tu fais une version rapide du protocole en 30 secondes. Tu fermes la plateforme "
    "physiquement pendant ce temps."
]))
story.extend(phrase("Le lâcher est une technique. 6 étapes. 90 secondes. Pratiquées, elles deviennent réflexes."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(8, 4, "Le piège du contrôle",
    "Pourquoi plus tu serres, plus tu te brûles", ACCENT))
story.extend(idee(
    "Le contrôle est utile dans les domaines où ton effort a un impact direct (ton corps en entraînement, "
    "ton business ATHÉNA, ta relation avec ta filly). Il est <b>destructeur</b> dans les domaines où ton "
    "effort n'a aucun impact direct (la direction du marché, le comportement des autres, le résultat d'un "
    "trade individuel). Confondre les deux est le piège classique."
))
story.extend(mecan(
    "Le contrôle est une stratégie qui marche dans les systèmes <b>linéaires</b> (effort → résultat "
    "proportionnel). Le marché est un système <b>non-linéaire</b> et <b>stochastique</b> (effort n'a pas "
    "de relation directe avec résultat individuel). Appliquer la stratégie linéaire à un système non-linéaire "
    "produit systématiquement de l'échec. Plus tu serres dans un système où serrer n'a pas de prise, plus "
    "tu te crispes inutilement, et plus tu fais des erreurs (parce que la crispation altère le jugement)."
))
story.extend(lien([
    "Pour toi, c'est une distinction VITALE à intégrer. Tu confonds les domaines. Tu appliques au trading "
    "(non-linéaire) les mêmes outils mentaux que tu appliques à l'équitation (linéaire — un cheval qui "
    "refuse un obstacle, tu insistes, ça finit par passer). En trading, insister produit l'inverse de "
    "l'équitation : ça crame le compte.",
    "Le tableau ci-dessous t'aide à classer tes domaines de vie. Tu sauras dans lequel tu peux serrer et "
    "dans lequel tu dois lâcher."
]))
story.append(styled_table([
    [C("Domaine", cell_gold), C("Type", cell_gold), C("Stratégie", cell_gold)],
    [C("Ta méthode SMC", cell_bold), C("Linéaire (entraînement)"),
     C("CONTRÔLER. Plus tu pratiques, mieux tu lis.")],
    [C("Le résultat d'un trade individuel", cell_bold), C("Stochastique"),
     C("LÂCHER. Aucun contrôle possible. Probabiliste.")],
    [C("Ton respect du protocole", cell_bold), C("Linéaire (comportement)"),
     C("CONTRÔLER. Tu peux choisir à chaque clic.")],
    [C("La direction du marché", cell_bold), C("Stochastique"),
     C("LÂCHER. Aucun pouvoir.")],
    [C("Ton corps en rééducation", cell_bold), C("Linéaire (entraînement)"),
     C("CONTRÔLER. Discipline donne résultat.")],
    [C("Tes émotions qui montent", cell_bold), C("Stochastique"),
     C("LÂCHER. Tu ne choisis pas ce qui monte. Tu choisis ce que tu en fais.")],
    [C("ATHÉNA — production 3D", cell_bold), C("Linéaire (entraînement)"),
     C("CONTRÔLER. Effort = résultat sur le moyen terme.")],
    [C("Ce que les autres pensent de toi", cell_bold), C("Stochastique"),
     C("LÂCHER. Aucun contrôle direct.")],
], [4.5*cm, 4.5*cm, 7*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu prends un trade XAUUSD. Le marché va contre toi. Tu te dis « je dois forcer mon "
    "hypothèse à se valider ». Tu rajoutes au perdant. Tu décales le SL. Tu appliques la stratégie de "
    "contrôle dans un système où le contrôle n'a pas de prise.",
    "<b>Cible :</b> tu prends le trade. Marché va contre toi. Tu te dis « je ne contrôle pas le marché. Je "
    "contrôle uniquement ma sortie. » SL touché. Tu sors. Tu n'as rien forcé. Tu as joué ce que tu pouvais "
    "jouer (ton plan), tu as lâché ce que tu ne pouvais pas jouer (le résultat de ce trade individuel)."
]))
story.extend(exo([
    "<b>L'audit du contrôle.</b> Pour chacun de tes domaines de vie (5-7 domaines), classe : linéaire/stochastique. "
    "Cette carte mentale doit être claire et tu dois t'y référer souvent.",
    "<b>La règle d'or pré-trade.</b> Avant chaque session, tu te récites : « je contrôle ma méthode, ma "
    "taille, mon SL, mon TP, mon respect du plan, le moment où je ferme la plateforme. Je ne contrôle "
    "rien d'autre. » Cette récitation t'aide à rester dans ta zone d'action.",
    "<b>L'exercice du serrement.</b> Quand tu te surprends à serrer (mâchoire, poings, épaules) en trade : "
    "tu prends ce signal comme un indicateur que tu essayes de contrôler quelque chose qui ne se contrôle "
    "pas. Tu relâches physiquement (mâchoire, poings, épaules). Tu observes ce qui change mentalement. "
    "Le corps et l'esprit suivent le même mouvement."
]))
story.extend(phrase("Je contrôle mes gestes. Je lâche les résultats. Cette distinction est ma liberté."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(8, 5, "L'acceptation comme puissance",
    "Pas la résignation — l'arrêt du combat", ACCENT))
story.extend(idee(
    "L'acceptation est souvent confondue avec la résignation passive. C'est exactement l'inverse. "
    "Accepter ne veut pas dire « approuver », « se satisfaire de », « ne rien faire ». Accepter veut "
    "dire <b>reconnaître ce qui est déjà là, sans le combattre</b>. À partir de cette reconnaissance, "
    "tu peux agir de façon adaptée. Sans cette reconnaissance, tu agis contre une réalité illusoire."
))
story.extend(mecan(
    "Quand tu n'acceptes pas une réalité, tu dépenses de l'énergie à la nier, à la combattre, à la "
    "compenser. Cette énergie est <b>dépensée à vide</b> — elle ne change pas la réalité, elle la rend "
    "juste plus pénible à vivre. Quand tu acceptes, tu libères cette énergie. Elle redevient disponible "
    "pour l'action utile (celle qui peut effectivement changer ce qui est changeable). L'acceptation est "
    "donc une stratégie d'<b>économie énergétique</b>, pas une mollesse."
))
story.extend(lien([
    "Pour toi, plusieurs choses demandent acceptation et tu y résistes activement. <b>Ton TBI 2022 et ses "
    "séquelles</b> : si tu acceptes que ton SN n'est pas neurotypique aujourd'hui, tu peux travailler "
    "intelligemment AVEC lui. Si tu résistes (« je devrais être comme avant »), tu travailles CONTRE lui — "
    "et ça t'épuise. <b>Tes patterns destructeurs</b> : si tu acceptes qu'ils existent, qu'ils sont "
    "puissants, qu'ils ne disparaîtront pas du jour au lendemain, tu peux construire une stratégie "
    "longue de transformation. Si tu résistes (« je devrais déjà être réparé »), tu te blâmes en boucle "
    "sans avancer. <b>Le temps long du changement</b> : si tu acceptes que la transformation prend des "
    "années, tu peux la mener. Si tu résistes (« ça devrait aller plus vite »), tu abandonnes à chaque "
    "plateau.",
    "L'acceptation paradoxalement DÉBLOQUE le changement. Tant que tu refuses où tu en es, tu ne peux pas "
    "bouger d'où tu es. Tu es figé contre une réalité que tu ne reconnais pas. Reconnais-la, et tu peux "
    "commencer à bouger à partir d'elle."
]))
story.append(P("Ce que l'acceptation n'est PAS", h_subsection))
story.append(styled_table([
    [C("Confusion à éviter", cell_gold), C("Réalité de l'acceptation", cell_gold)],
    [C("« Accepter c'est se résigner »", cell_bold),
     C("Non. C'est reconnaître le point de départ pour avancer.")],
    [C("« Accepter c'est ne rien faire »", cell_bold),
     C("Non. C'est libérer l'énergie pour faire ce qui est utile.")],
    [C("« Accepter c'est valider »", cell_bold),
     C("Non. Tu peux accepter une réalité que tu trouves injuste / pénible.")],
    [C("« Accepter c'est oublier »", cell_bold),
     C("Non. C'est cesser de combattre en pensée ce qui est déjà arrivé.")],
    [C("« Accepter c'est faible »", cell_bold),
     C("Non. C'est plus dur que combattre. Demande plus de courage.")],
], [6*cm, 10*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu refuses d'accepter que tu as un système nerveux dérégulé. Tu te dis « je devrais "
    "être normal à 25 ans, j'ai pas le temps pour ça ». Tu trades comme si tu étais neurotypique. Tu "
    "craquesselon des mécaniques que tu refuses de reconnaître. Tu te juges sur chaque crash. Cycle "
    "auto-destructeur.",
    "<b>Cible :</b> tu acceptes : « j'ai vécu un TBI en 2022. Mon SN porte encore des empreintes. C'est "
    "une réalité, pas un jugement. À partir de là, qu'est-ce que je peux faire intelligemment ? » "
    "Acceptation libère stratégie : tu intègres des pratiques somatiques, tu consultes un thérapeute SE, "
    "tu adaptes ton protocole de trading à ta réalité actuelle. Acceptation a débloqué l'action utile."
]))
story.extend(exo([
    "<b>L'inventaire des refus.</b> Liste 5 réalités de ta vie actuelle que tu refuses d'accepter "
    "intérieurement. Pour chacune, écris pourquoi tu la refuses, puis ce que serait une acceptation "
    "(sans résignation). Tu vas voir : l'acceptation ouvre des chemins que la résistance bloque.",
    "<b>La phrase de désamorçage.</b> Quand tu te surprends à combattre intérieurement une réalité "
    "(événement passé, état actuel, comportement d'autrui), tu te dis : « ceci est. Je peux ne pas "
    "l'aimer. Je n'ai pas à le combattre dans ma tête. À partir d'ici, qu'est-ce que je fais ? »",
    "<b>Méditation d'acceptation.</b> 5 min/jour : tu fermes les yeux, tu énonces une réalité que tu "
    "as du mal à accepter. Tu respires. Tu te dis « je laisse cela être ». Tu observes ce qui se "
    "passe dans ton corps. À force, la résistance se relâche."
]))
story.extend(phrase("Accepter n'est pas se résigner. C'est cesser de combattre dans ma tête ce qui est déjà là."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(8, 6, "Le lâcher comme compétence opérationnelle",
    "Application au trading quotidien", ACCENT))
story.extend(idee(
    "Tout ce qu'on a vu dans ce livre se concrétise dans des situations de trading précises. Voici comment "
    "le lâcher-prise s'applique opérationnellement à tes patterns destructeurs. C'est l'aboutissement "
    "pratique du livre, applicable dès demain."
))
story.append(P("Les 7 moments-clés où lâcher en trading", h_subsection))
story.append(styled_table([
    [C("Moment", cell_gold), C("Ce qu'il faut LÂCHER", cell_gold), C("Comment", cell_gold)],
    [C("Avant un trade", cell_bold),
     C("Le besoin de savoir si ce trade va marcher"),
     C("Récitation V2 : « je n'ai pas besoin de savoir pour gagner »")],
    [C("Au TP atteint", cell_bold),
     C("Le désir de pousser au-delà"),
     C("Protocole 6 étapes en 90 secondes + couper le TP")],
    [C("Au SL approché", cell_bold),
     C("Le besoin d'éviter cette perte"),
     C("Close the platform. SL fait son boulot. Lâcher physiquement.")],
    [C("Après une perte", cell_bold),
     C("La narration « j'ai eu tort »"),
     C("Reframe : « ce trade est dans les 45% qui perdent ». Pas de jugement.")],
    [C("Après une série de pertes", cell_bold),
     C("L'urgence de se refaire"),
     C("Pause 24h. Tu lâches l'envie de revanche. Tu reprends froid.")],
    [C("Après un gros gain", cell_bold),
     C("Le sentiment d'invincibilité"),
     C("Pause 24h aussi. Tu ne fais pas confiance à l'euphorie.")],
    [C("En fin de session", cell_bold),
     C("Le besoin de checker encore"),
     C("Plateforme désactivée. Vie reprise. Le marché continue sans toi.")],
], [3.2*cm, 5.5*cm, 7.3*cm]))
story.append(Spacer(1, 8))
story.extend(lien([
    "Pour toi, sur les 7 moments, les plus critiques sont : <b>au TP atteint</b> (ton pattern +1500), "
    "<b>au SL approché</b> (ton décalage signature), <b>après une série de pertes</b> (ton FOMO compensatoire). "
    "Ces trois moments demandent un travail spécifique. Si tu maîtrises le lâcher dans ces trois moments, "
    "ton trading change de nature.",
    "Note : maîtriser le lâcher n'est pas un événement (« j'y arrive »). C'est une <b>compétence progressive</b>. "
    "Au début, tu vas réussir 2 fois sur 10. Puis 5 sur 10. Puis 8 sur 10. Sur 6-12 mois de pratique "
    "consciente, ça devient un réflexe disponible."
]))
story.extend(exemple([
    "<b>Saboteur :</b> XAUUSD à +800. TP à +1000. Tu coupes pas. +1500. Vague d'euphorie. Tu ne lâches rien. "
    "Reverse. -200. Tu ne lâches toujours rien. Tu décales le SL. -800. Compte cassé.",
    "<b>Cible :</b> +800. Tu sens monter le désir de pousser. Tu pratiques le protocole en 90s sans fermer "
    "la plateforme. Le désir baisse. Tu coupes au TP +1000. Tu fermes la plateforme. Tu ne sais pas si "
    "ça serait monté à +1500 ou redescendu — tu n'as pas besoin de le savoir. Tu as lâché."
]))
story.extend(exo([
    "<b>Cartographier tes lâchers difficiles.</b> Sur les 7 moments, identifie tes 2-3 plus difficiles. "
    "Pour chacun, écris une stratégie spécifique (technique du lâcher en 6 étapes + action physique "
    "concrète comme fermer la plateforme).",
    "<b>Le journal du lâcher.</b> Chaque session, sur ton journal, une ligne dédiée : « moments où j'ai "
    "lâché aujourd'hui / moments où je n'ai pas lâché ». Tu mesures ta compétence sur 30 jours.",
    "<b>L'engagement opérationnel.</b> Choisis UN seul des 7 moments à travailler intensément pendant 30 "
    "jours. Pas les 7. Un. Tu installes la compétence sur ce moment. Puis tu passes au suivant. "
    "Sur 6 mois, tu auras travaillé tous les moments."
]))
story.extend(phrase("Le lâcher est ma compétence à entraîner. Pas un événement à attendre."))
story.append(PageBreak())


# --- LIVRE 8 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 8", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "Ce à quoi tu résistes persiste. Ce que tu acceptes traverse.",
    "Trois options face à une émotion : supprimer, exprimer, lâcher. Seul lâcher résout.",
    "Le protocole du lâcher en 6 étapes : nommer, localiser, accepter, respirer, attendre, constater.",
    "Une émotion dure 60-90 secondes si elle n'est pas alimentée par résistance.",
    "Le contrôle marche dans les systèmes linéaires. Pas dans les stochastiques.",
    "Acceptation n'est pas résignation — c'est l'arrêt du combat intérieur.",
    "Plus tu serres en trading, plus tu te brûles. Plus tu lâches, plus tu performe.",
    "Le lâcher se pratique dans 7 moments-clés de la journée trading.",
    "Maîtriser le lâcher est une compétence progressive (6-12 mois).",
    "L'acceptation libère l'énergie pour l'action utile.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Combattre une émotion mentalement (résistance = amplification).",
    "Vouloir contrôler ce qui n'est pas contrôlable (marché, autres, résultats).",
    "Supprimer ses émotions (s'accumulent dans le corps).",
    "Exprimer toutes ses émotions impulsivement (renforce le pattern).",
    "Confondre acceptation et résignation.",
    "Croire que lâcher est une faiblesse.",
    "Vouloir lâcher en un événement plutôt qu'en compétence progressive.",
    "Pousser au-delà du TP (refus de lâcher le gain potentiel).",
    "Décaler le SL (refus de lâcher la position).",
    "Refuser d'accepter son état actuel (TBI, patterns, etc.).",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je pratique le protocole de lâcher 1 fois par jour minimum.",
    "Quand une émotion monte, j'observe 90 secondes avant d'agir.",
    "Je distingue domaines linéaires (contrôler) et stochastiques (lâcher).",
    "Je lâche les résultats individuels — je contrôle mes gestes.",
    "Je ferme la plateforme dès que les ordres sont placés.",
    "Au TP atteint, je pratique le lâcher du désir de pousser.",
    "Après une série, j'impose 24h de pause — pas de revanche.",
    "Après un gros gain, j'impose 24h aussi — pas d'euphorie qui pilote.",
    "Je reconnais et accepte les réalités que je refuse silencieusement.",
    "Je traite l'acceptation comme une compétence, pas comme une attitude.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║          LÂCHER PRISE  —  FICHE D'ANCRAGE                ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    Ce à quoi je résiste persiste.                          ║
   ║    Ce que j'accepte traverse.                              ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Contrôler ce qui n'est pas contrôlable.                 ║
   ║    Combattre des émotions au lieu de les laisser passer.   ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE                                           ║
   ║    - Mâchoire serrée pendant un trade                      ║
   ║    - "Je dois absolument..."                               ║
   ║    - Émotion qui dure plus de 5 minutes                    ║
   ║    - Refus mental d'une réalité ("ça devrait pas être")    ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    Protocole 6 étapes :                                    ║
   ║    1. NOMMER l'émotion exactement                          ║
   ║    2. LOCALISER dans le corps                              ║
   ║    3. ACCEPTER (autoriser la présence)                     ║
   ║    4. RESPIRER vers la sensation                           ║
   ║    5. ATTENDRE 60-90 sec                                   ║
   ║    6. CONSTATER la dissolution                             ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je contrôle mes gestes. Je lâche les résultats."       ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    1 pratique du protocole par jour pendant 30 jours.      ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Au TP atteint : protocole 90s, puis couper.             ║
   ║    Au SL approché : close the platform.                    ║
   ║    Après série : 24h de pause, lâcher la revanche.         ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 8 complet (6 modules + synthèse)")


# ============================================================
# LIVRE 9 — LA PSYCHOLOGIE DE L'ARGENT (Morgan Housel)
# ============================================================
_current_book_color[0] = BOOK_COLORS[8]
ACCENT = BOOK_COLORS[8]

story.extend(book_separator_page(
    9, "La psychologie de l'argent", "Morgan Housel", "The Psychology of Money", 2020, ACCENT,
    quote='« Faire de l\'argent est une compétence.<br/>En garder est une autre, très différente. »',
    subtitle="Comportements intemporels en matière de richesse, d'avidité et de bonheur"
))

story.extend(book_intro_header(9, "La psychologie de l'argent", "Morgan Housel — 2020", ACCENT))
story.append(P("A.  Pourquoi ce livre est important pour toi", h_section))
story.append(P(
    "Morgan Housel est ancien chroniqueur du Wall Street Journal et collaborateur de Collaborative Fund. "
    "Ce livre n'est pas un manuel d'investissement — c'est un livre sur le <b>rapport psychologique à "
    "l'argent</b>. Et c'est précisément ton angle mort. Tu sais (intellectuellement) que le trading est "
    "une activité financière. Tu ignores (concrètement) que ton rapport à l'argent est probablement "
    "déréglé bien au-delà du trading."
))
story.append(P(
    "Ce livre adresse une vérité qui dérange tous les traders : <b>faire de l'argent et en garder sont deux "
    "compétences différentes</b>. La première demande optimisme, prise de risque, ambition. La seconde "
    "demande humilité, peur, conservation. Tu es plutôt câblé pour la première. Tu n'as probablement "
    "jamais développé la seconde. C'est pour ça que même les rares fois où tu as bien gagné, tu n'as pas "
    "su garder."
))
story.append(P(
    "Pour ton cas, ce livre clôture la bibliothèque en posant une question qui dépasse le trading : "
    "<b>quel rapport veux-tu construire avec l'argent pour les 30 prochaines années ?</b> Si tu réponds "
    "« faire le max », tu reproduiras tes patterns sur des montants plus grands. Si tu réponds « construire "
    "une liberté », tout change. Housel t'aide à reformuler la question."
))
story.append(P(
    "Lis-le après tout le reste. À ce moment-là, ton rapport à l'argent peut commencer à se reconfigurer "
    "en profondeur — parce que les fondations psychologiques et somatiques sont en place."
))

story.append(P("B.  Résumé global profond", h_section))
story.append(P("La thèse centrale", h_subsection))
story.append(P('<b>L\'argent est avant tout un comportement, pas un calcul. La maîtrise psychologique bat l\'intelligence financière, presque toujours.</b>', pull_quote))
story.append(P(
    "Housel défend l'idée que le succès financier durable a très peu à voir avec l'intelligence, le QI, "
    "la chance technique. Il dépend presque entièrement de <b>comportements simples et reproductibles</b>, "
    "appliqués sur des décennies. Quelqu'un avec un QI moyen et des comportements financiers sains battra "
    "presque toujours quelqu'un avec un QI exceptionnel et des comportements financiers déséquilibrés. "
    "C'est la marche du temps long, pas l'éclat du moment."
))
story.append(P("Les mécanismes exposés", h_subsection))
story.append(P(
    "<b>1. Le rôle massif de la chance et du risque</b> dans les résultats financiers — sous-estimé "
    "systématiquement. On confond souvent succès et compétence. <b>2. La composition du temps long</b> "
    "comme force la plus puissante en finance — ignorée par les traders qui pensent en jours. "
    "<b>3. Faire de l'argent ≠ en garder</b> : deux compétences distinctes qui demandent des mentalités "
    "opposées (optimisme vs paranoïa adaptative). <b>4. La marge de sécurité</b> : laisser de la "
    "place pour l'erreur dans tous tes paris financiers. <b>5. La richesse invisible</b> : la vraie "
    "richesse est ce que tu ne vois pas (ce qui n'est pas dépensé). <b>6. Raisonnable, pas rationnel</b> : "
    "le plan financier doit être tenable émotionnellement, pas optimal mathématiquement. <b>7. Le coût "
    "de la liberté</b> : la liberté de choisir comment tu utilises ton temps est le plus grand luxe "
    "achetable avec l'argent."
))
story.append(P("Les transformations proposées", h_subsection))
story.append(P(
    "<b>Privilégier la durée à l'amplitude</b> : tenir 30 ans avec un système modeste bat exploser 5 ans "
    "avec un système brillant. <b>Construire une marge de sécurité</b> : sur tes positions, sur ton "
    "capital, sur ton temps. <b>Définir « assez »</b> : sans cette définition, tu cours après l'infini "
    "et tu ne t'arrêtes jamais. <b>Acheter du temps libre</b> : la vraie utilité de l'argent est de te "
    "permettre de choisir ce que tu fais de tes journées. <b>Vivre en dessous de tes moyens</b> : "
    "l'épargne est ce qui finance ta liberté future, pas ton statut présent."
))
story.append(P("Les limites du livre", h_subsection))
story.append(P(
    "Housel est principalement orienté investissement long terme (style buy-and-hold), pas trading "
    "actif. Tu vas trouver peu de conseils opérationnels pour ton activité quotidienne. Le livre est "
    "aussi parfois anecdotique et répétitif. Sa vraie valeur pour toi : il pose des questions de fond "
    "(qu'est-ce que tu fais de tout ça ?) que tu n'as probablement jamais posées sérieusement."
))

story.append(P("C.  Carte mentale", h_section))
story.append(Schema(8.5*cm, lambda c, w, h: draw_mindmap(c, w, h,
    "Psychologie de l'argent",
    [
        {"label": "THÈSE", "leaves": ["argent = comportement", "durée > amplitude"], "color": DARK_GREY},
        {"label": "PRINCIPES", "leaves": ["chance + risque", "composition LT", "faire ≠ garder"], "color": ACCENT},
        {"label": "ATTITUDES", "leaves": ["définir assez", "marge sécurité", "acheter du temps"], "color": GREEN},
    ],
    accent=ACCENT
)))
story.append(P("Comportements financiers durables — au-delà du coup.", diagram_caption))
story.append(PageBreak())


# --- MODULE 1 ---
story.extend(module_header(9, 1, "Le rôle massif de la chance et du risque",
    "Pourquoi ton interprétation des résultats est probablement fausse", ACCENT))
story.extend(idee(
    "La chance et le risque sont les forces les plus sous-estimées dans les résultats financiers. Quand "
    "quelqu'un réussit, on attribue son succès à sa compétence. Quand quelqu'un échoue, à ses erreurs. "
    "La réalité est que la chance et le risque jouent un rôle beaucoup plus grand qu'on ne le pense — "
    "dans les deux directions."
))
story.extend(mecan(
    "Le biais cognitif appelé « illusion de contrôle » nous pousse à voir nos résultats comme des conséquences "
    "directes de nos décisions. C'est en partie vrai (les décisions comptent). C'est en partie faux (l'aléa "
    "compte aussi). Quand tu fais +5000€ sur un trade, ce n'est probablement pas 100% ta compétence — c'est "
    "aussi du timing favorable, de la liquidité présente, d'un événement macro non prévu. Quand tu fais "
    "-5000€, ce n'est pas 100% ta faute — c'est aussi un mouvement imprévu, une nouvelle inattendue, etc."
))
story.extend(lien([
    "Pour toi, cette compréhension est libératrice et exigeante en même temps. <b>Libératrice</b> : tu peux "
    "arrêter de te flageller pour chaque perte comme si c'était 100% ta responsabilité. Une partie est "
    "structurelle. <b>Exigeante</b> : tu dois arrêter de te féliciter pour chaque gain comme si c'était "
    "100% ta compétence. Tu en deviens humble face à tes propres victoires.",
    "Cette humilité est cruciale pour ton scaling futur. Beaucoup de traders ont fait des fortunes brèves "
    "sur des coups de chance qu'ils ont attribués à leur compétence — puis ils ont scalé en pensant que "
    "leur compétence reproduirait, et ils ont tout perdu. Ne tombe pas dans ce piège. Quand tu auras "
    "une belle série, attribue lui 50% à ta compétence et 50% à la chance. Tu vas penser que c'est "
    "exagéré. Ce ne l'est pas."
]))
story.extend(exemple([
    "<b>Saboteur (interprétation chance/risque) :</b> tu fais 3 trades gagnants d'affilée. Tu te dis « j'ai "
    "trouvé la formule. Je passe en taille x2. » Le 4e est perdant. Le 5e aussi. Tu te dis « j'ai perdu la "
    "main ». Sur 5 trades, tu as confondu chance et compétence dans les deux sens.",
    "<b>Cible :</b> 3 trades gagnants. Tu te dis « bonne série. C'est dans la distribution. Je maintiens ma "
    "taille — la prochaine peut être perdante. Je n'augmente pas sur base d'échantillon. » Le 4e perdant. "
    "« Normal — c'est dans la distribution. Je continue. » Tu joues la durée, pas l'amplitude."
]))
story.extend(exo([
    "<b>Audit des 10 derniers gros gains et 10 dernières grosses pertes.</b> Pour chaque, estime "
    "honnêtement le % de compétence vs % de chance/risque externe. Tu vas être surpris.",
    "<b>Règle d'humilité.</b> Après chaque grosse série gagnante (3-5 trades), tu ne changes pas ta taille "
    "pendant 7 jours. Tu laisses la chance s'estomper pour voir ta compétence vraie.",
    "<b>Phrase pré-décision.</b> Avant chaque décision de scaling : « est-ce que je base sur de la compétence "
    "démontrée sur 100 trades minimum, ou sur une série récente ? »"
]))
story.extend(phrase("Mes résultats sont moi + chance + risque. Je suis humble dans les deux directions."))
story.append(PageBreak())


# --- MODULE 2 ---
story.extend(module_header(9, 2, "La puissance de la composition long terme",
    "L'arme la plus sous-utilisée par les traders", ACCENT))
story.extend(idee(
    "La composition (intérêts composés appliqués sur le long terme) est la force la plus puissante en "
    "finance. Quelqu'un qui gagne 10% par an pendant 30 ans devient riche. Quelqu'un qui essaie de "
    "gagner 30% par an pendant 5 ans, en prenant les risques associés, finit le plus souvent ruiné. "
    "Le secret n'est pas l'amplitude — c'est la <b>durée</b>."
))
story.extend(mecan(
    "Mathématiquement : 100€ à 10% / an pendant 30 ans = 1745€ (par effet composé). 100€ à 10% pendant 5 ans = "
    "161€. Le facteur durée est >10x plus puissant que le facteur amplitude pour un effort équivalent. "
    "Cette logique est contre-intuitive parce que l'humain pense linéairement. Mais c'est ce qui sépare "
    "Warren Buffett des autres : la majorité de sa fortune a été construite après ses 60 ans, par "
    "composition pure sur des décennies. Ce n'est pas son génie technique. C'est sa durée d'exposition."
))
story.extend(lien([
    "Pour toi, c'est <b>la</b> leçon. Tu fonctionnes en mode « cours après l'amplitude » : tu veux les gros "
    "gains rapidement, les comptes funded rapidement, le scaling rapide. Cette mentalité te disqualifie "
    "automatiquement de la composition long terme. Le trader rentable et durable n'est pas celui qui fait "
    "3% par jour pendant 6 mois puis crame. C'est celui qui fait 1-2% par mois pendant 20 ans.",
    "Concrètement : si tu maîtrises ton edge et ton comportement, et que tu produis 1% par mois moyen sur "
    "30 ans avec un capital initial modeste, tu construis une fortune énorme. Sur 30 ans, 1% par mois "
    "= multiplication par environ 35. 10 000€ deviennent 350 000€. 30 000€ deviennent 1 050 000€. "
    "C'est lent, c'est ennuyeux, c'est rarement glamour — c'est ce qui marche.",
    "Mais surtout : 1% par mois est <b>atteignable</b> par un trader rigoureux. 30% par mois est "
    "<b>insoutenable</b> sur la durée. Le piège : viser 30% te fait souvent finir avec moins que ce que "
    "1% aurait produit."
]))
story.extend(exemple([
    "<b>Saboteur :</b> tu vises 50% sur le compte funded en 2 mois pour passer en payout maximal. Tu prends "
    "des risques qui rendent ça possible. Tu cramés le compte. Tu repars à zéro. Année après année, tu "
    "stagnes au même endroit.",
    "<b>Cible :</b> tu vises 1% par semaine. Soit ~4% par mois. Soit ~60% par an composé. C'est ÉNORME en "
    "rendement annuel — bien au-dessus de tous les fonds professionnels. C'est aussi atteignable avec un "
    "edge propre exécuté discipliné. Sur 10 ans : 60% par an compose = multiplication par environ 100. "
    "Tu construis vraiment."
]))
story.extend(exo([
    "<b>Calculer ton chemin de composition.</b> Avec ton capital actuel, fais le calcul : si je fais 1% par "
    "semaine en moyenne pendant 10 ans, je termine à combien ? Le résultat va te ramener à la modestie "
    "des bons rendements.",
    "<b>Re-paramétrage des objectifs.</b> Définis des objectifs en termes de COMPOSITION, pas d'amplitude. "
    "« Faire 0,5% à 1% par semaine, en moyenne, sur 12 mois consécutifs. » Cet objectif te protège des "
    "comportements destructeurs.",
    "<b>L'engagement de durée.</b> Décide aujourd'hui que tu trades comme métier sérieux pendant AU MOINS "
    "10 ans. Pas 2 ans pour faire fortune et arrêter. 10 ans minimum. Cet horizon change tout : il rend "
    "le 1% par semaine séduisant et le 30% par mois absurde."
]))
story.extend(phrase("La durée bat l'amplitude. Je joue 30 ans, pas 30 jours."))
story.append(PageBreak())


# --- MODULE 3 ---
story.extend(module_header(9, 3, "Faire de l'argent ≠ en garder",
    "Deux compétences opposées que tu dois cumuler", ACCENT))
story.extend(idee(
    "Faire de l'argent demande une mentalité : optimisme, prise de risque, conviction, ambition. "
    "En garder demande la mentalité inverse : humilité, peur, conservation, paranoïa adaptative. "
    "Très peu de gens cumulent les deux. La plupart des fortunes faites sont reperdues parce que les "
    "détenteurs n'ont jamais développé la deuxième compétence."
))
story.extend(mecan(
    "Optimisme et paranoïa ne cohabitent pas naturellement dans le même cerveau. Si tu es trop optimiste, "
    "tu prends des risques qui te ruinent. Si tu es trop paranoïaque, tu ne prends pas les risques qui "
    "construisent. La maîtrise est de cultiver les deux <b>séquentiellement</b> selon le contexte : "
    "optimiste quand tu prends position, paranoïaque quand tu protèges les gains."
))
story.extend(lien([
    "Toi, tu es <b>très optimiste</b> dans ta personnalité de trader. Tu prends des risques. Tu pousses. "
    "Tu pyramides parfois. Tu vises grand. Cette compétence est utile — elle te permet d'entrer dans le "
    "jeu et d'y rester émotionnellement. Mais tu n'as <b>presque aucune</b> compétence de paranoïa "
    "adaptative — tu ne sais pas protéger ce que tu as. Tu ne dévalues pas le capital existant. Tu n'as "
    "pas de stratégies de sortie quand tu es en gain. Tu ne mets pas d'argent de côté pour les périodes "
    "difficiles. Tu fonctionnes en mode « tout ou rien ».",
    "Cette asymétrie te garantit de ne jamais construire durablement. Même si tu fais 100 000€ en 6 mois, "
    "sans la compétence de garder, tu en aura perdu 90 000 dans les 6 mois suivants. La compétence de "
    "garder s'apprend, mais elle demande un travail mental dirigé."
]))
story.append(P("Les comportements de garder", h_subsection))
story.append(styled_table([
    [C("Comportement", cell_gold), C("Description", cell_gold)],
    [C("Sortir une partie des gains", cell_bold),
     C("Toutes les semaines / mois, retirer une part fixe du compte trading vers un compte sécurisé. Ce qui est sorti ne peut plus être perdu en trading.")],
    [C("Définir un seuil de réussite", cell_bold),
     C("« Au-dessus de X dans le compte, je sors le surplus. » Tu plafonnes ton exposition au risque de perte.")],
    [C("Construire un coussin de sécurité", cell_bold),
     C("3-6 mois de dépenses courantes sur compte épargne, indépendant du trading. Sans ce coussin, chaque perte est existentielle.")],
    [C("Diversifier ailleurs", cell_bold),
     C("ATHÉNA, immobilier, fonds indiciels, etc. Tu n'as pas tous tes œufs dans le panier trading.")],
    [C("Ne pas augmenter ton mode de vie", cell_bold),
     C("Quand tu gagnes plus, tu n'augmentes PAS proportionnellement tes dépenses. La différence va à l'épargne et l'investissement.")],
], [4*cm, 12*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu gagnes 8000€ sur 2 mois. Tu te dis « c'est cool, ça va continuer ». Tu achètes "
    "un nouveau matériel ATHÉNA premium, tu sors plus, tu prends une selle plus chère. Tu ne mets rien "
    "de côté. Mois 3, tu perds 5000€. Tu te retrouves avec moins de marge financière qu'avant la série "
    "gagnante.",
    "<b>Cible :</b> tu gagnes 8000€ en 2 mois. Tu te dis « belle série, à protéger ». Tu retires 50% du "
    "gain (4000€) vers un compte épargne séparé. Tu maintiens ton mode de vie. Tu utilises peut-être "
    "1500€ pour une chose qui compte vraiment. Tu gardes 2500€ comme tampon dans le compte trading. "
    "Tu protèges ce qui a été gagné. Tu construis."
]))
story.extend(exo([
    "<b>Le compte épargne dédié.</b> Cette semaine : ouverture d'un compte épargne (livret A ou LDDS) "
    "DÉDIÉ au surplus du trading. Aucun virement sortant possible pendant 12 mois (mentalement).",
    "<b>La règle des 50/30/20 du gain mensuel.</b> Sur tout gain mensuel net en trading : 50% reste en "
    "compte trading (capitalisation), 30% va à l'épargne dédiée, 20% au plaisir/qualité de vie. Pourcentages "
    "fixes, pas négociables.",
    "<b>Le seuil de prélèvement.</b> Définis un seuil au-dessus duquel tu prélèves automatiquement. "
    "Exemple : « au-dessus de 15 000€ dans le compte funded, je prélève le surplus mensuellement ». "
    "Cette règle automatique te protège de toi-même."
]))
story.extend(phrase("Faire de l'argent et le garder sont deux compétences. Je les développe en parallèle."))
story.append(PageBreak())


# --- MODULE 4 ---
story.extend(module_header(9, 4, "Définir « assez »",
    "La question que tu n'as jamais posée sérieusement", ACCENT))
story.extend(idee(
    "Sans définition explicite de ce qui constitue « assez » pour toi, tu cours après l'infini. Et l'infini "
    "ne s'attrape jamais. Tu peux multiplier ton capital par 10, par 100, par 1000 — sans définition de "
    "« assez », tu ressentiras toujours un manque. Cette absence de définition est l'origine de la "
    "majorité des comportements destructeurs des traders qui gagnent."
))
story.extend(mecan(
    "L'humain est câblé pour la comparaison sociale et l'adaptation hédonique. Quel que soit ton niveau "
    "de richesse, tu te compares à un référent plus élevé et tu t'adaptes rapidement à ton niveau actuel. "
    "Conséquence : sans cible définie consciemment, tu ressens un déficit permanent. Pour sortir de cette "
    "trappe, tu dois définir <b>en avance</b>, à froid, ce qui constitue « assez » dans ta vie. Cette "
    "définition devient ton point d'ancrage. Tu sais quand tu y es arrivé."
))
story.extend(lien([
    "Toi, tu n'as probablement aucune définition claire de « assez ». Si on te demande « quel niveau de "
    "compte / patrimoine / revenu serait suffisant pour que tu ressentes que tu as gagné », ta réponse "
    "est probablement vague ou ne vient pas. Cette absence garantit que tu ne ressentiras jamais d'avoir "
    "gagné — quel que soit le montant atteint.",
    "Pour construire cette définition, tu dois te poser des questions concrètes : combien je dépense par "
    "mois pour vivre comme je veux vivre ? Combien me faut-il en capital pour que ce mode de vie soit "
    "financé par mes investissements sans avoir à trader pour vivre ? À ce niveau, je peux trader pour "
    "le plaisir et la croissance, pas pour la survie."
]))
story.append(P("Le calcul de ton « assez »", h_subsection))
story.append(styled_table([
    [C("Question", cell_gold), C("À te poser honnêtement", cell_gold)],
    [C("Dépenses mensuelles", cell_bold),
     C("Combien je dépense en moyenne par mois pour vivre comme je veux vivre ? (Loyer + charges + nourriture + chevaux + équitation + ATHÉNA + plaisirs + provisions). Honnêtement.")],
    [C("Multiplicateur", cell_bold),
     C("La règle standard est 25-30x les dépenses annuelles. Permet un retrait de 3-4% par an sans toucher au capital.")],
    [C("Capital cible", cell_bold),
     C("Dépenses annuelles × 25-30. C'est ton « assez ».")],
    [C("Délai réaliste", cell_bold),
     C("À quel horizon je peux y arriver ? 10 ans ? 15 ans ? Pose un délai réaliste en fonction de ton edge réel.")],
    [C("Plan", cell_bold),
     C("Combien je dois épargner et investir par mois pour y arriver dans ce délai ?")],
], [3.5*cm, 12.5*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu trades sans cible. Tu te dis « je veux gagner beaucoup ». Tu fais 5000€ en un mois. "
    "Tu ne ressens pas que c'est « assez » parce que tu n'as jamais défini « assez ». Tu vises 10 000€ "
    "le mois suivant. Tu prends plus de risques. Tu cramés.",
    "<b>Cible :</b> tu fais le calcul. Dépenses mensuelles 3000€. Annuelles 36 000€. Capital cible 900 000€ "
    "à 1 100 000€. À atteindre en 15 ans. Soit besoin d'épargner/investir ~3000€ par mois en moyenne. "
    "Soudain, tu sais ce que tu vises. Quand tu fais 5000€ en un mois, tu sais que 3000 vont à l'objectif "
    "et 2000 sont du surplus. Tu trades sans la pression de l'infini."
]))
story.extend(exo([
    "<b>Le calcul de ton « assez ».</b> Cette semaine, prends 1 heure pour faire le calcul complet. "
    "Écris-le. C'est ton point d'ancrage à vie.",
    "<b>L'évaluation mensuelle.</b> Chaque fin de mois, calcule où tu en es par rapport à ton objectif. "
    "Tu vois la composition s'accumuler. Tu sais que tu avances.",
    "<b>Le test de la liberté.</b> Demande-toi : « si j'avais atteint mon &laquo;assez&raquo; demain, "
    "qu'est-ce que je ferais de ma vie ? » Si la réponse est « la même chose » ou « je sais pas », tu es "
    "en train de fuir une vie que tu n'as pas conçue. C'est la vraie question derrière l'argent."
]))
story.extend(phrase("Sans « assez » défini, je cours après l'infini. Je définis. Je sais où je vais."))
story.append(PageBreak())


# --- MODULE 5 ---
story.extend(module_header(9, 5, "La marge de sécurité",
    "Laisser de la place pour ce que tu ne prévois pas", ACCENT))
story.extend(idee(
    "La marge de sécurité est l'écart entre ton niveau d'engagement et ta capacité réelle à absorber un "
    "choc. Plus la marge est grande, plus tu survis aux mauvaises surprises. La majorité des faillites "
    "vient non pas d'erreurs spécifiques, mais d'<b>absence de marge</b> qui transforme une petite "
    "erreur en catastrophe."
))
story.extend(mecan(
    "L'univers est plus imprévisible que tes modèles ne le supposent. Un événement « impensable » arrive "
    "à peu près tous les 10 ans en finance (1987, 2000, 2008, 2020). Si ta marge de sécurité ne tient "
    "qu'en conditions normales, tu seras balayé lors d'un événement extrême. La marge de sécurité protège "
    "contre l'inconnu. Elle te coûte un peu de performance en conditions normales — c'est la prime "
    "d'assurance que tu paies."
))
story.extend(lien([
    "Pour toi, plusieurs niveaux de marge à construire. <b>Marge sur les positions individuelles</b> : "
    "risque par trade ≤ 0,5-1% du compte (pas 2-3% comme tu fais peut-être). <b>Marge sur le drawdown</b> : "
    "stop trading à -5% du compte (sortie obligatoire, pas négociable). <b>Marge sur le capital total</b> : "
    "ne mets jamais 100% de ton argent disponible en trading. <b>Marge sur les revenus</b> : ne dépends "
    "pas du trading pour payer ton loyer. <b>Marge sur le temps</b> : ne te mets pas en situation où tu "
    "DOIS gagner cette semaine.",
    "Le principe Housel : « il vaut mieux être à peu près correct avec une marge qu'exactement correct sans "
    "marge ». Tu peux avoir raison sur l'analyse mais tort sur le timing — la marge te permet de survivre "
    "à ce décalage."
]))
story.append(P("Les 5 marges à construire", h_subsection))
story.append(styled_table([
    [C("Marge", cell_gold), C("Norme habituelle", cell_gold), C("Marge sécurisée", cell_gold)],
    [C("Risque par trade", cell_bold),
     C("2-3% du compte"),
     C("0,5-1% du compte")],
    [C("Drawdown max session", cell_bold),
     C("Pas de limite"),
     C("-3% : arrêt immédiat de la journée")],
    [C("Drawdown max compte", cell_bold),
     C("Limite prop firm uniquement"),
     C("-7-10% personnel : suspension du compte 30 jours")],
    [C("Capital exposé au trading", cell_bold),
     C("100% du capital disponible"),
     C("≤ 25-40% du capital total")],
    [C("Coussin de sécurité", cell_bold),
     C("0 mois de dépenses"),
     C("6-12 mois de dépenses sur compte séparé")],
], [4*cm, 5*cm, 7*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu trades avec 100% de ton capital disponible. Tu risques 3% par trade. Tu n'as "
    "aucun coussin de sécurité. Un drawdown de 30% (qui arrive à tout trader sur un horizon de 5-10 ans) "
    "te met en situation existentielle. Tu prends des décisions désespérées pour te refaire. Tu cramés.",
    "<b>Cible :</b> tu trades avec 30% de ton capital total. Tu risques 0,75% par trade. Tu as 8 mois de "
    "dépenses en coussin sur un compte séparé. Un drawdown de 30% sur ton capital trading représente seulement "
    "9% de ton patrimoine total. Tu peux le traverser sereinement. Tu prends des décisions calmes. "
    "Tu te refais avec le temps. Tu ne cramés pas."
]))
story.extend(exo([
    "<b>L'audit des 5 marges.</b> Pour chaque marge, note où tu es aujourd'hui et où tu devrais être. "
    "Identifie les 1-2 plus à risque. Plan de mise à niveau sur 6 mois.",
    "<b>La règle du coussin.</b> Avant toute prise de risque significative en trading, exige de toi un "
    "coussin de sécurité de 6 mois minimum. Sans ce coussin, tu trades en mode survie — donc émotionnel.",
    "<b>La diversification de revenus.</b> Le trading ne doit pas être ta seule source de revenu. Construis "
    "ATHÉNA en parallèle, prends des contrats équestres, varie. Chaque source autonome augmente ta marge "
    "et réduit ta charge émotionnelle pendant les phases difficiles."
]))
story.extend(phrase("La marge de sécurité est ma prime d'assurance contre l'imprévisible. Je la paie sans regret."))
story.append(PageBreak())


# --- MODULE 6 ---
story.extend(module_header(9, 6, "Acheter du temps",
    "La vraie utilité de l'argent que tu n'as pas identifiée", ACCENT))
story.extend(idee(
    "L'argent a une valeur d'usage qui dépasse largement les biens qu'il permet d'acheter. Sa valeur "
    "la plus précieuse est <b>la liberté de choisir comment tu utilises ton temps</b>. Pouvoir dire non "
    "à un travail qui ne te plaît plus. Pouvoir consacrer 3 mois à un projet sans pression financière. "
    "Pouvoir dormir quand tu es fatigué. Cette liberté est ce qui distingue richesse vécue et richesse "
    "comptable."
))
story.extend(mecan(
    "Les humains sont mauvais à prédire ce qui les rendra heureux. Ils accumulent des biens (voitures, "
    "maisons, statut) qui produisent de l'adaptation hédonique rapide (le plaisir s'éteint en quelques mois). "
    "Ils ignorent ce qui produit de la satisfaction durable : autonomie, sens, relations, présence. "
    "L'argent investi dans le temps libre (vacances, choix de carrière, équilibre vie pro / vie perso) "
    "produit des rendements de bonheur très supérieurs à l'argent investi dans les biens."
))
story.extend(lien([
    "Pour toi à 25 ans, c'est crucial. Si tu construis une fortune à 40 ans en sacrifiant 15 ans de "
    "temps libre, en n'allant pas en compétition équestre, en ne nourrissant pas ATHÉNA pour ses qualités "
    "propres, en n'investissant pas dans ta relation à ta filly, etc. — ces 15 ans ne reviendront pas. "
    "L'argent gagné ne pourra pas les racheter.",
    "À l'inverse, si tu choisis dès maintenant de construire une vie qui mêle progression financière "
    "raisonnable ET temps de qualité, tu cumules les deux. C'est plus lent pour l'argent. C'est immensément "
    "plus riche pour la vie. À 40 ans, tu auras un patrimoine moindre que dans le scénario sacrificiel — "
    "mais tu auras 15 ans de vie pleinement vécue derrière toi. Ce ratio est presque toujours en faveur "
    "de la deuxième option, comme le démontrent les recherches sur le bonheur."
]))
story.append(P("Le temps comme actif", h_subsection))
story.append(styled_table([
    [C("Dépense d'argent", cell_gold), C("Rendement bonheur", cell_gold)],
    [C("Voiture premium", cell_bold), C("Faible. Adaptation en 3-6 mois.")],
    [C("Maison plus grande", cell_bold), C("Faible. Adaptation en 6-12 mois.")],
    [C("Statut social (marque, restaurant)", cell_bold), C("Très faible. Adaptation en jours.")],
    [C("Temps libre supplémentaire", cell_bold), C("Très fort. Pas d'adaptation.")],
    [C("Expériences avec proches", cell_bold), C("Très fort. Renforcé par la mémoire.")],
    [C("Liberté de choix professionnel", cell_bold), C("Très fort. Permanent.")],
    [C("Santé (sport, qualité de vie)", cell_bold), C("Très fort. Cumulé.")],
    [C("Apprentissage / développement", cell_bold), C("Fort. Cumulé.")],
], [7*cm, 9*cm]))
story.append(Spacer(1, 8))
story.extend(exemple([
    "<b>Saboteur :</b> tu gagnes 6000€ ce mois. Tu décides « je vais m'offrir une montre ». Tu paies 4500€ "
    "pour la montre. Tu ressens un pic de plaisir 3 jours. Puis tu t'y habitues. La montre devient "
    "ordinaire. Tu as échangé 4500€ contre 3 jours de plaisir.",
    "<b>Cible :</b> tu gagnes 6000€. Tu retires 50% (3000€) vers ton compte épargne stratégique. "
    "Tu utilises 1500€ pour une expérience qui compte : 4 jours en montagne avec un proche, un stage "
    "intensif d'équitation avec un grand maître, une thérapie SE qui te transforme. Tu gagnes du "
    "patrimoine ET de la mémoire / compétence. Les deux capitalisent."
]))
story.extend(exo([
    "<b>L'audit des dépenses de l'année.</b> Liste tes 10 plus grosses dépenses de l'année (hors charges "
    "fixes). Pour chaque, évalue 1-10 ton rendement bonheur 6 mois après. Tu vas voir qu'une majorité "
    "était un mauvais investissement de bonheur.",
    "<b>La règle « temps avant chose ».</b> Pendant les 12 prochains mois, prioritise toute dépense "
    "discrétionnaire vers les catégories à fort rendement bonheur (temps libre, expériences, santé, "
    "relations, apprentissage). Évite les catégories à faible rendement (statut, biens, accumulation).",
    "<b>La projection à 80 ans.</b> Imagine-toi à 80 ans. Qu'est-ce que tu regretteras d'avoir fait ? "
    "De ne pas avoir fait ? Cette projection oriente tes choix d'aujourd'hui mieux que n'importe quel "
    "calcul financier."
]))
story.extend(phrase("L'argent gagne sa valeur quand il achète du temps, du sens, de la liberté. Pas des choses."))
story.append(PageBreak())


# --- LIVRE 9 SYNTHÈSE ---
story.append(P("E.  Synthèse complète — Livre 9", h_section))

story.append(P("Les 10 idées clés", h_subsection))
for i, idea in enumerate([
    "L'argent est comportement, pas calcul. La maîtrise psychologique bat l'intelligence financière.",
    "Chance et risque jouent un rôle massif. Sois humble dans les deux directions.",
    "La composition long terme est l'arme la plus puissante. La durée bat l'amplitude.",
    "Faire de l'argent et le garder sont 2 compétences distinctes. Cumule les deux.",
    "Sans définition de « assez », tu cours après l'infini.",
    "La marge de sécurité est ta prime d'assurance contre l'inconnu.",
    "La vraie utilité de l'argent : acheter du temps, du sens, de la liberté.",
    "Adaptation hédonique : les biens cessent de produire du plaisir rapidement.",
    "Raisonnable bat rationnel : ton plan financier doit être tenable émotionnellement.",
    "Vivre en dessous de tes moyens finance ta liberté future.",
], 1):
    story.append(P(f"<b>{i}.</b> {idea}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 erreurs à arrêter", h_subsection))
for i, err in enumerate([
    "Confondre série gagnante et compétence acquise.",
    "Viser l'amplitude au lieu de la durée.",
    "Croire que faire de l'argent suffit (sans apprendre à garder).",
    "Trader sans définition de « assez ».",
    "Vivre sans marge de sécurité.",
    "Acheter des biens pour ressentir de la richesse.",
    "Augmenter le mode de vie proportionnellement aux gains.",
    "Tout mettre dans le trading (pas de diversification).",
    "Ignorer le temps comme actif principal.",
    "Optimiser le rendement au détriment de la tenabilité.",
], 1):
    story.append(P(f"<b>{i}.</b> {err}", body))
story.append(Spacer(1, 6))

story.append(P("Les 10 nouvelles règles", h_subsection))
for i, rule in enumerate([
    "Je calcule mon « assez » et je le pose comme objectif.",
    "Je joue 30 ans, pas 30 jours. Engagement de durée.",
    "Je retire 30-50% des gains mensuels vers un compte séparé.",
    "Je risque 0,5-1% par trade maximum.",
    "Je maintiens un coussin de 6-12 mois de dépenses, séparé du trading.",
    "Je diversifie : trading + ATHÉNA + investissements long terme.",
    "Je n'augmente pas mon mode de vie en parallèle des gains.",
    "Je dépense pour du temps et des expériences, pas pour du statut.",
    "Je définis 1 priorité non-trading par trimestre (relation, santé, apprentissage).",
    "Je relis mes objectifs financiers chaque mois et ajuste si besoin.",
], 1):
    story.append(P(f"<b>{i}.</b> {rule}", body))
story.append(Spacer(1, 12))

story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║      LA PSYCHOLOGIE DE L'ARGENT  —  FICHE D'ANCRAGE      ║
   ║                                                            ║
   ║  IDÉE CENTRALE                                             ║
   ║    L'argent est comportement. La durée bat l'amplitude.    ║
   ║    Je définis "assez". Je construis pour 30 ans.           ║
   ║                                                            ║
   ║  DANGER PRINCIPAL                                          ║
   ║    Course à l'infini sans cible. Vivre au niveau des gains.║
   ║    Confondre série de chance et compétence.                ║
   ║                                                            ║
   ║  SIGNAL D'ALERTE                                           ║
   ║    - Aucun montant ne te semble "assez"                    ║
   ║    - Tu réinvestis 100% des gains en trading               ║
   ║    - Tes dépenses suivent tes revenus exactement           ║
   ║    - Pas de coussin de sécurité                            ║
   ║                                                            ║
   ║  NOUVELLE RÉPONSE                                          ║
   ║    1. Calculer "assez" : dépenses annuelles × 25-30        ║
   ║    2. Sortir 30-50% des gains mensuels                     ║
   ║    3. Maintenir 6-12 mois de dépenses en coussin           ║
   ║    4. Diversifier (trading + ATHÉNA + investissements LT)  ║
   ║    5. Privilégier temps et expériences sur biens           ║
   ║                                                            ║
   ║  PHRASE D'ANCRAGE                                          ║
   ║    "Je joue 30 ans, pas 30 jours."                         ║
   ║                                                            ║
   ║  EXERCICE IMMÉDIAT                                         ║
   ║    Calculer mon "assez" complet cette semaine.             ║
   ║    Ouvrir le compte épargne séparé.                        ║
   ║                                                            ║
   ║  APPLICATION TRADING                                       ║
   ║    Objectif : 0,5-1% par semaine en moyenne sur 12 mois.   ║
   ║    Non : 30% par mois ambitieux mais insoutenable.         ║
   ║    Retrait automatique mensuel vers épargne.               ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=ACCENT))

story.append(PageBreak())

print("✓ Livre 9 complet (6 modules + synthèse)")


# ============================================================
# CONCLUSION GÉNÉRALE — INTÉGRATION DES 9 LIVRES
# ============================================================
_current_book_color[0] = GOLD

story.append(P("CONCLUSION GÉNÉRALE", h_book))
story.append(P("Intégrer les 9 livres dans une vie", h_book_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Si tu as lu jusqu'ici, tu portes maintenant en toi un système de pensée et de pratique qui couvre "
    "9 dimensions du même problème : ton rapport à toi-même, à ton corps, à tes émotions, à ton mental, "
    "à tes habitudes, à ton argent. Aucun livre seul ne te transforme. C'est l'<b>intégration</b> des "
    "9 qui peut produire un changement réel."
))
story.append(P(
    "Mais l'intégration ne se fait pas en lisant. Elle se fait en <b>vivant les 9 livres au quotidien</b>, "
    "sur des années. Voici comment articuler le tout pour que cela devienne réalité, pas connaissance."
))

story.append(P("La cartographie d'intégration — qui répond à quoi", h_section))
story.append(styled_table([
    [C("Ton problème", cell_gold), C("Le livre qui répond en premier", cell_gold), C("Les livres qui complètent", cell_gold)],
    [C("Pattern +1500 (technique)", cell_bold), C("Best Loser Wins (1)"), C("Trader dans la zone (5)")],
    [C("Besoin d'intensité, addiction", cell_bold), C("Un monde sous dopamine (2)"), C("Lâcher prise (8)")],
    [C("Système nerveux dérégulé TBI", cell_bold), C("Le corps n'oublie rien (3)"), C("Réveiller le tigre (4)")],
    [C("Décharge corporelle traumatique", cell_bold), C("Réveiller le tigre (4)"), C("Le corps n'oublie rien (3)")],
    [C("Erreurs mentales en trade", cell_bold), C("Trader dans la zone (5)"), C("Best Loser Wins (1)")],
    [C("Suppression émotionnelle, surcharge", cell_bold), C("Quand le corps dit non (6)"), C("Lâcher prise (8)")],
    [C("Difficulté à installer routines", cell_bold), C("Un rien peut tout changer (7)"), C("(tous, en application)")],
    [C("Crispation / contrôle excessif", cell_bold), C("Lâcher prise (8)"), C("Réveiller le tigre (4)")],
    [C("Rapport flou à l'argent / à la durée", cell_bold), C("Psychologie de l'argent (9)"), C("Atomic Habits (7)")],
], [5*cm, 5.5*cm, 5.5*cm]))
story.append(Spacer(1, 12))

story.append(P("Plan d'intégration sur 12 mois", h_section))
story.append(P(
    "Voici un plan calibré pour transformer ce manuel en pratique réelle, sans te surcharger. Le rythme "
    "est volontairement lent pour que chaque acquis s'installe avant le suivant. Si tu suis ce plan, "
    "tu seras un autre Marien fin avril 2027."
))
story.append(styled_table([
    [C("Mois", cell_gold), C("Livre focus", cell_gold), C("Pratique principale à installer", cell_gold)],
    [C("M1-M2", cell_bold), C("Livre 1 — Best Loser Wins"),
     C("Inventaire des patterns. Journal manuscrit lancé. Phrase d'ancrage quotidienne.")],
    [C("M3", cell_bold), C("Livre 2 — Dopamine"),
     C("Sevrage trading 4 semaines. Cold shower quotidien. Sport 3x/sem.")],
    [C("M4", cell_bold), C("Livre 3 — Body Keeps the Score"),
     C("Praticien somatique (SE / EMDR) trouvé. Pansage conscient hebdo. Scan corporel quotidien.")],
    [C("M5", cell_bold), C("Livre 4 — Réveiller le tigre"),
     C("Pratique SE quotidienne. SIBAM pour chaque état confus.")],
    [C("M6", cell_bold), C("Livre 5 — Trader dans la zone"),
     C("Récitation 5 vérités. Reformulation probabiliste. Inventaire des 4 peurs.")],
    [C("M7", cell_bold), C("Livre 6 — Quand le corps dit non"),
     C("5 non par semaine. Jour OFF hebdomadaire non négociable. Quart d'heure émotionnel quotidien.")],
    [C("M8", cell_bold), C("Livre 7 — Atomic Habits"),
     C("Architecture d'habitudes. Empilement. Suivi visuel. Une habitude par mois.")],
    [C("M9-M10", cell_bold), C("Livre 8 — Lâcher prise"),
     C("Protocole 6 étapes quotidien. Lâcher au TP, au SL, après pertes/gains.")],
    [C("M11-M12", cell_bold), C("Livre 9 — Psychologie de l'argent"),
     C("Calcul de « assez ». Compte épargne dédié. Plan d'investissement 30 ans.")],
], [1.5*cm, 5.5*cm, 9*cm]))
story.append(Spacer(1, 12))

story.append(P("Les 9 phrases d'ancrage — à imprimer ensemble", h_section))
story.extend(ascii_schema("""
   ╔══════════════════════════════════════════════════════════╗
   ║              LES 9 PHRASES D'ANCRAGE                      ║
   ║                                                            ║
   ║  L1.  "Je joue 100 trades. Je suis le casino,             ║
   ║        pas le joueur."                                     ║
   ║                                                            ║
   ║  L2.  "Chaque pic produit un creux. Je suis le protocole,  ║
   ║        pas mon envie."                                     ║
   ║                                                            ║
   ║  L3.  "Je soigne par le corps. C'est là que c'est stocké." ║
   ║                                                            ║
   ║  L4.  "Goutte par goutte. Mon corps se libère              ║
   ║        à son rythme."                                      ║
   ║                                                            ║
   ║  L5.  "Je pense en probabilités. Pas en certitudes."       ║
   ║                                                            ║
   ║  L6.  "Je vaux. Indépendamment de ce que je produis."      ║
   ║                                                            ║
   ║  L7.  "1% par jour. Pendant 365 jours."                    ║
   ║                                                            ║
   ║  L8.  "Je contrôle mes gestes. Je lâche les résultats."    ║
   ║                                                            ║
   ║  L9.  "Je joue 30 ans, pas 30 jours."                      ║
   ║                                                            ║
   ║  RECETTE                                                   ║
   ║    1 phrase / jour, le matin.                              ║
   ║    Tu tournes sur les 9 toutes les 9 jours.                ║
   ║    Sur 12 mois, chaque phrase est intégrée                 ║
   ║    ~40 fois.                                               ║
   ╚══════════════════════════════════════════════════════════╝
""", accent=GOLD))

story.append(P("Dernier mot", h_section))
story.append(P(
    "Tu as 25 ans. Tu as un coma derrière toi, un système nerveux qui se reconstruit, une intelligence "
    "rare, une ambition intacte, et désormais 9 livres qui composent ensemble un système de transformation. "
    "Ce système ne marchera que si tu l'habites, pas si tu le consultes."
))
story.append(P(
    "Si à la fin de 2027, tu as travaillé ce manuel jour après jour, lentement, sans drame ni renoncement, "
    "tu seras un autre. Pas un trader plus performant — un Marien plus complet, plus calme, plus puissant, "
    "plus libre. Le trading suivra. Le reste suivra. Mais l'ordre compte : c'est toi qui changes, et tout "
    "le reste découle de ce changement."
))
story.append(P(
    "Bonne route. Le travail commence aujourd'hui — par 2 minutes de respiration après ton café.", body_italic
))

story.append(Spacer(1, 24))
story.append(P("— Fin du manuel d'étude —",
    ParagraphStyle("end", fontName="DejaVu-Italic", fontSize=11,
        textColor=MID_GREY, alignment=TA_CENTER)))


# ============================================================
# BUILD
# ============================================================
def on_first_page(canv, doc): cover_page(canv, doc)
def on_later_pages(canv, doc): standard_page(canv, doc)

doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)
print(f"✓ PDF généré : {OUTPUT}")
