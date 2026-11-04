

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Slurp(UniversalBaseModel):
    """
    transaction data as returned from by remote APIs
    """

    hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    the hash of the transaction
    """

    block_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="blockHash"),
        pydantic.Field(alias="blockHash", description="the hash of the block containing this transaction"),
    ] = None
    """
    the hash of the block containing this transaction
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of the block"),
    ] = None
    """
    the number of the block
    """

    transaction_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="transactionIndex"),
        pydantic.Field(
            alias="transactionIndex", description="the zero-indexed position of the transaction in the block"
        ),
    ] = None
    """
    the zero-indexed position of the transaction in the block
    """

    nonce: typing.Optional[float] = pydantic.Field(default=None)
    """
    sequence number of the transactions sent by the sender
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the Unix timestamp of the object
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="address from which the transaction was sent"),
    ] = None
    """
    address from which the transaction was sent
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    address to which the transaction was sent
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    the amount of wei sent with this transactions
    """

    ether: typing.Optional[str] = pydantic.Field(default=None)
    """
    if --ether is specified, the value in ether (calculated)
    """

    gas: typing.Optional[float] = pydantic.Field(default=None)
    """
    the maximum number of gas allowed for this transaction
    """

    gas_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="gasPrice"),
        pydantic.Field(
            alias="gasPrice", description="the number of wei per unit of gas the sender is willing to spend"
        ),
    ] = None
    """
    the number of wei per unit of gas the sender is willing to spend
    """

    input: typing.Optional[str] = pydantic.Field(default=None)
    """
    byte data either containing a message or funcational data for a smart contracts. See the --articulate
    """

    has_token: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hasToken"),
        pydantic.Field(alias="hasToken", description="`true` if the transaction is token related, `false` otherwise"),
    ] = None
    """
    `true` if the transaction is token related, `false` otherwise
    """

    articulated_tx: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="articulatedTx"),
        pydantic.Field(
            alias="articulatedTx", description="if present, the function that was called in the transaction"
        ),
    ] = None
    """
    if present, the function that was called in the transaction
    """

    compressed_tx: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="compressedTx"),
        pydantic.Field(
            alias="compressedTx", description="truncated, more readable version of the articulation (calculated)"
        ),
    ] = None
    """
    truncated, more readable version of the articulation (calculated)
    """

    is_error: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isError"),
        pydantic.Field(alias="isError", description="`true` if the transaction ended in error, `false` otherwise"),
    ] = None
    """
    `true` if the transaction ended in error, `false` otherwise
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
