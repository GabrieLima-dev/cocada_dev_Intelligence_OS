#!/usr/bin/env python3
"""Deterministic routing regression checks plus a manual qualitative manifest."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from cocada_os import classify_request  # noqa: E402


def main() -> int:
    cases = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
    failures = []
    results = []
    for case in cases:
        actual = classify_request(case["input"], case["mode"])
        expected = case["expected"]
        problems = []
        for key in ("intent", "workflow"):
            if actual[key] != expected[key]:
                problems.append(f"{key}: expected {expected[key]!r}, got {actual[key]!r}")
        missing_agents = [agent for agent in expected["required_agents"] if agent not in actual["agents"]]
        if missing_agents:
            problems.append(f"missing agents: {missing_agents}")
        result = {"id": case["id"], "routing": "FAIL" if problems else "PASS", "problems": problems, "manual_criteria": expected["qualitative"], "forbidden": case["forbidden"]}
        results.append(result)
        if problems:
            failures.append(case["id"])
    print(json.dumps({"status": "FAIL" if failures else "PASS", "routing_cases": results, "manual_review_required": True}, ensure_ascii=False, indent=2))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
