

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod(enum.StrEnum):
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
        if self is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod.SINGLE_LINKAGE:
            return single_linkage()
        if (
            self
            is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod.AVERAGE_LINKAGE
        ):
            return average_linkage()
        if (
            self
            is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod.COMPLETE_LINKAGE
        ):
            return complete_linkage()
        if self is PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod.WARD_LINKAGE:
            return ward_linkage()
