

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserType(enum.StrEnum):
    """
    Type of the user account.
    """

    USER = "user"
    MANAGED_USER = "managed_user"
    SERVICE_ACCOUNT = "service_account"
    SYSTEM_ACCOUNT = "system_account"

    def visit(
        self,
        user: typing.Callable[[], T_Result],
        managed_user: typing.Callable[[], T_Result],
        service_account: typing.Callable[[], T_Result],
        system_account: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UserType.USER:
            return user()
        if self is UserType.MANAGED_USER:
            return managed_user()
        if self is UserType.SERVICE_ACCOUNT:
            return service_account()
        if self is UserType.SYSTEM_ACCOUNT:
            return system_account()
