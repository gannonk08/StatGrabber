import scrapy

from scrapy.item import Item, Field


class awayTeamItem(Item):
    awayTeam = Field()
    Q1 = Field()
    Q2 = Field()
    Q3 = Field()
    Q4 = Field()
    final = Field()


class homeTeamItem(Item):
    homeTeam = Field()
    Q1 = Field()
    Q2 = Field()
    Q3 = Field()
    Q4 = Field()
    final = Field()
