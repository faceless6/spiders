# -*- coding: utf-8 -*-
import scrapy
from fangtianxiaershoufang.items import ftxershouItem,ftxershouItemLoader
from scrapy.http import Request
from urllib import parse
from datetime import datetime

class ErshouSpider(scrapy.Spider):
    name = 'ershou'
    allowed_domains = ['www.http://esf.fang.com/']
    start_urls = ['']

    def parse(self, response):

        ershou_items = ftxershouItem()
        nodes=response.css('.list.rel')
        for node in nodes:
            title=node.css('.title a ::attr(title)').extract_first("")#标题
            huxing=node.xpath('//p[@class="mt12"]/text()[1]').extract_first("").strip()#户型
            louceng=node.xpath('//p[@class="mt12"]/text()[2]').extract_first("").strip()#楼层
            chaoxiang=node.xpath('//p[@class="mt12"]/text()[3]').extract_first("").strip()#朝向
            niandai=node.xpath('//p[@class="mt12"]/text()[4]').extract_first("").strip()#年代
            xiaoqu=node.css('.mt10 span ::text').extract_first("")#小区
            dizhi=node.css('.mt10 span:nth-child(2) ::text').extract_first("")#地址
            huzhu=node.css('.gray6.mt10 a ::text').extract_first("")#户主
            mianji=node.css('.area.alignR p:nth-child(1) ::text').extract_first("")#面积
            zongjia=node.css('.mt5.alignR .price::text').extract_first("")#总价
            danjia=node.css('.danjia.alignR.mt5 ::text').extract_first("")#单价
            ershou_items['title']=title
            ershou_items['huxing']=huxing
            ershou_items['louceng']=louceng
            ershou_items['chaoxiang']=chaoxiang
            ershou_items['niandai']=niandai
            ershou_items['xiaoqu']=xiaoqu
            ershou_items['dizhi']=dizhi
            ershou_items['huzhu']=huzhu
            ershou_items['mianji']=mianji
            ershou_items['zongjia']=zongjia
            ershou_items['danjia']=danjia
            ershou_items['crawl_time']=str(datetime.now())
            yield ershou_items
        # item_loader = ftxershouItemLoader(item=ftxershouItem(), response=response)
        #
        # item_loader.add_css('title', '.houseList .title a ::attr(title)')  # 标题
        # item_loader.add_xpath('huxing', '//p[@class="mt12"]/text()[1]')  # 户型
        # item_loader.add_xpath('louceng', '//p[@class="mt12"]/text()[2]')  # 楼层
        # item_loader.add_xpath('chaoxiang', '//p[@class="mt12"]/text()[3]')  # 朝向
        # item_loader.add_xpath('niandai', '//p[@class="mt12"]/text()[4]')  # 年代
        # item_loader.add_css('xiaoqu', '.houseList .mt10 span ::text')  # 小区
        # item_loader.add_css('dizhi', '.houseList .mt10 span:nth-child(2) ::text')  # 地址
        # item_loader.add_css('huzhu', '.houseList .gray6.mt10 a ::text')  # 户主
        # item_loader.add_css('mianji', '.houseList .area.alignR p:nth-child(1) ::text')#面积
        # item_loader.add_css('zongjia', '.houseList .mt5.alignR .price::text')  # 总价
        # item_loader.add_css('danjia', '.houseList .danjia.alignR.mt5 ::text')  # 单价
        # item_loader.add_value('crawl_time', str(datetime.now()))  # 爬取时间
        #
        # ershou_items = item_loader.load_item()
        # yield ershou_items
        next_url=response.css('.fanye.gray6 #PageControl1_hlk_next ::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse,dont_filter=True)


    # def start_requests(self):
    #
    #     starturl='http://esf.fang.com/house-a01/y71/'
    #     yield Request(url=starturl,callback=self.parse_after)


    # def parse_after(self,response):
    #     ershou_items=ftxershouItem()
    #     item_loader=ftxershouItemLoader(item=ftxershouItem(),response=response)
    #     item_loader.add_css('title','.houseList .title a ::attr(title)')#标题
    #     item_loader.add_xpath('huxing','//p[@class="mt12"]/text()[1]')#户型
    #     item_loader.add_xpath('louceng','//p[@class="mt12"]/text()[2]')#楼层
    #     item_loader.add_xpath('chaoxiang','//p[@class="mt12"]/text()[3]')#朝向
    #     item_loader.add_xpath('niandai','//p[@class="mt12"]/text()[4]')#年代
    #     item_loader.add_css('xiaoqu','.houseList .mt10 span ::text')#小区
    #     item_loader.add_css('dizhi','.houseList .mt10 span:nth-child(2) ::text')#地址
    #     item_loader.add_css('huzhu','.houseList .gray6.mt10 a ::text')#户主
    #     item_loader.add_css('mianji','.houseList .area.alignR p:nth-child(1) ::text')#面积
    #     item_loader.add_css('zongjia','.houseList .mt5.alignR .price::text')#总价
    #     item_loader.add_css('danjia','.houseList .danjia.alignR.mt5 ::text')#单价
    #     item_loader.add_value('crawl_time',str(datetime.now()))#爬取时间
    #
    #     ershou_items=item_loader.load_item()
    #     yield ershou_items


