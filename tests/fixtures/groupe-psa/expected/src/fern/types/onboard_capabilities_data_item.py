

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesDataItem(enum.StrEnum):
    DATA_VEHICLE_DEVICES_PNC = "data:vehicle:devices:pnc"
    DATA_TELEMETRY = "data:telemetry"
    DATA_TELEMETRY_ENVIRONMENT = "data:telemetry:environment"
    DATA_TELEMETRY_PRIVACY = "data:telemetry:privacy"
    DATA_TELEMETRY_VEHICLE = "data:telemetry:vehicle"
    DATA_TELEMETRY_VEHICLE_IGNITION = "data:telemetry:vehicle:ignition"
    DATA_TELEMETRY_VEHICLE_PRECONDITIONING = "data:telemetry:vehicle:preconditioning"
    DATA_TELEMETRY_VEHICLE_ENERGIES = "data:telemetry:vehicle:energies"
    DATA_TELEMETRY_VEHICLE_ENGINES = "data:telemetry:vehicle:engines"
    DATA_TELEMETRY_VEHICLE_DOORS_STATE = "data:telemetry:vehicle:doorsState"
    DATA_TELEMETRY_VEHICLE_POWERTRAIN = "data:telemetry:vehicle:powertrain"
    DATA_TELEMETRY_VEHICLE_BATTERY = "data:telemetry:vehicle:battery"
    DATA_TELEMETRY_VEHICLE_SAFETY = "data:telemetry:vehicle:safety"
    DATA_TELEMETRY_VEHICLE_ODOMETER = "data:telemetry:vehicle:odometer"
    DATA_TELEMETRY_VEHICLE_KINETIC = "data:telemetry:vehicle:kinetic"
    DATA_TELEMETRY_VEHICLE_TRANSMISSION = "data:telemetry:vehicle:transmission"
    DATA_TELEMETRY_VEHICLE_ADAS = "data:telemetry:vehicle:adas"
    DATA_TELEMETRY_VEHICLE_LIGHTING_SYSTEM = "data:telemetry:vehicle:lightingSystem"
    DATA_TELEMETRY_VEHICLE_MAINTENANCE = "data:telemetry:vehicle:maintenance"
    DATA_TELEMETRY_VEHICLE_DRIVING_BEHAVIOR = "data:telemetry:vehicle:drivingBehavior"
    DATA_TELEMETRY_VEHICLE_WIPING_BLADES = "data:telemetry:vehicle:wipingBlades"
    DATA_TELEMETRY_VEHICLE_ALARM = "data:telemetry:vehicle:alarm"
    DATA_POSITION = "data:position"
    DATA_TRIP = "data:trip"
    DATA_ALERT = "data:alert"
    DATA_COLLISION = "data:collision"

    def visit(
        self,
        data_vehicle_devices_pnc: typing.Callable[[], T_Result],
        data_telemetry: typing.Callable[[], T_Result],
        data_telemetry_environment: typing.Callable[[], T_Result],
        data_telemetry_privacy: typing.Callable[[], T_Result],
        data_telemetry_vehicle: typing.Callable[[], T_Result],
        data_telemetry_vehicle_ignition: typing.Callable[[], T_Result],
        data_telemetry_vehicle_preconditioning: typing.Callable[[], T_Result],
        data_telemetry_vehicle_energies: typing.Callable[[], T_Result],
        data_telemetry_vehicle_engines: typing.Callable[[], T_Result],
        data_telemetry_vehicle_doors_state: typing.Callable[[], T_Result],
        data_telemetry_vehicle_powertrain: typing.Callable[[], T_Result],
        data_telemetry_vehicle_battery: typing.Callable[[], T_Result],
        data_telemetry_vehicle_safety: typing.Callable[[], T_Result],
        data_telemetry_vehicle_odometer: typing.Callable[[], T_Result],
        data_telemetry_vehicle_kinetic: typing.Callable[[], T_Result],
        data_telemetry_vehicle_transmission: typing.Callable[[], T_Result],
        data_telemetry_vehicle_adas: typing.Callable[[], T_Result],
        data_telemetry_vehicle_lighting_system: typing.Callable[[], T_Result],
        data_telemetry_vehicle_maintenance: typing.Callable[[], T_Result],
        data_telemetry_vehicle_driving_behavior: typing.Callable[[], T_Result],
        data_telemetry_vehicle_wiping_blades: typing.Callable[[], T_Result],
        data_telemetry_vehicle_alarm: typing.Callable[[], T_Result],
        data_position: typing.Callable[[], T_Result],
        data_trip: typing.Callable[[], T_Result],
        data_alert: typing.Callable[[], T_Result],
        data_collision: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OnboardCapabilitiesDataItem.DATA_VEHICLE_DEVICES_PNC:
            return data_vehicle_devices_pnc()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY:
            return data_telemetry()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_ENVIRONMENT:
            return data_telemetry_environment()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_PRIVACY:
            return data_telemetry_privacy()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE:
            return data_telemetry_vehicle()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_IGNITION:
            return data_telemetry_vehicle_ignition()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_PRECONDITIONING:
            return data_telemetry_vehicle_preconditioning()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_ENERGIES:
            return data_telemetry_vehicle_energies()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_ENGINES:
            return data_telemetry_vehicle_engines()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_DOORS_STATE:
            return data_telemetry_vehicle_doors_state()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_POWERTRAIN:
            return data_telemetry_vehicle_powertrain()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_BATTERY:
            return data_telemetry_vehicle_battery()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_SAFETY:
            return data_telemetry_vehicle_safety()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_ODOMETER:
            return data_telemetry_vehicle_odometer()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_KINETIC:
            return data_telemetry_vehicle_kinetic()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_TRANSMISSION:
            return data_telemetry_vehicle_transmission()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_ADAS:
            return data_telemetry_vehicle_adas()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_LIGHTING_SYSTEM:
            return data_telemetry_vehicle_lighting_system()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_MAINTENANCE:
            return data_telemetry_vehicle_maintenance()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_DRIVING_BEHAVIOR:
            return data_telemetry_vehicle_driving_behavior()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_WIPING_BLADES:
            return data_telemetry_vehicle_wiping_blades()
        if self is OnboardCapabilitiesDataItem.DATA_TELEMETRY_VEHICLE_ALARM:
            return data_telemetry_vehicle_alarm()
        if self is OnboardCapabilitiesDataItem.DATA_POSITION:
            return data_position()
        if self is OnboardCapabilitiesDataItem.DATA_TRIP:
            return data_trip()
        if self is OnboardCapabilitiesDataItem.DATA_ALERT:
            return data_alert()
        if self is OnboardCapabilitiesDataItem.DATA_COLLISION:
            return data_collision()
