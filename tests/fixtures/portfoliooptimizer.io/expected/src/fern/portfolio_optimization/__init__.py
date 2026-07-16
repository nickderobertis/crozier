



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
        PostPortfolioOptimizationEqualRiskContributionsResponse,
        PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
        PostPortfolioOptimizationEqualVolatilityWeightedResponse,
        PostPortfolioOptimizationEqualWeightedResponse,
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod,
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod,
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering,
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod,
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
        PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod,
        PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering,
        PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
        PostPortfolioOptimizationHierarchicalRiskParityResponse,
        PostPortfolioOptimizationInverseVarianceWeightedResponse,
        PostPortfolioOptimizationInverseVolatilityWeightedResponse,
        PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
        PostPortfolioOptimizationMaximumDecorrelationRequestConstraints,
        PostPortfolioOptimizationMaximumDecorrelationResponse,
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem,
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints,
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
        PostPortfolioOptimizationMinimumCorrelationResponse,
        PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem,
        PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints,
        PostPortfolioOptimizationMinimumUlcerIndexResponse,
        PostPortfolioOptimizationMostDiversifiedRequestConstraints,
        PostPortfolioOptimizationMostDiversifiedResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioOptimizationEqualRiskContributionsRequestConstraints": ".types",
    "PostPortfolioOptimizationEqualRiskContributionsResponse": ".types",
    "PostPortfolioOptimizationEqualSharpeRatioContributionsResponse": ".types",
    "PostPortfolioOptimizationEqualVolatilityWeightedResponse": ".types",
    "PostPortfolioOptimizationEqualWeightedResponse": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints": ".types",
    "PostPortfolioOptimizationHierarchicalRiskParityResponse": ".types",
    "PostPortfolioOptimizationInverseVarianceWeightedResponse": ".types",
    "PostPortfolioOptimizationInverseVolatilityWeightedResponse": ".types",
    "PostPortfolioOptimizationMarketCapitalizationWeightedResponse": ".types",
    "PostPortfolioOptimizationMaximumDecorrelationRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumDecorrelationResponse": ".types",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem": ".types",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse": ".types",
    "PostPortfolioOptimizationMinimumCorrelationResponse": ".types",
    "PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem": ".types",
    "PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints": ".types",
    "PostPortfolioOptimizationMinimumUlcerIndexResponse": ".types",
    "PostPortfolioOptimizationMostDiversifiedRequestConstraints": ".types",
    "PostPortfolioOptimizationMostDiversifiedResponse": ".types",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "PostPortfolioOptimizationEqualRiskContributionsRequestConstraints",
    "PostPortfolioOptimizationEqualRiskContributionsResponse",
    "PostPortfolioOptimizationEqualSharpeRatioContributionsResponse",
    "PostPortfolioOptimizationEqualVolatilityWeightedResponse",
    "PostPortfolioOptimizationEqualWeightedResponse",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints",
    "PostPortfolioOptimizationHierarchicalRiskParityResponse",
    "PostPortfolioOptimizationInverseVarianceWeightedResponse",
    "PostPortfolioOptimizationInverseVolatilityWeightedResponse",
    "PostPortfolioOptimizationMarketCapitalizationWeightedResponse",
    "PostPortfolioOptimizationMaximumDecorrelationRequestConstraints",
    "PostPortfolioOptimizationMaximumDecorrelationResponse",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse",
    "PostPortfolioOptimizationMinimumCorrelationResponse",
    "PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem",
    "PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints",
    "PostPortfolioOptimizationMinimumUlcerIndexResponse",
    "PostPortfolioOptimizationMostDiversifiedRequestConstraints",
    "PostPortfolioOptimizationMostDiversifiedResponse",
]
