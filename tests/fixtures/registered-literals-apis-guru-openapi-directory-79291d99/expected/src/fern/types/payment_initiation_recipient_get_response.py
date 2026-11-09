

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .payment_initiation_recipient import PaymentInitiationRecipient
from .request_id import RequestId


class PaymentInitiationRecipientGetResponse(PaymentInitiationRecipient):
    """
    PaymentInitiationRecipientGetResponse defines the response schema for `/payment_initiation/recipient/get`
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
