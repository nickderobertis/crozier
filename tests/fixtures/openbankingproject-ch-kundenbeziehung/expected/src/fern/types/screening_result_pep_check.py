

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScreeningResultPepCheck(enum.StrEnum):
    CLEAR = "clear"
    MATCH = "match"
    POTENTIAL_MATCH = "potential_match"

    def visit(
        self,
        clear: typing.Callable[[], T_Result],
        match: typing.Callable[[], T_Result],
        potential_match: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScreeningResultPepCheck.CLEAR:
            return clear()
        if self is ScreeningResultPepCheck.MATCH:
            return match()
        if self is ScreeningResultPepCheck.POTENTIAL_MATCH:
            return potential_match()
