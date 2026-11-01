

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .berth import Berth
from .crossing_days_item import CrossingDaysItem
from .crossing_deck import CrossingDeck
from .crossing_weather import CrossingWeather
from .vessel import Vessel


class Crossing(UniversalBaseModel):
    days: typing.Optional[typing.List[CrossingDaysItem]] = None
    weather: typing.Optional[CrossingWeather] = pydantic.Field(default=None)
    """
    
    """

    deck: typing.Optional[CrossingDeck] = pydantic.Field(default=None)
    """
     
    """

    vessel: typing.Optional[Vessel] = None
    berth: typing.Optional[Berth] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
