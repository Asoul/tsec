#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import html
import requests
import csv
from os.path import isfile, join, getsize
from datetime import datetime, date, timedelta

# 從 stocknumber.csv 中讀出要爬的股票清單
stock_id_list = [line.strip() for line in open('stocknumber.csv', 'rb')]

# 錯誤輸出檔案
error_log = open('error.log', 'a')

def perror(error_str):
    error_log.write(error_str+'\n')
    print error_str

for stock_id in stock_id_list:
    row_count = 0
    for row in  csv.reader(open('data/'+stock_id+'.csv', 'rb'), delimiter=','):
        row_count += 1
        # 交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數，共 9 欄。

        if len(row) != 9:
            perror('%s %d : row length error' % (stock_id, row_count))
        
        # 日期錯誤
        if len(row[0].split('/')) != 3:
            perror('%s %d : time length error' % (stock_id, row_count))

        year, month, day = [int(x) for x in row[0].split('/')]
        if year > (datetime.now().year-1911) or year < 80:
            perror('%s %d : year error' % (stock_id, row_count))
        if month > 12 or month < 1:
            perror('%s %d : month error' % (stock_id, row_count))
        if day > 31 or day < 1:
            perror('%s %d : day error' % (stock_id, row_count))

        # 日期回溯
        if row_count > 2 and (yesterday - date(year+1911, month, day)).days > 0:
            perror('%s %d : date reverse %d/%d/%d to %d/%d/%d' % (stock_id, row_count, yesterday.year, yesterday.month, yesterday.day, year, month, day))
        
        yesterday = date(year+1911, month, day)
        
        # 沒有交易
        if row[3] == '--' and row[4] == '--' and row[5] == '--' and row[6] == '--':
            continue

        # 神奇的都是 0
        if (row[1] == '0.0' and row[2] == '0.0' and row[3] == '0.0' and row[4] == '0.0' and
            row[5] == '0.0' and row[6] == '0.0' and row[7] == '0.0' and row[8] == '0.0'):
           continue

        # 有時候會只有交易股數和金額和漲跌價差
        if row[3] == '0.0' and row[4] == '0.0' and row[5] == '0.0' and row[6] == '0.0':
            continue

        # 其他錯誤
        if float(row[1]) <= 0:
            perror('%s %d : volume error %f' % (stock_id, row_count, float(row[1])))
        if float(row[2]) <= 0:
            perror('%s %d : money error %f' % (stock_id, row_count, float(row[2])))
        if float(row[3]) <= 0:
            perror('%s %d : start error %f' % (stock_id, row_count, float(row[3])))
        if float(row[4]) < float(row[5]):
            perror('%s %d : high low error %f < %f' % (stock_id, row_count, float(row[4]), float(row[5])))
        if float(row[6]) <= 0:
            perror('%s %d : close error %f' % (stock_id, row_count, float(row[6])))
        if float(row[8]) <= 0:
            perror('%s %d : trade error %f' % (stock_id, row_count, float(row[8])))

