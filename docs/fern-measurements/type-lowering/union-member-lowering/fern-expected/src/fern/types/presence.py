

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Presence(enum.StrEnum):
    """
    Presence status
    """

    ONLINE = "Online"
    IDLE = "Idle"
    AWAY = "Away"
    BUSY = "Busy"

    def visit(
        self,
        online: typing.Callable[[], T_Result],
        idle: typing.Callable[[], T_Result],
        away: typing.Callable[[], T_Result],
        busy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Presence.ONLINE:
            return online()
        if self is Presence.IDLE:
            return idle()
        if self is Presence.AWAY:
            return away()
        if self is Presence.BUSY:
            return busy()
