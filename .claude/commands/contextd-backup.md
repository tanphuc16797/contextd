# /contextd-backup — Backup Workspace

Tạo bản sao lưu local cho dữ liệu Wiki trong `~/.claude/` trước khi upgrade.

## CHECKPOINT 0 — Pre-check

Xác nhận tồn tại thư mục `~/.claude/`.
Nếu không tồn tại: dừng và báo rõ không có dữ liệu để backup.

## CHECKPOINT 1 — Scope backup (in trước khi chạy)

In danh sách sẽ backup nếu tồn tại:
- `~/.claude/wiki-global.json`
- `~/.claude/wiki-install-meta.json`
- `~/.claude/commands/`
- `~/.claude/agents/`

Output backup:
- `~/.claude/backups/contextd-backup-{timestamp}.tgz` (macOS/Linux)
- `~/.claude/backups/contextd-backup-{timestamp}.zip` (Windows PowerShell)

## CHECKPOINT 2 — Xác nhận thực thi

Hỏi user xác nhận chạy backup ngay bây giờ.
Chỉ chạy khi user đồng ý.

## CHECKPOINT 3 — Chạy backup theo OS

- macOS/Linux: dùng `tar -czf`
- Windows PowerShell: dùng `Compress-Archive`

Luôn tạo `~/.claude/backups/` nếu chưa có.

## CHECKPOINT 4 — Verify artifact

Sau khi chạy, bắt buộc verify:
- File backup tồn tại
- Kích thước file > 0

Nếu fail verify: báo lỗi, không báo thành công.

## CHECKPOINT 5 — Kết quả

In:

```text
Backup complete
- File: {backup_path}
- Created at (UTC): {timestamp}
- Next step: chạy /contextd-upgrade
```
