

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompletePaymentRequest(UniversalBaseModel):
    """
    Describes a request to complete (capture) a payment using
    [CompletePayment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/complete-payment).

    By default, payments are set to `autocomplete` immediately after they are created.
    To complete payments manually, set `autocomplete` to `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
