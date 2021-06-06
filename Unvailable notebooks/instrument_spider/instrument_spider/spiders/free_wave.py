from scrapy import Spider,Request
from scrapy.loader import ItemLoader
import os,sys
sys.path.append(r"C:\Users\DELL\Desktop\MySpiders\instrument_spider\instrument_spider")
from items import CrawlerItem

class free_wave_sample(Spider):
    name = "free_wave"
    def start_requests(self):
        urls = [
            r"https://freewavesamples.com/"
        ]
        for url in urls:
            yield Request(url=url, callback=self.parse, meta={'root_url': url})

    def parse(self, response):
        rela_links = response.xpath("//p[@class='leafnode']//@href").getall()
        
        for  link in rela_links:
            full_path = response.urljoin(link)
            yield Request(full_path, callback=self.parse_list_of_type)
    
    def parse_list_of_type(self, response):
        instrument_links = response.xpath(r"//h2//@href").getall()
        for link in instrument_links:
            yield response.follow(link, callback = self.extract_download)

        next_page = response.xpath("//a[@title='Next Page']/@href").get()
        if next_page:
            yield response.follow(next_page, callback = self.parse_list_of_type)
    
    def extract_download(self, response):
        loader = ItemLoader(item = CrawlerItem(), response = response)
        rela_url = response.xpath(r"//p[@class='graylink']//a/@href").get()
        file_url = response.urljoin(rela_url)
        type_name = "Unknown"
        extract_type_name =  response.xpath("//h2[@class='catname']//text()").getall()
        if extract_type_name:
            type_name = "".join(response.xpath("//h2[@class='catname']//a//text()").getall())
        loader.add_value("type_name", type_name)
        loader.add_value("file_urls", [file_url])
        return loader.load_item()
        