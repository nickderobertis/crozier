

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TrajectoryStationIn(UniversalBaseModel):
    azimuth: float
    dx: typing.Optional[float] = None
    dy: typing.Optional[float] = None
    dz: typing.Optional[float] = None
    inclination: float
    md: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
