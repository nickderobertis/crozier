

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_type import TransactionType


class Transaction(UniversalBaseModel):
    id: typing.Optional[str] = None
    order_id: typing.Optional[str] = None
    type: typing.Optional[TransactionType] = None
    product_id: typing.Optional[int] = None
    amount: typing.Optional[float] = None
    currency: typing.Optional[str] = None
    customer_email: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
