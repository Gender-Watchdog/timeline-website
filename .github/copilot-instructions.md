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
- **Always use `index.html` (English) as the sole source** when translating timeline cards. Never translate from another translated file.
- Current translation branch: `translation-20260410`

### Date Formats

| Language | Format example |
|----------|---------------|
| `ko` | `2025년 5월 24일` |
| `ja` | `2025年5月24日` |
| `zh_cn` / `zh_tw` | `2025年5月24日` |
| `vi` | `Ngày 24 tháng 5, 2025` |

### Tooltip Strings Per Language

| Field | `ko` | `ja` | `zh_cn` | `zh_tw` | `vi` |
|-------|------|------|---------|---------|------|
| Help text | `(위 링크를 클릭하여 전체 텍스트 읽기)` | `（全文を読むには上記のリンクをクリックしてください）` | `(点击上方链接阅读全文)` | `(點擊上方連結閱讀全文)` | `(Nhấp vào liên kết trên để đọc toàn văn)` |
| "Read the full report:" | `전체 보고서 읽기:` | `レポート全文を読む：` | `阅读完整报告：` | `閱讀完整報告：` | `Đọc báo cáo đầy đủ:` |
| "Available in:" | `다음 언어로 제공:` | `以下の言語で提供:` | `提供语言：` | `提供語言：` | `Có sẵn bằng:` |
| No links note | `(이 이벤트에는 문서 링크가 없습니다)` | `（このイベントにはドキュメントリンクがありません）` | `(此事件无文档链接)` | `(此事件無文件連結)` | `(Không có liên kết tài liệu cho sự kiện này)` |

### Translated Blog Posts Available at blog.genderwatchdog.org

These external posts have confirmed translated URLs — use them in tooltips instead of the English URL when writing a language-specific timeline card.

#### Post: Panic Scrub (Jan 19, 2026)
- EN: `https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names/`
- KO: `https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names-ko/`
- JA: `https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names-ja/`
- VI: `https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names-vi/`
- ZH-CN: `https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/panic-scrub-dongguk-deletes-ubc-reverts-to-dead-names-zh-tw/`

#### Post: Japanese Studies Professor / 2nd Department (Jan 28 & Mar 23–24, 2026)
- EN: `https://blog.genderwatchdog.org/dongguk-japanese-studies-professor-sexual-violence-second-department-2026/`
- JA: `https://blog.genderwatchdog.org/dongguk-japanese-studies-professor-sexual-violence-second-department-2026-ja/`
- ZH-CN: `https://blog.genderwatchdog.org/dongguk-japanese-studies-professor-sexual-violence-second-department-2026-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/dongguk-japanese-studies-professor-sexual-violence-second-department-2026-zh-tw/`
- KO: `https://blog.genderwatchdog.org/dongguk-japanese-studies-professor-sexual-violence-second-department-2026-ko/`
- VI: `https://blog.genderwatchdog.org/dongguk-japanese-studies-professor-sexual-violence-second-department-2026-vi/`

#### Post: Film Faculty Purge / EU Cleanup (Apr 1, 2026)
- EN: `https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026/`
- ZH-CN: `https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026-zh-tw/`
- JA: `https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026-ja/`
- KO: `https://blog.genderwatchdog.org/dongguk-faculty-purge-paper-faculty-eu-cleanup-april-2026-ko/`
- VI: (not yet translated)

#### Post: Netflix / K-Pop Exploitation
- EN: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library/`
- KO: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library-ko/`
- JA: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library-ja/`
- VI: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library-vi/`
- ZH-CN: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library-zh-tw/`
- ES: `https://blog.genderwatchdog.org/netflix-knew-kpop-exploitation-documentary-library-es/`

#### Post: SNU Goes Dark
- EN: `https://blog.genderwatchdog.org/the-harvard-of-korea-has-pulled-the-plug-snu-goes-dark/`
- KO: `https://blog.genderwatchdog.org/the-harvard-of-korea-has-pulled-the-plug-snu-goes-dark-ko/`
- JA: `https://blog.genderwatchdog.org/the-harvard-of-korea-has-pulled-the-plug-snu-goes-dark-ja/`
- VI: `https://blog.genderwatchdog.org/the-harvard-of-korea-has-pulled-the-plug-snu-goes-dark-vi/`
- ZH-CN: `https://blog.genderwatchdog.org/the-harvard-of-korea-has-pulled-the-plug-snu-goes-dark-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/the-harvard-of-korea-has-pulled-the-plug-snu-goes-dark-zh-tw/`

