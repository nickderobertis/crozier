

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Coordinates(UniversalBaseModel):
    """
    Latitude and longitude coordinates.
    """

    latitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The latitude of the coordinate expressed in degrees.
    """

    longitude: typing.Optional[float] = pydantic.Field(default=None)
    """
    The longitude of the coordinate expressed in degrees.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
