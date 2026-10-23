

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_chains_chain_id_assets_response_assets_item_asset_type import (
    GetChainsChainIdAssetsResponseAssetsItemAssetType,
)
from .get_chains_chain_id_assets_response_assets_item_state import GetChainsChainIdAssetsResponseAssetsItemState
from .get_chains_chain_id_assets_response_assets_item_trust import GetChainsChainIdAssetsResponseAssetsItemTrust


class GetChainsChainIdAssetsResponseAssetsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    `${chainId}:${address}`
    """

    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    address: str
    symbol: str
    name: str
    asset_type: typing_extensions.Annotated[
        GetChainsChainIdAssetsResponseAssetsItemAssetType,
        FieldMetadata(alias="assetType"),
        pydantic.Field(alias="assetType"),
    ]
    decimals: int
    status: str
    source: str
    source_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="sourceUri"), pydantic.Field(alias="sourceUri")
    ] = None
    observed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="observedAt"), pydantic.Field(alias="observedAt")
    ] = None
    first_seen_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="firstSeenAt"),
        pydantic.Field(
            alias="firstSeenAt", description="When Fletch first saw the token; Robinhood publishes no listing date"
        ),
    ] = None
    """
    When Fletch first saw the token; Robinhood publishes no listing date
    """

    verified_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="verifiedAt"), pydantic.Field(alias="verifiedAt")
    ] = None
    onchain_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="onchainName"), pydantic.Field(alias="onchainName")
    ] = None
    onchain_symbol: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="onchainSymbol"), pydantic.Field(alias="onchainSymbol")
    ] = None
    onchain_decimals: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="onchainDecimals"), pydantic.Field(alias="onchainDecimals")
    ] = None
    metadata_checked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="metadataCheckedAt"),
        pydantic.Field(alias="metadataCheckedAt"),
    ] = None
    isin: typing.Optional[str] = None
    logo_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="logoUrl"), pydantic.Field(alias="logoUrl")
    ] = None
    trust: typing.Optional[GetChainsChainIdAssetsResponseAssetsItemTrust] = pydantic.Field(default=None)
    """
    Derived from the row: whether bytecode was found and the contract agrees with the listing.
    """

    state: typing.Optional[GetChainsChainIdAssetsResponseAssetsItemState] = pydantic.Field(default=None)
    """
    The asset's live state as the registry daemon last read it; every sub-block carries the time it was read.
    """

    lookalikes: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    corporate_actions: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="corporateActions"),
        pydantic.Field(alias="corporateActions"),
    ] = None
    multiplier_history: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="multiplierHistory"),
        pydantic.Field(alias="multiplierHistory"),
    ] = None
    feed_rounds: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="feedRounds"),
        pydantic.Field(alias="feedRounds"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
