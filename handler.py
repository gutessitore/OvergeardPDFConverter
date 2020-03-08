import sys

import scrapper


def convert(argv):
    arguments = argv[1:]

    linkIndex = arguments.index("-l") + 1
    link = arguments[linkIndex]

    if "-all" in arguments:
        print("This might take a few minutes...")
        chapterEnd = scrapper.getLastChapter(link)
        scrapper.pdfGenerator(link, 1, chapterEnd)

    else:
        try:
            linkIndex = arguments.index("-s") + 1
            chapterStart = int(arguments[linkIndex])

            linkIndex = arguments.index("-e") + 1
            chapterEnd = int(arguments[linkIndex])

            scrapper.pdfGenerator(link, chapterStart, chapterEnd)
        except:
            print("Error")

    return None


if __name__ == "__main__":
    convert(sys.argv)
