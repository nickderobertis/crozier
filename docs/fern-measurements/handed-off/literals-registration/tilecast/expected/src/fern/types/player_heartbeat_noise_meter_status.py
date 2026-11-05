

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PlayerHeartbeatNoiseMeterStatus(enum.StrEnum):
    ACTIVE = "active"
    NORMAL = "normal"
    LOUD = "loud"
    UNAVAILABLE = "unavailable"
    INACTIVE = "inactive"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        normal: typing.Callable[[], T_Result],
        loud: typing.Callable[[], T_Result],
        unavailable: typing.Callable[[], T_Result],
        inactive: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PlayerHeartbeatNoiseMeterStatus.ACTIVE:
            return active()
        if self is PlayerHeartbeatNoiseMeterStatus.NORMAL:
            return normal()
        if self is PlayerHeartbeatNoiseMeterStatus.LOUD:
            return loud()
        if self is PlayerHeartbeatNoiseMeterStatus.UNAVAILABLE:
            return unavailable()
        if self is PlayerHeartbeatNoiseMeterStatus.INACTIVE:
            return inactive()
