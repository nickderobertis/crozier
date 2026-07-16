

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .assets_analysis.client import AssetsAnalysisClient, AsyncAssetsAnalysisClient
    from .assets_correlation_matrix.client import AssetsCorrelationMatrixClient, AsyncAssetsCorrelationMatrixClient
    from .assets_covariance_matrix.client import AssetsCovarianceMatrixClient, AsyncAssetsCovarianceMatrixClient
    from .assets_kurtosis.client import AssetsKurtosisClient, AsyncAssetsKurtosisClient
    from .assets_prices.client import AssetsPricesClient, AsyncAssetsPricesClient
    from .assets_returns.client import AssetsReturnsClient, AsyncAssetsReturnsClient
    from .assets_returns_simulation.client import AssetsReturnsSimulationClient, AsyncAssetsReturnsSimulationClient
    from .assets_skewness.client import AssetsSkewnessClient, AsyncAssetsSkewnessClient
    from .assets_variance.client import AssetsVarianceClient, AsyncAssetsVarianceClient
    from .assets_volatility.client import AssetsVolatilityClient, AsyncAssetsVolatilityClient
    from .factors.client import AsyncFactorsClient, FactorsClient
    from .portfolio_analysis.client import AsyncPortfolioAnalysisClient, PortfolioAnalysisClient
    from .portfolio_analysis_sharpe_ratio.client import (
        AsyncPortfolioAnalysisSharpeRatioClient,
        PortfolioAnalysisSharpeRatioClient,
    )
    from .portfolio_construction.client import AsyncPortfolioConstructionClient, PortfolioConstructionClient
    from .portfolio_optimization.client import AsyncPortfolioOptimizationClient, PortfolioOptimizationClient
    from .portfolio_optimization_mean_variance.client import (
        AsyncPortfolioOptimizationMeanVarianceClient,
        PortfolioOptimizationMeanVarianceClient,
    )
    from .portfolio_simulation.client import AsyncPortfolioSimulationClient, PortfolioSimulationClient


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._assets_analysis: typing.Optional[AssetsAnalysisClient] = None
        self._assets_correlation_matrix: typing.Optional[AssetsCorrelationMatrixClient] = None
        self._assets_covariance_matrix: typing.Optional[AssetsCovarianceMatrixClient] = None
        self._assets_kurtosis: typing.Optional[AssetsKurtosisClient] = None
        self._assets_prices: typing.Optional[AssetsPricesClient] = None
        self._assets_returns: typing.Optional[AssetsReturnsClient] = None
        self._assets_returns_simulation: typing.Optional[AssetsReturnsSimulationClient] = None
        self._assets_skewness: typing.Optional[AssetsSkewnessClient] = None
        self._assets_variance: typing.Optional[AssetsVarianceClient] = None
        self._assets_volatility: typing.Optional[AssetsVolatilityClient] = None
        self._factors: typing.Optional[FactorsClient] = None
        self._portfolio_analysis: typing.Optional[PortfolioAnalysisClient] = None
        self._portfolio_analysis_sharpe_ratio: typing.Optional[PortfolioAnalysisSharpeRatioClient] = None
        self._portfolio_construction: typing.Optional[PortfolioConstructionClient] = None
        self._portfolio_optimization: typing.Optional[PortfolioOptimizationClient] = None
        self._portfolio_optimization_mean_variance: typing.Optional[PortfolioOptimizationMeanVarianceClient] = None
        self._portfolio_simulation: typing.Optional[PortfolioSimulationClient] = None

    @property
    def assets_analysis(self):
        if self._assets_analysis is None:
            from .assets_analysis.client import AssetsAnalysisClient

            self._assets_analysis = AssetsAnalysisClient(client_wrapper=self._client_wrapper)
        return self._assets_analysis

    @property
    def assets_correlation_matrix(self):
        if self._assets_correlation_matrix is None:
            from .assets_correlation_matrix.client import AssetsCorrelationMatrixClient

            self._assets_correlation_matrix = AssetsCorrelationMatrixClient(client_wrapper=self._client_wrapper)
        return self._assets_correlation_matrix

    @property
    def assets_covariance_matrix(self):
        if self._assets_covariance_matrix is None:
            from .assets_covariance_matrix.client import AssetsCovarianceMatrixClient

            self._assets_covariance_matrix = AssetsCovarianceMatrixClient(client_wrapper=self._client_wrapper)
        return self._assets_covariance_matrix

    @property
    def assets_kurtosis(self):
        if self._assets_kurtosis is None:
            from .assets_kurtosis.client import AssetsKurtosisClient

            self._assets_kurtosis = AssetsKurtosisClient(client_wrapper=self._client_wrapper)
        return self._assets_kurtosis

    @property
    def assets_prices(self):
        if self._assets_prices is None:
            from .assets_prices.client import AssetsPricesClient

            self._assets_prices = AssetsPricesClient(client_wrapper=self._client_wrapper)
        return self._assets_prices

    @property
    def assets_returns(self):
        if self._assets_returns is None:
            from .assets_returns.client import AssetsReturnsClient

            self._assets_returns = AssetsReturnsClient(client_wrapper=self._client_wrapper)
        return self._assets_returns

    @property
    def assets_returns_simulation(self):
        if self._assets_returns_simulation is None:
            from .assets_returns_simulation.client import AssetsReturnsSimulationClient

            self._assets_returns_simulation = AssetsReturnsSimulationClient(client_wrapper=self._client_wrapper)
        return self._assets_returns_simulation

    @property
    def assets_skewness(self):
        if self._assets_skewness is None:
            from .assets_skewness.client import AssetsSkewnessClient

            self._assets_skewness = AssetsSkewnessClient(client_wrapper=self._client_wrapper)
        return self._assets_skewness

    @property
    def assets_variance(self):
        if self._assets_variance is None:
            from .assets_variance.client import AssetsVarianceClient

            self._assets_variance = AssetsVarianceClient(client_wrapper=self._client_wrapper)
        return self._assets_variance

    @property
    def assets_volatility(self):
        if self._assets_volatility is None:
            from .assets_volatility.client import AssetsVolatilityClient

            self._assets_volatility = AssetsVolatilityClient(client_wrapper=self._client_wrapper)
        return self._assets_volatility

    @property
    def factors(self):
        if self._factors is None:
            from .factors.client import FactorsClient

            self._factors = FactorsClient(client_wrapper=self._client_wrapper)
        return self._factors

    @property
    def portfolio_analysis(self):
        if self._portfolio_analysis is None:
            from .portfolio_analysis.client import PortfolioAnalysisClient

            self._portfolio_analysis = PortfolioAnalysisClient(client_wrapper=self._client_wrapper)
        return self._portfolio_analysis

    @property
    def portfolio_analysis_sharpe_ratio(self):
        if self._portfolio_analysis_sharpe_ratio is None:
            from .portfolio_analysis_sharpe_ratio.client import PortfolioAnalysisSharpeRatioClient

            self._portfolio_analysis_sharpe_ratio = PortfolioAnalysisSharpeRatioClient(
                client_wrapper=self._client_wrapper
            )
        return self._portfolio_analysis_sharpe_ratio

    @property
    def portfolio_construction(self):
        if self._portfolio_construction is None:
            from .portfolio_construction.client import PortfolioConstructionClient

            self._portfolio_construction = PortfolioConstructionClient(client_wrapper=self._client_wrapper)
        return self._portfolio_construction

    @property
    def portfolio_optimization(self):
        if self._portfolio_optimization is None:
            from .portfolio_optimization.client import PortfolioOptimizationClient

            self._portfolio_optimization = PortfolioOptimizationClient(client_wrapper=self._client_wrapper)
        return self._portfolio_optimization

    @property
    def portfolio_optimization_mean_variance(self):
        if self._portfolio_optimization_mean_variance is None:
            from .portfolio_optimization_mean_variance.client import (
                PortfolioOptimizationMeanVarianceClient,
            )

            self._portfolio_optimization_mean_variance = PortfolioOptimizationMeanVarianceClient(
                client_wrapper=self._client_wrapper
            )
        return self._portfolio_optimization_mean_variance

    @property
    def portfolio_simulation(self):
        if self._portfolio_simulation is None:
            from .portfolio_simulation.client import PortfolioSimulationClient

            self._portfolio_simulation = PortfolioSimulationClient(client_wrapper=self._client_wrapper)
        return self._portfolio_simulation


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._assets_analysis: typing.Optional[AsyncAssetsAnalysisClient] = None
        self._assets_correlation_matrix: typing.Optional[AsyncAssetsCorrelationMatrixClient] = None
        self._assets_covariance_matrix: typing.Optional[AsyncAssetsCovarianceMatrixClient] = None
        self._assets_kurtosis: typing.Optional[AsyncAssetsKurtosisClient] = None
        self._assets_prices: typing.Optional[AsyncAssetsPricesClient] = None
        self._assets_returns: typing.Optional[AsyncAssetsReturnsClient] = None
        self._assets_returns_simulation: typing.Optional[AsyncAssetsReturnsSimulationClient] = None
        self._assets_skewness: typing.Optional[AsyncAssetsSkewnessClient] = None
        self._assets_variance: typing.Optional[AsyncAssetsVarianceClient] = None
        self._assets_volatility: typing.Optional[AsyncAssetsVolatilityClient] = None
        self._factors: typing.Optional[AsyncFactorsClient] = None
        self._portfolio_analysis: typing.Optional[AsyncPortfolioAnalysisClient] = None
        self._portfolio_analysis_sharpe_ratio: typing.Optional[AsyncPortfolioAnalysisSharpeRatioClient] = None
        self._portfolio_construction: typing.Optional[AsyncPortfolioConstructionClient] = None
        self._portfolio_optimization: typing.Optional[AsyncPortfolioOptimizationClient] = None
        self._portfolio_optimization_mean_variance: typing.Optional[AsyncPortfolioOptimizationMeanVarianceClient] = None
        self._portfolio_simulation: typing.Optional[AsyncPortfolioSimulationClient] = None

    @property
    def assets_analysis(self):
        if self._assets_analysis is None:
            from .assets_analysis.client import AsyncAssetsAnalysisClient

            self._assets_analysis = AsyncAssetsAnalysisClient(client_wrapper=self._client_wrapper)
        return self._assets_analysis

    @property
    def assets_correlation_matrix(self):
        if self._assets_correlation_matrix is None:
            from .assets_correlation_matrix.client import AsyncAssetsCorrelationMatrixClient

            self._assets_correlation_matrix = AsyncAssetsCorrelationMatrixClient(client_wrapper=self._client_wrapper)
        return self._assets_correlation_matrix

    @property
    def assets_covariance_matrix(self):
        if self._assets_covariance_matrix is None:
            from .assets_covariance_matrix.client import AsyncAssetsCovarianceMatrixClient

            self._assets_covariance_matrix = AsyncAssetsCovarianceMatrixClient(client_wrapper=self._client_wrapper)
        return self._assets_covariance_matrix

    @property
    def assets_kurtosis(self):
        if self._assets_kurtosis is None:
            from .assets_kurtosis.client import AsyncAssetsKurtosisClient

            self._assets_kurtosis = AsyncAssetsKurtosisClient(client_wrapper=self._client_wrapper)
        return self._assets_kurtosis

    @property
    def assets_prices(self):
        if self._assets_prices is None:
            from .assets_prices.client import AsyncAssetsPricesClient

            self._assets_prices = AsyncAssetsPricesClient(client_wrapper=self._client_wrapper)
        return self._assets_prices

    @property
    def assets_returns(self):
        if self._assets_returns is None:
            from .assets_returns.client import AsyncAssetsReturnsClient

            self._assets_returns = AsyncAssetsReturnsClient(client_wrapper=self._client_wrapper)
        return self._assets_returns

    @property
    def assets_returns_simulation(self):
        if self._assets_returns_simulation is None:
            from .assets_returns_simulation.client import AsyncAssetsReturnsSimulationClient

            self._assets_returns_simulation = AsyncAssetsReturnsSimulationClient(client_wrapper=self._client_wrapper)
        return self._assets_returns_simulation

    @property
    def assets_skewness(self):
        if self._assets_skewness is None:
            from .assets_skewness.client import AsyncAssetsSkewnessClient

            self._assets_skewness = AsyncAssetsSkewnessClient(client_wrapper=self._client_wrapper)
        return self._assets_skewness

    @property
    def assets_variance(self):
        if self._assets_variance is None:
            from .assets_variance.client import AsyncAssetsVarianceClient

            self._assets_variance = AsyncAssetsVarianceClient(client_wrapper=self._client_wrapper)
        return self._assets_variance

    @property
    def assets_volatility(self):
        if self._assets_volatility is None:
            from .assets_volatility.client import AsyncAssetsVolatilityClient

            self._assets_volatility = AsyncAssetsVolatilityClient(client_wrapper=self._client_wrapper)
        return self._assets_volatility

    @property
    def factors(self):
        if self._factors is None:
            from .factors.client import AsyncFactorsClient

            self._factors = AsyncFactorsClient(client_wrapper=self._client_wrapper)
        return self._factors

    @property
    def portfolio_analysis(self):
        if self._portfolio_analysis is None:
            from .portfolio_analysis.client import AsyncPortfolioAnalysisClient

            self._portfolio_analysis = AsyncPortfolioAnalysisClient(client_wrapper=self._client_wrapper)
        return self._portfolio_analysis

    @property
    def portfolio_analysis_sharpe_ratio(self):
        if self._portfolio_analysis_sharpe_ratio is None:
            from .portfolio_analysis_sharpe_ratio.client import AsyncPortfolioAnalysisSharpeRatioClient

            self._portfolio_analysis_sharpe_ratio = AsyncPortfolioAnalysisSharpeRatioClient(
                client_wrapper=self._client_wrapper
            )
        return self._portfolio_analysis_sharpe_ratio

    @property
    def portfolio_construction(self):
        if self._portfolio_construction is None:
            from .portfolio_construction.client import AsyncPortfolioConstructionClient

            self._portfolio_construction = AsyncPortfolioConstructionClient(client_wrapper=self._client_wrapper)
        return self._portfolio_construction

    @property
    def portfolio_optimization(self):
        if self._portfolio_optimization is None:
            from .portfolio_optimization.client import AsyncPortfolioOptimizationClient

            self._portfolio_optimization = AsyncPortfolioOptimizationClient(client_wrapper=self._client_wrapper)
        return self._portfolio_optimization

    @property
    def portfolio_optimization_mean_variance(self):
        if self._portfolio_optimization_mean_variance is None:
            from .portfolio_optimization_mean_variance.client import (
                AsyncPortfolioOptimizationMeanVarianceClient,
            )

            self._portfolio_optimization_mean_variance = AsyncPortfolioOptimizationMeanVarianceClient(
                client_wrapper=self._client_wrapper
            )
        return self._portfolio_optimization_mean_variance

    @property
    def portfolio_simulation(self):
        if self._portfolio_simulation is None:
            from .portfolio_simulation.client import AsyncPortfolioSimulationClient

            self._portfolio_simulation = AsyncPortfolioSimulationClient(client_wrapper=self._client_wrapper)
        return self._portfolio_simulation


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
