import csv


class CsvGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        # Open the file in write mode
        with open(f"{filename}.csv", mode="w", newline="") as file:
            writer = csv.writer(file)

            csv_content = [
                ["Name", "Age", "City"],
                ["Alice", 30, "New York"],
                ["Bob", 25, "San Francisco"],
                ["Charlie", 35, content],
            ]

            # Write each row to the CSV file
            for row in csv_content:
                writer.writerow(row)
