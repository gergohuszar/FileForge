from PIL import Image, ImageFont, ImageDraw, ImageColor


class JpegGenerator:
    @staticmethod
    def generate_image(content, filename="example", color="white"):
        font_align = "center"

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

        img.save(f"{filename}.jpeg")
