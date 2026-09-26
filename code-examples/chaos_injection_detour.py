"""
Demonstrates Iterative Reframing via Chaos Engineering.
Forces network latency detours to verify system resilience.

Principle: docs/04-observability-and-views.md#1-iterative-reframing--deliberate-detours
Run: python3 code-examples/chaos_injection_detour.py
"""
import time
import random

def execute_resilient_call(payload: dict, failure_rate: float = 0.20, delay_s: float = 1.5):
    # Deliberate failure injection to reframe performance expectations
    if random.random() < failure_rate:
        time.sleep(delay_s)
        raise TimeoutError("Chaos Detour: Simulated Network Latency")
    return {"status": "SUCCESS", "data": payload}


if __name__ == "__main__":
    outcomes = {"SUCCESS": 0, "TIMEOUT": 0}
    for i in range(20):
        try:
            execute_resilient_call({"request": i}, delay_s=0.01)
            outcomes["SUCCESS"] += 1
        except TimeoutError:
            outcomes["TIMEOUT"] += 1
    print(outcomes)
