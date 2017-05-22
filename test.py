import os
import json
import scrapy
from scrapy.crawler import CrawlerProcess

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

import metalcat
from metalcat.spiders.metrolyrics_spider import MetrolyricsSpider

def metalcat():
    with open('output/lyrics.json') as json_data:
        verses = json.load(json_data)
        first_line = verses[0]['lines'][0]
        second_line = verses[0]['lines'][1]

    img = Image.open("static/cat.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('/Library/Fonts/Impact.ttf', 60)
    draw.text((25, 50), first_line, (200,40,40), font=font)
    draw.text((100, 100), second_line, (200,40,40), font=font)
    img.save('output/metalcat.jpg')

def crawl():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output/lyrics.json',
        'FEED_EXPORT_ENCODING':'utf-8'
    })

    process.crawl(MetrolyricsSpider)
    process.start()

if __name__ == "__main__":
    if not os.path.isfile('output/lyrics.json'):
        crawl()
    metalcat()

