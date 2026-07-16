

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortfolioOptimizationMeanVarianceClient, RawPortfolioOptimizationMeanVarianceClient
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


class PortfolioOptimizationMeanVarianceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioOptimizationMeanVarianceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioOptimizationMeanVarianceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioOptimizationMeanVarianceClient
        """
        return self._raw_client

    def maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumReturnResponse:
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
        PostPortfolioOptimizationMaximumReturnResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMaximumReturnRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.maximum_return_portfolio(
            assets=2,
            assets_returns=[0.02, 0.01],
            constraints=PostPortfolioOptimizationMaximumReturnRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
            ),
        )
        """
        _response = self._raw_client.maximum_return_portfolio(
            assets=assets,
            assets_returns=assets_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def diversified_maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumReturnDiversifiedResponse:
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
        PostPortfolioOptimizationMaximumReturnDiversifiedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.diversified_maximum_return_portfolio(
            assets=2,
            assets_returns=[0.02, 0.01],
            constraints=PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
            ),
        )
        """
        _response = self._raw_client.diversified_maximum_return_portfolio(
            assets=assets,
            assets_returns=assets_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.subset_resampling_based_maximum_return_portfolio(
            assets=3,
            assets_returns=[0.01, 0.02, 0.03],
            subset_portfolios_enumeration_method=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.COMPLETE,
        )
        """
        _response = self._raw_client.subset_resampling_based_maximum_return_portfolio(
            assets=assets,
            assets_returns=assets_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data

    def maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumSharpeRatioResponse:
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
        PostPortfolioOptimizationMaximumSharpeRatioResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.maximum_sharpe_ratio_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.05, 0.02], [0.02, 0.07]],
            assets_returns=[0.05, 0.1],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.maximum_sharpe_ratio_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def diversified_maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse:
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
        PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.diversified_maximum_sharpe_ratio_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.05, 0.02], [0.02, 0.07]],
            assets_returns=[0.05, 0.1],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.diversified_maximum_sharpe_ratio_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.subset_resampling_based_maximum_sharpe_ratio_portfolio(
            assets=3,
            assets_covariance_matrix=[
                [0.05, 0.02, 0.0],
                [0.02, 0.07, 0.5],
                [0.0, 0.5, 0.1],
            ],
            assets_returns=[0.05, 0.1, 0.025],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.subset_resampling_based_maximum_sharpe_ratio_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data

    def mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMeanVarianceEfficientResponse:
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
        PostPortfolioOptimizationMeanVarianceEfficientResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.mean_variance_efficient_portfolio(
            assets=2,
            assets_covariance_matrix=[[1.0, 0.3], [0.3, 1.0]],
            assets_returns=[0.1, 0.2],
            constraints=PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints(
                portfolio_return=0.15,
            ),
        )
        """
        _response = self._raw_client.mean_variance_efficient_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def diversified_mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse:
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
        PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.diversified_mean_variance_efficient_portfolio(
            assets=2,
            assets_covariance_matrix=[[1.0, 0.3], [0.3, 1.0]],
            assets_returns=[0.1, 0.2],
            constraints=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints(
                delta_return=0.05,
                delta_volatility=0.05,
                portfolio_return=0.175,
            ),
        )
        """
        _response = self._raw_client.diversified_mean_variance_efficient_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.subset_resampling_based_mean_variance_efficient_portfolio(
            assets=3,
            assets_covariance_matrix=[
                [1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0],
            ],
            assets_returns=[0.1, 0.2, 0.3],
            constraints=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints(
                risk_tolerance=2.0,
            ),
        )
        """
        _response = self._raw_client.subset_resampling_based_mean_variance_efficient_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data

    def minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumVarianceResponse:
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
        PostPortfolioOptimizationMinimumVarianceResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMinimumVarianceRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.minimum_variance_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            constraints=PostPortfolioOptimizationMinimumVarianceRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
                maximum_portfolio_exposure=0.5,
                minimum_portfolio_exposure=0.5,
            ),
        )
        """
        _response = self._raw_client.minimum_variance_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    def diversified_minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumVarianceDiversifiedResponse:
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
        PostPortfolioOptimizationMinimumVarianceDiversifiedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.diversified_minimum_variance_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            constraints=PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
                maximum_portfolio_exposure=0.5,
                minimum_portfolio_exposure=0.5,
            ),
        )
        """
        _response = self._raw_client.diversified_minimum_variance_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse
            OK

        Examples
        --------
        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_optimization_mean_variance.subset_resampling_based_minimum_variance_portfolio(
            assets=2,
            assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
            constraints=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints(
                maximum_assets_weights=[0.4, 1.0],
                maximum_portfolio_exposure=0.5,
                minimum_portfolio_exposure=0.5,
            ),
            subset_portfolios=1,
        )
        """
        _response = self._raw_client.subset_resampling_based_minimum_variance_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data


