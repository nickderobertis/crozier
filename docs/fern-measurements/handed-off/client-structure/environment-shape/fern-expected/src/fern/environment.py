

from __future__ import annotations


class FernApiEnvironment:
    PRODUCTION: FernApiEnvironment
    ARCHIVE: FernApiEnvironment

    def __init__(self, *, base: str, production: str, archive: str, alerts: str):
        self.base = base
        self.production = production
        self.archive = archive
        self.alerts = alerts


FernApiEnvironment.PRODUCTION = FernApiEnvironment(
    base="https://api.observatory.example.org",
    production="https://api.observatory.example.org",
    archive="https://archive.observatory.example.org",
    alerts="https://alerts.observatory.example.org",
)
FernApiEnvironment.ARCHIVE = FernApiEnvironment(
    base="https://archive.observatory.example.org",
    production="https://api.observatory.example.org",
    archive="https://archive.observatory.example.org",
    alerts="https://alerts.observatory.example.org",
)
