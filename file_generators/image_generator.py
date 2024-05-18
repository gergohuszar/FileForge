from PIL import Image, ImageFont, ImageDraw


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
