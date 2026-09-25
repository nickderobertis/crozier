

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RemoteType(enum.StrEnum):
    THERMAL_PRECONDITIONING = "ThermalPreconditioning"
    ELECTRIC_BATTERY_CHARGING_REQUEST = "ElectricBatteryChargingRequest"
    HORN = "Horn"
    DOORS = "Doors"
    LIGHTS = "Lights"
    IMMOBILIZATION = "Immobilization"
    STOLEN = "Stolen"
    WAKE_UP = "WakeUp"
    NAVIGATION = "Navigation"

    def visit(
        self,
        thermal_preconditioning: typing.Callable[[], T_Result],
        electric_battery_charging_request: typing.Callable[[], T_Result],
        horn: typing.Callable[[], T_Result],
        doors: typing.Callable[[], T_Result],
        lights: typing.Callable[[], T_Result],
        immobilization: typing.Callable[[], T_Result],
        stolen: typing.Callable[[], T_Result],
        wake_up: typing.Callable[[], T_Result],
        navigation: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RemoteType.THERMAL_PRECONDITIONING:
            return thermal_preconditioning()
        if self is RemoteType.ELECTRIC_BATTERY_CHARGING_REQUEST:
            return electric_battery_charging_request()
        if self is RemoteType.HORN:
            return horn()
        if self is RemoteType.DOORS:
            return doors()
        if self is RemoteType.LIGHTS:
            return lights()
        if self is RemoteType.IMMOBILIZATION:
            return immobilization()
        if self is RemoteType.STOLEN:
            return stolen()
        if self is RemoteType.WAKE_UP:
            return wake_up()
        if self is RemoteType.NAVIGATION:
            return navigation()
