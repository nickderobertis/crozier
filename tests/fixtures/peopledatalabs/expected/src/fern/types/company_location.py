

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .company_location_continent import CompanyLocationContinent
from .company_location_country import CompanyLocationCountry
from .company_location_metro import CompanyLocationMetro


class CompanyLocation(UniversalBaseModel):
    geo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's current HQ city-level Geo
    """

    street_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's current HQ street address
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="address_line_2"),
        pydantic.Field(alias="address_line_2", description="The company's current HQ address line 2"),
    ] = None
    """
    The company's current HQ address line 2
    """

    continent: typing.Optional[CompanyLocationContinent] = pydantic.Field(default=None)
    """
    The company's current HQ continent
    """

    locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's current HQ locality
    """

    metro: typing.Optional[CompanyLocationMetro] = pydantic.Field(default=None)
    """
    The company's current HQ metro (US only)
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's current HQ postal code
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's current HQ location name, generated from our canonical location data with the format locality, region, country
    """

    country: typing.Optional[CompanyLocationCountry] = pydantic.Field(default=None)
    """
    The company's current HQ country    united states
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The company's current HQ region
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
