

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemAddressLine1Scale(enum.StrEnum):
    NUMBER = "number"
    SMILEY = "smiley"
    STAR = "star"

    def visit(
        self,
        number: typing.Callable[[], T_Result],
        smiley: typing.Callable[[], T_Result],
        star: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyBlocksItemElementsItemAddressLine1Scale.NUMBER:
            return number()
        if self is SurveyBlocksItemElementsItemAddressLine1Scale.SMILEY:
            return smiley()
        if self is SurveyBlocksItemElementsItemAddressLine1Scale.STAR:
            return star()
