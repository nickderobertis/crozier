

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Statement(UniversalBaseModel):
    """
    a statement, including all inflows and outflows, for a single transfer of an asset (including ETH) to or from a given address
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

    transaction_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionHash"),
        pydantic.Field(
            alias="transactionHash", description="the hash of the transaction that triggered this reconciliation"
        ),
    ] = None
    """
    the hash of the transaction that triggered this reconciliation
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the Unix timestamp of the object
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    asset: typing.Optional[str] = pydantic.Field(default=None)
    """
    0xeeee...eeee for ETH reconciliations, the token address otherwise
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    either ETH, WEI, or the symbol of the asset being reconciled as extracted from the chain
    """

    decimals: typing.Optional[float] = pydantic.Field(default=None)
    """
    the value of `decimals` from an ERC20 contract or, if ETH or WEI, then 18
    """

    spot_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="spotPrice"),
        pydantic.Field(
            alias="spotPrice",
            description="the on-chain price in USD (or if a token in ETH, or zero) at the time of the transaction",
        ),
    ] = None
    """
    the on-chain price in USD (or if a token in ETH, or zero) at the time of the transaction
    """

    price_source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="priceSource"),
        pydantic.Field(alias="priceSource", description="the on-chain source from which the spot price was taken"),
    ] = None
    """
    the on-chain source from which the spot price was taken
    """

    accounted_for: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountedFor"),
        pydantic.Field(alias="accountedFor", description="the address being accounted for in this reconciliation"),
    ] = None
    """
    the address being accounted for in this reconciliation
    """

    sender: typing.Optional[str] = pydantic.Field(default=None)
    """
    the initiator of the transfer (the sender)
    """

    recipient: typing.Optional[str] = pydantic.Field(default=None)
    """
    the receiver of the transfer (the recipient)
    """

    beg_bal: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="begBal"),
        pydantic.Field(
            alias="begBal",
            description="the on-chain or running beginning balance prior to the transaction (see notes about intra-block reconciliations)",
        ),
    ] = None
    """
    the on-chain or running beginning balance prior to the transaction (see notes about intra-block reconciliations)
    """

    amount_net: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="amountNet"),
        pydantic.Field(alias="amountNet", description="totalIn - totalOut (calculated)"),
    ] = None
    """
    totalIn - totalOut (calculated)
    """

    end_bal: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endBal"),
        pydantic.Field(
            alias="endBal",
            description="the on-chain or running balance after the transaction (see notes about intra-block reconciliations)",
        ),
    ] = None
    """
    the on-chain or running balance after the transaction (see notes about intra-block reconciliations)
    """

    reconciled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    true if `endBal === endBalCalc` and `begBal === prevBal`. `false` otherwise. (calculated)
    """

    total_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totalIn"),
        pydantic.Field(alias="totalIn", description="the sum of the following `In` fields (calculated)"),
    ] = None
    """
    the sum of the following `In` fields (calculated)
    """

    amount_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="amountIn"),
        pydantic.Field(
            alias="amountIn", description="the top-level value of the incoming transfer for the accountedFor address"
        ),
    ] = None
    """
    the top-level value of the incoming transfer for the accountedFor address
    """

    internal_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="internalIn"),
        pydantic.Field(
            alias="internalIn", description="the internal value of the incoming transfer for the accountedFor address"
        ),
    ] = None
    """
    the internal value of the incoming transfer for the accountedFor address
    """

    self_destruct_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="selfDestructIn"),
        pydantic.Field(
            alias="selfDestructIn",
            description="the incoming value of a self-destruct if recipient is the accountedFor address",
        ),
    ] = None
    """
    the incoming value of a self-destruct if recipient is the accountedFor address
    """

    miner_base_reward_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerBaseRewardIn"),
        pydantic.Field(
            alias="minerBaseRewardIn", description="the base fee reward if the miner is the accountedFor address"
        ),
    ] = None
    """
    the base fee reward if the miner is the accountedFor address
    """

    miner_nephew_reward_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerNephewRewardIn"),
        pydantic.Field(
            alias="minerNephewRewardIn", description="the nephew reward if the miner is the accountedFor address"
        ),
    ] = None
    """
    the nephew reward if the miner is the accountedFor address
    """

    miner_tx_fee_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerTxFeeIn"),
        pydantic.Field(
            alias="minerTxFeeIn", description="the transaction fee reward if the miner is the accountedFor address"
        ),
    ] = None
    """
    the transaction fee reward if the miner is the accountedFor address
    """

    miner_uncle_reward_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="minerUncleRewardIn"),
        pydantic.Field(
            alias="minerUncleRewardIn",
            description="the uncle reward if the miner who won the uncle block is the accountedFor address",
        ),
    ] = None
    """
    the uncle reward if the miner who won the uncle block is the accountedFor address
    """

    correct_beg_bal_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctBegBalIn"),
        pydantic.Field(
            alias="correctBegBalIn",
            description="for unreconciled transfers, increase in beginning balance need to match previous balance",
        ),
    ] = None
    """
    for unreconciled transfers, increase in beginning balance need to match previous balance
    """

    correct_amount_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctAmountIn"),
        pydantic.Field(
            alias="correctAmountIn", description="for unreconciled transfers, increase in the amount of a transfer"
        ),
    ] = None
    """
    for unreconciled transfers, increase in the amount of a transfer
    """

    correct_end_bal_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctEndBalIn"),
        pydantic.Field(
            alias="correctEndBalIn",
            description="for unreconciled transfers, increase in ending balance need to match running balance or block balance",
        ),
    ] = None
    """
    for unreconciled transfers, increase in ending balance need to match running balance or block balance
    """

    prefund_in: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="prefundIn"),
        pydantic.Field(
            alias="prefundIn",
            description="at block zero (0) only, the amount of genesis income for the accountedFor address",
        ),
    ] = None
    """
    at block zero (0) only, the amount of genesis income for the accountedFor address
    """

    total_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totalOut"),
        pydantic.Field(alias="totalOut", description="the sum of the following `Out` fields (calculated)"),
    ] = None
    """
    the sum of the following `Out` fields (calculated)
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
            alias="internalOut", description="the value of any internal value transfers out of the accountedFor account"
        ),
    ] = None
    """
    the value of any internal value transfers out of the accountedFor account
    """

    correct_beg_bal_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctBegBalOut"),
        pydantic.Field(
            alias="correctBegBalOut",
            description="for unreconciled transfers, decrease in beginning balance need to match previous balance",
        ),
    ] = None
    """
    for unreconciled transfers, decrease in beginning balance need to match previous balance
    """

    correct_amount_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctAmountOut"),
        pydantic.Field(
            alias="correctAmountOut", description="for unreconciled transfers, decrease in the amount of a transfer"
        ),
    ] = None
    """
    for unreconciled transfers, decrease in the amount of a transfer
    """

    correct_end_bal_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctEndBalOut"),
        pydantic.Field(
            alias="correctEndBalOut",
            description="for unreconciled transfers, decrease in ending balance need to match running balance or block balance",
        ),
    ] = None
    """
    for unreconciled transfers, decrease in ending balance need to match running balance or block balance
    """

    self_destruct_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="selfDestructOut"),
        pydantic.Field(
            alias="selfDestructOut",
            description="the value of the self-destructed value out if the accountedFor address was self-destructed",
        ),
    ] = None
    """
    the value of the self-destructed value out if the accountedFor address was self-destructed
    """

    gas_out: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="gasOut"),
        pydantic.Field(
            alias="gasOut",
            description="if the transaction's original sender is the accountedFor address, the amount of gas expended",
        ),
    ] = None
    """
    if the transaction's original sender is the accountedFor address, the amount of gas expended
    """

    prev_bal: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="prevBal"),
        pydantic.Field(
            alias="prevBal", description="the account balance for the given asset for the previous reconciliation"
        ),
    ] = None
    """
    the account balance for the given asset for the previous reconciliation
    """

    beg_bal_diff: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="begBalDiff"),
        pydantic.Field(
            alias="begBalDiff",
            description="difference between expected beginning balance and balance at last reconciliation, if non-zero, the reconciliation failed (calculated)",
        ),
    ] = None
    """
    difference between expected beginning balance and balance at last reconciliation, if non-zero, the reconciliation failed (calculated)
    """

    end_bal_diff: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endBalDiff"),
        pydantic.Field(
            alias="endBalDiff", description="endBal - endBalCalc, if non-zero, the reconciliation failed (calculated)"
        ),
    ] = None
    """
    endBal - endBalCalc, if non-zero, the reconciliation failed (calculated)
    """

    end_bal_calc: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endBalCalc"),
        pydantic.Field(alias="endBalCalc", description="begBal + amountNet (calculated)"),
    ] = None
    """
    begBal + amountNet (calculated)
    """

    correcting_reasons: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="correctingReasons"),
        pydantic.Field(
            alias="correctingReasons",
            description="for unreconciled transfers, the reasons for the correcting entries, if any",
        ),
    ] = None
    """
    for unreconciled transfers, the reasons for the correcting entries, if any
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
