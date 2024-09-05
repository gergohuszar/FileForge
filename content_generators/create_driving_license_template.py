from faker import Faker

from faker.providers import DynamicProvider

driving_license_provider = DynamicProvider(
    provider_name="driving_license",
    elements=[
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
        "{{us_driver_license}}",
    ],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(driving_license_provider)

# now you can use:
# print(fake.driving_license())


print(fake.paragraph(nb_sentences=20))
# 'Expedita at beatae voluptatibus nulla omnis.'
