

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .school_location_continent import SchoolLocationContinent
from .school_location_country import SchoolLocationCountry


class SchoolLocation(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The canonical name of the location associated with the school
    """

    locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The locality associated with the school
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region associated with the school
    """

    country: typing.Optional[SchoolLocationCountry] = pydantic.Field(default=None)
    """
    The country associated with the school
    """

    continent: typing.Optional[SchoolLocationContinent] = pydantic.Field(default=None)
    """
    The continent associated with the school
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
