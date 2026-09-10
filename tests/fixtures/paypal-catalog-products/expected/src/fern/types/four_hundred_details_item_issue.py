

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FourHundredDetailsItemIssue(enum.StrEnum):
    INVALID_PARAMETER_VALUE = "INVALID_PARAMETER_VALUE"

    def visit(self, invalid_parameter_value: typing.Callable[[], T_Result]) -> T_Result:
        if self is FourHundredDetailsItemIssue.INVALID_PARAMETER_VALUE:
            return invalid_parameter_value()
