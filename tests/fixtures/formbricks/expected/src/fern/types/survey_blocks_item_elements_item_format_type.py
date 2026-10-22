

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemFormatType(enum.StrEnum):
    DATE = "date"

    def visit(self, date: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemFormatType.DATE:
            return date()
