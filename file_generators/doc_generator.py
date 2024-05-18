from docx import Document


class DocGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        doc = Document()
        doc.add_paragraph(content)
        doc.save(f"{filename}.docx")
