import html
from FileForge import FileForge
from content_generators.european_national_id_generator import EuropeanNationalIdGenerator


def main():
    file_forge = FileForge()
    id_generator = EuropeanNationalIdGenerator()

    for i, content in enumerate(id_generator.generate_all_predefined(num_of_paragraph_sentences=30)):
        file_name = f"national_id_{i}"
        file_forge.generate_text(content, file_name)
        file_forge.generate_pdf(html.escape(content), file_name)

    for j, content in enumerate(id_generator.generate_random_ids(num_of_random_piis=10, num_of_paragraph_sentences=30)):
        file_name = f"national_id_{i+j}"
        file_forge.generate_text(content, file_name)
        file_forge.generate_pdf(html.escape(content), file_name)


if __name__ == '__main__':
    main()