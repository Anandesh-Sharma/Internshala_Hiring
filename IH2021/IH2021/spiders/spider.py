import scrapy
from ..items import Ih2021Item

class IHAssignment(scrapy.Spider):

    # Couldn't get Rotating ip's using scrapy as Page Source didnt have IP's . IP's Were Encoded
    # If we can use any ip regarless of country the we can use package name - scrapy proxy pool
    # def start_requests(self):
    #     for url in self.start_urls:
    #         return scrapy.Request(url=url, callback=self.parse,headers={"User-Agent":"scrape web"},meta={"proxy":""})
    page_num = 2
    name = 'iha'
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']

    def parse(self, response):
        items = Ih2021Item()


        for i in response.css("div.product"):
            price = i.css("span.price span::text").extract()
            title = i.css("a.catalog-item-name::text").extract()
            if i.css("span.status span::attr(class)").extract()[0] == 'out-of-stock':
                stock = False
            else:               # to be more precise we can also use else if statement to check "in-stock"
                stock = True
            maftr = i.css("a.catalog-item-brand::text").extract()

            items["price"] = price
            items["title"] = title
            items["stock"] = stock
            items["maftr"] = maftr

            yield items

        # next_page = "https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=" + str(IHAssignment.page_num)
        #
        # if next_page is not None:
        #     IHAssignment.page_num += 1
        #     yield response.follow(next_page,callback= self.parse)

        #here is next page logic but the website is giving same page 1 on other currentpages so, it is going in infinite iteration