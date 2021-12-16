import scrapy
class ShootersSpider(scrapy.Spider):
    name = "NeuronSquare_Assigment"

    def start_requests(self):
        urls = [
            'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for item in response.css("div#Div1.product"):
            yield{
                'price':float(item.css('span.price').css('span::text').get()),
                'title':item.css('a.catalog-item-name::text').get(),
                'status':item.css('span.out-of-stock::text').get(),
                'manufacturer':item.css('a.catalog-item-brand::text').get()
                }
