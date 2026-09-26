"""
Demonstrates 'The Parti' principle in software design.
Enforces an append-only event-sourcing strategy via immutable data structures.

Principle: docs/01-foundational-vision.md#1-the-parti-primary-conceptual-anchor
Run: python3 code-examples/append_only_parti.py
"""
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass(frozen=True)
class SystemEvent:
    event_id: str
    payload: dict
    timestamp: datetime

    def compensate(self, reason: str) -> "SystemEvent":
        """Appends a reversing event rather than mutating internal state."""
        return SystemEvent(
            event_id=f"COMP-{self.event_id}",
            payload={"reversal_for": self.event_id, "reason": reason},
            timestamp=datetime.now(timezone.utc)
        )


if __name__ == "__main__":
    log = [SystemEvent("E1", {"action": "grant_access", "user": "alice"}, datetime.now(timezone.utc))]
    log.append(log[0].compensate("access granted in error"))
    for event in log:
        print(event.event_id, event.payload)
