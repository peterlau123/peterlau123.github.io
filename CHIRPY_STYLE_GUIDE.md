# Chirpy风格博客使用指南

## 概述

本项目已成功添加Chirpy风格的简洁布局，特点包括：
- 左侧固定边栏导航
- 简洁的卡片式首页
- 时间线式归档页面
- 优化的文章详情页
- 完整的响应式设计

## 文件结构

### 新增的布局文件
```
_layouts/
  ├── chirpy-default.html    # Chirpy风格基础布局
  ├── chirpy-page.html       # 页面布局（About等）
  └── chirpy-post.html       # 文章详情页布局

_includes/
  ├── chirpy-sidebar.html    # 左侧边栏组件
  └── chirpy-topbar.html     # 顶部面包屑+搜索栏

less/
  └── left-sidebar.less      # 左侧边栏样式

根目录/
  ├── index-chirpy.html      # Chirpy风格首页
  └── archive-chirpy.html    # 时间线式归档页
```

## 使用方法

### 1. 使用Chirpy风格首页

**方式A：直接替换（推荐）**
```bash
# 备份原首页
mv index.html index-old.html

# 使用Chirpy首页
mv index-chirpy.html index.html
```

**方式B：渐进测试**
- 访问 `yoursite.com/index-chirpy.html` 查看效果
- 满意后再执行方式A

### 2. 使用Chirpy风格归档页

替换原有的archive.html：
```bash
# 备份
mv archive.html archive-old.html

# 使用新归档页
mv archive-chirpy.html archive.html
```

### 3. 为文章应用Chirpy布局

在文章的Front Matter中指定layout：

```yaml
---
layout: chirpy-post
title: 你的文章标题
subtitle: 文章副标题（可选）
date: 2025-01-27
author: Peter Lau
update_date: 2025-01-28  # 更新日期（可选）
tags: [tag1, tag2, tag3]
---
```

### 4. 为页面应用Chirpy布局

对于About等页面，使用chirpy-page布局：

```yaml
---
layout: chirpy-page
title: About
description: 关于我
---
```

## 核心特性

### 1. 左侧固定边栏
- **品牌区域**：显示头像、站点名称和标语
- **导航菜单**：HOME, ARCHIVES, ABOUT等
- **SNS链接**：GitHub, Zhihu, Twitter等社交媒体图标
- **响应式**：移动端自动隐藏，点击按钮展开

### 2. 面包屑导航
- 位于页面顶部
- 格式：Home › 当前页面
- 清晰展示页面层级

### 3. 卡片式首页
- 每篇文章独立卡片
- 显示标题、副标题、摘要
- 底部显示发布日期、作者、标签
- 悬停效果增强交互性

### 4. 时间线归档
- 按年份分组
- 垂直时间线设计
- 每篇文章显示月份、日期
- 带标签显示

### 5. 文章详情页增强
- **元数据**：发布时间、作者、更新时间、阅读时长
- **标签链接**：点击跳转到相关标签页
- **版权声明**：页脚显示版权信息
- **文章导航**：上一篇/下一篇快速跳转

### 6. 阅读时间估算
自动计算文章阅读时间（基于字数）：
- 中文：180字/分钟
- 英文：360词/分钟

## 样式配色

### 主色调
```less
@sidebar-bg: #f8f9fa;          // 侧边栏背景
@sidebar-link-color: #404040;   // 链接颜色
@sidebar-link-hover: #0085a1;   // 链接悬停色
@sidebar-active-bg: #e9ecef;    // 激活背景
```

### 自定义配色
修改 `less/left-sidebar.less` 中的变量即可：

```less
// 示例：改为深色主题
@sidebar-bg: #1a1a1a;
@sidebar-text-color: #ffffff;
@sidebar-link-hover: #00bcd4;
```

## 响应式断点

```css
/* 移动端 */
@media (max-width: 768px) {
  /* 侧边栏隐藏，点击按钮展开 */
}

/* 平板 */
@media (min-width: 769px) and (max-width: 1024px) {
  /* 侧边栏220px宽度 */
}

/* 桌面 */
@media (min-width: 1025px) {
  /* 侧边栏260px宽度 */
}
```

## 编译CSS

本项目使用LESS预处理器，修改样式后需要编译：

```bash
# 方法1：使用npm script
npm run dev

# 方法2：使用grunt
npx grunt less

# 方法3：监听模式（自动编译）
npx grunt watch
```

