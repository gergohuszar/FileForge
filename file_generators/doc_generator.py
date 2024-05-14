from docx import Document


class DocGenerator:
    @staticmethod
    def generate_document(content, filename="example"):
        doc = Document()
        doc.add_paragraph(content)
        doc.save(f"{filename}.docx")
