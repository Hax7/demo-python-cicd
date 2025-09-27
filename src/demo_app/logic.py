"""Core business logic for the demo application."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Summary:
    """Numeric summary produced from a collection of numbers."""

    count: int
    total: float
    average: float
    minimum: float
    maximum: float


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    clean_name = name.strip()
    if not clean_name:
        raise ValueError("name must contain at least one non-space character")
    return f"Hello, {clean_name}!"


def summarize(numbers: Iterable[float]) -> Summary:
    """Generate a summary for the provided *numbers*."""
    values: List[float] = [float(n) for n in numbers]
    if not values:
        raise ValueError("numbers must contain at least one value")
    total = sum(values)
    return Summary(
        count=len(values),
        total=total,
        average=total / len(values),
        minimum=min(values),
        maximum=max(values),
    )
