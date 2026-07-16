

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering(str, enum.Enum):
    """
    The order to impose on the hierarchical clustering tree leaves
    """

    R_HCLUST = "r-hclust"
    OPTIMAL = "optimal"

    def visit(self, r_hclust: typing.Callable[[], T_Result], optimal: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering.R_HCLUST:
            return r_hclust()
        if self is PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering.OPTIMAL:
            return optimal()
