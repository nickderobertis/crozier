

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class V1ListEmployeesRequestStatus(enum.StrEnum):
    """ """

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is V1ListEmployeesRequestStatus.ACTIVE:
            return active()
        if self is V1ListEmployeesRequestStatus.INACTIVE:
            return inactive()
