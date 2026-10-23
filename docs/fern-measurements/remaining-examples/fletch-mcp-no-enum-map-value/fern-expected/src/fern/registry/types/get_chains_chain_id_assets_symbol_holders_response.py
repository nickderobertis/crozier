

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_assets_symbol_holders_response_holders_item import (
    GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem,
)


class GetChainsChainIdAssetsSymbolHoldersResponse(UniversalBaseModel):
    symbol: typing.Optional[str] = None
    decimals: typing.Optional[int] = None
    total_supply_raw: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="totalSupplyRaw"),
        pydantic.Field(
            alias="totalSupplyRaw", description="Live total supply in base units, the denominator of sharePct"
        ),
    ] = None
    """
    Live total supply in base units, the denominator of sharePct
    """

    holders: typing.Optional[typing.List[GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem]] = None
    holder_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="holderCount"), pydantic.Field(alias="holderCount")
    ] = None
    concentration: typing.Optional[typing.Dict[str, typing.Any]] = None
    progress: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
