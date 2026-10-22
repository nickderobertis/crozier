

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserAccountRole(enum.StrEnum):
    """
    User role in the account
    """

    ADMINISTRATOR = "Administrator"
    DEVELOPER = "Developer"
    ANALYST = "Analyst"
    BILLING_MANAGER = "Billing Manager"

    def visit(
        self,
        administrator: typing.Callable[[], T_Result],
        developer: typing.Callable[[], T_Result],
        analyst: typing.Callable[[], T_Result],
        billing_manager: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserAccountRole.ADMINISTRATOR:
            return administrator()
        if self is UserAccountRole.DEVELOPER:
            return developer()
        if self is UserAccountRole.ANALYST:
            return analyst()
        if self is UserAccountRole.BILLING_MANAGER:
            return billing_manager()
