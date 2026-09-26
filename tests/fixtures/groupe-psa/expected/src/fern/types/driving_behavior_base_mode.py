

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DrivingBehaviorBaseMode(enum.StrEnum):
    """
    Driving mode by driver selection
    """

    NORMAL = "Normal"
    SPORT = "Sport"
    COMFORT = "Comfort"
    ECO = "Eco"
    SAND = "Sand"
    MUD = "Mud"
    SNOW = "Snow"
    ZEV = "ZEV"
    HYBRID = "Hybrid"
    ZEV_ECO = "ZEVEco"
    HYBRID_ECO = "HybridEco"
    ECO_PLUS = "EcoPlus"
    E_AWD = "eAWD"
    FOUR_AWD = "4AWD"
    REINFORCED_LOAD = "ReinforcedLoad"

    def visit(
        self,
        normal: typing.Callable[[], T_Result],
        sport: typing.Callable[[], T_Result],
        comfort: typing.Callable[[], T_Result],
        eco: typing.Callable[[], T_Result],
        sand: typing.Callable[[], T_Result],
        mud: typing.Callable[[], T_Result],
        snow: typing.Callable[[], T_Result],
        zev: typing.Callable[[], T_Result],
        hybrid: typing.Callable[[], T_Result],
        zev_eco: typing.Callable[[], T_Result],
        hybrid_eco: typing.Callable[[], T_Result],
        eco_plus: typing.Callable[[], T_Result],
        e_awd: typing.Callable[[], T_Result],
        four_awd: typing.Callable[[], T_Result],
        reinforced_load: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DrivingBehaviorBaseMode.NORMAL:
            return normal()
        if self is DrivingBehaviorBaseMode.SPORT:
            return sport()
        if self is DrivingBehaviorBaseMode.COMFORT:
            return comfort()
        if self is DrivingBehaviorBaseMode.ECO:
            return eco()
        if self is DrivingBehaviorBaseMode.SAND:
            return sand()
        if self is DrivingBehaviorBaseMode.MUD:
            return mud()
        if self is DrivingBehaviorBaseMode.SNOW:
            return snow()
        if self is DrivingBehaviorBaseMode.ZEV:
            return zev()
        if self is DrivingBehaviorBaseMode.HYBRID:
            return hybrid()
        if self is DrivingBehaviorBaseMode.ZEV_ECO:
            return zev_eco()
        if self is DrivingBehaviorBaseMode.HYBRID_ECO:
            return hybrid_eco()
        if self is DrivingBehaviorBaseMode.ECO_PLUS:
            return eco_plus()
        if self is DrivingBehaviorBaseMode.E_AWD:
            return e_awd()
        if self is DrivingBehaviorBaseMode.FOUR_AWD:
            return four_awd()
        if self is DrivingBehaviorBaseMode.REINFORCED_LOAD:
            return reinforced_load()
