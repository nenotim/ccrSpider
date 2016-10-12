#!/usr/bin/env pythonmZ
# -*- coding: utf-8 -*-
#import pdb
import re
import scrapy
from ccopyrightSpider.items import CCopyRightItem
from pyquery import PyQuery as pq
 
class CCopyRightSpider(scrapy.Spider):
    name = 'catchCCRofSh'
    allowed_domains = ['ccopyright.com.cn']
    start_urls = [
            "http://www.ccopyright.com.cn"
    ]

    def printCatchPercent(self, pageIndex, startPageIndex, endPageIndex):
        print "========>> PageIndex of Shanghai CopyRight:["+ str(pageIndex) + "]  From Page "+str(startPageIndex)+" to Page "+str(endPageIndex - 1)+" [ "+ str((pageIndex - startPageIndex)*100/(endPageIndex - startPageIndex))  +" Percent Finished ]"
        

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

        maxPageIndex = 0
        for pageIndex in range(startPageIndex, endPageIndex):
            if maxPageIndex == 0:
                pattern = re.compile("\/共(\d*)页")
                res = pattern.search(doc(u'form[name="generalForm"] table:eq(2) td:eq(0)').text()).groups()
                print res[0]
                maxPageIndex = int(res[0])
            else:
                if pageIndex > maxPageIndex:
                    print "====>Reach Max Page : BREAK"
                    break
            self.printCatchPercent(pageIndex, startPageIndex, endPageIndex)
            doc = pq(
                "http://www.ccopyright.com.cn/cpcc/RRegisterAction.do?method=list&no=fck&sql_name=&sql_regnum=&sql_author=%C9%CF%BA%A3&curPage="+str(pageIndex)
            )
            #pdb.set_trace()
            d = 1
            for i in range(10):
                id+=1;
                item = CCopyRightItem()
                if len(doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(0)').text())==0:
                    continue
                item['number'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(0)').text()
                item['type'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(1)').text()
                item['name'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(2)').text()
                item['shortName'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(3)').text()
                item['version'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(4)').text()
                item['company'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(5)').text()
                item['publishDate'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(6)').text()
                item['registerDate'] = doc(u'form[name="generalForm"] table:eq(1) tr:eq('+str(id)+') td:eq(7)').text()
                yield item
