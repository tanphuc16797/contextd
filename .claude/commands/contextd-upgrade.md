# Wiki Upgrade

Nâng cấp contextd trên máy user lên bản mới nhất từ GitHub release.

## CHECKPOINT 0 — Release note & cảnh báo

In thông báo này trước khi làm gì khác:

```text
⚠️ Bạn sắp upgrade contextd lên bản mới nhất.
Tác động:
- Sẽ cập nhật slash commands + agents trong ~/.claude/
- Có thể thay đổi behavior theo rules/commands mới
- Nên commit hoặc lưu lại công việc đang làm trước khi tiếp tục
```

Nếu đọc được metadata cũ tại `~/.claude/wiki-install-meta.json` (hoặc `%USERPROFILE%\\.claude\\wiki-install-meta.json` trên Windows), in thêm:

```text
Current installed version: {release_tag}
```

Khuyến nghị chạy backup trước bằng `/contextd-backup` để có rollback nhanh bằng `/contextd-restore`.

## CHECKPOINT 1 — Xác nhận thực thi

Thông báo rõ lệnh sẽ chạy:
- Linux/macOS:
  `curl -fsSL https://github.com/tanphuc16797/workspace-wiki/releases/latest/download/install.sh | sh`
- Windows PowerShell:
  `iwr https://github.com/tanphuc16797/workspace-wiki/releases/latest/download/install.ps1 -UseBasicParsing | iex`

Hỏi user xác nhận chạy upgrade ngay bây giờ. Chỉ chạy khi user đồng ý.

## CHECKPOINT 2 — Chạy installer theo OS

- Nếu môi trường là Windows PowerShell, chạy lệnh PowerShell.
- Ngược lại, chạy lệnh Linux/macOS.

Nếu lỗi: in stderr ngắn gọn + gợi ý kiểm tra network, quyền shell, và khả dụng của `curl`/`bash` (hoặc `iwr`).

## CHECKPOINT 3 — Verify metadata sau upgrade

Bắt buộc đọc và in file metadata:
- `~/.claude/wiki-install-meta.json` (macOS/Linux)
- `%USERPROFILE%\\.claude\\wiki-install-meta.json` (Windows)

In tối thiểu:

```text
Upgrade complete
- Repo: {repo}
- Release tag: {release_tag}
- Installed at (UTC): {installed_at_utc}
```

Nếu không đọc được metadata thì cảnh báo và gợi ý chạy `/contextd-version`.

## CHECKPOINT 4 — Post-upgrade guidance

In:

```text
Gợi ý: /exit rồi mở lại Claude Code session.
Nếu có vấn đề sau upgrade, chạy /contextd-restore để rollback.
```
