#!/usr/bin/env bash
# Helper for this manual: scaffold ADRs and run local checks.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ADR_DIR="$ROOT/adrs"

usage() {
    cat <<EOF
Usage: $(basename "$0") <command> [args]

Commands:
  adr "Title"   Create the next numbered ADR from the template
  check         Run examples, tests, config validation, and Markdown link checks
  help          Show this message

Optional tools used by 'check' when installed: uv (pytest), nginx, cfn-lint (or uvx).
EOF
}

new_adr() {
    local title="${1:-}"
    [[ -n "$title" ]] || { echo "Error: ADR title required." >&2; usage; exit 1; }

    local last next slug file
    last=$(find "$ADR_DIR" -name 'ADR-[0-9][0-9][0-9]-*.md' -exec basename {} \; \
        | sed -E 's/^ADR-([0-9]{3}).*/\1/' | sort -n | tail -1)
    next=$(printf '%03d' $((10#${last:-0} + 1)))
    slug=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9' '-' | sed -E 's/^-+|-+$//g')
    file="$ADR_DIR/ADR-$next-$slug.md"

    [[ ! -e "$file" ]] || { echo "Error: $file already exists." >&2; exit 1; }

    sed -e "s/^# ADR-NNN: Title$/# ADR-$next: $title/" \
        -e "s/^YYYY-MM-DD$/$(date +%F)/" \
        -e "s/^Proposed | Accepted | Superseded by ADR-NNN | Deprecated$/Proposed/" \
        "$ADR_DIR/ADR-000-template.md" > "$file"

    echo "Created ${file#"$ROOT"/}"
    echo "Next: add it to adrs/README.md"
}

run_checks() {
    cd "$ROOT"
    echo "== Python examples"
    for f in code-examples/*.py; do
        python3 "$f" > /dev/null && echo "ok  $f"
    done

    echo "== Unit tests"
    if command -v uv > /dev/null; then
        uv run --quiet --no-project --with pytest pytest -q tests/
    elif python3 -m pytest --version > /dev/null 2>&1; then
        python3 -m pytest -q tests/
    else
        echo "skip  pytest (install uv or pytest)"
    fi

    echo "== nginx config"
    if command -v nginx > /dev/null; then
        nginx -t -q -c "$ROOT/code-examples/nginx_dual_purpose.conf" && echo "ok  nginx_dual_purpose.conf"
    else
        echo "skip  nginx not installed"
    fi

    echo "== CloudFormation template"
    if command -v cfn-lint > /dev/null; then
        cfn-lint code-examples/sqs_dead_letter_void.yaml && echo "ok  sqs_dead_letter_void.yaml"
    elif command -v uvx > /dev/null; then
        uvx --quiet cfn-lint code-examples/sqs_dead_letter_void.yaml && echo "ok  sqs_dead_letter_void.yaml"
    else
        echo "skip  cfn-lint not installed"
    fi

    echo "== Markdown links"
    python3 - <<'PY'
import pathlib, re, sys

def slug(heading: str) -> str:
    # GitHub-style anchor: lowercase, drop punctuation, spaces to hyphens.
    return re.sub(r"[^\w\- ]", "", heading.strip().lower()).replace(" ", "-")

broken = []
for md in pathlib.Path(".").rglob("*.md"):
    if any(part.startswith(".") for part in md.parts):
        continue
    for link in re.findall(r"\]\(([^)\s]+)\)", md.read_text()):
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        path, _, anchor = link.partition("#")
        target = (md.parent / path) if path else md
        if not target.exists():
            broken.append(f"{md}: {link}")
        elif anchor and target.suffix == ".md":
            heads = {slug(h) for h in re.findall(r"^#+\s+(.*)$", target.read_text(), re.M)}
            if anchor not in heads:
                broken.append(f"{md}: {link} (missing anchor)")

if broken:
    print("\n".join(broken))
    sys.exit(1)
print("ok  all relative links resolve")
PY
}

case "${1:-help}" in
    adr)   shift; new_adr "$@" ;;
    check) run_checks ;;
    help|-h|--help) usage ;;
    *) echo "Unknown command: $1" >&2; usage; exit 1 ;;
esac
