

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DashboardUserStatus(enum.StrEnum):
    """
    The current status of the user.
    """

    INVITED = "invited"
    ACTIVE = "active"
    DEACTIVATED = "deactivated"

    def visit(
        self,
        invited: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        deactivated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DashboardUserStatus.INVITED:
            return invited()
        if self is DashboardUserStatus.ACTIVE:
            return active()
        if self is DashboardUserStatus.DEACTIVATED:
            return deactivated()
