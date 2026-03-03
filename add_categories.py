#!/usr/bin/env python3
import os
import re

category_map = {
    'ai': 'AI',
    'essay': 'Essay', 
    'growth': 'Growth',
    'software': 'Software',
    'wemedia': 'Wemedia'
}

posts_dir = '_posts'
count = 0

for category in os.listdir(posts_dir):
    category_path = os.path.join(posts_dir, category)
    if os.path.isdir(category_path):
        for root, dirs, files in os.walk(category_path):
            for filename in files:
                if filename.endswith('.md') and filename != 'post_template.md':
                    filepath = os.path.join(root, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if not re.search(r'^categories:', content, re.MULTILINE):
                        cat_name = category_map.get(category, category.capitalize())
                        new_content = re.sub(
                            r'^(tags:)',
                            r'categories:\n  - ' + cat_name + r'\n\1',
                            content,
                            flags=re.MULTILINE
                        )
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f'Added {cat_name} to: {filepath}')
                        count += 1

print(f'\nTotal: {count} files updated')
