# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    
    title = scrapy.Field()
    author = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    
    
