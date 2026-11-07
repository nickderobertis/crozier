

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServiceRequirementForUserConnectionStatus(enum.StrEnum):
    """
    User's current connection status with this service
    """

    CONNECTED = "connected"
    NOT_CONNECTED = "not_connected"

    def visit(self, connected: typing.Callable[[], T_Result], not_connected: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServiceRequirementForUserConnectionStatus.CONNECTED:
            return connected()
        if self is ServiceRequirementForUserConnectionStatus.NOT_CONNECTED:
            return not_connected()
