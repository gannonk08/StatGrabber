from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem

class StackSpider(Spider):
    name = "espn"
    allowed_domains = ["espn.com"]
    start_urls = [
        "http://www.espn.com/nfl/game?gameId=400874605",
    ]

    def parse(self, response):
        gameTimes = Selector(response).xpath('//*[@id="gamepackage-matchup-wrap"]/header/div[2]/div[2]/span[2]/span')

        item = StackItem()
        item['time'] = gameTimes

        yield item
