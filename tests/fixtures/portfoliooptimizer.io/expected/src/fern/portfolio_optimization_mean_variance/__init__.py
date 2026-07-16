



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
        PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
        PostPortfolioOptimizationMaximumReturnRequestConstraints,
        PostPortfolioOptimizationMaximumReturnResponse,
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints,
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
        PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints,
        PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
        PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints,
        PostPortfolioOptimizationMaximumSharpeRatioResponse,
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints,
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
        PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
        PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        PostPortfolioOptimizationMeanVarianceEfficientResponse,
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
        PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
        PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
        PostPortfolioOptimizationMinimumVarianceRequestConstraints,
        PostPortfolioOptimizationMinimumVarianceResponse,
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumReturnDiversifiedResponse": ".types",
    "PostPortfolioOptimizationMaximumReturnRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumReturnResponse": ".types",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".types",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".types",
    "PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioResponse": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".types",
    "PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientResponse": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".types",
    "PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse": ".types",
    "PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints": ".types",
    "PostPortfolioOptimizationMinimumVarianceDiversifiedResponse": ".types",
    "PostPortfolioOptimizationMinimumVarianceRequestConstraints": ".types",
    "PostPortfolioOptimizationMinimumVarianceResponse": ".types",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints": ".types",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod": ".types",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod": ".types",
    "PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse": ".types",
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
