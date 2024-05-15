class TxtGenerator:
    @staticmethod
    def generate(content, filename="example"):
        with open(f"{filename}.txt", mode="w", newline="") as file:
            file.write(content)
