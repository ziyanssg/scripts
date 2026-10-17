#!/usr/bin/env python3
"""给一个文件夹里的文件加上前缀。默认只预览，加 --apply 才改名。"""

import argparse
from pathlib import Path


def plan(folder: Path, prefix: str):
    changes = []
    for path in sorted(p for p in folder.iterdir() if p.is_file()):
        if path.name.startswith(prefix):
            continue
        changes.append((path, path.with_name(prefix + path.name)))
    return changes


def main():
    parser = argparse.ArgumentParser(description="给文件名加前缀")
    parser.add_argument("folder", type=Path)
    parser.add_argument("prefix")
    parser.add_argument("--apply", action="store_true", help="真正改名。不加就只打印")
    args = parser.parse_args()
    if not args.folder.is_dir():
        raise SystemExit(f"不是文件夹: {args.folder}")
    changes = plan(args.folder, args.prefix)
    if not changes:
        print("没有要改的文件")
        return
    for src, dst in changes:
        print(f"{src.name} -> {dst.name}")
        if args.apply:
            src.rename(dst)


if __name__ == "__main__":
    main()
