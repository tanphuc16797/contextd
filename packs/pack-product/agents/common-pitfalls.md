# pack-product — Top 10 Common Pitfalls

Anti-pattern lặp lại với product brief / OKR / roadmap / PRD. Additive trên [constraints.md](constraints.md).

## P01 — Brief thiếu Problem / Metric / Acceptance
- **NG**: brief chỉ mô tả feature, không nêu vấn đề + cách đo thành công.
- **OK**: Problem statement → Metric (baseline + target) → Acceptance criteria.
- **Why**: build xong không biết thành/bại.
- **Detect**: Layer-1 `pack-product-brief-incomplete` (new) — md có heading `# Problem`, `# Metric`/`# Success`, `# Acceptance`.
- **Severity**: error

## P02 — OKR Key Result không measurable
- **NG**: KR "improve UX", "make faster".
- **OK**: "p95 page load < 2s by Q3"; "NPS từ 30 → 45".
- **Why**: KR không đo = OKR vô nghĩa.
- **Detect**: Layer-1 `pack-product-kr-vague` (new) — KR thiếu số + đơn vị + deadline.
- **Severity**: error

## P03 — Jargon kỹ thuật trong product doc
- **NG**: "use Redis pub/sub for event fanout".
- **OK**: nói nhu cầu user; implementation để eng chốt.
- **Why**: lock decision sai layer; stakeholder không hiểu.
- **Detect**: Layer-2 — review jargon list (Redis, Kafka, microservice, ...).
- **Severity**: warn

## P04 — Brief dictate implementation
- **NG**: "build a REST API with Postgres".
- **OK**: "expose data X để mobile sync offline" — let eng chose stack.
- **Why**: PM lockin tech mà không có context engineering.
- **Detect**: Layer-2 — review brief cho tech directive.
- **Severity**: error

## P05 — Roadmap dùng date mơ hồ
- **NG**: "soon", "Q2-ish", "TBD".
- **OK**: target month (commit) + confidence level.
- **Why**: stakeholder không plan được; trust break.
- **Detect**: Layer-1 `pack-product-vague-date` (new) — regex `soon|TBD|Q\d-ish|asap`.
- **Severity**: warn

## P06 — Persona generic ("user")
- **NG**: "user wants to ...".
- **OK**: named persona với role, context, JTBD; ít nhất 2 persona.
- **Why**: thiết kế cho ai cũng = không cho ai.
- **Detect**: Layer-2 — brief có persona section.
- **Severity**: warn

## P07 — Missing success metric baseline
- **NG**: target "increase signup", không nêu hiện tại bao nhiêu.
- **OK**: baseline (giá trị + thời điểm đo + dimension) → target.
- **Why**: không đo delta, claim arbitrary.
- **Detect**: Layer-2 — metric có cả baseline + target.
- **Severity**: error

## P08 — Thiếu non-goals
- **NG**: brief chỉ liệt kê What.
- **OK**: section "Non-goals" liệt kê 3-5 điều không làm trong scope này.
- **Why**: scope creep; stakeholder mở rộng silent.
- **Detect**: Layer-1 `pack-product-no-non-goals` (new) — md thiếu section `Non-goals|Out of scope`.
- **Severity**: warn

## P09 — Thiếu stakeholder list / RACI
- **NG**: không nêu ai approve, ai informed.
- **OK**: RACI hoặc DRI + reviewer + informed list.
- **Why**: launch chậm vì 1 stakeholder veto cuối.
- **Detect**: Layer-2 — brief có RACI/DRI.
- **Severity**: warn

## P10 — Scope creep không revisit
- **NG**: brief original 3 feature, ship 8 mà không update doc.
- **OK**: change log; revisit metric; cắt scope nếu cần.
- **Why**: history mất, retrospective vô ích.
- **Detect**: Layer-2 — brief có change log.
- **Severity**: info

## Mapping to validator

| Pitfall | Layer-1 rule ID | Layer-2 self-check |
|---|---|---|
| P01 PMA | `pack-product-brief-incomplete` (new) | ✓ |
| P02 KR | `pack-product-kr-vague` (new) | ✓ |
| P03 jargon | — | ✓ |
| P04 dictate | — | ✓ |
| P05 date | `pack-product-vague-date` (new) | ✓ |
| P06 persona | — | ✓ |
| P07 baseline | — | ✓ |
| P08 non-goals | `pack-product-no-non-goals` (new) | ✓ |
| P09 RACI | — | ✓ |
| P10 change-log | — | ✓ |
