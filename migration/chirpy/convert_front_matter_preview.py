#!/usr/bin/env python3
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "migration" / "chirpy" / "converted_posts"

SAMPLES = [
    ROOT / "_posts/ai/2026-04-15-Agent-Harness-Enineering.md",
    ROOT / "_posts/ai/2025-02-10-transformer-detail.md",
    ROOT / "_posts/ai/2025-02-12-paged-attention-one.md",
    ROOT / "_posts/software/2023-11-11-torchserve-practices.md",
    ROOT / "_posts/growth/2024-11-30-cursor实践总结.md",
]


def split_fm(text: str):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_text = text[4:end]
    body = text[end + 5 :]
    return yaml.safe_load(fm_text) or {}, body


def normalize(fm: dict):
    out = dict(fm)
    if "subtitle" in out and out.get("subtitle"):
        out.setdefault("description", out.get("subtitle"))
    out.pop("header-style", None)
    out.pop("toc_sticky", None)
    out["toc"] = True
    if "layout" not in out:
        out["layout"] = "post"
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for src in SAMPLES:
        text = src.read_text(encoding="utf-8")
        fm, body = split_fm(text)
        fm2 = normalize(fm)
        dump = yaml.safe_dump(fm2, allow_unicode=True, sort_keys=False).strip()
        out_text = f"---\n{dump}\n---\n\n{body}"
        dst = OUT / src.name
        dst.write_text(out_text, encoding="utf-8")
        print(f"preview generated: {dst.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
