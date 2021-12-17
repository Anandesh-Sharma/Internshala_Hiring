import scrapy

class TutorialSpider(scrapy.Spider):
    name = 'SCRAPY_PROJECT'

    def start_requests(self):
        urls = [
            'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    


    def parse(self, response):
        for title in response.css('div.product'):
            price = title.css('div.price-rating-container div.catalog-item-price span span::text').extract_first()
            heading=title.css('div.product-description a::text').extract_first()
            stock=title.css('div.price-rating-container div.catalog-item-price div div span span::text').extract_first()
            maftr=title.css('div.product-description div a::text').extract_first()
                
            yield {
                'price':price,
                'title':heading,
                'stock':bool(stock=='In Stock'),
                'maftr':maftr
            }