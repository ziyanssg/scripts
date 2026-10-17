#!/usr/bin/env python3
"""数一个文件夹里文本文件的行数。跳过空行。"""

import argparse
from pathlib import Path

TEXT = {".txt", ".md", ".py", ".csv", ".json", ".yaml", ".yml", ".srt"}


def count(folder: Path):
    total = 0
    files = 0
    for path in sorted(p for p in folder.rglob("*") if p.is_file() and p.suffix.lower() in TEXT):
        lines = 0
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip():
                lines += 1
        print(f"{lines}\t{path}")
        total += lines
        files += 1
    print(f"合计 {files} 个文件，{total} 行")
    return total


def main():
    parser = argparse.ArgumentParser(description="数文本行数，不算空行")
    parser.add_argument("folder", type=Path)
    args = parser.parse_args()
    if not args.folder.is_dir():
        raise SystemExit(f"不是文件夹: {args.folder}")
    count(args.folder)


if __name__ == "__main__":
    main()
