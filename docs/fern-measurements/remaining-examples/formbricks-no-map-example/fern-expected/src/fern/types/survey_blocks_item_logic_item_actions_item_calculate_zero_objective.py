

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective(enum.StrEnum):
    CALCULATE = "calculate"

    def visit(self, calculate: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemLogicItemActionsItemCalculateZeroObjective.CALCULATE:
            return calculate()
