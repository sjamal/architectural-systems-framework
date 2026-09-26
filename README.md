# Architectural Systems Reference Manual
*An Engineering Adaptation of Spatial Design Principles for IT, DevOps, and Software Systems*

---

## Overview

Software architecture and physical architecture share a fundamental goal: organizing complex, heterogeneous components into coherent, durable systems. This manual draws on design principles described in Matthew Frederick's *101 Things I Learned in Architecture School* and applies them, as the author's own engineering interpretation, to software systems, platform engineering, and infrastructure operations.

---

## Source and Scope

### Source and Attribution
This project is inspired by Matthew Frederick's book *101 Things I Learned in Architecture School* (MIT Press). The ideas borrowed are general design principles; the IT applications, code examples, and decisions in this repository are the author's own.

Read the book itself. This repository is not a summary of it and cannot stand in for it.

### What This Project Is
- An educational engineering reference written from an IT practitioner's perspective.
- The author's own interpretation of selected design principles as software, infrastructure, and team practices.
- A set of principles, code examples, and decision records that any IT team can adapt.

### What This Project Is Not
- It is not a review, summary, or promotion of the book.
- It is not affiliated with or endorsed by the author or publisher.
- It is not architecture (building design) guidance.

### Lesson References
*Lesson N* labels point readers to the corresponding lesson in the book for its original context. Short quoted phrases are included for reference only.

---

## Architectural Principles Index

### 1. Foundational Vision & Intent
* [The "Parti" (Primary Conceptual Anchor)](docs/01-foundational-vision.md#1-the-parti-primary-conceptual-anchor) — *Lesson 11*
* [The Specificity Paradox](docs/01-foundational-vision.md#2-the-specificity-paradox) — *Lesson 17*
* [Cross-Domain Synthesis & Broad Intuition](docs/01-foundational-vision.md#3-cross-domain-synthesis) — *Lesson 21*

### 2. Structural & Spatial Integrity
* [Dual-Justification Components](docs/02-structural-integrity.md#1-dual-justification-components) — *Lesson 18*
* [Positive and Negative Space (Solid vs. Void)](docs/02-structural-integrity.md#2-positive-and-negative-space-solid-vs-void) — *Lessons 2, 3, 5, 6*
* [Spatial Organization as Information Architecture](docs/02-structural-integrity.md#3-spatial-organization) — *Lessons 12, 13, 15*

### 3. Governance, Process & Evolution
* [Process-Oriented System Evolution](docs/03-governance-and-process.md#1-process-oriented-system-evolution) — *Lesson 26*
* [Objectivity & Consistency Over Subjective Preference](docs/03-governance-and-process.md#2-objectivity-and-consistency) — *Lessons 12, 13, 15*
* [Courage to Retire Legacy Components](docs/03-governance-and-process.md#3-courage-to-retire-legacy-components) — *Lesson 44*
* [The Arrival Sequence (System Onboarding)](docs/03-governance-and-process.md#4-the-arrival-sequence) — *Lesson 62*

### 4. Observability, Iteration & Modeling
* [Iterative Reframing & Deliberate Detours](docs/04-observability-and-views.md#1-iterative-reframing--deliberate-detours) — *Lessons 28, 37*
* [Design with Prototypes over Abstract Theory](docs/04-observability-and-views.md#2-design-with-prototypes) — *Lesson 45*
* [Tiered Observability (Distance, Approach, Interior)](docs/04-observability-and-views.md#3-tiered-observability) — *Lessons 39, 40, 41*

---

## Implementation & Practice

* [Architecture Decision Records (ADRs)](adrs/README.md)
* [Code Examples & Configs](code-examples/README.md)
* [Runbook: Running and Testing the Examples](docs/RUNBOOK.md)
* [Contributing](CONTRIBUTING.md)

---

## How to Use This Manual
1. Pick the principle closest to the decision in front of you from the index above.
2. Read its *Principle* and *IT Application*, then review the linked code example.
3. Record how you applied it as an ADR using the [template](adrs/ADR-000-template.md).

Run the Python examples (Python 3.10+, no dependencies):
```bash
python3 code-examples/append_only_parti.py
python3 code-examples/chaos_injection_detour.py
```

Run every example, test, config validation, and link check at once:
```bash
./scripts/init_repo.sh check
```

See the [runbook](docs/RUNBOOK.md) for per-example commands, expected output, and troubleshooting.

Create a new ADR from the template:
```bash
./scripts/init_repo.sh adr "Adopt event sourcing for audit log"
```

---

## Repository Layout
```text
adrs/           Architecture Decision Records and template
code-examples/  Runnable and reference patterns linked from the docs
docs/           The four principle modules and the runbook
scripts/        Helper scripts (ADR scaffolding, checks)
tests/          Unit tests for the Python examples
```

---

## License
The [MIT License](LICENSE) covers this repository's source code and original documentation only. It grants no rights to the book or its contents.

---
**Related docs:** [ADRs](adrs/README.md) · [Code examples](code-examples/README.md) · [Runbook](docs/RUNBOOK.md) · [Contributing](CONTRIBUTING.md) · Modules: [1](docs/01-foundational-vision.md) · [2](docs/02-structural-integrity.md) · [3](docs/03-governance-and-process.md) · [4](docs/04-observability-and-views.md)
