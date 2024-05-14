from file_generators.doc_generator import DocGenerator
from file_generators.xlsx_generator import XlsxGenerator
from file_generators.jpeg_generator import JpegGenerator


class FileGeneratorAPI:
    def __init__(self):
        pass

    def generate_all_files(self, content, filename):
        self.generate_doc(content, filename)
        self.generate_xlsx(content, filename)
        self.generate_jpeg(content, filename)

    def generate_doc(self, content, filename):
        DocGenerator.generate_document(content, filename)

    def generate_xlsx(self, content, filename):
        XlsxGenerator.generate_spreadsheet(content, filename)

    def generate_jpeg(self, content, filename):
        JpegGenerator.generate_image(content, filename)


if __name__ == "__main__":
    api = FileGeneratorAPI()
    api.generate_all_files("my ssn number is: 309-80-2677", "ssn")
