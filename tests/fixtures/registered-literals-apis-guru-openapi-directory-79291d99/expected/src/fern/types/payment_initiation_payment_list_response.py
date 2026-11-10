

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_initiation_payment import PaymentInitiationPayment
from .request_id import RequestId


class PaymentInitiationPaymentListResponse(UniversalBaseModel):
    """
    PaymentInitiationPaymentListResponse defines the response schema for `/payment_initiation/payment/list`
    """

    next_cursor: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The value that, when used as the optional `cursor` parameter to `/payment_initiation/payment/list`, will return the next unreturned payment as its first payment.
    """

    payments: typing.List[PaymentInitiationPayment] = pydantic.Field()
    """
    An array of payments that have been created, associated with the given `client_id`.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
