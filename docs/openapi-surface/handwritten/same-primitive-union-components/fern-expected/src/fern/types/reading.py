

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gauge_channel_two import GaugeChannelTwo
from .station_code_one import StationCodeOne


class Reading(UniversalBaseModel):
    reading_id: str
    station_code: typing.Optional[StationCodeOne] = None
    channel: typing.Optional[GaugeChannelTwo] = None
    level_cm: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
