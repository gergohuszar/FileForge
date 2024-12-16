import random

from .random_paragraph_generator import ParagraphGenerator


class DriverLicenseGenerator:
    context_words = [
        "Driver License Number",
        "DLN",
        "License Number",
        "Driving License Number",
        "Driver's License No.",
        "License ID",
        "DL#",
        "Driver's ID",
        "Permit Number",
        "License ID Number",
        "State ID Number",
        "Issued Date",
        "Class (A/B/C/D)",
        "Restrictions",
        "Vehicle Type",
        "Issuing Authority",
        "State of Issuance",
        "Expiration Year",
    ]

    license_numbers = [
        "6940579",
        "S530-460-99-424-0",
        "2270-66-1551",
        "4031276",
        "481195160",
        "006984185",
        "852858485",
        "425700624",
        "409540487",
        "220804772",
        "222861714",
        "A230-279-135-866",
        "A312-032-153-620",
        "FRANCRF705BA",
        "P362-738-729-232",
        "9741673",
        "9100575",
        "U94783965",
        "341308170",
        "J1003878",
        "449451270",
        "281211981",
        "1662897",
        "6348590",
        "M943688896309",
        "915182692",
        "133197326",
        "LH329609T",
        "B20093214252",
        "5761491745",
        "366211894",
        "578988637",
        "385441539",
        "A125325867",
        "9385623",
        "F162823540116",
        "984540232",
        "D377768453473",
        "Y829244176735",
        "535284465",
        "964844313",
        "515606188",
        "A56319335",
        "284831437936",
        "92RPI23272",
        "U62928788557186",
        "220053935",
        "950735093",
        "982959903687",
        "749899989",
        "QM2899809",
        "755600751",
        "3560604",
        "89621179",
        "2900880",
        "989832883",
        "925014173",
        "103089471",
        "50473044",
        "951448502",
        "758840603",
        "755947796",
        "JJHCJX451MC",
        "5130634",
        "X1977104127784",
        "527525559",
    ]

    templates = [
        "John Smith's driver license number is {{us_driver_license}}, issued by the State of California on June 15, 2020. The license is valid until June 15, 2026, and covers Class C vehicles. He is required to carry corrective lenses while driving, as indicated in the restrictions section of his license.",
        "Please provide a valid form of identification such as a driver’s license.E.g: {{us_driver_license}} . Your driver license number should be clearly visible on the front of the card, along with your full name and expiration date. Ensure the document is up-to-date and has not expired.",
        "During the verification process, Sarah's driver license number ({{us_driver_license}}) was entered into the system for identification purposes. The system confirmed that the license was issued in Texas and is set to expire in December 2025. The document serves as her primary form of ID for all official matters.",
    ]

    def driver_license_gen_random(self, num_of_sentences: int) -> str:
        generator = ParagraphGenerator()

        return generator.generate_with_random_choice_of_piis(
            self.license_numbers, self.context_words, num_of_sentences
        )

    def driver_license_gen_from_templates(self) -> str:
        # palce a random driver licenser from license_numbers list into the template

        random_license = random.choice(self.license_numbers)
        random_template = random.choice(self.templates)
        text = random_template.replace("{{us_driver_license}}", random_license)

        return text
