

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .buoys_by_station import BuoysByStation
from .depths_by_station import DepthsByStation
from .soundings_by_station import SoundingsByStation
from .tide_grid import TideGrid


class StationBoard(UniversalBaseModel):
    depths: typing.Optional[DepthsByStation] = None
    buoys: typing.Optional[BuoysByStation] = None
    soundings: typing.Optional[SoundingsByStation] = None
    grid: typing.Optional[TideGrid] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
