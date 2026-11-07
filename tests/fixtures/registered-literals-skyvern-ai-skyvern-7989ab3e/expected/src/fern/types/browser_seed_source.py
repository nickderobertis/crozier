

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BrowserSeedSource(enum.StrEnum):
    """
    Which layer of the seed-precedence chain seeded a run's browser (provenance).

    Resolved once at run setup, before any browser creation, for all run types (C-semantics).
    - override: explicit request browser_profile_id (one-run-only pick via API)
    - picked: the workflow's explicit profile pick (workflows.browser_profile_id) — "always start here"
    - own_memory: the workflow's own auto-profile (no pick + persist_browser_session)
    - credential: the run's selected credential's profile (rotation-aware; also the empty-own boot)
    - fresh: no seed profile
    - degraded_fresh: a resolved profile failed to load; ran fresh
    """

    OVERRIDE = "override"
    PICKED = "picked"
    OWN_MEMORY = "own_memory"
    CREDENTIAL = "credential"
    FRESH = "fresh"
    DEGRADED_FRESH = "degraded_fresh"

    def visit(
        self,
        override: typing.Callable[[], T_Result],
        picked: typing.Callable[[], T_Result],
        own_memory: typing.Callable[[], T_Result],
        credential: typing.Callable[[], T_Result],
        fresh: typing.Callable[[], T_Result],
        degraded_fresh: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BrowserSeedSource.OVERRIDE:
            return override()
        if self is BrowserSeedSource.PICKED:
            return picked()
        if self is BrowserSeedSource.OWN_MEMORY:
            return own_memory()
        if self is BrowserSeedSource.CREDENTIAL:
            return credential()
        if self is BrowserSeedSource.FRESH:
            return fresh()
        if self is BrowserSeedSource.DEGRADED_FRESH:
            return degraded_fresh()
