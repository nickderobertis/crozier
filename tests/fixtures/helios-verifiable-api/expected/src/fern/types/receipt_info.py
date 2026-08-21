

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .address import Address
from .byte import Byte
from .bytes256 import Bytes256
from .hash32 import Hash32
from .log import Log
from .uint import Uint


class ReceiptInfo(UniversalBaseModel):
    type: typing.Optional[Byte] = None
    transaction_hash: typing_extensions.Annotated[
        Hash32, FieldMetadata(alias="transactionHash"), pydantic.Field(alias="transactionHash")
    ]
    transaction_index: typing_extensions.Annotated[
        Uint, FieldMetadata(alias="transactionIndex"), pydantic.Field(alias="transactionIndex")
    ]
    block_hash: typing_extensions.Annotated[Hash32, FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")]
    block_number: typing_extensions.Annotated[
        Uint, FieldMetadata(alias="blockNumber"), pydantic.Field(alias="blockNumber")
    ]
    from_: typing_extensions.Annotated[Address, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    to: typing.Optional[Address] = pydantic.Field(default=None)
    """
    Address of the receiver or null in a contract creation transaction.
    """

    cumulative_gas_used: typing_extensions.Annotated[
        Uint,
        FieldMetadata(alias="cumulativeGasUsed"),
        pydantic.Field(
            alias="cumulativeGasUsed",
            description="The sum of gas used by this transaction and all preceding transactions in the same block.",
        ),
    ]
    """
    The sum of gas used by this transaction and all preceding transactions in the same block.
    """

    gas_used: typing_extensions.Annotated[
        Uint,
        FieldMetadata(alias="gasUsed"),
        pydantic.Field(alias="gasUsed", description="The amount of gas used for this specific transaction alone."),
    ]
    """
    The amount of gas used for this specific transaction alone.
    """

    blob_gas_used: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="blobGasUsed"),
        pydantic.Field(
            alias="blobGasUsed",
            description="The amount of blob gas used for this specific transaction. Only specified for blob transactions as defined by EIP-4844.",
        ),
    ] = None
    """
    The amount of blob gas used for this specific transaction. Only specified for blob transactions as defined by EIP-4844.
    """

    contract_address: typing_extensions.Annotated[
        typing.Optional[Address],
        FieldMetadata(alias="contractAddress"),
        pydantic.Field(
            alias="contractAddress",
            description="The contract address created, if the transaction was a contract creation, otherwise null.",
        ),
    ] = None
    """
    The contract address created, if the transaction was a contract creation, otherwise null.
    """

    logs: typing.List[Log]
    logs_bloom: typing_extensions.Annotated[
        Bytes256, FieldMetadata(alias="logsBloom"), pydantic.Field(alias="logsBloom")
    ]
    root: typing.Optional[Hash32] = pydantic.Field(default=None)
    """
    The post-transaction state root. Only specified for transactions included before the Byzantium upgrade.
    """

    status: typing.Optional[Uint] = pydantic.Field(default=None)
    """
    Either 1 (success) or 0 (failure). Only specified for transactions included after the Byzantium upgrade.
    """

    effective_gas_price: typing_extensions.Annotated[
        Uint,
        FieldMetadata(alias="effectiveGasPrice"),
        pydantic.Field(
            alias="effectiveGasPrice",
            description="The actual value per gas deducted from the sender's account. Before EIP-1559, this is equal to the transaction's gas price. After, it is equal to baseFeePerGas + min(maxFeePerGas - baseFeePerGas, maxPriorityFeePerGas).",
        ),
    ]
    """
    The actual value per gas deducted from the sender's account. Before EIP-1559, this is equal to the transaction's gas price. After, it is equal to baseFeePerGas + min(maxFeePerGas - baseFeePerGas, maxPriorityFeePerGas).
    """

    blob_gas_price: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="blobGasPrice"),
        pydantic.Field(
            alias="blobGasPrice",
            description="The actual value per gas deducted from the sender's account for blob gas. Only specified for blob transactions as defined by EIP-4844.",
        ),
    ] = None
    """
    The actual value per gas deducted from the sender's account for blob gas. Only specified for blob transactions as defined by EIP-4844.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
