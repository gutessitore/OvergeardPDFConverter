import itertools
from textwrap import wrap

import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from requests import get
from tqdm import tqdm

import urlExtractor


def getLastChapter(randomChapterUrl):
    novel, noChapterUrl = urlExtractor.getUrl(randomChapterUrl)
    urls = urlExtractor.urlChapterGenerator(noChapterUrl, 1, 7000, 100)

    for url in urls:
        if get(url).status_code != requests.codes.ok:
            lastError100 = urls.index(url) * 100 - 99
            break
    newUrls = urlExtractor.urlChapterGenerator(noChapterUrl, lastError100, lastError100 + 100, 1)

    for url in newUrls:
        if get(url).status_code != requests.codes.ok:
            lastError = newUrls.index(url) + lastError100 - 1
            break

    return lastError


def pdfGenerator(randomChapterUrl, chapterStart, chapterEnd):
    pdfmetrics.registerFont(TTFont("DejaVuSansCondensed", "DejaVuSansCondensed.ttf"))

    novel, noChapterUrl = urlExtractor.getUrl(randomChapterUrl)
    urls = urlExtractor.urlChapterGenerator(noChapterUrl, chapterStart, chapterEnd)
    chapters = [str(i) for i in range(chapterStart, chapterEnd + 1, 1)]

    fileName = novel.replace("-", " ") + " Chapters " + str(chapterStart) + "-" + str(chapterEnd) + ".pdf"
    c = canvas.Canvas(fileName, pagesize=letter)

    print("Starting to convert...")

    for master in tqdm(range(len(urls))):

        html = get(urls[master]).content
        content = BeautifulSoup(html, 'html.parser')
        div = content.find('div', id='chapter-content')
        texts = div.find_all('p')
        chapter_text = []
        new_text = []

        for counter in range(len(texts)):
            if len(texts[counter].find_all("span")) > 0:
                for span in texts[counter].find_all("span"):
                    chapter_text.append(span.text.strip())
            else:
                chapter_text.append(texts[counter].text.strip())

        for text in chapter_text:
            n_text = "\n ".join(wrap(text, 70))
            new_text.append(n_text.split("\n"))

        new_text = list(itertools.chain.from_iterable(new_text))

        pages = [new_text[35 * i:35 * (i + 1)] for i in range(int(len(new_text) / 35 + 1))]

        c.setFont('DejaVuSansCondensed', 70)
        c.drawString(100, 600, "Chapter " + str(chapters[master]))
        c.showPage()
        for page in pages:
            for counter in range(len(page)):
                c.setFont('DejaVuSansCondensed', 16)
                c.drawString(40, (750 - counter * 20), page[counter])
            c.showPage()
    c.save()
    c.getAvailableFonts()
    return print("Done writing", fileName)
