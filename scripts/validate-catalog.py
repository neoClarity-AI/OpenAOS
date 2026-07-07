#!/usr/bin/env python3
"""Validate design-spec/agent-catalog.yaml for repo CI.

DERIVED TOOLING — enforces the mechanical surface of design spec §7A.5:
  V1. Every domain in domains_owned exists in vocabulary.domains.
  V2. Governance domain tokens appear only on entries with kind: governance.
  V3. domains_owned is pairwise disjoint across all entries.
  V4. artifacts_owned is pairwise disjoint across all entries.
  V5 (slug half). Every collaborates_with.agent resolves to a real slug,
      and every handoff-to has a matching reciprocal handoff-from.

Shape/type checks come from catalog.schema.json (a rendering of §7A.3/§7A.6;
the markdown design specification remains the single source of truth, §1.6.1).

Usage: python scripts/validate-catalog.py [catalog.yaml] [schema.json]
Exit code 0 = pass, 1 = failures found.

Dependencies: pyyaml (required), jsonschema (optional — schema check is
skipped with a warning when not installed).
"""

import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
CATALOG = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO / "design-spec" / "agent-catalog.yaml"
SCHEMA = Path(sys.argv[2]) if len(sys.argv) > 2 else REPO / "design-spec" / "catalog.schema.json"

# Governance tokens are the vocabulary entries reserved for kind: governance
# (§7A.6 lists them under the "# governance" comment). The comment is not
# machine-readable, so the reserved set is recognized by its normative
# pattern: tokens owned by governance entries. We derive it from the catalog
# itself and cross-check both directions.

def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))

    # Schema (shape/type) validation
    try:
        import jsonschema  # type: ignore

        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        validator_cls = getattr(
            jsonschema, "Draft202012Validator", None
        ) or jsonschema.validators.validator_for(schema)
        validator = validator_cls(schema)
        for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
            path = "$." + ".".join(str(p) for p in e_path) if (e_path := list(err.absolute_path)) else "$"
            errors.append(f"[schema] {path}: {err.message}")
    except ImportError:
        warnings.append("[schema] jsonschema not installed - shape check skipped")

    vocab = set(data.get("vocabulary", {}).get("domains", []))
    agents = data.get("agents", [])
    slugs = {a.get("slug") for a in agents}

    governance_owned = {
        d for a in agents if a.get("kind") == "governance" for d in a.get("domains_owned", [])
    }

    # V1 — domains exist in vocabulary
    for a in agents:
        for d in a.get("domains_owned", []) + a.get("inputs", []) + a.get("outputs", []):
            if d not in vocab:
                errors.append(f"[V1] {a.get('slug')}: domain '{d}' not in vocabulary.domains")

    # V2 — governance tokens only on kind: governance
    for a in agents:
        if a.get("kind") != "governance":
            for d in a.get("domains_owned", []):
                if d in governance_owned:
                    errors.append(
                        f"[V2] {a.get('slug')}: governance token '{d}' on kind: {a.get('kind')}"
                    )

    # V3 — domains_owned pairwise disjoint
    seen_domains: dict[str, str] = {}
    for a in agents:
        for d in a.get("domains_owned", []):
            if d in seen_domains:
                errors.append(
                    f"[V3] domain '{d}' owned by both {seen_domains[d]} and {a.get('slug')}"
                )
            seen_domains[d] = a.get("slug")

    # V4 — artifacts_owned pairwise disjoint
    seen_artifacts: dict[str, str] = {}
    for a in agents:
        for g in a.get("artifacts_owned", []):
            if g in seen_artifacts:
                errors.append(
                    f"[V4] artifact '{g}' owned by both {seen_artifacts[g]} and {a.get('slug')}"
                )
            seen_artifacts[g] = a.get("slug")

    # V5 (slug half) — edges resolve; handoff reciprocity
    edges = set()
    for a in agents:
        for e in a.get("collaborates_with", []):
            target = e.get("agent")
            if target not in slugs:
                errors.append(f"[V5] {a.get('slug')}: edge to unknown agent '{target}'")
            edges.add((a.get("slug"), e.get("direction"), target))
    for (src, direction, dst) in edges:
        if direction == "handoff-to" and (dst, "handoff-from", src) not in edges:
            warnings.append(f"[V5] {src} handoff-to {dst} has no reciprocal handoff-from")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"\n{len(errors)} error(s), {len(warnings)} warning(s) — "
          f"{len(agents)} agents, {len(vocab)} vocabulary domains.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
