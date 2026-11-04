

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .receipt_merchant_data_merchant_profile_address import ReceiptMerchantDataMerchantProfileAddress


class ReceiptMerchantDataMerchantProfile(UniversalBaseModel):
    """
    Merchant profile details displayed on the receipt.
    """

    merchant_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short unique identifier for the merchant.
    """

    business_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Business name of the merchant.
    """

    company_registration_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company registration number of the merchant.
    """

    vat_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    VAT identification number of the merchant.
    """

    website: typing.Optional[str] = pydantic.Field(default=None)
    """
    Website of the merchant.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the merchant.
    """

    language: typing.Optional[str] = pydantic.Field(default=None)
    """
    Language configured for the merchant profile.
    """

    address: typing.Optional[ReceiptMerchantDataMerchantProfileAddress] = pydantic.Field(default=None)
    """
    Business address of the merchant.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
