import pycraigslist
import scrapy
import json

class BikeSpider(scrapy.Spider):
    name = "bikeSpider"

    def start_requests(self):
        bike_listing = pycraigslist.forsale.bia(site="worcester", has_image=True).search()
        self.log(bike_listing)
        urls = [result.get('url') for result in bike_listing]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):

        for posting_data in response.css('#ld_posting_data::text').getall():
            data = json.loads(posting_data.strip())
            source_url = response.request.url
            self.logger.debug(f'Data from source {source_url}: {data}')
            yield {
                'listing_url': response.request.url,
                'image_urls': data.get('image')
            }

    def closed(self, reason):
        start_time = self.crawler.stats.get_value('start_time')
        finish_time = self.crawler.stats.get_value('finish_time')
        print(f'Total run time: {finish_time - start_time}')
