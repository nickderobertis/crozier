

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WeatherStatusForecastDataNext1HoursDetails(UniversalBaseModel):
    precipitation_amount: float
    precipitation_amount_max: float
    precipitation_amount_min: float
    probability_of_precipitation: float
    probability_of_thunder: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
