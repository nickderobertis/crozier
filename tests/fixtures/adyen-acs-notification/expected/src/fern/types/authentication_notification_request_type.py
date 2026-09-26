

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AuthenticationNotificationRequestType(enum.StrEnum):
    """
    Type of notification.
    """

    BALANCE_PLATFORM_AUTHENTICATION_CREATED = "balancePlatform.authentication.created"

    def visit(self, balance_platform_authentication_created: typing.Callable[[], T_Result]) -> T_Result:
        if self is AuthenticationNotificationRequestType.BALANCE_PLATFORM_AUTHENTICATION_CREATED:
            return balance_platform_authentication_created()
