

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_asset_type import AssetAssetType


class Asset(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    `${chainId}:${address}`
    """

    chain_id: typing_extensions.Annotated[int, FieldMetadata(alias="chainId"), pydantic.Field(alias="chainId")]
    address: str
    symbol: str
    name: str
    asset_type: typing_extensions.Annotated[
        AssetAssetType, FieldMetadata(alias="assetType"), pydantic.Field(alias="assetType")
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
