

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod(
    str, enum.Enum
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
            is PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.COMPLETE
        ):
            return complete()
        if (
            self
            is PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.RANDOM_SAMPLING
        ):
            return random_sampling()
