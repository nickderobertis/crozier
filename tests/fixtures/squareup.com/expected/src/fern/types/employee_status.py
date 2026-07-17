

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmployeeStatus(enum.StrEnum):
    """
    The status of the Employee being retrieved.
    """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is EmployeeStatus.ACTIVE:
            return active()
        if self is EmployeeStatus.INACTIVE:
            return inactive()
