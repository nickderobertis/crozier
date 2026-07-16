

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisTrackingErrorResponsePortfoliosItem(UniversalBaseModel):
    portfolio_tracking_error: typing_extensions.Annotated[float, FieldMetadata(alias="portfolioTrackingError")] = (
        pydantic.Field()
    )
    """
    The tracking error of the portfolio
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
