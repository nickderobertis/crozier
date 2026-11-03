

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sensor_reading_bench import SensorReadingBench
from .sensor_reading_channels_item import SensorReadingChannelsItem
from .sensor_reading_checks_item import SensorReadingChecksItem
from .window import Window


class PanelReading_Sensors(UniversalBaseModel):
    source: typing.Literal["sensors"] = "sensors"
    channels: typing.Optional[typing.List[SensorReadingChannelsItem]] = None
    window: typing.Optional[Window] = None
    bench: typing.Optional[SensorReadingBench] = None
    checks: typing.Optional[typing.List[SensorReadingChecksItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PanelReading_Forecast(UniversalBaseModel):
    source: typing.Literal["forecast"] = "forecast"
    days: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PanelReading = typing_extensions.Annotated[
    typing.Union[PanelReading_Sensors, PanelReading_Forecast], pydantic.Field(discriminator="source")
]
