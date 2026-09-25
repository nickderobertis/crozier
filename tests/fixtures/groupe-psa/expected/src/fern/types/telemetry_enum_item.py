

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TelemetryEnumItem(enum.StrEnum):
    ENVIRONMENT = "environment"
    PRIVACY = "privacy"
    VEHICLE = "vehicle"
    VEHICLE_ADAS = "vehicle.adas"
    VEHICLE_BATTERY = "vehicle.battery"
    VEHICLE_DOORS_STATE = "vehicle.doorsState"
    VEHICLE_ENERGIES = "vehicle.energies"
    VEHICLE_ENGINES = "vehicle.engines"
    VEHICLE_IGNITION = "vehicle.ignition"
    VEHICLE_LIGHTING = "vehicle.lighting"
    VEHICLE_LIGHTING_SYSTEM = "vehicle.lightingSystem"
    VEHICLE_SAFETY = "vehicle.safety"
    VEHICLE_TRANSMISSION = "vehicle.transmission"
    VEHICLE_DRIVING_BEHAVIOR = "vehicle.drivingBehavior"
    VEHICLE_ALARM_STATUS = "vehicle.alarm.status"
    VEHICLE_ALARM_TRIGGER = "vehicle.alarm.trigger"
    VEHICLE_WIPING_BLADES = "vehicle.wipingBlades"

    def visit(
        self,
        environment: typing.Callable[[], T_Result],
        privacy: typing.Callable[[], T_Result],
        vehicle: typing.Callable[[], T_Result],
        vehicle_adas: typing.Callable[[], T_Result],
        vehicle_battery: typing.Callable[[], T_Result],
        vehicle_doors_state: typing.Callable[[], T_Result],
        vehicle_energies: typing.Callable[[], T_Result],
        vehicle_engines: typing.Callable[[], T_Result],
        vehicle_ignition: typing.Callable[[], T_Result],
        vehicle_lighting: typing.Callable[[], T_Result],
        vehicle_lighting_system: typing.Callable[[], T_Result],
        vehicle_safety: typing.Callable[[], T_Result],
        vehicle_transmission: typing.Callable[[], T_Result],
        vehicle_driving_behavior: typing.Callable[[], T_Result],
        vehicle_alarm_status: typing.Callable[[], T_Result],
        vehicle_alarm_trigger: typing.Callable[[], T_Result],
        vehicle_wiping_blades: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TelemetryEnumItem.ENVIRONMENT:
            return environment()
        if self is TelemetryEnumItem.PRIVACY:
            return privacy()
        if self is TelemetryEnumItem.VEHICLE:
            return vehicle()
        if self is TelemetryEnumItem.VEHICLE_ADAS:
            return vehicle_adas()
        if self is TelemetryEnumItem.VEHICLE_BATTERY:
            return vehicle_battery()
        if self is TelemetryEnumItem.VEHICLE_DOORS_STATE:
            return vehicle_doors_state()
        if self is TelemetryEnumItem.VEHICLE_ENERGIES:
            return vehicle_energies()
        if self is TelemetryEnumItem.VEHICLE_ENGINES:
            return vehicle_engines()
        if self is TelemetryEnumItem.VEHICLE_IGNITION:
            return vehicle_ignition()
        if self is TelemetryEnumItem.VEHICLE_LIGHTING:
            return vehicle_lighting()
        if self is TelemetryEnumItem.VEHICLE_LIGHTING_SYSTEM:
            return vehicle_lighting_system()
        if self is TelemetryEnumItem.VEHICLE_SAFETY:
            return vehicle_safety()
        if self is TelemetryEnumItem.VEHICLE_TRANSMISSION:
            return vehicle_transmission()
        if self is TelemetryEnumItem.VEHICLE_DRIVING_BEHAVIOR:
            return vehicle_driving_behavior()
        if self is TelemetryEnumItem.VEHICLE_ALARM_STATUS:
            return vehicle_alarm_status()
        if self is TelemetryEnumItem.VEHICLE_ALARM_TRIGGER:
            return vehicle_alarm_trigger()
        if self is TelemetryEnumItem.VEHICLE_WIPING_BLADES:
            return vehicle_wiping_blades()
