# ADR-001: Define the Parti for Systems in This Manual

## Status
Accepted

## Date
2026-09-25

## Principle
[The "Parti" (Primary Conceptual Anchor)](../docs/01-foundational-vision.md#1-the-parti-primary-conceptual-anchor)

## Context
Architectural proposals are often judged on local merit (a faster library, a newer service) without a shared reference point. Over time the system loses coherence: each part is reasonable, but the whole has no organizing idea. This manual needs a consistent way to express that organizing idea for IT systems.

## Decision
Every system that applies this manual states its **parti**: a one-sentence central organizing concept, recorded as the system's first ADR. Examples:
- "All state changes are immutable, append-only events." (see [`append_only_parti.py`](../code-examples/append_only_parti.py))
- "Every request is authenticated and authorized at the edge; no implicit trust inside."

Design reviews and significant pull requests are checked against the parti. A change that conflicts with it requires either a redesign or a new ADR that explicitly revises the parti.

## Alternatives Considered
- **No explicit parti:** relies on tribal knowledge; coherence erodes as teams change.
- **A long architecture vision document:** harder to apply in reviews; rarely re-read.

## Consequences
- Positive: a short, reviewable anchor for decisions; faster onboarding; clearer grounds for rejecting drift.
- Negative: a poorly chosen parti can constrain the system; revising it needs deliberate effort.
- Follow-up: include a "Does this align with the parti?" item in design review and PR templates.

## References
- [Code example: append-only events](../code-examples/append_only_parti.py)
- [Process-Oriented System Evolution](../docs/03-governance-and-process.md#1-process-oriented-system-evolution)

---
**Related docs:** [ADR index](README.md) · [ADR template](ADR-000-template.md) · [Main index](../README.md) · [Module 1](../docs/01-foundational-vision.md) · [Code examples](../code-examples/README.md)
