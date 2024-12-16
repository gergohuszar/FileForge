from FileForge import FileForge
from content_generators.imei_generator import IMEIGenerator


def main():
    file_forge = FileForge()

    gen = IMEIGenerator()

    for i in range(0, 2):
        content = gen.imei_gen_from_templates()
        file_name = f"imei_docs{i}"
        file_forge.generate_all_files(content, file_name)


if __name__ == "__main__":
    main()
