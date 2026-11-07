

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weather_status_forecast_data_instant_details import WeatherStatusForecastDataInstantDetails


class WeatherStatusForecastDataInstant(UniversalBaseModel):
    details: WeatherStatusForecastDataInstantDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
