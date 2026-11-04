

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weather_status_weather_status_use_personal_address200response_ocs import (
    WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcs,
)


class WeatherStatusWeatherStatusUsePersonalAddress200Response(UniversalBaseModel):
    ocs: WeatherStatusWeatherStatusUsePersonalAddress200ResponseOcs

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
