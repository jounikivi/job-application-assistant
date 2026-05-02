from __future__ import annotations

import html
from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import ListFlowable, ListItem, PageBreak, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "toteutussuunnitelma.md"
TARGET = ROOT / "docs" / "toteutussuunnitelma.pdf"
TITLE = "Job Application Assistant - Toteutussuunnitelma"


def escape(text: str) -> str:
    return html.escape(text, quote=False)


def build_styles():
    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="CoverTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=24,
            leading=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#0F172A"),
            spaceAfter=8,
        )
    )
    styles.add(
        ParagraphStyle(
            name="CoverSubtitle",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=11,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#334155"),
            spaceAfter=6,
        )
    )
    styles["Heading1"].fontName = "Helvetica-Bold"
    styles["Heading1"].fontSize = 18
    styles["Heading1"].leading = 22
    styles["Heading1"].textColor = colors.HexColor("#0F172A")
    styles["Heading1"].spaceBefore = 12
    styles["Heading1"].spaceAfter = 6

    styles["Heading2"].fontName = "Helvetica-Bold"
    styles["Heading2"].fontSize = 13
    styles["Heading2"].leading = 17
    styles["Heading2"].textColor = colors.HexColor("#1D4ED8")
    styles["Heading2"].spaceBefore = 10
    styles["Heading2"].spaceAfter = 4

    styles["BodyText"].fontName = "Helvetica"
    styles["BodyText"].fontSize = 10.5
    styles["BodyText"].leading = 15
    styles["BodyText"].spaceAfter = 4

    styles.add(
        ParagraphStyle(
            name="BulletText",
            parent=styles["BodyText"],
            leftIndent=8,
            spaceBefore=1,
            spaceAfter=1,
        )
    )
    return styles


def parse_markdown(text: str, styles):
    story = []
    bullet_buffer: list[str] = []
    number_buffer: list[str] = []
    paragraph_buffer: list[str] = []

    def flush_paragraph():
        nonlocal paragraph_buffer
        if paragraph_buffer:
            paragraph = " ".join(part.strip() for part in paragraph_buffer if part.strip())
            if paragraph:
                story.append(Paragraph(escape(paragraph), styles["BodyText"]))
            paragraph_buffer = []

    def flush_bullets():
        nonlocal bullet_buffer
        if bullet_buffer:
            items = [ListItem(Paragraph(escape(item), styles["BulletText"])) for item in bullet_buffer]
            story.append(ListFlowable(items, bulletType="bullet", bulletFontName="Helvetica", bulletFontSize=9))
            story.append(Spacer(1, 4))
            bullet_buffer = []

    def flush_numbers():
        nonlocal number_buffer
        if number_buffer:
            items = [ListItem(Paragraph(escape(item), styles["BulletText"])) for item in number_buffer]
            story.append(ListFlowable(items, bulletType="1", start="1"))
            story.append(Spacer(1, 4))
            number_buffer = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            flush_bullets()
            flush_numbers()
            story.append(Spacer(1, 4))
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            flush_bullets()
            flush_numbers()
            story.append(Paragraph(escape(stripped[2:].strip()), styles["Heading1"]))
            continue

        if stripped.startswith("## "):
            flush_paragraph()
            flush_bullets()
            flush_numbers()
            story.append(Paragraph(escape(stripped[3:].strip()), styles["Heading2"]))
            continue

        if stripped.startswith("- "):
            flush_paragraph()
            flush_numbers()
            bullet_buffer.append(stripped[2:].strip())
            continue

        if re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            flush_bullets()
            number_buffer.append(re.sub(r"^\d+\.\s+", "", stripped))
            continue

        paragraph_buffer.append(stripped)

    flush_paragraph()
    flush_bullets()
    flush_numbers()
    return story


def add_page_number(canvas, doc):
    page = canvas.getPageNumber()
    canvas.setFont("Helvetica", 9)
    canvas.setFillColor(colors.HexColor("#64748B"))
    canvas.drawRightString(195 * mm, 12 * mm, f"Sivu {page}")


def build_pdf():
    styles = build_styles()
    source_text = SOURCE.read_text(encoding="utf-8")

    doc = SimpleDocTemplate(
        str(TARGET),
        pagesize=A4,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        title=TITLE,
        author="OpenAI Codex",
    )

    story = [
        Spacer(1, 45 * mm),
        Paragraph(TITLE, styles["CoverTitle"]),
        Paragraph("Kattava toteutussuunnitelma paikallisesti ajettavalle Python-tyokalulle.", styles["CoverSubtitle"]),
        Paragraph("Sisalto pohjautuu projektille maariteltyyn MVP-ajatteluun, laajennettavaan arkkitehtuuriin, testaukseen ja tietosuojaperiaatteisiin.", styles["CoverSubtitle"]),
        Spacer(1, 10 * mm),
        Paragraph("Versio 0.1", styles["CoverSubtitle"]),
        PageBreak(),
    ]
    story.extend(parse_markdown(source_text, styles))
    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf()
