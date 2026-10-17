几个自己用的小脚本。没有商业项目，也没有播放量。

## rename_prefix.py

给一个文件夹里的文件加前缀。不加 `--apply` 只打印，不会改名。

```
python3 rename_prefix.py ./照片 2026-
python3 rename_prefix.py ./照片 2026- --apply
```

## csv_drop_empty.py

丢掉 CSV 里整行都空的记录，结果写到另一个文件。

```
python3 csv_drop_empty.py 原始.csv 干净.csv
```

## count_lines.py

数文本文件的非空行。认 txt、md、py、csv、json、yaml、srt。

```
python3 count_lines.py .
```

Python 3 就行，不用装包。
