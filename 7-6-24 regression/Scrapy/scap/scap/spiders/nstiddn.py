import  scrapy
from urllib.parse import urllib
import csv


class EciSpider(scrapy.spider):
    name = 'adit'
    allowed_domains = ['https://results.eci.gov.in/P']
    start_urls = ['https://results.eci.gov.in/PcResultGenJune2024/index.htm']
    count=0
    custom_settings = {
        'download_delay':1
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        party_urls = response.xpath('//table[@class="table"]/tbody/tr/td[2]/a/@href')
        for party_url in party_urls:
            absolute_party_url = urljoin(response.url, party_url)
            yield response.follow(absolute_party_url,callback=self.parse_constituecny)