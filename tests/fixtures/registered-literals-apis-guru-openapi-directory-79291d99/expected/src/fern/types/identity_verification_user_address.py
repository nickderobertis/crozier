

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .city_nullable import CityNullable
from .generic_country_code import GenericCountryCode
from .postal_code_nullable import PostalCodeNullable
from .region_nullable import RegionNullable
from .street2 import Street2
from .street_nullable import StreetNullable


class IdentityVerificationUserAddress(UniversalBaseModel):
    """
    Even if an address has been collected, some fields may be null depending on the region's addressing system. For example:

    Addresses from the United Kingdom will not include a region

    Addresses from Hong Kong will not include postal code
    """

    city: typing.Optional[CityNullable] = None
    country: GenericCountryCode
    postal_code: typing.Optional[PostalCodeNullable] = None
    region: typing.Optional[RegionNullable] = None
    street: typing.Optional[StreetNullable] = None
    street2: typing.Optional[Street2] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
