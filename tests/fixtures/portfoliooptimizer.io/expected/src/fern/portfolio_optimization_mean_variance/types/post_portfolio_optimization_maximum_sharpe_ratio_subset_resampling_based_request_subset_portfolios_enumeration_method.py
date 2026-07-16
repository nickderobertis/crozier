

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod(
    enum.StrEnum
):
    """
    The method to enumerate the subset portfolios
    """

    COMPLETE = "complete"
    RANDOM_SAMPLING = "randomSampling"

    def visit(
        self, complete: typing.Callable[[], T_Result], random_sampling: typing.Callable[[], T_Result]
    ) -> T_Result:
        if (
            self
            is PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.COMPLETE
        ):
            return complete()
        if (
            self
            is PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.RANDOM_SAMPLING
        ):
            return random_sampling()
