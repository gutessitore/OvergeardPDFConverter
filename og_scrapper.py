
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
from requests import get
from textwrap import wrap
import itertools


pdfmetrics.registerFont(TTFont("DejaVuSansCondensed", "DejaVuSansCondensed.ttf"))
url = "https://www.wuxiaworld.com/novel/overgeared/og-chapter-"
chapters = [str(i) for i in range(1101, 1184, 1)]
urls = [url + chapter for chapter in chapters]


c = canvas.Canvas("Overgeared_Chapter_" + chapters[0] + "-" + chapters[-1] + ".pdf", pagesize = letter)

for master in range(len(urls)):
    
    html = get(urls[master]).content
    content = BeautifulSoup(html, 'html.parser')
    texts = content.find_all('p', dir = 'ltr')
    chapter_text = []
    new_text = []

    for counter in range(len(texts)):
        for span in texts[counter].find_all("span"):
            chapter_text.append(span.text.strip())

    for text in chapter_text:
        n_text = "\n ".join(wrap(text, 70))
        new_text.append(n_text.split("\n"))

    new_text = list(itertools.chain.from_iterable(new_text))

    pages = [new_text[35*i:35*(i+1)] for i in range(int(len(new_text)/35 + 1))]

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

