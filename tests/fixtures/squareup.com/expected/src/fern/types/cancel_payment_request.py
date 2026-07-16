

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CancelPaymentRequest(UniversalBaseModel):
    """
    Describes the request to cancel (void) a payment using
    [CancelPayment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/cancel-payment).
    You can only cancel a payment that is approved (not completed).
    For more information, see
    [Delayed capture of a payment](https://developer.squareup.com/docs/payments-api/take-payments/card-payments#delayed-capture-of-a-card-payment).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
