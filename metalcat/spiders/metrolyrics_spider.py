import logging

from scrapy import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.spiders import Spider

from metalcat.items import MetrolyricsItem

class MetrolyricsSpider(Spider):
    name = "metrolyrics_spider"
    allowed_domains = ["metrolyrics.com"]

    logging.getLogger('scrapy').setLevel(logging.WARNING)
    logging.getLogger('scrapy').propagate = False

    def start_requests(self):
        song = getattr(self, 'song', 'dopesmoker')
        artist = getattr(self, 'artist', 'sleep')
        url = 'http://www.metrolyrics.com/'+song+'-lyrics-'+artist+'.html'
        yield Request(url, self.parse)

    def parse(self, response):
        verses = response.xpath('//div[@id="lyrics-body-text"]/p[@class="verse"]')
        items = []
        for verse in verses:
            item = MetrolyricsItem()
            item['lines'] = verse.xpath('text()').extract()
            items.append(item)
        return items
