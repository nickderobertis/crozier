

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_payment_methods_response_available_payment_methods_item import (
    GetPaymentMethodsResponseAvailablePaymentMethodsItem,
)


class GetPaymentMethodsResponse(UniversalBaseModel):
    available_payment_methods: typing.Optional[typing.List[GetPaymentMethodsResponseAvailablePaymentMethodsItem]] = (
        pydantic.Field(default=None)
    )
    """
    Payment methods available to the merchant for the checkout.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
