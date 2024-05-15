from pathlib import Path

from file_generators.doc_generator import DocGenerator
from file_generators.xlsx_generator import XlsxGenerator
from file_generators.pdf_generator import PdfGenerator
from file_generators.csv_generator import CsvGenerator
from file_generators.txt_generator import TxtGenerator
from file_generators.image_generator import ImageGenerator


class FileGeneratorAPI:
    generators = [
        DocGenerator,
        XlsxGenerator,
        PdfGenerator,
        CsvGenerator,
        TxtGenerator,
        ImageGenerator,
    ]

    def generate_all_files(self, content, filename):
        # get current working directory
        cwd = Path.cwd()
        # create a new directory called output
        output_dir = cwd.joinpath("output")
        output_dir.mkdir(exist_ok=True)

        filename = output_dir.joinpath(filename)

        for generator in self.generators:
            generator.generate(content, filename)


if __name__ == "__main__":
    api = FileGeneratorAPI()
    api.generate_all_files("my ssn number is: 309-80-2677", "ssn")
