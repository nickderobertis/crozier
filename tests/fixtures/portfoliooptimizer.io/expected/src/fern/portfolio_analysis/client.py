

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortfolioAnalysisClient, RawPortfolioAnalysisClient
from .types.post_portfolio_analysis_alpha_request import PostPortfolioAnalysisAlphaRequest
from .types.post_portfolio_analysis_alpha_response import PostPortfolioAnalysisAlphaResponse
from .types.post_portfolio_analysis_beta_request import PostPortfolioAnalysisBetaRequest
from .types.post_portfolio_analysis_beta_response import PostPortfolioAnalysisBetaResponse
from .types.post_portfolio_analysis_conditional_value_at_risk_request_portfolios_item import (
    PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_conditional_value_at_risk_response import (
    PostPortfolioAnalysisConditionalValueAtRiskResponse,
)
from .types.post_portfolio_analysis_contributions_return_request_portfolios_item import (
    PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_contributions_return_response import (
    PostPortfolioAnalysisContributionsReturnResponse,
)
from .types.post_portfolio_analysis_contributions_risk_request_portfolios_item import (
    PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_contributions_risk_response import PostPortfolioAnalysisContributionsRiskResponse
from .types.post_portfolio_analysis_correlation_spectrum_request import PostPortfolioAnalysisCorrelationSpectrumRequest
from .types.post_portfolio_analysis_correlation_spectrum_response import (
    PostPortfolioAnalysisCorrelationSpectrumResponse,
)
from .types.post_portfolio_analysis_diversification_ratio_request import (
    PostPortfolioAnalysisDiversificationRatioRequest,
)
from .types.post_portfolio_analysis_diversification_ratio_response import (
    PostPortfolioAnalysisDiversificationRatioResponse,
)
from .types.post_portfolio_analysis_drawdowns_request_portfolios_item import (
    PostPortfolioAnalysisDrawdownsRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_drawdowns_response import PostPortfolioAnalysisDrawdownsResponse
from .types.post_portfolio_analysis_effective_number_of_bets_request_factors_extraction_method import (
    PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod,
)
from .types.post_portfolio_analysis_effective_number_of_bets_request_portfolios_item import (
    PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_effective_number_of_bets_response import (
    PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
)
from .types.post_portfolio_analysis_factors_exposures_request_factors_item import (
    PostPortfolioAnalysisFactorsExposuresRequestFactorsItem,
)
from .types.post_portfolio_analysis_factors_exposures_request_portfolios_item import (
    PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_factors_exposures_response import PostPortfolioAnalysisFactorsExposuresResponse
from .types.post_portfolio_analysis_mean_variance_efficient_frontier_request_constraints import (
    PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
)
from .types.post_portfolio_analysis_mean_variance_efficient_frontier_response import (
    PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
)
from .types.post_portfolio_analysis_mean_variance_minimum_variance_frontier_request_constraints import (
    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
)
from .types.post_portfolio_analysis_mean_variance_minimum_variance_frontier_response import (
    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
)
from .types.post_portfolio_analysis_return_request import PostPortfolioAnalysisReturnRequest
from .types.post_portfolio_analysis_return_response import PostPortfolioAnalysisReturnResponse
from .types.post_portfolio_analysis_returns_average_request_portfolios_item import (
    PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_returns_average_response import PostPortfolioAnalysisReturnsAverageResponse
from .types.post_portfolio_analysis_tracking_error_request_portfolios_item import (
    PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_tracking_error_response import PostPortfolioAnalysisTrackingErrorResponse
from .types.post_portfolio_analysis_ulcer_index_request_portfolios_item import (
    PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_ulcer_index_response import PostPortfolioAnalysisUlcerIndexResponse
from .types.post_portfolio_analysis_ulcer_performance_index_request_portfolios_item import (
    PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_ulcer_performance_index_response import (
    PostPortfolioAnalysisUlcerPerformanceIndexResponse,
)
from .types.post_portfolio_analysis_value_at_risk_request_portfolios_item import (
    PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_value_at_risk_response import PostPortfolioAnalysisValueAtRiskResponse
from .types.post_portfolio_analysis_volatility_request import PostPortfolioAnalysisVolatilityRequest
from .types.post_portfolio_analysis_volatility_response import PostPortfolioAnalysisVolatilityResponse


OMIT = typing.cast(typing.Any, ...)


class PortfolioAnalysisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioAnalysisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioAnalysisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioAnalysisClient
        """
        return self._raw_client

    def alpha(
        self, *, request: PostPortfolioAnalysisAlphaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioAnalysisAlphaResponse:
        """
        Compute the Jensen’s alpha of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisAlphaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisAlphaResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisAlphaRequestRiskFreeRate,
            PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.alpha(
            request=PostPortfolioAnalysisAlphaRequestRiskFreeRate(
                benchmark_returns=[0.002, 0.025, 0.018, -0.011, 0.014],
                portfolios=[
                    PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem(
                        portfolio_returns=[0.003, 0.026, 0.011, -0.01, 0.015],
                    )
                ],
                risk_free_rate=0.01,
            ),
        )
        """
        _response = self._raw_client.alpha(request=request, request_options=request_options)
        return _response.data

    def beta(
        self, *, request: PostPortfolioAnalysisBetaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioAnalysisBetaResponse:
        """
        Compute the beta of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisBetaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisBetaResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisBetaRequestRiskFreeRate,
            PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.beta(
            request=PostPortfolioAnalysisBetaRequestRiskFreeRate(
                benchmark_returns=[0.002, 0.025, 0.018, -0.011, 0.014],
                portfolios=[
                    PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem(
                        portfolio_returns=[0.003, 0.026, 0.011, -0.01, 0.015],
                    )
                ],
                risk_free_rate=0.01,
            ),
        )
        """
        _response = self._raw_client.beta(request=request, request_options=request_options)
        return _response.data

    def conditional_value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisConditionalValueAtRiskResponse:
        """
        Compute the conditional value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The conditional value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisConditionalValueAtRiskResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.conditional_value_at_risk(
            alpha=0.05,
            portfolios=[
                PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
        )
        """
        _response = self._raw_client.conditional_value_at_risk(
            alpha=alpha, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    def return_contributions(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisContributionsReturnResponse:
        """
        Perform a return contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisContributionsReturnResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.return_contributions(
            assets=3,
            assets_groups=[[1, 2]],
            assets_returns=[0.01, -0.01, 0.025],
            portfolios=[
                PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem(
                    assets_weights=[0.5, 0.25, 0.25],
                )
            ],
        )
        """
        _response = self._raw_client.return_contributions(
            assets=assets,
            assets_returns=assets_returns,
            portfolios=portfolios,
            assets_groups=assets_groups,
            request_options=request_options,
        )
        return _response.data

    def risk_contributions(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisContributionsRiskResponse:
        """
        Perform a risk contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisContributionsRiskResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.risk_contributions(
            assets=3,
            assets_covariance_matrix=[
                [0.0001, 0.0, 0.0],
                [0.0, 0.0001, 0.0],
                [0.0, 0.0, 0.04],
            ],
            portfolios=[
                PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem(
                    assets_weights=[0.5, 0.25, 0.25],
                )
            ],
        )
        """
        _response = self._raw_client.risk_contributions(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            portfolios=portfolios,
            assets_groups=assets_groups,
            request_options=request_options,
        )
        return _response.data

    def correlation_spectrum(
        self,
        *,
        request: PostPortfolioAnalysisCorrelationSpectrumRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisCorrelationSpectrumResponse:
        """
        Compute the correlation spectrum of one or several portfolio(s).

        References
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisCorrelationSpectrumRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisCorrelationSpectrumResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix,
            PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.correlation_spectrum(
            request=PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                portfolios=[
                    PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem(
                        assets_weights=[0.5, 0.5],
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.correlation_spectrum(request=request, request_options=request_options)
        return _response.data

    def diversification_ratio(
        self,
        *,
        request: PostPortfolioAnalysisDiversificationRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisDiversificationRatioResponse:
        """
        Compute the diversification ratio of one or several portfolio(s).

        References
        * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisDiversificationRatioRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisDiversificationRatioResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix,
            PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.diversification_ratio(
            request=PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                portfolios=[
                    PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem(
                        assets_weights=[0.5, 0.5],
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.diversification_ratio(request=request, request_options=request_options)
        return _response.data

    def drawdowns(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisDrawdownsResponse:
        """
        Compute the drawdown function - also called the underwater equity curve -, as well as the worst 10 drawdowns of one or several portfolio(s).

        References
        * [Wikipedia, Drawdown](https://en.wikipedia.org/wiki/Drawdown_(economics))

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisDrawdownsResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisDrawdownsRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.drawdowns(
            portfolios=[
                PostPortfolioAnalysisDrawdownsRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
        )
        """
        _response = self._raw_client.drawdowns(portfolios=portfolios, request_options=request_options)
        return _response.data

    def effective_number_of_bets(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem],
        factors_extraction_method: typing.Optional[
            PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisEffectiveNumberOfBetsResponse:
        """
        Compute the effective number of bets of one or several portfolio(s).

        References
        * [Meucci, Attilio and Santangelo, Alberto and Deguest, Romain, Risk Budgeting and Diversification Based on Optimized Uncorrelated Factors (November 10, 2015)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2276632)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem]

        factors_extraction_method : typing.Optional[PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod]
            The method used to extract the uncorrelated risk factors from the asset covariance matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisEffectiveNumberOfBetsResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.effective_number_of_bets(
            assets=3,
            assets_covariance_matrix=[
                [1.0, 0.0, 0.0],
                [0.0, 286.31, 100.79],
                [0.0, 100.79, 601.36],
            ],
            portfolios=[
                PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem(
                    assets_weights=[10.96, 1.06, 0.22],
                )
            ],
        )
        """
        _response = self._raw_client.effective_number_of_bets(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            portfolios=portfolios,
            factors_extraction_method=factors_extraction_method,
            request_options=request_options,
        )
        return _response.data

    def factor_exposures(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem],
        factors: typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisFactorsExposuresResponse:
        """
        Compute the exposures of one or several portfolio(s) to a set of factors, using a returns-based linear regression analysis.

        References
        * [Measuring Factor Exposures: Uses and Abuses, Ronen Israel and Adrienne Ross, The Journal of Alternative Investments Summer 2017, 20 (1) 10-25](https://jai.pm-research.com/content/20/1/10.short)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem]

        factors : typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisFactorsExposuresResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisFactorsExposuresRequestFactorsItem,
            PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.factor_exposures(
            factors=[
                PostPortfolioAnalysisFactorsExposuresRequestFactorsItem(
                    factor_returns=[-0.00414169934, 0.01201656108, 0.0087181369],
                ),
                PostPortfolioAnalysisFactorsExposuresRequestFactorsItem(
                    factor_returns=[-0.01387258782, -0.01097961581, 0.01742002062],
                ),
            ],
            portfolios=[
                PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem(
                    portfolio_returns=[-0.04302, 0.01310372213, 0.06482589323],
                )
            ],
        )
        """
        _response = self._raw_client.factor_exposures(
            portfolios=portfolios, factors=factors, request_options=request_options
        )
        return _response.data

    def mean_variance_efficient_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse:
        """
        Compute the discretized mean-variance efficient frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance efficient frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.mean_variance_efficient_frontier(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            assets_returns=[0.01, 0.05],
            constraints=PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints(
                minimum_assets_weights=[0.2, 0.0],
            ),
            portfolios=3,
        )
        """
        _response = self._raw_client.mean_variance_efficient_frontier(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            portfolios=portfolios,
            request_options=request_options,
        )
        return _response.data

    def mean_variance_minimum_variance_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse:
        """
        Compute the discretized mean-variance minimum variance frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        > This endpoint is similar to the endpoint [`/portfolio/analysis/mean-variance/efficient-frontier`](#post-/portfolio/analysis/mean-variance/efficient-frontier), because the mean-variance efficient frontier is the "top" portion of the mean-variance minimum variance frontier.

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance minimum variance frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.mean_variance_minimum_variance_frontier(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            assets_returns=[0.01, 0.05],
            constraints=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints(
                minimum_assets_weights=[0.2, 0.0],
            ),
            portfolios=4,
        )
        """
        _response = self._raw_client.mean_variance_minimum_variance_frontier(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            portfolios=portfolios,
            request_options=request_options,
        )
        return _response.data

    def arithmetic_return(
        self, *, request: PostPortfolioAnalysisReturnRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioAnalysisReturnResponse:
        """
        Compute the arithmetic return of one or several portfolio(s) from either:
        * Portfolio assets arithmetic returns
        * Portfolio values

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisReturnRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisReturnResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisReturnRequestAssets,
            PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.arithmetic_return(
            request=PostPortfolioAnalysisReturnRequestAssets(
                assets=2,
                assets_returns=[0.01, 0.05],
                portfolios=[
                    PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem(
                        assets_weights=[1.0, 0.0],
                    ),
                    PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem(
                        assets_weights=[0.0, 1.0],
                    ),
                ],
            ),
        )
        """
        _response = self._raw_client.arithmetic_return(request=request, request_options=request_options)
        return _response.data

    def arithmetic_average_return(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisReturnsAverageResponse:
        """
        Compute the arithmetic average of the arithmetic return(s) of one or several portfolio(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisReturnsAverageResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.arithmetic_average_return(
            portfolios=[
                PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
        )
        """
        _response = self._raw_client.arithmetic_average_return(portfolios=portfolios, request_options=request_options)
        return _response.data

    def tracking_error(
        self,
        *,
        benchmark_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisTrackingErrorResponse:
        """
        Compute the tracking error between a benchmark and one or several portfolio(s).

        References
        * [Wikipedia, Tracking error](https://en.wikipedia.org/wiki/Tracking_error)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        benchmark_returns : typing.Sequence[float]
            benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays

        portfolios : typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisTrackingErrorResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.tracking_error(
            benchmark_returns=[
                0.002,
                0.025,
                0.018,
                -0.011,
                0.014,
                0.018,
                0.014,
                0.065,
                -0.015,
                0.042,
                -0.006,
                0.083,
                0.039,
                -0.038,
                -0.062,
                0.015,
                -0.048,
                0.021,
                0.06,
                0.056,
                -0.067,
                0.019,
                -0.003,
                0.0,
            ],
            portfolios=[
                PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem(
                    portfolio_returns=[
                        0.003,
                        0.026,
                        0.011,
                        -0.01,
                        0.015,
                        0.025,
                        0.016,
                        0.067,
                        -0.014,
                        0.04,
                        -0.005,
                        0.081,
                        0.04,
                        -0.037,
                        -0.061,
                        0.017,
                        -0.049,
                        -0.022,
                        0.07,
                        0.058,
                        -0.065,
                        0.024,
                        -0.005,
                        -0.009,
                    ],
                )
            ],
        )
        """
        _response = self._raw_client.tracking_error(
            benchmark_returns=benchmark_returns, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    def ulcer_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisUlcerIndexResponse:
        """
        Compute the Ulcer Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisUlcerIndexResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.ulcer_index(
            portfolios=[
                PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
            risk_free_rate=1.1,
        )
        """
        _response = self._raw_client.ulcer_index(
            portfolios=portfolios, risk_free_rate=risk_free_rate, request_options=request_options
        )
        return _response.data

    def ulcer_performance_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisUlcerPerformanceIndexResponse:
        """
        Compute the Ulcer Performance Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisUlcerPerformanceIndexResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.ulcer_performance_index(
            portfolios=[
                PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.ulcer_performance_index(
            portfolios=portfolios, risk_free_rate=risk_free_rate, request_options=request_options
        )
        return _response.data

    def value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisValueAtRiskResponse:
        """
        Compute the value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisValueAtRiskResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.value_at_risk(
            alpha=0.05,
            portfolios=[
                PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
        )
        """
        _response = self._raw_client.value_at_risk(alpha=alpha, portfolios=portfolios, request_options=request_options)
        return _response.data

    def volatility(
        self,
        *,
        request: PostPortfolioAnalysisVolatilityRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisVolatilityResponse:
        """
        Compute the volatility (i.e., standard deviation) of one or several portfolio(s) from either:
        * Portfolio assets covariance matrix
        * Portfolio values

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Finance)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisVolatilityResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis import (
            PostPortfolioAnalysisVolatilityRequestAssets,
            PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis.volatility(
            request=PostPortfolioAnalysisVolatilityRequestAssets(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                portfolios=[
                    PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem(
                        assets_weights=[1.0, 0.0],
                    ),
                    PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem(
                        assets_weights=[0.0, 1.0],
                    ),
                ],
            ),
        )
        """
        _response = self._raw_client.volatility(request=request, request_options=request_options)
        return _response.data


class AsyncPortfolioAnalysisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioAnalysisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioAnalysisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioAnalysisClient
        """
        return self._raw_client

    async def alpha(
        self, *, request: PostPortfolioAnalysisAlphaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioAnalysisAlphaResponse:
        """
        Compute the Jensen’s alpha of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisAlphaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisAlphaResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisAlphaRequestRiskFreeRate,
            PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.alpha(
                request=PostPortfolioAnalysisAlphaRequestRiskFreeRate(
                    benchmark_returns=[0.002, 0.025, 0.018, -0.011, 0.014],
                    portfolios=[
                        PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem(
                            portfolio_returns=[0.003, 0.026, 0.011, -0.01, 0.015],
                        )
                    ],
                    risk_free_rate=0.01,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alpha(request=request, request_options=request_options)
        return _response.data

    async def beta(
        self, *, request: PostPortfolioAnalysisBetaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioAnalysisBetaResponse:
        """
        Compute the beta of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisBetaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisBetaResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisBetaRequestRiskFreeRate,
            PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.beta(
                request=PostPortfolioAnalysisBetaRequestRiskFreeRate(
                    benchmark_returns=[0.002, 0.025, 0.018, -0.011, 0.014],
                    portfolios=[
                        PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem(
                            portfolio_returns=[0.003, 0.026, 0.011, -0.01, 0.015],
                        )
                    ],
                    risk_free_rate=0.01,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.beta(request=request, request_options=request_options)
        return _response.data

    async def conditional_value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisConditionalValueAtRiskResponse:
        """
        Compute the conditional value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The conditional value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisConditionalValueAtRiskResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.conditional_value_at_risk(
                alpha=0.05,
                portfolios=[
                    PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.conditional_value_at_risk(
            alpha=alpha, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    async def return_contributions(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisContributionsReturnResponse:
        """
        Perform a return contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisContributionsReturnResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.return_contributions(
                assets=3,
                assets_groups=[[1, 2]],
                assets_returns=[0.01, -0.01, 0.025],
                portfolios=[
                    PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem(
                        assets_weights=[0.5, 0.25, 0.25],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_contributions(
            assets=assets,
            assets_returns=assets_returns,
            portfolios=portfolios,
            assets_groups=assets_groups,
            request_options=request_options,
        )
        return _response.data

    async def risk_contributions(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisContributionsRiskResponse:
        """
        Perform a risk contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisContributionsRiskResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.risk_contributions(
                assets=3,
                assets_covariance_matrix=[
                    [0.0001, 0.0, 0.0],
                    [0.0, 0.0001, 0.0],
                    [0.0, 0.0, 0.04],
                ],
                portfolios=[
                    PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem(
                        assets_weights=[0.5, 0.25, 0.25],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.risk_contributions(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            portfolios=portfolios,
            assets_groups=assets_groups,
            request_options=request_options,
        )
        return _response.data

    async def correlation_spectrum(
        self,
        *,
        request: PostPortfolioAnalysisCorrelationSpectrumRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisCorrelationSpectrumResponse:
        """
        Compute the correlation spectrum of one or several portfolio(s).

        References
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisCorrelationSpectrumRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisCorrelationSpectrumResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix,
            PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.correlation_spectrum(
                request=PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix(
                    assets=2,
                    assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                    portfolios=[
                        PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem(
                            assets_weights=[0.5, 0.5],
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_spectrum(request=request, request_options=request_options)
        return _response.data

    async def diversification_ratio(
        self,
        *,
        request: PostPortfolioAnalysisDiversificationRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisDiversificationRatioResponse:
        """
        Compute the diversification ratio of one or several portfolio(s).

        References
        * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisDiversificationRatioRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisDiversificationRatioResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix,
            PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.diversification_ratio(
                request=PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix(
                    assets=2,
                    assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                    portfolios=[
                        PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem(
                            assets_weights=[0.5, 0.5],
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diversification_ratio(request=request, request_options=request_options)
        return _response.data

    async def drawdowns(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisDrawdownsResponse:
        """
        Compute the drawdown function - also called the underwater equity curve -, as well as the worst 10 drawdowns of one or several portfolio(s).

        References
        * [Wikipedia, Drawdown](https://en.wikipedia.org/wiki/Drawdown_(economics))

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisDrawdownsResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisDrawdownsRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.drawdowns(
                portfolios=[
                    PostPortfolioAnalysisDrawdownsRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drawdowns(portfolios=portfolios, request_options=request_options)
        return _response.data

    async def effective_number_of_bets(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem],
        factors_extraction_method: typing.Optional[
            PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisEffectiveNumberOfBetsResponse:
        """
        Compute the effective number of bets of one or several portfolio(s).

        References
        * [Meucci, Attilio and Santangelo, Alberto and Deguest, Romain, Risk Budgeting and Diversification Based on Optimized Uncorrelated Factors (November 10, 2015)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2276632)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem]

        factors_extraction_method : typing.Optional[PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod]
            The method used to extract the uncorrelated risk factors from the asset covariance matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisEffectiveNumberOfBetsResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.effective_number_of_bets(
                assets=3,
                assets_covariance_matrix=[
                    [1.0, 0.0, 0.0],
                    [0.0, 286.31, 100.79],
                    [0.0, 100.79, 601.36],
                ],
                portfolios=[
                    PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem(
                        assets_weights=[10.96, 1.06, 0.22],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.effective_number_of_bets(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            portfolios=portfolios,
            factors_extraction_method=factors_extraction_method,
            request_options=request_options,
        )
        return _response.data

    async def factor_exposures(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem],
        factors: typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisFactorsExposuresResponse:
        """
        Compute the exposures of one or several portfolio(s) to a set of factors, using a returns-based linear regression analysis.

        References
        * [Measuring Factor Exposures: Uses and Abuses, Ronen Israel and Adrienne Ross, The Journal of Alternative Investments Summer 2017, 20 (1) 10-25](https://jai.pm-research.com/content/20/1/10.short)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem]

        factors : typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisFactorsExposuresResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisFactorsExposuresRequestFactorsItem,
            PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.factor_exposures(
                factors=[
                    PostPortfolioAnalysisFactorsExposuresRequestFactorsItem(
                        factor_returns=[-0.00414169934, 0.01201656108, 0.0087181369],
                    ),
                    PostPortfolioAnalysisFactorsExposuresRequestFactorsItem(
                        factor_returns=[-0.01387258782, -0.01097961581, 0.01742002062],
                    ),
                ],
                portfolios=[
                    PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem(
                        portfolio_returns=[-0.04302, 0.01310372213, 0.06482589323],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.factor_exposures(
            portfolios=portfolios, factors=factors, request_options=request_options
        )
        return _response.data

    async def mean_variance_efficient_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse:
        """
        Compute the discretized mean-variance efficient frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance efficient frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.mean_variance_efficient_frontier(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                assets_returns=[0.01, 0.05],
                constraints=PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints(
                    minimum_assets_weights=[0.2, 0.0],
                ),
                portfolios=3,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mean_variance_efficient_frontier(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            portfolios=portfolios,
            request_options=request_options,
        )
        return _response.data

    async def mean_variance_minimum_variance_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse:
        """
        Compute the discretized mean-variance minimum variance frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        > This endpoint is similar to the endpoint [`/portfolio/analysis/mean-variance/efficient-frontier`](#post-/portfolio/analysis/mean-variance/efficient-frontier), because the mean-variance efficient frontier is the "top" portion of the mean-variance minimum variance frontier.

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance minimum variance frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.mean_variance_minimum_variance_frontier(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                assets_returns=[0.01, 0.05],
                constraints=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints(
                    minimum_assets_weights=[0.2, 0.0],
                ),
                portfolios=4,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mean_variance_minimum_variance_frontier(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            portfolios=portfolios,
            request_options=request_options,
        )
        return _response.data

    async def arithmetic_return(
        self, *, request: PostPortfolioAnalysisReturnRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioAnalysisReturnResponse:
        """
        Compute the arithmetic return of one or several portfolio(s) from either:
        * Portfolio assets arithmetic returns
        * Portfolio values

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisReturnRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisReturnResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisReturnRequestAssets,
            PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.arithmetic_return(
                request=PostPortfolioAnalysisReturnRequestAssets(
                    assets=2,
                    assets_returns=[0.01, 0.05],
                    portfolios=[
                        PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem(
                            assets_weights=[1.0, 0.0],
                        ),
                        PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem(
                            assets_weights=[0.0, 1.0],
                        ),
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.arithmetic_return(request=request, request_options=request_options)
        return _response.data

    async def arithmetic_average_return(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisReturnsAverageResponse:
        """
        Compute the arithmetic average of the arithmetic return(s) of one or several portfolio(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisReturnsAverageResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.arithmetic_average_return(
                portfolios=[
                    PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.arithmetic_average_return(
            portfolios=portfolios, request_options=request_options
        )
        return _response.data

    async def tracking_error(
        self,
        *,
        benchmark_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisTrackingErrorResponse:
        """
        Compute the tracking error between a benchmark and one or several portfolio(s).

        References
        * [Wikipedia, Tracking error](https://en.wikipedia.org/wiki/Tracking_error)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        benchmark_returns : typing.Sequence[float]
            benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays

        portfolios : typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisTrackingErrorResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.tracking_error(
                benchmark_returns=[
                    0.002,
                    0.025,
                    0.018,
                    -0.011,
                    0.014,
                    0.018,
                    0.014,
                    0.065,
                    -0.015,
                    0.042,
                    -0.006,
                    0.083,
                    0.039,
                    -0.038,
                    -0.062,
                    0.015,
                    -0.048,
                    0.021,
                    0.06,
                    0.056,
                    -0.067,
                    0.019,
                    -0.003,
                    0.0,
                ],
                portfolios=[
                    PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem(
                        portfolio_returns=[
                            0.003,
                            0.026,
                            0.011,
                            -0.01,
                            0.015,
                            0.025,
                            0.016,
                            0.067,
                            -0.014,
                            0.04,
                            -0.005,
                            0.081,
                            0.04,
                            -0.037,
                            -0.061,
                            0.017,
                            -0.049,
                            -0.022,
                            0.07,
                            0.058,
                            -0.065,
                            0.024,
                            -0.005,
                            -0.009,
                        ],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.tracking_error(
            benchmark_returns=benchmark_returns, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    async def ulcer_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisUlcerIndexResponse:
        """
        Compute the Ulcer Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisUlcerIndexResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.ulcer_index(
                portfolios=[
                    PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
                risk_free_rate=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ulcer_index(
            portfolios=portfolios, risk_free_rate=risk_free_rate, request_options=request_options
        )
        return _response.data

    async def ulcer_performance_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisUlcerPerformanceIndexResponse:
        """
        Compute the Ulcer Performance Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisUlcerPerformanceIndexResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.ulcer_performance_index(
                portfolios=[
                    PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ulcer_performance_index(
            portfolios=portfolios, risk_free_rate=risk_free_rate, request_options=request_options
        )
        return _response.data

    async def value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisValueAtRiskResponse:
        """
        Compute the value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisValueAtRiskResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.value_at_risk(
                alpha=0.05,
                portfolios=[
                    PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.value_at_risk(
            alpha=alpha, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    async def volatility(
        self,
        *,
        request: PostPortfolioAnalysisVolatilityRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisVolatilityResponse:
        """
        Compute the volatility (i.e., standard deviation) of one or several portfolio(s) from either:
        * Portfolio assets covariance matrix
        * Portfolio values

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Finance)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisVolatilityResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis import (
            PostPortfolioAnalysisVolatilityRequestAssets,
            PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis.volatility(
                request=PostPortfolioAnalysisVolatilityRequestAssets(
                    assets=2,
                    assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                    portfolios=[
                        PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem(
                            assets_weights=[1.0, 0.0],
                        ),
                        PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem(
                            assets_weights=[0.0, 1.0],
                        ),
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.volatility(request=request, request_options=request_options)
        return _response.data
