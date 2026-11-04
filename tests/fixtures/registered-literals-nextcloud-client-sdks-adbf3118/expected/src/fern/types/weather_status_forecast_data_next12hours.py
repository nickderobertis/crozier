

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .weather_status_forecast_data_next12hours_details import WeatherStatusForecastDataNext12HoursDetails
from .weather_status_forecast_data_next12hours_summary import WeatherStatusForecastDataNext12HoursSummary


class WeatherStatusForecastDataNext12Hours(UniversalBaseModel):
    summary: WeatherStatusForecastDataNext12HoursSummary
    details: WeatherStatusForecastDataNext12HoursDetails

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
