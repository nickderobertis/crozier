

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weather_status_weather_status_get_forecast200response_ocs import (
    WeatherStatusWeatherStatusGetForecast200ResponseOcs,
)


class WeatherStatusWeatherStatusGetForecast200Response(UniversalBaseModel):
    ocs: WeatherStatusWeatherStatusGetForecast200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
