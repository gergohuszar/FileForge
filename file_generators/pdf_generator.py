from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


class PdfGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        pdf = SimpleDocTemplate(f"{filename}.pdf", pagesize=A4)

        styles = getSampleStyleSheet()
        style = styles["Normal"]

        # NOTE: If content has html characters then the program will crash. Should we use html.escape(content) here?
        paragraph = Paragraph(content, style)

        story = [paragraph]

        pdf.build(story)
