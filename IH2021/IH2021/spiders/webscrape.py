# importing the scrapy module
import scrapy
  
class Extractdata(scrapy.Spider):
    name = "webscrape"
    allowed_domains = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
    start_urls = ['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1']
  
    # Parse function
    def parse(self, response):
          
        # Extra feature to get title
        price = response.xpath('//span[contains(@class, "price")]//text()').extract()
        title = response.css(".catalog-item-name::text").extract()
        status = response.xpath('//span[contains(@class, "status")]//text()').extract()
        manufacturer = response.css(".catalog-item-brand::text").extract()

        #Give the extracted content row wise
        for item in zip(price,title,status,manufacturer):
            #create a dictionary to store the scraped info
            scraped_info = {
                'price' : item[0],
                'title' : item[1],
                'status' : item[2],
                'manufacturer' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
