

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .transaction_base import TransactionBase
from .transaction_checkout_info import TransactionCheckoutInfo


class CheckoutTransactionsItem(TransactionBase, TransactionCheckoutInfo):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
