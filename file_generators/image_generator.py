from PIL import Image, ImageFont, ImageDraw


class ImageGenerator:
    @staticmethod
    def generate(content, filename="example"):
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

        img.save(f"{filename}.png")
        img.save(f"{filename}.bmp")
        img.save(f"{filename}.gif")
        img.save(f"{filename}.jpeg")
        img.save(f"{filename}.jpg")
        img.save(f"{filename}.tif")
        img.save(f"{filename}.tiff")
        img.save(f"{filename}.jp2")
        img.save(f"{filename}.jpf")
        img.save(f"{filename}.j2c")
