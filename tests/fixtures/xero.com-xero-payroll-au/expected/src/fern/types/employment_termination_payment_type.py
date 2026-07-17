

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmploymentTerminationPaymentType(enum.StrEnum):
    O = "O"
    R = "R"

    def visit(self, o: typing.Callable[[], T_Result], r: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmploymentTerminationPaymentType.O:
            return o()
        if self is EmploymentTerminationPaymentType.R:
            return r()
