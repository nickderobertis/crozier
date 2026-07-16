



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_portfolio_optimization_equal_risk_contributions_request_constraints import (
        PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
    )
    from .post_portfolio_optimization_equal_risk_contributions_response import (
        PostPortfolioOptimizationEqualRiskContributionsResponse,
    )
    from .post_portfolio_optimization_equal_sharpe_ratio_contributions_response import (
        PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
    )
    from .post_portfolio_optimization_equal_volatility_weighted_response import (
        PostPortfolioOptimizationEqualVolatilityWeightedResponse,
    )
    from .post_portfolio_optimization_equal_weighted_response import PostPortfolioOptimizationEqualWeightedResponse
    from .post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_across_cluster_allocation_method import (
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_method import (
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_ordering import (
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_constraints import (
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_within_cluster_allocation_method import (
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_clustering_based_response import (
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_request_clustering_method import (
        PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_request_clustering_ordering import (
        PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_request_constraints import (
        PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
    )
    from .post_portfolio_optimization_hierarchical_risk_parity_response import (
        PostPortfolioOptimizationHierarchicalRiskParityResponse,
    )
    from .post_portfolio_optimization_inverse_variance_weighted_response import (
        PostPortfolioOptimizationInverseVarianceWeightedResponse,
    )
    from .post_portfolio_optimization_inverse_volatility_weighted_response import (
        PostPortfolioOptimizationInverseVolatilityWeightedResponse,
    )
    from .post_portfolio_optimization_market_capitalization_weighted_response import (
        PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
    )
    from .post_portfolio_optimization_maximum_decorrelation_request_constraints import (
        PostPortfolioOptimizationMaximumDecorrelationRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_decorrelation_response import (
        PostPortfolioOptimizationMaximumDecorrelationResponse,
    )
    from .post_portfolio_optimization_maximum_ulcer_performance_index_request_assets_item import (
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem,
    )
    from .post_portfolio_optimization_maximum_ulcer_performance_index_request_constraints import (
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_ulcer_performance_index_response import (
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
    )
    from .post_portfolio_optimization_minimum_correlation_response import (
        PostPortfolioOptimizationMinimumCorrelationResponse,
    )
    from .post_portfolio_optimization_minimum_ulcer_index_request_assets_item import (
        PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem,
    )
    from .post_portfolio_optimization_minimum_ulcer_index_request_constraints import (
        PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints,
    )
    from .post_portfolio_optimization_minimum_ulcer_index_response import (
        PostPortfolioOptimizationMinimumUlcerIndexResponse,
    )
    from .post_portfolio_optimization_most_diversified_request_constraints import (
        PostPortfolioOptimizationMostDiversifiedRequestConstraints,
    )
    from .post_portfolio_optimization_most_diversified_response import PostPortfolioOptimizationMostDiversifiedResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioOptimizationEqualRiskContributionsRequestConstraints": ".post_portfolio_optimization_equal_risk_contributions_request_constraints",
    "PostPortfolioOptimizationEqualRiskContributionsResponse": ".post_portfolio_optimization_equal_risk_contributions_response",
    "PostPortfolioOptimizationEqualSharpeRatioContributionsResponse": ".post_portfolio_optimization_equal_sharpe_ratio_contributions_response",
    "PostPortfolioOptimizationEqualVolatilityWeightedResponse": ".post_portfolio_optimization_equal_volatility_weighted_response",
    "PostPortfolioOptimizationEqualWeightedResponse": ".post_portfolio_optimization_equal_weighted_response",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod": ".post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_across_cluster_allocation_method",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod": ".post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_method",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering": ".post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_ordering",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints": ".post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_constraints",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod": ".post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_within_cluster_allocation_method",
    "PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse": ".post_portfolio_optimization_hierarchical_risk_parity_clustering_based_response",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod": ".post_portfolio_optimization_hierarchical_risk_parity_request_clustering_method",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering": ".post_portfolio_optimization_hierarchical_risk_parity_request_clustering_ordering",
    "PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints": ".post_portfolio_optimization_hierarchical_risk_parity_request_constraints",
    "PostPortfolioOptimizationHierarchicalRiskParityResponse": ".post_portfolio_optimization_hierarchical_risk_parity_response",
    "PostPortfolioOptimizationInverseVarianceWeightedResponse": ".post_portfolio_optimization_inverse_variance_weighted_response",
    "PostPortfolioOptimizationInverseVolatilityWeightedResponse": ".post_portfolio_optimization_inverse_volatility_weighted_response",
    "PostPortfolioOptimizationMarketCapitalizationWeightedResponse": ".post_portfolio_optimization_market_capitalization_weighted_response",
    "PostPortfolioOptimizationMaximumDecorrelationRequestConstraints": ".post_portfolio_optimization_maximum_decorrelation_request_constraints",
    "PostPortfolioOptimizationMaximumDecorrelationResponse": ".post_portfolio_optimization_maximum_decorrelation_response",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem": ".post_portfolio_optimization_maximum_ulcer_performance_index_request_assets_item",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints": ".post_portfolio_optimization_maximum_ulcer_performance_index_request_constraints",
    "PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse": ".post_portfolio_optimization_maximum_ulcer_performance_index_response",
    "PostPortfolioOptimizationMinimumCorrelationResponse": ".post_portfolio_optimization_minimum_correlation_response",
    "PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem": ".post_portfolio_optimization_minimum_ulcer_index_request_assets_item",
    "PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints": ".post_portfolio_optimization_minimum_ulcer_index_request_constraints",
    "PostPortfolioOptimizationMinimumUlcerIndexResponse": ".post_portfolio_optimization_minimum_ulcer_index_response",
    "PostPortfolioOptimizationMostDiversifiedRequestConstraints": ".post_portfolio_optimization_most_diversified_request_constraints",
    "PostPortfolioOptimizationMostDiversifiedResponse": ".post_portfolio_optimization_most_diversified_response",
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
