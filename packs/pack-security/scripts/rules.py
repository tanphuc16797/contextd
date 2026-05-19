#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
from typing import Dict, List
import re


def _vio(rule, severity, file_path, lineno, snippet, message):
    return {"rule": rule, "severity": severity, "file": file_path.as_posix(), "line": lineno, "snippet": snippet.strip()[:200], "message": message}

def _is_md(p: Path) -> bool:
    return p.as_posix().lower().endswith('.md')

def rule_missing_threat_model(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t='\n'.join(lines).lower()
    if 'security' not in t and 'design' not in t: return []
    if 'threat' in t or 'abuse case' in t: return []
    return [_vio('pack-security-missing-threat-model','error',file_path,1,lines[0] if lines else '','Missing threat assumptions/abuse cases.')]

def rule_secrets_in_config(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    out=[]
    pat=re.compile(r'(api[_-]?key|secret|token|password)\s*[:=]\s*["\'][^"\']{8,}["\']',re.I)
    for i,l in enumerate(lines,1):
        if pat.search(l): out.append(_vio('pack-security-secrets-in-config','error',file_path,i,l,'Potential hardcoded secret found.'))
    return out

def rule_missing_authz_boundary(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t='\n'.join(lines).lower()
    if 'endpoint' not in t and 'flow' not in t: return []
    if 'authz' in t or 'authorization' in t or 'permission' in t: return []
    return [_vio('pack-security-missing-authz-boundary','warn',file_path,1,lines[0] if lines else '','Sensitive flow should document authorization boundary.')]

def rule_no_logging_redaction(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t='\n'.join(lines).lower()
    if 'log' not in t: return []
    if 'redact' in t or 'mask' in t: return []
    return [_vio('pack-security-no-logging-redaction','warn',file_path,1,lines[0] if lines else '','Logging guidance should include redaction/masking for sensitive data.')]

WEAK_CRYPTO = re.compile(
    r'\b(MD5|SHA-?1)\b|'
    r'MessageDigest\.getInstance\(\s*"(MD5|SHA-?1)"\s*\)|'
    r'hashlib\.(md5|sha1)\s*\(|'
    r'createHash\(\s*[\'"](md5|sha1)[\'"]\s*\)|'
    r'\bDES\b|\bRC4\b',
    re.IGNORECASE,
)

def rule_weak_crypto(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if _is_md(file_path): return []
    out = []
    for i, l in enumerate(lines, 1):
        m = WEAK_CRYPTO.search(l)
        if not m:
            continue
        if re.search(r'(audit|legacy|interop|fingerprint|etag|cache.?key)', l, re.IGNORECASE):
            continue
        out.append(_vio(
            'pack-security-weak-crypto', 'error', file_path, i, l,
            f"Weak/deprecated algorithm '{m.group(0)}' — use SHA-256+/bcrypt/argon2/scrypt for auth; AES-GCM for symmetric."
        ))
    return out


JWT_NO_VERIFY = re.compile(
    r'jwt\.\w+\([^)]*verify\s*=\s*False|'
    r'algorithms\s*=\s*\[\s*["\']none["\']|'
    r'verifySignature\s*:\s*false',
    re.IGNORECASE,
)

def rule_jwt_no_verify(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if _is_md(file_path): return []
    out = []
    for i, l in enumerate(lines, 1):
        if JWT_NO_VERIFY.search(l):
            out.append(_vio(
                'pack-security-jwt-no-verify', 'error', file_path, i, l,
                "JWT decoded without signature verification — token forgery trivial. Verify signature + issuer + audience + exp."
            ))
    return out


def rule_pentest_finding_no_evidence(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path):
        return []
    text = '\n'.join(lines).lower()
    if 'finding' not in text and 'vulnerability' not in text:
        return []
    if any(k in text for k in ['poc', 'evidence', 'proof', 'reproduce', 'steps to reproduce']):
        return []
    return [_vio('pack-security-pentest-finding-no-evidence', 'error', file_path, 1, lines[0] if lines else '', 'Finding missing minimum evidence/PoC details.')]


def rule_pentest_missing_scope_boundary(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path):
        return []
    text = '\n'.join(lines).lower()
    if 'pentest' not in text and 'assessment' not in text:
        return []
    if ('in-scope' in text or 'in scope' in text) and ('out-of-scope' in text or 'out of scope' in text):
        return []
    return [_vio('pack-security-pentest-missing-scope-boundary', 'error', file_path, 1, lines[0] if lines else '', 'Pentest doc should declare both in-scope and out-of-scope boundaries.')]


def rule_pentest_no_risk_rating(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path):
        return []
    text = '\n'.join(lines).lower()
    if 'finding' not in text and 'vulnerability' not in text:
        return []
    if any(k in text for k in ['severity', 'risk rating', 'impact', 'likelihood']):
        return []
    return [_vio('pack-security-pentest-no-risk-rating', 'warn', file_path, 1, lines[0] if lines else '', 'Finding should include severity/risk rating.')]


def rule_pentest_no_remediation(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path):
        return []
    text = '\n'.join(lines).lower()
    if 'finding' not in text and 'vulnerability' not in text:
        return []
    if any(k in text for k in ['remediation', 'mitigation', 'fix recommendation', 'verification step', 'retest']):
        return []
    return [_vio('pack-security-pentest-no-remediation', 'warn', file_path, 1, lines[0] if lines else '', 'Finding should include remediation or verification step.')]


RULES=[rule_missing_threat_model,rule_secrets_in_config,rule_missing_authz_boundary,rule_no_logging_redaction,rule_weak_crypto,rule_jwt_no_verify,rule_pentest_finding_no_evidence,rule_pentest_missing_scope_boundary,rule_pentest_no_risk_rating,rule_pentest_no_remediation]
