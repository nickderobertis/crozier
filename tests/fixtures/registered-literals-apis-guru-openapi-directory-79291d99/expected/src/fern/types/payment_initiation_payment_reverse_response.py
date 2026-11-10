

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .wallet_transaction_status import WalletTransactionStatus


class PaymentInitiationPaymentReverseResponse(UniversalBaseModel):
    """
    PaymentInitiationPaymentReverseResponse defines the response schema for `/payment_initation/payment/reverse`
    """

    refund_id: str = pydantic.Field()
    """
    A unique ID identifying the refund
    """

    request_id: RequestId
    status: WalletTransactionStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
