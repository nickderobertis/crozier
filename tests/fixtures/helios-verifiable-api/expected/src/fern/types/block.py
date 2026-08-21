

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .block_transactions import BlockTransactions
from .bytes import Bytes
from .bytes8 import Bytes8
from .bytes256 import Bytes256
from .hash32 import Hash32
from .uint import Uint
from .withdrawal import Withdrawal


class Block(UniversalBaseModel):
    hash: Hash32
    parent_hash: typing_extensions.Annotated[
        Hash32, FieldMetadata(alias="parentHash"), pydantic.Field(alias="parentHash")
    ]
    sha3uncles: typing_extensions.Annotated[
        Hash32, FieldMetadata(alias="sha3Uncles"), pydantic.Field(alias="sha3Uncles")
    ]
    miner: Address
    state_root: typing_extensions.Annotated[Hash32, FieldMetadata(alias="stateRoot"), pydantic.Field(alias="stateRoot")]
    transactions_root: typing_extensions.Annotated[
        Hash32, FieldMetadata(alias="transactionsRoot"), pydantic.Field(alias="transactionsRoot")
    ]
    receipts_root: typing_extensions.Annotated[
        Hash32, FieldMetadata(alias="receiptsRoot"), pydantic.Field(alias="receiptsRoot")
    ]
    logs_bloom: typing_extensions.Annotated[
        Bytes256, FieldMetadata(alias="logsBloom"), pydantic.Field(alias="logsBloom")
    ]
    difficulty: typing.Optional[Uint] = None
    number: Uint
    gas_limit: typing_extensions.Annotated[Uint, FieldMetadata(alias="gasLimit"), pydantic.Field(alias="gasLimit")]
    gas_used: typing_extensions.Annotated[Uint, FieldMetadata(alias="gasUsed"), pydantic.Field(alias="gasUsed")]
    timestamp: Uint
    extra_data: typing_extensions.Annotated[Bytes, FieldMetadata(alias="extraData"), pydantic.Field(alias="extraData")]
    mix_hash: typing_extensions.Annotated[Hash32, FieldMetadata(alias="mixHash"), pydantic.Field(alias="mixHash")]
    nonce: Bytes8
    base_fee_per_gas: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="baseFeePerGas"), pydantic.Field(alias="baseFeePerGas")
    ] = None
    withdrawals_root: typing_extensions.Annotated[
        typing.Optional[Hash32], FieldMetadata(alias="withdrawalsRoot"), pydantic.Field(alias="withdrawalsRoot")
    ] = None
    blob_gas_used: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="blobGasUsed"), pydantic.Field(alias="blobGasUsed")
    ] = None
    excess_blob_gas: typing_extensions.Annotated[
        typing.Optional[Uint], FieldMetadata(alias="excessBlobGas"), pydantic.Field(alias="excessBlobGas")
    ] = None
    parent_beacon_block_root: typing_extensions.Annotated[
        typing.Optional[Hash32],
        FieldMetadata(alias="parentBeaconBlockRoot"),
        pydantic.Field(alias="parentBeaconBlockRoot"),
    ] = None
    size: Uint
    transactions: BlockTransactions
    withdrawals: typing.Optional[typing.List[Withdrawal]] = None
    uncles: typing.List[Hash32]
    requests_hash: typing_extensions.Annotated[
        typing.Optional[Hash32], FieldMetadata(alias="requestsHash"), pydantic.Field(alias="requestsHash")
    ] = None
    block_access_list_hash: typing_extensions.Annotated[
        typing.Optional[Hash32], FieldMetadata(alias="blockAccessListHash"), pydantic.Field(alias="blockAccessListHash")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
