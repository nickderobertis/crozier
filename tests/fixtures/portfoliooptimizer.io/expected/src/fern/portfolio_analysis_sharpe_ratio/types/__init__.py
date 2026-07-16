



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_portfolio_analysis_sharpe_ratio_bias_adjusted_request_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_bias_adjusted_response import (
        PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse,
    )
    from .post_portfolio_analysis_sharpe_ratio_bias_adjusted_response_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioBiasAdjustedResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_confidence_interval_request_confidence_interval_type import (
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType,
    )
    from .post_portfolio_analysis_sharpe_ratio_confidence_interval_request_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_confidence_interval_response import (
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse,
    )
    from .post_portfolio_analysis_sharpe_ratio_confidence_interval_response_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatio,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatioPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_request import (
        PostPortfolioAnalysisSharpeRatioProbabilisticRequest,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio import (
        PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatio,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatioPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values import (
        PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_response import (
        PostPortfolioAnalysisSharpeRatioProbabilisticResponse,
    )
    from .post_portfolio_analysis_sharpe_ratio_probabilistic_response_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioProbabilisticResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_request import PostPortfolioAnalysisSharpeRatioRequest
    from .post_portfolio_analysis_sharpe_ratio_request_assets import PostPortfolioAnalysisSharpeRatioRequestAssets
    from .post_portfolio_analysis_sharpe_ratio_request_assets_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_request_one import PostPortfolioAnalysisSharpeRatioRequestOne
    from .post_portfolio_analysis_sharpe_ratio_request_one_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioRequestOnePortfoliosItem,
    )
    from .post_portfolio_analysis_sharpe_ratio_response import PostPortfolioAnalysisSharpeRatioResponse
    from .post_portfolio_analysis_sharpe_ratio_response_portfolios_item import (
        PostPortfolioAnalysisSharpeRatioResponsePortfoliosItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_bias_adjusted_request_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse": ".post_portfolio_analysis_sharpe_ratio_bias_adjusted_response",
    "PostPortfolioAnalysisSharpeRatioBiasAdjustedResponsePortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_bias_adjusted_response_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType": ".post_portfolio_analysis_sharpe_ratio_confidence_interval_request_confidence_interval_type",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_confidence_interval_request_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse": ".post_portfolio_analysis_sharpe_ratio_confidence_interval_response",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponsePortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_confidence_interval_response_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatio": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatioPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_sharpe_ratio_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request_benchmark_values_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponsePortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequest": ".post_portfolio_analysis_sharpe_ratio_probabilistic_request",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatio": ".post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatioPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_sharpe_ratio_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues": ".post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_probabilistic_request_benchmark_values_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioProbabilisticResponse": ".post_portfolio_analysis_sharpe_ratio_probabilistic_response",
    "PostPortfolioAnalysisSharpeRatioProbabilisticResponsePortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_probabilistic_response_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioRequest": ".post_portfolio_analysis_sharpe_ratio_request",
    "PostPortfolioAnalysisSharpeRatioRequestAssets": ".post_portfolio_analysis_sharpe_ratio_request_assets",
    "PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_request_assets_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioRequestOne": ".post_portfolio_analysis_sharpe_ratio_request_one",
    "PostPortfolioAnalysisSharpeRatioRequestOnePortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_request_one_portfolios_item",
    "PostPortfolioAnalysisSharpeRatioResponse": ".post_portfolio_analysis_sharpe_ratio_response",
    "PostPortfolioAnalysisSharpeRatioResponsePortfoliosItem": ".post_portfolio_analysis_sharpe_ratio_response_portfolios_item",
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
    "PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse",
    "PostPortfolioAnalysisSharpeRatioBiasAdjustedResponsePortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse",
    "PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponsePortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatio",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkSharpeRatioPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse",
    "PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponsePortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequest",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatio",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkSharpeRatioPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues",
    "PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioProbabilisticResponse",
    "PostPortfolioAnalysisSharpeRatioProbabilisticResponsePortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioRequest",
    "PostPortfolioAnalysisSharpeRatioRequestAssets",
    "PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioRequestOne",
    "PostPortfolioAnalysisSharpeRatioRequestOnePortfoliosItem",
    "PostPortfolioAnalysisSharpeRatioResponse",
    "PostPortfolioAnalysisSharpeRatioResponsePortfoliosItem",
]