#### Post: Unclean Hands / Vietnam / NATO
- EN: `https://blog.genderwatchdog.org/unclean-hands-why-korea-must-acknowledge-vietnam-before-arming-ukraine-through-nato/`
- VI: `https://blog.genderwatchdog.org/unclean-hands-why-korea-must-acknowledge-vietnam-before-arming-ukraine-through-nato-vi/`
- ZH-CN: `https://blog.genderwatchdog.org/unclean-hands-why-korea-must-acknowledge-vietnam-before-arming-ukraine-through-nato-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/unclean-hands-why-korea-must-acknowledge-vietnam-before-arming-ukraine-through-nato-zh-tw/`
- JA: `https://blog.genderwatchdog.org/unclean-hands-why-korea-must-acknowledge-vietnam-before-arming-ukraine-through-nato-ja/`
- KO: `https://blog.genderwatchdog.org/unclean-hands-why-korea-must-acknowledge-vietnam-before-arming-ukraine-through-nato-ko/`

#### Post: Cannes Jury
- EN: `https://blog.genderwatchdog.org/cannes-gave-its-jury-to-a-director-whose-industry-criminalizes-survivors/`
- JA: `https://blog.genderwatchdog.org/cannes-gave-its-jury-to-a-director-whose-industry-criminalizes-survivors-ja/`
- KO: `https://blog.genderwatchdog.org/cannes-gave-its-jury-to-a-director-whose-industry-criminalizes-survivors-ko/`
- ZH-CN: `https://blog.genderwatchdog.org/cannes-gave-its-jury-to-a-director-whose-industry-criminalizes-survivors-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/cannes-gave-its-jury-to-a-director-whose-industry-criminalizes-survivors-zh-tw/`
- VI: `https://blog.genderwatchdog.org/cannes-gave-its-jury-to-a-director-whose-industry-criminalizes-survivors-vi/`

#### Post: Nine Universities, Zero Rebuttals
- EN: `https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud/`
- KO: `https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud-ko/`
- JA: `https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud-ja/`
- VI: `https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud-vi/`
- ZH-CN: `https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/nine-universities-zero-rebuttals-korea-partnership-fraud-zh-tw/`

#### Post: THE Rankings — Three Sentences (Tu Anh)
- EN: `https://blog.genderwatchdog.org/the-ranking-body-defers-to-moe-prestige-loop-confirmed/`
- VI: `https://blog.genderwatchdog.org/the-ranking-body-defers-to-moe-prestige-loop-confirmed-vi/`
- KO: `https://blog.genderwatchdog.org/the-ranking-body-defers-to-moe-prestige-loop-confirmed-ko/`
- ZH-CN: `https://blog.genderwatchdog.org/the-ranking-body-defers-to-moe-prestige-loop-confirmed-zh-cn/`
- ZH-TW: `https://blog.genderwatchdog.org/the-ranking-body-defers-to-moe-prestige-loop-confirmed-zh-tw/`
- JA: (not yet translated)

### Posts with English-Only Links (no translations on blog.genderwatchdog.org)

These cards exist in `index.html` but their linked blog posts have not been translated. Use English URL and label the link "English" only:

- Tcha Seung-jai / Ghost Dean: `https://blog.genderwatchdog.org/from-indictment-to-deans-office-how-dongguk-university-rewarded-a-criminal-conviction-with-promotions/`
- Xiaohongshu Viral (May 24, 2025): `https://blog.genderwatchdog.org/viral-xiaohongshu-post-exposes-dongguk-university-sexual-violence-crisis-victims-break-their-silence/`
- Sidus Legal Threat (May 27, 2025): `https://blog.genderwatchdog.org/sidus-legal-threat-backfires-evidence-of-corporate-panic-and-institutional-cover-up-at-dongguk-university/`
- DC Inside Censorship (Jul 6, 2025): `https://blog.genderwatchdog.org/korean-government-systematic-censorship-of-lgbt-military-content-evidence-of-institutional-suppression/`
- Visual Ping Tokenism (Jul 24, 2025): `https://blog.genderwatchdog.org/visual-ping-catches-dongguk-university-in-real-time-tokenism-the-loyal-insider-strategy-exposed/`
- 34 Fake Partners / Semantic Fraud (Dec 31, 2025): `https://blog.genderwatchdog.org/semantic-fraud-how-dongguk-universitys-global-network-collapsed-34-fake-partners-exposed/`
- Hollow GEP (Mar 18, 2026): `https://blog.genderwatchdog.org/gep-theatre-dongguk-chung-ang-horizon-europe-unguarded-gate/`

## Python / Conda Environment

- Always use the `dw-env` conda environment for Python operations.
- `conda run -n dw-env python <script_name>` or activate first with `conda activate dw-env`.
- Install packages with `conda install -n dw-env <pkg>` or pip inside the activated env.
