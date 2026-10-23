

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator(enum.StrEnum):
    ASSIGN = "assign"
    CONCAT = "concat"

    def visit(self, assign: typing.Callable[[], T_Result], concat: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator.ASSIGN:
            return assign()
        if self is SurveyBlocksItemLogicItemActionsItemCalculateZeroOperator.CONCAT:
            return concat()
