

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .receipt_acquirer_data import ReceiptAcquirerData
from .receipt_merchant_data import ReceiptMerchantData
from .receipt_transaction import ReceiptTransaction


class Receipt(UniversalBaseModel):
    """
    Receipt details for a transaction.
    """

    transaction_data: typing.Optional[ReceiptTransaction] = None
    merchant_data: typing.Optional[ReceiptMerchantData] = None
    emv_data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    EMV-specific metadata returned for card-present payments.
    """

    acquirer_data: typing.Optional[ReceiptAcquirerData] = pydantic.Field(default=None)
    """
    Acquirer-specific metadata related to the card authorization.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
