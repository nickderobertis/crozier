

from __future__ import annotations


class FernApiEnvironment:
    PRODUCTION: FernApiEnvironment

    def __init__(self, *, base: str, synthesis: str):
        self.base = base
        self.synthesis = synthesis


FernApiEnvironment.PRODUCTION = FernApiEnvironment(
    base="https://app.resemble.ai/api/v2", synthesis="https://f.cluster.resemble.ai"
)
