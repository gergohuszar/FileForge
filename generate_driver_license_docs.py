from FileForge import FileForge
from content_generators.driver_license_gen import driver_license_gen

file_forge = FileForge()

for i in range(0, 20):
    content = driver_license_gen(30)
    file_name = f"driving_license_{i}"
    file_forge.generate_text(content, file_name)
    file_forge.generate_pdf(content, file_name)
