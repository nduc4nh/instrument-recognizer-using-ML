# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class InstrumentSpiderItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CrawlerItem(Item):
    # define the fields for your item here like:
    name = Field()
    type_name = Field()
    file_urls = Field()
    pass