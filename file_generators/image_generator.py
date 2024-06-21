from PIL import Image, ImageDraw, ImageFont
from . import metadata_utils
from pathlib import Path


class ImageGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        lines = []
        words = content.split()
        line = ""
        line_height_ratio = 1.2
        padding = 20
        max_width = 600
        font_size = 30

        font = ImageFont.truetype("arial.ttf", font_size)

        temp_image = Image.new("RGB", (1, 1))
        draw = ImageDraw.Draw(temp_image)

        for word in words:
            test_line = f"{line} {word}".strip()
            bbox = draw.textbbox((0, 0), test_line, font=font)
            width = bbox[2] - bbox[0]

            if width > max_width:
                lines.append(line)
                line = word
            else:
                line = test_line

        if line:
            lines.append(line)

        line_height = int(font_size * line_height_ratio)
        image_height = len(lines) * line_height + padding * 2

        image = Image.new("RGB", (max_width + padding * 2, image_height), color="white")
        draw = ImageDraw.Draw(image)

        y = padding
        for line in lines:
            draw.text((padding, y), line, font=font, fill="black")
            y += line_height

        supported_extensions = (
            "png",
            "bmp",
            "gif",
            "jpeg",
            "jpg",
            "tif",
            "tiff",
            "jp2",
            "jpf",
            "j2c",
        )
        for extension in supported_extensions:
            image.save(f"{filename}.{extension}", quality=95)

        if "metadatas" in kwargs:
            for extension in supported_extensions:
                for key, value in kwargs["metadatas"].items():
                    metadata_utils.modify_metadata(
                        Path(f"{filename}.{extension}"), key, value
                    )
