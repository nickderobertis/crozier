

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetUserPresenceResponsePresenceWebsiteStatus(enum.StrEnum):
    """
    The status of the user. Will be either `"idle"` or
    `"active"`.
    """

    IDLE = "idle"
    ACTIVE = "active"

    def visit(self, idle: typing.Callable[[], T_Result], active: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetUserPresenceResponsePresenceWebsiteStatus.IDLE:
            return idle()
        if self is GetUserPresenceResponsePresenceWebsiteStatus.ACTIVE:
            return active()
