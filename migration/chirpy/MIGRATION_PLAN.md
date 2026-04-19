# Chirpy 迁移计划（并行迁移，不覆盖现网）

## 目标

- 在不影响当前 Hux 站点的前提下，建立 Chirpy 并行预览环境。
- 先迁移样例文章验证 TOC/Mermaid/图片渲染，再决定是否全量切换。

## 当前状态

- 分支：`feat/migrate-chirpy`
- Chirpy 骨架：`migration/chirpy/theme`

## Step 1：字段映射（Hux -> Chirpy）

| Hux 字段 | Chirpy 字段 | 处理策略 |
|---|---|---|
| `title` | `title` | 保留 |
| `subtitle` | `description`（可选） | 可转为 `description` 或并入正文导语 |
| `layout: post` | `layout: post` | 保留 |
| `author` | `author` | 保留 |
| `published` | `published` | 保留 |
| `categories` | `categories` | 保留（建议统一大小写） |
| `tags` | `tags` | 保留 |
| `toc`, `toc_sticky` | `toc`（Chirpy 已内建） | 统一为 `toc: true` |
| `header-style` | N/A | 移除 |

## Step 2：样例迁移范围（5 篇）

1. `_posts/ai/2026-04-15-Agent-Harness-Enineering.md`（长文 + Mermaid + TOC）
2. `_posts/ai/2025-02-10-transformer-detail.md`（含图片）
3. `_posts/ai/2025-02-12-paged-attention-one.md`（含图片）
4. `_posts/software/2023-11-11-torchserve-practices.md`（工程类长文）
5. `_posts/growth/2024-11-30-cursor实践总结.md`（中文排版）

## Step 3：验收标准

- Mermaid 图可渲染，且首图不报错
- TOC 层级正确（H1/H2/H3 有缩进差异）
- TOC 可折叠/展开
- 图片路径可访问（`/img/...`）
- 文章页无明显样式破碎

## Step 4：灰度与回滚

- 灰度：新主题先本地预览 1 周（只在迁移分支）
- 回滚：保留 Hux 分支不动，切换回 `feat/add_agent_harness` 即可
