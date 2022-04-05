import json
import scrapy
from bs4 import BeautifulSoup


class VrbospyderSpider(scrapy.Spider):
    name = 'vrbos'

    start_urls = ['https://www.vrbo.com/vacation-rentals/beach/usa/florida']

    def parse(self, response):
        # script = response.xpath('//script[2]').re_first('\((\[.*\])\)')
        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find_all('script')[25].text.strip()[29:-1] # remove 1st 29 char
        data = json.loads(script)

        #  data['abacus']['ha_gdpr_banner']['bucket']
        destinations = data['destination']['listings']
        for destination in destinations:
            yield {
                'property_name': destination['propertyName'],
                'property_price': destination['price']['value'],
                'property_thumb': destination['thumbnailUrl'],
                'property_details': destination['toplineDescription']
            }



