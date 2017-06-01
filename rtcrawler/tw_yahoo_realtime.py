# -*- coding:utf-8 -*-  
import json
import csv
import urllib,urllib2
import lxml  
import lxml.html as HTML  
import lxml.etree as etree
from bs4 import BeautifulSoup

class YahooWebStockCrawler():
    def getTargetURL(self, stockNum):
        targetURL = 'https://tw.stock.yahoo.com/q/q?s=' + stockNum
        return targetURL
    def parseURL(self, targetURL):
        #html_file = urllib2.urlopen(targetURL)
        req = urllib2.Request(targetURL, headers={ 'User-Agent': 'Mozilla/5.0' })
        html_file = urllib2.urlopen(req)
        #html_doc =  html_file.read().decode('big5').encode('utf8')
        html_doc =  html_file.read()
        html_file.close()
        return html_doc
    def getVolume(self, html_doc, soup):
        #soup = BeautifulSoup(html_doc)
        volume = soup.findAll('td',align="center", nowrap="")[6].contents[0]
        #print volume
        return volume
    def getHighest(self, html_doc, soup):
        #soup = BeautifulSoup(html_doc)
        hprice = soup.findAll('td',align="center", nowrap="")[9].contents[0]
        #print volume
        return hprice
    def getLowest(self, html_doc, soup):
        #soup = BeautifulSoup(html_doc)
        lprice = soup.findAll('td',align="center", nowrap="")[10].contents[0]
        #print volume
        return lprice   
    def getRTprice(self, html_doc, soup):
        #soup = BeautifulSoup(html_doc)
        rtprice = soup.findAll('td',align="center", nowrap="")[2].contents[0].contents[0]
        return rtprice

def main():
    crawler = YahooWebStockCrawler()
    targetURL = crawler.getTargetURL('2498')
    html_doc = crawler.parseURL(targetURL)
    soup = BeautifulSoup(html_doc)
    print crawler.getVolume(html_doc, soup)
    print crawler.getRTprice(html_doc, soup)
    
if __name__ == '__main__':
    main()

        