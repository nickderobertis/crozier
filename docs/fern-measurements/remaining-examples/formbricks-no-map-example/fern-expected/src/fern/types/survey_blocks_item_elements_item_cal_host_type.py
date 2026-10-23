

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemCalHostType(enum.StrEnum):
    CAL = "cal"

    def visit(self, cal: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemCalHostType.CAL:
            return cal()
