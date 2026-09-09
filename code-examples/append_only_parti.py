"""
Demonstrates 'The Parti' principle in software design.
Enforces an append-only event-sourcing strategy via immutable data structures.
"""
from dataclass import dataclass
from datetime import datetime

@dataclass(frozen=True)
class SystemEvent:
    event_id: str
    payload: dict
    timestamp: datetime

    def Compensate(self, reason: str) -> "SystemEvent":
        """Appends a reversing event rather than mutating internal state."""
        return SystemEvent(
            event_id=f"COMP-{self.event_id}",
            payload={"reversal_for": self.event_id, "reason": reason},
            timestamp=datetime.utcnow()
        )
