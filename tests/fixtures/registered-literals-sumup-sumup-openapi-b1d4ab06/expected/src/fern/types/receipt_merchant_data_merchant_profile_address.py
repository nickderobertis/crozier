

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ReceiptMerchantDataMerchantProfileAddress(UniversalBaseModel):
    """
    Business address of the merchant.
    """

    address_line1: typing.Optional[str] = pydantic.Field(default=None)
    """
    First line of the merchant address.
    """

    address_line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Second line of the merchant address.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City of the merchant address.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Two-letter ISO 3166-1 alpha-2 country code of the merchant address.
    """

    country_en_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    English name of the country in the merchant address.
    """

    country_native_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Localized name of the country in the merchant address.
    """

    region_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Region or state of the merchant address.
    """

    post_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postal code of the merchant address.
    """

    landline: typing.Optional[str] = pydantic.Field(default=None)
    """
    Landline phone number of the merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
