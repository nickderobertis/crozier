

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_portfolio_analysis_return_request_assets_portfolios_item import (
    PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem,
)


class PostPortfolioAnalysisReturnRequestAssets(UniversalBaseModel):
    assets: int = pydantic.Field()
    """
    The number of assets
    """

    assets_returns: typing_extensions.Annotated[
        typing.List[float],
        FieldMetadata(alias="assetsReturns"),
        pydantic.Field(alias="assetsReturns", description="assetsReturns[i] is the arithmetic return of asset i"),
    ]
    """
    assetsReturns[i] is the arithmetic return of asset i
    """

    portfolios: typing.List[PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
