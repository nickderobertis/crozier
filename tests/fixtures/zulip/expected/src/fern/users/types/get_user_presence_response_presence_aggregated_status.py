

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetUserPresenceResponsePresenceAggregatedStatus(enum.StrEnum):
    """
    The status of the user. Will be either `"idle"`,
    `"active"`, or `"offline"`.
    """

    IDLE = "idle"
    ACTIVE = "active"
    OFFLINE = "offline"

    def visit(
        self,
        idle: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        offline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetUserPresenceResponsePresenceAggregatedStatus.IDLE:
            return idle()
        if self is GetUserPresenceResponsePresenceAggregatedStatus.ACTIVE:
            return active()
        if self is GetUserPresenceResponsePresenceAggregatedStatus.OFFLINE:
            return offline()
