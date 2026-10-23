

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemFormatFormat(enum.StrEnum):
    MDY = "M-d-y"
    DMY = "d-M-y"
    YMD = "y-M-d"

    def visit(
        self, mdy: typing.Callable[[], T_Result], dmy: typing.Callable[[], T_Result], ymd: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is SurveyBlocksItemElementsItemFormatFormat.MDY:
            return mdy()
        if self is SurveyBlocksItemElementsItemFormatFormat.DMY:
            return dmy()
        if self is SurveyBlocksItemElementsItemFormatFormat.YMD:
            return ymd()
