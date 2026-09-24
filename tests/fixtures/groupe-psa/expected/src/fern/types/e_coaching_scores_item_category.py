

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ECoachingScoresItemCategory(enum.StrEnum):
    """
    category of the score. Global, ACCELERATION, BREAKING, A/C system, Runing cold engine, Direct Shift Gear, Speed, STT system, ZEV (Zero emission vehicle).
    """

    GLOBAL = "Global"
    ACCELERATION = "Acceleration"
    BREAK = "Break"
    AIR_CONDIONER = "AirCondioner"
    COLD_ENGINE = "ColdEngine"
    TIRE_PRESSURE = "TirePressure"
    SLOPE = "Slope"
    SPEED = "Speed"
    START_STOP = "StartStop"

    def visit(
        self,
        global_: typing.Callable[[], T_Result],
        acceleration: typing.Callable[[], T_Result],
        break_: typing.Callable[[], T_Result],
        air_condioner: typing.Callable[[], T_Result],
        cold_engine: typing.Callable[[], T_Result],
        tire_pressure: typing.Callable[[], T_Result],
        slope: typing.Callable[[], T_Result],
        speed: typing.Callable[[], T_Result],
        start_stop: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ECoachingScoresItemCategory.GLOBAL:
            return global_()
        if self is ECoachingScoresItemCategory.ACCELERATION:
            return acceleration()
        if self is ECoachingScoresItemCategory.BREAK:
            return break_()
        if self is ECoachingScoresItemCategory.AIR_CONDIONER:
            return air_condioner()
        if self is ECoachingScoresItemCategory.COLD_ENGINE:
            return cold_engine()
        if self is ECoachingScoresItemCategory.TIRE_PRESSURE:
            return tire_pressure()
        if self is ECoachingScoresItemCategory.SLOPE:
            return slope()
        if self is ECoachingScoresItemCategory.SPEED:
            return speed()
        if self is ECoachingScoresItemCategory.START_STOP:
            return start_stop()
