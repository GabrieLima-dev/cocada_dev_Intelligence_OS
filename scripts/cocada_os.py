#!/usr/bin/env python3
"""Local utilities for COCADA Content Intelligence OS (stdlib only)."""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ID = re.compile(r"^CNT-(\d{4})-(\d{4})$")
REQUIRED_AGENT_SECTIONS = (
    "ROLE", "MISSION", "INPUTS", "OUTPUTS", "TOOLS", "CONTEXT REQUIRED",
    "PROCESS", "QUALITY CHECK", "BOUNDARIES", "HANDOFFS", "MEMORY READ",
    "MEMORY WRITE", "FAILURE MODES",
)
REQUIRED_WORKFLOW_SECTIONS = (
    "Trigger", "Inputs", "Agents", "Sequence", "Decision points", "Outputs",
    "Memory updates", "Quality gates", "Failure and escalation",
)
REQUIRED_PATHS = (
    "README.md", "AGENTS.md", "CHANGELOG.md", "brand/BRAND_OS.md",
    "strategy/CURRENT_STRATEGY.md", "memory/creator/profile.md",
    "agents/orchestrator/AGENT.md", "agents/system-architect/AGENT.md",
    "workflows/request_routing.md", "workflows/idea_to_publish.md",
    "workflows/metrics_to_learning.md", "schemas/content.schema.json",
    "templates/CONTENT_TEMPLATE.md", "evals/cases.json",
)


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso_z(value: datetime) -> str:
    return value.isoformat().replace("+00:00", "Z")


def ascii_fold(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value)
    return "".join(ch for ch in normalized if not unicodedata.combining(ch)).lower()


def yaml_quote(value: str) -> str:
    # A JSON string is a valid YAML scalar and safely handles punctuation/newlines.
    return json.dumps(value, ensure_ascii=False)


def iter_content_files(base: Path | None = None) -> list[Path]:
    base = base or ROOT
    content = base / "content"
    return [p for p in content.rglob("*.md") if p.name != "README.md"]


def ids_in_files(base: Path | None = None) -> dict[str, list[Path]]:
    base = base or ROOT
    found: dict[str, list[Path]] = {}
    pattern = re.compile(r"(?m)^id:\s*(CNT-\d{4}-\d{4})\s*$")
    for path in iter_content_files(base):
        for value in pattern.findall(path.read_text(encoding="utf-8")):
            found.setdefault(value, []).append(path)
    return found


def next_content_id(year: int, base: Path | None = None) -> str:
    base = base or ROOT
    largest = 0
    for value in ids_in_files(base):
        match = CONTENT_ID.match(value)
        if match and int(match.group(1)) == year:
            largest = max(largest, int(match.group(2)))
    return f"CNT-{year}-{largest + 1:04d}"


def slugify(value: str) -> str:
    folded = ascii_fold(value)
    slug = re.sub(r"[^a-z0-9]+", "-", folded).strip("-")
    return (slug[:60].rstrip("-") or "conteudo")


def parse_scoring_config(path: Path) -> tuple[dict[str, float], dict[str, float], dict[str, float]]:
    section = None
    parsed: dict[str, dict[str, float]] = {"weights": {}, "gates": {}, "priority_thresholds": {}}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line:
            continue
        if not line.startswith(" ") and line.endswith(":"):
            section = line[:-1]
            continue
        if section in parsed and line.startswith("  ") and ":" in line:
            key, value = line.strip().split(":", 1)
            parsed[section][key] = float(value.strip())
    return parsed["weights"], parsed["gates"], parsed["priority_thresholds"]


METRIC_NAMES = {
    "views", "reach", "retention_3s", "avg_watch_time_seconds", "completion_rate",
    "replays", "shares", "saves", "comments", "profile_visits", "followers_gained",
    "conversions",
}
RATE_METRICS = {"retention_3s", "completion_rate"}
PLATFORMS = {"instagram", "tiktok", "youtube", "linkedin", "other"}


