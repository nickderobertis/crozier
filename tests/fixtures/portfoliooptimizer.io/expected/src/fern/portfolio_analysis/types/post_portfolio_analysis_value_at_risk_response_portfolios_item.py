

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisValueAtRiskResponsePortfoliosItem(UniversalBaseModel):
    portfolio_value_at_risk: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="portfolioValueAtRisk"),
        pydantic.Field(alias="portfolioValueAtRisk", description="The value at risk of the portfolio"),
    ]
    """
    The value at risk of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