## 兼容性说明

### 保持原有功能
- ✅ 原有的搜索功能完全保留
- ✅ MathJax数学公式支持
- ✅ Mermaid图表支持
- ✅ 代码高亮
- ✅ 评论系统（Disqus）
- ✅ 多语言支持

### 新旧布局共存
- 原有布局文件未被修改
- 可以在文章中灵活选择使用哪种布局
- 新旧布局可以共存，实现渐进式迁移

## 迁移步骤建议

### 阶段1：测试阶段（当前）
1. 访问 `/index-chirpy.html` 查看首页效果
2. 访问 `/archive-chirpy.html` 查看归档页效果
3. 选择1-2篇文章改为 `layout: chirpy-post` 测试

### 阶段2：部分迁移
1. 将新文章使用chirpy-post布局
2. 保持旧文章使用原有布局
3. 收集用户反馈

### 阶段3：全面迁移
1. 替换首页：`index-chirpy.html` → `index.html`
2. 替换归档：`archive-chirpy.html` → `archive.html`
3. 批量修改所有文章layout
4. 更新About等页面为chirpy-page

## 自定义指南

### 修改侧边栏内容
编辑 `_includes/chirpy-sidebar.html`：

```html
<!-- 修改LOGO -->
<img src="{{ site.baseurl }}/img/your-logo.jpg">

<!-- 添加新的导航项 -->
<li>
    <a href="/projects.html">PROJECTS</a>
</li>

<!-- 修改SNS链接 -->
<a href="https://linkedin.com/in/yourprofile">
    <i class="fa fa-linkedin"></i>
</a>
```

### 调整内容宽度
修改 `less/left-sidebar.less`：

```less
@sidebar-width: 260px;  // 改为你想要的宽度

.content-wrapper {
    max-width: 1000px;  // 改为你想要的内容宽度
}
```

### 自定义卡片样式
修改 `index-chirpy.html` 中的 `<style>` 部分：

```css
.post-card {
    border-radius: 8px;     /* 圆角 */
    padding: 30px;          /* 内边距 */
    box-shadow: ...;        /* 阴影 */
}
```

## 故障排查

### 问题1：样式不生效
**解决方案**：
```bash
# 重新编译LESS
npx grunt less

# 清除浏览器缓存
Ctrl + Shift + R (Windows/Linux)
Cmd + Shift + R (Mac)
```

### 问题2：移动端侧边栏无法展开
**检查**：
- 确保jQuery已加载
- 检查浏览器console是否有JS错误

### 问题3：面包屑导航不显示
**检查**：
- 确保page.title已设置
- 检查_includes/chirpy-topbar.html是否正确引入

## 最佳实践

### 1. Front Matter规范
```yaml
---
layout: chirpy-post
title: "文章标题"
subtitle: "副标题（可选但推荐）"
date: 2025-01-27 10:00:00
author: Peter Lau
update_date: 2025-01-28 15:00:00  # 更新时添加
tags: [AI, Python, 教程]          # 3-5个标签
---
```

### 2. 图片使用
```markdown
![图片描述](/img/path/to/image.jpg)

<!-- 推荐使用相对路径 -->
![示例](/img/example.jpg)
```

### 3. 代码块
````markdown
```python
def hello_world():
    print("Hello, World!")
```
````

## 进一步优化建议

### 短期（已完成）
- ✅ 左侧边栏布局
- ✅ 卡片式首页
- ✅ 时间线归档
- ✅ 文章详情页优化
- ✅ 阅读时间估算

### 中期（待实现）
- [ ] 标签云页面优化
- [ ] 添加目录（TOC）功能
- [ ] 代码块复制按钮
- [ ] 图片灯箱效果
- [ ] 深色模式支持

### 长期（计划中）
- [ ] 全文搜索增强
- [ ] 文章推荐系统
- [ ] 阅读进度条
- [ ] 文章统计（字数、浏览量）
- [ ] 评论系统升级

## 技术支持

如有问题或建议：
1. 查看 `REFACTOR_PLAN.md` 了解重构计划
2. 参考 `Chirpy博客样式和结构分析报告.md` 了解设计理念
3. 提交Issue到GitHub仓库

---

**最后更新**: 2026年1月27日
**版本**: v1.0.0
**作者**: Peter Lau
