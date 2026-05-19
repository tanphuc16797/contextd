# pack-ba — Constraints

Hard rules cho business analysis (requirement, acceptance, process, stakeholder). Additive trên engine constraints. Strict-only direction.

## Requirement Clarity

- **Requirement PHẢI mô tả outcome business, actor, và trigger** — không chấp nhận requirement chỉ mô tả solution kỹ thuật.
- **1 requirement = 1 testable outcome** — chia khi gặp "and"/"or" composite; gắn ID stable (`R-{epic}-{nn}`).
- **Requirement có impact cross-team PHẢI nêu dependency/handoff** rõ ràng + DRI per side.
- **Source attribution bắt buộc** — link interview ID / ticket / Slack thread; KHÔNG "user wants" mơ hồ.

## Acceptance Discipline

- **Acceptance criteria PHẢI measurable + testable** — tránh từ mơ hồ ("nhanh", "tốt hơn", "thân thiện") khi không có metric.
- **KHÔNG trộn assumption ngầm vào acceptance criteria** — assumption ghi rõ và reviewable trong section riêng.
- **Mỗi user story PHẢI có ≥ 3 AC** (happy + edge + error) format Gherkin/rule-based.
- **NFR section bắt buộc** trong mọi epic — perf, security, accessibility, i18n, compliance.

## Terminology Consistency

- **Business term chính (entity/process/status) PHẢI nhất quán** trong cùng tài liệu — tránh dùng nhiều tên cho cùng khái niệm.
- **Khi thay đổi nghĩa của term đã có** — phải nêu migration note cho stakeholder liên quan + version bump.
- **Acronym PHẢI expand ở first use** trong mọi document; có Glossary section per epic.

## Scope Discipline

- **Non-goals section bắt buộc** — liệt kê 3-5 điều không làm trong scope này.
- **Scope change PHẢI có change log** — ngày, người, lý do, impact metric/timeline.
- **KHÔNG silently expand scope** giữa epic — revisit AC + estimate.

## Stakeholder & Sign-off

- **RACI/DRI PHẢI documented** cho mọi major decision — single accountable owner.
- **Sign-off log bắt buộc** — ai approve, version nào, ngày nào.

## Related

- Engine baseline: [`agents/constraints.md`](../../../agents/constraints.md)
- Pack validator rules: [pipeline/validator-rules.md](pipeline/validator-rules.md)
- Pack coding rules: [coding-rules.md](coding-rules.md)

> Anti-patterns lặp lại trong domain này: xem [common-pitfalls.md](common-pitfalls.md) (Top 10 với rule/why/detect/severity).
