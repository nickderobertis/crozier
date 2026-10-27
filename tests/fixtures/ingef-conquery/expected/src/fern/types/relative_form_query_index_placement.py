

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelativeFormQueryIndexPlacement(enum.StrEnum):
    BEFORE = "BEFORE"
    NEUTRAL = "NEUTRAL"
    AFTER = "AFTER"

    def visit(
        self,
        before: typing.Callable[[], T_Result],
        neutral: typing.Callable[[], T_Result],
        after: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RelativeFormQueryIndexPlacement.BEFORE:
            return before()
        if self is RelativeFormQueryIndexPlacement.NEUTRAL:
            return neutral()
        if self is RelativeFormQueryIndexPlacement.AFTER:
            return after()
