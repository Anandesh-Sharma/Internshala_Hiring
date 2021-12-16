'''
Task 1 by Gariman Singh
To scrape and store the result in JSON execute: scrapy crawl task1 -O task1.json
To set rotating proxies check out my changes in settings.py.
'''
import scrapy

class task1Spider(scrapy.Spider):
    name = 'task1'
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']

    def parse(self, response):
        products = response.css('div.product')
        for product in products:
            title = product.css('a.catalog-item-name::text').get().strip()
            maftr = product.css('a.catalog-item-brand::text').get().strip()
            price = float(product.css('span.price').css('span::text').get().replace('$', ''))
            status = product.css('span.status').css('span::text').get()
            if status == 'Out of Stock':
                stock = False
            else:
                stock = True

            yield{
                    'price': price, # type(float)
                    'title': title, # type(string)
                    'stock': stock, # type(boolean)
                    'maftr': maftr  # type(string)
                }