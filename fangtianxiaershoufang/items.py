# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst

class FangtianxiaershoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
def return_value(value):
    return value
def rm_kongge(value):
    return value.strip()
class ftxershouItem(scrapy.Item):
    title=scrapy.Field(
        input_processor=MapCompose(return_value)
    )
    huxing=scrapy.Field(
        input_processor=MapCompose(rm_kongge)
    )
    louceng=scrapy.Field(
        input_processor=MapCompose(rm_kongge)
    )
    chaoxiang=scrapy.Field(
        input_processor=MapCompose(rm_kongge)
    )
    niandai=scrapy.Field(
        input_processor=MapCompose(rm_kongge)
    )
    xiaoqu=scrapy.Field()
    mianji=scrapy.Field()
    huzhu=scrapy.Field()
    danjia=scrapy.Field()
    zongjia=scrapy.Field()
    dizhi=scrapy.Field()
    crawl_time=scrapy.Field()
    def get_insert_sql(self):
        insert_sql="""
            insert into fangtianxiaershoufang(title,huxing,louceng,chaoxiang,niandai,xiaoqu,mianji,huzhu,danjia,zongjia,dizhi,crawl_time)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE title=VALUES (title),crawl_time=VALUES (crawl_time),danjia=VALUES (danjia),zongjia=VALUES (zongjia) 
         
        """

        params=(self['title'],self['huxing'],self['louceng'],self['chaoxiang'],self['niandai'],self['xiaoqu'],self['mianji'],self['huzhu'],self['danjia'],self['zongjia'],self['dizhi'],self['crawl_time'])

        return insert_sql,params

class ftxershouItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
