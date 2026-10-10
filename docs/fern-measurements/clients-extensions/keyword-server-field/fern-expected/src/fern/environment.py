

from __future__ import annotations


class FernApiEnvironment:
    DEFAULT: FernApiEnvironment

    def __init__(self, *, base: str, class_: str):
        self.base = base
        self.class_ = class_


FernApiEnvironment.DEFAULT = FernApiEnvironment(base="https://main.test", class_="https://kw.test")
