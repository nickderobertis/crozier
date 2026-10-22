

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .block_time import BlockTime
from .transaction_type import TransactionType


class Transaction(UniversalBaseModel):
    transaction_type: TransactionType
    txid: str
    received: int
    sent: int
    fee: int
    confirmation_time: typing.Optional[BlockTime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
