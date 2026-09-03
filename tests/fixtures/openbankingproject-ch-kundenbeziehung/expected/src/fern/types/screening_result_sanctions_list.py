

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScreeningResultSanctionsList(enum.StrEnum):
    CLEAR = "clear"
    MATCH = "match"
    POTENTIAL_MATCH = "potential_match"

    def visit(
        self,
        clear: typing.Callable[[], T_Result],
        match: typing.Callable[[], T_Result],
        potential_match: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScreeningResultSanctionsList.CLEAR:
            return clear()
        if self is ScreeningResultSanctionsList.MATCH:
            return match()
        if self is ScreeningResultSanctionsList.POTENTIAL_MATCH:
            return potential_match()
