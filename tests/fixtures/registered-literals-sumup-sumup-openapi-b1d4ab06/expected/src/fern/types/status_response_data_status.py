

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusResponseDataStatus(enum.StrEnum):
    """
    Status of a device
    """

    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

    def visit(self, online: typing.Callable[[], T_Result], offline: typing.Callable[[], T_Result]) -> T_Result:
        if self is StatusResponseDataStatus.ONLINE:
            return online()
        if self is StatusResponseDataStatus.OFFLINE:
            return offline()
