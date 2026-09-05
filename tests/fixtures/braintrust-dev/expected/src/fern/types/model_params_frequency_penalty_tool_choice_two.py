

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelParamsFrequencyPenaltyToolChoiceTwo(enum.StrEnum):
    REQUIRED = "required"

    def visit(self, required: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelParamsFrequencyPenaltyToolChoiceTwo.REQUIRED:
            return required()
