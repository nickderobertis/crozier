

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisCorrelationSpectrumRequestOneAssetsItem(UniversalBaseModel):
    asset_prices: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="assetPrices"),
        pydantic.Field(
            alias="assetPrices",
            description="assetPrices[t] is the price of the asset at the time t; all the assetPrices arrays must have the same length",
        ),
    ]
    """
    assetPrices[t] is the price of the asset at the time t; all the assetPrices arrays must have the same length
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
