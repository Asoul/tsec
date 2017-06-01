import os
import re
import sys
import csv
import time
import string
import logging
import requests
import argparse
import glob
import math
from lxml import html
from datetime import datetime, timedelta
sys.path.append('../rtcrawler')
from tw_yahoo_realtime import YahooWebStockCrawler
from os import mkdir
from os.path import isdir


class Calc():
    def calc_volma(self, stock_id_csv, days):
        #os.chdir("./data")
        vol = 0
        m_days = days
        f = open(stock_id_csv, 'r')
        for row in csv.reader(f):
           vol += int(row[1])
           days = days - 1
           if days == 0:
               break
        f.close()
        vol = (vol / m_days) / 1000
        return vol

    def calc_valma(self, stock_id_csv, days):
        val = 0
        m_days = days
        val_array = []
        f = open(stock_id_csv, 'r')
        for row in csv.reader(f):
           if row[6] == '---':
               return 0
           #row[6] is closing price
           val += float(row[6])
           val_array.append(row[6])
           days = days - 1
           if days == 0:
               break
        f.close()
        val = round((val / m_days) + 0.001, 2)
        print stock_id_csv
        #print val_array
        return val
    def calc_std_dev(self, stock_id_csv, days):
        temp_val = 0
        m_days = days
        valma = self.calc_valma(stock_id_csv, days)
        print valma
        f = open(stock_id_csv, 'r')
        for row in csv.reader(f):
           if row[6] == '---':
               return 0
           
           temp_val += pow(float(row[6]) - valma, 2)
           days = days - 1
           if days == 0:
               break
        std_dev = round(pow(temp_val / m_days, 0.5) + 0.001, 2)
        f.close()

        print stock_id_csv
        #print val_array
        print std_dev * 2 + valma
        print valma - std_dev * 2
        return std_dev

def routine():
    calc = Calc()
    os.chdir("../ahcrawler/data")
    files = glob.glob('*.csv')
    # iterate over the list getting each file 
    for fle in files:
        vol = calc.calc_volma(fle, 10)
        #calc.calc_valma(fle, 20)
        #calc.calc_std_dev(fle, 20)
        if vol < 200:
            continue
        stockid = fle.split('.')[0]
        print stockid
if __name__ == '__main__':
    routine()
