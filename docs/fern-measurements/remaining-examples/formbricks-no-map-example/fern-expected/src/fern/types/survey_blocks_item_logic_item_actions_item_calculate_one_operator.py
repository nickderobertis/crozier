

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemLogicItemActionsItemCalculateOneOperator(enum.StrEnum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    ASSIGN = "assign"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        subtract: typing.Callable[[], T_Result],
        multiply: typing.Callable[[], T_Result],
        divide: typing.Callable[[], T_Result],
        assign: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SurveyBlocksItemLogicItemActionsItemCalculateOneOperator.ADD:
            return add()
        if self is SurveyBlocksItemLogicItemActionsItemCalculateOneOperator.SUBTRACT:
            return subtract()
        if self is SurveyBlocksItemLogicItemActionsItemCalculateOneOperator.MULTIPLY:
            return multiply()
        if self is SurveyBlocksItemLogicItemActionsItemCalculateOneOperator.DIVIDE:
            return divide()
        if self is SurveyBlocksItemLogicItemActionsItemCalculateOneOperator.ASSIGN:
            return assign()
