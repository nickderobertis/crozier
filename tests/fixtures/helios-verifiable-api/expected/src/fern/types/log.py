

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .bytes import Bytes
from .bytes32 import Bytes32
from .hash32 import Hash32
from .uint import Uint


class Log(UniversalBaseModel):
    removed: typing.Optional[bool] = None
    log_index: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="logIndex"), pydantic.Field(alias="logIndex")
    ] = None
    transaction_index: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="transactionIndex"), pydantic.Field(alias="transactionIndex")
    ] = None
    transaction_hash: typing_extensions.Annotated[
        Hash32, FieldMetadata(alias="transactionHash"), pydantic.Field(alias="transactionHash")
    ]
    block_hash: typing_extensions.Annotated[
        typing.Optional[Hash32], FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")
    ] = None
    block_number: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="blockNumber"), pydantic.Field(alias="blockNumber")
    ] = None
    block_timestamp: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="blockTimestamp"), pydantic.Field(alias="blockTimestamp")
    ] = None
    address: typing.Optional[Address] = None
    data: typing.Optional[Bytes] = None
    topics: typing.Optional[typing.List[Bytes32]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
