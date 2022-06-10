# Markdown Calendar Generator

## Examples
To get the markdown calendar of June, 2022, just run 

`python main.py --year 2022 --month 6 --start_sunday`

```
| Sun             | Mon             | Tue             | Wed             | Thu             | Fri             | Sat             |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
|                 |                 |                 | [1](#20220601)  | [2](#20220602)  | [3](#20220603)  | [4](#20220604)  |
| [5](#20220605)  | [6](#20220606)  | [7](#20220607)  | [8](#20220608)  | [9](#20220609)  | [10](#20220610) | [11](#20220611) |
| [12](#20220612) | [13](#20220613) | [14](#20220614) | [15](#20220615) | [16](#20220616) | [17](#20220617) | [18](#20220618) |
| [19](#20220619) | [20](#20220620) | [21](#20220621) | [22](#20220622) | [23](#20220623) | [24](#20220624) | [25](#20220625) |
| [26](#20220626) | [27](#20220627) | [28](#20220628) | [29](#20220629) | [30](#20220630) |                 |                 |
```

Japanese calendars are also supported

`python main.py --start_sunday --locale 'ja_JP'`

```
| 日              | 月              | 火              | 水              | 木              | 金              | 土              |
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
|                 |                 |                 | [1](#20220601)  | [2](#20220602)  | [3](#20220603)  | [4](#20220604)  |
| [5](#20220605)  | [6](#20220606)  | [7](#20220607)  | [8](#20220608)  | [9](#20220609)  | [10](#20220610) | [11](#20220611) |
| [12](#20220612) | [13](#20220613) | [14](#20220614) | [15](#20220615) | [16](#20220616) | [17](#20220617) | [18](#20220618) |
| [19](#20220619) | [20](#20220620) | [21](#20220621) | [22](#20220622) | [23](#20220623) | [24](#20220624) | [25](#20220625) |
| [26](#20220626) | [27](#20220627) | [28](#20220628) | [29](#20220629) | [30](#20220630) |                 |                 |
```

## Options

- `--year`: Integer specifying the year. Default value is the current year.

- `--month`: Integer specifying the month. Default value is the current month.

- `--locale`: String specifying the locale. Default value is "en_US". "ja_JP" and "zh_TW" are also available.

- `--link_style`: String specifying the style of the hyperlink. Default value is "%Y%m%d".

- `--format`: String specifying the output format. Default value is "md". "csv" is also available.

- `--start_sunday`: Flag that specifys whether a week starts from Sunday.