



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_portfolio_optimization_maximum_return_diversified_request_constraints import (
        PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_return_diversified_response import (
        PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
    )
    from .post_portfolio_optimization_maximum_return_request_constraints import (
        PostPortfolioOptimizationMaximumReturnRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_return_response import PostPortfolioOptimizationMaximumReturnResponse
    from .post_portfolio_optimization_maximum_return_subset_resampling_based_request_constraints import (
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_aggregation_method import (
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
    )
    from .post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_enumeration_method import (
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
    )
    from .post_portfolio_optimization_maximum_return_subset_resampling_based_response import (
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_diversified_request_constraints import (
        PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_diversified_response import (
        PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_request_constraints import (
        PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_response import (
        PostPortfolioOptimizationMaximumSharpeRatioResponse,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_constraints import (
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_aggregation_method import (
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_enumeration_method import (
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
    )
    from .post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_response import (
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
    )
    from .post_portfolio_optimization_mean_variance_efficient_diversified_request_constraints import (
        PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
    )
    from .post_portfolio_optimization_mean_variance_efficient_diversified_response import (
        PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
    )
    from .post_portfolio_optimization_mean_variance_efficient_request_constraints import (
        PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
    )
    from .post_portfolio_optimization_mean_variance_efficient_response import (
        PostPortfolioOptimizationMeanVarianceEfficientResponse,
    )
    from .post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_constraints import (
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
    )
    from .post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_aggregation_method import (
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
    )
    from .post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_enumeration_method import (
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
    )
    from .post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_response import (
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
    )
    from .post_portfolio_optimization_minimum_variance_diversified_request_constraints import (
        PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
    )
    from .post_portfolio_optimization_minimum_variance_diversified_response import (
        PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
    )
    from .post_portfolio_optimization_minimum_variance_request_constraints import (
        PostPortfolioOptimizationMinimumVarianceRequestConstraints,
    )
    from .post_portfolio_optimization_minimum_variance_response import PostPortfolioOptimizationMinimumVarianceResponse
    from .post_portfolio_optimization_minimum_variance_subset_resampling_based_request_constraints import (
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
    )
    from .post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_aggregation_method import (
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
    )
    from .post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_enumeration_method import (
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
    )
    from .post_portfolio_optimization_minimum_variance_subset_resampling_based_response import (
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints": ".post_portfolio_optimization_maximum_return_diversified_request_constraints",
    "PostPortfolioOptimizationMaximumReturnDiversifiedResponse": ".post_portfolio_optimization_maximum_return_diversified_response",
    "PostPortfolioOptimizationMaximumReturnRequestConstraints": ".post_portfolio_optimization_maximum_return_request_constraints",
    "PostPortfolioOptimizationMaximumReturnResponse": ".post_portfolio_optimization_maximum_return_response",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints": ".post_portfolio_optimization_maximum_return_subset_resampling_based_request_constraints",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_aggregation_method",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_enumeration_method",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse": ".post_portfolio_optimization_maximum_return_subset_resampling_based_response",
    "PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints": ".post_portfolio_optimization_maximum_sharpe_ratio_diversified_request_constraints",
    "PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse": ".post_portfolio_optimization_maximum_sharpe_ratio_diversified_response",
    "PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints": ".post_portfolio_optimization_maximum_sharpe_ratio_request_constraints",
    "PostPortfolioOptimizationMaximumSharpeRatioResponse": ".post_portfolio_optimization_maximum_sharpe_ratio_response",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints": ".post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_constraints",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_aggregation_method",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_enumeration_method",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse": ".post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_response",
    "PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints": ".post_portfolio_optimization_mean_variance_efficient_diversified_request_constraints",
    "PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse": ".post_portfolio_optimization_mean_variance_efficient_diversified_response",
    "PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints": ".post_portfolio_optimization_mean_variance_efficient_request_constraints",
    "PostPortfolioOptimizationMeanVarianceEfficientResponse": ".post_portfolio_optimization_mean_variance_efficient_response",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints": ".post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_constraints",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_aggregation_method",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_enumeration_method",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse": ".post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_response",
    "PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints": ".post_portfolio_optimization_minimum_variance_diversified_request_constraints",
    "PostPortfolioOptimizationMinimumVarianceDiversifiedResponse": ".post_portfolio_optimization_minimum_variance_diversified_response",
    "PostPortfolioOptimizationMinimumVarianceRequestConstraints": ".post_portfolio_optimization_minimum_variance_request_constraints",
    "PostPortfolioOptimizationMinimumVarianceResponse": ".post_portfolio_optimization_minimum_variance_response",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints": ".post_portfolio_optimization_minimum_variance_subset_resampling_based_request_constraints",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_aggregation_method",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_enumeration_method",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse": ".post_portfolio_optimization_minimum_variance_subset_resampling_based_response",
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
    "PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints",
    "PostPortfolioOptimizationMaximumReturnDiversifiedResponse",
    "PostPortfolioOptimizationMaximumReturnRequestConstraints",
    "PostPortfolioOptimizationMaximumReturnResponse",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse",
    "PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints",
    "PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse",
    "PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints",
    "PostPortfolioOptimizationMaximumSharpeRatioResponse",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse",
    "PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints",
    "PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse",
    "PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints",
    "PostPortfolioOptimizationMeanVarianceEfficientResponse",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse",
    "PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints",
    "PostPortfolioOptimizationMinimumVarianceDiversifiedResponse",
    "PostPortfolioOptimizationMinimumVarianceRequestConstraints",
    "PostPortfolioOptimizationMinimumVarianceResponse",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse",
]
