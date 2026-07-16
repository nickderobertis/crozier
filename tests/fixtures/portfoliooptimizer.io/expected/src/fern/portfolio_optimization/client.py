

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortfolioOptimizationClient, RawPortfolioOptimizationClient
from .types.post_portfolio_optimization_equal_risk_contributions_request_constraints import (
    PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
)
from .types.post_portfolio_optimization_equal_risk_contributions_response import (
    PostPortfolioOptimizationEqualRiskContributionsResponse,
)
from .types.post_portfolio_optimization_equal_sharpe_ratio_contributions_response import (
    PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
)
from .types.post_portfolio_optimization_equal_volatility_weighted_response import (
    PostPortfolioOptimizationEqualVolatilityWeightedResponse,
)
from .types.post_portfolio_optimization_equal_weighted_response import PostPortfolioOptimizationEqualWeightedResponse
from .types.post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_across_cluster_allocation_method import (
    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_method import (
    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_clustering_ordering import (
    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_constraints import (
    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_clustering_based_request_within_cluster_allocation_method import (
    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_clustering_based_response import (
    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_request_clustering_method import (
    PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_request_clustering_ordering import (
    PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_request_constraints import (
    PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
)
from .types.post_portfolio_optimization_hierarchical_risk_parity_response import (
    PostPortfolioOptimizationHierarchicalRiskParityResponse,
)
from .types.post_portfolio_optimization_inverse_variance_weighted_response import (
    PostPortfolioOptimizationInverseVarianceWeightedResponse,
)
from .types.post_portfolio_optimization_inverse_volatility_weighted_response import (
    PostPortfolioOptimizationInverseVolatilityWeightedResponse,
)
from .types.post_portfolio_optimization_market_capitalization_weighted_response import (
    PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
)
from .types.post_portfolio_optimization_maximum_decorrelation_request_constraints import (
    PostPortfolioOptimizationMaximumDecorrelationRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_decorrelation_response import (
    PostPortfolioOptimizationMaximumDecorrelationResponse,
)
from .types.post_portfolio_optimization_maximum_ulcer_performance_index_request_assets_item import (
    PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem,
)
from .types.post_portfolio_optimization_maximum_ulcer_performance_index_request_constraints import (
    PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_ulcer_performance_index_response import (
    PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
)
from .types.post_portfolio_optimization_minimum_correlation_response import (
    PostPortfolioOptimizationMinimumCorrelationResponse,
)
from .types.post_portfolio_optimization_minimum_ulcer_index_request_assets_item import (
    PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem,
)
from .types.post_portfolio_optimization_minimum_ulcer_index_request_constraints import (
    PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints,
)
from .types.post_portfolio_optimization_minimum_ulcer_index_response import (
    PostPortfolioOptimizationMinimumUlcerIndexResponse,
)
from .types.post_portfolio_optimization_most_diversified_request_constraints import (
    PostPortfolioOptimizationMostDiversifiedRequestConstraints,
)
from .types.post_portfolio_optimization_most_diversified_response import (
    PostPortfolioOptimizationMostDiversifiedResponse,
)


OMIT = typing.cast(typing.Any, ...)


class PortfolioOptimizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioOptimizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioOptimizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioOptimizationClient
        """
        return self._raw_client

    def equal_risk_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationEqualRiskContributionsResponse:
        """
        Compute the asset weights of the equal risk contributions portfolio, optionally subject to:
        * Minimum and maximum weights constraints

        References
         * [Richard, Jean-Charles and Roncalli, Thierry, Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications & Puzzles](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3331184)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualRiskContributionsResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization import (
            PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.equal_risk_contributions_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            constraints=PostPortfolioOptimizationEqualRiskContributionsRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
            ),
        )
        """
        _response = self._raw_client.equal_risk_contributions_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def equal_sharpe_ratio_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationEqualSharpeRatioContributionsResponse:
        """
        Compute the asset weights of the equal Sharpe Ratio contributions portfolio.

        References
         * [Andreas Steiner, Sharpe Ratio Contribution and Attribution Analysis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1839166")

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualSharpeRatioContributionsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.equal_sharpe_ratio_contributions_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.05, 0.02], [0.02, 0.07]],
            assets_returns=[0.05, 0.1],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.equal_sharpe_ratio_contributions_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            request_options=request_options,
        )
        return _response.data

    def equal_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationEqualVolatilityWeightedResponse:
        """
        Compute the asset weights of the equal volatility-weighted portfolio.

        References
         * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_volatilities : typing.Sequence[float]
            assetsVolatilities[i] is the volatility of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualVolatilityWeightedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.equal_volatility_weighted_portfolio(
            assets=2,
            assets_volatilities=[0.05, 0.1],
        )
        """
        _response = self._raw_client.equal_volatility_weighted_portfolio(
            assets=assets, assets_volatilities=assets_volatilities, request_options=request_options
        )
        return _response.data

    def equal_weighted_portfolio(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioOptimizationEqualWeightedResponse:
        """
        Compute the asset weights of the equal-weighted portfolio.

        References
         * [Victor DeMiguel and al., Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901?redirectedFrom=fulltext)

        Parameters
        ----------
        assets : int
            The number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualWeightedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.equal_weighted_portfolio(
            assets=2,
        )
        """
        _response = self._raw_client.equal_weighted_portfolio(assets=assets, request_options=request_options)
        return _response.data

    def hierarchical_risk_parity_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        clustering_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod
        ] = OMIT,
        clustering_ordering: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering
        ] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationHierarchicalRiskParityResponse:
        """
        Compute the asset weights of the hierarchical risk parity portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Lopez de Prado, M. (2016). Building diversified portfolios that outperform out-of-sample. Journal of Portfolio Management, 42(4), 59–69](https://jpm.pm-research.com/content/42/4/59)
         * [Johann Pfitzinger & Nico Katzke, 2019. A constrained hierarchical risk parity algorithm with cluster-based capital allocation. Working Papers 14/2019, Stellenbosch University, Department of Economics](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        clustering_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod]
            The hierarchical clustering method to use

        clustering_ordering : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering]
            The order to impose on the hierarchical clustering tree leaves

        constraints : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationHierarchicalRiskParityResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization import (
            PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.hierarchical_risk_parity_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            constraints=PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
                maximum_portfolio_exposure=0.5,
                minimum_portfolio_exposure=0.5,
            ),
        )
        """
        _response = self._raw_client.hierarchical_risk_parity_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            clustering_method=clustering_method,
            clustering_ordering=clustering_ordering,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def hierarchical_clustering_based_risk_parity_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        across_cluster_allocation_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod
        ] = OMIT,
        clustering_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod
        ] = OMIT,
        clustering_ordering: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering
        ] = OMIT,
        clusters: typing.Optional[int] = OMIT,
        constraints: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints
        ] = OMIT,
        within_cluster_allocation_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse:
        """
        Compute the asset weights of the hierarchical clustering-based risk parity portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Machine Learning for Asset Management: New Developments and Financial Applications, Emmanuel Jurczenko, Chapter 9, Harald Lohre,Carsten Rother,Kilian Axel Schäfer, Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi-asset Multi-factor Allocations](https://onlinelibrary.wiley.com/doi/10.1002/9781119751182.ch9)
         * [Thomas Raffinot, Hierarchical Clustering-Based Asset Allocation, The Journal of Portfolio Management Multi-Asset Special Issue 2018, 44 (2) 89-99](https://jpm.pm-research.com/content/44/2/89.abstract)
         * [Raffinot, Thomas, The Hierarchical Equal Risk Contribution Portfolio](https://ssrn.com/abstract=3237540)
         * [Johann Pfitzinger & Nico Katzke, 2019. A constrained hierarchical risk parity algorithm with cluster-based capital allocation. Working Papers 14/2019, Stellenbosch University, Department of Economics](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        across_cluster_allocation_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod]
            The allocation method to use across clusters

        clustering_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod]
            The hierarchical clustering method to use

        clustering_ordering : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering]
            The order to impose on the hierarchical clustering tree leaves

        clusters : typing.Optional[int]
            The number of clusters to use in the hierarchical clustering tree; if not provided, the number of clusters to use is computed using the gap statistic method, as described in the first reference

        constraints : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints]

        within_cluster_allocation_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod]
            The allocation method to use within clusters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization import (
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.hierarchical_clustering_based_risk_parity_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            constraints=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
                maximum_portfolio_exposure=0.5,
                minimum_portfolio_exposure=0.5,
            ),
        )
        """
        _response = self._raw_client.hierarchical_clustering_based_risk_parity_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            across_cluster_allocation_method=across_cluster_allocation_method,
            clustering_method=clustering_method,
            clustering_ordering=clustering_ordering,
            clusters=clusters,
            constraints=constraints,
            within_cluster_allocation_method=within_cluster_allocation_method,
            request_options=request_options,
        )
        return _response.data

    def inverse_variance_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_variances: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationInverseVarianceWeightedResponse:
        """
        Compute the asset weights of the inverse variance-weighted portfolio.

        References
         * [Raul Leote de Carvalho and al., Demystifying Equity Risk-Based Strategies: A Simple Alpha Plus Beta Description](https://doi.org/10.3905/jpm.2012.38.3.056)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_variances : typing.Sequence[float]
            assetsVariances[i] is the variance of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationInverseVarianceWeightedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.inverse_variance_weighted_portfolio(
            assets=2,
            assets_variances=[1.0, 0.5],
        )
        """
        _response = self._raw_client.inverse_variance_weighted_portfolio(
            assets=assets, assets_variances=assets_variances, request_options=request_options
        )
        return _response.data

    def inverse_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationInverseVolatilityWeightedResponse:
        """
        Compute the asset weights of the inverse volatility-weighted portfolio.

        References
         * [Raul Leote de Carvalho and al., Demystifying Equity Risk-Based Strategies: A Simple Alpha Plus Beta Description](https://doi.org/10.3905/jpm.2012.38.3.056)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_volatilities : typing.Sequence[float]
            assetsVolatilities[i] is the volatility of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationInverseVolatilityWeightedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.inverse_volatility_weighted_portfolio(
            assets=2,
            assets_volatilities=[0.05, 0.1],
        )
        """
        _response = self._raw_client.inverse_volatility_weighted_portfolio(
            assets=assets, assets_volatilities=assets_volatilities, request_options=request_options
        )
        return _response.data

    def market_capitalization_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_market_capitalizations: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMarketCapitalizationWeightedResponse:
        """
        Compute the asset weights of the market capitalization-weighted portfolio.

        References
         * [Wikipedia, Capitalization-weighted Index](https://en.wikipedia.org/wiki/Capitalization-weighted_index)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_market_capitalizations : typing.Sequence[float]
            assetsMarketCapitalizations[i] is the market capitalization of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMarketCapitalizationWeightedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.market_capitalization_weighted_portfolio(
            assets=2,
            assets_market_capitalizations=[1.0, 2.0],
        )
        """
        _response = self._raw_client.market_capitalization_weighted_portfolio(
            assets=assets, assets_market_capitalizations=assets_market_capitalizations, request_options=request_options
        )
        return _response.data

    def maximum_decorrelation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumDecorrelationResponse:
        """
        Compute the asset weights of the maximum decorrelation portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [F. Goltz, S. Sivasubramanian, Scientific Beta Maximum Decorrelation Indices](http://www.scientificbeta.com/download/file/scientific-beta-max-decorrelation-indices)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMaximumDecorrelationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.maximum_decorrelation_portfolio(
            assets=3,
            assets_correlation_matrix=[
                [1.0, 0.9, 0.85],
                [0.9, 1.0, 0.7],
                [0.85, 0.7, 1.0],
            ],
        )
        """
        _response = self._raw_client.maximum_decorrelation_portfolio(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def maximum_ulcer_performance_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse:
        """
        Compute the asset weights of the maximum Ulcer Performance Index portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        Notes:
        * This endpoint will return an error if the maximum Ulcer Performance Index portfolio has a negative Ulcer Performance Index

        References
         * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Portfolio Optimization with Drawdown Constraints, Supply Chain and Finance, p 209-228](https://doi.org/10.1142/9789812562586_0013)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Drawdown Measure in Portfolio Optimization, International Journal of Theoretical and Applied FinanceVol. 08, No. 01, pp. 13-58 (2005)](https://www.worldscientific.com/doi/10.1142/S0219024905002767)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem]

        risk_free_rate : float
            The risk free rate

        constraints : typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization import (
            PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.maximum_ulcer_performance_index_portfolio(
            assets=[
                PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem(
                    asset_prices=[100.0, 95.0, 110.0],
                ),
                PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem(
                    asset_prices=[100.0, 105.0, 100.0],
                ),
            ],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.maximum_ulcer_performance_index_portfolio(
            assets=assets, risk_free_rate=risk_free_rate, constraints=constraints, request_options=request_options
        )
        return _response.data

    def minimum_correlation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumCorrelationResponse:
        """
        Compute the asset weights of the (heuristic) minimum correlation portfolio, which is a portfolio built using the Minimum Correlation Algorithm discovered by [David Varadi](https://cssanalytics.wordpress.com/).

        References
         * [CSSA, Minimum Correlation Algorithm Paper Release](https://cssanalytics.wordpress.com/2012/09/21/minimum-correlation-algorithm-paper-release/)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j; required if assetsReturns is not provided

        assets_volatilities : typing.Sequence[float]
            assetsVariances[i] is the volatility of the asset i; required if assetsCorrelationMatrix is provided and assetsVariances is not provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMinimumCorrelationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.minimum_correlation_portfolio(
            assets=3,
            assets_correlation_matrix=[
                [1.0, 0.9, 0.85],
                [0.9, 1.0, 0.7],
                [0.85, 0.7, 1.0],
            ],
            assets_volatilities=[0.14, 0.18, 0.22],
        )
        """
        _response = self._raw_client.minimum_correlation_portfolio(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_volatilities=assets_volatilities,
            request_options=request_options,
        )
        return _response.data

    def minimum_ulcer_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem],
        constraints: typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumUlcerIndexResponse:
        """
        Compute the asset weights of the minimum Ulcer Index portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Portfolio Optimization with Drawdown Constraints, Supply Chain and Finance, p 209-228](https://doi.org/10.1142/9789812562586_0013)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Drawdown Measure in Portfolio Optimization, International Journal of Theoretical and Applied FinanceVol. 08, No. 01, pp. 13-58 (2005)](https://www.worldscientific.com/doi/10.1142/S0219024905002767)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem]

        constraints : typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMinimumUlcerIndexResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization import (
            PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.minimum_ulcer_index_portfolio(
            assets=[
                PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem(
                    asset_prices=[100.0, 95.0, 110.0],
                ),
                PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem(
                    asset_prices=[100.0, 105.0, 100.0],
                ),
            ],
        )
        """
        _response = self._raw_client.minimum_ulcer_index_portfolio(
            assets=assets, constraints=constraints, request_options=request_options
        )
        return _response.data

    def most_diversified_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMostDiversifiedResponse:
        """
        Compute the asset weights of the most diversified portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMostDiversifiedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization.most_diversified_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.04, 0.01], [0.01, 0.01]],
        )
        """
        _response = self._raw_client.most_diversified_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data


class AsyncPortfolioOptimizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioOptimizationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioOptimizationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioOptimizationClient
        """
        return self._raw_client

    async def equal_risk_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationEqualRiskContributionsResponse:
        """
        Compute the asset weights of the equal risk contributions portfolio, optionally subject to:
        * Minimum and maximum weights constraints

        References
         * [Richard, Jean-Charles and Roncalli, Thierry, Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications & Puzzles](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3331184)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualRiskContributionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization import (
            PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.equal_risk_contributions_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                constraints=PostPortfolioOptimizationEqualRiskContributionsRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.equal_risk_contributions_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def equal_sharpe_ratio_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationEqualSharpeRatioContributionsResponse:
        """
        Compute the asset weights of the equal Sharpe Ratio contributions portfolio.

        References
         * [Andreas Steiner, Sharpe Ratio Contribution and Attribution Analysis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1839166")

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualSharpeRatioContributionsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.equal_sharpe_ratio_contributions_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.05, 0.02], [0.02, 0.07]],
                assets_returns=[0.05, 0.1],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.equal_sharpe_ratio_contributions_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            request_options=request_options,
        )
        return _response.data

    async def equal_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationEqualVolatilityWeightedResponse:
        """
        Compute the asset weights of the equal volatility-weighted portfolio.

        References
         * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_volatilities : typing.Sequence[float]
            assetsVolatilities[i] is the volatility of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualVolatilityWeightedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.equal_volatility_weighted_portfolio(
                assets=2,
                assets_volatilities=[0.05, 0.1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.equal_volatility_weighted_portfolio(
            assets=assets, assets_volatilities=assets_volatilities, request_options=request_options
        )
        return _response.data

    async def equal_weighted_portfolio(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> PostPortfolioOptimizationEqualWeightedResponse:
        """
        Compute the asset weights of the equal-weighted portfolio.

        References
         * [Victor DeMiguel and al., Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901?redirectedFrom=fulltext)

        Parameters
        ----------
        assets : int
            The number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationEqualWeightedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.equal_weighted_portfolio(
                assets=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.equal_weighted_portfolio(assets=assets, request_options=request_options)
        return _response.data

    async def hierarchical_risk_parity_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        clustering_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod
        ] = OMIT,
        clustering_ordering: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering
        ] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationHierarchicalRiskParityResponse:
        """
        Compute the asset weights of the hierarchical risk parity portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Lopez de Prado, M. (2016). Building diversified portfolios that outperform out-of-sample. Journal of Portfolio Management, 42(4), 59–69](https://jpm.pm-research.com/content/42/4/59)
         * [Johann Pfitzinger & Nico Katzke, 2019. A constrained hierarchical risk parity algorithm with cluster-based capital allocation. Working Papers 14/2019, Stellenbosch University, Department of Economics](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        clustering_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod]
            The hierarchical clustering method to use

        clustering_ordering : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering]
            The order to impose on the hierarchical clustering tree leaves

        constraints : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationHierarchicalRiskParityResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization import (
            PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.hierarchical_risk_parity_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                constraints=PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                    maximum_portfolio_exposure=0.5,
                    minimum_portfolio_exposure=0.5,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.hierarchical_risk_parity_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            clustering_method=clustering_method,
            clustering_ordering=clustering_ordering,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def hierarchical_clustering_based_risk_parity_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        across_cluster_allocation_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod
        ] = OMIT,
        clustering_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod
        ] = OMIT,
        clustering_ordering: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering
        ] = OMIT,
        clusters: typing.Optional[int] = OMIT,
        constraints: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints
        ] = OMIT,
        within_cluster_allocation_method: typing.Optional[
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse:
        """
        Compute the asset weights of the hierarchical clustering-based risk parity portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Machine Learning for Asset Management: New Developments and Financial Applications, Emmanuel Jurczenko, Chapter 9, Harald Lohre,Carsten Rother,Kilian Axel Schäfer, Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi-asset Multi-factor Allocations](https://onlinelibrary.wiley.com/doi/10.1002/9781119751182.ch9)
         * [Thomas Raffinot, Hierarchical Clustering-Based Asset Allocation, The Journal of Portfolio Management Multi-Asset Special Issue 2018, 44 (2) 89-99](https://jpm.pm-research.com/content/44/2/89.abstract)
         * [Raffinot, Thomas, The Hierarchical Equal Risk Contribution Portfolio](https://ssrn.com/abstract=3237540)
         * [Johann Pfitzinger & Nico Katzke, 2019. A constrained hierarchical risk parity algorithm with cluster-based capital allocation. Working Papers 14/2019, Stellenbosch University, Department of Economics](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        across_cluster_allocation_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod]
            The allocation method to use across clusters

        clustering_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod]
            The hierarchical clustering method to use

        clustering_ordering : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering]
            The order to impose on the hierarchical clustering tree leaves

        clusters : typing.Optional[int]
            The number of clusters to use in the hierarchical clustering tree; if not provided, the number of clusters to use is computed using the gap statistic method, as described in the first reference

        constraints : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints]

        within_cluster_allocation_method : typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod]
            The allocation method to use within clusters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization import (
            PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.hierarchical_clustering_based_risk_parity_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                constraints=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                    maximum_portfolio_exposure=0.5,
                    minimum_portfolio_exposure=0.5,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.hierarchical_clustering_based_risk_parity_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            across_cluster_allocation_method=across_cluster_allocation_method,
            clustering_method=clustering_method,
            clustering_ordering=clustering_ordering,
            clusters=clusters,
            constraints=constraints,
            within_cluster_allocation_method=within_cluster_allocation_method,
            request_options=request_options,
        )
        return _response.data

    async def inverse_variance_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_variances: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationInverseVarianceWeightedResponse:
        """
        Compute the asset weights of the inverse variance-weighted portfolio.

        References
         * [Raul Leote de Carvalho and al., Demystifying Equity Risk-Based Strategies: A Simple Alpha Plus Beta Description](https://doi.org/10.3905/jpm.2012.38.3.056)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_variances : typing.Sequence[float]
            assetsVariances[i] is the variance of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationInverseVarianceWeightedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.inverse_variance_weighted_portfolio(
                assets=2,
                assets_variances=[1.0, 0.5],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inverse_variance_weighted_portfolio(
            assets=assets, assets_variances=assets_variances, request_options=request_options
        )
        return _response.data

    async def inverse_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationInverseVolatilityWeightedResponse:
        """
        Compute the asset weights of the inverse volatility-weighted portfolio.

        References
         * [Raul Leote de Carvalho and al., Demystifying Equity Risk-Based Strategies: A Simple Alpha Plus Beta Description](https://doi.org/10.3905/jpm.2012.38.3.056)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_volatilities : typing.Sequence[float]
            assetsVolatilities[i] is the volatility of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationInverseVolatilityWeightedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.inverse_volatility_weighted_portfolio(
                assets=2,
                assets_volatilities=[0.05, 0.1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inverse_volatility_weighted_portfolio(
            assets=assets, assets_volatilities=assets_volatilities, request_options=request_options
        )
        return _response.data

    async def market_capitalization_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_market_capitalizations: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMarketCapitalizationWeightedResponse:
        """
        Compute the asset weights of the market capitalization-weighted portfolio.

        References
         * [Wikipedia, Capitalization-weighted Index](https://en.wikipedia.org/wiki/Capitalization-weighted_index)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_market_capitalizations : typing.Sequence[float]
            assetsMarketCapitalizations[i] is the market capitalization of the asset i

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMarketCapitalizationWeightedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.market_capitalization_weighted_portfolio(
                assets=2,
                assets_market_capitalizations=[1.0, 2.0],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.market_capitalization_weighted_portfolio(
            assets=assets, assets_market_capitalizations=assets_market_capitalizations, request_options=request_options
        )
        return _response.data

    async def maximum_decorrelation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumDecorrelationResponse:
        """
        Compute the asset weights of the maximum decorrelation portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [F. Goltz, S. Sivasubramanian, Scientific Beta Maximum Decorrelation Indices](http://www.scientificbeta.com/download/file/scientific-beta-max-decorrelation-indices)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMaximumDecorrelationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.maximum_decorrelation_portfolio(
                assets=3,
                assets_correlation_matrix=[
                    [1.0, 0.9, 0.85],
                    [0.9, 1.0, 0.7],
                    [0.85, 0.7, 1.0],
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.maximum_decorrelation_portfolio(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def maximum_ulcer_performance_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse:
        """
        Compute the asset weights of the maximum Ulcer Performance Index portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        Notes:
        * This endpoint will return an error if the maximum Ulcer Performance Index portfolio has a negative Ulcer Performance Index

        References
         * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Portfolio Optimization with Drawdown Constraints, Supply Chain and Finance, p 209-228](https://doi.org/10.1142/9789812562586_0013)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Drawdown Measure in Portfolio Optimization, International Journal of Theoretical and Applied FinanceVol. 08, No. 01, pp. 13-58 (2005)](https://www.worldscientific.com/doi/10.1142/S0219024905002767)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem]

        risk_free_rate : float
            The risk free rate

        constraints : typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization import (
            PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.maximum_ulcer_performance_index_portfolio(
                assets=[
                    PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem(
                        asset_prices=[100.0, 95.0, 110.0],
                    ),
                    PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem(
                        asset_prices=[100.0, 105.0, 100.0],
                    ),
                ],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.maximum_ulcer_performance_index_portfolio(
            assets=assets, risk_free_rate=risk_free_rate, constraints=constraints, request_options=request_options
        )
        return _response.data

    async def minimum_correlation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumCorrelationResponse:
        """
        Compute the asset weights of the (heuristic) minimum correlation portfolio, which is a portfolio built using the Minimum Correlation Algorithm discovered by [David Varadi](https://cssanalytics.wordpress.com/).

        References
         * [CSSA, Minimum Correlation Algorithm Paper Release](https://cssanalytics.wordpress.com/2012/09/21/minimum-correlation-algorithm-paper-release/)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j; required if assetsReturns is not provided

        assets_volatilities : typing.Sequence[float]
            assetsVariances[i] is the volatility of the asset i; required if assetsCorrelationMatrix is provided and assetsVariances is not provided

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMinimumCorrelationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.minimum_correlation_portfolio(
                assets=3,
                assets_correlation_matrix=[
                    [1.0, 0.9, 0.85],
                    [0.9, 1.0, 0.7],
                    [0.85, 0.7, 1.0],
                ],
                assets_volatilities=[0.14, 0.18, 0.22],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.minimum_correlation_portfolio(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_volatilities=assets_volatilities,
            request_options=request_options,
        )
        return _response.data

    async def minimum_ulcer_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem],
        constraints: typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumUlcerIndexResponse:
        """
        Compute the asset weights of the minimum Ulcer Index portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Portfolio Optimization with Drawdown Constraints, Supply Chain and Finance, p 209-228](https://doi.org/10.1142/9789812562586_0013)
         * [A. Chekhlov, S. Uryasev, M. Zabarankin, Drawdown Measure in Portfolio Optimization, International Journal of Theoretical and Applied FinanceVol. 08, No. 01, pp. 13-58 (2005)](https://www.worldscientific.com/doi/10.1142/S0219024905002767)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem]

        constraints : typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMinimumUlcerIndexResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization import (
            PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.minimum_ulcer_index_portfolio(
                assets=[
                    PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem(
                        asset_prices=[100.0, 95.0, 110.0],
                    ),
                    PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem(
                        asset_prices=[100.0, 105.0, 100.0],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.minimum_ulcer_index_portfolio(
            assets=assets, constraints=constraints, request_options=request_options
        )
        return _response.data

    async def most_diversified_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMostDiversifiedResponse:
        """
        Compute the asset weights of the most diversified portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioOptimizationMostDiversifiedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization.most_diversified_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.04, 0.01], [0.01, 0.01]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.most_diversified_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data
