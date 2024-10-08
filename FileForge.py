from pathlib import Path

from file_generators.doc_generator import DocGenerator
from file_generators.html_generator import HtmlGenerator
from file_generators.xlsx_generator import XlsxGenerator
from file_generators.pdf_generator import PdfGenerator
from file_generators.csv_generator import CsvGenerator
from file_generators.txt_generator import TxtGenerator
from file_generators.image_generator import ImageGenerator
from file_generators.eml_generator import EmlGenerator
from file_generators.pptx_generator import PptxGenerator
from file_generators.xml_generator import XmlGenerator


class FileForge:
    generators = (
        DocGenerator,
        XlsxGenerator,
        PdfGenerator,
        CsvGenerator,
        TxtGenerator,
        ImageGenerator,
        EmlGenerator,
        PptxGenerator,
        XmlGenerator,
        HtmlGenerator,
    )

    def __init__(self) -> None:
        cwd = Path.cwd()

        self.output_dir = cwd.joinpath("output")
        self.output_dir.mkdir(exist_ok=True)

    def generate_all_files(self, content, filename, **kwargs):
        filename = self.output_dir.joinpath(filename)

        for generator in self.generators:
            generator.generate(content, filename, **kwargs)

    def generate_pdf(self, content, filename, **kwargs):
        filename = self.output_dir.joinpath(filename)

        PdfGenerator.generate(content, filename, **kwargs)

    def generate_text(self, content, filename, **kwargs):
        filename = self.output_dir.joinpath(filename)

        TxtGenerator.generate(content, filename, **kwargs)


if __name__ == "__main__":
    file_forge = FileForge()
    file_forge.generate_all_files(
        """my ssn number is: ssn
814-08-4006
195-66-8635
394-39-9750
""",
        "ssn",
        attachment=True,
        metadatas={
            "Title": "alkapone",
        },
    )
