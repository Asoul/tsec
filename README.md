# twse

## Usage

### 更新該抓的清單

1. 先去 `http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php` 下載昨日全部資料
2. 更改 `getCurrentList.py` 中的 `FILE_NAME`, `FIRST_INDEX`, 和 `LAST_INDEX`
3. <code>python getCurrentList.py</code> 就可以在 `stocknumber.csv` 中看到昨天為止還存活的清單了。

### 抓全部（會把舊的檔案刪掉）

<code>python crawl.py</code>

### 抓完全部後重新排序（因為抓完會倒著排）

### 只更新

### 直接下載我抓好的資料

<code>git clone https://github.com/Asoul/twse.git</code> 抓完後，`/data` 內的就是所有資料囉

## Note

1. 連續抓到過去某一個月無資料就停止 

## TODOs

1. 讓他可以只更新
2. 讓他可以相反排序

## 資料來源

台灣證券交易所 `http://www.twse.com.tw/`

## 聯絡我

有 Bug 麻煩跟我說：`azx754@gmail.com`

最後更新時間：`2015/02/13`