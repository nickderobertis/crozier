

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ThemeStatusPhase(enum.StrEnum):
    """
    Current theme lifecycle phase.
    """

    READY = "READY"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        ready: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ThemeStatusPhase.READY:
            return ready()
        if self is ThemeStatusPhase.FAILED:
            return failed()
        if self is ThemeStatusPhase.UNKNOWN:
            return unknown()
