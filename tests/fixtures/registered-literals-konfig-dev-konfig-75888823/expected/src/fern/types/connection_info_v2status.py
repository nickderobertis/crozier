

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConnectionInfoV2Status(enum.StrEnum):
    """
    `exposedPort` will only be available when the `status` of a room is "active".
    """

    STARTING = "starting"
    ACTIVE = "active"

    def visit(self, starting: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is ConnectionInfoV2Status.STARTING:
            return starting()
        if self is ConnectionInfoV2Status.ACTIVE:
            return active()
