#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
from os import listdir
from os.path import isfile, join


mypath = 'data'
file_list = [ f for f in listdir(mypath) if f[-4:] == '.csv' ]

for f in file_list:
    csvfile = open(join(mypath,f), 'rb')
    rows = []
    for row in csv.reader(csvfile, delimiter=','):
        rows.append(row)
    rows.reverse()
    csvfile.close()
    fo = open(join(mypath,f), 'wb')
    cw = csv.writer(fo, delimiter=',')
    for row in rows:
        cw.writerow(row)