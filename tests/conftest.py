"""Pytest configuration helpers."""
from __future__ import annotations

import sys
from pathlib import Path


def pytest_configure() -> None:
    """Ensure the src/ directory is on sys.path for imports."""
    src_path = Path(__file__).resolve().parent.parent / "src"
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
