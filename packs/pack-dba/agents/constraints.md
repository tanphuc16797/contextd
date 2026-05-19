# pack-dba — Constraints

Hard rules cho database administration (schema/query/backup/operational). Additive trên engine constraints. Strict-only direction.

## Schema Change

- **Mọi thay đổi schema PHẢI có rollback plan hoặc forward-fix strategy rõ ràng** — không chấp nhận "deploy rồi xử lý sau".
- **Migration PHẢI immutable + versioned** — dùng migration tool (Flyway/Alembic/Prisma); KHÔNG edit migration đã merge.
- **DDL có khả năng lock lớn PHẢI nêu maintenance strategy** + impact scope (rows affected, lock duration estimate). Online schema change (gh-ost/pt-osc) cho table > 1M rows.
- **Foreign key PHẢI có index trên child column** (MySQL không auto-index như Postgres) — declare cùng FK.

## Query & Index

- **Query tuning recommendation PHẢI dựa trên evidence** — EXPLAIN plan, p95 latency, slow log entry. KHÔNG tối ưu cảm tính.
- **Index proposal PHẢI nêu trade-off** — read benefit vs write cost vs storage; verify by EXPLAIN before/after.
- **KHÔNG `SELECT *` trong application query** — list column explicitly. Migration/admin script được miễn.
- **Transaction PHẢI ngắn + chỉ bao DB ops** — KHÔNG gọi HTTP / external service / sleep trong open transaction.

## Backup & DR

- **Backup policy PHẢI nêu RPO + RTO** với số cụ thể; KHÔNG "best effort".
- **Backup PHẢI có restore verification định kỳ** (monthly drill tối thiểu) — backup không verify = không có backup.
- **Cross-region/offsite copy PHẢI có** cho production data; air-gapped backup cho ransomware protection.

## Operational

- **Slow query log PHẢI bật + alert threshold** ở production; weekly review top-N query.
- **Connection pool size PHẢI từ config**, không hardcode; alert khi saturation > 80%.
- **Incident DB PHẢI nêu blast radius** + recovery checkpoints + data-loss estimate.

## Knowledge

- **KHÔNG đoán schema** — đọc actual `\d table` / migration history; rebase wiki nếu drift.
- **KHÔNG copy query pattern từ workspace khác** — local data shape có thể khác.

## Related

- Engine baseline: [`agents/constraints.md`](../../../agents/constraints.md)
- Pack validator rules: [pipeline/validator-rules.md](pipeline/validator-rules.md)
- Pack coding rules: [coding-rules.md](coding-rules.md)

> Anti-patterns lặp lại trong domain này: xem [common-pitfalls.md](common-pitfalls.md) (Top 10 với rule/why/detect/severity).
