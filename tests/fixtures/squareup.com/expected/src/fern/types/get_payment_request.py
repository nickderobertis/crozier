

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetPaymentRequest(UniversalBaseModel):
    """
    Describes a request to retrieve a payment using
    [GetPayment](https://developer.squareup.com/reference/square_2021-08-18/payments-api/get-payment).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
