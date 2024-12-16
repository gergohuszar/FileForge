from FileForge import FileForge
from content_generators.driver_license_gen import DriverLicenseGenerator


def main():
    file_forge = FileForge()

    gen = DriverLicenseGenerator()

    for i in range(0, 20):
        content = gen.driver_license_gen_random(30)
        file_name = f"driving_license_{i}"
        file_forge.generate_text(content, file_name)
        file_forge.generate_pdf(content, file_name)

    for i in range(0, 5):
        content = gen.driver_license_gen_from_templates()
        file_name = f"driving_license_{i}_template"
        file_forge.generate_text(content, file_name)
        file_forge.generate_pdf(content, file_name)


if __name__ == "__main__":
    main()
