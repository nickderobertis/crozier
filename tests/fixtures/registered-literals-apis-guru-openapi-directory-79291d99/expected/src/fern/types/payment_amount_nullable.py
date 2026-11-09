

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_amount_currency import PaymentAmountCurrency


class PaymentAmountNullable(UniversalBaseModel):
    """
    The amount and currency of a payment
    """

    currency: PaymentAmountCurrency
    value: float = pydantic.Field()
    """
    The amount of the payment. Must contain at most two digits of precision e.g. `1.23`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
