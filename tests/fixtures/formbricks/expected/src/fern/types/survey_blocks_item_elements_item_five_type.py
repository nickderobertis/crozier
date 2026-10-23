

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemFiveType(enum.StrEnum):
    RATING = "rating"

    def visit(self, rating: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemFiveType.RATING:
            return rating()
