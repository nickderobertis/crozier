

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payment_instrument import PaymentInstrument
from .payment_status_reason import PaymentStatusReason


class Payment(UniversalBaseModel):
    """
    The payment associated with the expense.
    """

    id: str = pydantic.Field()
    """
    Unique ID for the payment.
    """

    payment_instrument: PaymentInstrument
    status_reason: PaymentStatusReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
