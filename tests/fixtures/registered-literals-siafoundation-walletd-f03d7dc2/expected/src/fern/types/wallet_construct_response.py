

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chain_index import ChainIndex
from .currency import Currency
from .transaction import Transaction
from .transaction_id import TransactionId


class WalletConstructResponse(UniversalBaseModel):
    basis: ChainIndex
    id: TransactionId
    transaction: Transaction
    estimated_fee: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="estimatedFee"), pydantic.Field(alias="estimatedFee")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
