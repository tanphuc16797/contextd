# /contextd-version — Show Installed Version

Hiển thị phiên bản contextd đang cài trên máy user, đọc từ metadata local do installer ghi.

## Bước 1 — Đọc metadata install

Ưu tiên đọc file:
- macOS/Linux: `~/.claude/wiki-install-meta.json`
- Windows: `%USERPROFILE%\.claude\wiki-install-meta.json`

Nếu không tồn tại, in:

```text
Chưa tìm thấy metadata cài đặt tại ~/.claude/wiki-install-meta.json.
Hãy chạy lại lệnh cài đặt từ release mới nhất:
curl -fsSL https://github.com/tanphuc16797/workspace-wiki/releases/latest/download/install.sh | sh
```

## Bước 2 — In kết quả

In gọn theo format:

```text
contextd (installed)
- Repo: {repo}
- Release tag: {release_tag}
- Installed at (UTC): {installed_at_utc}
- Installer: {installer}
```

Nếu thiếu field nào thì in `unknown` cho field đó.

## Bước 3 — Gợi ý update

Nếu có `release_tag`, in thêm:

```text
Để cập nhật bản mới nhất:
curl -fsSL https://github.com/tanphuc16797/workspace-wiki/releases/latest/download/install.sh | sh
```
