#!/usr/bin/env pythonmZ
# -*- coding: utf-8 -*-
#import pdb
import scrapy
from ccopyrightSpider.items import CCopyRightItem
from pyquery import PyQuery as pq
 
class CCopyRightSpider(scrapy.Spider):
    name = 'CatchCCopyRight'
    allowed_domains = ['ccopyright.com.cn']
    start_urls = [
            "http://www.ccopyright.com.cn/cpcc/RRegisterAction.do?method=list&no=fck&sql_name=&sql_regnum=&sql_author=%C9%CF%BA%A3&curPage=1"
    ]

    def parse(self, response):
        startPageIndex = 0
        endPageIndex = 0
        pageRange = open("/root/ccrSpider/ccopyrightSpider/pageIndexRange.txt")
        for line in pageRange:
            if startPageIndex == 0:
                startPageIndex = int(line)
            else:
                endPageIndex = int(line) + 1
        pageRange.close()

        for pageIndex in range(startPageIndex, endPageIndex):
	    #print str(pageIndex-startPageIndex)
	    #print str(endPageIndex - startPageIndex)
            print "PageIndex of Shanghai CopyRight:["+ str(pageIndex) + "]  From Page "+str(startPageIndex)+" to Page "+str(endPageIndex - 1)+" [ "+ str((pageIndex - startPageIndex)*100/(endPageIndex - startPageIndex))  +" Percent Finished ]"
            
            doc = pq(
                "http://www.ccopyright.com.cn/cpcc/RRegisterAction.do?method=list&no=fck&sql_name=&sql_regnum=&sql_author=%C9%CF%BA%A3&curPage="+str(pageIndex)
            )
            #pdb.set_trace()
            id = 1
            for i in range(10):
                id+=1;
                item = CCopyRightItem()
                print "getScript: doc(u'form[name=""generalForm""] table:eq(1) tr:eq("+str(id)+") td:eq(0)').text()"
                item['number'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(0)').text()
                item['type'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(1)').text()
                item['name'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(2)').text()
                item['shortName'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(3)').text()
                item['version'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(4)').text()
                item['company'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(5)').text()
                item['publishDate'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(6)').text()
                item['registerDate'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(7)').text()
                yield item
