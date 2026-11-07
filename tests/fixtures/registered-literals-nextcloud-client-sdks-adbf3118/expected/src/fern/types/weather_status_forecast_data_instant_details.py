

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WeatherStatusForecastDataInstantDetails(UniversalBaseModel):
    air_pressure_at_sea_level: float
    air_temperature: float
    cloud_area_fraction: float
    cloud_area_fraction_high: float
    cloud_area_fraction_low: float
    cloud_area_fraction_medium: float
    dew_point_temperature: float
    fog_area_fraction: float
    relative_humidity: float
    ultraviolet_index_clear_sky: float
    wind_from_direction: float
    wind_speed: float
    wind_speed_of_gust: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
