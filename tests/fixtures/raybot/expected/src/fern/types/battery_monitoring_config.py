

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .battery_cell_voltage_diff_config import BatteryCellVoltageDiffConfig
from .battery_cell_voltage_high_config import BatteryCellVoltageHighConfig
from .battery_cell_voltage_low_config import BatteryCellVoltageLowConfig
from .battery_current_high_config import BatteryCurrentHighConfig
from .battery_health_low_config import BatteryHealthLowConfig
from .battery_percent_low_config import BatteryPercentLowConfig
from .battery_temp_high_config import BatteryTempHighConfig
from .battery_voltage_high_config import BatteryVoltageHighConfig
from .battery_voltage_low_config import BatteryVoltageLowConfig


class BatteryMonitoringConfig(UniversalBaseModel):
    voltage_low: typing_extensions.Annotated[
        BatteryVoltageLowConfig, FieldMetadata(alias="voltageLow"), pydantic.Field(alias="voltageLow")
    ]
    voltage_high: typing_extensions.Annotated[
        BatteryVoltageHighConfig, FieldMetadata(alias="voltageHigh"), pydantic.Field(alias="voltageHigh")
    ]
    cell_voltage_high: typing_extensions.Annotated[
        BatteryCellVoltageHighConfig, FieldMetadata(alias="cellVoltageHigh"), pydantic.Field(alias="cellVoltageHigh")
    ]
    cell_voltage_low: typing_extensions.Annotated[
        BatteryCellVoltageLowConfig, FieldMetadata(alias="cellVoltageLow"), pydantic.Field(alias="cellVoltageLow")
    ]
    cell_voltage_diff: typing_extensions.Annotated[
        BatteryCellVoltageDiffConfig, FieldMetadata(alias="cellVoltageDiff"), pydantic.Field(alias="cellVoltageDiff")
    ]
    current_high: typing_extensions.Annotated[
        BatteryCurrentHighConfig, FieldMetadata(alias="currentHigh"), pydantic.Field(alias="currentHigh")
    ]
    temp_high: typing_extensions.Annotated[
        BatteryTempHighConfig, FieldMetadata(alias="tempHigh"), pydantic.Field(alias="tempHigh")
    ]
    percent_low: typing_extensions.Annotated[
        BatteryPercentLowConfig, FieldMetadata(alias="percentLow"), pydantic.Field(alias="percentLow")
    ]
    health_low: typing_extensions.Annotated[
        BatteryHealthLowConfig, FieldMetadata(alias="healthLow"), pydantic.Field(alias="healthLow")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
