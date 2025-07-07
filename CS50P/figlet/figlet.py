import pyfiglet
from pyfiglet import Figlet
import sys
import random


def main():
    if len(sys.argv) == 1:
        text = input("Input: ")
        font2 = random_font()
        fig = pyfiglet.Figlet(font=font2)
        print(fig.renderText(text))
    elif len(sys.argv) == 3:
        if sys.argv[1].strip() in ["-f", "--font"]:
            font_name = sys.argv[2]
            if is_font(font_name):
                text = input("Input: ")
                fig = pyfiglet.Figlet(font=font_name)
                print(fig.renderText(text))
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def is_font(font_name):
    figlet = Figlet()
    avaliable_fonts = figlet.getFonts()
    return font_name in avaliable_fonts

def random_font():
    available_fonts = pyfiglet.FigletFont.getFonts()
    return random.choice(available_fonts)


if __name__ == "__main__":
    main()
