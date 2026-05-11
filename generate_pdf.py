# -*- coding: utf-8 -*-
"""
Génération du PDF coaching personnalisé pour Marien.
Application des concepts de "Best Loser Wins" (Tom Hougaard).
Tout le contenu est paraphrasé/transformé — pas de citations longues.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
    KeepTogether, Flowable
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# ---------- FONTS ----------
pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Italic", "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Serif", "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Serif-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily
registerFontFamily("DejaVu", normal="DejaVu", bold="DejaVu-Bold", italic="DejaVu-Italic")

# ---------- COULEURS ----------
GOLD       = HexColor("#D4AF37")
GOLD_SOFT  = HexColor("#B8962E")
DARK_BG    = HexColor("#1A1A1A")
DARK_GREY  = HexColor("#2A2A2A")
MID_GREY   = HexColor("#5A5A5A")
LIGHT_GREY = HexColor("#E8E8E8")
TEXT       = HexColor("#1A1A1A")
RED_ACC    = HexColor("#B33A3A")
GREEN      = HexColor("#2D5016")
PURPLE     = HexColor("#3A2A4A")
CREAM      = HexColor("#F8F4EC")

# ---------- STYLES ----------
styles = getSampleStyleSheet()

body = ParagraphStyle(
    "body", fontName="DejaVu", fontSize=10.5, leading=15,
    textColor=TEXT, alignment=TA_JUSTIFY, spaceAfter=8,
)
body_center = ParagraphStyle(
    "body_center", parent=body, alignment=TA_CENTER,
)
body_light = ParagraphStyle(
    "body_light", parent=body, textColor=LIGHT_GREY,
)
body_white = ParagraphStyle(
    "body_white", parent=body, textColor=white,
)
body_dark = ParagraphStyle(
    "body_dark", parent=body, textColor=DARK_BG,
)
body_italic = ParagraphStyle(
    "body_italic", parent=body, fontName="DejaVu-Italic",
)
h_chapter = ParagraphStyle(
    "h_chapter", fontName="DejaVu-Serif-Bold", fontSize=22, leading=26,
    textColor=GOLD, alignment=TA_LEFT, spaceBefore=0, spaceAfter=4,
)
h_chapter_sub = ParagraphStyle(
    "h_chapter_sub", fontName="DejaVu-Italic", fontSize=12, leading=15,
    textColor=MID_GREY, alignment=TA_LEFT, spaceAfter=18,
)
h_section = ParagraphStyle(
    "h_section", fontName="DejaVu-Bold", fontSize=13.5, leading=17,
    textColor=GOLD_SOFT, alignment=TA_LEFT, spaceBefore=12, spaceAfter=8,
)
h_part = ParagraphStyle(
    "h_part", fontName="DejaVu-Serif-Bold", fontSize=28, leading=32,
    textColor=GOLD, alignment=TA_CENTER, spaceBefore=80, spaceAfter=20,
)
cover_title = ParagraphStyle(
    "cover_title", fontName="DejaVu-Serif-Bold", fontSize=42, leading=46,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10,
)
cover_sub = ParagraphStyle(
    "cover_sub", fontName="DejaVu-Italic", fontSize=18, leading=22,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=80,
)
cover_for = ParagraphStyle(
    "cover_for", fontName="DejaVu", fontSize=14, leading=18,
    textColor=LIGHT_GREY, alignment=TA_CENTER, spaceAfter=4,
)
cover_name = ParagraphStyle(
    "cover_name", fontName="DejaVu-Serif-Bold", fontSize=32, leading=38,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=80,
)
cover_quote = ParagraphStyle(
    "cover_quote", fontName="DejaVu-Italic", fontSize=14, leading=20,
    textColor=GOLD, alignment=TA_CENTER, spaceAfter=10,
)
callout_label = ParagraphStyle(
    "callout_label", fontName="DejaVu-Bold", fontSize=10.5, leading=13,
    textColor=white, alignment=TA_LEFT, spaceAfter=6,
)
callout_label_dark = ParagraphStyle(
    "callout_label_dark", parent=callout_label, textColor=DARK_BG,
)
callout_body = ParagraphStyle(
    "callout_body", fontName="DejaVu", fontSize=10.5, leading=15,
    textColor=white, alignment=TA_JUSTIFY, spaceAfter=6,
)
callout_body_dark = ParagraphStyle(
    "callout_body_dark", parent=callout_body, textColor=DARK_BG,
)
pull_quote = ParagraphStyle(
    "pull_quote", fontName="DejaVu-Italic", fontSize=13, leading=18,
    textColor=GOLD_SOFT, alignment=TA_CENTER, spaceBefore=10, spaceAfter=14,
    leftIndent=30, rightIndent=30,
)
roman_principle = ParagraphStyle(
    "roman_principle", fontName="DejaVu-Serif-Bold", fontSize=16, leading=20,
    textColor=GOLD, alignment=TA_LEFT, spaceBefore=18, spaceAfter=6,
)
phase_title = ParagraphStyle(
    "phase_title", fontName="DejaVu-Serif-Bold", fontSize=18, leading=22,
    textColor=GOLD, alignment=TA_LEFT, spaceBefore=14, spaceAfter=10,
)
small_label = ParagraphStyle(
    "small_label", fontName="DejaVu-Bold", fontSize=9.5, leading=12,
    textColor=GOLD_SOFT, alignment=TA_LEFT, spaceAfter=2,
)

# ---------- CALLOUT ----------
def make_callout(label, text, bg, fg, label_style=None, body_style=None):
    """Crée un bloc callout coloré, label en gras + corps."""
    if label_style is None:
        label_style = callout_label if fg == white else callout_label_dark
    if body_style is None:
        body_style = callout_body if fg == white else callout_body_dark

    inner = []
    inner.append(Paragraph(label, label_style))
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
    return KeepTogether([Spacer(1, 6), t, Spacer(1, 10)])


def concept(text):
    return make_callout("◆  LE CONCEPT", text, DARK_GREY, white)

def miroir(text):
    return make_callout("◈  TON MIROIR", text, GOLD, DARK_BG)

def action(text):
    return make_callout("▶  ACTION CONCRÈTE", text, GREEN, white)

def journal(text):
    return make_callout("?  POUR TON JOURNAL", text, PURPLE, white)

def warning(text):
    return make_callout("!  VÉRITÉ BRUTALE", text, RED_ACC, white)


def hougaard_block(text):
    """Le bloc 'Ce que dit Hougaard' — un fond crème discret."""
    inner = []
    inner.append(Paragraph("◇  CE QUE DIT HOUGAARD", small_label))
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


# ---------- DECORATIONS ----------
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


def P(text, style=None):
    return Paragraph(text, style or body)


# ---------- PAGE TEMPLATES ----------
def cover_page(canv, doc):
    canv.saveState()
    # full black background
    canv.setFillColor(DARK_BG)
    canv.rect(0, 0, A4[0], A4[1], fill=1, stroke=0)
    # top gold band
    canv.setFillColor(GOLD)
    canv.rect(0, A4[1] - 1.4 * cm, A4[0], 1.4 * cm, fill=1, stroke=0)
    # bottom gold band
    canv.rect(0, 0, A4[0], 1.4 * cm, fill=1, stroke=0)
    # thin inner rules
    canv.setStrokeColor(GOLD)
    canv.setLineWidth(0.5)
    canv.rect(1.2 * cm, 2.2 * cm, A4[0] - 2.4 * cm, A4[1] - 4.4 * cm, fill=0, stroke=1)
    canv.restoreState()


def standard_page(canv, doc):
    canv.saveState()
    # header
    canv.setStrokeColor(GOLD)
    canv.setLineWidth(0.6)
    canv.line(2 * cm, A4[1] - 1.4 * cm, A4[0] - 2 * cm, A4[1] - 1.4 * cm)
    canv.setFont("DejaVu-Bold", 8)
    canv.setFillColor(GOLD_SOFT)
    canv.drawString(2 * cm, A4[1] - 1.15 * cm, "BEST LOSER WINS")
    canv.setFont("DejaVu-Italic", 8)
    canv.setFillColor(MID_GREY)
    canv.drawRightString(A4[0] - 2 * cm, A4[1] - 1.15 * cm, "Guide personnalisé — Marien")
    # footer page number
    canv.setFont("DejaVu", 8.5)
    canv.setFillColor(MID_GREY)
    canv.drawCentredString(A4[0] / 2.0, 1.2 * cm, f"— {doc.page} —")
    # footer rule
    canv.setStrokeColor(GOLD)
    canv.setLineWidth(0.3)
    canv.line(2 * cm, 1.7 * cm, A4[0] - 2 * cm, 1.7 * cm)
    canv.restoreState()


# ---------- DOC BUILD ----------
OUTPUT = "/home/user/Site-Enzo/best_loser_wins_marien.pdf"

doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2.5 * cm, rightMargin=2.5 * cm,
    topMargin=2.2 * cm, bottomMargin=2.2 * cm,
    title="Best Loser Wins — Guide personnalisé pour Marien",
    author="Adapté de Tom Hougaard",
)


# ============================================================
# CONTENU
# ============================================================
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
    "Ce document existe pour une raison simple : le livre <b>Best Loser Wins</b> de Tom Hougaard "
    "n'a jamais été traduit en français. Et même s'il l'était, il ne te parlerait pas à toi. "
    "Il parlerait à un public général. Toi tu es un cas spécifique : 25 ans, ex-coma, prop firm trader sur XAUUSD, "
    "méthode Smart Money Concepts, un pattern destructeur précis qui crame tes comptes encore et encore."
))
story.append(P(
    "Ce que tu tiens entre les mains n'est donc pas une traduction. C'est une <b>transposition</b>. "
    "Les concepts viennent de Hougaard, l'application est faite sur mesure pour toi. Le contenu est "
    "structuré pour que chaque chapitre te renvoie un miroir — pas un cours."
))
story.append(P("Comment l'utiliser", h_section))
story.append(P(
    "Ne lis pas ce document d'une traite. Si tu fais ça, tu vas absorber des informations et rien ne va changer. "
    "C'est exactement ce que tu fais déjà avec les livres et vidéos de trading depuis trois ans, et regarde où ça t'a mené."
))
story.append(P(
    "La règle est la suivante : <b>un chapitre tous les deux ou trois jours</b>. Tu lis, tu refermes, "
    "tu fais l'action concrète, tu écris dans ton journal. Tu ne passes pas au chapitre suivant tant que "
    "tu n'as pas appliqué le précédent au moins une fois en conditions réelles ou en simulation. "
    "Seize chapitres × 2-3 jours = environ six semaines de travail. C'est le bon rythme."
))
story.append(P(
    "Chaque chapitre suit la même architecture pour que ton cerveau s'habitue au pattern et que tu sois "
    "capable de retrouver l'information sans la chercher :"
))

# Structure récurrente — tableau
struct_data = [
    ["Section", "Rôle"],
    ["◇  CE QUE DIT HOUGAARD", "Le concept du livre, en français, paraphrasé."],
    ["◆  LE CONCEPT", "L'essence en 3-4 lignes. Tu retiens ça si tu retiens rien d'autre."],
    ["◈  TON MIROIR", "Application directe à ton cas. Le cœur du document."],
    ["▶  ACTION CONCRÈTE", "Le protocole à mettre en place cette semaine. Pas le mois prochain."],
    ["?  POUR TON JOURNAL", "Les questions à écrire à la main, le soir."],
    ["!  VÉRITÉ BRUTALE", "Quand pertinent. Ce que tu vas vouloir éviter de regarder."],
]
struct_table = Table(struct_data, colWidths=[5.5 * cm, 10.5 * cm])
struct_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), DARK_GREY),
    ("TEXTCOLOR", (0, 0), (-1, 0), GOLD),
    ("FONTNAME", (0, 0), (-1, 0), "DejaVu-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("FONTNAME", (0, 1), (0, -1), "DejaVu-Bold"),
    ("FONTNAME", (1, 1), (1, -1), "DejaVu"),
    ("TEXTCOLOR", (0, 1), (-1, -1), TEXT),
    ("BACKGROUND", (0, 1), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(Spacer(1, 6))
story.append(struct_table)
story.append(Spacer(1, 14))

story.append(P(
    "Une dernière chose. Ce document ne va pas te ménager. Tu as explicitement demandé qu'on soit direct, blunt, "
    "qu'on évite le bullshit. Donc on évite. Si à un moment tu te dis « ouais mais moi c'est différent », c'est "
    "exactement à ce moment-là qu'il faut relire la page deux fois. Le « moi c'est différent » est le mensonge "
    "préféré de ton cerveau de trader."
))
story.append(PageBreak())


# ---------- INTRODUCTION ----------
story.append(P("INTRODUCTION", h_chapter))
story.append(P("La thèse centrale — pourquoi tu perds en sachant tout", h_chapter_sub))
story.append(GoldRule())
story.append(Spacer(1, 12))

story.append(P(
    "Hougaard a passé plus de vingt ans à trader. Pas en démo, pas en backtest : avec son propre argent et celui "
    "de fonds. Il a vu défiler des centaines de traders dans les salles où il a travaillé. Et il en est arrivé "
    "à une conclusion qui contredit à peu près tout ce que tu trouves sur Internet, YouTube, Discord et Twitter."
))
story.append(P(
    "Les meilleurs traders n'ont pas un meilleur edge technique que les perdants. Ils ne lisent pas mieux les charts. "
    "Ils n'ont pas un système plus sophistiqué. Ils ne devinent pas la direction avec plus de précision. "
    "Ce qu'ils font de différent tient en une phrase :"
))
story.append(P("Ils gèrent leurs trades perdants mieux que les autres.", pull_quote))
story.append(P(
    "C'est tout. C'est ça la thèse. Le « best loser wins ». Pas celui qui gagne plus souvent. "
    "Celui qui perd <b>mieux</b> : plus petit, plus vite, plus calmement, sans contamination émotionnelle "
    "sur les trades suivants."
))

story.append(P("La phrase qu'il faut tatouer", h_section))
story.append(P(
    "Hougaard répète cette idée sous des formes différentes tout au long du livre : les gens ne perdent pas "
    "en trading à cause de l'analyse technique. Ils perdent à cause de ce qu'il y a entre l'analyse et l'exécution — "
    "c'est-à-dire eux. Leurs réflexes humains parfaitement normaux."
))
story.append(P(
    "Tu peux connaître le SMC mieux que 95% des traders. Tu peux identifier un CHoCH les yeux fermés. "
    "Tu peux dessiner un order block en dormant. Si tu décales ton stop loss quand le trade va contre toi, "
    "tu perds. Point. La compétence technique ne te sauvera pas du comportement qui te détruit."
))

story.append(P("La preuve, c'est toi", h_section))
story.append(miroir([
    "Tu es la démonstration vivante de cette thèse. Tu connais ta méthode. Tu sais lire London et NY killzones. "
    "Tu sais identifier une FVG. Tu repères tes OB. Tu n'es pas un débutant qui galère parce qu'il ne comprend pas "
    "ce qu'est un swing high. Ton problème n'est pas là.",
    "Ton problème c'est ce qui se passe entre +800 PnL et +1500 PnL. C'est ce qui se passe quand le marché commence "
    "à reverser et que tu refuses de couper. C'est ce qui se passe quand tu décales ton SL « juste un peu » parce "
    "que tu es <b>sûr</b> que ça va repartir. C'est ce qui se passe dans les trois secondes après une perte, quand "
    "ton corps cherche une revanche.",
    "Si la solution était technique, tu l'aurais déjà trouvée. T'as les outils. T'as la méthode. T'as l'intelligence. "
    "Ce qui te manque c'est pas une stratégie de plus. C'est une révolution de la façon dont tu gères la perte, "
    "le profit qui court, et l'intensité émotionnelle qui passe dans ton corps quand le PnL bouge."
]))

story.append(P(
    "Le reste de ce document est construit autour de cette idée. On va décortiquer pourquoi tu fais ce que tu fais, "
    "et on va construire — pas à pas, chapitre après chapitre — une nouvelle façon de te tenir devant l'écran."
))
story.append(P(
    "Six semaines. Seize chapitres. Une seule promesse : si tu fais le travail, tu ne seras plus le même trader "
    "fin juin. Tu ne deviendras pas riche en six semaines. Tu deviendras quelqu'un qui n'a plus besoin de cramer "
    "un compte pour apprendre une leçon qu'il connaît déjà."
))
story.append(PageBreak())


# ============================================================
# CHAPITRES — Liste de tuples (titre, sous-titre, sections)
# Chaque chapitre est défini comme une liste de flowables.
# ============================================================

def chapter_header(num, title, subtitle):
    out = []
    out.append(P(f"CHAPITRE {num}", small_label))
    out.append(P(title, h_chapter))
    out.append(P(subtitle, h_chapter_sub))
    out.append(GoldRule())
    out.append(Spacer(1, 12))
    return out


# ============ CHAPITRE 1 ============
story.extend(chapter_header(1, "Un début prometteur", "Pourquoi la connaissance technique ne sauve personne"))

story.extend(hougaard_block([
    "Hougaard ouvre son livre en racontant son propre parcours. Il a commencé dans la City de Londres, "
    "obsédé par l'analyse technique, persuadé que la compétence en lecture des marchés était la clé. "
    "Il a englouti des centaines de livres, suivi des dizaines de mentors, traqué chaque pattern de prix.",
    "Et il perdait. Pas par ignorance. Par incapacité à <b>exécuter</b> ce qu'il savait. "
    "Le décalage entre ce qu'il pouvait voir sur un graphique et ce qu'il faisait avec son argent l'a obsédé.",
    "C'est là qu'il a commencé à comprendre que le trading n'est pas un problème intellectuel mais un problème "
    "psychologique. Que l'edge n'est pas dans la méthode, il est dans la capacité à exécuter la méthode quand "
    "tout dans ton corps te pousse à faire autre chose."
]))

story.append(concept(
    "L'analyse technique est nécessaire mais ne suffit pas. C'est le ticket d'entrée. "
    "Le vrai jeu commence quand tu sais lire un graphique correctement et que tu continues quand même à perdre. "
    "À ce moment-là, la question n'est plus « comment lire le marché » mais « comment me lire moi »."
))

story.append(miroir([
    "Tu trades XAUUSD avec une méthode Smart Money Concepts que tu maîtrises. CHoCH, BOS, FVG, order blocks, "
    "killzones London et NY — tu connais. Tu peux justifier chaque entrée avec une lecture cohérente du marché. "
    "Si on prenait dix de tes derniers setups en isolation, ils seraient probablement bons.",
    "Donc pourquoi tu cramés tes comptes Apex, Topstep, Alpha Futures ? Pas parce que ta méthode est mauvaise. "
    "Parce que ton <b>exécution</b> est polluée. Parce qu'entre l'analyse et la sortie du trade, il y a toi. "
    "Et toi, tu décales les SL, tu laisses courir au-delà du TP, tu refuses de couper quand le marché te dit non.",
    "La leçon de ce premier chapitre c'est de tuer définitivement l'illusion qui te tient encore : "
    "l'idée que « si j'apprends un truc de plus, si je trouve le bon setup, si je comprends mieux les FVG, "
    "ça va marcher ». Non. Tu n'as pas un problème de méthode. Tu as un problème d'humain.",
    "C'est une bonne nouvelle. Ça veut dire que tu n'as pas besoin d'aller chercher quelque chose de nouveau. "
    "Tu as déjà tout. Il faut juste arrêter de saboter ce que tu as déjà."
]))

story.append(action(
    "Cette semaine, écris en haut d'une page de ton journal cette phrase, à la main, en lettres capitales : "
    "<b>MA MÉTHODE EST SUFFISANTE. CE QUI N'EST PAS SUFFISANT, C'EST MOI.</b> "
    "Relis cette phrase chaque matin avant d'ouvrir ta plateforme. Sept jours d'affilée. "
    "Pas de nouveau setup, pas de nouvelle stratégie, pas de nouveau livre de trading. "
    "Juste cette phrase, et l'application stricte de ce que tu sais déjà."
))

story.append(journal([
    "Combien de méthodes différentes j'ai essayées depuis que je trade ? Liste-les.",
    "Si je suis honnête : est-ce que c'est la méthode qui était insuffisante, ou c'est moi qui n'ai jamais "
    "exécuté la même méthode pendant 100 trades d'affilée ?",
    "Qu'est-ce que je gagne, émotionnellement, à croire que le problème vient de la méthode ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 2 ============
story.extend(chapter_header(2, "Histoires du trading floor", "Les cinq patterns destructeurs universels"))

story.extend(hougaard_block([
    "Hougaard a passé des années en salle de marché. Il y a vu des centaines de traders, novices et expérimentés, "
    "rejouer les mêmes erreurs dans des configurations différentes. Au point d'identifier des patterns "
    "comportementaux récurrents — pas chez quelques traders, chez <b>tous</b> les traders perdants, quel que soit "
    "leur niveau technique ou leur instrument.",
    "Ces patterns ne sont pas dûs à une mauvaise méthode ou à un manque d'expérience. Ils sont dûs à la façon "
    "dont le cerveau humain réagit face à l'incertitude monétaire. Et ils sont si universels qu'on peut presque "
    "les coter à l'avance : voici ce que tu vas faire, dans quel ordre, et pourquoi."
]))

story.append(P("Les cinq patterns que tu reconnais", h_section))

# Tableau des 5 patterns
patterns_data = [
    ["#", "Pattern", "Mécanique"],
    ["P1", "Doubler sur la perte", "Le trade va contre toi. Au lieu de couper, tu rajoutes pour « baisser ton prix moyen ». Espoir déguisé en stratégie."],
    ["P2", "Couper le gain trop tôt", "Le trade est en profit. Tu coupes à +200 alors que ton plan disait +800. La peur de voir le gain disparaître est plus forte que le plan."],
    ["P3", "Peur post-perte", "Après une perte, le setup suivant est valide, mais tu n'oses plus prendre. Tu rates le trade qui aurait compensé."],
    ["P4", "FOMO compensatoire", "Après une perte, tu prends n'importe quoi pour récupérer. Setup B-grade, taille augmentée, killzone passée. Tu reprends une deuxième perte."],
    ["P5", "Décaler le SL", "Le trade va contre toi vers ton stop. Tu te dis « il va revenir ». Tu décales le SL « juste un peu ». Et puis encore. Et puis c'est trop tard."],
]
pat_table = Table(patterns_data, colWidths=[1 * cm, 4.5 * cm, 10.5 * cm])
pat_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), DARK_GREY),
    ("TEXTCOLOR", (0, 0), (-1, 0), GOLD),
    ("FONTNAME", (0, 0), (-1, 0), "DejaVu-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 10),
    ("FONTSIZE", (0, 1), (-1, -1), 9.5),
    ("FONTNAME", (0, 1), (1, -1), "DejaVu-Bold"),
    ("FONTNAME", (2, 1), (2, -1), "DejaVu"),
    ("TEXTCOLOR", (0, 1), (-1, -1), TEXT),
    ("BACKGROUND", (0, 1), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(pat_table)
story.append(Spacer(1, 14))

story.append(concept(
    "Les patterns destructeurs ne sont pas tes patterns à toi. Ils sont les patterns du cerveau humain "
    "face à une perte d'argent incertaine. Tu ne les inventes pas. Tu les reproduis, comme tous les autres."
))

story.append(miroir([
    "Regardons ton pattern signature. Tu rentres en trade XAUUSD. Le marché va dans ton sens. "
    "Tu atteins ton TP, et tu ne coupes pas — tu décides de laisser courir. +1000 PnL. +1200. +1500. "
    "À ce moment précis, le cerveau dopaminergique a pris le contrôle.",
    "Le marché commence à reverser. Premier signal d'alerte ignoré. Le PnL descend à +1200. Tu te dis « ça va repartir ». "
    "Il descend à +800. Tu te dis « j'attends que ça revienne à +1500 ». Il descend à +200. Là tu rentres en panique. "
    "Le marché casse ton entrée. Tu es en perte. <b>Et tu décales ton SL initial.</b> Parce que sortir maintenant "
    "ce serait acter d'avoir laissé filer +1500 ET de prendre une perte. Inacceptable pour l'ego.",
    "Tu viens de combiner P2 (mauvaise gestion du gain), P5 (décalage du SL) et tu vas probablement enchaîner avec "
    "P4 (FOMO compensatoire) sur un autre trade pour te refaire. Pattern complet. Compte crammé.",
    "Ce que tu fais n'est pas une bizarrerie. C'est la séquence la plus documentée du trading. Hougaard l'a vu "
    "des milliers de fois. La seule différence entre toi et un trader rentable, c'est que lui a appris à "
    "interrompre la séquence au moment où tu la nourris."
]))

story.append(action(
    "Imprime le tableau des cinq patterns. Scotche-le à côté de ton écran. À la fin de chaque session de trading, "
    "marque sur une feuille à quels patterns tu as cédé aujourd'hui. Une simple croix dans une colonne P1 P2 P3 P4 P5. "
    "Sur 30 jours tu vas voir tes deux ou trois patterns dominants. Ce sont eux qu'il faut tuer."
))

story.append(journal([
    "Sur mes dix derniers comptes prop firm crammés, quelle séquence de patterns je peux identifier ? "
    "Est-ce que c'est toujours la même ?",
    "Quel pattern est mon préféré ? Celui que je rejoue le plus ? Pourquoi celui-là particulièrement ?"
]))

story.append(warning(
    "Tu vas être tenté de dire « ouais mais hier c'était différent ». Non. Ce n'était pas différent. "
    "Le contexte change, les patterns sont identiques. Tant que tu n'auras pas accepté que tu n'as pas "
    "un problème unique mais le problème universel des traders, tu chercheras une solution unique à un problème "
    "universel. Et tu ne la trouveras pas."
))

story.append(PageBreak())


# ============ CHAPITRE 3 ============
story.extend(chapter_header(3, "Pourquoi nous échouons", "Les quatre forces psychologiques qui te détruisent"))

story.extend(hougaard_block([
    "Hougaard explore les racines psychologiques du comportement du trader. Il s'appuie notamment sur les travaux "
    "de Daniel Kahneman et Amos Tversky, qui ont démontré expérimentalement que l'humain n'est pas un agent rationnel "
    "face au risque. Nous sommes câblés pour éviter la perte au point d'accepter une perte plus grande plus tard "
    "plutôt que d'acter une petite perte maintenant.",
    "Il identifie quatre forces psychologiques qui se combinent pour rendre le trading rentable contre-intuitif :",
    "<b>1. Le besoin d'avoir raison.</b> L'ego humain est construit autour de la certitude. Être prouvé tort "
    "est ressenti comme une attaque identitaire. En trading, ton SL touché est une preuve publique que tu avais tort. "
    "Donc tu le décales.",
    "<b>2. L'aversion à la perte (Kahneman).</b> La douleur de perdre 100€ est environ 2 à 2,5 fois plus intense "
    "que le plaisir de gagner 100€. Donc tu vas prendre des risques irrationnels pour éviter d'acter une perte, "
    "et tu vas couper trop tôt tes gains pour éviter de les voir s'évaporer.",
    "<b>3. Le besoin de certitude.</b> L'humain déteste l'incertitude. Or le trading <b>est</b> de l'incertitude. "
    "Chaque trade est probabiliste, jamais certain. Ton cerveau va chercher à imposer de la certitude là où il "
    "n'y en a pas : « je suis sûr que ça va remonter ». Cette phrase est l'expression de ton inconfort, pas de "
    "la réalité du marché.",
    "<b>4. La projection émotionnelle.</b> Tu projettes sur le marché tes désirs. Tu veux que le prix monte, donc "
    "tu lis les indices qui confirment qu'il va monter et tu ignores ceux qui disent l'inverse. Biais de confirmation, "
    "version trading."
]))

story.append(concept(
    "Tu ne perds pas parce que tu es stupide ou paresseux. Tu perds parce que tu es <b>humain</b>. "
    "Quatre forces psychologiques universelles transforment chaque trade en piège émotionnel. "
    "Les contrer demande de l'entraînement, pas de l'intelligence."
))

story.append(miroir([
    "Reprends ton pattern +1500. Décompose-le avec ces quatre forces.",
    "<b>Besoin d'avoir raison :</b> tu as prédit que XAUUSD allait monter. Le marché a confirmé jusqu'à +1500. "
    "Tu as eu raison. Couper et empocher 800-1000 ce serait acter que tu as eu raison <i>partiellement</i>. "
    "Pas assez pour ton ego. Tu veux la confirmation totale.",
    "<b>Aversion à la perte :</b> quand le marché reverse de +1500 à +1000, tu ressens cette baisse comme une "
    "<b>perte</b> de 500. Pas comme un gain réduit. Émotionnellement, perdre 500 de PnL flottant fait plus mal "
    "que gagner 1000 ne fait plaisir. Ton cerveau veut éviter d'acter cette « perte ». Donc il attend.",
    "<b>Besoin de certitude :</b> ton cerveau te dit « ça va remonter à +1500, je le sens ». Cette certitude "
    "n'existe que dans ta tête. Le marché ne t'a rien promis. Mais l'inconfort de l'incertitude est tel que tu "
    "préfères une certitude inventée à une réalité ambiguë.",
    "<b>Projection émotionnelle :</b> tu projettes ton désir (revenir à +1500) sur le chart. Tu lis le pullback "
    "comme une « respiration normale avant continuation », pas comme un signal de reversal — alors qu'objectivement "
    "le signal est identique dans les deux cas, et seule la suite révèle lequel c'était.",
    "Ces quatre forces ne sont pas des bugs de Marien. Ce sont les features standard du cerveau humain. "
    "Ce qui se passe avec ton TBI de 2022, c'est que ton système nerveux dérégulé amplifie ces réactions — "
    "tu ressens plus fort, plus vite, et avec moins de modulation possible. Donc tu ne dois pas juste les contrer, "
    "tu dois les contrer dans un système nerveux moins coopératif que la moyenne. C'est ton handicap. C'est aussi "
    "ta carte à jouer : si tu apprends à réguler dans ces conditions, tu deviendras meilleur que quelqu'un de neurotypique."
]))

story.append(action(
    "Pendant cette semaine, avant chaque trade, écris sur ta feuille de session ces quatre lettres : R / P / C / E "
    "(Raison / Perte / Certitude / Émotion). Pendant le trade, si tu ressens un déclencheur lié à une de ces forces, "
    "tu cocheras la lettre correspondante. C'est un outil de méta-conscience : tu ne combats pas la force, tu la nommes. "
    "Nommer une force la rend opérable. La force qu'on ne nomme pas te pilote."
))

story.append(journal([
    "Laquelle de ces quatre forces est la plus active chez moi ? Celle que je sens le plus souvent en trade ?",
    "Mon TBI a-t-il amplifié une de ces forces en particulier ? Est-ce que je peux le sentir dans mon corps "
    "quand elle se déclenche ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 4 ============
story.extend(chapter_header(4, "La dure vérité", "70 à 90% des traders perdent — et toi ?"))

story.extend(hougaard_block([
    "Hougaard rappelle un chiffre que l'industrie du trading retail aime camoufler : la grande majorité des traders "
    "particuliers perdent de l'argent. Selon les régulateurs européens et les rapports des brokers eux-mêmes, "
    "entre 70% et 90% des comptes retail sont en perte sur un horizon de quelques années.",
    "Ce chiffre est cohérent quelle que soit la décennie, le marché, la méthode. Forex, actions, futures, crypto : "
    "même taux d'échec. Ce n'est donc pas un problème de marché ou d'instrument. C'est un problème humain.",
    "Le piège, c'est que les traders perdants attribuent leur échec à ce qu'ils peuvent <b>changer techniquement</b> : "
    "la méthode, l'indicateur, le timing. C'est la zone de confort : changer un outil. Changer son comportement, "
    "c'est plus douloureux. Donc on fuit dans la technique."
]))

story.append(concept(
    "Si 80% perdent, ce n'est pas un accident. C'est une feature du jeu. Le marché est conçu pour transférer "
    "l'argent des impatients aux patients, des émotionnels aux calmes, des humains aux disciplinés. "
    "Ta tâche n'est pas d'être plus malin que la moyenne. C'est d'être moins humain qu'elle."
))

story.append(miroir([
    "Tu fais partie des 80%. Pas par accident, pas par malchance, pas parce que les prop firms sont conçues pour "
    "te faire échouer (elles ne sont pas conçues pour ça — elles sont juste des miroirs efficaces). "
    "Tu y es parce que tu trades exactement comme un humain est câblé pour trader.",
    "Et tu as une caractéristique en plus qui te rend particulièrement vulnérable : ton lien identité-performance "
    "est très fort. Tu te perçois à travers tes résultats. Quand tu gagnes, tu existes ; quand tu perds, tu "
    "doutes de ta valeur entière. Cette équation rend chaque trade insupportablement chargé émotionnellement.",
    "Le post-coma joue ici aussi. À 22 ans tu as failli mourir. Tu as dû prouver que ton cerveau marchait, que ton "
    "corps marchait, que ta vie continuait. Cette pulsion de preuve est puissante, elle t'a sauvé. Mais en trading, "
    "cette même pulsion devient ton ennemi : tu trades pour <b>te prouver</b>, pas pour <b>gagner</b>. Ce sont deux "
    "intentions opposées. La première te coûte des comptes. La deuxième en construit.",
    "La sortie n'est pas dans plus de connaissance. C'est dans un repositionnement : trader cesse d'être un test "
    "identitaire et devient un métier exécuté avec détachement. Une compétence professionnelle, pas une "
    "réhabilitation personnelle."
]))

story.append(P("La fuite dans la technique", h_section))
story.append(P(
    "Combien de fois tu as téléchargé un nouvel indicateur, regardé une nouvelle vidéo SMC, suivi un nouveau mentor "
    "Twitter ? Tu sais déjà que ça ne va rien changer. Tu le fais quand même. Pourquoi ?",
))
story.append(P(
    "Parce que c'est <b>confortable</b>. Apprendre un nouvel indicateur ne te confronte pas à toi-même. Ça nourrit "
    "l'illusion du progrès. Tu te sens productif. Pendant ce temps, le vrai travail — celui qui fait mal, celui "
    "qui consiste à regarder en face tes mécaniques de saboteur — reste à faire."
))

story.append(action(
    "Liste les cinq derniers contenus de trading que tu as consommés ce mois-ci (vidéos, articles, threads X, formations). "
    "Pour chacun, demande-toi : est-ce que je l'ai consommé pour apprendre quelque chose de précis, "
    "ou pour fuir le travail psychologique ? Sois honnête. <b>Coupe immédiatement</b> tout contenu de trading purement "
    "technique pendant les six prochaines semaines. Tu n'as plus besoin d'apprendre. Tu as besoin d'appliquer."
))

story.append(journal([
    "Si je suis dans les 80% perdants — pas par hasard, mais structurellement — qu'est-ce que ça change "
    "à ma manière de me parler le matin ?",
    "Trader, pour moi, est-ce un métier ou une réhabilitation personnelle ? Question pas piégée. Réponse pas piégée."
]))

story.append(warning(
    "Tu vas vouloir te dire « je suis dans les 20% qui vont y arriver ». Possible. Mais tu seras dans les 20% "
    "exactement parce que tu auras arrêté de te raconter ça et que tu auras commencé à acter que tu es dans les 80% "
    "<i>aujourd'hui</i>. La sortie commence par l'admission."
))

story.append(PageBreak())


# ============ CHAPITRE 5 ============
story.extend(chapter_header(5, "Pourquoi la pensée normale ne marche pas", "Vie normale vs trading rentable"))

story.extend(hougaard_block([
    "L'une des observations centrales de Hougaard est que les qualités qui te servent à réussir dans la vie "
    "ordinaire sont précisément celles qui te détruisent en trading. Persévérer dans la difficulté est une vertu "
    "dans la vie. En trading, c'est s'accrocher à un trade perdant. Refuser d'abandonner est une vertu dans la vie. "
    "En trading, c'est ne pas couper.",
    "Cette inversion explique pourquoi tant de gens performants dans leur métier deviennent des traders catastrophiques. "
    "Ils appliquent les heuristiques qui ont construit leur réussite, et ces heuristiques se retournent contre eux.",
    "Le trading rentable demande donc une sorte de déprogrammation : apprendre à activer un mode de pensée différent "
    "quand tu te mets devant l'écran, et à le désactiver quand tu en sors."
]))

story.append(P("Le tableau de l'inversion", h_section))

inv_data = [
    ["Vie normale (qualité)", "Trading (défaut)"],
    ["Persévérer malgré l'échec", "Tenir un trade perdant en espérant le retour"],
    ["Travailler plus pour réussir plus", "Sur-trader pour compenser une perte"],
    ["Avoir raison, défendre son point", "Refuser d'admettre que le marché t'a contredit"],
    ["Investir dans le long terme", "Refuser de couper, « c'est temporaire »"],
    ["Suivre son intuition", "Trader sur feeling au lieu du plan"],
    ["Récompenser l'effort", "Récompenser l'agitation au lieu de la patience"],
    ["Croire en soi", "Surconfiance, taille de position augmentée"],
    ["Apprendre des autres", "Suivre Twitter au lieu de son propre plan"],
]
inv_table = Table(inv_data, colWidths=[8 * cm, 8 * cm])
inv_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), DARK_GREY),
    ("TEXTCOLOR", (0, 0), (-1, 0), GOLD),
    ("FONTNAME", (0, 0), (-1, 0), "DejaVu-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("FONTNAME", (0, 1), (-1, -1), "DejaVu"),
    ("TEXTCOLOR", (0, 1), (-1, -1), TEXT),
    ("BACKGROUND", (0, 1), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(inv_table)
story.append(Spacer(1, 14))

story.append(concept(
    "Ce qui te rend humain te rend mauvais trader. Les vertus de la vie ordinaire deviennent des défauts devant "
    "l'écran. Le bon trader n'est pas un humain meilleur — c'est un humain qui sait activer un autre mode mental "
    "pendant les heures de marché."
))

story.append(miroir([
    "Tu es cavalier de saut d'obstacles. Quand ton cheval refuse un obstacle, qu'est-ce que tu fais ? "
    "Tu ne dis pas « bon ben tant pis ». Tu repasses, tu insistes, tu corriges, tu retravailles jusqu'à ce qu'il passe. "
    "C'est <b>la bonne réaction</b> en équitation. C'est ce qui construit un binôme cheval-cavalier solide.",
    "Tu appliques la même logique en trading : le marché refuse mon idée, je repasse, j'insiste, je rajoute du collatéral, "
    "je décale mon SL pour « lui laisser le temps ». C'est exactement comment tu cramés tes comptes. "
    "Tu importes une qualité (la persévérance équestre) dans un contexte où elle est un défaut.",
    "ATHÉNA pareil. Tu construis ton business 3D, tu rencontres un mur, tu insistes, tu cherches, tu trouves. "
    "Bonne approche entrepreneuriale. Appliquée au marché XAUUSD, ça donne : « ce trade va finir par marcher, je le sens ». "
    "Non. Le marché n'est pas une imprimante 3D que tu calibres. Le marché n'a aucune mémoire de ton effort, aucune "
    "récompense pour ta persévérance. Il n'en a rien à faire de toi.",
    "Ta tâche : <b>compartimenter</b>. Quand tu passes au-dessus d'un obstacle, persévère. Quand tu travailles ATHÉNA, "
    "persévère. Quand tu cliques sur Buy XAUUSD, deviens quelqu'un d'autre. Pas une autre personne — la même, "
    "mais dans un autre mode."
]))

story.append(action(
    "Crée-toi un <b>rituel d'entrée en mode trader</b> de 3 minutes. Pas plus. Avant chaque session : "
    "tu fermes les yeux, tu prends cinq respirations profondes (4 secondes inspi, 6 expi), tu dis à voix basse : "
    "« je ne suis pas en train de prouver quoi que ce soit, je suis en train d'exécuter un protocole ». "
    "C'est l'interrupteur. Tu rentres en mode trader. À la fin de la session, autre rituel : tu fermes la plateforme, "
    "tu te lèves, tu marches 5 minutes. Tu sors du mode."
))

story.append(journal([
    "Quelles qualités de moi, qui marchent en équitation ou avec ATHÉNA, est-ce que j'importe à tort en trading ?",
    "Si je devais me décrire en deux personnes — Marien-le-cavalier et Marien-le-trader — quelles seraient "
    "leurs différences ? Lequel des deux fait son boulot proprement aujourd'hui ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 6 ============
story.extend(chapter_header(6, "Le mindset du gagnant", "Penser en probabilités, pas en certitudes"))

story.extend(hougaard_block([
    "Hougaard reprend ici un thème central développé par Mark Douglas dans <i>Trading in the Zone</i> : "
    "la nature du trading est probabiliste, et la majorité des traders raisonnent en termes de certitudes. "
    "C'est le décalage fondamental.",
    "Un trader rentable ne sait pas si <b>ce</b> trade va marcher. Il sait que sur 100 trades exécutés "
    "selon le même protocole, statistiquement, une proportion connue gagnera et une proportion connue perdra. "
    "Il joue la <b>distribution</b>, pas l'instance.",
    "C'est la métaphore du casino. Un casino ne sait pas si <b>cette</b> main de blackjack va gagner. "
    "Il sait qu'à l'échelle de 10 000 mains, son edge mathématique se matérialise. Le casino ne s'énerve pas "
    "quand un joueur gagne une main. Il ne célèbre pas quand il en perd une. Il exécute, il enregistre, il avance.",
    "Douglas a formulé cinq vérités fondamentales que Hougaard reprend : 1) tout peut arriver, "
    "2) tu n'as pas besoin de savoir ce qui va se passer pour faire de l'argent, 3) il y a une distribution "
    "aléatoire entre gagnants et perdants pour n'importe quel ensemble de variables qui définit un edge, "
    "4) un edge n'est rien d'autre qu'une indication d'une plus haute probabilité d'un mouvement plutôt qu'un autre, "
    "5) chaque instant sur le marché est unique."
]))

story.append(concept(
    "Tu n'es pas un devin. Tu es un opérateur de probabilités. Tu ne sais pas si <b>ce</b> trade va gagner. "
    "Tu sais que ton edge, exécuté proprement sur 100 trades, donne un résultat positif. Joue la série, "
    "pas l'instance. Le casino ne s'attache à aucune main."
))

story.append(miroir([
    "Toi, tu trades comme un parieur. Chaque trade XAUUSD est une mission individuelle, un test, une preuve. "
    "Quand tu rentres, ton cerveau se dit <i>celui-là il faut qu'il marche</i>. Cette phrase est le problème. "
    "Aucune phrase de ce type ne devrait exister dans ta tête en trade.",
    "Imagine que tu sois le casino à la place du joueur. Tu sais que ton edge donne 55% de gagnants à 1R "
    "et un RR de 1:2 sur les gagnants. Si tu prends 100 setups propres ce mois-ci, peu importe que les dix "
    "premiers soient perdants. Peu importe. Tu continues. Tu sais que la distribution va se révéler.",
    "Mais toi, après trois pertes d'affilée, tu changes de logique. Tu doutes de ta méthode. Tu changes de timeframe. "
    "Tu rajoutes un filtre. Tu lis un nouveau thread Twitter. Tu casses ta propre série de 100 setups. "
    "Tu interromps ta propre distribution. Tu n'es jamais le casino — tu es toujours le joueur émotionnel.",
    "La pratique Joe Dispenza que tu fais (méditation, visualisation) est un atout ici si tu l'utilises bien. "
    "Sa méthode te permet d'entraîner l'état de calme, de présence non-réactive. C'est exactement l'état du casino. "
    "Si tu médites sérieusement le matin, tu installes le système nerveux du croupier. Ne gaspille pas cette "
    "ressource. Elle est rare chez les traders, c'est ton avantage caché."
]))

story.append(P("Les cinq vérités à imprimer", h_section))
truths = [
    "<b>1.</b> Tout peut arriver sur le marché. Aucun setup, même le plus propre, n'a 100% de chances.",
    "<b>2.</b> Tu n'as pas besoin de savoir ce qui va se passer pour faire de l'argent.",
    "<b>3.</b> Il y a une distribution aléatoire entre gagnants et perdants à l'intérieur même d'un edge valide.",
    "<b>4.</b> Un edge est juste une probabilité plus haute, jamais une certitude.",
    "<b>5.</b> Chaque instant du marché est unique — les patterns se ressemblent, ils ne se répètent jamais à l'identique.",
]
for t in truths:
    story.append(P(t, body))

story.append(Spacer(1, 8))

story.append(action(
    "Sur ton journal, dessine une grille de 100 cases (10x10). À chaque trade exécuté selon ton protocole, "
    "tu coches une case : verte si gagné, rouge si perdu. <b>Tu vises 100 trades.</b> Tu ne juges pas avant. "
    "Tu ne tires aucune conclusion avant. Tu apprends à expérimenter ta méthode comme une distribution, pas comme "
    "100 jugements individuels."
))

story.append(journal([
    "Si je traitais chaque trade comme un croupier traite chaque main de blackjack, qu'est-ce que je ferais "
    "différemment cette semaine ?",
    "Quelle est la dernière fois où j'ai laissé un trade perdant se résoudre proprement, sans interférence ? "
    "Vraiment ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 7 ============
story.extend(chapter_header(7, "Douleur et plaisir", "Le trader comme junkie dopaminergique"))

story.extend(hougaard_block([
    "Ce chapitre est sans doute le plus utile du livre pour Marien, donc je vais y consacrer le temps qu'il mérite. "
    "Hougaard explique comment le trading active les mêmes circuits cérébraux que les jeux d'argent, les drogues, "
    "et toute activité fournissant une récompense intermittente.",
    "Le mécanisme est simple. Quand tu ouvres un trade, le cerveau libère de la dopamine en <b>anticipation</b> "
    "de la récompense. Pas à cause de la récompense elle-même. C'est l'attente qui est addictive, "
    "pas le résultat. C'est pour ça que les pertes en trading n'arrêtent pas l'addiction : le cerveau "
    "veut le shoot d'anticipation suivant.",
    "Quand le trade va dans ton sens, dopamine. Quand il revient contre toi, cortisol et noradrénaline. "
    "Quand tu coupes en gain, dopamine. Quand tu décales un SL, soulagement temporaire (chute de cortisol) "
    "qui agit comme une récompense — donc le comportement « décaler le SL » est <b>renforcé</b> à chaque fois "
    "que le marché finit par revenir, même si tu perds globalement.",
    "Le trader perdant est neurochimiquement entretenu dans son comportement. Ce n'est pas une métaphore. "
    "C'est de la chimie du cerveau. Pour en sortir il faut traiter le problème comme on traite une addiction : "
    "comprendre les déclencheurs, casser les associations, installer des comportements de substitution."
]))

story.append(concept(
    "Tu n'es pas faible. Tu es <b>câblé</b>. Le trading provoque les mêmes pics dopaminergiques que les machines à sous. "
    "Tant que tu attaques le problème en termes de discipline ou de mental, tu rates la cible. "
    "C'est une question de chimie et de routine. On déconditionne, on reconditionne."
))

story.append(miroir([
    "Reprends ton pattern signature. Tu es à +1500 PnL XAUUSD. Qu'est-ce qui se passe dans ton corps à cet instant précis ?",
    "Cœur qui bat plus vite. Souffle plus court. Une espèce de chaleur dans la poitrine. Une excitation qui ressemble "
    "à celle juste avant un saut d'obstacle sur ta filly. Sauf que cette excitation, en trading, est le signal "
    "que ton préfrontal vient de partir en vacances et que ton système limbique pilote. <b>À +1500, tu n'es plus le décideur. "
    "Tu es le passager.</b>",
    "Tu décides ensuite de « laisser courir ». Cette décision n'est pas une décision rationnelle. C'est ton cerveau qui "
    "demande un autre shoot. +1500 c'était bien, mais l'anticipation de +3000 est encore meilleure. La dopamine veut "
    "plus de dopamine. Tu n'es pas en train de gérer un trade, tu es en train de chasser un buzz.",
    "Tu reconnais ce mécanisme. Tu es addict à l'intensité depuis ton coma. Tu l'as dit toi-même : le calme te semble vide. "
    "C'est cohérent. Quand un système nerveux a été soufflé par un TBI et reconstruit dans un contexte de "
    "survie/réhabilitation à haute intensité, il calibre son baseline plus haut. Le calme est ressenti comme une "
    "anomalie. L'intensité comme normalité.",
    "Cette caractéristique te dessert massivement en trading. Le trading rentable est lent, ennuyeux, répétitif. "
    "Si ton système nerveux ne peut pas tolérer l'ennui, tu vas le saboter pour récupérer de l'intensité. "
    "C'est ce que tu fais quand tu décales un SL ou que tu pousses un winner au-delà du TP : tu fabriques "
    "artificiellement de l'intensité dans une activité qui devrait être plate.",
    "La sortie passe par deux travaux parallèles. Un, augmenter ta tolérance au calme (méditation longue, "
    "respiration cohérente, marches longues sans téléphone, temps avec les chevaux en pansage tranquille). "
    "Deux, chercher ton intensité ailleurs qu'en trading. Box, saut d'obstacles compétition, sorties physiques "
    "intenses. <b>Si ta vie est plate à côté de l'écran, l'écran va devenir ton seul shoot. Et tu vas le faire payer.</b>"
]))

story.append(action(
    "Cette semaine, deux protocoles à mettre en place en parallèle. "
    "<b>Protocole « plate-life »</b> : 20 minutes par jour de calme imposé. Respiration 5-5 (5s inspi, 5s expi) "
    "ou méditation Dispenza guidée. Pas négociable. Tu entraînes ton SN à tolérer le calme. "
    "<b>Protocole « intensité OFF screen »</b> : 3 séances physiques intenses par semaine minimum "
    "(box, équitation cross, sport explosif). Tu sors l'intensité du corps avant qu'il aille la chercher à l'écran."
))

story.append(journal([
    "Quand est-ce que je ressens dans la journée un besoin physique d'ouvrir la plateforme ? "
    "Qu'est-ce qui se passe dans mon corps à ce moment-là ?",
    "Si je devais classer mes activités quotidiennes par niveau d'intensité ressentie, où se situe le trading ? "
    "Est-ce que je trouve cette intensité ailleurs assez souvent ?"
]))

story.append(warning(
    "Tu ne vaincras pas ton pattern +1500 par la volonté. C'est de la chimie. À +1500 ton préfrontal n'est plus en ligne. "
    "Si tu n'as pas <b>pré-décidé</b> ce que tu fais à +1500 alors que tu étais encore à +0 et calme, "
    "tu vas faire ce que ta chimie te dicte. La discipline ne se gagne pas dans le trade, elle se gagne <b>avant</b> le trade."
))

story.append(PageBreak())


# ============ CHAPITRE 8 ============
story.extend(chapter_header(8, "Croyances limitantes", "Le thermostat financier que tu ne vois pas"))

story.extend(hougaard_block([
    "Hougaard décrit un phénomène que beaucoup de coachs financiers appellent le « thermostat financier » : "
    "chacun a, inconsciemment, un niveau de richesse ou de profit qu'il considère comme « normal pour lui ». "
    "Dès qu'il dépasse ce niveau, un mécanisme inconscient se déclenche pour le ramener au baseline. "
    "Dès qu'il passe en dessous, un autre mécanisme se déclenche pour le ramener au baseline.",
    "Ce thermostat est construit dans l'enfance et l'adolescence à partir de phrases entendues, "
    "d'attitudes parentales face à l'argent, d'expériences personnelles. « L'argent est sale », "
    "« les riches sont malhonnêtes », « il faut travailler dur pour gagner », « ne pas se croire au-dessus », "
    "« on n'est pas faits pour ça » : autant de programmes qui s'installent silencieusement.",
    "Le résultat en trading : tu peux construire ton compte jusqu'à 5 000€ de profit, puis quelque chose en toi "
    "te pousse à le crasher pour revenir à zéro. Tu ne le sais pas consciemment. Tu te dis « j'ai fait des erreurs ». "
    "Mais les erreurs n'étaient pas aléatoires. Elles se sont produites <b>précisément</b> quand tu approchais "
    "d'un seuil mental.",
    "Tant que tu ne montes pas ton thermostat, tu reprendras toujours ce que tu auras gagné. C'est mécanique."
]))

story.append(concept(
    "Ton plafond financier est mental avant d'être technique. Tant que ton inconscient pense que tu n'es pas le genre "
    "de personne qui mérite de garder 30 000€ par mois, tu vas saboter chaque tentative de t'en approcher. "
    "Et tu vas appeler ça « malchance » ou « erreur d'exécution »."
))

story.append(miroir([
    "Réfléchis aux phrases que tu as entendues enfant ou adolescent à propos de l'argent. Pas avec les parents idéalisés. "
    "Vraiment. Quelles phrases reviennent ? « On ne roule pas sur l'or », « il faut faire attention », "
    "« les gens qui gagnent beaucoup le payent ailleurs », « ne te montre pas trop » ? Toutes ces phrases sont "
    "des paramètres dans ton thermostat.",
    "Maintenant croise ça avec ton pattern. Tu approches +1500. C'est probablement déjà un montant qui dépasse ton baseline. "
    "Une journée de trading qui te rapporte plus que ce que beaucoup de gens autour de toi gagnent en deux semaines. "
    "Quelque chose en toi murmure : « c'est trop, c'est suspect, c'est pas pour moi ». Tu ne l'entends pas. Mais "
    "tu obéis : tu fais ce qu'il faut pour ramener à zéro.",
    "Le sabotage du +1500 n'est pas <b>juste</b> dopaminergique. Il est aussi identitaire. Garder ce profit, "
    "ce serait te valider comme quelqu'un qui peut gagner ça. Pour quelqu'un dont l'identité se construit "
    "sur la preuve constante (post-coma : prouver que tu es capable, prouver que tu es à la hauteur), une preuve "
    "acquise est une preuve qui s'éteint. Tu as besoin de continuer à <b>prouver</b>, donc tu détruis la preuve "
    "pour la rejouer.",
    "C'est sombre mais c'est précis. Tant que ton identité dépend du combat, tu auras besoin de combats. "
    "Donc tu créeras des comptes à reconstruire. Tant que tu ne deviens pas quelqu'un qui <b>est</b> riche "
    "indépendamment de la dernière preuve, tu ne pourras pas garder ce que tu gagnes.",
    "ATHÉNA peut t'aider ici. C'est une preuve qui se construit lentement, qui ne se crame pas en une journée. "
    "Tu construis une identité d'entrepreneur, d'artisan, de fondateur. Cette identité est plus stable qu'une "
    "identité de trader-qui-vient-de-faire-+1500. Plus tu nourris l'autre identité, plus le besoin de prouver "
    "via le trading diminue. Et plus tu peux trader proprement, parce que le trade n'est plus une preuve. C'est juste un trade."
]))

story.append(P("Les croyances probables à examiner", h_section))
beliefs = [
    "« Je dois mériter chaque euro par l'effort visible » → contradiction avec un edge qui paye 5 secondes de clic.",
    "« Si je gagne trop, je dois m'attendre à perdre autant après » → loi du retour, garantit le crash.",
    "« Je ne suis pas le genre de personne qui gagne ça » → le thermostat brut.",
    "« Pour être respecté il faut souffrir » → tu vas créer la souffrance qui justifiera la réussite.",
    "« Je dois prouver que mon cerveau marche encore » → chaque trade devient un test du cerveau, pas un trade.",
]
for b in beliefs:
    story.append(P("•  " + b, body))

story.append(Spacer(1, 6))

story.append(action(
    "Écris à la main, dans ton journal, les phrases que tu as entendues sur l'argent dans ta famille et ton entourage "
    "jusqu'à 18 ans. Vraiment. Une page complète. Puis souligne les trois qui te touchent encore aujourd'hui. "
    "Pour chacune, écris en dessous la nouvelle phrase que tu choisis. Tu ne combats pas l'ancienne — tu en plantes "
    "une nouvelle à côté, et tu l'arroses tous les jours."
))

story.append(journal([
    "Quel montant mensuel de profit me semble « normal pour moi » ? À quel montant je commence à ressentir "
    "« c'est trop » ? Ce montant correspond-il à mon pattern de crash ?",
    "Quelle preuve est-ce que je cherche encore à donner depuis 2022 ? À qui ? Cette preuve est-elle "
    "encore nécessaire aujourd'hui ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 9 ============
story.extend(chapter_header(9, "Visualisation pré-trade", "Pré-vivre la perte pour la désactiver"))

story.extend(hougaard_block([
    "La visualisation est une technique connue dans le sport de haut niveau. Hougaard la transpose au trading "
    "avec une nuance importante : il ne s'agit pas de visualiser le succès du trade. C'est trop facile, et c'est "
    "ce que tout le monde fait déjà. Il s'agit de visualiser <b>la perte</b>, de la pré-vivre émotionnellement avant "
    "qu'elle arrive.",
    "Quand tu vis la perte pour la première fois pendant le trade, ton système nerveux réagit en mode urgence : "
    "il déclenche des comportements de survie (décaler le SL, doubler, fuir). Si tu as déjà vécu mentalement "
    "cette même perte plusieurs fois <b>au calme</b>, le système nerveux la reconnaît comme une situation connue "
    "et ne déclenche pas la cascade d'urgence. Tu peux exécuter le plan.",
    "C'est une forme de désensibilisation contrôlée. La même logique que celle utilisée en thérapie pour les "
    "phobies. Tu exposes le système nerveux à la situation menaçante en sécurité, jusqu'à ce que la situation "
    "ne déclenche plus de réponse d'urgence."
]))

story.append(concept(
    "Tu visualises ton SL touché avant de cliquer Buy. Pendant 60 à 90 secondes, tu te vois perdre exactement la somme "
    "prévue, calmement, en exécutant le SL. Ton système nerveux apprend que cette issue est gérable. "
    "Pendant le trade, si le SL est touché, c'est juste une répétition de quelque chose de déjà vécu."
))

story.append(miroir([
    "Toi, tu fais le contraire. Tu visualises le gain. Tu te projettes à +1500 avant même de cliquer. "
    "Tu te vois faire le screenshot, le poster, ressentir cette satisfaction. Tu pré-vis l'extase. "
    "Le problème c'est que cette pré-vision charge émotionnellement le trade. Quand le marché t'offre +800 "
    "tu refuses de couper parce que tu <b>vises</b> +1500 — c'est dans ta visualisation, c'est presque acquis. "
    "Et quand le marché reverse, tu refuses d'acter parce que +1500 t'avait été mentalement promis.",
    "On va inverser ça. Avant chaque trade, tu vas pré-vivre <b>trois</b> scénarios, dans cet ordre :",
    "<b>Scénario 1 (40 secondes) :</b> tu cliques, le marché part dans le mauvais sens, ton SL est touché. "
    "Tu sens la petite déception. Tu respires. Tu fermes la perte. Tu notes dans ton journal. Tu passes à autre chose. "
    "C'est OK. C'est juste un trade qui s'est terminé. Visualise ce calme post-perte.",
    "<b>Scénario 2 (30 secondes) :</b> tu cliques, le marché part dans ton sens, atteint le TP. Tu coupes. "
    "Tu prends ton gain prévu. Pas plus. Tu fermes la plateforme. Tu te lèves. Visualise le détachement, "
    "pas l'extase. La routine du gain encaissé.",
    "<b>Scénario 3 — le piège +1500 (30 secondes) :</b> tu cliques, le marché part dans ton sens, dépasse ton TP. "
    "Tu approches +1500. <b>Visualise-toi en train de couper.</b> Pas le rêve de +3000. Visualise le clic de fermeture à +1500 "
    "exactement. La sensation un peu frustrante de « j'aurais pu plus ». Et l'absorption de cette frustration "
    "comme prix à payer pour ne pas cramer le compte. Cette visualisation est la plus importante pour toi.",
    "Tu prépares ton système nerveux à <b>survivre à un gros gain</b>. C'est un travail aussi important que la "
    "préparation à une grosse perte. Pour quelqu'un avec ton pattern, c'est même plus important."
]))

story.append(action(
    "À partir de demain : <b>aucun trade exécuté sans visualisation préalable de 90 secondes</b>. Trois scénarios, "
    "dans l'ordre, à voix basse si nécessaire. C'est ton sas. Si tu n'as pas fait la visualisation, "
    "tu ne cliques pas. Période. Tu peux décider d'attendre le prochain setup. Mais tu ne cliques pas sans le sas."
))

story.append(journal([
    "Quand je visualise la coupe à +1500 (alors que je pourrais aller plus loin), qu'est-ce que je ressens dans le corps ? "
    "Que se passe-t-il ?",
    "Le scénario 3 (couper à +1500 dans le plan) déclenche-t-il plus d'inconfort que le scénario 1 (perdre proprement) ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 10 ============
story.extend(chapter_header(10, "Lâcher prise", "Le paradoxe du contrôle"))

story.extend(hougaard_block([
    "Hougaard développe un paradoxe central : plus tu essayes de contrôler le marché, plus tu perds. "
    "Le contrôle est une illusion. Tu ne contrôles pas où va le prix. Tu ne contrôles pas qui achète, qui vend, "
    "quelles nouvelles tombent. La seule chose que tu contrôles, c'est <b>toi</b> : ton entrée, ta taille, ton SL, "
    "ton TP, et le bouton de fermeture.",
    "Le paradoxe : c'est en lâchant prise sur ce que tu ne contrôles pas que tu deviens efficace sur ce que tu contrôles. "
    "Le trader débutant essaye de contrôler le marché. Le trader expérimenté lâche prise sur le marché et contrôle "
    "uniquement sa propre exécution.",
    "Cette posture s'appelle le « surrender opérationnel ». Tu te rends. Tu acceptes l'incertitude. Tu acceptes "
    "que ce trade peut perdre. Tu acceptes que tu ne sais pas ce qui va se passer. Et paradoxalement, "
    "cette acceptation te rend libre d'exécuter sereinement."
]))

story.append(concept(
    "Le contrôle du marché n'existe pas. Plus tu serres, plus tu te brûles. La paix du trader vient d'un acte "
    "de reddition : j'accepte que je ne sais pas. Je joue mon edge, je laisse le marché faire ce qu'il fait."
))

story.append(miroir([
    "Toi, tu es un contrôleur. Tu l'as toujours été. À cheval, tu contrôles le binôme. Sur ATHÉNA, tu contrôles "
    "la production. Dans ton entraînement post-coma, tu as dû reconstruire un contrôle sur un corps et un cerveau "
    "qui ne t'obéissaient plus. Le contrôle est ta stratégie de survie. Lâcher prise n'est pas naturel pour toi — "
    "c'est même associé à la perte (le coma a été un lâcher prise forcé, et tu en es revenu en serrant tout).",
    "Et tu importes cette stratégie en trading. Tu serres. Tu décales un SL pour ne pas perdre le contrôle. "
    "Tu refuses de couper parce que couper c'est admettre que tu ne contrôlais pas. Tu négocies avec le marché "
    "alors que le marché ne négocie pas.",
    "Le travail ici est un travail de différentiation : reconnaître que les domaines où le contrôle marche "
    "(ta filly, ta production 3D, ta rééducation) sont des domaines où ton effort a un impact direct sur le résultat. "
    "Et que le trading est un domaine où ton effort a <b>aucun impact</b> sur le résultat individuel d'un trade. "
    "Le marché ne réagit pas à ta volonté.",
    "Le « close the platform » que Hougaard recommande est puissant pour toi. Quand un trade va contre toi vers le SL : "
    "tu fermes la plateforme. Pas le trade — la plateforme. Tu te lèves. Tu sors. Le SL fait son boulot sans toi. "
    "Tu reviens 30 minutes plus tard. Tu vois le résultat. C'est tout. Tu n'as pas pu interférer parce que tu n'étais pas là.",
    "Au début ça va être atroce. Tu vas avoir envie de revenir devant l'écran toutes les deux minutes. C'est normal. "
    "C'est le sevrage du contrôle. Tu l'as fait avec d'autres choses, tu peux le faire avec ça."
]))

story.append(action(
    "Règle <b>« close the platform »</b> activée cette semaine. Dès qu'un trade est en cours avec SL et TP placés, "
    "tu fermes l'application/le terminal. Téléphone retourné. Tu te lèves. Tu fais autre chose : pansage, marche, "
    "tâche ATHÉNA. Tu reviens uniquement quand le trade s'est résolu (notification de SL ou TP). "
    "Trois jours d'application stricte. Tu vas voir ton PnL changer."
))

story.append(journal([
    "Dans quels domaines de ma vie le contrôle me sert vraiment ? Dans lesquels il me détruit ?",
    "Quand j'imagine fermer la plateforme avec un trade en cours, qu'est-ce que mon corps fait ? "
    "Quelle peur ça active ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 11 ============
story.extend(chapter_header(11, "Ajouter aux gagnants", "Contre-instinct — mais pas encore pour toi"))

story.extend(hougaard_block([
    "Hougaard consacre un chapitre à une pratique des grands traders qu'il a connus : ils rajoutent à leurs trades "
    "<b>gagnants</b>, pas à leurs trades perdants. Tu rajoutes au gagnant quand il a déjà prouvé qu'il est dans la bonne "
    "direction, pas au perdant pour « moyenner ».",
    "Cette technique amplifie les gains sur les gros mouvements et reste ininvasive sur les petits. "
    "Combinée à un SL géré, elle peut transformer le profil de risque/récompense d'une stratégie.",
    "Mais Hougaard met aussi en garde : ajouter aux gagnants demande une discipline d'exécution irréprochable. "
    "Si tu n'as pas déjà cette discipline sur des trades simples, ajouter au gagnant va juste démultiplier "
    "tes problèmes d'exécution. Tu vas pyramider la quantité d'erreur."
]))

story.append(concept(
    "Tu rajoutes uniquement aux trades qui ont déjà prouvé. Jamais à ceux qui essayent encore de prouver. "
    "Mais c'est une technique avancée : avant de l'utiliser, tu dois être capable de gérer un seul trade proprement. "
    "Sinon tu pyramides ton désordre."
))

story.append(miroir([
    "Tu vas être tenté de lire ce chapitre et de te dire « ah ouais c'est exactement ça qu'il me faut pour atteindre +3000 ». "
    "<b>Non.</b> Pour toi, à ce stade, ajouter aux gagnants serait du carburant sur ton pattern destructeur. "
    "Tu prendrais ton +800, tu ajouterais, ça monterait à +2000, tu refuserais de couper, et tu cramerais "
    "deux fois plus vite avec deux positions ouvertes au lieu d'une.",
    "Donc on va prendre une version <b>simplifiée et adaptée à ton cas</b>. La seule technique « avancée » que je "
    "t'autorise pour les 90 prochains jours est celle-ci : <b>SL au break-even dès que le trade atteint +1R</b>. "
    "Pas d'ajout. Pas de pyramide. Juste la sécurité du capital.",
    "Concrètement sur XAUUSD : tu rentres à 2 400, SL à 2 397 (3 dollars), TP à 2 406 (6 dollars). "
    "Dès que le prix touche 2 403 (1R en ta faveur), tu remontes manuellement ton SL à 2 400 — break-even. "
    "À partir de ce moment-là, le pire qui peut t'arriver est de sortir à zéro. Tu as gelé ton downside.",
    "Cette technique simple a un effet psychologique massif pour toi : elle <b>désamorce</b> le piège du gain perdu. "
    "Tu sais que tu ne peux plus perdre. Donc tu n'as plus besoin de défendre la position désespérément. "
    "Tu peux laisser le trade respirer jusqu'au TP sans interférer.",
    "Quand tu auras tenu cette règle 100 trades d'affilée sans la casser, on parlera d'ajouter aux gagnants. "
    "Pas avant. Promesse à toi-même."
]))

story.append(action(
    "Règle <b>BE à +1R</b> non négociable pendant 90 jours. À chaque trade XAUUSD : alarme TradingView ou alerte "
    "sur ta plateforme au niveau +1R. Dès que ça sonne, tu remontes le SL à l'entrée. C'est mécanique. "
    "Tu ne discutes pas avec toi-même à ce moment-là, tu exécutes. "
    "Tu loggues dans ton journal chaque trade : « BE déplacé à temps : OUI/NON »."
))

story.append(journal([
    "Quand j'imagine déplacer mon SL au break-even (donc renoncer à plus de gain si ça reverse direct), "
    "qu'est-ce que je ressens ? Est-ce que ça active un manque ?",
    "Pourquoi est-ce que je serais tenté de ne pas le faire ? Quelle voix intérieure dit « laisse-le tranquille » ?"
]))

story.append(warning(
    "Si tu commences à pyramider sans avoir d'abord maîtrisé la règle simple BE+1R sur 100 trades, "
    "tu vas accélérer ta destruction. Le sevrage de l'intensité passe d'abord par la simplification, "
    "pas par l'optimisation. Tu n'es pas prêt pour l'optimisation. Tu es prêt pour la rigueur de la base."
))

story.append(PageBreak())


# ============ CHAPITRE 12 ============
story.extend(chapter_header(12, "Couper les perdants vite", "La compétence numéro un"))

story.extend(hougaard_block([
    "Si Hougaard ne devait retenir qu'une seule compétence du trading, ce serait celle-ci. La capacité à couper "
    "ses perdants vite est, selon lui, l'écart le plus net entre les traders rentables et les autres. "
    "Avant la lecture du marché. Avant le money management. Avant la psychologie générale.",
    "Pourquoi ? Parce qu'une perte non coupée n'est pas linéaire. Elle a quatre effets cumulés : "
    "1) elle prend du capital, 2) elle prend du temps mental, 3) elle prend de l'attention sur les setups suivants, "
    "4) elle conditionne ton cerveau à accepter des pertes plus grandes au prochain tour.",
    "Le décalage de SL est la version pathologique du « ne pas couper ». Il ne s'agit même plus d'inaction. "
    "C'est une <b>action</b> contre toi-même, contre ton plan. Le décalage de SL est, statistiquement, le geste "
    "qui détruit le plus de comptes."
]))

story.append(concept(
    "Couper vite n'est pas une option. C'est la compétence centrale. Le SL est sacré : tu le poses avec l'entrée, "
    "et il ne bouge que dans une direction — vers le profit, jamais loin de lui. "
    "Décaler un SL est un acte autodestructeur déguisé en patience."
))

story.append(miroir([
    "Ton pattern de décalage de SL est documenté. Tu rentres, le trade va contre toi, tu te dis « il va revenir », "
    "tu décales le SL « juste un peu pour lui laisser le temps ». Cette phrase est ton mensonge personnel. "
    "Le marché n'a pas besoin de temps. Le marché a besoin que tu te trompes pour empocher ton SL. C'est neutre. "
    "C'est mécanique. Tu personnalises ce qui n'est pas personnel.",
    "Et tu as un facteur aggravant : les prop firms. Apex, Topstep, Alpha Futures ont toutes des règles de drawdown "
    "qui amplifient la sanction du décalage. Tu décales un SL XAUUSD, le marché te tape -300, tu décales encore, "
    "il te tape -600. À -800 tu casses la règle trailing drawdown du compte Apex. Compte mort. Tu n'as pas "
    "juste perdu 800 dollars, tu as perdu le compte. Avec les frais d'inscription tu es à -1 000 à -1 500 réels.",
    "C'est exactement le mécanisme que la prop firm utilise comme business model : elle parie que des traders "
    "comme toi vont casser la règle de drawdown rapidement. Elle ne te veut pas du mal, elle exécute son edge à elle. "
    "<b>Toi, tu peux refuser d'être le carburant.</b>",
    "Voici ton protocole anti-décalage de SL en quatre niveaux. C'est un escalier que tu construis cette semaine.",
    "<b>Niveau 1 — SL placé à l'entrée, non négociable.</b> Avec l'ordre. Pas après. Pas « je vais voir ». "
    "Avec l'ordre. Si tu cliques Buy, tu cliques SL dans la seconde.",
    "<b>Niveau 2 — Alerte visuelle.</b> Tu places à côté du SL une grosse ligne rouge avec une alerte sonore. "
    "Quand le marché s'en approche, ton cerveau a déjà commencé à anticiper la perte (cf. chapitre 9, visualisation). "
    "Tu sais ce qui va se passer.",
    "<b>Niveau 3 — Engagement physique.</b> Tu écris sur une feuille avant l'ouverture de la session : « JE NE DÉCALE PAS DE SL AUJOURD'HUI ». "
    "Tu signes en bas. Tu colles la feuille au mur derrière l'écran. Petit, ridicule, mais ça active la conscience "
    "au moment du déclencheur.",
    "<b>Niveau 4 — Close the platform.</b> Si malgré tout tu sens que tu vas décaler, tu ne décales pas — "
    "tu fermes la plateforme. Tu laisses le SL travailler. Tu reviens après. Si tu sens que tu vas tricher, tu disparais."
]))

story.append(action(
    "Implémente les quatre niveaux dès demain matin. Imprime le protocole. Affiche-le. "
    "Sur ton journal de session, en bas de chaque page, une croix verte si tu n'as pas décalé, "
    "une croix rouge si tu as décalé. Vise <b>zéro croix rouge sur 20 sessions consécutives</b>. "
    "Si tu casses une fois, tu repars à zéro. Sans drame. Mais tu repars à zéro."
))

story.append(journal([
    "Sur mes 10 derniers décalages de SL, à quel niveau de PnL flottant je l'ai fait ? Y a-t-il un seuil récurrent ?",
    "Quelle est la phrase exacte que je me dis dans la tête au moment de décaler ? Écris-la mot pour mot.",
    "Quel serait le coût total sur 12 mois si je ne décalais plus jamais ? Estime."
]))

story.append(warning(
    "Si tu lis ce chapitre et que tu te dis « OK c'est bien mais des fois ça revient », tu n'as rien lu. "
    "Le fait que parfois ça revient est exactement ce qui rend le décalage de SL si destructeur : le renforcement "
    "intermittent est la forme de conditionnement la plus puissante connue en psychologie. Le décalage qui paye une fois "
    "sur dix te conditionne plus solidement que le décalage qui paye à chaque fois. Tu deviens un pigeon de Skinner. "
    "Tu cherches le grain qui tombe parfois. <b>La règle est : zéro décalage. Pas même un.</b>"
))

story.append(PageBreak())


# ============ CHAPITRE 13 ============
story.extend(chapter_header(13, "Le journal", "L'outil de transformation numéro un"))

story.extend(hougaard_block([
    "Le journal de trading est, selon Hougaard, l'outil de transformation le plus puissant à la disposition du trader. "
    "Pas un journal de PnL — n'importe quel logiciel fait ça. Un journal <b>introspectif</b>, manuscrit, où tu écris ton "
    "état émotionnel avant, pendant et après chaque trade, et chaque session.",
    "Pourquoi manuscrit ? Parce que l'acte d'écrire à la main mobilise différemment le cerveau que la frappe au clavier. "
    "Tu écris plus lentement, donc tu réfléchis plus profondément. Tu peux moins fuir : c'est plus engageant que de "
    "remplir un champ de logiciel.",
    "Le journal sert trois fonctions : 1) acter ce qui s'est passé (mémoire externe), 2) repérer tes patterns à travers "
    "le temps (l'analyse rétrospective des sessions est l'endroit où la transformation se produit), "
    "3) construire l'identité du trader que tu deviens (en t'observant écrire, tu deviens cette personne)."
]))

story.append(concept(
    "Pas de journal manuscrit, pas de transformation. C'est aussi simple que ça. Tout le reste est "
    "consommation passive de contenu. Le journal est le seul endroit où ta tête se rencontre vraiment, "
    "et où le changement peut s'enraciner."
))

story.append(miroir([
    "Toi, tu prends des notes sur ton téléphone, parfois. Ou rien. Ou tu te promets de tenir un journal et tu craques après trois jours. "
    "C'est l'erreur classique. Tu rates l'outil qui est précisément celui dont tu as besoin.",
    "Voici le format. Tu vas acheter un beau cahier — pas un carnet bas de gamme, un <b>vrai cahier</b> que tu auras "
    "envie d'ouvrir. Cuir, papier épais, ce que tu veux mais que tu respectes. Sur la page de couverture intérieure, "
    "tu écris une phrase : « Cahier de Marien, trader chirurgical en formation. Ouvert le [date]. » "
    "Ce cahier devient sacré. On ne fait pas n'importe quoi dedans.",
    "Le template à utiliser est en annexe à la fin de ce document. Tu le recopies à la main au début. "
    "Pas de tablette, pas de Notion, pas d'Excel.",
    "L'objectif n'est pas que tu te transformes en moine. L'objectif est de créer un point d'ancrage quotidien "
    "où le « toi qui s'observe » rencontre le « toi qui exécute ». Sans ce point d'ancrage, le toi qui exécute "
    "fait ce qu'il veut et le toi qui s'observe lit des livres en parallèle. Ils ne se parlent jamais.",
    "Pour quelqu'un qui pratique Joe Dispenza, le journal est la version écrite de ta méditation : c'est l'observation "
    "consciente de tes patterns en mode écrit. C'est la même opération neurologique. Tu installes la position "
    "d'observateur. À force, tu deviens cet observateur même pendant le trade — et c'est là que tu reprends "
    "le contrôle de tes décisions."
]))

story.append(action(
    "Cette semaine : tu achètes le cahier. Tu recopies à la main la première page du template d'annexe. "
    "Tu remplis le journal à chaque session — sans exception — pendant les six semaines à venir. "
    "Si tu skip une session, tu ne trades pas la suivante. Pas négociable. Le journal est la condition d'accès à l'écran."
))

story.append(journal([
    "Quel cahier je vais choisir ? Vais-je le prendre au sérieux ou est-ce que je vais saboter cet outil aussi ?",
    "Quelle est ma résistance face à écrire à la main mes émotions ? Honte, paresse, peur de me voir ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 14 ============
story.extend(chapter_header(14, "L'inner game", "Le vrai adversaire est intérieur"))

story.extend(hougaard_block([
    "Hougaard reprend ici une notion popularisée par Timothy Gallwey dans le tennis et le sport : "
    "l'inner game. L'idée que l'adversaire que tu affrontes n'est pas l'extérieur (l'autre joueur, le marché) "
    "mais une voix intérieure qui te commente, te juge, te déstabilise.",
    "Cette voix intérieure — parfois appelée « Self 1 » — est constamment active. Elle évalue, elle compare, "
    "elle anticipe. En trading elle te dit « tu vas le rater », « tu vas exploser », « tu n'es pas à la hauteur », "
    "ou inversement « tu maîtrises, tu peux y aller plus fort, tu es au-dessus ». Les deux versions sont des "
    "interférences.",
    "Le but de l'inner game n'est pas de faire taire cette voix — c'est impossible. C'est d'apprendre à <b>l'observer "
    "sans lui obéir</b>. Tu l'entends parler, tu la reconnais, tu continues à exécuter ton protocole. La voix devient "
    "une compagne, plus une dirigeante."
]))

story.append(concept(
    "Ton adversaire n'est pas le marché. C'est la voix dans ta tête qui commente le marché. "
    "Le jeu intérieur consiste à entendre cette voix sans lui obéir. Tu la prends en flagrant délit. "
    "Tu la nommes. Tu la regardes parler. Et tu cliques selon ton plan, pas selon elle."
))

story.append(miroir([
    "Voici à quoi ressemble ton dialogue interne typique en trade, je vais l'écrire pour que tu le reconnaisses :",
    "<i>« OK setup propre, FVG marquée, killzone NY, je rentre. Allez ça doit marcher celui-là. "
    "Bon ça commence à monter, c'est good. Putain je devrais peut-être augmenter la taille, je sens que ça va exploser. "
    "Non, reste calme. +400. +600. +800. C'est mon TP, je devrais couper. Mais regarde la momentum, c'est en train de "
    "vraiment décoller. Si je coupe maintenant je vais regretter. +1000. +1200. Voilà tu vois, t'avais raison "
    "d'attendre. +1500. OK on s'approche, garde encore un peu. Oh ça ralentit. Bon c'est juste une respiration. "
    "+1400. Ouais c'est temporaire. +1200. Putain ça redescend. Mais ça va repartir, le contexte est haussier. "
    "+800. Bon là je devrais couper, j'ai laissé filer. Mais si je coupe à +800 alors que j'étais à +1500 c'est "
    "comme si j'avais perdu 700. Non, j'attends que ça remonte à +1200. +400. Ouais bon c'est mort. Non, ça va repartir. "
    "+0. Putain. Non non non, ça va repartir. -200. OK je décale mon SL c'est juste un retest. -400. Allez retest. "
    "-600. Mais merde. -800. Compte cramé. »</i>",
    "Tu reconnais ? Cette voix est constante, rapide, et elle te ment à chaque phrase. Mais elle est crédible "
    "parce qu'elle <b>est toi</b>. Du moins une partie de toi.",
    "Le travail de l'inner game pour toi consiste à apprendre à entendre cette voix comme une radio qui passe en arrière-plan. "
    "Pas comme la commande de l'avion. Tu peux dire à voix basse pendant le trade : « j'entends ma voix qui veut "
    "que je laisse courir, je la note, et j'exécute mon plan ». Cette phrase casse l'identification. Tu n'es plus "
    "la voix. Tu es la conscience qui écoute la voix.",
    "La méditation Dispenza t'a déjà entraîné à cette posture. Quand tu médites et que tu observes tes pensées sans "
    "les suivre, c'est exactement le même muscle qui s'entraîne. Le problème c'est que tu n'utilises pas ce muscle "
    "devant l'écran. Tu médites le matin, tu deviens un junkie devant l'écran l'après-midi. Il faut que ce soit "
    "le <b>même</b> Marien dans les deux contextes. Le matin pose les fondations. L'après-midi te demande de "
    "tenir debout sur ces fondations."
]))

story.append(action(
    "Pendant tes trades cette semaine, tu vas dire à voix basse — vraiment à voix basse — une phrase au moment "
    "des déclencheurs émotionnels. Choisis-en une : « j'entends la voix, je continue le plan » ou simplement "
    "« voix notée ». L'intérêt n'est pas la phrase. L'intérêt est la rupture entre toi et ta voix. "
    "Tu crées une distance. Cette distance est le siège de la liberté."
))

story.append(journal([
    "Si je devais nommer la voix qui me parle pendant les trades, comment je l'appellerais ? "
    "(Quelqu'un l'appelle Charlie, ou Bob, ou « le saboteur ». Donne-lui un nom.)",
    "Cette voix a-t-elle l'âge de Marien aujourd'hui, ou celui de Marien adolescent ? À quel moment de ma vie "
    "elle s'est installée ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 15 ============
story.extend(chapter_header(15, "Devenir le trader", "Le changement identitaire en trois niveaux"))

story.extend(hougaard_block([
    "Hougaard conclut son analyse psychologique en proposant un cadre de changement à trois niveaux. "
    "Il rejoint ici, sans le citer toujours, le modèle popularisé par James Clear dans <i>Atomic Habits</i> : "
    "les niveaux de transformation sont superposés et seul le plus profond produit du changement durable.",
    "<b>Niveau 1 — Résultat.</b> Tu vises un résultat (« je veux gagner 10 000€ ce mois »). C'est le niveau le plus "
    "instable. Le résultat dépend de variables hors de ton contrôle. Tu peux faire tout juste et le rater. "
    "Tu peux faire tout faux et l'atteindre (chance). Donc baser ta motivation et ton identité dessus est précaire.",
    "<b>Niveau 2 — Processus.</b> Tu vises un processus (« je vais exécuter mon protocole 100 trades »). C'est plus "
    "stable. Tu contrôles le processus. Mais le processus tient tant que tu te récompenses pour le résultat. "
    "Si trois semaines passent sans résultat, le processus s'effrite.",
    "<b>Niveau 3 — Identité.</b> Tu deviens quelqu'un dont le processus est l'expression naturelle. "
    "« Je suis un trader chirurgical. » Pas « je veux trader chirurgicalement ». Pas « je vais le faire ». "
    "« Je le <b>suis</b>. » À ce niveau, le processus ne demande plus de discipline — il demande de la cohérence "
    "avec qui tu es. Et la cohérence est beaucoup plus stable que la discipline.",
    "Le travail consiste à descendre du niveau 1 (où tu es actuellement coincé) au niveau 3, en passant par "
    "le niveau 2. La descente prend du temps. Elle se fait par des actes répétés, pas par des affirmations creuses."
]))

story.append(concept(
    "Tu ne deviens pas un trader rentable en gagnant de l'argent. Tu gagnes de l'argent parce que tu es "
    "devenu un trader rentable. L'ordre compte. Identité d'abord, comportement ensuite, résultat enfin. "
    "Pas l'inverse."
))

story.append(miroir([
    "Aujourd'hui ton identité de trader est instable. Quand tu gagnes, tu es « un trader qui réussit ». Quand tu perds, "
    "tu es « un trader qui galère ». Ton identité fluctue avec ton PnL. C'est pour ça que tu ne peux pas être stable "
    "dans tes décisions : l'opérateur change selon le résultat de l'opération précédente.",
    "Tu vas choisir une identité cible. Je te propose celle-ci, à toi de l'ajuster mais je pense qu'elle te va : "
    "<b>« Je suis un trader chirurgical. »</b>",
    "Décomposons. Chirurgical veut dire : précis, calme, ennuyeux à observer de l'extérieur, exécution propre, "
    "pas de geste superflu, pas d'émotion visible. Un chirurgien ne « croit » pas qu'une opération va marcher. "
    "Il ouvre, il fait le geste prévu, il referme. Il sait qu'il existe une distribution de réussite. Il assume.",
    "Quand tu adoptes cette identité, plusieurs choses deviennent <b>cohérentes</b> et donc faciles. Un chirurgien ne "
    "double pas sur une perte. Ça n'a aucun sens. Un chirurgien ne décale pas son SL. Ça n'a aucun sens. "
    "Un chirurgien ne court pas après le gain de la veille. Il fait son geste, il rentre chez lui. "
    "Tu vois comment l'identité résout le problème de discipline ? Tu n'as pas à te forcer. C'est juste qui tu es.",
    "Le problème c'est que cette identité doit être <b>installée</b>. Elle ne s'auto-installe pas en lisant cette page. "
    "Elle s'installe par des actes répétés qui sont cohérents avec elle. Chaque fois que tu coupes un SL sans le décaler, "
    "tu déposes un vote pour cette identité. Chaque fois que tu prends ton TP sans le pousser, tu déposes un vote. "
    "À force de votes, l'identité devient majoritaire dans ta perception de toi.",
    "C'est l'inverse aussi qui marche : chaque décalage de SL, chaque dépassement de TP, est un vote pour l'identité "
    "« je suis un trader émotionnel qui crame ses comptes ». Tu votes pour l'une ou pour l'autre, à chaque clic. "
    "Tu choisis qui tu deviens dans l'année à venir.",
    "Cavalier en saut d'obstacles tu l'as déjà fait. Tu ne t'es pas réveillé un matin cavalier compétitif. "
    "Tu as fait des milliers d'heures de selle, et à un moment l'identité « cavalier » est devenue ta vérité, "
    "pas un projet. Le trading suit la même loi. Tu fais le geste cohérent assez de fois, l'identité s'installe. "
    "Et là tout devient simple."
]))

story.append(action(
    "Écris dans ton journal cette phrase, en majuscules, sur une page dédiée : "
    "<b>« JE SUIS UN TRADER CHIRURGICAL. »</b> "
    "Avant chaque session, relis cette page. Avant chaque trade, demande-toi : « est-ce qu'un trader chirurgical "
    "ferait ce clic ? ». Si la réponse est non, tu ne cliques pas. Tu attends le clic dont la réponse est oui."
))

story.append(journal([
    "Quelle identité de trader je porte actuellement, sans m'en rendre compte ? Si je m'observais de l'extérieur, "
    "qu'est-ce que je dirais de moi en trade ?",
    "Si je devenais un trader chirurgical à 30 ans (donc dans cinq ans), quelle première décision je dois prendre "
    "aujourd'hui pour que ça soit possible ?"
]))

story.append(PageBreak())


# ============ CHAPITRE 16 ============
story.extend(chapter_header(16, "Conclusion", "Les dix principes finaux"))

story.extend(hougaard_block([
    "En clôture, Hougaard récapitule sa pensée en une série de principes qui synthétisent les chapitres précédents. "
    "Ces principes ne sont pas des règles techniques — c'est délibéré. Aucun ne te dit comment lire un graphique. "
    "Tous te disent comment <b>te tenir</b> face au marché.",
    "Je te restitue ces principes dans une version adaptée à ton contexte. Tu les retrouveras "
    "ensuite dans la synthèse finale, où ils seront reformulés comme « les dix commandements de Marien » "
    "pour que tu puisses les imprimer et les scotcher au-dessus de ton écran."
]))

story.append(P("Les dix principes en synthèse rapide", h_section))

principles_short = [
    ("1. L'edge n'est pas dans la méthode.", "Ta méthode SMC est suffisante. Le levier est dans l'exécution."),
    ("2. Tu joues une distribution, pas un trade.", "Tu ne sais pas si celui-là va gagner. Tu sais ce que donne ta série."),
    ("3. Tes pertes sont sacrées.", "Ce qui définit un grand trader, c'est comment il perd. Petit, vite, calme."),
    ("4. Ton SL ne se touche pas.", "Sauf pour le serrer vers le profit. Jamais l'éloigner. Jamais."),
    ("5. Tu n'es pas tes trades.", "Un trade qui rate n'est pas Marien qui rate. Tu sépares résultat et identité."),
    ("6. Tu pré-vis la perte.", "Avant chaque clic, scénarios visualisés. Le sas est non négociable."),
    ("7. Tu fermes la plateforme.", "Une fois SL/TP placés, tu sors physiquement de l'écran. Tu laisses faire."),
    ("8. Tu tiens un journal manuscrit.", "Chaque session, chaque trade. Sans exception. C'est ton outil principal."),
    ("9. Tu nourris une vie hors écran.", "ATHÉNA, chevaux, box, relations. Si ta vie est plate, l'écran te bouffe."),
    ("10. Tu deviens, tu ne forces pas.", "Trader chirurgical n'est pas un objectif. C'est l'identité que tu installes."),
]
for title, sub in principles_short:
    story.append(P("<b>" + title + "</b> " + sub, body))

story.append(Spacer(1, 10))
story.append(concept(
    "Tu as maintenant lu ce que dit Hougaard. La phase suivante n'est plus dans les pages. "
    "Elle est dans le cahier, devant l'écran, et dans tes décisions du jour. Le livre est terminé. "
    "Ton vrai travail commence."
))

story.append(miroir([
    "Tu es au bout des seize chapitres. Si tu as appliqué un par un, tu as déjà commencé à devenir quelqu'un d'autre. "
    "Si tu as juste lu en diagonale, tu n'as rien changé — tu as juste ajouté un livre à ta bibliothèque de trader.",
    "Ce qui suit dans ce document est la cartographie pratique des 90 prochains jours. C'est elle qui va transformer "
    "les idées en réalité. Si tu sautes cette partie, tout ce qui précède est intellectuel. C'est dans la suite "
    "que tout se joue."
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
    "Ce qui suit est à imprimer en grand, à scotcher au-dessus de ton écran, et à relire à voix haute chaque matin "
    "avant la session. Si tu trouves ça ridicule, tant mieux : ton cerveau émotionnel n'a pas honte du ridicule, "
    "il a juste besoin d'ancrage."
))
story.append(Spacer(1, 12))

commandments = [
    ("I.", "Ma méthode est suffisante. Je suis le problème, et je suis aussi la solution.",
     "SMC + killzones + risk fixe = système viable. Le levier n'est pas technique. Il est dans ma main qui clique."),
    ("II.", "Je joue une série, jamais un trade.",
     "Cent setups exécutés proprement. Je ne tire aucune conclusion avant cent. Je suis le casino, pas le joueur."),
    ("III.", "Mon stop loss est sacré et ne bouge jamais vers la perte.",
     "Placé avec l'entrée. Déplacé uniquement vers le BE à +1R, puis vers le profit. Jamais agrandi. Jamais."),
    ("IV.", "Je coupe à mon TP. Point.",
     "Le piège +1500 est ma signature destructrice. Je l'ai cartographié. Je le casse en respectant le TP préfixé."),
    ("V.", "Je pré-vis chaque trade pendant 90 secondes avant de cliquer.",
     "Trois scénarios : perte propre, gain propre, gain qui dépasse mon TP et que je coupe quand même. Sas non négociable."),
    ("VI.", "Je ferme la plateforme dès que les ordres sont placés.",
     "Une fois SL et TP en place, je me lève. Je sors de la pièce. Je laisse le trade respirer sans moi."),
    ("VII.", "J'écris mon journal manuscrit à chaque session, sans exception.",
     "Pas de journal = pas de session le lendemain. C'est la condition d'accès à l'écran."),
    ("VIII.", "Je ne consomme aucun contenu trading hors application.",
     "Pas de nouvelle vidéo, pas de nouveau mentor, pas de nouveau setup. Six semaines de purge. J'applique, point."),
    ("IX.", "Je nourris ma vie hors écran chaque jour.",
     "ATHÉNA, mes chevaux, ma filly, box, lectures, relations, soleil. Une vie plate produit un trader saboteur."),
    ("X.", "Je suis un trader chirurgical. Ce n'est pas un objectif, c'est qui je deviens.",
     "Chaque clic est un vote. Je vote pour cette identité, ou je vote contre. Pas d'entre-deux. Chaque jour. Chaque trade."),
]

for roman, titre, detail in commandments:
    block_data = [[
        Paragraph(f"<font color='#D4AF37'><b>{roman}</b></font>", ParagraphStyle("rn", fontName="DejaVu-Serif-Bold", fontSize=24, textColor=GOLD)),
        [
            Paragraph(f"<b>{titre}</b>", ParagraphStyle("ct", fontName="DejaVu-Bold", fontSize=12, leading=15, textColor=DARK_BG)),
            Paragraph(detail, ParagraphStyle("cd", fontName="DejaVu", fontSize=10, leading=13.5, textColor=MID_GREY, alignment=TA_JUSTIFY)),
        ]
    ]]
    t = Table(block_data, colWidths=[1.5 * cm, 14.5 * cm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("LINEBELOW", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
    ]))
    story.append(t)
    story.append(Spacer(1, 4))

story.append(Spacer(1, 12))
story.append(P(
    "Imprime cette liste. Plastifie-la si tu veux. Mais qu'elle soit visible. Tous les jours. "
    "Sans elle à portée de regard, tu vas oublier — ton cerveau émotionnel est puissant et rapide.",
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

story.append(P(
    "Ce qui suit est ta carte routière. Trois phases de 30 jours. Chacune a un objectif spécifique, "
    "des règles de trading précises, un travail psychologique dédié, des soins du corps, et des métriques "
    "claires pour savoir si tu peux passer à la phase suivante. <b>Si tu rates les métriques d'une phase, "
    "tu ne passes pas à la suivante. Tu refais la phase.</b>"
))
story.append(Spacer(1, 14))


# ---- PHASE 1 ----
story.append(P("Phase 1 — Jours 1 à 30", phase_title))
story.append(P("Sevrage et fondations", h_section))

story.append(P(
    "<b>Objectif :</b> casser les automatismes destructeurs et installer les routines de base. Cette phase est "
    "la plus difficile psychologiquement. Tu vas avoir envie de trader, et tu ne tradera pas — pas en réel, en tout cas. "
    "C'est l'équivalent d'un sevrage. Tu réapprends à exister sans le shoot.", body
))

story.append(P("Trading", small_label))
story.append(P(
    "<b>Semaines 1 et 2 :</b> arrêt total du trading. Aucun ordre passé, aucun compte ouvert, "
    "aucune connexion Apex/Topstep/Alpha. Tu ne regardes même plus les charts. Tu désinstalles les apps "
    "sur ton téléphone. Tu te coupes le shoot.", body
))
story.append(P(
    "<b>Semaines 3 et 4 :</b> reprise uniquement en démo (simulateur ou compte non funded). Application stricte "
    "du protocole : SL non négociable, BE+1R systématique, TP fixe, fermeture de la plateforme après placement. "
    "Minimum 30 trades en démo avec zéro décalage de SL avant de passer à la phase 2.", body
))

story.append(P("Psychologie", small_label))
story.append(P(
    "Lecture d'un chapitre tous les deux jours de ce document. Application des actions concrètes. "
    "Tu commences ton cahier manuscrit dès le jour 1. Tu écris chaque soir 15 minutes : ce que tu as ressenti dans la journée, "
    "ce que tu as fait à la place du trading, ce que tu as appris. Méditation Joe Dispenza 20 minutes minimum chaque matin.", body
))

story.append(P("Corps", small_label))
story.append(P(
    "Trois séances physiques intenses par semaine minimum. Box, équitation cross, sport explosif au choix. "
    "Tu sors l'intensité hors écran. Sommeil priorisé : couché avant 23h, levé 7h-8h, pas de téléphone après 22h. "
    "Hydratation, alimentation basique propre. Ton TBI demande une régulation neuro-vagale — la base physique en est la clé.", body
))

story.append(P("Métriques de validation pour passer en phase 2", small_label))
story.append(P(
    "•  30 jours sans aucun trade réel<br/>"
    "•  Minimum 30 trades démo exécutés selon protocole strict<br/>"
    "•  Zéro décalage de SL sur ces 30 trades<br/>"
    "•  Journal rempli chaque jour, sans exception (28 entrées minimum sur 30 jours)<br/>"
    "•  Trois séances physiques par semaine minimum sur les 4 semaines<br/>"
    "•  Méditation quotidienne (25/30 jours minimum)", body
))
story.append(Spacer(1, 10))

story.append(warning(
    "Si à J+30 tu as triché — même une fois sur un compte réel, même un trade « juste pour voir » — "
    "tu reprends la phase 1 à zéro. Pas par punition. Parce que la phase 1 a pour seul objectif de désinstaller "
    "le réflexe de trader pour soulager l'envie. Si l'envie a gagné une fois, le réflexe est encore là. "
    "Tu reprends. C'est non négociable."
))

story.append(PageBreak())


# ---- PHASE 2 ----
story.append(P("Phase 2 — Jours 31 à 60", phase_title))
story.append(P("Transition réel", h_section))

story.append(P(
    "<b>Objectif :</b> repasser en compte réel avec une exposition contrôlée. Tu n'es pas là pour faire de l'argent. "
    "Tu es là pour <b>installer le comportement</b> en conditions réelles, où la dimension monétaire active à nouveau "
    "tes circuits dopaminergiques. C'est la phase test.", body
))

story.append(P("Trading", small_label))
story.append(P(
    "Tu rouvres <b>un seul</b> compte prop firm — pas trois, pas deux. Un. Le plus petit que tu puisses te permettre, "
    "Apex 25K évaluation par exemple. Tu te concentres sur un seul compte. Pas de pyramide multi-comptes : "
    "elle multiplie l'intensité et casse ta concentration.", body
))
story.append(P(
    "Règles strictes : 1 à 2 trades XAUUSD par session maximum. Risque par trade plafonné à 0,5% du compte. "
    "SL placé avec l'entrée. BE à +1R automatique. TP fixe préfixé. Fermeture de la plateforme une fois "
    "les ordres en place. Aucune intervention manuelle pendant le trade.", body
))
story.append(P(
    "Si trois pertes consécutives dans une session : arrêt immédiat de la journée. Si deux pertes consécutives "
    "dans une semaine : pause d'une journée complète sans aucun trading.", body
))

story.append(P("Psychologie", small_label))
story.append(P(
    "Continuation de la lecture de ce document, deuxième passage si nécessaire sur les chapitres 7, 11, 12, 15. "
    "Journal manuscrit obligatoire : sans journal du soir, pas de session le lendemain. "
    "Visualisation pré-trade de 90 secondes systématique. Toujours méditation matinale 20 minutes minimum.", body
))

story.append(P("Corps", small_label))
story.append(P(
    "Maintien des trois séances par semaine minimum. Suivi du sommeil avec une montre ou app si tu peux. "
    "Surveillance des marqueurs neuro-vag : tremblements, irritabilité, sommeil. Si dégradation : pause trading "
    "et travail corps prioritaire pendant 48h.", body
))

story.append(P("Métriques de validation pour passer en phase 3", small_label))
story.append(P(
    "•  30 jours de trading réel sans casser une règle de prop firm<br/>"
    "•  Zéro décalage de SL sur la phase entière<br/>"
    "•  BE+1R appliqué systématiquement (vérifiable dans le journal)<br/>"
    "•  Aucune session sans journal (28/30 minimum)<br/>"
    "•  PnL n'est pas une métrique de validation — ce qui compte c'est le respect du protocole<br/>"
    "•  Si protocole respecté à 100%, peu importe que tu sois en gain ou perte à J+60 : tu passes", body
))

story.append(Spacer(1, 8))
story.append(concept(
    "En phase 2, tu ne juges pas ta réussite à ton PnL. Tu la juges à ton respect du protocole. "
    "Si tu respectes à 100% et que tu es en perte de 5%, tu as réussi. "
    "Si tu casses le protocole une fois et que tu es en profit de 10%, tu as raté. Ordre des valeurs : protocole d'abord."
))

story.append(PageBreak())


# ---- PHASE 3 ----
story.append(P("Phase 3 — Jours 61 à 90", phase_title))
story.append(P("Consolidation et décision", h_section))

story.append(P(
    "<b>Objectif :</b> ancrer l'identité du trader chirurgical et décider, à J+90, comment scaler. "
    "Cette phase est moins technique que les précédentes. Elle est identitaire. Tu installes la "
    "version définitive du trader que tu deviens.", body
))

story.append(P("Trading", small_label))
story.append(P(
    "Continuation des règles de la phase 2 sur le compte unique. Si la phase 2 s'est terminée avec un compte funded, "
    "tu peux passer en exécution sur ce compte funded avec les mêmes règles. Pas d'augmentation de taille avant J+90.", body
))
story.append(P(
    "À partir de J+75, tu peux commencer à tester (en parallèle, en démo) la technique « ajouter aux gagnants » "
    "du chapitre 11. Mais uniquement en démo. La technique en réel arrivera après J+90 si tout le reste est ancré.", body
))

story.append(P("Psychologie", small_label))
story.append(P(
    "Travail identitaire central. Tu relis chaque jour la liste des 10 commandements. Tu poses une question simple "
    "à la fin de chaque session dans ton journal : <b>« Aujourd'hui, est-ce que j'ai voté pour le trader chirurgical, "
    "ou contre ? »</b> Tu réponds honnêtement. Tu observes la tendance sur 30 jours.", body
))
story.append(P(
    "Tu peux à ce stade commencer à parler à un coach ou un thérapeute spécialisé en trauma (si pas déjà fait). "
    "Ton TBI 2022 a probablement laissé des séquelles régulatrices que la méditation seule ne résoudra pas complètement. "
    "Un travail somatique (TRE, somatic experiencing) pourrait massivement aider.", body
))

story.append(P("Corps", small_label))
story.append(P(
    "Maintien et progression. Si possible reprise des compétitions équestres à un rythme soutenable. "
    "ATHÉNA gagne en place dans ta semaine. Le trading prend <b>moins</b> de place mentale relative, pas plus.", body
))

story.append(P("Décision à J+90", small_label))
story.append(P(
    "À la fin du jour 90, tu prends rendez-vous avec toi-même. Tu relis tout ton journal. Tu analyses tes 90 jours. "
    "Tu réponds à trois questions :", body
))
story.append(P(
    "1. <b>Est-ce que je suis devenu le trader chirurgical ?</b> (oui / partiellement / non, avec preuves dans le journal)", body
))
story.append(P(
    "2. <b>Mon protocole est-il rentable sur 90 jours ?</b> (analyse honnête du PnL, sans excuses)", body
))
story.append(P(
    "3. <b>Ai-je trouvé une vie hors écran qui me nourrit ?</b> (ATHÉNA, chevaux, box, relations — concret)", body
))
story.append(P(
    "Selon les réponses : tu scales (augmente la taille, ouvre un deuxième compte, intègres l'ajout au gagnant), "
    "tu prolonges la phase 3 de 30 jours, ou tu reviens à la phase 2 pour ancrer plus profondément. "
    "Pas d'orgueil dans la décision. C'est de l'ingénierie.", body
))

story.append(Spacer(1, 10))
story.append(miroir([
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
    "Reproduis-les exactement. Le copier-coller mental tue le journal. La main qui trace les questions "
    "fait partie du processus.", body
))
story.append(Spacer(1, 10))

# Avant session
story.append(P("AVANT SESSION (5 minutes)", h_section))
avant_data = [
    ["Date :", ""],
    ["État émotionnel (1 à 10) :", ""],
    ["Qualité du sommeil :", ""],
    ["Niveau d'énergie :", ""],
    ["Killzone visée :", "London / NY"],
    ["Bias macro XAUUSD :", ""],
    ["Setup que je guette :", ""],
    ["Taille max autorisée aujourd'hui :", ""],
    ["Phrase d'ancrage :", "Je suis un trader chirurgical."],
    ["Engagement de la session :", "Aucun décalage de SL. BE à +1R systématique. TP fixe."],
]
t = Table(avant_data, colWidths=[6.5 * cm, 9.5 * cm])
t.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "DejaVu-Bold"),
    ("FONTNAME", (1, 0), (1, -1), "DejaVu"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("TEXTCOLOR", (0, 0), (-1, -1), TEXT),
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(t)
story.append(Spacer(1, 14))

# Pour chaque trade
story.append(P("POUR CHAQUE TRADE", h_section))
trade_data = [
    ["Heure d'entrée :", ""],
    ["Direction :", "Long / Short"],
    ["Prix d'entrée :", ""],
    ["SL :", ""],
    ["TP :", ""],
    ["Taille :", ""],
    ["Justification SMC (1 phrase) :", ""],
    ["Visualisation 90s faite :", "OUI / NON"],
    ["État corps à l'entrée :", ""],
    ["BE déplacé à +1R :", "OUI / NON / N/A"],
    ["Résultat :", "TP / SL / BE / Manuel (pourquoi ?)"],
    ["Décalage SL :", "OUI (raison) / NON"],
    ["Plateforme fermée après ordres :", "OUI / NON"],
    ["État corps à la sortie :", ""],
]
t = Table(trade_data, colWidths=[6.5 * cm, 9.5 * cm])
t.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "DejaVu-Bold"),
    ("FONTNAME", (1, 0), (1, -1), "DejaVu"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("TEXTCOLOR", (0, 0), (-1, -1), TEXT),
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(t)

story.append(PageBreak())

# Après session
story.append(P("APRÈS SESSION (10 minutes)", h_section))
apres_data = [
    ["Nombre de trades :", ""],
    ["Gagnants / Perdants :", ""],
    ["PnL session :", ""],
    ["Protocole respecté à 100% ? :", "OUI / NON (détails)"],
    ["Pattern destructeur déclenché ? :", "P1 / P2 / P3 / P4 / P5 / aucun"],
    ["Voix intérieure dominante :", ""],
    ["Émotion la plus présente :", ""],
    ["Une chose à corriger demain :", ""],
    ["Une chose à célébrer (même petite) :", ""],
    ["Vote du jour :", "Trader chirurgical / Trader émotionnel"],
]
t = Table(apres_data, colWidths=[6.5 * cm, 9.5 * cm])
t.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "DejaVu-Bold"),
    ("FONTNAME", (1, 0), (1, -1), "DejaVu"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("TEXTCOLOR", (0, 0), (-1, -1), TEXT),
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(t)
story.append(Spacer(1, 14))

# Revue hebdomadaire
story.append(P("REVUE HEBDOMADAIRE (30 minutes, dimanche soir)", h_section))
revue_data = [
    ["Semaine du :", ""],
    ["Nombre de sessions :", ""],
    ["Nombre de trades :", ""],
    ["Win rate :", ""],
    ["PnL semaine :", ""],
    ["Pattern destructeur le plus fréquent :", ""],
    ["Vote de la semaine :", "Combien de votes chirurgical / combien contre"],
    ["3 leçons de la semaine :", ""],
    ["Engagement principal pour la semaine prochaine :", ""],
    ["État du corps cette semaine (sommeil/énergie/nerveux) :", ""],
    ["Vie hors écran (qualité, quantité) :", ""],
    ["Méditation (sessions tenues) :", ""],
]
t = Table(revue_data, colWidths=[6.5 * cm, 9.5 * cm])
t.setStyle(TableStyle([
    ("FONTNAME", (0, 0), (0, -1), "DejaVu-Bold"),
    ("FONTNAME", (1, 0), (1, -1), "DejaVu"),
    ("FONTSIZE", (0, 0), (-1, -1), 9.5),
    ("TEXTCOLOR", (0, 0), (-1, -1), TEXT),
    ("BACKGROUND", (0, 0), (-1, -1), CREAM),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOX", (0, 0), (-1, -1), 0.6, GOLD),
    ("INNERGRID", (0, 0), (-1, -1), 0.3, GOLD_SOFT),
]))
story.append(t)
story.append(Spacer(1, 14))

story.append(P(
    "Une chose à retenir : le journal n'est pas joli. Il n'a pas besoin de l'être. Il a besoin d'être <b>fait</b>. "
    "Si tu écris mal, c'est OK. Si tu raies, c'est OK. Si tu sautes une ligne, c'est OK. Mais tu fais.", body_italic
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
    "Tu es arrivé à la dernière page d'un document qui ne devait pas exister. "
    "Le livre que tu voulais lire en français n'existe pas. Alors on a fait mieux : on a fait celui qui te parle à toi. "
    "Pas à un trader moyen. Pas à un débutant. À toi, Marien, 25 ans, retour de coma, prop firm, XAUUSD, ATHÉNA, "
    "ta filly, ton ambition, ton intensité, tes patterns destructeurs, et ta part qui veut autre chose.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Si tu n'as retenu qu'une seule idée de tout ce que tu as lu, retiens celle-ci : "
    "<b>tu n'as pas un problème de méthode, tu as un problème d'identité.</b> "
    "Et l'identité, ça se sculpte. Pas en un week-end. Pas en un mois. En milliers de petits gestes alignés "
    "avec qui tu décides de devenir.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Tu as 25 ans. Tu en aurais pu en avoir zéro. En 2022 quelque chose a presque tout fauché. "
    "Et tu es là. Tu tiens debout. Tu trades. Tu construis une boîte. Tu sautes des obstacles. "
    "Tu fais des affirmations. Tu te bats avec un système nerveux qui n'a pas envie de coopérer. "
    "Et tu continues. C'est déjà énorme. Ne le banalise pas pour aller chercher la preuve suivante. "
    "La preuve, c'est toi qui lis cette phrase. Tout le reste n'est qu'élaboration.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Le trading n'est pas ta valeur. C'est un métier. C'est une compétence. Quand tu la possèdes, elle te donne "
    "de la liberté. Quand elle te possède, elle te bouffe. Aujourd'hui elle te bouffe. Dans 90 jours, "
    "si tu fais le travail décrit dans ce document, l'équilibre commencera à basculer. Dans un an, "
    "si tu maintiens la cohérence, tu seras quelqu'un que ton « toi de 2024 » n'aurait pas reconnu en bien.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Continue à monter à cheval. Continue à boxer. Continue ATHÉNA — c'est un beau projet, "
    "il a une logique propre, tu peux y faire ce que tu n'as pas pu faire dans le trading : "
    "construire patiemment quelque chose qui se cumule au lieu de se cramer. Le 3D printing equestrian, "
    "personne d'autre que toi ne va le faire avec ta sensibilité. C'est rare. Protège-le.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Et ta filly. Tu la regardes, elle te regarde. Vous êtes deux jeunes êtres en construction. Elle apprend "
    "à faire confiance. Toi aussi, à ta façon. Ne néglige pas ce binôme pendant que tu construis le trader. "
    "Les chevaux ont une fonction régulatrice neuro-vagale documentée. Ce n'est pas du folklore. "
    "Le pansage, la respiration partagée, le calme imposé par le rythme animal — tout ça travaille pour toi, "
    "même quand tu ne tradés pas.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Une dernière chose, parce qu'il faut bien finir. Tu n'es pas en retard. Tu vas peut-être te dire que oui, "
    "que tu as déjà cramé X comptes, perdu Y temps, qu'à 25 ans tu devrais déjà avoir réussi. C'est faux. "
    "Tu n'es pas en retard. Tu es <b>à l'heure</b>. Le calendrier de ta vie n'est pas celui de Twitter trading. "
    "Tu as un coma derrière toi, un système nerveux qui se reconstruit, une intelligence rare, une ambition "
    "intacte, et désormais une méthode psychologique sérieuse à appliquer. C'est largement assez pour les "
    "vingt prochaines années.", body
))
story.append(Spacer(1, 6))

story.append(P(
    "Va, applique, échoue parfois, reprends, écris dans ton cahier, ferme la plateforme, rentre chez toi, "
    "monte à cheval, dors sept heures, et reviens demain avec la même intention. C'est tout. C'est tout "
    "ce qu'il y a à faire.", body
))
story.append(Spacer(1, 10))

story.append(P('« Les meilleurs traders ne gagnent pas mieux. Ils perdent mieux. »', pull_quote))
story.append(Spacer(1, 4))
story.append(P("Et toi, à partir d'aujourd'hui, tu fais partie de ceux qui apprennent à perdre mieux.", body_center))
story.append(Spacer(1, 30))

story.append(P("— Fin du document —", ParagraphStyle("end", fontName="DejaVu-Italic", fontSize=11, textColor=MID_GREY, alignment=TA_CENTER)))


# ---------- BUILD ----------
class CustomDocTemplate(SimpleDocTemplate):
    """Doc avec page templates spécifiques pour la cover."""
    def afterFlowable(self, flowable):
        pass


# Première page = cover, suivantes = standard
def on_first_page(canv, doc):
    cover_page(canv, doc)

def on_later_pages(canv, doc):
    standard_page(canv, doc)


doc.build(story, onFirstPage=on_first_page, onLaterPages=on_later_pages)

print(f"✓ PDF généré : {OUTPUT}")
