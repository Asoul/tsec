#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import html
import requests
import csv

stock_id_list = []
f = open('stocknumber.csv', 'rb')
for row in csv.reader(f, delimiter=','):
    stock_id_list.append(row[0])

for stock_id in stock_id_list:

    fo = open('data/'+stock_id+'.csv', 'wb')
    cw = csv.writer(fo, delimiter=',')

    # For each page
    date_range = [[x, y] for x in range(2015, 0, -1) for y in range(12, 0, -1)]
    for ym_pair in date_range[10:]:
        year = str(ym_pair[0]).zfill(4)
        month = str(ym_pair[1]).zfill(2)
        print stock_id, year, month

        page = requests.get('http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report'+year+month+'/'+year+month+'_F3_1_8_'+stock_id+'.php')
        tree = html.fromstring(page.text)

        try:
            # Check Table Exist
            if len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]')) > 1:
                raise Exception('Find More Than 1 Table')
            if len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]')) == 0:
                # 該支股票抓完了
                break

            # Check TR Content Exist
            tr_range = len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]/tr'))
            if tr_range == 0:
                raise Exception('Can not found tr')
            if tr_range <= 2:# 前兩行會是表頭
                raise Exception('Find TR less than 2')

            rows = []

            for tr_index in range(3, tr_range+1):#xml path 的 index 會多 1
                
                row = []

                # date, ex.'98/02/02'
                date = tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]/tr['+str(tr_index)+']/td/div/text()')
                if len(date) == 0:
                    # 該月資料結束了
                    break
                if len(date) > 1:
                    raise Exception("Date more than 1")
                
                row.append(date[0])
                
                # TD contents
                td_range = len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]/tr['+str(tr_index)+']/td'))
                if td_range != 9:
                    raise Exception("Find TD Length not equal to 9")
                for td_index in range(2, td_range + 1):
                    td_content = tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]/tr['+str(tr_index)+']/td['+str(td_index)+']/text()')
                    if len(td_content) == 0:
                        raise Exception("TD content not exist")
                    if len(td_content) > 1:
                        raise Exception("TD content more than 1")

                    # convert TD content to float point
                    raw_str = td_content[0].replace(",","")
                    try:
                        float(raw_str)
                    except ValueError:
                        row.append(raw_str)
                    else:
                        row.append(float(raw_str))

                # output
                if len(row) != 9:
                    raise Exception("output length != 9")

                rows.append(row)

            rows.reverse()
            for row in rows:
                cw.writerow(row)


        except Exception as e:
            print '[ERROR] stock_id =',stock_id, ', year =', year, ', month =', month, ', tr_index =', tr_index,', td_index =', td_index
            print e
