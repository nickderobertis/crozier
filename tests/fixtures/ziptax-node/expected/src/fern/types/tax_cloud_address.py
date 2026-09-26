

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tax_cloud_address_country_code import TaxCloudAddressCountryCode


class TaxCloudAddress(UniversalBaseModel):
    city: str = pydantic.Field()
    """
    City or post-town of the address.
    """

    country_code: typing_extensions.Annotated[
        typing.Optional[TaxCloudAddressCountryCode],
        FieldMetadata(alias="countryCode"),
        pydantic.Field(
            alias="countryCode",
            description="ISO 3166-1 alpha-2 country code of the address. US (United States) or CA (Canada). Defaults to US when omitted.",
        ),
    ] = None
    """
    ISO 3166-1 alpha-2 country code of the address. US (United States) or CA (Canada). Defaults to US when omitted.
    """

    line1: str = pydantic.Field()
    """
    First line of the address: street number and name, PO Box, or building. Values longer than 50 characters are automatically truncated by TaxCloud.
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Second line of the address, if any (e.g. apartment, suite, or unit number). Values longer than 50 characters are automatically truncated by TaxCloud.
    """

    state: str = pydantic.Field()
    """
    State, province, or other large territorial division, as a two-letter abbreviation (e.g. MN, CA, ON).
    """

    zip: str = pydantic.Field()
    """
    Postal or ZIP code. Five-digit (55401) and ZIP+4 (55401-2427) formats are accepted for US addresses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
