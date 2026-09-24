

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlarmType(enum.StrEnum):
    """
    The type of alarm
    """

    BATTERY_VOLTAGE_LOW = "battery_voltage_low"
    BATTERY_VOLTAGE_HIGH = "battery_voltage_high"
    BATTERY_CELL_VOLTAGE_HIGH = "battery_cell_voltage_high"
    BATTERY_CELL_VOLTAGE_LOW = "battery_cell_voltage_low"
    BATTERY_CELL_VOLTAGE_DIFF = "battery_cell_voltage_diff"
    BATTERY_CURRENT_HIGH = "battery_current_high"
    BATTERY_TEMP_HIGH = "battery_temp_high"
    BATTERY_PERCENT_LOW = "battery_percent_low"
    BATTERY_HEALTH_LOW = "battery_health_low"

    def visit(
        self,
        battery_voltage_low: typing.Callable[[], T_Result],
        battery_voltage_high: typing.Callable[[], T_Result],
        battery_cell_voltage_high: typing.Callable[[], T_Result],
        battery_cell_voltage_low: typing.Callable[[], T_Result],
        battery_cell_voltage_diff: typing.Callable[[], T_Result],
        battery_current_high: typing.Callable[[], T_Result],
        battery_temp_high: typing.Callable[[], T_Result],
        battery_percent_low: typing.Callable[[], T_Result],
        battery_health_low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlarmType.BATTERY_VOLTAGE_LOW:
            return battery_voltage_low()
        if self is AlarmType.BATTERY_VOLTAGE_HIGH:
            return battery_voltage_high()
        if self is AlarmType.BATTERY_CELL_VOLTAGE_HIGH:
            return battery_cell_voltage_high()
        if self is AlarmType.BATTERY_CELL_VOLTAGE_LOW:
            return battery_cell_voltage_low()
        if self is AlarmType.BATTERY_CELL_VOLTAGE_DIFF:
            return battery_cell_voltage_diff()
        if self is AlarmType.BATTERY_CURRENT_HIGH:
            return battery_current_high()
        if self is AlarmType.BATTERY_TEMP_HIGH:
            return battery_temp_high()
        if self is AlarmType.BATTERY_PERCENT_LOW:
            return battery_percent_low()
        if self is AlarmType.BATTERY_HEALTH_LOW:
            return battery_health_low()
