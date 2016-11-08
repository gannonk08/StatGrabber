# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from stat_grabber.items import *
import logging



class EspnCrawlerSpider(CrawlSpider):
    name = 'espn_crawler'
    allowed_domains = ['espn.com']
    start_urls = ['http://www.espn.com/nfl/game?gameId=400874607']

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=False),
    )

    def parse(self, response):
        scores = response.xpath('//*[@id="linescore"]/tbody/tr/td/text()')

        i = 0
        homeIndex = 1
        awayIndex = 1
        awayItem = awayTeamItem()
        homeItem = homeTeamItem()

        for score in scores:
            if i <= 5:
                if i == 0:
                    awayItem['awayTeam'] = score.extract()
                elif i == 5:
                    awayItem['final'] = score.extract()
                else:
                    awayItem['Q' + str(awayIndex)] = score.extract()
                    awayIndex = awayIndex + 1
            if i > 5:
                if i == 6:
                    homeItem['homeTeam'] = score.extract()
                elif i == 11:
                    homeItem['final'] = score.extract()
                else:
                    homeItem['Q' + str(homeIndex)] = score.extract()
                    homeIndex = homeIndex + 1
            i += 1

        yield awayItem
        yield homeItem
