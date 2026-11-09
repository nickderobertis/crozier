

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_payment_create_status import PaymentInitiationPaymentCreateStatus
from .request_id import RequestId


class PaymentInitiationPaymentCreateResponse(UniversalBaseModel):
    """
    PaymentInitiationPaymentCreateResponse defines the response schema for `/payment_initiation/payment/create`
    """

    payment_id: str = pydantic.Field()
    """
    A unique ID identifying the payment
    """

    request_id: RequestId
    status: PaymentInitiationPaymentCreateStatus

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
