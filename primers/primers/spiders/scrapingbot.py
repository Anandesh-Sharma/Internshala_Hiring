import scrapy
from scrapy.selector import Selector
from twisted.internet import reactor
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule

class ScrapingbotSpider(scrapy.Spider):
    name = 'scrapingbot'
    allowed_domains = ['file:///C:/Users/Sanjana/AppData/Local/Temp/tmpnud14cye.html']
    start_urls = ['http://file:///C:/Users/Sanjana/AppData/Local/Temp/tmpnud14cye.html/']

    rules = (Rule(LinkExtractor(allow=r"/item/"), callback="parse_items", follow=True),)

def start_requests(self):
        url = "file:///C:/Users/Sanjana/AppData/Local/Temp/tmpnud14cye.html"
        yield scrapy.Request(url)
        
def parse_books(self, response):
        if response.xpath('div.product').get() is not None:
            title = response.xpath('a.catalog-item-name::text').extract_first()
            price = response.xpath('div.price-rating-container div.catalog-item-price span span::text').extract_first()
            stock = (
                response.xpath('div.catalog-item-price div div span span::text')
                .extract_first()
            )
            maftr = response.xpath('div.product-description div a::text').extract_first()

            yield{
            item["price"] = price    
            item["title"] = title
            item["stock"] = stock
            item["maftr"] = maftr
            }