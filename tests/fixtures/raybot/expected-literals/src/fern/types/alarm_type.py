

import typing

AlarmType = typing.Union[
    typing.Literal[
        "battery_voltage_low",
        "battery_voltage_high",
        "battery_cell_voltage_high",
        "battery_cell_voltage_low",
        "battery_cell_voltage_diff",
        "battery_current_high",
        "battery_temp_high",
        "battery_percent_low",
        "battery_health_low",
    ],
    typing.Any,
]
