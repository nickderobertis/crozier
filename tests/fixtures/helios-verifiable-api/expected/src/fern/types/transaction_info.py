

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .hash32 import Hash32
from .uint import Uint


class TransactionInfo(UniversalBaseModel):
    block_hash: typing_extensions.Annotated[Hash32, FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")]
    block_number: typing_extensions.Annotated[
        Uint, FieldMetadata(alias="blockNumber"), pydantic.Field(alias="blockNumber")
    ]
    block_timestamp: typing_extensions.Annotated[
        Uint, FieldMetadata(alias="blockTimestamp"), pydantic.Field(alias="blockTimestamp")
    ]
    from_: typing_extensions.Annotated[Address, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    hash: Hash32
    transaction_index: typing_extensions.Annotated[
        Uint, FieldMetadata(alias="transactionIndex"), pydantic.Field(alias="transactionIndex")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
