

from __future__ import annotations


class FernApiEnvironment:
    DEFAULT: FernApiEnvironment

    def __init__(self, *, base: str, live: str):
        self.base = base
        self.live = live


FernApiEnvironment.DEFAULT = FernApiEnvironment(base="https://feeds.buoys.test", live="https://live.buoys.test")
