#!/usr/bin/env python3
"""丢掉 CSV 里整行都是空的记录，写到新文件。"""

import argparse
import csv
from pathlib import Path


def drop_empty(src: Path, dst: Path):
    with src.open(newline="", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    if not rows:
        kept = []
    else:
        header, body = rows[0], rows[1:]
        kept = [header] + [row for row in body if any(cell.strip() for cell in row)]
    with dst.open("w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(kept)
    return len(rows) - len(kept)


def main():
    parser = argparse.ArgumentParser(description="删除 CSV 空行")
    parser.add_argument("src", type=Path)
    parser.add_argument("dst", type=Path)
    args = parser.parse_args()
    removed = drop_empty(args.src, args.dst)
    print(f"去掉 {removed} 行，写到 {args.dst}")


if __name__ == "__main__":
    main()
