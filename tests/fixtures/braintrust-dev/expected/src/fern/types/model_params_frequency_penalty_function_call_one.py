

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ModelParamsFrequencyPenaltyFunctionCallOne(enum.StrEnum):
    NONE = "none"

    def visit(self, none: typing.Callable[[], T_Result]) -> T_Result:
        if self is ModelParamsFrequencyPenaltyFunctionCallOne.NONE:
            return none()
