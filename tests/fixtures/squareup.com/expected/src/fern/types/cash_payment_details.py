

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class CashPaymentDetails(UniversalBaseModel):
    """
    Stores details about a cash payment. Contains only non-confidential information. For more information, see
    [Take Cash Payments](https://developer.squareup.com/docs/payments-api/take-payments/cash-payments).
    """

    buyer_supplied_money: Money
    change_back_money: typing.Optional[Money] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
