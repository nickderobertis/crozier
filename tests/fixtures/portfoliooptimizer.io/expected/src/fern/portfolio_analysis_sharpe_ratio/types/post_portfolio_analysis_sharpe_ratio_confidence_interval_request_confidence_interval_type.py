

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType(str, enum.Enum):
    """
    The type of confidence interval to build
    """

    TWO_SIDED = "twoSided"
    LOWER_ONE_SIDED = "lowerOneSided"
    UPPER_ONE_SIDED = "upperOneSided"

    def visit(
        self,
        two_sided: typing.Callable[[], T_Result],
        lower_one_sided: typing.Callable[[], T_Result],
        upper_one_sided: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType.TWO_SIDED:
            return two_sided()
        if self is PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType.LOWER_ONE_SIDED:
            return lower_one_sided()
        if self is PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType.UPPER_ONE_SIDED:
            return upper_one_sided()
