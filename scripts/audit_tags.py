#!/usr/bin/env python3
"""临时审计脚本：统计 _posts 下所有 categories / tags 使用情况"""
import os
import re
from collections import Counter, defaultdict

POSTS_DIR = '_posts'

def parse_front_matter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    block = m.group(1)
    lines = block.split('\n')
    key = None
    for line in lines:
        km = re.match(r'^(\w[\w-]*):\s*(.*)$', line)
        if km:
            key = km.group(1)
            val = km.group(2).strip()
            if val.startswith('['):
                fm[key] = [v.strip().strip("'\"") for v in val.strip('[]').split(',') if v.strip()]
            elif val:
                fm[key] = val.strip("'\"")
            else:
                fm[key] = []
        elif re.match(r'^\s*-\s+', line) and key is not None:
            item = re.sub(r'^\s*-\s+', '', line).strip().strip("'\"")
            if isinstance(fm.get(key), list):
                fm[key].append(item)
            else:
                fm[key] = [item]
    return fm

cat_count = Counter()
tag_count = Counter()
files_by_tag = defaultdict(list)
files_by_cat = defaultdict(list)

for root, dirs, files in os.walk(POSTS_DIR):
    for fn in sorted(files):
        if not fn.endswith('.md'):
            continue
        path = os.path.join(root, fn)
        with open(path, encoding='utf-8') as f:
            fm = parse_front_matter(f.read())
        rel = os.path.relpath(path, POSTS_DIR)
        cats = fm.get('categories') or []
        tags = fm.get('tags') or []
        if isinstance(cats, str):
            cats = [cats]
        if isinstance(tags, str):
            tags = [tags]
        for c in cats:
            cat_count[c] += 1
            files_by_cat[c].append(rel)
        for t in tags:
            tag_count[t] += 1
            files_by_tag[t].append(rel)

print('== CATEGORIES ==')
for c, n in cat_count.most_common():
    print(f'{n:3d}  {c}')
print()
print('== TAGS (by count) ==')
for t, n in tag_count.most_common():
    print(f'{n:3d}  {t}')
print()
print('== TAG DETAIL (files) ==')
for t in sorted(files_by_tag):
    print(f'--- {t} ---')
    for f in files_by_tag[t]:
        print(f'    {f}')
