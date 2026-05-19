# pack-ba — Coding Rules

Idioms cho BA writing — requirement, acceptance criteria, process map, stakeholder doc. Less strict than constraints — đây là convention.

## Requirement Format

- Cấu trúc 1 requirement: **Actor → Trigger → Action → Business Outcome** (4 element bắt buộc).
- Ưu tiên bullet ngắn (≤ 2 dòng/bullet) cho assumptions, dependencies, out-of-scope.
- 1 requirement = 1 testable outcome; chia khi gặp "and"/"or" composite.
- Tag mỗi requirement với ID stable (`R-{epic}-{nn}`) để trace xuyên acceptance/test.
- Source attribution: link interview ID / ticket / Slack thread; KHÔNG "user wants" mơ hồ.

## Acceptance Criteria Format

- Dùng **Given/When/Then** (Gherkin) hoặc **Rule-based** (data table). Chọn 1, dùng nhất quán per epic.
- Mỗi tiêu chí: 1 condition path; happy + edge + error case tách thành scenario riêng.
- Có owner xác nhận / nguồn xác minh (PM, domain expert, regulation doc).
- Testable: dev/QA đọc xong viết được test case mà không cần hỏi lại.

## Non-Functional Requirement (NFR)

- Section **NFR bắt buộc** trong mọi epic: performance (số), security (level), accessibility (WCAG level), i18n (locale list), compliance (regulation list).
- Mỗi NFR có metric đo được + verification method (load test, audit, manual check).
- KHÔNG "fast/easy/user-friendly" không kèm số.

## Persona & User Story

- Format `As a {persona}, I want {capability}, so that {business outcome}` — bắt buộc 3 element.
- Persona named + linked tới persona doc; KHÔNG generic "user".
- Permission/role được nêu rõ cho mọi capability (admin / standard / read-only / guest).

## Process Map (As-Is / To-Be)

- Swimlane theo role/actor; mỗi lane chỉ chứa step actor đó thực hiện.
- Decision point đặt tên dạng câu hỏi (`Is invoice approved?`); branch label `Yes/No` rõ.
- As-Is + To-Be cùng template để diff rõ; gap analysis section liệt kê delta + change impact.
- Notation chuẩn: BPMN 2.0 subset (event, task, gateway, sequence flow) — không free-form box.

## Stakeholder Doc

- RACI (Responsible/Accountable/Consulted/Informed) cho mọi major decision.
- DRI (single Directly Responsible Individual) named, không "team X" tập thể.
- Communication cadence: scheduled (weekly sync) vs on-demand (escalation path).
- Sign-off log: ai approve, khi nào, version nào.

## Glossary & Term Hygiene

- Mỗi epic có **Glossary** section với business term + 1-line definition + first-use link.
- Acronym expand ở first use trong mọi document.
- Term mơ hồ ("system", "user", "data") PHẢI specify trong context cụ thể.

## Versioning & Change Log

- Doc có version footer + last-modified date + author.
- Change log section: ngày, người, lý do, scope impact.
- Major version bump khi behavior thay đổi; minor cho clarification.
