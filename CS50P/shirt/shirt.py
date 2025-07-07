import sys
from PIL import Image, ImageOps
import os

def main():
    input_file, output_file = get_input_and_open()

    shirtfile = Image.open("shirt.png")
    imagefile = Image.open(input_file)

    shirt_size = shirtfile.size
    muppet = ImageOps.fit(imagefile, shirt_size)

    muppet.paste(shirtfile, shirtfile)
    muppet.save(output_file)

def get_input_and_open():
    if len(sys.argv) == 3:
        try:
            formats = [".jpeg", ".jpg", ".png"]
            input_name, input_extension = os.path.splitext(sys.argv[1])
            output, output_extension = os.path.splitext(sys.argv[2])
            if input_extension in formats:
                    if output_extension in formats:
                         if output_extension == input_extension:
                              return sys.argv[1], sys.argv[2]
                         else:
                              sys.exit("Input and output have different extensions")
                    else:
                         sys.exit("Invalid output")
            else:
                sys.exit("Invalid input")
        except FileNotFoundError:
            sys.exit("Input does not exist")

    elif len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()

