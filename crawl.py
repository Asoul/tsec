#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import html
import requests
import csv
from os.path import isfile, join, getsize
from datetime import date

# 從 stocknumber.csv 中讀出要爬的股票清單
stock_id_list = []
f = open('stocknumber.csv', 'rb')
for row in csv.reader(f, delimiter=','):
    stock_id_list.append(row[0])

# 錯誤輸出檔案
error_log = open('error.log', 'a')

# 輸入股票代號、年份、月份，輸出由遠至近的該月資料清單
def get_single_page(stock_id, year, month):

    page = requests.get('http://www.twse.com.tw/ch/trading/exchange/STOCK_DAY/genpage/Report'+year+month+'/'+year+month+'_F3_1_8_'+stock_id+'.php?STK_NO='+stock_id+'&myear='+year+'&mmon='+month)
    tree = html.fromstring(page.text)
    rows = []

    try:
        # Check Table Exist
        if len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]')) > 1:
            raise Exception('Find More Than 1 Table')
        if len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]')) == 0:
            # 該頁無內容
            return []

        # Check TR Content Exist
        tr_range = len(tree.xpath('//tr[@id="contentblock"]/td/table[@class="board_trad"]/tr'))
        if tr_range == 0:
            raise Exception('Can not found tr')
        if tr_range <= 2:# 前兩行會是表頭
            raise Exception('Find TR less than 2')

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

    except Exception as e:
        err_str = '[ERROR] stock_id = '+str(stock_id)+', year = '+str(year)+', month = '+str(month)+', tr_index = '+str(tr_index)+', td_index = '+str(td_index)
        print err_str
        error_log.write(err_str+'\n')
        print e
    
    return rows

for stock_id in stock_id_list:

    if isfile('data/'+stock_id+'.csv') and getsize('data/'+stock_id+'.csv') > 0: # file exist and not empty

        fi = open('data/'+stock_id+'.csv', 'rb')
        for row in csv.reader(fi, delimiter=','):
            pass
        if type(row[0]) != str or len(row[0].split('/')) != 3:
            # 舊的資料格式錯誤
            error_log.write(stock_id+", date format error\n")
            print stock_id, "date format error"
            continue

        old_year = int(row[0].split('/')[0])+1911
        old_month = int(row[0].split('/')[1])
        old_date = row[0]
        fi.close()

        fo = open('data/'+stock_id+'.csv', 'ab')
        cw = csv.writer(fo, delimiter=',')

        new_year = date.today().year
        new_month = date.today().month

        yearINT = old_year
        monthINT = old_month

        while True:
            year = str(yearINT).zfill(4)
            month = str(monthINT).zfill(2)
            print stock_id, year, month

            rows = get_single_page(stock_id, year, month)
            if len(rows) == 0:
                break
            
            if month == str(old_month).zfill(2):# 同一個月份
                startFlag = False
                for row in rows:
                    if row[0] == old_date:
                        startFlag = True
                    elif startFlag:
                        cw.writerow(row)
            else:# 之後的月份
                for row in rows:
                    cw.writerow(row)
            
            # next month
            if yearINT == new_year and monthINT == new_month:
                break
            else:
                monthINT += 1
                if monthINT == 12:
                    monthINT = 1
                    yearINT += 1
        
    else:
        fo = open('data/'+stock_id+'.csv', 'wb')
        cw = csv.writer(fo, delimiter=',')

        all_rows = []

        # For each page
        # TODO: 改成可以從任何月份開始，目前是2015/02 -> 其實就直接抓我的就好了吧(茶)
        date_range = [[x, y] for x in range(2015, 0, -1) for y in range(12, 0, -1)]
        for ym_pair in date_range[10:]:
            year = str(ym_pair[0]).zfill(4)
            month = str(ym_pair[1]).zfill(2)
            print stock_id, year, month

            rows = get_single_page(stock_id, year, month)
            if len(rows) == 0:# 沒東西了
                break

            rows.reverse()
            all_rows.extend(rows)

        all_rows.reverse()
        for row in all_rows:
            cw.writerow(row)
