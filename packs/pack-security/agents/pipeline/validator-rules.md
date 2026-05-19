# pack-security — Validator Rules

Layer-1 rule. Prefix `pack-security-`.

| Rule ID | Severity | Check |
|---------|----------|-------|
| `pack-security-missing-threat-model` | error | Security/design doc thiếu threat assumptions hoặc abuse cases |
| `pack-security-secrets-in-config` | error | Có dấu hiệu secret hardcoded trong config/examples |
| `pack-security-missing-authz-boundary` | warn | Luồng/endpoint nhạy cảm thiếu authz boundary |
| `pack-security-no-logging-redaction` | warn | Logging/security note thiếu redaction guidance |
| `pack-security-weak-crypto` | error | MD5/SHA-1/DES/RC4 sử dụng cho auth/integrity ngoài context legacy/audit |
| `pack-security-jwt-no-verify` | error | JWT decode với `verify=False` hoặc `alg=none` — forge token trivial |
| `pack-security-pentest-finding-no-evidence` | error | Finding doc thiếu PoC/evidence tối thiểu |
| `pack-security-pentest-missing-scope-boundary` | error | Pentest doc thiếu in-scope/out-of-scope |
| `pack-security-pentest-no-risk-rating` | warn | Finding thiếu severity/risk rating |
| `pack-security-pentest-no-remediation` | warn | Finding thiếu remediation hoặc verification step |

## Layer-2 self-check

```md
### Security Engineering (pack-security)
- Security/design doc có threat assumptions hoặc abuse cases
- Không hardcode secret trong config/examples
- Luồng/endpoint nhạy cảm có authz boundary
- Logging guidance có redaction/masking cho dữ liệu nhạy cảm

### Pentest (pack-security — pentest workflow)
- Có in-scope/out-of-scope rõ ràng
- Finding có evidence có thể kiểm chứng
- Finding có risk rating
- Finding có remediation + verification step
```

## Related

- Implementation: [`scripts/rules.py`](../../scripts/rules.py)
- Engine validator pipeline: [`agents/pipeline/validator-rules.md`](../../../../agents/pipeline/validator-rules.md)
