from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


class PdfGenerator:
    @staticmethod
    def generate(content, filename="example"):
        canvas = Canvas(f"{filename}.pdf", pagesize=LETTER)
        canvas.setFont("Times-Roman", 12)
        canvas.setFillColor(blue)
        canvas.drawString(1 * inch, 10 * inch, content)
        canvas.save()
