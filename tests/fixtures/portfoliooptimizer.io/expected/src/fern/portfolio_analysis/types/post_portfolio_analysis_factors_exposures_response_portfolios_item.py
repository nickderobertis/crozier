

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisFactorsExposuresResponsePortfoliosItem(UniversalBaseModel):
    portfolio_alpha: typing_extensions.Annotated[float, FieldMetadata(alias="portfolioAlpha")] = pydantic.Field()
    """
    The portfolio alpha, which correponds to the portion of the portfolio returns that cannot be explained by the portfolio factor exposures
    """

    portfolio_betas: typing_extensions.Annotated[typing.List[float], FieldMetadata(alias="portfolioBetas")] = (
        pydantic.Field()
    )
    """
    The portfolio betas, which correspond to the portfolio factor exposures
    """

    portfolio_r_squared: typing_extensions.Annotated[float, FieldMetadata(alias="portfolioRSquared")] = pydantic.Field()
    """
    The portfolio R^2, which indicates how much of the variability in the portfolio returns can be explained by the portfolio factor exposures; generally, the higher the R^2 the better the portfolio factor exposures explain the portfolio returns
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
