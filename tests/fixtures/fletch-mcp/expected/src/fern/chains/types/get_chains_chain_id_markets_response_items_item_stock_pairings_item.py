

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_markets_response_items_item_stock_pairings_item_stock_verdict import (
    GetChainsChainIdMarketsResponseItemsItemStockPairingsItemStockVerdict,
)


class GetChainsChainIdMarketsResponseItemsItemStockPairingsItem(UniversalBaseModel):
    pool_id: typing_extensions.Annotated[str, FieldMetadata(alias="poolId"), pydantic.Field(alias="poolId")]
    venue: str
    stock_symbol: typing_extensions.Annotated[
        str, FieldMetadata(alias="stockSymbol"), pydantic.Field(alias="stockSymbol")
    ]
    stock_address: typing_extensions.Annotated[
        str, FieldMetadata(alias="stockAddress"), pydantic.Field(alias="stockAddress")
    ]
    canonical_address: typing_extensions.Annotated[
        str, FieldMetadata(alias="canonicalAddress"), pydantic.Field(alias="canonicalAddress")
    ]
    stock_verdict: typing_extensions.Annotated[
        GetChainsChainIdMarketsResponseItemsItemStockPairingsItemStockVerdict,
        FieldMetadata(alias="stockVerdict"),
        pydantic.Field(alias="stockVerdict"),
    ]
    community_address: typing_extensions.Annotated[
        str, FieldMetadata(alias="communityAddress"), pydantic.Field(alias="communityAddress")
    ]
    community_symbol: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="communitySymbol"), pydantic.Field(alias="communitySymbol")
    ] = None
    observed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="observedAt"), pydantic.Field(alias="observedAt")
    ] = None
    last_swap_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastSwapAt"), pydantic.Field(alias="lastSwapAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
