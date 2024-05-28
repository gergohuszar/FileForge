from PIL import Image, ImageFont, ImageDraw
from . import metadata_utils
from pathlib import Path


class ImageGenerator:
    @staticmethod
    def generate(content, filename="example", **kwargs):
        color = "white"
        font = ImageFont.truetype(
            r"FiraCode-Retina.ttf",
            162,
        )
        img = Image.new("RGB", font.getmask(content).size)

        draw = ImageDraw.Draw(img)
        draw_point = (0, 0)

        draw.multiline_text(draw_point, content, font=font, fill=color)

        text_window = img.getbbox()
        img = img.crop(text_window)

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
            img.save(f"{filename}.{extension}")

        if "metadatas" in kwargs:
            for key, value in kwargs["metadatas"].items():
                metadata_utils.modify_metadata(
                    Path(f"{filename}.{extension}"), key, value
                )
