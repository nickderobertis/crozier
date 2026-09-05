

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RegionCordinates(UniversalBaseModel):
    """
    approximate longitude latitude of the region
    """

    latitude: typing.Optional[str] = pydantic.Field(default=None)
    """
    Approximate Latitude for the site location
    """

    longitude: typing.Optional[str] = pydantic.Field(default=None)
    """
    Approximate Longitude for the site location
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
