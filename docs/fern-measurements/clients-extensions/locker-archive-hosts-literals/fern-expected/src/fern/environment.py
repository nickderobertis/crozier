

from __future__ import annotations


class FernApiEnvironment:
    DEFAULT: FernApiEnvironment

    def __init__(self, *, base: str, archive: str):
        self.base = base
        self.archive = archive


FernApiEnvironment.DEFAULT = FernApiEnvironment(
    base="https://lockers.test/v2", archive="https://archive.lockers.test/v1"
)
