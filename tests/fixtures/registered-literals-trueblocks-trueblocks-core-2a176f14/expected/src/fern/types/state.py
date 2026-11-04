

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class State(UniversalBaseModel):
    """
    the state of an Ethereum account (EOA or smart contract) on-chain
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the block number at which this call was made"),
    ] = None
    """
    the block number at which this call was made
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block for this call
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of contract being called
    """

    account_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accountType"),
        pydantic.Field(alias="accountType", description="the type of account at the given block"),
    ] = None
    """
    the type of account at the given block
    """

    balance: typing.Optional[str] = pydantic.Field(default=None)
    """
    the balance of the account at the given block
    """

    ether: typing.Optional[str] = pydantic.Field(default=None)
    """
    if --ether is specified, the balance in ether (calculated)
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    the code of the account
    """

    deployed: typing.Optional[float] = pydantic.Field(default=None)
    """
    for smart contracts only, the block number at which the contract was deployed
    """

    nonce: typing.Optional[float] = pydantic.Field(default=None)
    """
    the nonce of the account at the given block
    """

    proxy: typing.Optional[str] = pydantic.Field(default=None)
    """
    the proxy address of the account at the given block
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
