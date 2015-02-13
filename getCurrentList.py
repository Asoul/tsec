#!/bin/python
# -*- coding: utf-8 -*-

import csv

FIRST_INDEX = '0050'
LAST_INDEX = '9958'
FILE_NAME = 'A11220150212ALL.csv' 

f = open(FILE_NAME, 'rb')

startFlag = False
stock_list = []
count = 0
for row in csv.reader(f, delimiter=','):
    # 0050 是當日股票清單第一個
    if not startFlag and len(row) > 1 and row[0].replace("=","").replace("\"","").replace("\'","").strip() == FIRST_INDEX:
        startFlag = True

    if startFlag:
        if row[0].find('=') >= 0:
            stock_list.append(row[0].replace("=","").replace("\"","").replace("\'","").strip())
        else:
            stock_list.append(row[0].strip())
        # 9958 是當日股票清單最後一個
        if row[0].strip() == LAST_INDEX:
            break
fo = open('stocknumber.csv', 'wb')
cw = csv.writer(fo, delimiter=',')
for stock_index in stock_list:
    cw.writerow([stock_index])