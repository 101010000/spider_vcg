import scrapy
from scrapy_VCG.items import ScrapyVcgItem

class VcgSpider(scrapy.Spider):
    name = "vcg"
    allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.xxx.com/xxx/xxx/"]
    base_url = "https://www.xxx.com/xxx/xxx/?page="
    page = 1
    def parse(self, response):
        # //div[@class="gallery_inner"]/figure[@class="galleryItem"]/a/@title
        # //div[@class="gallery_inner"]/figure[@class="galleryItem"]/a/img/@src
        path_list = response.xpath('//div[@class="gallery_inner"]/figure[@class="galleryItem"]/a')
        for li in path_list:
            name = li.xpath('.//@title').extract_first()
            src =  li.xpath('.//img/@data-src').extract_first()
            book = ScrapyVcgItem(name=name,src=src)
            yield book
#        https://www.xxx.com/xxx/xxx/?page=2
#        https://www.xxx.com/xxx/xxx/?page=3
        if self.page < 22:
            self.page += 1
            url = self.base_url + str(self.page)
            yield scrapy.Request(url=url,callback=self.parse)
