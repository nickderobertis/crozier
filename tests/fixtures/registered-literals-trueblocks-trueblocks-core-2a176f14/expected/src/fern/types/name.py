

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Name(UniversalBaseModel):
    """
    an association between a human-readable name and an address used throughout TrueBlocks
    """

    tags: typing.Optional[str] = pydantic.Field(default=None)
    """
    colon separated list of tags
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address associated with this name
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the name associated with this address (retrieved from on-chain data if available)
    """

    symbol: typing.Optional[str] = pydantic.Field(default=None)
    """
    the symbol for this address (retrieved from on-chain data if available)
    """

    source: typing.Optional[str] = pydantic.Field(default=None)
    """
    user supplied source of where this name was found (or on-chain if name is on-chain)
    """

    decimals: typing.Optional[int] = pydantic.Field(default=None)
    """
    number of decimals retrieved from an ERC20 smart contract, defaults to 18
    """

    deleted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    `true` if deleted, `false` otherwise
    """

    is_custom: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isCustom"),
        pydantic.Field(alias="isCustom", description="`true` if the address is a custom address, `false` otherwise"),
    ] = None
    """
    `true` if the address is a custom address, `false` otherwise
    """

    is_prefund: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPrefund"),
        pydantic.Field(
            alias="isPrefund", description="`true` if the address was one of the prefund addresses, `false` otherwise"
        ),
    ] = None
    """
    `true` if the address was one of the prefund addresses, `false` otherwise
    """

    is_contract: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isContract"),
        pydantic.Field(alias="isContract", description="`true` if the address is a smart contract, `false` otherwise"),
    ] = None
    """
    `true` if the address is a smart contract, `false` otherwise
    """

    is_erc20: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isErc20"),
        pydantic.Field(alias="isErc20", description="`true` if the address is an ERC20, `false` otherwise"),
    ] = None
    """
    `true` if the address is an ERC20, `false` otherwise
    """

    is_erc721: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isErc721"),
        pydantic.Field(alias="isErc721", description="`true` if the address is an ERC720, `false` otherwise"),
    ] = None
    """
    `true` if the address is an ERC720, `false` otherwise
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
