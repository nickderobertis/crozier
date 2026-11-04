

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weather_status_forecast_data_next1hours_details import WeatherStatusForecastDataNext1HoursDetails
from .weather_status_forecast_data_next12hours_summary import WeatherStatusForecastDataNext12HoursSummary


class WeatherStatusForecastDataNext1Hours(UniversalBaseModel):
    summary: WeatherStatusForecastDataNext12HoursSummary
    details: WeatherStatusForecastDataNext1HoursDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
