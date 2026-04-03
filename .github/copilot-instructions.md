# GitHub Copilot Instructions — timeline-website

## Git Workflow

- **Never push feature branches to remote.** All feature/topic branches (e.g. `add-events-*`, `legal-*`) are local only.
- Merge completed branches into `master` locally, then push only `master` to `origin`.
- Infrastructure commits (GitHub Actions, config fixes) may go directly to `master`.
- Delete feature branches after merging: `git branch -d <branch>`.

## Branch Naming

- `add-events-YYYYMMDD` — timeline event additions
- `legal-*` — licensing and legal hardening work
- Always branch from `master` with `git checkout -b <name>`.

## Jekyll

- Run `bundle exec jekyll serve` to preview locally at http://127.0.0.1:4000/
- The `docs/`, `.venv/`, and `vendor/` directories are excluded from Jekyll builds (see `_config.yml`).
- Do not add front matter to files in `docs/` — they are working notes, not Jekyll pages.

## File Structure

- `index.html` — English timeline (primary)
- `timeline_ko.html`, `timeline_ja.html`, `timeline_zh_cn.html`, `timeline_zh_tw.html`, `timeline_vi.html` — translated timelines
- `blog_posts/<lang>/` — local blog post HTML files (en, ko, ja, zh_ch, zh_tw, vi)
- `_includes/` — shared partials (support_section.html, resources_section.html, footer.html)
- `_data/ui_text.yml` — multilingual UI strings
- `docs/` — working notes and drafts only, not served by Jekyll

## Timeline Event Cards

- New events link externally to `blog.genderwatchdog.org` unless a local HTML file exists in `blog_posts/en/`.
- Card HTML pattern: `col-xl-3 col-lg-4 col-md-6 col-12 mb-4` outer div, `data-link` on the `timeline-event` div, tooltip with description + "Read the full report:" link list.
- English-only cards use a single `<li>` link; multi-language cards list all available languages.
- When adding events, insert in strict chronological order.

## Translations

- After updating `index.html`, mirror all new events into all 5 language files.
- Date format per language: `ko` → `2025년 5월 24일`, `ja` → `2025年5月24日`, `zh_cn`/`zh_tw` → `2025年5月24日`, `vi` → `Ngày 24 tháng 5, 2025`.
- Tooltip help text per language: `ko` → `(위 링크를 클릭하여 전체 텍스트 읽기)`, `ja` → `(上記リンクをクリックして全文を読む)`, `zh_cn` → `(点击上方链接阅读全文)`, `zh_tw` → `(點擊上方連結閱讀全文)`, `vi` → `(Nhấp vào liên kết trên để đọc toàn văn)`.
