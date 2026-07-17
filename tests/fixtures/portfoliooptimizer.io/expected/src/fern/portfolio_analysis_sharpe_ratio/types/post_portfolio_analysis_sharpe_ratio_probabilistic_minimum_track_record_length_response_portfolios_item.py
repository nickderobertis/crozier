

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponsePortfoliosItem(UniversalBaseModel):
    portfolio_sharpe_ratio_minimum_track_record_length: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="portfolioSharpeRatioMinimumTrackRecordLength"),
        pydantic.Field(
            alias="portfolioSharpeRatioMinimumTrackRecordLength",
            description="The minimum track record length of the portfolio, in number of required arithmetic returns, possibly equal to null in case the minimum track record length does not exist",
        ),
    ]
    """
    The minimum track record length of the portfolio, in number of required arithmetic returns, possibly equal to null in case the minimum track record length does not exist
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
