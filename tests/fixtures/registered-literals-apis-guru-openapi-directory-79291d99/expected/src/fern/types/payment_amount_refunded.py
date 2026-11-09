

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .payment_amount_nullable import PaymentAmountNullable


class PaymentAmountRefunded(PaymentAmountNullable):
    """
    The amount and currency of a payment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
