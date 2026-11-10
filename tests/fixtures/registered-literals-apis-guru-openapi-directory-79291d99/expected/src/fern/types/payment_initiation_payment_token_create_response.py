

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId


class PaymentInitiationPaymentTokenCreateResponse(UniversalBaseModel):
    """
    PaymentInitiationPaymentTokenCreateResponse defines the response schema for `/payment_initiation/payment/token/create`
    """

    payment_token: str = pydantic.Field()
    """
    A `payment_token` that can be provided to Link initialization to enter the payment initiation flow
    """

    payment_token_expiration_time: dt.datetime = pydantic.Field()
    """
    The date and time at which the token will expire, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format. A `payment_token` expires after 15 minutes.
    """

    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
