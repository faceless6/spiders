# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
import MySQLdb.cursors
class FangtianxiaershoufangPipeline(object):
    def process_item(self, item, spider):
        return item
class MysqlTwistedPipline(object):
    #异步插入mysql数据库 一般为固定模式 只需更改do_insert方法的插入语句即可
    def __init__(self,dbpool):
        self.dbpool=dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparms=dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool=adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)
    def process_item(self,item,spider):
        #使用twisted将mysql变成异步插入
        qurey=self.dbpool.runInteraction(self.do_insert,item)
        qurey.addErrback(self.handle_error,item,spider)
    def handle_error(self,failure,item,spider):
        #处理异步插入的异常
        print(failure)
    def do_insert(self, cursor, item):
        #具体的插入语句
        insert_sql, params = item.get_insert_sql()
        cursor.execute(insert_sql,params)