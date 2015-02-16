# twse

## Usage

### 更新該抓的清單

1. 先去 `http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php` 下載昨日全部資料
2. 更改 `getCurrentList.py` 中的 `FILE_NAME`, `FIRST_INDEX`, 和 `LAST_INDEX`
3. <code>python getCurrentList.py</code> 就可以在 `stocknumber.csv` 中看到昨天為止還存活的清單了。

### 沒有的抓全部、有的更新

<code>python crawl.py</code>

### 直接下載我抓好的資料

<code>git clone https://github.com/Asoul/twse.git</code> 抓完後，`/data` 內的就是所有資料囉

## Note

1. 連續抓到過去某一個月無資料就停止 

## TODOs

1. http://mis.twse.com.tw/stock/fibest.jsp
2. 處理沒有內容的檔案

## 資料來源

台灣證券交易所 `http://www.twse.com.tw/`

## 聯絡我

有 Bug 麻煩跟我說：`azx754@gmail.com`

最後更新時間：`2015/02/13`