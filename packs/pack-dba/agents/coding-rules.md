# pack-dba — Coding Rules

Idioms + preferred patterns cho DBA work. Less strict than constraints — đây là convention, không phải gate.

## Migration Authoring

- Trình bày migration theo thứ tự: **precheck → change → validation → rollback**. Mỗi step là 1 SQL block riêng.
- Precheck: idempotent assertion (`IF NOT EXISTS`, row count check) — re-run an toàn.
- Đặt tên migration: `{timestamp}_{verb}_{object}.sql` (vd `20260518T093000_add_idx_orders_user_id.sql`).
- 1 migration = 1 logical change; KHÔNG bundle nhiều object change vào 1 file.
- Comment trên top file: ticket link, expected duration, lock impact, rollback notes.

## Query Recommendation Format

- Mọi đề xuất index/query nêu **expected trade-off** (read latency / write throughput / storage / cache impact).
- Kèm EXPLAIN plan before/after (hoặc dự kiến nếu chưa chạy được).
- Latency claim PHẢI nêu percentile + sample size + workload condition.
- Recommendation PHẢI link tới slow log entry / dashboard panel cụ thể.

## Index Strategy

- Composite index: prefix order = highest selectivity first; verify trên thực tế query pattern.
- Partial index khi WHERE clause cố định (Postgres) — giảm size đáng kể.
- Covering index khi query là index-only scan candidate.
- KHÔNG để index "phòng hờ" — mỗi index có cost trên write path.

## Schema Idioms

- ID: `BIGINT` (hoặc `UUID v7` nếu distributed) — KHÔNG `INT` cho table có thể vượt 2B rows.
- Timestamp: `TIMESTAMPTZ` (Postgres) / `DATETIME(6)` (MySQL); ghi tên `created_at`, `updated_at`, `deleted_at`.
- Soft delete: `deleted_at NULL` thay vì `is_deleted` boolean.
- Enum: lookup table có FK, KHÔNG `ENUM` type (khó migrate).
- JSON column: chỉ dùng cho schema-less data thực sự; có index GIN/expression khi cần query.

## Backup & Restore Doc

- Doc backup PHẢI nêu: tool, schedule, retention, storage location, encryption, RPO/RTO.
- Restore runbook: step-by-step + estimated time + dependencies + verification query.
- Drill log: lưu kết quả monthly drill (date, duration, issues found).

## Incident DB

- Với incident DB, luôn nêu **blast radius** (table/row count affected) và **recovery checkpoints**.
- Cung cấp 2 path: full-restore (RPO/RTO baseline) vs partial-restore (selective).
- Postmortem: include slow query / lock graph evidence khi root cause là perf-related.
