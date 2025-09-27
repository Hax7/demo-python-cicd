from __future__ import annotations

import math
import pytest

from demo_app.logic import Summary, greet, summarize


def test_greet_returns_polite_message() -> None:
    assert greet("Ada") == "Hello, Ada!"


def test_greet_rejects_blank_input() -> None:
    with pytest.raises(ValueError):
        greet("   ")


def test_summarize_handles_numbers() -> None:
    summary = summarize([1, 2, 3, 4])

    assert isinstance(summary, Summary)
    assert summary.count == 5
    assert math.isclose(summary.total, 10)
    assert math.isclose(summary.average, 2.5)
    assert summary.minimum == 1
    assert summary.maximum == 4


def test_summarize_requires_values() -> None:
    with pytest.raises(ValueError):
        summarize([])
