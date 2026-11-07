

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chain_index import ChainIndex
from .v2transaction import V2Transaction


class TxpoolUpdateV2TransactionsResponse(UniversalBaseModel):
    basis: ChainIndex
    transactions: typing.List[V2Transaction]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
