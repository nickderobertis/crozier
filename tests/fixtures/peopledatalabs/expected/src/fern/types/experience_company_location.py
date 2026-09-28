

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .experience_company_location_continent import ExperienceCompanyLocationContinent
from .experience_company_location_country import ExperienceCompanyLocationCountry
from .experience_company_location_metro import ExperienceCompanyLocationMetro


class ExperienceCompanyLocation(UniversalBaseModel):
    street_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company HQ address
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="address_line_2"),
        pydantic.Field(alias="address_line_2", description="The address line 2 associated with the company HQ"),
    ] = None
    """
    The address line 2 associated with the company HQ
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The canonical location name associated with the company HQ
    """

    locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company locality
    """

    metro: typing.Optional[ExperienceCompanyLocationMetro] = pydantic.Field(default=None)
    """
    Company metro area
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company region
    """

    country: typing.Optional[ExperienceCompanyLocationCountry] = pydantic.Field(default=None)
    """
    Company country
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The postal code associated with the company
    """

    continent: typing.Optional[ExperienceCompanyLocationContinent] = pydantic.Field(default=None)
    """
    The continent associated with the company HQ
    """

    geo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The geo code associated with the company HQ
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
