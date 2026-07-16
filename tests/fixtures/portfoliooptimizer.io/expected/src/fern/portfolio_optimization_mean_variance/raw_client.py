

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_portfolio_optimization_maximum_return_diversified_request_constraints import (
    PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_return_diversified_response import (
    PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
)
from .types.post_portfolio_optimization_maximum_return_request_constraints import (
    PostPortfolioOptimizationMaximumReturnRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_return_response import PostPortfolioOptimizationMaximumReturnResponse
from .types.post_portfolio_optimization_maximum_return_subset_resampling_based_request_constraints import (
    PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_aggregation_method import (
    PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
)
from .types.post_portfolio_optimization_maximum_return_subset_resampling_based_request_subset_portfolios_enumeration_method import (
    PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
)
from .types.post_portfolio_optimization_maximum_return_subset_resampling_based_response import (
    PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_diversified_request_constraints import (
    PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_diversified_response import (
    PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_request_constraints import (
    PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_response import (
    PostPortfolioOptimizationMaximumSharpeRatioResponse,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_constraints import (
    PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_aggregation_method import (
    PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_request_subset_portfolios_enumeration_method import (
    PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
)
from .types.post_portfolio_optimization_maximum_sharpe_ratio_subset_resampling_based_response import (
    PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
)
from .types.post_portfolio_optimization_mean_variance_efficient_diversified_request_constraints import (
    PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
)
from .types.post_portfolio_optimization_mean_variance_efficient_diversified_response import (
    PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
)
from .types.post_portfolio_optimization_mean_variance_efficient_request_constraints import (
    PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
)
from .types.post_portfolio_optimization_mean_variance_efficient_response import (
    PostPortfolioOptimizationMeanVarianceEfficientResponse,
)
from .types.post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_constraints import (
    PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
)
from .types.post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_aggregation_method import (
    PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
)
from .types.post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_request_subset_portfolios_enumeration_method import (
    PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
)
from .types.post_portfolio_optimization_mean_variance_efficient_subset_resampling_based_response import (
    PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
)
from .types.post_portfolio_optimization_minimum_variance_diversified_request_constraints import (
    PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
)
from .types.post_portfolio_optimization_minimum_variance_diversified_response import (
    PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
)
from .types.post_portfolio_optimization_minimum_variance_request_constraints import (
    PostPortfolioOptimizationMinimumVarianceRequestConstraints,
)
from .types.post_portfolio_optimization_minimum_variance_response import (
    PostPortfolioOptimizationMinimumVarianceResponse,
)
from .types.post_portfolio_optimization_minimum_variance_subset_resampling_based_request_constraints import (
    PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
)
from .types.post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_aggregation_method import (
    PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod,
)
from .types.post_portfolio_optimization_minimum_variance_subset_resampling_based_request_subset_portfolios_enumeration_method import (
    PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
)
from .types.post_portfolio_optimization_minimum_variance_subset_resampling_based_response import (
    PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
)


OMIT = typing.cast(typing.Any, ...)


class RawPortfolioOptimizationMeanVarianceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumReturnResponse]:
        """
        Compute the asset weights of the maximum return portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        assets_covariance_matrix : typing.Optional[typing.Sequence[typing.Sequence[float]]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMaximumReturnResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-return",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumReturnRequestConstraints,
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
                    PostPortfolioOptimizationMaximumReturnResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumReturnResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def diversified_maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumReturnDiversifiedResponse]:
        """
        Compute the asset weights of the diversified maximum return portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        assets_covariance_matrix : typing.Optional[typing.Sequence[typing.Sequence[float]]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMaximumReturnDiversifiedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-return/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def subset_resampling_based_maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints
        ] = OMIT,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of the subset resampling-based maximum return portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        assets_covariance_matrix : typing.Optional[typing.Sequence[typing.Sequence[float]]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints]

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-return/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumSharpeRatioResponse]:
        """
        Compute the asset weights of the maximum Sharpe ratio portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

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

        risk_free_rate : float
            The risk free rate

        constraints : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMaximumSharpeRatioResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-sharpe-ratio",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints,
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
                    PostPortfolioOptimizationMaximumSharpeRatioResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumSharpeRatioResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def diversified_maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse]:
        """
        Compute the asset weights of the diversified maximum Sharpe ratio portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

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

        constraints : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-sharpe-ratio/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def subset_resampling_based_maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[
            PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints
        ] = OMIT,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of the susbet resampling-based maximum Sharpe ratio portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

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

        constraints : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints]

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-sharpe-ratio/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMeanVarianceEfficientResponse]:
        """
        Compute the asset weights of a mean-variance efficient portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        > A mean-variance efficient portfolio is a portfolio belonging to [the mean-variance efficient frontier](#post-/portfolio/analysis/mean-variance/efficient-frontier).

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

        constraints : PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMeanVarianceEfficientResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/mean-variance-efficient",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
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
                    PostPortfolioOptimizationMeanVarianceEfficientResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMeanVarianceEfficientResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def diversified_mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse]:
        """
        Compute the asset weights of a diversified mean-variance efficient portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        > A diversified mean-variance efficient portfolio does NOT belong to [the mean-variance efficient frontier](#post-/portfolio/analysis/mean-variance/efficient-frontier), but is close to this frontier.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/mean-variance-efficient/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def subset_resampling_based_mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of a subset resampling-based  mean-variance efficient portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/mean-variance-efficient/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMinimumVarianceResponse]:
        """
        Compute the asset weights of the minimum variance portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMinimumVarianceResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-variance",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumVarianceRequestConstraints,
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
                    PostPortfolioOptimizationMinimumVarianceResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumVarianceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def diversified_minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMinimumVarianceDiversifiedResponse]:
        """
        Compute the asset weights of the diversified minimum variance portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMinimumVarianceDiversifiedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-variance/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def subset_resampling_based_minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints
        ] = OMIT,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of the subset resampling-based minimum variance portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints]

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-variance/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPortfolioOptimizationMeanVarianceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumReturnResponse]:
        """
        Compute the asset weights of the maximum return portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        assets_covariance_matrix : typing.Optional[typing.Sequence[typing.Sequence[float]]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMaximumReturnResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-return",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumReturnRequestConstraints,
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
                    PostPortfolioOptimizationMaximumReturnResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumReturnResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def diversified_maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumReturnDiversifiedResponse]:
        """
        Compute the asset weights of the diversified maximum return portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        assets_covariance_matrix : typing.Optional[typing.Sequence[typing.Sequence[float]]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMaximumReturnDiversifiedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-return/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumReturnDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def subset_resampling_based_maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints
        ] = OMIT,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of the subset resampling-based maximum return portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        assets_covariance_matrix : typing.Optional[typing.Sequence[typing.Sequence[float]]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        constraints : typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints]

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-return/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumSharpeRatioResponse]:
        """
        Compute the asset weights of the maximum Sharpe ratio portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

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

        risk_free_rate : float
            The risk free rate

        constraints : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMaximumSharpeRatioResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-sharpe-ratio",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints,
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
                    PostPortfolioOptimizationMaximumSharpeRatioResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumSharpeRatioResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def diversified_maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse]:
        """
        Compute the asset weights of the diversified maximum Sharpe ratio portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

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

        constraints : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-sharpe-ratio/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def subset_resampling_based_maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[
            PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints
        ] = OMIT,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of the susbet resampling-based maximum Sharpe ratio portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

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

        constraints : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints]

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/maximum-sharpe-ratio/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMeanVarianceEfficientResponse]:
        """
        Compute the asset weights of a mean-variance efficient portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        > A mean-variance efficient portfolio is a portfolio belonging to [the mean-variance efficient frontier](#post-/portfolio/analysis/mean-variance/efficient-frontier).

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

        constraints : PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMeanVarianceEfficientResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/mean-variance-efficient",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
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
                    PostPortfolioOptimizationMeanVarianceEfficientResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMeanVarianceEfficientResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def diversified_mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse]:
        """
        Compute the asset weights of a diversified mean-variance efficient portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        > A diversified mean-variance efficient portfolio does NOT belong to [the mean-variance efficient frontier](#post-/portfolio/analysis/mean-variance/efficient-frontier), but is close to this frontier.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/mean-variance-efficient/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def subset_resampling_based_mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of a subset resampling-based  mean-variance efficient portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/mean-variance-efficient/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMinimumVarianceResponse]:
        """
        Compute the asset weights of the minimum variance portfolio, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMinimumVarianceResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-variance",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumVarianceRequestConstraints,
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
                    PostPortfolioOptimizationMinimumVarianceResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumVarianceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def diversified_minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMinimumVarianceDiversifiedResponse]:
        """
        Compute the asset weights of the diversified minimum variance portfolio, as defined in the first reference, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

        References
         * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
         * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMinimumVarianceDiversifiedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-variance/diversified",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
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
                    PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumVarianceDiversifiedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def subset_resampling_based_minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints
        ] = OMIT,
        subset_portfolios: typing.Optional[int] = OMIT,
        subset_portfolios_aggregation_method: typing.Optional[
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod
        ] = OMIT,
        subset_portfolios_enumeration_method: typing.Optional[
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod
        ] = OMIT,
        subset_size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse]:
        """
        Compute the asset weights of the subset resampling-based minimum variance portfolio, following the methodology described in the first and the second references, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
         * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
         * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Optional[typing.Sequence[float]]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints]

        subset_portfolios : typing.Optional[int]
            The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling

        subset_portfolios_aggregation_method : typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]
            The method to aggregate the subset portfolios

        subset_portfolios_enumeration_method : typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]
            The method to enumerate the subset portfolios

        subset_size : typing.Optional[int]
            The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/optimization/minimum-variance/subset-resampling-based",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
                    direction="write",
                ),
                "subsetPortfolios": subset_portfolios,
                "subsetPortfoliosAggregationMethod": subset_portfolios_aggregation_method,
                "subsetPortfoliosEnumerationMethod": subset_portfolios_enumeration_method,
                "subsetSize": subset_size,
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
                    PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
                    parse_obj_as(
                        type_=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
