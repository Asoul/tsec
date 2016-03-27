# Taiwan Stock Exchange Crawler

這是一個去爬 [台灣證券交易所](http://www.twse.com.tw/) 和 [證券櫃檯買賣中心](http://www.tpex.org.tw/) 的爬蟲，秉持著 Open Data 的理念，公開爬蟲公開資料最安心。

## Note

2016/02/15 - 過年重大更新，把爬蟲速度提升很多，也把過去的一些資料補上，詳情請看 [更新日誌](https://github.com/Asoul/tsec/blob/master/CHANGELOG.md)

## Setup

```
$ git clone https://github.com/Asoul/tsec.git

$ cd tsec

$ pip install -r requirements.txt
```

## Usage

### Command

爬當日

```
$ python crawl.py
```

爬指定日期

```
$ python crawl.py YYYY MM DD

e.g.

$ python crawl.py 2016 02 15
```

### Flag

`-b, --back`: 往回爬直到 `2004/2/11`

`-c, --check`: 往回爬 10 天

### 後處理

清除重複的檔案，按日期排序

```
$ python post_process.py
```

## 資料格式

- 每個檔案的檔名 `XXX.csv`，`XXX` 是股票編號
- 每個檔案中有數列，每列為一天交易的資訊
- 每列包含：交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數，共 9 欄。
- 符號說明: +表示漲、- 表示跌、X表示不比價
- 當日統計資訊含一般、零股、盤後定價、鉅額交易，不含拍賣、標購。

範例：`104/02/13,7599922.0,528270219.0,69.35,69.65,69.35,69.45,0.45,1771.0`

## 資料來源

- [台灣證券交易所](http://www.twse.com.tw/)

- [證券櫃檯買賣中心](http://www.tpex.org.tw/)

## 附上免責聲明

本人旨在為廣大投資人提供正確可靠之資訊及最好之服務，作為投資研究的參考依據，若因任何資料之不正確或疏漏所衍生之損害或損失，本人將不負法律責任。是否經由本網站使用下載或取得任何資料，應由您自行考量且自負風險，因任何資料之下載而導致您電腦系統之任何損壞或資料流失，您應負完全責任。

## 聯絡我

有 Bug 麻煩跟我說，改進的地方或交流也非常歡迎：`azx754@gmail.com`

最後更新時間：`2016/02/15`

## 我的其他專案

[股票即時資料爬蟲](https://github.com/Asoul/tsrtc)
