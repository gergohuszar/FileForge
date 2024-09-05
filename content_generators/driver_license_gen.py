import pandas as pd
from pathlib import Path

from faker import Faker

from presidio_evaluator import InputSample
from presidio_evaluator.data_generator import PresidioDataGenerator
from presidio_evaluator.data_generator.faker_extensions import (
    FakerSpansResult,
    RecordsFaker,
    UsDriverLicenseProvider,
)


fake_name_generator_file = Path("FakeNameGenerator.com_3000.csv")

fake_name_generator_df = pd.read_csv(fake_name_generator_file)


fake_name_generator_df = PresidioDataGenerator.update_fake_name_generator_df(
    fake_name_generator_df
)
# print(fake_name_generator_df.head())

fake = RecordsFaker(records=fake_name_generator_df, locale="en_US")
fake.add_provider(UsDriverLicenseProvider)
lower_case_ratio = 0.05
number_of_samples = 1500
data_generator = PresidioDataGenerator(
    custom_faker=fake, lower_case_ratio=lower_case_ratio
)


sentence_templates = PresidioDataGenerator.read_template_file(
    Path("driver_license_template.txt")
)
fake_records = data_generator.generate_fake_data(
    templates=sentence_templates, n_samples=number_of_samples
)

fake_records = list(fake_records)

print(len(fake_records))

breakpoint()
