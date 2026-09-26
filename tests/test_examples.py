"""Tests for the runnable Python code examples."""

import dataclasses
import importlib.util
import pathlib

import pytest

EXAMPLES = pathlib.Path(__file__).resolve().parent.parent / "code-examples"


def _load(name):
    # code-examples/ is not a package (hyphenated name), so load modules by path.
    spec = importlib.util.spec_from_file_location(name, EXAMPLES / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


parti = _load("append_only_parti")
chaos = _load("chaos_injection_detour")


def test_compensate_appends_reversing_event():
    original = parti.SystemEvent("E1", {"action": "grant"}, parti.datetime.now())
    reversal = original.compensate("granted in error")

    assert reversal.event_id == "COMP-E1"
    assert reversal.payload == {"reversal_for": "E1", "reason": "granted in error"}
    assert original.payload == {"action": "grant"}


def test_events_are_immutable():
    event = parti.SystemEvent("E1", {}, parti.datetime.now())
    with pytest.raises(dataclasses.FrozenInstanceError):
        event.event_id = "E2"


def test_chaos_call_succeeds_without_injection():
    assert chaos.execute_resilient_call({"x": 1}, failure_rate=0.0) == {
        "status": "SUCCESS",
        "data": {"x": 1},
    }


def test_chaos_call_raises_when_injected():
    with pytest.raises(TimeoutError, match="Chaos Detour"):
        chaos.execute_resilient_call({}, failure_rate=1.0, delay_s=0)
