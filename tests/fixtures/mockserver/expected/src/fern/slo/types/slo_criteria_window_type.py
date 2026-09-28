

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class SloCriteriaWindowType(enum.StrEnum):
    LOOKBACK = "LOOKBACK"
    EXPLICIT = "EXPLICIT"

    def visit(self, lookback: typing.Callable[[], T_Result], explicit: typing.Callable[[], T_Result]) -> T_Result:
        if self is SloCriteriaWindowType.LOOKBACK:
            return lookback()
        if self is SloCriteriaWindowType.EXPLICIT:
            return explicit()
