

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod(
    str, enum.Enum
):
    """
    The method to aggregate the subset portfolios
    """

    AVERAGE = "average"
    MEDIAN = "median"

    def visit(self, average: typing.Callable[[], T_Result], median: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod.AVERAGE
        ):
            return average()
        if (
            self
            is PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod.MEDIAN
        ):
            return median()