class AsyncPortfolioOptimizationMeanVarianceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioOptimizationMeanVarianceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioOptimizationMeanVarianceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioOptimizationMeanVarianceClient
        """
        return self._raw_client

    async def maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumReturnResponse:
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
        PostPortfolioOptimizationMaximumReturnResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMaximumReturnRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.maximum_return_portfolio(
                assets=2,
                assets_returns=[0.02, 0.01],
                constraints=PostPortfolioOptimizationMaximumReturnRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.maximum_return_portfolio(
            assets=assets,
            assets_returns=assets_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def diversified_maximum_return_portfolio(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Optional[typing.Sequence[typing.Sequence[float]]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumReturnDiversifiedResponse:
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
        PostPortfolioOptimizationMaximumReturnDiversifiedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.diversified_maximum_return_portfolio(
                assets=2,
                assets_returns=[0.02, 0.01],
                constraints=PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diversified_maximum_return_portfolio(
            assets=assets,
            assets_returns=assets_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.subset_resampling_based_maximum_return_portfolio(
                assets=3,
                assets_returns=[0.01, 0.02, 0.03],
                subset_portfolios_enumeration_method=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.COMPLETE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subset_resampling_based_maximum_return_portfolio(
            assets=assets,
            assets_returns=assets_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data

    async def maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumSharpeRatioResponse:
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
        PostPortfolioOptimizationMaximumSharpeRatioResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.maximum_sharpe_ratio_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.05, 0.02], [0.02, 0.07]],
                assets_returns=[0.05, 0.1],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.maximum_sharpe_ratio_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def diversified_maximum_sharpe_ratio_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        risk_free_rate: float,
        constraints: typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse:
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
        PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.diversified_maximum_sharpe_ratio_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.05, 0.02], [0.02, 0.07]],
                assets_returns=[0.05, 0.1],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diversified_maximum_sharpe_ratio_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.subset_resampling_based_maximum_sharpe_ratio_portfolio(
                assets=3,
                assets_covariance_matrix=[
                    [0.05, 0.02, 0.0],
                    [0.02, 0.07, 0.5],
                    [0.0, 0.5, 0.1],
                ],
                assets_returns=[0.05, 0.1, 0.025],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subset_resampling_based_maximum_sharpe_ratio_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            risk_free_rate=risk_free_rate,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data

    async def mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMeanVarianceEfficientResponse:
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
        PostPortfolioOptimizationMeanVarianceEfficientResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.mean_variance_efficient_portfolio(
                assets=2,
                assets_covariance_matrix=[[1.0, 0.3], [0.3, 1.0]],
                assets_returns=[0.1, 0.2],
                constraints=PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints(
                    portfolio_return=0.15,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mean_variance_efficient_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def diversified_mean_variance_efficient_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse:
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
        PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.diversified_mean_variance_efficient_portfolio(
                assets=2,
                assets_covariance_matrix=[[1.0, 0.3], [0.3, 1.0]],
                assets_returns=[0.1, 0.2],
                constraints=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints(
                    delta_return=0.05,
                    delta_volatility=0.05,
                    portfolio_return=0.175,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diversified_mean_variance_efficient_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.subset_resampling_based_mean_variance_efficient_portfolio(
                assets=3,
                assets_covariance_matrix=[
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0],
                ],
                assets_returns=[0.1, 0.2, 0.3],
                constraints=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints(
                    risk_tolerance=2.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subset_resampling_based_mean_variance_efficient_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data

    async def minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumVarianceResponse:
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
        PostPortfolioOptimizationMinimumVarianceResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMinimumVarianceRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.minimum_variance_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                constraints=PostPortfolioOptimizationMinimumVarianceRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                    maximum_portfolio_exposure=0.5,
                    minimum_portfolio_exposure=0.5,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.minimum_variance_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

    async def diversified_minimum_variance_portfolio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Optional[typing.Sequence[float]] = OMIT,
        constraints: typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioOptimizationMinimumVarianceDiversifiedResponse:
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
        PostPortfolioOptimizationMinimumVarianceDiversifiedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.diversified_minimum_variance_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                constraints=PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                    maximum_portfolio_exposure=0.5,
                    minimum_portfolio_exposure=0.5,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.diversified_minimum_variance_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            request_options=request_options,
        )
        return _response.data

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
    ) -> PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse:
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
        PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_optimization_mean_variance import (
            PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_optimization_mean_variance.subset_resampling_based_minimum_variance_portfolio(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                constraints=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints(
                    maximum_assets_weights=[0.4, 1.0],
                    maximum_portfolio_exposure=0.5,
                    minimum_portfolio_exposure=0.5,
                ),
                subset_portfolios=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.subset_resampling_based_minimum_variance_portfolio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            constraints=constraints,
            subset_portfolios=subset_portfolios,
            subset_portfolios_aggregation_method=subset_portfolios_aggregation_method,
            subset_portfolios_enumeration_method=subset_portfolios_enumeration_method,
            subset_size=subset_size,
            request_options=request_options,
        )
        return _response.data
