# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import datetime

dbuser = 'root'
dbpass = 'www.123.com'
dbname = 'test'
dbhost = '10.1.1.83'
dbpost = '3306'

class cCopyRightPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=dbname, host = dbhost, charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()
        #Clear Table
        #self.cursor.execute("truncate table cCopyRight;")
        self.conn.commit();

    def process_item(self, item, spider):
        curDate = datetime.datetime.now().date()
        try:
            self.cursor.execute("""INSERT INTO cCopyRight (number, type, name, shortName, version, company, publishDate, registerDate, dataVersion)  
                                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                                (
                                    item['number'].encode('utf-8'), 
                                    item['type'].encode('utf-8'),
                                    item['name'].encode('utf-8'),
                                    item['shortName'].encode('utf-8'),
                                    item['version'].encode('utf-8'),
                                    item['company'].encode('utf-8'),
                                    item['publishDate'].encode('utf-8'),
                                    item['registerDate'].encode('utf-8'),
                                    curDate,
                                )
            )

            self.conn.commit()
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
        return item

