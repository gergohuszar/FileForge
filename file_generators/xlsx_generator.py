import openpyxl

class XlsxGenerator:
    @staticmethod
    def generate_spreadsheet(content, filename="example"):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet['A1'] = content
        workbook.save(f"{filename}.xlsx")