

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .chain_index import ChainIndex
from .currency import Currency
from .hash256 import Hash256
from .transaction_id import TransactionId
from .v2transaction import V2Transaction


class WalletConstructV2Response(UniversalBaseModel):
    basis: ChainIndex
    id: TransactionId
    transaction: V2Transaction
    estimated_fee: typing_extensions.Annotated[
        Currency, FieldMetadata(alias="estimatedFee"), pydantic.Field(alias="estimatedFee")
    ]
    input_sig_hash: typing_extensions.Annotated[
        Hash256, FieldMetadata(alias="inputSigHash"), pydantic.Field(alias="inputSigHash")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
