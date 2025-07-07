from fpdf import FPDF
from PIL import Image

class Shirt():
    def __init__(self, name):
        if not name:
            raise ValueError("Name is missing")

        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.set_font("Times","B", 40)
        pdf.set_y(30)
        pdf.cell(0, 10, txt="CS50 Certificate", ln=True, align='C')

        image_width, image_height = self.size()
        dpi_x, dpi_y = self.dpi()

        image_width_mm = image_width * 25.4 / dpi_x
        image_height_mm = image_height * 25.4 / dpi_y

        image_x = 10
        image_y = 297 - 70 - image_height_mm
        image_w = 190
        aspect_ratio = image_height_mm / image_width_mm
        image_h = image_w * aspect_ratio

        pdf.image("shirtificate.png", x=image_x, y=image_y, w=image_w, h=image_h)
        text = f"{name} took CS50"

        pdf.set_text_color(255, 255, 255)
        text_y = image_y + (image_h / 4)
        pdf.set_xy(image_x, text_y)
        pdf.cell(image_w, pdf.font_size, txt=text, ln=True, align='C')

        pdf.output("shirtificate.pdf")


    def size(self):
        with Image.open("shirtificate.png") as img:
            return img.size

    def dpi(self):
        with Image.open("shirtificate.png") as img:
            return img.info.get('dpi', (72, 72))


def main():
    name = input("Name: ")
    Shirt(name)


if __name__ == "__main__":
    main()
