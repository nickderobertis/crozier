

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod(
    enum.StrEnum
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
