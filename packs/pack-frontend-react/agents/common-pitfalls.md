# pack-frontend-react — Top 10 Common Pitfalls

Anti-pattern lặp lại với React/Next.js. Additive trên [constraints.md](constraints.md).

## P01 — Direct state mutation
- **NG**: `state.items.push(x); setState(state)`.
- **OK**: `setState({...state, items: [...state.items, x]})` hoặc immer.
- **Why**: React so sánh reference → không re-render; bug khó tìm.
- **Detect**: Layer-1 `pack-frontend-react-state-mutation` (new) — regex `\.push\(|\.pop\(|\.splice\(` trên state ref.
- **Severity**: error

## P02 — useEffect thiếu cleanup
- **NG**: `useEffect(() => { setInterval(...) }, [])` không clear.
- **OK**: return cleanup `() => clearInterval(id)`.
- **Why**: memory leak, callback chạy sau unmount → set state on unmounted.
- **Detect**: Layer-2 — effect có `setInterval|addEventListener|subscribe` mà không có return.
- **Severity**: error

## P03 — Dependency array sai/thiếu
- **NG**: `useEffect(() => { fetch(url) }, [])` nhưng `url` thay đổi.
- **OK**: liệt kê đủ dep; dùng `eslint-plugin-react-hooks`.
- **Why**: stale closure, fetch sai data.
- **Detect**: ESLint `react-hooks/exhaustive-deps`; Layer-2.
- **Severity**: error

## P04 — `key={index}` trong dynamic list
- **NG**: `items.map((x, i) => <Row key={i} />)` khi list có reorder/insert/delete.
- **OK**: `key={x.id}` stable.
- **Why**: re-mount sai, mất focus/state input.
- **Detect**: Layer-1 `pack-frontend-react-key-index` (new) — regex `key=\{(idx|index|i)\}`.
- **Severity**: warn

## P05 — Fetch trong render body
- **NG**: `function X() { const data = fetch(...); }` ngoài effect.
- **OK**: `useEffect`/`useQuery`/server component.
- **Why**: fetch mỗi render, race condition, infinite loop.
- **Detect**: Layer-2 — fetch ngoài hook.
- **Severity**: error

## P06 — Thiếu a11y (alt, label, role)
- **NG**: `<img src=... />` không `alt`; button bằng `<div onClick>`.
- **OK**: `<img alt>`, `<button>`, `aria-label`.
- **Why**: screen reader broken, lint fail, lawsuit risk.
- **Detect**: Layer-1 `pack-frontend-react-missing-alt` (new) — regex `<img(?![^>]*\balt=)`.
- **Severity**: warn

## P07 — Prop drilling > 3-4 levels
- **NG**: pass `user` qua 5 component trung gian.
- **OK**: Context, hoặc state management (Zustand/Redux/Jotai).
- **Why**: refactor đau, coupling cao.
- **Detect**: Layer-2 review.
- **Severity**: info

## P08 — Không memo cho expensive child
- **NG**: parent re-render mỗi keystroke → render lại table 10k row.
- **OK**: `React.memo`, `useMemo`, `useCallback` cho prop fn.
- **Why**: jank, UX kém.
- **Detect**: Layer-2 review React Profiler trace.
- **Severity**: warn

## P09 — useState cho derived value
- **NG**: `const [fullName, setFullName] = useState(first+last); useEffect(() => setFullName(...))`.
- **OK**: `const fullName = first + ' ' + last;` (tính trực tiếp).
- **Why**: double render, state drift.
- **Detect**: Layer-2 review.
- **Severity**: warn

## P10 — Suspense / error boundary thiếu
- **NG**: lazy component không bọc Suspense; throw làm white-screen toàn app.
- **OK**: `<Suspense fallback>`, `<ErrorBoundary>` ở route level.
- **Why**: UX vỡ khi 1 component lỗi.
- **Detect**: Layer-2 — root layout có boundary.
- **Severity**: warn

## Mapping to validator

| Pitfall | Layer-1 rule ID | Layer-2 self-check |
|---|---|---|
| P01 mutation | `pack-frontend-react-state-mutation` (new) | ✓ |
| P02 cleanup | — | ✓ |
| P03 deps | — (ESLint) | ✓ |
| P04 key-index | `pack-frontend-react-key-index` (new) | ✓ |
| P05 fetch-render | — | ✓ |
| P06 a11y-alt | `pack-frontend-react-missing-alt` (new) | ✓ |
| P07 drilling | — | ✓ |
| P08 memo | — | ✓ |
| P09 derived-state | — | ✓ |
| P10 boundary | — | ✓ |
