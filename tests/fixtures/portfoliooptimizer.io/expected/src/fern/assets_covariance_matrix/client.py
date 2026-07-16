

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsCovarianceMatrixClient, RawAssetsCovarianceMatrixClient
from .types.post_assets_covariance_matrix_effective_rank_response import PostAssetsCovarianceMatrixEffectiveRankResponse
from .types.post_assets_covariance_matrix_exponentially_weighted_request_assets_item import (
    PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem,
)
from .types.post_assets_covariance_matrix_exponentially_weighted_response import (
    PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
)
from .types.post_assets_covariance_matrix_request import PostAssetsCovarianceMatrixRequest
from .types.post_assets_covariance_matrix_response import PostAssetsCovarianceMatrixResponse
from .types.post_assets_covariance_matrix_validation_response import PostAssetsCovarianceMatrixValidationResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsCovarianceMatrixClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsCovarianceMatrixClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsCovarianceMatrixClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsCovarianceMatrixClient
        """
        return self._raw_client

    def covariance_matrix(
        self, *, request: PostAssetsCovarianceMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsCovarianceMatrixResponse:
        """
        Compute the covariance matrix of assets from either:
        * The asset correlation matrix and their volatilities (i.e., standard deviations)
        * The asset correlation matrix and their variances
        * The asset returns

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        request : PostAssetsCovarianceMatrixRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixResponse
            OK

        Examples
        --------
        from fern.assets_covariance_matrix import (
            PostAssetsCovarianceMatrixRequestAssets,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_covariance_matrix.covariance_matrix(
            request=PostAssetsCovarianceMatrixRequestAssets(
                assets=2,
                assets_correlation_matrix=[[1.0, -0.5], [-0.5, 1.0]],
                assets_volatilities=[0.1, 0.05],
            ),
        )
        """
        _response = self._raw_client.covariance_matrix(request=request, request_options=request_options)
        return _response.data

    def covariance_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCovarianceMatrixEffectiveRankResponse:
        """
        Compute the effective rank of an asset covariance matrix.

        References
        * [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixEffectiveRankResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_covariance_matrix.covariance_matrix_effective_rank(
            assets=2,
            assets_covariance_matrix=[[0.00035, -0.00035], [-0.00035, 0.00035]],
        )
        """
        _response = self._raw_client.covariance_matrix_effective_rank(
            assets=assets, assets_covariance_matrix=assets_covariance_matrix, request_options=request_options
        )
        return _response.data

    def exponentially_weighted_covariance_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem],
        decay_factor: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCovarianceMatrixExponentiallyWeightedResponse:
        """
        Compute an exponentially weighted covariance matrix of assets returns.

        References
        * [RiskMetrics Group. Longerstaey, J. (1996). RiskMetrics technical document, Technical Report fourth edition](https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem]

        decay_factor : typing.Optional[float]
            The exponential decay factor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixExponentiallyWeightedResponse
            OK

        Examples
        --------
        from fern.assets_covariance_matrix import (
            PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_covariance_matrix.exponentially_weighted_covariance_matrix(
            assets=[
                PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(
                    asset_returns=[0.01, 0.01, 0.02, 0.01],
                ),
                PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(
                    asset_returns=[-0.02, -0.02, -0.04, -0.02],
                ),
            ],
            decay_factor=0.5,
        )
        """
        _response = self._raw_client.exponentially_weighted_covariance_matrix(
            assets=assets, decay_factor=decay_factor, request_options=request_options
        )
        return _response.data

    def covariance_matrix_validation(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCovarianceMatrixValidationResponse:
        """
        Validate whether a matrix is a covariance matrix.

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixValidationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_covariance_matrix.covariance_matrix_validation(
            assets=2,
            assets_covariance_matrix=[[0.00035, -0.00035], [-0.00035, 0.00035]],
        )
        """
        _response = self._raw_client.covariance_matrix_validation(
            assets=assets, assets_covariance_matrix=assets_covariance_matrix, request_options=request_options
        )
        return _response.data


class AsyncAssetsCovarianceMatrixClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsCovarianceMatrixClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsCovarianceMatrixClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsCovarianceMatrixClient
        """
        return self._raw_client

    async def covariance_matrix(
        self, *, request: PostAssetsCovarianceMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsCovarianceMatrixResponse:
        """
        Compute the covariance matrix of assets from either:
        * The asset correlation matrix and their volatilities (i.e., standard deviations)
        * The asset correlation matrix and their variances
        * The asset returns

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        request : PostAssetsCovarianceMatrixRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_covariance_matrix import (
            PostAssetsCovarianceMatrixRequestAssets,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_covariance_matrix.covariance_matrix(
                request=PostAssetsCovarianceMatrixRequestAssets(
                    assets=2,
                    assets_correlation_matrix=[[1.0, -0.5], [-0.5, 1.0]],
                    assets_volatilities=[0.1, 0.05],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.covariance_matrix(request=request, request_options=request_options)
        return _response.data

    async def covariance_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCovarianceMatrixEffectiveRankResponse:
        """
        Compute the effective rank of an asset covariance matrix.

        References
        * [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixEffectiveRankResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_covariance_matrix.covariance_matrix_effective_rank(
                assets=2,
                assets_covariance_matrix=[[0.00035, -0.00035], [-0.00035, 0.00035]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.covariance_matrix_effective_rank(
            assets=assets, assets_covariance_matrix=assets_covariance_matrix, request_options=request_options
        )
        return _response.data

    async def exponentially_weighted_covariance_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem],
        decay_factor: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCovarianceMatrixExponentiallyWeightedResponse:
        """
        Compute an exponentially weighted covariance matrix of assets returns.

        References
        * [RiskMetrics Group. Longerstaey, J. (1996). RiskMetrics technical document, Technical Report fourth edition](https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem]

        decay_factor : typing.Optional[float]
            The exponential decay factor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixExponentiallyWeightedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_covariance_matrix import (
            PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_covariance_matrix.exponentially_weighted_covariance_matrix(
                assets=[
                    PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(
                        asset_returns=[0.01, 0.01, 0.02, 0.01],
                    ),
                    PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(
                        asset_returns=[-0.02, -0.02, -0.04, -0.02],
                    ),
                ],
                decay_factor=0.5,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.exponentially_weighted_covariance_matrix(
            assets=assets, decay_factor=decay_factor, request_options=request_options
        )
        return _response.data

    async def covariance_matrix_validation(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCovarianceMatrixValidationResponse:
        """
        Validate whether a matrix is a covariance matrix.

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsCovarianceMatrixValidationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_covariance_matrix.covariance_matrix_validation(
                assets=2,
                assets_covariance_matrix=[[0.00035, -0.00035], [-0.00035, 0.00035]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.covariance_matrix_validation(
            assets=assets, assets_covariance_matrix=assets_covariance_matrix, request_options=request_options
        )
        return _response.data
