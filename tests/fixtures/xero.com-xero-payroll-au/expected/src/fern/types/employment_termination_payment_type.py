

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmploymentTerminationPaymentType(str, enum.Enum):
    O = "O"
    R = "R"

    def visit(self, o: typing.Callable[[], T_Result], r: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmploymentTerminationPaymentType.O:
            return o()
        if self is EmploymentTerminationPaymentType.R:
            return r()
