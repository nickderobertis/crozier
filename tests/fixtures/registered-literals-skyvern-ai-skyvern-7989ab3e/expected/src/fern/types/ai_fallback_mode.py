

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AiFallbackMode(enum.StrEnum):
    """
    Controls how an action block uses a CSS/XPath selector relative to AI.

    - `fallback`: attempt the selector first; fall back to AI on failure.
    - `proactive`: always use AI; the selector (if any) is a hint only.

    When `selector` is None, both modes degrade to AI-only — the difference
    is purely semantic (whether the author expected to have a selector here).
    """

    FALLBACK = "fallback"
    PROACTIVE = "proactive"

    def visit(self, fallback: typing.Callable[[], T_Result], proactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is AiFallbackMode.FALLBACK:
            return fallback()
        if self is AiFallbackMode.PROACTIVE:
            return proactive()
