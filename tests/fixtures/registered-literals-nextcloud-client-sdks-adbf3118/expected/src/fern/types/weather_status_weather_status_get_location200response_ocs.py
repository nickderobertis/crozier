

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ocs_meta import OcsMeta
from .weather_status_weather_status_get_location200response_ocs_data import (
    WeatherStatusWeatherStatusGetLocation200ResponseOcsData,
)


class WeatherStatusWeatherStatusGetLocation200ResponseOcs(UniversalBaseModel):
    meta: OcsMeta
    data: WeatherStatusWeatherStatusGetLocation200ResponseOcsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
