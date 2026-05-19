# pack-event-driven — Top 10 Common Pitfalls

Anti-pattern lặp lại với Kafka/MQTT/broker. Additive trên [constraints.md](constraints.md).

## P01 — Commit offset trước khi process
- **NG**: `consumer.commitSync()` rồi mới gọi `process(msg)`.
- **OK**: process xong (idempotent) → commit. Crash giữa chừng → reprocess.
- **Why**: data loss khi worker crash sau commit.
- **Detect**: Layer-1 `pack-event-driven-commit-before-process` (new).
- **Severity**: error

## P02 — Thiếu DLQ / retry strategy
- **NG**: lỗi parse → log + skip, hoặc retry vô hạn block partition.
- **OK**: bounded retry (exponential) → DLQ topic; alert khi DLQ tăng.
- **Why**: 1 poison message dừng cả partition; mất visibility.
- **Detect**: Layer-2 — consumer có DLQ producer + max-retries config.
- **Severity**: error

## P03 — Hardcoded topic name
- **NG**: `consume("orders.created.v1")`.
- **OK**: topic name từ config; helper `topicFor(domain, event, version)`.
- **Why**: rename topic = redeploy toàn cluster; lỗi typo silent.
- **Detect**: Layer-1 `pack-event-driven-hardcoded-topic` (new).
- **Severity**: warn

## P04 — Inline MQTT topic string
- **NG**: `client.publish("topic/" + region + "/" + gw + "/up/temp", ...)`.
- **OK**: `buildTopic({region, gatewayId, direction: 'up', type})` per contract.
- **Why**: drift khỏi contract; refactor format = grep toàn repo.
- **Detect**: Layer-1 regex `"topic/"\s*\+`.
- **Severity**: warn

## P05 — Per-message loop khi batch mode
- **NG**: `for msg in poll()` xử lý từng cái + commit từng cái.
- **OK**: process batch atomically, 1 commit cuối.
- **Why**: throughput thấp 10–100x; commit overhead.
- **Detect**: Layer-2 — consumer config batch nhưng code loop single.
- **Severity**: warn

## P06 — Thiếu dedup khi at-least-once
- **NG**: producer retry → consumer xử lý 2 lần → duplicate order.
- **OK**: idempotency key (eventId) + dedup store / upsert.
- **Why**: at-least-once là default Kafka semantics.
- **Detect**: Layer-2 — handler có check `seenEventIds`.
- **Severity**: error

## P07 — Ordering assumption khi partition > 1
- **NG**: code giả định msg đến đúng thứ tự global.
- **OK**: partition key = entity ID; ordering chỉ trong cùng partition.
- **Why**: out-of-order race condition.
- **Detect**: Layer-2 — review partition key strategy doc.
- **Severity**: error

## P08 — Thiếu schema versioning
- **NG**: payload đổi field, không version → consumer cũ crash.
- **OK**: schema registry / version trong payload (`schemaVersion: 2`); backward compat.
- **Why**: rolling deploy break; consumer lag spike.
- **Detect**: Layer-2 — contract doc có schema version field.
- **Severity**: error

## P09 — Swallow deserialize error
- **NG**: `try { parse(msg) } catch { return }` — message biến mất.
- **OK**: parse fail → DLQ với raw bytes + error.
- **Why**: poison message disappears, không debug được.
- **Detect**: Layer-2 — deser error path đến DLQ.
- **Severity**: error

## P10 — Không propagate correlationId
- **NG**: log `"processed msg"` không kèm event ID, trace ID.
- **OK**: trace context (W3C) trong header; log `correlationId`.
- **Why**: không trace được flow xuyên service.
- **Detect**: Layer-2 — handler log có trace ID.
- **Severity**: warn

## Mapping to validator

| Pitfall | Layer-1 rule ID | Layer-2 self-check |
|---|---|---|
| P01 commit-before | `pack-event-driven-commit-before-process` (new) | ✓ |
| P02 DLQ | — (design) | ✓ |
| P03 hardcoded-topic | `pack-event-driven-hardcoded-topic` (new) | ✓ |
| P04 inline-topic | `pack-event-driven-inline-mqtt-topic` (new) | ✓ |
| P05 per-msg loop | — | ✓ |
| P06 dedup | — | ✓ |
| P07 ordering | — | ✓ |
| P08 schema-ver | — | ✓ |
| P09 swallow-deser | — | ✓ |
| P10 correlation | — | ✓ |
