

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemTwoTypeOne(enum.StrEnum):
    MULTIPLE_CHOICE_MULTI = "multipleChoiceMulti"

    def visit(self, multiple_choice_multi: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemTwoTypeOne.MULTIPLE_CHOICE_MULTI:
            return multiple_choice_multi()
