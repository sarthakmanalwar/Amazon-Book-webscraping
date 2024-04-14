import scrapy
from ..items import AmazonSpiderItem

class AmazonScrapSpider(scrapy.Spider):
    name = "amazon_scrap"
    allowed_domains = ["amazon.com"]
    start_urls = ["https://www.amazon.in/s?k=books&s=date-desc-rank&crid=1NS15HGRI3PAQ&qid=1713018285&sprefix=book%2Caps%2C276&ref=sr_st_date-desc-rank&ds=v1%3A%2Fb5Vg3xu82bhzTCUVQJ%2FsqmjmQq6Xl%2FqvUxMmQsyuvE"]

    def parse(self, response):
        books = response.css('.a-section.a-spacing-small.a-spacing-top-small')
        items = AmazonSpiderItem()
        for book in books: 
            
            items['title'] = book.css('.a-size-medium.a-color-base.a-text-normal::text').extract()
            items['author'] = book.css('.a-size-base::text').extract()
            items['price'] = book.css('.a-price-whole::text').extract()
            #items['image'] = book.css('.s-image::attr(src)').extract()

            yield items
