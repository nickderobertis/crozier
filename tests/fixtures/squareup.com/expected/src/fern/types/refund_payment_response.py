

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .payment_refund import PaymentRefund


class RefundPaymentResponse(UniversalBaseModel):
    """
    Defines the response returned by
    [RefundPayment](https://developer.squareup.com/reference/square_2021-08-18/refunds-api/refund-payment).

    If there are errors processing the request, the `refund` field might not be
    present, or it might be present with a status of `FAILED`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    refund: typing.Optional[PaymentRefund] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
