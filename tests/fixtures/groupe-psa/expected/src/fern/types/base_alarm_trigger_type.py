

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BaseAlarmTriggerType(enum.StrEnum):
    """
    Define the vehicle break-in type.
    """

    NO_BREAK_IN = "NoBreakIn"
    FRONT_RIGHT_DOOR_BREAK_IN = "FrontRightDoorBreakIn"
    FRONT_LEFT_DOOR_BREAK_IN = "FrontLeftDoorBreakIn"
    REAR_RIGHT_FRONT_DOOR_BREAK_IN = "RearRightFrontDoorBreakIn"
    REAR_LEFT_FRONT_DOOR_BREAK_IN = "RearLeftFrontDoorBreakIn"
    HOOD_DOOR_BREAK_IN = "HoodDoorBreakIn"
    TRUNK_DOOR_BREAK_IN = "TrunkDoorBreakIn"
    BACKLITE_DOOR_BREAK_IN = "BackliteDoorBreakIn"
    ROOF_BREAK_IN = "RoofBreakIn"
    VOLUMETRIC_BREAK_IN = "VolumetricBreakIn"
    VEHICLE_LIFTING = "VehicleLifting"
    ELECTRICALSYSTEM_BREAK_IN = "ElectricalsystemBreakIn"
    KEY_LEARNING = "KeyLearning"
    UNAUTHENTICATED_STARTUP = "UnauthenticatedStartup"

    def visit(
        self,
        no_break_in: typing.Callable[[], T_Result],
        front_right_door_break_in: typing.Callable[[], T_Result],
        front_left_door_break_in: typing.Callable[[], T_Result],
        rear_right_front_door_break_in: typing.Callable[[], T_Result],
        rear_left_front_door_break_in: typing.Callable[[], T_Result],
        hood_door_break_in: typing.Callable[[], T_Result],
        trunk_door_break_in: typing.Callable[[], T_Result],
        backlite_door_break_in: typing.Callable[[], T_Result],
        roof_break_in: typing.Callable[[], T_Result],
        volumetric_break_in: typing.Callable[[], T_Result],
        vehicle_lifting: typing.Callable[[], T_Result],
        electricalsystem_break_in: typing.Callable[[], T_Result],
        key_learning: typing.Callable[[], T_Result],
        unauthenticated_startup: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BaseAlarmTriggerType.NO_BREAK_IN:
            return no_break_in()
        if self is BaseAlarmTriggerType.FRONT_RIGHT_DOOR_BREAK_IN:
            return front_right_door_break_in()
        if self is BaseAlarmTriggerType.FRONT_LEFT_DOOR_BREAK_IN:
            return front_left_door_break_in()
        if self is BaseAlarmTriggerType.REAR_RIGHT_FRONT_DOOR_BREAK_IN:
            return rear_right_front_door_break_in()
        if self is BaseAlarmTriggerType.REAR_LEFT_FRONT_DOOR_BREAK_IN:
            return rear_left_front_door_break_in()
        if self is BaseAlarmTriggerType.HOOD_DOOR_BREAK_IN:
            return hood_door_break_in()
        if self is BaseAlarmTriggerType.TRUNK_DOOR_BREAK_IN:
            return trunk_door_break_in()
        if self is BaseAlarmTriggerType.BACKLITE_DOOR_BREAK_IN:
            return backlite_door_break_in()
        if self is BaseAlarmTriggerType.ROOF_BREAK_IN:
            return roof_break_in()
        if self is BaseAlarmTriggerType.VOLUMETRIC_BREAK_IN:
            return volumetric_break_in()
        if self is BaseAlarmTriggerType.VEHICLE_LIFTING:
            return vehicle_lifting()
        if self is BaseAlarmTriggerType.ELECTRICALSYSTEM_BREAK_IN:
            return electricalsystem_break_in()
        if self is BaseAlarmTriggerType.KEY_LEARNING:
            return key_learning()
        if self is BaseAlarmTriggerType.UNAUTHENTICATED_STARTUP:
            return unauthenticated_startup()