def validate_metric_values(metrics: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(metrics, dict):
        return ["metrics must be an object"]
    unknown = sorted(set(metrics) - METRIC_NAMES)
    if unknown:
        errors.append(f"unknown metrics: {unknown}")
    for name, value in metrics.items():
        if name not in METRIC_NAMES or value is None:
            continue
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{name} must be numeric or null")
        elif value < 0:
            errors.append(f"{name} must be non-negative")
        elif name in RATE_METRICS and value > 1:
            errors.append(f"{name} must be a ratio from 0 to 1")
    return errors


def classify_request(text: str, mode: str) -> dict[str, Any]:
    value = ascii_fold(text)
    routes = [
        (("metrica", "views", "retencao", "saves", "shares", "desempenho"), "metrics", "workflows/metrics_to_learning.md", ["AGENT-ANALYTICS", "AGENT-EXPERIMENTS", "AGENT-KNOWLEDGE-CURATOR"]),
        (("noticia", "lancou", "versao nova", "mudanca recente", "novidade", "tendencia"), "news", "workflows/news_to_content.md", ["AGENT-MARKET-RADAR", "AGENT-TECHNICAL-REVIEWER", "AGENT-CONTENT-STRATEGIST"]),
        (("hook", "primeiros segundos", "abertura"), "hooks", "workflows/idea_to_publish.md", ["AGENT-HOOK-LAB"]),
        (("roteiro", "script"), "script", "workflows/idea_to_publish.md", ["AGENT-HOOK-LAB", "AGENT-SCRIPTWRITER", "AGENT-TECHNICAL-REVIEWER"]),
        (("story ou reel", "reel ou story", "vira story", "vira reel"), "format", "workflows/story_or_reel.md", ["AGENT-CONTENT-STRATEGIST"]),
        (("experiencia do trabalho", "transformar uma experiencia", "aconteceu no trabalho"), "experience_to_content", "workflows/story_or_reel.md", ["AGENT-CONTENT-STRATEGIST", "AGENT-IDEA-LAB"]),
        (("creator", "fireship", "primeagen", "attekita", "kibum"), "creator_research", "workflows/reverse_engineer_creator.md", ["AGENT-CREATOR-INTELLIGENCE", "AGENT-BRAND-STRATEGIST"]),
        (("estrategia", "pilares", "posicionamento"), "strategy", "workflows/request_routing.md", ["AGENT-BRAND-STRATEGIST", "AGENT-CONTENT-STRATEGIST"]),
        (("tenho uma ideia", "ideia sobre", "o que acha dessa ideia"), "idea_review", "workflows/idea_scoring.md", ["AGENT-BRAND-STRATEGIST", "AGENT-CONTENT-STRATEGIST", "AGENT-IDEA-LAB"]),
        (("o que postar", "produzir hoje", "nao sei o que", "me de ideias", "/idea"), "direction", "workflows/daily_direction.md", ["AGENT-CONTENT-STRATEGIST", "AGENT-IDEA-LAB", "AGENT-HOOK-LAB"]),
    ]
    for keywords, intent, workflow, agents in routes:
        if any(keyword in value for keyword in keywords):
            break
    else:
        intent, workflow, agents = "consulting", "workflows/request_routing.md", ["AGENT-ORCHESTRATOR"]
    if mode == "FAST":
        agents = agents[:2]
    return {"intent": intent, "mode": mode, "workflow": workflow, "agents": agents, "always_reads": ["brand/BRAND_OS.md", "strategy/CURRENT_STRATEGY.md", "memory/creator/profile.md"]}


def cmd_doctor(_: argparse.Namespace) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    content_ids = ids_in_files()
    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).exists():
            errors.append(f"missing required path: {relative}")

    schemas = sorted((ROOT / "schemas").glob("*.json"))
    for path in schemas:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if "$schema" not in data:
                warnings.append(f"schema has no $schema: {path.relative_to(ROOT)}")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {path.relative_to(ROOT)}: {exc}")

    for path in sorted((ROOT / "analytics" / "events").glob("*.json")):
        try:
            event = json.loads(path.read_text(encoding="utf-8"))
            errors.extend(f"{path.relative_to(ROOT)}: {item}" for item in validate_metric_values(event.get("metrics")))
            if event.get("platform") not in PLATFORMS:
                errors.append(f"{path.relative_to(ROOT)}: invalid platform")
            if not CONTENT_ID.match(str(event.get("content_id", ""))):
                errors.append(f"{path.relative_to(ROOT)}: invalid content_id")
            elif event.get("content_id") not in content_ids:
                errors.append(f"{path.relative_to(ROOT)}: orphan content_id {event.get('content_id')}")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid metric event JSON {path.relative_to(ROOT)}: {exc}")

    agent_files = sorted((ROOT / "agents").glob("*/AGENT.md"))
    if len(agent_files) < 18:
        errors.append(f"expected at least 18 agents, found {len(agent_files)}")
    for path in agent_files:
        text = path.read_text(encoding="utf-8")
        if "brand/BRAND_OS.md" not in text:
            errors.append(f"{path.relative_to(ROOT)} does not declare Brand OS reading")
        for section in REQUIRED_AGENT_SECTIONS:
            if f"## {section}" not in text:
                errors.append(f"{path.relative_to(ROOT)} missing section {section}")

    workflow_files = sorted((ROOT / "workflows").glob("*.md"))
    for path in workflow_files:
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_WORKFLOW_SECTIONS:
            if f"## {section}" not in text:
                errors.append(f"{path.relative_to(ROOT)} missing section {section}")

    weights, _, _ = parse_scoring_config(ROOT / "config/idea_scoring.yaml")
    if round(sum(weights.values()), 6) != 100:
        errors.append(f"idea scoring weights sum to {sum(weights.values())}, expected 100")

    for value, paths in content_ids.items():
        if len(paths) > 1:
            errors.append(f"duplicate content id {value}: {', '.join(str(p.relative_to(ROOT)) for p in paths)}")

    result = {"status": "FAIL" if errors else "PASS", "agents": len(agent_files), "workflows": len(workflow_files), "schemas": len(schemas), "errors": errors, "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


def cmd_route(args: argparse.Namespace) -> int:
    print(json.dumps(classify_request(args.request, args.mode), ensure_ascii=False, indent=2))
    return 0


def cmd_new_content(args: argparse.Namespace) -> int:
    now = utc_now()
    year = args.year or now.year
    content_id = next_content_id(year)
    path = ROOT / "content" / "inbox" / f"{content_id}-{slugify(args.title)}.md"
    body = f'''---
schema_version: 1.0.0
id: {content_id}
title: {yaml_quote(args.title)}
pillar: {args.pillar}
series: null
objective: {args.objective}
audience: UNKNOWN
problem: UNKNOWN
topic: {yaml_quote(args.title)}
angle: UNKNOWN
hook:
  structure: UNKNOWN
  spoken: UNKNOWN
  first_frame: UNKNOWN
  payoff: UNKNOWN
  version: 1
main_mechanism: UNKNOWN
secondary_mechanisms: []
format: {args.format}
duration_seconds: UNKNOWN
platforms: []
status: inbox
priority: LATER
source:
  type: user_input
  references: []
  verified: false
created_at: {iso_z(now)}
published_at: UNKNOWN
external_ids: {{}}
score: null
hypotheses: []
production:
  framing: UNKNOWN
  broll: []
  screen: []
  text: []
  cuts: []
performance:
  status: UNKNOWN
  event_ids: []
learnings: []
---

# Notas

## Entrega

## Claims e fontes

## Histórico de versões
'''
    path.write_text(body, encoding="utf-8")
    print(json.dumps({"id": content_id, "path": str(path.relative_to(ROOT)), "next": "Complete a ideia e execute workflows/idea_scoring.md"}, ensure_ascii=False, indent=2))
    return 0


def normalize_rating(value: Any, name: str) -> tuple[float, str]:
    if isinstance(value, dict):
        rating = value.get("rating")
        reason = str(value.get("reason", ""))
    else:
        rating, reason = value, ""
    if not isinstance(rating, (int, float)) or isinstance(rating, bool) or not 0 <= rating <= 5:
        raise ValueError(f"{name} must be a number from 0 to 5")
    return float(rating), reason


def cmd_score(args: argparse.Namespace) -> int:
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    values = payload.get("ratings", payload)
    weights, gates, thresholds = parse_scoring_config(ROOT / "config/idea_scoring.yaml")
    missing = [name for name in weights if name not in values]
    extra = [name for name in values if name not in weights]
    if missing or extra:
        raise ValueError(f"rating keys mismatch; missing={missing}, extra={extra}")
    details: dict[str, Any] = {}
    total = 0.0
    ratings: dict[str, float] = {}
    for name, weight in weights.items():
        rating, reason = normalize_rating(values[name], name)
        contribution = rating / 5 * weight
        ratings[name] = rating
        total += contribution
        details[name] = {"rating": rating, "weight": weight, "contribution": round(contribution, 2), "reason": reason}
    gate_pass = ratings["brand_fit"] >= gates["brand_fit_min"] and ratings["audience_fit"] >= gates["audience_fit_min"]
    if not gate_pass:
        priority = "ARCHIVE"
    elif total >= thresholds["NOW"]:
        priority = "NOW"
    elif total >= thresholds["NEXT"]:
        priority = "NEXT"
    elif total >= thresholds["LATER"]:
        priority = "LATER"
    else:
        priority = "ARCHIVE"
    result = {"config_version": 1, "score": round(total, 2), "gate_pass": gate_pass, "suggested_priority": priority, "details": details, "warning": "Score supports editorial judgment; timing, mix and experimental value may change priority."}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def content_exists(content_id: str) -> bool:
    return content_id in ids_in_files()


def cmd_record_metrics(args: argparse.Namespace) -> int:
    if not CONTENT_ID.match(args.content_id):
        raise ValueError("content_id must match CNT-YYYY-NNNN")
    if not content_exists(args.content_id):
        raise ValueError(f"content id not found: {args.content_id}")
    payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
    platform = payload.get("platform", "instagram")
    if platform not in PLATFORMS:
        raise ValueError(f"platform must be one of {sorted(PLATFORMS)}")
    metric_errors = validate_metric_values(payload.get("metrics"))
    if metric_errors:
        raise ValueError("; ".join(metric_errors))
    window_hours = payload.get("window_hours", "UNKNOWN")
    if window_hours != "UNKNOWN" and (not isinstance(window_hours, (int, float)) or isinstance(window_hours, bool) or window_hours < 0):
        raise ValueError("window_hours must be non-negative or UNKNOWN")
    now = utc_now()
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    event_id = f"MET-{stamp}-{args.content_id}"
    event = {
        "schema_version": "1.0.0", "event_id": event_id, "content_id": args.content_id,
        "platform": platform, "captured_at": iso_z(now),
        "window_hours": window_hours, "metrics": payload.get("metrics", {}),
        "source": payload.get("source", "manual_export"), "notes": payload.get("notes", ""),
        "supersedes": payload.get("supersedes"),
    }
    path = ROOT / "analytics" / "events" / f"{event_id}.json"
    if path.exists():
        raise ValueError(f"event already exists: {path.name}")
    path.write_text(json.dumps(event, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"event_id": event_id, "path": str(path.relative_to(ROOT)), "next": "Link the event in the content record, then run workflows/metrics_to_learning.md when the measurement window is mature."}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="COCADA Content Intelligence OS utilities")
    sub = parser.add_subparsers(dest="command", required=True)
    doctor = sub.add_parser("doctor", help="audit repository contracts")
    doctor.set_defaults(func=cmd_doctor)

    route = sub.add_parser("route", help="classify a request and show its workflow")
    route.add_argument("request")
    route.add_argument("--mode", choices=("FAST", "STANDARD", "DEEP"), default="STANDARD")
    route.set_defaults(func=cmd_route)

    new = sub.add_parser("new-content", help="create an immutable content ID and inbox record")
    new.add_argument("--title", required=True)
    new.add_argument("--pillar", choices=("java", "backend_architecture", "news", "education"), required=True)
    new.add_argument("--objective", choices=("reach", "authority", "saves", "shares", "relationship", "news", "conversion", "learning"), required=True)
    new.add_argument("--format", choices=("reel", "tiktok", "short", "story", "carousel", "long_video", "text"), default="reel")
    new.add_argument("--year", type=int)
    new.set_defaults(func=cmd_new_content)

    score = sub.add_parser("score", help="score an idea from a JSON ratings file")
    score.add_argument("--input", required=True)
    score.set_defaults(func=cmd_score)

    metrics = sub.add_parser("record-metrics", help="append an immutable metrics snapshot")
    metrics.add_argument("content_id")
    metrics.add_argument("--input", required=True)
    metrics.set_defaults(func=cmd_record_metrics)
    return parser


def main() -> int:
    try:
        args = build_parser().parse_args()
        return int(args.func(args))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "message": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
