

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganizationAddress(UniversalBaseModel):
    city: str
    company_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="companyName"), pydantic.Field(alias="companyName")
    ] = None
    country_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="The ISO 3166 two-letter country code"),
    ]
    """
    The ISO 3166 two-letter country code
    """

    country_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="countryName"),
        pydantic.Field(alias="countryName", description="The country name"),
    ] = None
    """
    The country name
    """

    firstname: str
    lastname: str
    post_code: typing_extensions.Annotated[str, FieldMetadata(alias="postCode"), pydantic.Field(alias="postCode")]
    street: str
    telephone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The telephone number e.g.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
