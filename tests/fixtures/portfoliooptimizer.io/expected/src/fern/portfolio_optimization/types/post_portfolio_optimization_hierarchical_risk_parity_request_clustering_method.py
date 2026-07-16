

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod(str, enum.Enum):
    """
    The hierarchical clustering method to use
    """

    SINGLE_LINKAGE = "singleLinkage"
    AVERAGE_LINKAGE = "averageLinkage"
    COMPLETE_LINKAGE = "completeLinkage"
    WARD_LINKAGE = "wardLinkage"

    def visit(
        self,
        single_linkage: typing.Callable[[], T_Result],
        average_linkage: typing.Callable[[], T_Result],
        complete_linkage: typing.Callable[[], T_Result],
        ward_linkage: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod.SINGLE_LINKAGE:
            return single_linkage()
        if self is PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod.AVERAGE_LINKAGE:
            return average_linkage()
        if self is PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod.COMPLETE_LINKAGE:
            return complete_linkage()
        if self is PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod.WARD_LINKAGE:
            return ward_linkage()
