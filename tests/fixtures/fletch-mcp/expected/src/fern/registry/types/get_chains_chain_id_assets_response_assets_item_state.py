

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_assets_response_assets_item_state_feed import (
    GetChainsChainIdAssetsResponseAssetsItemStateFeed,
)
from .get_chains_chain_id_assets_response_assets_item_state_quote import (
    GetChainsChainIdAssetsResponseAssetsItemStateQuote,
)


class GetChainsChainIdAssetsResponseAssetsItemState(UniversalBaseModel):
    """
    The asset's live state as the registry daemon last read it; every sub-block carries the time it was read.
    """

    multiplier: typing.Optional[float] = None
    pending_multiplier: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="pendingMultiplier"), pydantic.Field(alias="pendingMultiplier")
    ] = None
    multiplier_effective_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="multiplierEffectiveAt"),
        pydantic.Field(alias="multiplierEffectiveAt"),
    ] = None
    token_paused: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="tokenPaused"), pydantic.Field(alias="tokenPaused")
    ] = None
    oracle_paused: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="oraclePaused"), pydantic.Field(alias="oraclePaused")
    ] = None
    total_supply_raw: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="totalSupplyRaw"), pydantic.Field(alias="totalSupplyRaw")
    ] = None
    total_supply_ui: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="totalSupplyUi"), pydantic.Field(alias="totalSupplyUi")
    ] = None
    canonical: typing.Optional[bool] = None
    beacon: typing.Optional[str] = None
    implementation: typing.Optional[str] = None
    feed: typing.Optional[GetChainsChainIdAssetsResponseAssetsItemStateFeed] = None
    quote: typing.Optional[GetChainsChainIdAssetsResponseAssetsItemStateQuote] = None
    price_divergence_pct: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="priceDivergencePct"), pydantic.Field(alias="priceDivergencePct")
    ] = None
    dex: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The deepest dollar-priced pool and its premium to the feed.
    """

    second_source: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="secondSource"),
        pydantic.Field(
            alias="secondSource",
            description="The chain explorer's holders, transfers and supply, with supplyAgreement agree|close|differ|unknown.",
        ),
    ] = None
    """
    The chain explorer's holders, transfers and supply, with supplyAgreement agree|close|differ|unknown.
    """

    checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="checkedAt"), pydantic.Field(alias="checkedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
