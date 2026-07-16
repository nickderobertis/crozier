



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_portfolio_analysis_alpha_request import PostPortfolioAnalysisAlphaRequest
    from .post_portfolio_analysis_alpha_request_risk_free_rate import PostPortfolioAnalysisAlphaRequestRiskFreeRate
    from .post_portfolio_analysis_alpha_request_risk_free_rate_portfolios_item import (
        PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem,
    )
    from .post_portfolio_analysis_alpha_request_risk_free_returns import (
        PostPortfolioAnalysisAlphaRequestRiskFreeReturns,
    )
    from .post_portfolio_analysis_alpha_request_risk_free_returns_portfolios_item import (
        PostPortfolioAnalysisAlphaRequestRiskFreeReturnsPortfoliosItem,
    )
    from .post_portfolio_analysis_alpha_response import PostPortfolioAnalysisAlphaResponse
    from .post_portfolio_analysis_alpha_response_portfolios_item import PostPortfolioAnalysisAlphaResponsePortfoliosItem
    from .post_portfolio_analysis_beta_request import PostPortfolioAnalysisBetaRequest
    from .post_portfolio_analysis_beta_request_risk_free_rate import PostPortfolioAnalysisBetaRequestRiskFreeRate
    from .post_portfolio_analysis_beta_request_risk_free_rate_portfolios_item import (
        PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem,
    )
    from .post_portfolio_analysis_beta_request_risk_free_returns import PostPortfolioAnalysisBetaRequestRiskFreeReturns
    from .post_portfolio_analysis_beta_request_risk_free_returns_portfolios_item import (
        PostPortfolioAnalysisBetaRequestRiskFreeReturnsPortfoliosItem,
    )
    from .post_portfolio_analysis_beta_response import PostPortfolioAnalysisBetaResponse
    from .post_portfolio_analysis_beta_response_portfolios_item import PostPortfolioAnalysisBetaResponsePortfoliosItem
    from .post_portfolio_analysis_conditional_value_at_risk_request_portfolios_item import (
        PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_conditional_value_at_risk_response import (
        PostPortfolioAnalysisConditionalValueAtRiskResponse,
    )
    from .post_portfolio_analysis_conditional_value_at_risk_response_portfolios_item import (
        PostPortfolioAnalysisConditionalValueAtRiskResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_contributions_return_request_portfolios_item import (
        PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_contributions_return_response import PostPortfolioAnalysisContributionsReturnResponse
    from .post_portfolio_analysis_contributions_return_response_portfolios_item import (
        PostPortfolioAnalysisContributionsReturnResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_contributions_risk_request_portfolios_item import (
        PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_contributions_risk_response import PostPortfolioAnalysisContributionsRiskResponse
    from .post_portfolio_analysis_contributions_risk_response_portfolios_item import (
        PostPortfolioAnalysisContributionsRiskResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_correlation_spectrum_request import PostPortfolioAnalysisCorrelationSpectrumRequest
    from .post_portfolio_analysis_correlation_spectrum_request_assets_covariance_matrix import (
        PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix,
    )
    from .post_portfolio_analysis_correlation_spectrum_request_assets_covariance_matrix_portfolios_item import (
        PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem,
    )
    from .post_portfolio_analysis_correlation_spectrum_request_one import (
        PostPortfolioAnalysisCorrelationSpectrumRequestOne,
    )
    from .post_portfolio_analysis_correlation_spectrum_request_one_assets_item import (
        PostPortfolioAnalysisCorrelationSpectrumRequestOneAssetsItem,
    )
    from .post_portfolio_analysis_correlation_spectrum_request_one_portfolios_item import (
        PostPortfolioAnalysisCorrelationSpectrumRequestOnePortfoliosItem,
    )
    from .post_portfolio_analysis_correlation_spectrum_response import PostPortfolioAnalysisCorrelationSpectrumResponse
    from .post_portfolio_analysis_correlation_spectrum_response_portfolios_item import (
        PostPortfolioAnalysisCorrelationSpectrumResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_diversification_ratio_request import PostPortfolioAnalysisDiversificationRatioRequest
    from .post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix import (
        PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix,
    )
    from .post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix_portfolios_item import (
        PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem,
    )
    from .post_portfolio_analysis_diversification_ratio_request_one import (
        PostPortfolioAnalysisDiversificationRatioRequestOne,
    )
    from .post_portfolio_analysis_diversification_ratio_request_one_assets_item import (
        PostPortfolioAnalysisDiversificationRatioRequestOneAssetsItem,
    )
    from .post_portfolio_analysis_diversification_ratio_request_one_portfolios_item import (
        PostPortfolioAnalysisDiversificationRatioRequestOnePortfoliosItem,
    )
    from .post_portfolio_analysis_diversification_ratio_response import (
        PostPortfolioAnalysisDiversificationRatioResponse,
    )
    from .post_portfolio_analysis_diversification_ratio_response_portfolios_item import (
        PostPortfolioAnalysisDiversificationRatioResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_drawdowns_request_portfolios_item import (
        PostPortfolioAnalysisDrawdownsRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_drawdowns_response import PostPortfolioAnalysisDrawdownsResponse
    from .post_portfolio_analysis_drawdowns_response_portfolios_item import (
        PostPortfolioAnalysisDrawdownsResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_drawdowns_response_portfolios_item_portfolio_worst_drawdowns_item import (
        PostPortfolioAnalysisDrawdownsResponsePortfoliosItemPortfolioWorstDrawdownsItem,
    )
    from .post_portfolio_analysis_effective_number_of_bets_request_factors_extraction_method import (
        PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod,
    )
    from .post_portfolio_analysis_effective_number_of_bets_request_portfolios_item import (
        PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_effective_number_of_bets_response import (
        PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
    )
    from .post_portfolio_analysis_effective_number_of_bets_response_portfolios_item import (
        PostPortfolioAnalysisEffectiveNumberOfBetsResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_factors_exposures_request_factors_item import (
        PostPortfolioAnalysisFactorsExposuresRequestFactorsItem,
    )
    from .post_portfolio_analysis_factors_exposures_request_portfolios_item import (
        PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_factors_exposures_response import PostPortfolioAnalysisFactorsExposuresResponse
    from .post_portfolio_analysis_factors_exposures_response_portfolios_item import (
        PostPortfolioAnalysisFactorsExposuresResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_mean_variance_efficient_frontier_request_constraints import (
        PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
    )
    from .post_portfolio_analysis_mean_variance_efficient_frontier_response import (
        PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
    )
    from .post_portfolio_analysis_mean_variance_efficient_frontier_response_portfolios_item import (
        PostPortfolioAnalysisMeanVarianceEfficientFrontierResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_mean_variance_minimum_variance_frontier_request_constraints import (
        PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
    )
    from .post_portfolio_analysis_mean_variance_minimum_variance_frontier_response import (
        PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
    )
    from .post_portfolio_analysis_mean_variance_minimum_variance_frontier_response_portfolios_item import (
        PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_return_request import PostPortfolioAnalysisReturnRequest
    from .post_portfolio_analysis_return_request_assets import PostPortfolioAnalysisReturnRequestAssets
    from .post_portfolio_analysis_return_request_assets_portfolios_item import (
        PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem,
    )
    from .post_portfolio_analysis_return_request_one import PostPortfolioAnalysisReturnRequestOne
    from .post_portfolio_analysis_return_request_one_portfolios_item import (
        PostPortfolioAnalysisReturnRequestOnePortfoliosItem,
    )
    from .post_portfolio_analysis_return_response import PostPortfolioAnalysisReturnResponse
    from .post_portfolio_analysis_return_response_portfolios_item import (
        PostPortfolioAnalysisReturnResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_returns_average_request_portfolios_item import (
        PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_returns_average_response import PostPortfolioAnalysisReturnsAverageResponse
    from .post_portfolio_analysis_returns_average_response_portfolios_item import (
        PostPortfolioAnalysisReturnsAverageResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_tracking_error_request_portfolios_item import (
        PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_tracking_error_response import PostPortfolioAnalysisTrackingErrorResponse
    from .post_portfolio_analysis_tracking_error_response_portfolios_item import (
        PostPortfolioAnalysisTrackingErrorResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_ulcer_index_request_portfolios_item import (
        PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_ulcer_index_response import PostPortfolioAnalysisUlcerIndexResponse
    from .post_portfolio_analysis_ulcer_index_response_portfolios_item import (
        PostPortfolioAnalysisUlcerIndexResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_ulcer_performance_index_request_portfolios_item import (
        PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_ulcer_performance_index_response import (
        PostPortfolioAnalysisUlcerPerformanceIndexResponse,
    )
    from .post_portfolio_analysis_ulcer_performance_index_response_portfolios_item import (
        PostPortfolioAnalysisUlcerPerformanceIndexResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_value_at_risk_request_portfolios_item import (
        PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem,
    )
    from .post_portfolio_analysis_value_at_risk_response import PostPortfolioAnalysisValueAtRiskResponse
    from .post_portfolio_analysis_value_at_risk_response_portfolios_item import (
        PostPortfolioAnalysisValueAtRiskResponsePortfoliosItem,
    )
    from .post_portfolio_analysis_volatility_request import PostPortfolioAnalysisVolatilityRequest
    from .post_portfolio_analysis_volatility_request_assets import PostPortfolioAnalysisVolatilityRequestAssets
    from .post_portfolio_analysis_volatility_request_assets_portfolios_item import (
        PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem,
    )
    from .post_portfolio_analysis_volatility_request_one import PostPortfolioAnalysisVolatilityRequestOne
    from .post_portfolio_analysis_volatility_request_one_portfolios_item import (
        PostPortfolioAnalysisVolatilityRequestOnePortfoliosItem,
    )
    from .post_portfolio_analysis_volatility_response import PostPortfolioAnalysisVolatilityResponse
    from .post_portfolio_analysis_volatility_response_portfolios_item import (
        PostPortfolioAnalysisVolatilityResponsePortfoliosItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostPortfolioAnalysisAlphaRequest": ".post_portfolio_analysis_alpha_request",
    "PostPortfolioAnalysisAlphaRequestRiskFreeRate": ".post_portfolio_analysis_alpha_request_risk_free_rate",
    "PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem": ".post_portfolio_analysis_alpha_request_risk_free_rate_portfolios_item",
    "PostPortfolioAnalysisAlphaRequestRiskFreeReturns": ".post_portfolio_analysis_alpha_request_risk_free_returns",
    "PostPortfolioAnalysisAlphaRequestRiskFreeReturnsPortfoliosItem": ".post_portfolio_analysis_alpha_request_risk_free_returns_portfolios_item",
    "PostPortfolioAnalysisAlphaResponse": ".post_portfolio_analysis_alpha_response",
    "PostPortfolioAnalysisAlphaResponsePortfoliosItem": ".post_portfolio_analysis_alpha_response_portfolios_item",
    "PostPortfolioAnalysisBetaRequest": ".post_portfolio_analysis_beta_request",
    "PostPortfolioAnalysisBetaRequestRiskFreeRate": ".post_portfolio_analysis_beta_request_risk_free_rate",
    "PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem": ".post_portfolio_analysis_beta_request_risk_free_rate_portfolios_item",
    "PostPortfolioAnalysisBetaRequestRiskFreeReturns": ".post_portfolio_analysis_beta_request_risk_free_returns",
    "PostPortfolioAnalysisBetaRequestRiskFreeReturnsPortfoliosItem": ".post_portfolio_analysis_beta_request_risk_free_returns_portfolios_item",
    "PostPortfolioAnalysisBetaResponse": ".post_portfolio_analysis_beta_response",
    "PostPortfolioAnalysisBetaResponsePortfoliosItem": ".post_portfolio_analysis_beta_response_portfolios_item",
    "PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem": ".post_portfolio_analysis_conditional_value_at_risk_request_portfolios_item",
    "PostPortfolioAnalysisConditionalValueAtRiskResponse": ".post_portfolio_analysis_conditional_value_at_risk_response",
    "PostPortfolioAnalysisConditionalValueAtRiskResponsePortfoliosItem": ".post_portfolio_analysis_conditional_value_at_risk_response_portfolios_item",
    "PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem": ".post_portfolio_analysis_contributions_return_request_portfolios_item",
    "PostPortfolioAnalysisContributionsReturnResponse": ".post_portfolio_analysis_contributions_return_response",
    "PostPortfolioAnalysisContributionsReturnResponsePortfoliosItem": ".post_portfolio_analysis_contributions_return_response_portfolios_item",
    "PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem": ".post_portfolio_analysis_contributions_risk_request_portfolios_item",
    "PostPortfolioAnalysisContributionsRiskResponse": ".post_portfolio_analysis_contributions_risk_response",
    "PostPortfolioAnalysisContributionsRiskResponsePortfoliosItem": ".post_portfolio_analysis_contributions_risk_response_portfolios_item",
    "PostPortfolioAnalysisCorrelationSpectrumRequest": ".post_portfolio_analysis_correlation_spectrum_request",
    "PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix": ".post_portfolio_analysis_correlation_spectrum_request_assets_covariance_matrix",
    "PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem": ".post_portfolio_analysis_correlation_spectrum_request_assets_covariance_matrix_portfolios_item",
    "PostPortfolioAnalysisCorrelationSpectrumRequestOne": ".post_portfolio_analysis_correlation_spectrum_request_one",
    "PostPortfolioAnalysisCorrelationSpectrumRequestOneAssetsItem": ".post_portfolio_analysis_correlation_spectrum_request_one_assets_item",
    "PostPortfolioAnalysisCorrelationSpectrumRequestOnePortfoliosItem": ".post_portfolio_analysis_correlation_spectrum_request_one_portfolios_item",
    "PostPortfolioAnalysisCorrelationSpectrumResponse": ".post_portfolio_analysis_correlation_spectrum_response",
    "PostPortfolioAnalysisCorrelationSpectrumResponsePortfoliosItem": ".post_portfolio_analysis_correlation_spectrum_response_portfolios_item",
    "PostPortfolioAnalysisDiversificationRatioRequest": ".post_portfolio_analysis_diversification_ratio_request",
    "PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix": ".post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix",
    "PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem": ".post_portfolio_analysis_diversification_ratio_request_assets_covariance_matrix_portfolios_item",
    "PostPortfolioAnalysisDiversificationRatioRequestOne": ".post_portfolio_analysis_diversification_ratio_request_one",
    "PostPortfolioAnalysisDiversificationRatioRequestOneAssetsItem": ".post_portfolio_analysis_diversification_ratio_request_one_assets_item",
    "PostPortfolioAnalysisDiversificationRatioRequestOnePortfoliosItem": ".post_portfolio_analysis_diversification_ratio_request_one_portfolios_item",
    "PostPortfolioAnalysisDiversificationRatioResponse": ".post_portfolio_analysis_diversification_ratio_response",
    "PostPortfolioAnalysisDiversificationRatioResponsePortfoliosItem": ".post_portfolio_analysis_diversification_ratio_response_portfolios_item",
    "PostPortfolioAnalysisDrawdownsRequestPortfoliosItem": ".post_portfolio_analysis_drawdowns_request_portfolios_item",
    "PostPortfolioAnalysisDrawdownsResponse": ".post_portfolio_analysis_drawdowns_response",
    "PostPortfolioAnalysisDrawdownsResponsePortfoliosItem": ".post_portfolio_analysis_drawdowns_response_portfolios_item",
    "PostPortfolioAnalysisDrawdownsResponsePortfoliosItemPortfolioWorstDrawdownsItem": ".post_portfolio_analysis_drawdowns_response_portfolios_item_portfolio_worst_drawdowns_item",
    "PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod": ".post_portfolio_analysis_effective_number_of_bets_request_factors_extraction_method",
    "PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem": ".post_portfolio_analysis_effective_number_of_bets_request_portfolios_item",
    "PostPortfolioAnalysisEffectiveNumberOfBetsResponse": ".post_portfolio_analysis_effective_number_of_bets_response",
    "PostPortfolioAnalysisEffectiveNumberOfBetsResponsePortfoliosItem": ".post_portfolio_analysis_effective_number_of_bets_response_portfolios_item",
    "PostPortfolioAnalysisFactorsExposuresRequestFactorsItem": ".post_portfolio_analysis_factors_exposures_request_factors_item",
    "PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem": ".post_portfolio_analysis_factors_exposures_request_portfolios_item",
    "PostPortfolioAnalysisFactorsExposuresResponse": ".post_portfolio_analysis_factors_exposures_response",
    "PostPortfolioAnalysisFactorsExposuresResponsePortfoliosItem": ".post_portfolio_analysis_factors_exposures_response_portfolios_item",
    "PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints": ".post_portfolio_analysis_mean_variance_efficient_frontier_request_constraints",
    "PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse": ".post_portfolio_analysis_mean_variance_efficient_frontier_response",
    "PostPortfolioAnalysisMeanVarianceEfficientFrontierResponsePortfoliosItem": ".post_portfolio_analysis_mean_variance_efficient_frontier_response_portfolios_item",
    "PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints": ".post_portfolio_analysis_mean_variance_minimum_variance_frontier_request_constraints",
    "PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse": ".post_portfolio_analysis_mean_variance_minimum_variance_frontier_response",
    "PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponsePortfoliosItem": ".post_portfolio_analysis_mean_variance_minimum_variance_frontier_response_portfolios_item",
    "PostPortfolioAnalysisReturnRequest": ".post_portfolio_analysis_return_request",
    "PostPortfolioAnalysisReturnRequestAssets": ".post_portfolio_analysis_return_request_assets",
    "PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem": ".post_portfolio_analysis_return_request_assets_portfolios_item",
    "PostPortfolioAnalysisReturnRequestOne": ".post_portfolio_analysis_return_request_one",
    "PostPortfolioAnalysisReturnRequestOnePortfoliosItem": ".post_portfolio_analysis_return_request_one_portfolios_item",
    "PostPortfolioAnalysisReturnResponse": ".post_portfolio_analysis_return_response",
    "PostPortfolioAnalysisReturnResponsePortfoliosItem": ".post_portfolio_analysis_return_response_portfolios_item",
    "PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem": ".post_portfolio_analysis_returns_average_request_portfolios_item",
    "PostPortfolioAnalysisReturnsAverageResponse": ".post_portfolio_analysis_returns_average_response",
    "PostPortfolioAnalysisReturnsAverageResponsePortfoliosItem": ".post_portfolio_analysis_returns_average_response_portfolios_item",
    "PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem": ".post_portfolio_analysis_tracking_error_request_portfolios_item",
    "PostPortfolioAnalysisTrackingErrorResponse": ".post_portfolio_analysis_tracking_error_response",
    "PostPortfolioAnalysisTrackingErrorResponsePortfoliosItem": ".post_portfolio_analysis_tracking_error_response_portfolios_item",
    "PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem": ".post_portfolio_analysis_ulcer_index_request_portfolios_item",
    "PostPortfolioAnalysisUlcerIndexResponse": ".post_portfolio_analysis_ulcer_index_response",
    "PostPortfolioAnalysisUlcerIndexResponsePortfoliosItem": ".post_portfolio_analysis_ulcer_index_response_portfolios_item",
    "PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem": ".post_portfolio_analysis_ulcer_performance_index_request_portfolios_item",
    "PostPortfolioAnalysisUlcerPerformanceIndexResponse": ".post_portfolio_analysis_ulcer_performance_index_response",
    "PostPortfolioAnalysisUlcerPerformanceIndexResponsePortfoliosItem": ".post_portfolio_analysis_ulcer_performance_index_response_portfolios_item",
    "PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem": ".post_portfolio_analysis_value_at_risk_request_portfolios_item",
    "PostPortfolioAnalysisValueAtRiskResponse": ".post_portfolio_analysis_value_at_risk_response",
    "PostPortfolioAnalysisValueAtRiskResponsePortfoliosItem": ".post_portfolio_analysis_value_at_risk_response_portfolios_item",
    "PostPortfolioAnalysisVolatilityRequest": ".post_portfolio_analysis_volatility_request",
    "PostPortfolioAnalysisVolatilityRequestAssets": ".post_portfolio_analysis_volatility_request_assets",
    "PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem": ".post_portfolio_analysis_volatility_request_assets_portfolios_item",
    "PostPortfolioAnalysisVolatilityRequestOne": ".post_portfolio_analysis_volatility_request_one",
    "PostPortfolioAnalysisVolatilityRequestOnePortfoliosItem": ".post_portfolio_analysis_volatility_request_one_portfolios_item",
    "PostPortfolioAnalysisVolatilityResponse": ".post_portfolio_analysis_volatility_response",
    "PostPortfolioAnalysisVolatilityResponsePortfoliosItem": ".post_portfolio_analysis_volatility_response_portfolios_item",
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
    "PostPortfolioAnalysisAlphaRequest",
    "PostPortfolioAnalysisAlphaRequestRiskFreeRate",
    "PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem",
    "PostPortfolioAnalysisAlphaRequestRiskFreeReturns",
    "PostPortfolioAnalysisAlphaRequestRiskFreeReturnsPortfoliosItem",
    "PostPortfolioAnalysisAlphaResponse",
    "PostPortfolioAnalysisAlphaResponsePortfoliosItem",
    "PostPortfolioAnalysisBetaRequest",
    "PostPortfolioAnalysisBetaRequestRiskFreeRate",
    "PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem",
    "PostPortfolioAnalysisBetaRequestRiskFreeReturns",
    "PostPortfolioAnalysisBetaRequestRiskFreeReturnsPortfoliosItem",
    "PostPortfolioAnalysisBetaResponse",
    "PostPortfolioAnalysisBetaResponsePortfoliosItem",
    "PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem",
    "PostPortfolioAnalysisConditionalValueAtRiskResponse",
    "PostPortfolioAnalysisConditionalValueAtRiskResponsePortfoliosItem",
    "PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem",
    "PostPortfolioAnalysisContributionsReturnResponse",
    "PostPortfolioAnalysisContributionsReturnResponsePortfoliosItem",
    "PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem",
    "PostPortfolioAnalysisContributionsRiskResponse",
    "PostPortfolioAnalysisContributionsRiskResponsePortfoliosItem",
    "PostPortfolioAnalysisCorrelationSpectrumRequest",
    "PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix",
    "PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem",
    "PostPortfolioAnalysisCorrelationSpectrumRequestOne",
    "PostPortfolioAnalysisCorrelationSpectrumRequestOneAssetsItem",
    "PostPortfolioAnalysisCorrelationSpectrumRequestOnePortfoliosItem",
    "PostPortfolioAnalysisCorrelationSpectrumResponse",
    "PostPortfolioAnalysisCorrelationSpectrumResponsePortfoliosItem",
    "PostPortfolioAnalysisDiversificationRatioRequest",
    "PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix",
    "PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem",
    "PostPortfolioAnalysisDiversificationRatioRequestOne",
    "PostPortfolioAnalysisDiversificationRatioRequestOneAssetsItem",
    "PostPortfolioAnalysisDiversificationRatioRequestOnePortfoliosItem",
    "PostPortfolioAnalysisDiversificationRatioResponse",
    "PostPortfolioAnalysisDiversificationRatioResponsePortfoliosItem",
    "PostPortfolioAnalysisDrawdownsRequestPortfoliosItem",
    "PostPortfolioAnalysisDrawdownsResponse",
    "PostPortfolioAnalysisDrawdownsResponsePortfoliosItem",
    "PostPortfolioAnalysisDrawdownsResponsePortfoliosItemPortfolioWorstDrawdownsItem",
    "PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod",
    "PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem",
    "PostPortfolioAnalysisEffectiveNumberOfBetsResponse",
    "PostPortfolioAnalysisEffectiveNumberOfBetsResponsePortfoliosItem",
    "PostPortfolioAnalysisFactorsExposuresRequestFactorsItem",
    "PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem",
    "PostPortfolioAnalysisFactorsExposuresResponse",
    "PostPortfolioAnalysisFactorsExposuresResponsePortfoliosItem",
    "PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints",
    "PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse",
    "PostPortfolioAnalysisMeanVarianceEfficientFrontierResponsePortfoliosItem",
    "PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints",
    "PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse",
    "PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponsePortfoliosItem",
    "PostPortfolioAnalysisReturnRequest",
    "PostPortfolioAnalysisReturnRequestAssets",
    "PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem",
    "PostPortfolioAnalysisReturnRequestOne",
    "PostPortfolioAnalysisReturnRequestOnePortfoliosItem",
    "PostPortfolioAnalysisReturnResponse",
    "PostPortfolioAnalysisReturnResponsePortfoliosItem",
    "PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem",
    "PostPortfolioAnalysisReturnsAverageResponse",
    "PostPortfolioAnalysisReturnsAverageResponsePortfoliosItem",
    "PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem",
    "PostPortfolioAnalysisTrackingErrorResponse",
    "PostPortfolioAnalysisTrackingErrorResponsePortfoliosItem",
    "PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem",
    "PostPortfolioAnalysisUlcerIndexResponse",
    "PostPortfolioAnalysisUlcerIndexResponsePortfoliosItem",
    "PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem",
    "PostPortfolioAnalysisUlcerPerformanceIndexResponse",
    "PostPortfolioAnalysisUlcerPerformanceIndexResponsePortfoliosItem",
    "PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem",
    "PostPortfolioAnalysisValueAtRiskResponse",
    "PostPortfolioAnalysisValueAtRiskResponsePortfoliosItem",
    "PostPortfolioAnalysisVolatilityRequest",
    "PostPortfolioAnalysisVolatilityRequestAssets",
    "PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem",
    "PostPortfolioAnalysisVolatilityRequestOne",
    "PostPortfolioAnalysisVolatilityRequestOnePortfoliosItem",
    "PostPortfolioAnalysisVolatilityResponse",
    "PostPortfolioAnalysisVolatilityResponsePortfoliosItem",
]
