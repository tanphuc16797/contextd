# pack-qc — Validator Rules

Layer-1 rule. Prefix `pack-qc-`.

| Rule ID | Severity | Check |
|---------|----------|-------|
| `pack-qc-bug-missing-repro` | error | Bug/defect doc thiếu bước tái hiện hoặc expected/actual result |
| `pack-qc-bug-missing-severity-priority` | warn | Bug/defect doc có severity mà thiếu priority (hoặc ngược lại) |
| `pack-qc-release-no-evidence` | error | Release/gate decision không có test evidence (pass/fail/coverage/trend) |
| `pack-qc-regression-vague-scope` | warn | Regression plan dùng mô tả mơ hồ (all as needed/normal regression/...) |
| `pack-qc-perf-no-baseline-metric` | error | Tài liệu optimize thiếu baseline hoặc target metric |
| `pack-qc-perf-no-measure-loop` | warn | Thiếu đo trước/sau tối ưu |
| `pack-qc-perf-premature-tuning` | warn | Có tuning đề xuất nhưng thiếu profiling/bottleneck evidence |
| `pack-qc-perf-no-regression-check` | warn | Thiếu kế hoạch regression check cho perf change |

## Layer-2 self-check

```md
### Quality Control (pack-qc)
- Defect có đủ repro + expected/actual
- Severity và priority được ghi tách biệt
- Release decision có evidence kiểm thử
- Regression scope rõ module/flow/level

### Performance Optimization (pack-qc — perf)
- Có baseline metric và target metric trước khi tối ưu
- Có đo trước/sau cho thay đổi optimize
- Tuning có profiling/bottleneck evidence
- Có regression check hoặc rollback/guardrail plan
```

## Related

- Implementation: [`scripts/rules.py`](../../scripts/rules.py)
- Engine validator pipeline: [`agents/pipeline/validator-rules.md`](../../../../agents/pipeline/validator-rules.md)
