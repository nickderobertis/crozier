

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisConditionalValueAtRiskResponsePortfoliosItem(UniversalBaseModel):
    portfolio_conditional_value_at_risk: typing_extensions.Annotated[
        float, FieldMetadata(alias="portfolioConditionalValueAtRisk")
    ] = pydantic.Field()
    """
    The conditional value at risk of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
