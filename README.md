# Taiwan Stock Exchange Crawler

## Usage

### 直接下載我抓好的資料

1. [直接下載 ZIP](https://github.com/Asoul/twse/archive/master.zip)

2. <code>git clone https://github.com/Asoul/twse.git</code> 

抓完
後，`data` 內就是所有資料囉

### 沒有的抓全部、有的更新

<code>python crawl.py</code>

### 更新該抓的清單 (optional)

1. 先去 `http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php` 下載昨日全部資料
2. 更改 `getCurrentList.py` 中的 `FILE_NAME`, `FIRST_INDEX`, 和 `LAST_INDEX`
3. <code>python getCurrentList.py</code> 就可以在 `stocknumber.csv` 中看到昨天為止還存活的清單了。

### 爬蟲須知

1. 爬蟲會連續抓到過去某一個月無資料就停止

## 資料格式

1. 每個檔案的檔名 `XXX.csv`，`XXX` 是股票編號
2. 每個檔案中有數列，每列為一天交易的資訊
3. 每列包含：交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數，共 9 欄。
4. 符號說明: +表示漲、- 表示跌、X表示不比價
5. 當日統計資訊含一般、零股、盤後定價、鉅額交易，不含拍賣、標購。

範例：104/02/13,7599922.0,528270219.0,69.35,69.65,69.35,69.45,0.45,1771.0

## TODOs

1. 即時報價（http://mis.twse.com.tw/stock/fibest.jsp）

## 資料來源

台灣證券交易所 `http://www.twse.com.tw/`

## 附上免責聲明

本人旨在為廣大投資人提供正確可靠之資訊及最好之服務，作為投資研究的參考依據，若因任何資料之不正確或疏漏所衍生之損害或損失，本人將不負法律責任。是否經由本網站使用下載或取得任何資料，應由您自行考量且自負風險，因任何資料之下載而導致您電腦系統之任何損壞或資料流失，您應負完全責任。

## 聯絡我

有 Bug 麻煩跟我說：`azx754@gmail.com`

最後更新時間：`2015/02/17`