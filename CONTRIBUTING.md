# Contributing

Thank you for helping improve this manual.

## Before You Start
- Read [Source and Scope](README.md#source-and-scope) in the README.
- Open an issue to discuss larger changes first.

## Adding or Updating a Principle
1. Add the entry to the matching module in `docs/` using the existing structure:
   - **Architectural Reference:** lesson number and a short reference phrase.
   - **Principle:** the idea in your own words.
   - **IT Application:** how it applies to software, infrastructure, or teams.
   - **Implementation Reference** (optional): link to a code example.
2. Add the entry to the index in the [README](README.md).
3. If you add a code example, put it in `code-examples/`, add a header comment linking to its principle, and list it in the [code examples index](code-examples/README.md) and the [runbook](docs/RUNBOOK.md#3-running-each-example). Add tests for Python examples in `tests/`.

## Content Guidelines
- **Own words:** explain principles in your own words; keep quotes from the book short and for reference only.
- **Attribution:** keep the lesson reference so readers can find the original context.
- **No promotion:** describe IT applications, not the book.
- **Runnable examples:** Python examples should run with the standard library only.

## Recording Decisions
Record significant decisions as ADRs:
```bash
./scripts/init_repo.sh adr "Short decision title"
```
Then add the new ADR to the [ADR index](adrs/README.md).

## Checks
```bash
./scripts/init_repo.sh check
```
CI runs the same checks on every push and pull request. See the [runbook](docs/RUNBOOK.md) for tool setup and troubleshooting.

## Pull Requests
- Keep PRs focused on one change.
- Describe what changed and why.

---
**Related docs:** [Main index](README.md) · [ADRs](adrs/README.md) · [Code examples](code-examples/README.md) · [Runbook](docs/RUNBOOK.md)
