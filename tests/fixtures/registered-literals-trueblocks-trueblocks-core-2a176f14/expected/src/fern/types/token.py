

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Token(UniversalBaseModel):
    """
    on-chain token-related data such as totalSupply, symbol, decimals, and individual balances for a given address at a given block
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the block at which the report is made"),
    ] = None
    """
    the block at which the report is made
    """

    transaction_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="transactionIndex"),
        pydantic.Field(
            alias="transactionIndex", description="the transaction index (if applicable) at which the report is made"
        ),
    ] = None
    """
    the transaction index (if applicable) at which the report is made
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    total_supply: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totalSupply"),
        pydantic.Field(alias="totalSupply", description="the total supply of the token contract"),
    ] = None
    """
    the total supply of the token contract
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of the token contract
    """

    holder: typing.Optional[str] = pydantic.Field(default=None)
    """
    the holder address for which we are reporting
    """

    prior_balance: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="priorBalance"),
        pydantic.Field(alias="priorBalance", description="the holder's asset balance at its prior appearance"),
    ] = None
    """
    the holder's asset balance at its prior appearance
    """

    balance: typing.Optional[str] = pydantic.Field(default=None)
    """
    the holder's asset balance at the given block height
    """

    balance_dec: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="balanceDec"),
        pydantic.Field(
            alias="balanceDec",
            description="the holder's asset balance (in Ether) at the given block height (calculated)",
        ),
    ] = None
    """
    the holder's asset balance (in Ether) at the given block height (calculated)
    """

    diff: typing.Optional[str] = pydantic.Field(default=None)
    """
    the difference, if any, between the prior and current balance (calculated)
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name of the token contract, if available
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    the symbol of the token contract
    """

    decimals: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of decimals for the token contract
    """

    type: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    the type of token (ERC20 or ERC721) or none
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
