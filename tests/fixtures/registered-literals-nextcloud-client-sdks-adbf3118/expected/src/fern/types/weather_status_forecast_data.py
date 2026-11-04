

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .weather_status_forecast_data_instant import WeatherStatusForecastDataInstant
from .weather_status_forecast_data_next1hours import WeatherStatusForecastDataNext1Hours
from .weather_status_forecast_data_next6hours import WeatherStatusForecastDataNext6Hours
from .weather_status_forecast_data_next12hours import WeatherStatusForecastDataNext12Hours


class WeatherStatusForecastData(UniversalBaseModel):
    instant: WeatherStatusForecastDataInstant
    next12hours: typing_extensions.Annotated[
        WeatherStatusForecastDataNext12Hours,
        FieldMetadata(alias="next_12_hours"),
        pydantic.Field(alias="next_12_hours"),
    ]
    next1hours: typing_extensions.Annotated[
        WeatherStatusForecastDataNext1Hours, FieldMetadata(alias="next_1_hours"), pydantic.Field(alias="next_1_hours")
    ]
    next6hours: typing_extensions.Annotated[
        WeatherStatusForecastDataNext6Hours, FieldMetadata(alias="next_6_hours"), pydantic.Field(alias="next_6_hours")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
