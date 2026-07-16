

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .payment import Payment


class CreatePaymentResponse(UniversalBaseModel):
    """
    Defines the response returned by [CreatePayment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/create-payment).

    If there are errors processing the request, the `payment` field might not be
    present, or it might be present with a status of `FAILED`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    payment: typing.Optional[Payment] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
