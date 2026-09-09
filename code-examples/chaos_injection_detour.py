"""
Demonstrates Iterative Reframing via Chaos Engineering.
Forces network latency detours to verify system resilience.
"""
import time
import random

def execute_resilient_call(payload: dict):
    # Deliberate failure injection to reframe performance expectations
    if random.random() < 0.20:
        time.sleep(1.5)
        raise TimeoutError("Chaos Detour: Simulated Network Latency")
    return {"status": "SUCCESS", "data": payload}
