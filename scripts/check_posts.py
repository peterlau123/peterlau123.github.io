#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
POSTS_DIR = ROOT / "_posts"

REQUIRED_FRONT_MATTER = ["title", "layout", "author", "published", "tags"]


def split_front_matter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, text
    fm = text[4:end]
    body = text[end + 5 :]
    return fm, body


def check_file(path: Path):
    errors = []
    text = path.read_text(encoding="utf-8")
    fm, body = split_front_matter(text)

    if fm is None:
        errors.append("missing valid front matter")
        return errors

    for key in REQUIRED_FRONT_MATTER:
        if not re.search(rf"^\s*{re.escape(key)}\s*:\s*", fm, flags=re.M):
            errors.append(f"missing front matter field: {key}")

    in_fence = False
    fence_lang = ""
    for i, line in enumerate(body.splitlines(), 1):
        if line.startswith("```"):
            if not in_fence:
                in_fence = True
                fence_lang = line[3:].strip().lower()
            else:
                in_fence = False
                fence_lang = ""
            continue

        if in_fence and fence_lang == "markdown" and re.match(r"^#{1,6}\s+", line):
            errors.append(
                f"line {i}: heading syntax in ```markdown fence may break TOC; use ```text instead"
            )

    for i, line in enumerate(body.splitlines(), 1):
        for m in re.finditer(r"!\[([^\]]*)\]\(([^)]+)\)", line):
            alt = m.group(1).strip()
            src = m.group(2).strip()
            if not alt:
                errors.append(f"line {i}: image alt text must not be empty")
            if src.startswith("/img/"):
                abs_path = ROOT / src.lstrip("/")
                if not abs_path.exists():
                    errors.append(f"line {i}: image path not found: {src}")

    return errors


def main():
    md_files = sorted(POSTS_DIR.rglob("*.md"))
    total_errors = 0
    for f in md_files:
        errs = check_file(f)
        if errs:
            print(f"\n{f.relative_to(ROOT)}")
            for e in errs:
                print(f"  - {e}")
            total_errors += len(errs)

    if total_errors:
        print(f"\nFound {total_errors} issue(s).")
        return 1

    print("All post checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())