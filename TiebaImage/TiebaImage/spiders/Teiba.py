import scrapy
from ..items import  *
class TiebaSpider(scrapy.Spider):
    name = "Tieba"
    def start_requests(self):
        with  open('tiebalist.txt','r') as f:
            tiebalist=f.read()
        urls = tiebalist.split()[0,100]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        #   ['https://tieba.baidu.com/f?kw=%E8%A1%A8%E6%83%85%E5%8C%85&ie=utf-8']
    def parse(self, response):
        baseurl=response.url+'&pn={}'
        for  i  in range (0,100):
            furl=baseurl.format(str(i*50))
            yield scrapy.Request(furl, callback=self.parse_Tiezi)
    def   parse_Tiezi(self,response):
        for  href  in response.xpath('//ul[@id="thread_list"]//div[@class="t_con cleafix"]//div[@class="threadlist_title pull_left j_th_tit "]//a//@href').extract():
            yield response.follow(href, callback=self.parse_page)
    def  parse_page(self,response):
        image_urls=response.xpath('//img[@class="BDE_Image"]/@src').extract()
        if image_urls:
            item = TiebaImgsItem()
            item['image_urls'] = image_urls
            yield item
        pages=response.xpath('//li[@class="l_pager pager_theme_5 pb_list_pager"]//a/@href').extract()
        for  page in  pages:
           yield  response.follow(page,parse_page)
