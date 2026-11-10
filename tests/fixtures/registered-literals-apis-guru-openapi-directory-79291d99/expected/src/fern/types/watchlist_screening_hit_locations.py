

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .generic_country_code import GenericCountryCode


class WatchlistScreeningHitLocations(UniversalBaseModel):
    """
    Location information for the associated individual watchlist hit
    """

    country: GenericCountryCode
    full: str = pydantic.Field()
    """
    The full location string, potentially including elements like street, city, postal codes and country codes. Note that this is not necessarily a complete or well-formatted address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
