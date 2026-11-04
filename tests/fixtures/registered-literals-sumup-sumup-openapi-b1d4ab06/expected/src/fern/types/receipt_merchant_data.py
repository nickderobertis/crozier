

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .receipt_merchant_data_merchant_profile import ReceiptMerchantDataMerchantProfile


class ReceiptMerchantData(UniversalBaseModel):
    """
    Merchant details displayed on a transaction receipt.
    """

    merchant_profile: typing.Optional[ReceiptMerchantDataMerchantProfile] = pydantic.Field(default=None)
    """
    Merchant profile details displayed on the receipt.
    """

    locale: typing.Optional[str] = pydantic.Field(default=None)
    """
    Locale used for rendering localized receipt fields.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
