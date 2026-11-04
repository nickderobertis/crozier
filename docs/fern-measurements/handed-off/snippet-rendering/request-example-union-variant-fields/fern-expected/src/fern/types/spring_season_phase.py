

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpringSeasonPhase(enum.StrEnum):
    EARLY = "early"
    LATE = "late"

    def visit(self, early: typing.Callable[[], T_Result], late: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpringSeasonPhase.EARLY:
            return early()
        if self is SpringSeasonPhase.LATE:
            return late()
