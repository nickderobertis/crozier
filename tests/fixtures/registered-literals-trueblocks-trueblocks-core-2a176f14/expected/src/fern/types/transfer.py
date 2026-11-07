

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Transfer(UniversalBaseModel):
    """
    a movement of an asset from one address to another (derived from a transaction or a log)
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

    log_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="logIndex"),
        pydantic.Field(alias="logIndex", description="the zero-indexed position the log in the block, if applicable"),
    ] = None
    """
    the zero-indexed position the log in the block, if applicable
    """

    holder: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of the holder of the asset
    """

    asset: typing.Optional[str] = pydantic.Field(default=None)
    """
    0xeeee...eeee for ETH transfers, the token address otherwise
    """

    decimals: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of decimal places in the asset units
    """

    sender: typing.Optional[str] = pydantic.Field(default=None)
    """
    the initiator of the transfer (the sender)
    """

    recipient: typing.Optional[str] = pydantic.Field(default=None)
    """
    the receiver of the transfer (the recipient)
    """

    amount_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="amountIn"),
        pydantic.Field(
            alias="amountIn", description="the top-level value of the incoming transfer for the holder address"
        ),
    ] = None
    """
    the top-level value of the incoming transfer for the holder address
    """

    internal_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="internalIn"),
        pydantic.Field(
            alias="internalIn", description="the internal value of the incoming transfer for the holder address"
        ),
    ] = None
    """
    the internal value of the incoming transfer for the holder address
    """

    miner_base_reward_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerBaseRewardIn"),
        pydantic.Field(alias="minerBaseRewardIn", description="the base fee reward if the miner is the holder address"),
    ] = None
    """
    the base fee reward if the miner is the holder address
    """

    miner_nephew_reward_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerNephewRewardIn"),
        pydantic.Field(alias="minerNephewRewardIn", description="the nephew reward if the miner is the holder address"),
    ] = None
    """
    the nephew reward if the miner is the holder address
    """

    miner_tx_fee_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerTxFeeIn"),
        pydantic.Field(
            alias="minerTxFeeIn", description="the transaction fee reward if the miner is the holder address"
        ),
    ] = None
    """
    the transaction fee reward if the miner is the holder address
    """

    miner_uncle_reward_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerUncleRewardIn"),
        pydantic.Field(
            alias="minerUncleRewardIn",
            description="the uncle reward if the miner who won the uncle block is the holder address",
        ),
    ] = None
    """
    the uncle reward if the miner who won the uncle block is the holder address
    """

    prefund_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="prefundIn"),
        pydantic.Field(
            alias="prefundIn", description="at block zero (0) only, the amount of genesis income for the holder address"
        ),
    ] = None
    """
    at block zero (0) only, the amount of genesis income for the holder address
    """

    self_destruct_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="selfDestructIn"),
        pydantic.Field(
            alias="selfDestructIn",
            description="the incoming value of a self-destruct if recipient is the holder address",
        ),
    ] = None
    """
    the incoming value of a self-destruct if recipient is the holder address
    """

    amount_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="amountOut"),
        pydantic.Field(
            alias="amountOut",
            description="the amount (in units of the asset) of regular outflow during this transaction",
        ),
    ] = None
    """
    the amount (in units of the asset) of regular outflow during this transaction
    """

    internal_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="internalOut"),
        pydantic.Field(
            alias="internalOut", description="the value of any internal value transfers out of the holder account"
        ),
    ] = None
    """
    the value of any internal value transfers out of the holder account
    """

    gas_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="gasOut"),
        pydantic.Field(
            alias="gasOut",
            description="if the transaction's original sender is the holder address, the amount of gas expended",
        ),
    ] = None
    """
    if the transaction's original sender is the holder address, the amount of gas expended
    """

    self_destruct_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="selfDestructOut"),
        pydantic.Field(
            alias="selfDestructOut", description="the outgoing value of a self-destruct if sender is the holder address"
        ),
    ] = None
    """
    the outgoing value of a self-destruct if sender is the holder address
    """

    transaction: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    the transaction that triggered the transfer (calculated)
    """

    log: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    if a token transfer, the log that triggered the transfer (calculated)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
