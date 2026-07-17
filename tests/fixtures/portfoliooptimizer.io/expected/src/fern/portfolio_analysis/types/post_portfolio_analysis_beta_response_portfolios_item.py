

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisBetaResponsePortfoliosItem(UniversalBaseModel):
    portfolio_beta: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="portfolioBeta"),
        pydantic.Field(
            alias="portfolioBeta",
            description="The portfolio beta, which correponds to the portfolio systematic risk in the Capital Asset Pricing Model (CAPM)",
        ),
    ]
    """
    The portfolio beta, which correponds to the portfolio systematic risk in the Capital Asset Pricing Model (CAPM)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
