# Change Log

Here you can see the full list of notable changes.

## [1.0.1] - 2016/03/27

### Added

- 加上 check flag 往回爬遺失的資料，和重複確認資料，之後每天都會往回爬 10 天
- 加上 `post_process.py` 會把重複的去掉，和把資料按日期排
- 補上中間遺失的資料

## [1.0.0] - 2016/02/15

### Added

- 補上之前不在清單裡的資料
- 開始用 `CHANGELOG.md`

### Fixed

- 檢查資料時發現一些資料過去爬的時候爬到的跟現在再去爬的不一樣，不知道原因，已經換上更正的資料

### Changed

- 更新 `crawl.py`，現在會爬所有上市上櫃股票
- 更新 `error.log` 移到 `log/crawl-error.log`

### Removed

- 移除 `A11220150212ALL.csv` 、 `getCurrentList.py` 、 `stocknumber.csv`，現在去抓所有清單，已經用不到了
- 移除 `validateData.py`

### TODOs

- 補上 TSE 在 2004 之前有缺漏的檔案
- 補上 OTC 過去的資料，2007 年之前的資料有不完整的