

import typing

from .data_battery_cell_voltage_diff import DataBatteryCellVoltageDiff
from .data_battery_cell_voltage_high import DataBatteryCellVoltageHigh
from .data_battery_cell_voltage_low import DataBatteryCellVoltageLow
from .data_battery_current_high import DataBatteryCurrentHigh
from .data_battery_health_low import DataBatteryHealthLow
from .data_battery_percent_low import DataBatteryPercentLow
from .data_battery_temp_high import DataBatteryTempHigh
from .data_battery_voltage_high import DataBatteryVoltageHigh
from .data_battery_voltage_low import DataBatteryVoltageLow

AlarmData = typing.Union[
    DataBatteryVoltageLow,
    DataBatteryVoltageHigh,
    DataBatteryCellVoltageHigh,
    DataBatteryCellVoltageLow,
    DataBatteryCellVoltageDiff,
    DataBatteryCurrentHigh,
    DataBatteryTempHigh,
    DataBatteryPercentLow,
    DataBatteryHealthLow,
]
