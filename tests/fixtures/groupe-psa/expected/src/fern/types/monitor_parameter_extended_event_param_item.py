

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MonitorParameterExtendedEventParamItem(enum.StrEnum):
    VEHICLE_DOORS_STATE = "vehicle.doorsState"
    VEHICLE_STATUS = "vehicle.status"
    VEHICLE_MAINTENANCE = "vehicle.maintenance"
    VEHICLE_POSITION = "vehicle.position"
    VEHICLE_TELEMETRY = "vehicle.telemetry"
    VEHICLE_ALERTS = "vehicle.alerts"
    VEHICLE_COLLISIONS = "vehicle.collisions"
    VEHICLE_TRIP = "vehicle.trip"
    VEHICLE_STOLEN = "vehicle.stolen"

    def visit(
        self,
        vehicle_doors_state: typing.Callable[[], T_Result],
        vehicle_status: typing.Callable[[], T_Result],
        vehicle_maintenance: typing.Callable[[], T_Result],
        vehicle_position: typing.Callable[[], T_Result],
        vehicle_telemetry: typing.Callable[[], T_Result],
        vehicle_alerts: typing.Callable[[], T_Result],
        vehicle_collisions: typing.Callable[[], T_Result],
        vehicle_trip: typing.Callable[[], T_Result],
        vehicle_stolen: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_DOORS_STATE:
            return vehicle_doors_state()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_STATUS:
            return vehicle_status()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_MAINTENANCE:
            return vehicle_maintenance()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_POSITION:
            return vehicle_position()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_TELEMETRY:
            return vehicle_telemetry()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_ALERTS:
            return vehicle_alerts()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_COLLISIONS:
            return vehicle_collisions()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_TRIP:
            return vehicle_trip()
        if self is MonitorParameterExtendedEventParamItem.VEHICLE_STOLEN:
            return vehicle_stolen()
