

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class EmployeesFilterEmploymentStatus(enum.StrEnum):
    """
    Employment status to filter on
    """

    ACTIVE = "active"
    INACTIVE = "inactive"
    TERMINATED = "terminated"
    OTHER = "other"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
        terminated: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmployeesFilterEmploymentStatus.ACTIVE:
            return active()
        if self is EmployeesFilterEmploymentStatus.INACTIVE:
            return inactive()
        if self is EmployeesFilterEmploymentStatus.TERMINATED:
            return terminated()
        if self is EmployeesFilterEmploymentStatus.OTHER:
            return other()
