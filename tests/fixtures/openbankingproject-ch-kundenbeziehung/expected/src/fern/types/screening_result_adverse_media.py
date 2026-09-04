

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ScreeningResultAdverseMedia(enum.StrEnum):
    CLEAR = "clear"
    MATCH = "match"
    POTENTIAL_MATCH = "potential_match"

    def visit(
        self,
        clear: typing.Callable[[], T_Result],
        match: typing.Callable[[], T_Result],
        potential_match: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ScreeningResultAdverseMedia.CLEAR:
            return clear()
        if self is ScreeningResultAdverseMedia.MATCH:
            return match()
        if self is ScreeningResultAdverseMedia.POTENTIAL_MATCH:
            return potential_match()
