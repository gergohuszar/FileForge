from docx import Document


class DocGenerator:
    @staticmethod
    def generate(content, filename="example"):
        doc = Document()
        doc.add_paragraph(content)
        doc.save(f"{filename}.docx")
