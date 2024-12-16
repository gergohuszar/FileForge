import random
from faker import Faker


class ABA_RoutingNumberGenerator:
    context_words = [
        "ABA Routing Number",
        "Routing Number",
        "Bank Routing Number",
        "Routing #",
        "ABA #",
        "Bank ABA Routing Number",
        "Bank Routing #",
        "Bank ABA #",
        "Routing ID",
        "Bank ID",
        "Bank Number",
        "Bank Code",
        "Bank Identifier",
    ]

    templates = [
        "this is my banks routing number {{aba_routing_number}}",
    ]

    def ABA_gen_from_templates(self) -> str:
        # palce a random driver licenser from license_numbers list into the template
        fake = Faker()

        routing_number = fake.aba()
        random_template = random.choice(self.templates)
        text = random_template.replace("{{aba_routing_number}}", routing_number)

        return text


if __name__ == "__main__":
    generator = ABA_RoutingNumberGenerator()
    print(generator.ABA_gen_from_templates())
    print(generator.ABA_gen_from_templates())
    print(generator.ABA_gen_from_templates())