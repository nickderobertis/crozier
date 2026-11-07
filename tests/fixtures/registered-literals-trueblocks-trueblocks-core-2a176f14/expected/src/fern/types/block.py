

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hash import Hash
from .transaction import Transaction
from .withdrawal import Withdrawal


class Block(UniversalBaseModel):
    """
    block data as returned from the RPC (with slight enhancements)
    """

    gas_limit: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="gasLimit"),
        pydantic.Field(alias="gasLimit", description="the system-wide maximum amount of gas permitted in this block"),
    ] = None
    """
    the system-wide maximum amount of gas permitted in this block
    """

    hash: typing.Optional[str] = pydantic.Field(default=None)
    """
    the hash of the current block
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of the block"),
    ] = None
    """
    the number of the block
    """

    parent_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="parentHash"),
        pydantic.Field(alias="parentHash", description="hash of previous block"),
    ] = None
    """
    hash of previous block
    """

    miner: typing.Optional[str] = pydantic.Field(default=None)
    """
    address of block's winning miner
    """

    difficulty: typing.Optional[float] = pydantic.Field(default=None)
    """
    the computational difficulty at this block
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the Unix timestamp of the object
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    transactions: typing.Optional[typing.List[Transaction]] = pydantic.Field(default=None)
    """
    a possibly empty array of transactions
    """

    base_fee_per_gas: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="baseFeePerGas"),
        pydantic.Field(alias="baseFeePerGas", description="the base fee for this block"),
    ] = None
    """
    the base fee for this block
    """

    uncles: typing.Optional[typing.List[Hash]] = pydantic.Field(default=None)
    """
    a possibly empty array of uncle hashes
    """

    withdrawals: typing.Optional[typing.List[Withdrawal]] = pydantic.Field(default=None)
    """
    a possibly empty array of withdrawals (post Shanghai)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
