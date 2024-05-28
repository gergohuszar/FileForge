from pathlib import Path
import exiftool


def modify_metadata(file_path, tag, value):
    
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    # Modify the metadata
    with exiftool.ExifTool() as et:
        et.execute(f"-{tag}={value}", "-overwrite_original", str(file_path))

    with exiftool.ExifTool() as et:
        et.execute(f"-XMP:{tag}={value}", "-overwrite_original", str(file_path))



