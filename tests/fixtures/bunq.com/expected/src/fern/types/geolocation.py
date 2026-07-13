

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Geolocation(UniversalBaseModel):
    altitude: typing.Optional[int] = pydantic.Field(default=None)
    """
    The altitude for a geolocation restriction.
    """

    latitude: typing.Optional[int] = pydantic.Field(default=None)
    """
    The latitude for a geolocation restriction.
    """

    longitude: typing.Optional[int] = pydantic.Field(default=None)
    """
    The longitude for a geolocation restriction.
    """

    radius: typing.Optional[int] = pydantic.Field(default=None)
    """
    The radius for a geolocation restriction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
