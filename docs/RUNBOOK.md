# Runbook: Running and Testing the Examples

How to run, test, and validate the code examples in this manual. For adding content, see [Contributing](../CONTRIBUTING.md).

## 1. Prerequisites

| Tool | Needed for | Install (macOS) |
|---|---|---|
| Python 3.10+ | Python examples | `brew install python` |
| [uv](https://docs.astral.sh/uv/) | Running tests and `cfn-lint` without a manual venv | `brew install uv` |
| nginx | Validating `nginx_dual_purpose.conf` | `brew install nginx` |
| Docker (optional) | Validating nginx without installing it | Docker Desktop |

All tools except Python are optional; `check` skips whatever is missing.

## 2. One-Command Check

```bash
./scripts/init_repo.sh check
```

This runs, in order:
1. Each Python example in `code-examples/`.
2. Unit tests in `tests/` (via `uv`, or `python3 -m pytest` if uv is absent).
3. `nginx -t` against the nginx example.
4. `cfn-lint` against the CloudFormation example (via `cfn-lint` or `uvx`).
5. A relative Markdown link and anchor check across all docs.

CI runs the same command, plus an nginx validation in Docker (see [ci.yml](../.github/workflows/ci.yml)).

## 3. Running Each Example

| Example | Command | Expected result |
|---|---|---|
| [append_only_parti.py](../code-examples/append_only_parti.py) | `python3 code-examples/append_only_parti.py` | Prints `E1` and its compensating `COMP-E1` event |
| [chaos_injection_detour.py](../code-examples/chaos_injection_detour.py) | `python3 code-examples/chaos_injection_detour.py` | Prints success/timeout counts, e.g. `{'SUCCESS': 16, 'TIMEOUT': 4}` |
| [nginx_dual_purpose.conf](../code-examples/nginx_dual_purpose.conf) | `nginx -t -c "$PWD/code-examples/nginx_dual_purpose.conf"` | `syntax is ok` / `test is successful` |
| [sqs_dead_letter_void.yaml](../code-examples/sqs_dead_letter_void.yaml) | `uvx cfn-lint code-examples/sqs_dead_letter_void.yaml` | No output (no findings) |

Validate nginx with Docker instead of a local install:
```bash
docker run --rm -v "$PWD/code-examples:/examples:ro" nginx:stable \
  nginx -t -c /examples/nginx_dual_purpose.conf
```

The CloudFormation template is for illustration only. Deploying it (`aws cloudformation deploy`) creates real SQS queues in your AWS account.

## 4. Running Tests

```bash
uv run --no-project --with pytest pytest -v tests/
```

Or with an existing Python environment:
```bash
python3 -m pip install pytest
python3 -m pytest -v tests/
```

## 5. Creating an ADR

```bash
./scripts/init_repo.sh adr "Adopt event sourcing for audit log"
```

This creates the next numbered file in `adrs/` from the [template](../adrs/ADR-000-template.md). Add it to the [ADR index](../adrs/README.md).

## 6. Troubleshooting

| Symptom | Fix |
|---|---|
| `permission denied: ./scripts/init_repo.sh` | `chmod +x scripts/init_repo.sh` |
| `skip  nginx not installed` | Install nginx or use the Docker command above |
| `skip  pytest` | Install uv (`brew install uv`) or `pip install pytest` |
| Link check reports a missing anchor | Headings changed; update the link to match the new heading slug |

---
**Related docs:** [Main index](../README.md) · [Code examples](../code-examples/README.md) · [ADRs](../adrs/README.md) · [Contributing](../CONTRIBUTING.md)
