

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RoomStatus(enum.StrEnum):
    """
    The allocation status of a room.

    `scheduling`: a process is not allocated yet and the room is waiting to be scheduled

    `active`: ready to accept connections

    `suspended`: room is unallocated from the process but can be rescheduled later with the same `roomId`

    `destroyed`: all associated metadata is deleted
    """

    SCHEDULING = "scheduling"
    ACTIVE = "active"
    SUSPENDED = "suspended"
    DESTROYED = "destroyed"

    def visit(
        self,
        scheduling: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        suspended: typing.Callable[[], T_Result],
        destroyed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RoomStatus.SCHEDULING:
            return scheduling()
        if self is RoomStatus.ACTIVE:
            return active()
        if self is RoomStatus.SUSPENDED:
            return suspended()
        if self is RoomStatus.DESTROYED:
            return destroyed()
