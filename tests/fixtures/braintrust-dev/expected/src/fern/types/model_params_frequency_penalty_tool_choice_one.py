

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelParamsFrequencyPenaltyToolChoiceOne(enum.StrEnum):
    NONE = "none"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelParamsFrequencyPenaltyToolChoiceOne.NONE:
            return none()
