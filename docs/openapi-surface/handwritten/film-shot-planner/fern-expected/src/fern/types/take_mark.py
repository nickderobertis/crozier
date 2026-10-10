

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TakeMark(enum.StrEnum):
    GOOD = "good"
    HOLD = "hold"
    NO_GOOD = "no-good"

    def visit(
        self,
        good: typing.Callable[[], T_Result],
        hold: typing.Callable[[], T_Result],
        no_good: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TakeMark.GOOD:
            return good()
        if self is TakeMark.HOLD:
            return hold()
        if self is TakeMark.NO_GOOD:
            return no_good()
