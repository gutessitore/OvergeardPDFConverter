import sys
import scrapper


def convert(argv):
    arguments = argv[1:]
    if "--help" in arguments or "-h" in arguments:
        print("Usage: WuxiaWorldPDFConverter.py [-h] [-a] [-l <link>] [-s <number>] [-e <number>]")
        print("Arguments: \n -h, --help     Show this help message and exit")
        print(" --all, -a       Convert all chapters (may have teasers from last chapters)")
        print(" -l <link>       Link from any chapter of the novel")
        print(" -s <number>     Number of the first desired chapter")
        print(" -e <number>     Number of the last desired chapter")
        print("")
        print("Example $ python3 WuxiaWorldPDFConverter.py -l ")
        return None

    try:
        linkIndex = arguments.index("-l") + 1
        link = arguments[linkIndex]
    except:
        return print("Provide a valid link")

    if "--all" in arguments or "-a" in arguments:
        print("This might take a few minutes...")
        chapterEnd = scrapper.getLastChapter(link)
        scrapper.pdfGenerator(link, 1, chapterEnd)

    else:
        try:
            linkIndex = arguments.index("-s") + 1
            chapterStart = int(arguments[linkIndex])

            linkIndex = arguments.index("-e") + 1
            chapterEnd = int(arguments[linkIndex])
        except:
            print("Error: specify chapter start and end")

        scrapper.pdfGenerator(link, chapterStart, chapterEnd)


    return None


if __name__ == "__main__":
    convert(sys.argv)
