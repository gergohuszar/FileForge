import random
from faker import Faker


class CCNGenerator:
    context_words = [
        "Card number",
        "Credit card",
        "Visa",
        "Mastercard",
        "Cardholder",
        "Expiration date",
        "CVV",
        "Payment details",
        "Security code",
        "Billing address",
    ]

    templates = [
        "{{context}} {{ccn}}",
    ]

    ccn_types = [
        "visa16",
        "visa13",
        "visa19",
        "mastercard",
        "amex",
        "discover",
        "jcb15",
    ]

    def ccn_gen_from_templates(self) -> str:
        # palce a random driver licenser from license_numbers list into the template
        fake = Faker()

        random_type = random.choice(self.ccn_types)

        ccn = fake.credit_card_number(card_type=random_type)
        random_template = random.choice(self.templates)
        random_context = random.choice(self.context_words)
        text = random_template.replace("{{ccn}}", ccn)
        text = text.replace("{{context}}", random_context)

        return text


if __name__ == "__main__":
    """
    for _ in range(40):
        generator = CCNGenerator()

        print( generator.ccn_gen_from_templates())
    
    """
    fake = Faker()

    for _ in range(40):
        print(fake.credit_card_number(card_type="discover"))
