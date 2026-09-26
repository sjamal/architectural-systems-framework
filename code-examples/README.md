# Code Examples & Configs

Small patterns that illustrate principles from the manual. They are teaching examples, not production-ready modules.

| Example | Principle | How to try it |
|---|---|---|
| [append_only_parti.py](append_only_parti.py) | [The Parti](../docs/01-foundational-vision.md#1-the-parti-primary-conceptual-anchor) | `python3 code-examples/append_only_parti.py` |
| [nginx_dual_purpose.conf](nginx_dual_purpose.conf) | [Dual-Justification Components](../docs/02-structural-integrity.md#1-dual-justification-components) | `nginx -t -c "$PWD/code-examples/nginx_dual_purpose.conf"` |
| [sqs_dead_letter_void.yaml](sqs_dead_letter_void.yaml) | [Positive and Negative Space](../docs/02-structural-integrity.md#2-positive-and-negative-space-solid-vs-void) | `cfn-lint code-examples/sqs_dead_letter_void.yaml` |
| [chaos_injection_detour.py](chaos_injection_detour.py) | [Iterative Reframing](../docs/04-observability-and-views.md#1-iterative-reframing--deliberate-detours) | `python3 code-examples/chaos_injection_detour.py` |

Each file's header comment links back to its principle. See the [runbook](../docs/RUNBOOK.md) for prerequisites, expected output, and troubleshooting, and run everything with `./scripts/init_repo.sh check`.

---
**Related docs:** [Main index](../README.md) · [ADRs](../adrs/README.md) · [Runbook](../docs/RUNBOOK.md) · [Contributing](../CONTRIBUTING.md)
