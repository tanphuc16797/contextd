#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pack-qc — Layer 1 validator rules. Prefix: pack-qc-."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, List


def _vio(rule, severity, file_path, lineno, snippet, message):
    return {
        "rule": rule, "severity": severity,
        "file": file_path.as_posix(), "line": lineno,
        "snippet": snippet.strip()[:200], "message": message,
    }


def _is_md(file_path: Path) -> bool:
    return file_path.as_posix().lower().endswith(".md")


def _looks_like_defect_doc(path: Path, lines: List[str]) -> bool:
    p = path.as_posix().lower()
    if any(k in p for k in ["bug", "defect", "incident"]):
        return True
    text = "\n".join(lines[:60]).lower()
    return any(k in text for k in ["bug", "defect", "severity", "priority"])


def _looks_like_release_doc(path: Path, lines: List[str]) -> bool:
    p = path.as_posix().lower()
    if any(k in p for k in ["release", "go-no-go", "gate"]):
        return True
    text = "\n".join(lines[:60]).lower()
    return any(k in text for k in ["release decision", "go/no-go", "quality gate"])


def _looks_like_regression_doc(path: Path, lines: List[str]) -> bool:
    p = path.as_posix().lower()
    if "regression" in p:
        return True
    text = "\n".join(lines[:60]).lower()
    return "regression" in text


def rule_bug_missing_repro(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path) or not _looks_like_defect_doc(file_path, lines):
        return []
    text = "\n".join(lines).lower()
    has_steps = any(k in text for k in ["steps to reproduce", "reproduce steps", "repro steps"])
    has_expected = "expected" in text
    has_actual = "actual" in text
    if has_steps and has_expected and has_actual:
        return []
    return [_vio(
        "pack-qc-bug-missing-repro", "error", file_path, 1, lines[0] if lines else "",
        "Defect doc missing reproducibility details (steps + expected + actual)."
    )]


def rule_bug_missing_severity_priority(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path) or not _looks_like_defect_doc(file_path, lines):
        return []
    text = "\n".join(lines).lower()
    has_severity = "severity" in text
    has_priority = "priority" in text
    if has_severity == has_priority:
        return []
    return [_vio(
        "pack-qc-bug-missing-severity-priority", "warn", file_path, 1, lines[0] if lines else "",
        "Defect doc should include both severity and priority as separate fields."
    )]


def rule_release_no_evidence(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path) or not _looks_like_release_doc(file_path, lines):
        return []
    text = "\n".join(lines).lower()
    has_evidence = any(k in text for k in ["pass rate", "failed", "coverage", "test evidence", "defect trend", "tests passed"])
    if has_evidence:
        return []
    return [_vio(
        "pack-qc-release-no-evidence", "error", file_path, 1, lines[0] if lines else "",
        "Release decision missing test evidence (pass/fail/coverage/trend)."
    )]


VAGUE_SCOPE = re.compile(r"\b(all as needed|normal regression|full regression as needed|test broadly)\b", re.IGNORECASE)


def rule_regression_vague_scope(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path) or not _looks_like_regression_doc(file_path, lines):
        return []
    out = []
    for i, raw in enumerate(lines, start=1):
        if VAGUE_SCOPE.search(raw):
            out.append(_vio(
                "pack-qc-regression-vague-scope", "warn", file_path, i, raw,
                "Regression scope is vague; specify modules/flows/risk-based scope explicitly."
            ))
    return out


def rule_perf_no_baseline_metric(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t = "\n".join(lines).lower()
    if 'optimiz' not in t and 'performance' not in t: return []
    if 'baseline' in t and ('target' in t or 'goal' in t): return []
    return [_vio('pack-qc-perf-no-baseline-metric', 'error', file_path, 1, lines[0] if lines else '', 'Optimization doc missing baseline/target metric.')]


def rule_perf_no_measure_loop(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t = "\n".join(lines).lower()
    if 'before' in t and 'after' in t: return []
    if 'optimiz' not in t and 'performance' not in t: return []
    return [_vio('pack-qc-perf-no-measure-loop', 'warn', file_path, 1, lines[0] if lines else '', 'Include before/after measurement loop.')]


def rule_perf_premature_tuning(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t = "\n".join(lines).lower()
    if 'tuning' not in t and 'optimiz' not in t: return []
    if 'profil' in t or 'bottleneck' in t or 'hotspot' in t: return []
    return [_vio('pack-qc-perf-premature-tuning', 'warn', file_path, 1, lines[0] if lines else '', 'Tuning proposal should include profiling/bottleneck evidence.')]


def rule_perf_no_regression_check(file_path: Path, lines: List[str], ctx: Dict) -> List[Dict]:
    if not _is_md(file_path): return []
    t = "\n".join(lines).lower()
    if 'optimiz' not in t and 'performance' not in t: return []
    if 'regression' in t or 'rollback' in t or 'guardrail' in t: return []
    return [_vio('pack-qc-perf-no-regression-check', 'warn', file_path, 1, lines[0] if lines else '', 'Add regression check/rollback plan for optimization.')]


RULES = [
    rule_bug_missing_repro,
    rule_bug_missing_severity_priority,
    rule_release_no_evidence,
    rule_regression_vague_scope,
    rule_perf_no_baseline_metric,
    rule_perf_no_measure_loop,
    rule_perf_premature_tuning,
    rule_perf_no_regression_check,
]
