

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod(enum.StrEnum):
    """
    The method to aggregate the subset portfolios
    """

    AVERAGE = "average"
    MEDIAN = "median"

    def visit(self, average: typing.Callable[[], T_Result], median: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod.AVERAGE
        ):
            return average()
        if (
            self
            is PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod.MEDIAN
        ):
            return median()
