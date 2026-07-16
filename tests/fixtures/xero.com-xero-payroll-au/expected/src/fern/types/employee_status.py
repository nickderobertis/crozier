

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmployeeStatus(str, enum.Enum):
    """
    Employee Status Types
    """

    ACTIVE = "ACTIVE"
    TERMINATED = "TERMINATED"

    def visit(self, active: typing.Callable[[], T_Result], terminated: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmployeeStatus.ACTIVE:
            return active()
        if self is EmployeeStatus.TERMINATED:
            return terminated()
