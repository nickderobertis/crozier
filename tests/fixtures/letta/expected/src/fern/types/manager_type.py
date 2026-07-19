

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ManagerType(enum.StrEnum):
    ROUND_ROBIN = "round_robin"
    SUPERVISOR = "supervisor"
    DYNAMIC = "dynamic"
    SLEEPTIME = "sleeptime"
    VOICE_SLEEPTIME = "voice_sleeptime"
    SWARM = "swarm"

    def visit(
        self,
        round_robin: typing.Callable[[], T_Result],
        supervisor: typing.Callable[[], T_Result],
        dynamic: typing.Callable[[], T_Result],
        sleeptime: typing.Callable[[], T_Result],
        voice_sleeptime: typing.Callable[[], T_Result],
        swarm: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ManagerType.ROUND_ROBIN:
            return round_robin()
        if self is ManagerType.SUPERVISOR:
            return supervisor()
        if self is ManagerType.DYNAMIC:
            return dynamic()
        if self is ManagerType.SLEEPTIME:
            return sleeptime()
        if self is ManagerType.VOICE_SLEEPTIME:
            return voice_sleeptime()
        if self is ManagerType.SWARM:
            return swarm()
