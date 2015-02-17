# Taiwan Stock Exchange Crawler

這是一個去爬 [台灣證券交易所](http://www.twse.com.tw/) 的爬蟲，秉持著 open data 的理念，公開爬蟲公開資料最安心。

## 用法

### 直接下載我抓好的資料

1. [直接下載 ZIP](https://github.com/Asoul/twse/archive/master.zip)

2. 或來個 command line： `git clone https://github.com/Asoul/twse.git`

抓完後，`data` 內就是所有資料囉

### 沒有的抓全部、有的更新

<code>python crawl.py</code>

### 更新該抓的清單 (optional)

1. 先去 `http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php` 下載昨日全部資料
2. 更改 `getCurrentList.py` 中的 `FILE_NAME`, `FIRST_INDEX`, 和 `LAST_INDEX`
3. `python getCurrentList.py` 後，就可以在 `stocknumber.csv` 中看到昨天為止還存活的清單了，再接續用 `python crawl.py` 抓。

### 爬蟲須知

1. 爬蟲會連續抓到過去某一個月無資料就停止，所以可能有分段超過一個月的股票舊的就不會被抓到。
2. 有時候爬蟲戳一些不常被搜尋的股票會戳不到東西，目前不知原因為何，目前解法是開 Sikuli 把那些戳不到的清單戳一遍。
3. 最近放年假了，資料停在 `02/13`，年後應該會每日下午定時更新，祝大家新年快樂。

## 資料格式

1. 每個檔案的檔名 `XXX.csv`，`XXX` 是股票編號
2. 每個檔案中有數列，每列為一天交易的資訊
3. 每列包含：交易日期、成交股數、成交金額、開盤價、最高價、最低價、收盤價、漲跌價差、成交筆數，共 9 欄。
4. 符號說明: +表示漲、- 表示跌、X表示不比價
5. 當日統計資訊含一般、零股、盤後定價、鉅額交易，不含拍賣、標購。

範例：104/02/13,7599922.0,528270219.0,69.35,69.65,69.35,69.45,0.45,1771.0

## TODOs

1. 即時報價（http://mis.twse.com.tw/stock/fibest.jsp）
2. 可以把分段超過一個月的股票也抓一抓

## 資料來源

台灣證券交易所 `http://www.twse.com.tw/`

## 附上免責聲明

本人旨在為廣大投資人提供正確可靠之資訊及最好之服務，作為投資研究的參考依據，若因任何資料之不正確或疏漏所衍生之損害或損失，本人將不負法律責任。是否經由本網站使用下載或取得任何資料，應由您自行考量且自負風險，因任何資料之下載而導致您電腦系統之任何損壞或資料流失，您應負完全責任。

## 聯絡我

有 Bug 麻煩跟我說：`azx754@gmail.com`

最後更新時間：`2015/02/17`

## 贊助我

歡迎大家贊助辛苦大學生 >＿＿＿＿<

<form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
">
<input type="image" src="https://www.paypal.com/zh_HK/i/btn/btn_donateCC_LG.gif" border="0" name="submit" alt="PayPal － 更安全、更簡單的線上付款方式！">
<img alt="" border="0" src="https://www.paypalobjects.com/zh_TW/i/scr/pixel.gif" width="1" height="1">
</form>
