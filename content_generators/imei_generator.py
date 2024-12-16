import random


class IMEIGenerator:
    templates = [
        """Sample Document: Mobile Purchase Receipt with IMEI Number
ABC Electronics Store

Purchase Receipt

Date of Purchase: 2023-12-15
Customer Name: John Doe
Customer Contact: johndoe@email.com

Product Details:

Device Make and Model: XYZ Smartphone X12
Serial Number: 12345ABC6789
IMEI Number: {{imei}}
Price: $899.00
Payment Method: Credit Card

Store Contact: ABC Electronics, 123 Main St, Cityville
Phone: (123) 456-7890
Email: support@abcelectronics.com

This document serves as proof of purchase and should be kept for warranty and service needs.""",
    ]

    @staticmethod
    def generate_imei(use_separator: bool = False):
        pos = 0
        imei = []
        sum_ = 0
        len_offset = 0
        length = 15

        # Fill in the first two values of the string based on a specified prefix.
        # Example RBI values (replace with actual logic or list as necessary)
        RBI = ["35", "01", "10", "91", "86"]  # Add more as needed
        arr = random.choice(RBI)
        imei.append(int(arr[0]))
        imei.append(int(arr[1]))
        pos = 2

        # Fill all the remaining numbers except for the last one with random values.
        while pos < (length - 1):
            imei.append(random.randint(0, 9))
            pos += 1

        # Calculate the Luhn checksum of the values thus far
        len_offset = (length + 1) % 2
        for pos in range(length - 1):
            if (pos + len_offset) % 2 != 0:
                t = imei[pos] * 2
                if t > 9:
                    t -= 9
                sum_ += t
            else:
                sum_ += imei[pos]

        # Choose the last digit so that it causes the entire string to pass the checksum.
        imei.append((10 - (sum_ % 10)) % 10)

        if use_separator:
            # add separator to index 2, 9, 16 : AA-BBBBBB-CCCCCC-D
            imei.insert(2, "-")
            imei.insert(9, "-")
            imei.insert(16, "-")

        # Output the IMEI value.
        return "".join(map(str, imei))

    def imei_gen_from_templates(self) -> str:
        sep: bool = bool(random.getrandbits(1))
        random_imei = self.generate_imei(sep)
        random_template = random.choice(self.templates)
        text = random_template.replace("{{imei}}", random_imei)

        return text
