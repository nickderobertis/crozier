

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weather_status_forecast_data_next6hours_details import WeatherStatusForecastDataNext6HoursDetails
from .weather_status_forecast_data_next12hours_summary import WeatherStatusForecastDataNext12HoursSummary


class WeatherStatusForecastDataNext6Hours(UniversalBaseModel):
    summary: WeatherStatusForecastDataNext12HoursSummary
    details: WeatherStatusForecastDataNext6HoursDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
