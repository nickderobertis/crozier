

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemTwoTypeZero(enum.StrEnum):
    MULTIPLE_CHOICE_SINGLE = "multipleChoiceSingle"

    def visit(self, multiple_choice_single: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemTwoTypeZero.MULTIPLE_CHOICE_SINGLE:
            return multiple_choice_single()
