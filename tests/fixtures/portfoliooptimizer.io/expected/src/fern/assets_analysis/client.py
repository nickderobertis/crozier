

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsAnalysisClient, RawAssetsAnalysisClient
from .types.post_assets_analysis_absorption_ratio_request_assets_covariance_matrix_eigenvectors import (
    PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors,
)
from .types.post_assets_analysis_absorption_ratio_response import PostAssetsAnalysisAbsorptionRatioResponse
from .types.post_assets_analysis_turbulence_index_response import PostAssetsAnalysisTurbulenceIndexResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsAnalysisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsAnalysisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsAnalysisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsAnalysisClient
        """
        return self._raw_client

    def absorption_ratio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_covariance_matrix_eigenvectors: typing.Optional[
            PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsAnalysisAbsorptionRatioResponse:
        """
        Compute the absorption ratio associated to a universe of assets.

        References
        * [Mark Kritzman, Yuanzhen Li, Sebastien Page and Roberto Rigobon, Principal Components as a Measure of Systemic Risk, The Journal of Portfolio Management Summer 2011, 37 (4) 112-126](https://jpm.pm-research.com/content/37/4/112)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_covariance_matrix_eigenvectors : typing.Optional[PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsAnalysisAbsorptionRatioResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_analysis.absorption_ratio(
            assets=2,
            assets_covariance_matrix=[[9.0, 1.0], [1.0, 1.0]],
        )
        """
        _response = self._raw_client.absorption_ratio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_covariance_matrix_eigenvectors=assets_covariance_matrix_eigenvectors,
            request_options=request_options,
        )
        return _response.data

    def turbulence_index(
        self,
        *,
        assets: int,
        assets_average_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsAnalysisTurbulenceIndexResponse:
        """
        Compute the turbulence index associated to a universe of assets.

        References
        * [M. Kritzman, Y. Li, Skulls, Financial Turbulence, and Risk Management,Financial Analysts Journal, Volume 66, Number 5, Pages 30-41, Year 2010](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n5.3)
        * [Kinlaw, W., Turkington, D. Correlation surprise. J Asset Manag 14, 385–399 (2013)](https://link.springer.com/article/10.1057/jam.2013.27)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_average_returns : typing.Sequence[float]
            assetsAverageReturns[i] is the average return of asset i over an historical reference period

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j over an historical reference period

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the return of asset i over a period different from the historical reference period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsAnalysisTurbulenceIndexResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_analysis.turbulence_index(
            assets=2,
            assets_average_returns=[1.0, 1.0],
            assets_covariance_matrix=[[9.0, 1.0], [1.0, 1.0]],
            assets_returns=[1.0, 0.0],
        )
        """
        _response = self._raw_client.turbulence_index(
            assets=assets,
            assets_average_returns=assets_average_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            request_options=request_options,
        )
        return _response.data


class AsyncAssetsAnalysisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsAnalysisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsAnalysisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsAnalysisClient
        """
        return self._raw_client

    async def absorption_ratio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_covariance_matrix_eigenvectors: typing.Optional[
            PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsAnalysisAbsorptionRatioResponse:
        """
        Compute the absorption ratio associated to a universe of assets.

        References
        * [Mark Kritzman, Yuanzhen Li, Sebastien Page and Roberto Rigobon, Principal Components as a Measure of Systemic Risk, The Journal of Portfolio Management Summer 2011, 37 (4) 112-126](https://jpm.pm-research.com/content/37/4/112)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_covariance_matrix_eigenvectors : typing.Optional[PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsAnalysisAbsorptionRatioResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_analysis.absorption_ratio(
                assets=2,
                assets_covariance_matrix=[[9.0, 1.0], [1.0, 1.0]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.absorption_ratio(
            assets=assets,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_covariance_matrix_eigenvectors=assets_covariance_matrix_eigenvectors,
            request_options=request_options,
        )
        return _response.data

    async def turbulence_index(
        self,
        *,
        assets: int,
        assets_average_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsAnalysisTurbulenceIndexResponse:
        """
        Compute the turbulence index associated to a universe of assets.

        References
        * [M. Kritzman, Y. Li, Skulls, Financial Turbulence, and Risk Management,Financial Analysts Journal, Volume 66, Number 5, Pages 30-41, Year 2010](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n5.3)
        * [Kinlaw, W., Turkington, D. Correlation surprise. J Asset Manag 14, 385–399 (2013)](https://link.springer.com/article/10.1057/jam.2013.27)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_average_returns : typing.Sequence[float]
            assetsAverageReturns[i] is the average return of asset i over an historical reference period

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j over an historical reference period

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the return of asset i over a period different from the historical reference period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsAnalysisTurbulenceIndexResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_analysis.turbulence_index(
                assets=2,
                assets_average_returns=[1.0, 1.0],
                assets_covariance_matrix=[[9.0, 1.0], [1.0, 1.0]],
                assets_returns=[1.0, 0.0],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.turbulence_index(
            assets=assets,
            assets_average_returns=assets_average_returns,
            assets_covariance_matrix=assets_covariance_matrix,
            assets_returns=assets_returns,
            request_options=request_options,
        )
        return _response.data
