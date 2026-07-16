

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_assets_prices_adjusted_forward_request_assets_item_asset_dividends_item import (
    PostAssetsPricesAdjustedForwardRequestAssetsItemAssetDividendsItem,
)
from .post_assets_prices_adjusted_forward_request_assets_item_asset_prices_item import (
    PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem,
)
from .post_assets_prices_adjusted_forward_request_assets_item_asset_splits_item import (
    PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem,
)


class PostAssetsPricesAdjustedForwardRequestAssetsItem(UniversalBaseModel):
    asset_dividends: typing_extensions.Annotated[
        typing.Optional[typing.List[PostAssetsPricesAdjustedForwardRequestAssetsItemAssetDividendsItem]],
        FieldMetadata(alias="assetDividends"),
        pydantic.Field(
            alias="assetDividends",
            description="assetDividends[t] contains dividend information for the asset at the date t",
        ),
    ] = None
    """
    assetDividends[t] contains dividend information for the asset at the date t
    """

    asset_prices: typing_extensions.Annotated[
        typing.List[PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem],
        FieldMetadata(alias="assetPrices"),
        pydantic.Field(
            alias="assetPrices", description="assetPrices[t] contains price information for the asset at the date t"
        ),
    ]
    """
    assetPrices[t] contains price information for the asset at the date t
    """

    asset_splits: typing_extensions.Annotated[
        typing.Optional[typing.List[PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem]],
        FieldMetadata(alias="assetSplits"),
        pydantic.Field(
            alias="assetSplits", description="assetSplits[t] contains split information for the asset at the date t"
        ),
    ] = None
    """
    assetSplits[t] contains split information for the asset at the date t
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
