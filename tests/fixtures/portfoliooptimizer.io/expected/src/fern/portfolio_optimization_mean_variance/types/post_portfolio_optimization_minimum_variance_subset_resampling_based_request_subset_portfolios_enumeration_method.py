

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod(
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
            is PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.COMPLETE
        ):
            return complete()
        if (
            self
            is PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.RANDOM_SAMPLING
        ):
            return random_sampling()
