import re


def main():
    html = input("HTML: ")
    print(parse(html))


def parse(iframe):
    if matches := re.search(r'"https?://(?:www\.)?youtube.com/embed/([a-zA-Z0-9]+)"', iframe):
        final_part_of_url = matches.group(1)
        url = "https://youtu.be/" + str(final_part_of_url)
        return url
    else:
        return None

if __name__ == "__main__":
    main()
