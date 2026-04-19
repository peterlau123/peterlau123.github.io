#!/usr/bin/env python3
from pathlib import Path
import shutil
import yaml

ROOT = Path('/Users/liuxin/workspace/GitHub/peterlau123.github.io')
POSTS = ROOT / '_posts'
BACKUP = ROOT / 'migration' / 'chirpy' / 'backup_posts'


def split_fm(text: str):
    if not text.startswith('---\n'):
        return None, text
    end = text.find('\n---\n', 4)
    if end == -1:
        return None, text
    return text[4:end], text[end+5:]


def normalize(fm: dict):
    out = dict(fm)
    if out.get('subtitle') and not out.get('description'):
        out['description'] = out.get('subtitle')
    out.pop('header-style', None)
    out.pop('toc_sticky', None)
    out['toc'] = True
    out.setdefault('layout', 'post')
    return out


def main():
    if BACKUP.exists():
        shutil.rmtree(BACKUP)
    shutil.copytree(POSTS, BACKUP)

    changed = 0
    total = 0
    for p in POSTS.rglob('*.md'):
        total += 1
        text = p.read_text(encoding='utf-8')
        fm_text, body = split_fm(text)
        if fm_text is None:
            continue
        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception:
            continue
        new_fm = normalize(fm)
        old_dump = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
        new_dump = yaml.safe_dump(new_fm, allow_unicode=True, sort_keys=False).strip()
        if old_dump != new_dump:
            p.write_text(f"---\n{new_dump}\n---\n\n{body}", encoding='utf-8')
            changed += 1
            print('updated', p.relative_to(ROOT))

    print(f'finished: total={total}, changed={changed}')
    print(f'backup: {BACKUP.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
