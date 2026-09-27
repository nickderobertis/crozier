

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RelayedAuthenticationRequestType(enum.StrEnum):
    """
    Type of notification.
    """

    BALANCE_PLATFORM_AUTHENTICATION_RELAYED = "balancePlatform.authentication.relayed"

    def visit(self, balance_platform_authentication_relayed: typing.Callable[[], T_Result]) -> T_Result:
        if self is RelayedAuthenticationRequestType.BALANCE_PLATFORM_AUTHENTICATION_RELAYED:
            return balance_platform_authentication_relayed()
