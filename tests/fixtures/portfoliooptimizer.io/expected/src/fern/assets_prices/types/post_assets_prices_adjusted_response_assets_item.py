

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_assets_prices_adjusted_response_assets_item_asset_adjusted_prices_item import (
    PostAssetsPricesAdjustedResponseAssetsItemAssetAdjustedPricesItem,
)


class PostAssetsPricesAdjustedResponseAssetsItem(UniversalBaseModel):
    asset_adjusted_prices: typing_extensions.Annotated[
        typing.List[PostAssetsPricesAdjustedResponseAssetsItemAssetAdjustedPricesItem],
        FieldMetadata(alias="assetAdjustedPrices"),
        pydantic.Field(
            alias="assetAdjustedPrices",
            description="assetAdjustedPrices[t] contains adjusted price information for the asset at the date t",
        ),
    ]
    """
    assetAdjustedPrices[t] contains adjusted price information for the asset at the date t
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
