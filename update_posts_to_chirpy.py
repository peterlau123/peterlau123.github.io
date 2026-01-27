#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量更新文章的Front Matter为Chirpy风格
- 将layout从post改为chirpy-post
- 检查内容完整性，如果完整则设置published为true
"""

import os
import re
from pathlib import Path

def check_content_complete(content):
    """检查文章内容是否完整"""
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    article_content = parts[2].strip()
    
    # 基本完整性检查
    if len(article_content) < 200:
        return False
    
    # 检查是否有TODO标记
    if 'TODO' in article_content or 'todo' in article_content:
        return False
    
    # 检查是否有未完成标记
    if '待补充' in article_content or '未完成' in article_content:
        return False
    
    return True

def update_front_matter(file_path):
    """更新单个文件的Front Matter"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print(f"⚠️  {file_path}: 没有Front Matter，跳过")
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"⚠️  {file_path}: Front Matter格式错误，跳过")
            return False
        
        front_matter = parts[1]
        article_content = parts[2]
        
        # 检查内容完整性
        is_complete = check_content_complete(content)
        
        changed = False
        
        # 更新layout: post -> chirpy-post
        if re.search(r'^layout:\s*post\s*$', front_matter, re.MULTILINE):
            front_matter = re.sub(
                r'^layout:\s*post\s*$',
                'layout: chirpy-post',
                front_matter,
                flags=re.MULTILINE
            )
            changed = True
        
        # 更新或添加published字段
        if is_complete:
            if re.search(r'^published:', front_matter, re.MULTILINE):
                if not re.search(r'^published:\s*true\s*$', front_matter, re.MULTILINE):
                    front_matter = re.sub(
                        r'^published:\s*\w+\s*$',
                        'published: true',
                        front_matter,
                        flags=re.MULTILINE
                    )
                    changed = True
            else:
                # 在layout后面添加published字段
                if 'layout:' in front_matter:
                    front_matter = re.sub(
                        r'(^layout:.*$)',
                        r'\1\npublished: true',
                        front_matter,
                        flags=re.MULTILINE
                    )
                    changed = True
        
        if changed:
            new_content = f"---{front_matter}---{article_content}"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            status = "✅ 完整" if is_complete else "⚠️  可能未完成"
            print(f"{status} - 已更新: {file_path}")
            return True
        else:
            print(f"ℹ️  无需更新: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 错误 {file_path}: {e}")
        return False

def main():
    """主函数"""
    posts_dir = Path('_posts')
    
    if not posts_dir.exists():
        print("❌ _posts目录不存在！")
        return
    
    # 获取所有.md文件（排除模板）
    md_files = []
    for root, dirs, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md') and file != 'post_template.md':
                md_files.append(os.path.join(root, file))
    
    print(f"\n📚 找到 {len(md_files)} 篇文章\n")
    print("=" * 80)
    
    updated_count = 0
    complete_count = 0
    
    for file_path in sorted(md_files):
        if update_front_matter(file_path):
            updated_count += 1
            # 检查是否完整
            with open(file_path, 'r', encoding='utf-8') as f:
                if check_content_complete(f.read()):
                    complete_count += 1
    
    print("=" * 80)
    print(f"\n✨ 完成！")
    print(f"   - 共更新了 {updated_count} 篇文章")
    print(f"   - 其中 {complete_count} 篇内容完整，已设置 published: true\n")

if __name__ == '__main__':
    main()
