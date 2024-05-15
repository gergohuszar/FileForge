from file_generators.doc_generator import DocGenerator
from file_generators.xlsx_generator import XlsxGenerator
from file_generators.jpeg_generator import JpegGenerator
from file_generators.pdf_generator import PdfGenerator
from file_generators.csv_generator import CsvGenerator


class FileGeneratorAPI:
    generators = [
        DocGenerator,
        XlsxGenerator,
        JpegGenerator,
        PdfGenerator,
        CsvGenerator,
    ]

    def generate_all_files(self, content, filename):
        for generator in self.generators:
            generator.generate(content, filename)


if __name__ == "__main__":
    api = FileGeneratorAPI()
    api.generate_all_files("my ssn number is: 309-80-2677", "ssn")
