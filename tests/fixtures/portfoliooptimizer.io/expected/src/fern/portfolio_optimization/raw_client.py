

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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


class RawPortfolioOptimizationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def equal_risk_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationEqualRiskContributionsResponse]:
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
        HttpResponse[PostPortfolioOptimizationEqualRiskContributionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-risk-contributions",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualRiskContributionsResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualRiskContributionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def equal_sharpe_ratio_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationEqualSharpeRatioContributionsResponse]:
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
        HttpResponse[PostPortfolioOptimizationEqualSharpeRatioContributionsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-sharpe-ratio-contributions",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def equal_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationEqualVolatilityWeightedResponse]:
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
        HttpResponse[PostPortfolioOptimizationEqualVolatilityWeightedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-volatility-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsVolatilities": assets_volatilities,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualVolatilityWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualVolatilityWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def equal_weighted_portfolio(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostPortfolioOptimizationEqualWeightedResponse]:
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
        HttpResponse[PostPortfolioOptimizationEqualWeightedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-weighted",
            method="POST",
            json={
                "assets": assets,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PostPortfolioOptimizationHierarchicalRiskParityResponse]:
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
        HttpResponse[PostPortfolioOptimizationHierarchicalRiskParityResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/hierarchical-risk-parity",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "clusteringMethod": clustering_method,
                "clusteringOrdering": clustering_ordering,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationHierarchicalRiskParityResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationHierarchicalRiskParityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse]:
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
        HttpResponse[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/hierarchical-risk-parity/clustering-based",
            method="POST",
            json={
                "acrossClusterAllocationMethod": across_cluster_allocation_method,
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "clusteringMethod": clustering_method,
                "clusteringOrdering": clustering_ordering,
                "clusters": clusters,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
                    direction="write",
                ),
                "withinClusterAllocationMethod": within_cluster_allocation_method,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def inverse_variance_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_variances: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationInverseVarianceWeightedResponse]:
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
        HttpResponse[PostPortfolioOptimizationInverseVarianceWeightedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/inverse-variance-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsVariances": assets_variances,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationInverseVarianceWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationInverseVarianceWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def inverse_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationInverseVolatilityWeightedResponse]:
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
        HttpResponse[PostPortfolioOptimizationInverseVolatilityWeightedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/inverse-volatility-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsVolatilities": assets_volatilities,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationInverseVolatilityWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationInverseVolatilityWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def market_capitalization_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_market_capitalizations: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMarketCapitalizationWeightedResponse]:
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
        HttpResponse[PostPortfolioOptimizationMarketCapitalizationWeightedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/market-capitalization-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsMarketCapitalizations": assets_market_capitalizations,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def maximum_decorrelation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumDecorrelationResponse]:
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
        HttpResponse[PostPortfolioOptimizationMaximumDecorrelationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-decorrelation",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumDecorrelationRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMaximumDecorrelationResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumDecorrelationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def maximum_ulcer_performance_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse]:
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
        HttpResponse[PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-ulcer-performance-index",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem],
                    direction="write",
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints,
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def minimum_correlation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMinimumCorrelationResponse]:
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
        HttpResponse[PostPortfolioOptimizationMinimumCorrelationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-correlation",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsVolatilities": assets_volatilities,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMinimumCorrelationResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumCorrelationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def minimum_ulcer_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem],
        constraints: typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMinimumUlcerIndexResponse]:
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
        HttpResponse[PostPortfolioOptimizationMinimumUlcerIndexResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-ulcer-index",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem],
                    direction="write",
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMinimumUlcerIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumUlcerIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def most_diversified_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMostDiversifiedResponse]:
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
        HttpResponse[PostPortfolioOptimizationMostDiversifiedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/most-diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMostDiversifiedRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMostDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMostDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPortfolioOptimizationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def equal_risk_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationEqualRiskContributionsResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationEqualRiskContributionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-risk-contributions",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationEqualRiskContributionsRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualRiskContributionsResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualRiskContributionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def equal_sharpe_ratio_contributions_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationEqualSharpeRatioContributionsResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationEqualSharpeRatioContributionsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-sharpe-ratio-contributions",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualSharpeRatioContributionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def equal_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationEqualVolatilityWeightedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationEqualVolatilityWeightedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-volatility-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsVolatilities": assets_volatilities,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualVolatilityWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualVolatilityWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def equal_weighted_portfolio(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostPortfolioOptimizationEqualWeightedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationEqualWeightedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/equal-weighted",
            method="POST",
            json={
                "assets": assets,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationEqualWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationEqualWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PostPortfolioOptimizationHierarchicalRiskParityResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationHierarchicalRiskParityResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/hierarchical-risk-parity",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "clusteringMethod": clustering_method,
                "clusteringOrdering": clustering_ordering,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationHierarchicalRiskParityResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationHierarchicalRiskParityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/hierarchical-risk-parity/clustering-based",
            method="POST",
            json={
                "acrossClusterAllocationMethod": across_cluster_allocation_method,
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "clusteringMethod": clustering_method,
                "clusteringOrdering": clustering_ordering,
                "clusters": clusters,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints,
                    direction="write",
                ),
                "withinClusterAllocationMethod": within_cluster_allocation_method,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def inverse_variance_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_variances: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationInverseVarianceWeightedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationInverseVarianceWeightedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/inverse-variance-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsVariances": assets_variances,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationInverseVarianceWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationInverseVarianceWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def inverse_volatility_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationInverseVolatilityWeightedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationInverseVolatilityWeightedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/inverse-volatility-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsVolatilities": assets_volatilities,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationInverseVolatilityWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationInverseVolatilityWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def market_capitalization_weighted_portfolio(
        self,
        *,
        assets: int,
        assets_market_capitalizations: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMarketCapitalizationWeightedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationMarketCapitalizationWeightedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/market-capitalization-weighted",
            method="POST",
            json={
                "assets": assets,
                "assetsMarketCapitalizations": assets_market_capitalizations,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMarketCapitalizationWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def maximum_decorrelation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumDecorrelationResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationMaximumDecorrelationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-decorrelation",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumDecorrelationRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMaximumDecorrelationResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumDecorrelationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def maximum_ulcer_performance_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-ulcer-performance-index",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem],
                    direction="write",
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints,
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def minimum_correlation_portfolio(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_volatilities: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMinimumCorrelationResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationMinimumCorrelationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-correlation",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsVolatilities": assets_volatilities,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMinimumCorrelationResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumCorrelationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def minimum_ulcer_index_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem],
        constraints: typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMinimumUlcerIndexResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationMinimumUlcerIndexResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-ulcer-index",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem],
                    direction="write",
                ),
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMinimumUlcerIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumUlcerIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def most_diversified_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        constraints: typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMostDiversifiedResponse]:
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
        AsyncHttpResponse[PostPortfolioOptimizationMostDiversifiedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/most-diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMostDiversifiedRequestConstraints,
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioOptimizationMostDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMostDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
