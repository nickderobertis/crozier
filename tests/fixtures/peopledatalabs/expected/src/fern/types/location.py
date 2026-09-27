

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .location_continent import LocationContinent
from .location_country import LocationCountry


class Location(UniversalBaseModel):
    geo: typing.Optional[str] = pydantic.Field(default=None)
    """
    the geo of the location
    """

    subregion: typing.Optional[str] = pydantic.Field(default=None)
    """
    the subregion of the location
    """

    continent: typing.Optional[LocationContinent] = pydantic.Field(default=None)
    """
    the canonical continent of the location
    """

    locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    the locality of the location
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the canonical name of the location
    """

    country: typing.Optional[LocationCountry] = pydantic.Field(default=None)
    """
    the canonical country of the location
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    the region of the location
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    locality
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
