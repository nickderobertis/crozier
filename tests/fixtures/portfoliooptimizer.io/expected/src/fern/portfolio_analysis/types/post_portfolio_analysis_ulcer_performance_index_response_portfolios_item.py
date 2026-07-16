

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisUlcerPerformanceIndexResponsePortfoliosItem(UniversalBaseModel):
    portfolio_ulcer_performance_index: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="portfolioUlcerPerformanceIndex"),
        pydantic.Field(
            alias="portfolioUlcerPerformanceIndex", description="The Ulcer Performance Index of the portfolio"
        ),
    ]
    """
    The Ulcer Performance Index of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
