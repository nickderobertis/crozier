

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod(
    str, enum.Enum
):
    """
    The allocation method to use within clusters
    """

    EQUAL_WEIGHTING = "equalWeighting"
    INVERSE_VOLATILITY = "inverseVolatility"
    INVERSE_VARIANCE = "inverseVariance"

    def visit(
        self,
        equal_weighting: typing.Callable[[], T_Result],
        inverse_volatility: typing.Callable[[], T_Result],
        inverse_variance: typing.Callable[[], T_Result],
    ) -> T_Result:
        if (
            self
            is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod.EQUAL_WEIGHTING
        ):
            return equal_weighting()
        if (
            self
            is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod.INVERSE_VOLATILITY
        ):
            return inverse_volatility()
        if (
            self
            is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod.INVERSE_VARIANCE
        ):
            return inverse_variance()
