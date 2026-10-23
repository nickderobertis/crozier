

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_dex_response_venues_item_venue import GetChainsChainIdDexResponseVenuesItemVenue


class GetChainsChainIdDexResponseVenuesItem(UniversalBaseModel):
    venue: GetChainsChainIdDexResponseVenuesItemVenue
    pools: int = pydantic.Field()
    """
    Pools that trade a listed asset against a listed quote.
    """

    priced_pools: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pricedPools"),
        pydantic.Field(alias="pricedPools", description="Of those, how many the state read has put a dollar price on."),
    ]
    """
    Of those, how many the state read has put a dollar price on.
    """

    depth_usd: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="depthUsd"),
        pydantic.Field(
            alias="depthUsd",
            description="Depth in USD uses observed quote-side holdings for v3. For v4 it uses a bounded quote estimate for a 1% price move; per-pool token reserves are unavailable. Check the pool's observation time and stateCurrent flag. Venue depth is the sum over its priced pools.",
        ),
    ] = None
    """
    Depth in USD uses observed quote-side holdings for v3. For v4 it uses a bounded quote estimate for a 1% price move; per-pool token reserves are unavailable. Check the pool's observation time and stateCurrent flag. Venue depth is the sum over its priced pools.
    """

    swaps24h: typing.Optional[int] = pydantic.Field(default=None)
    """
    Swap logs in the exact indexed 24-hour window, null for incomplete or stale coverage.
    """

    volume_usd24h: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="volumeUsd24h"),
        pydantic.Field(
            alias="volumeUsd24h",
            description="USD over the same exact window using historical per-swap valuations; null when valuations are incomplete.",
        ),
    ] = None
    """
    USD over the same exact window using historical per-swap valuations; null when valuations are incomplete.
    """

    assets_priced_here: typing_extensions.Annotated[
        int, FieldMetadata(alias="assetsPricedHere"), pydantic.Field(alias="assetsPricedHere")
    ]
    checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="checkedAt"),
        pydantic.Field(alias="checkedAt", description="When the state read last priced a pool on this venue."),
    ] = None
    """
    When the state read last priced a pool on this venue.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
