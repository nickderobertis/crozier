

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsVarianceClient, RawAssetsVarianceClient
from .types.post_assets_variance_request import PostAssetsVarianceRequest
from .types.post_assets_variance_response import PostAssetsVarianceResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsVarianceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsVarianceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsVarianceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsVarianceClient
        """
        return self._raw_client

    def variance(
        self, *, request: PostAssetsVarianceRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsVarianceResponse:
        """
        Compute the variance of one or several asset(s) from either:
        * The asset returns
        * The asset covariance matrix
        * The asset volatility(ies)

        References
        * [Wikipedia, Variance](https://en.wikipedia.org/wiki/Variance)

        Parameters
        ----------
        request : PostAssetsVarianceRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsVarianceResponse
            OK

        Examples
        --------
        from fern.assets_variance import PostAssetsVarianceRequestAssetsCovarianceMatrix

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_variance.variance(
            request=PostAssetsVarianceRequestAssetsCovarianceMatrix(
                assets=2,
                assets_covariance_matrix=[[0.01, -0.0025], [-0.0025, 0.0025]],
            ),
        )
        """
        _response = self._raw_client.variance(request=request, request_options=request_options)
        return _response.data


class AsyncAssetsVarianceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsVarianceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsVarianceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsVarianceClient
        """
        return self._raw_client

    async def variance(
        self, *, request: PostAssetsVarianceRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsVarianceResponse:
        """
        Compute the variance of one or several asset(s) from either:
        * The asset returns
        * The asset covariance matrix
        * The asset volatility(ies)

        References
        * [Wikipedia, Variance](https://en.wikipedia.org/wiki/Variance)

        Parameters
        ----------
        request : PostAssetsVarianceRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsVarianceResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_variance import PostAssetsVarianceRequestAssetsCovarianceMatrix

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_variance.variance(
                request=PostAssetsVarianceRequestAssetsCovarianceMatrix(
                    assets=2,
                    assets_covariance_matrix=[[0.01, -0.0025], [-0.0025, 0.0025]],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.variance(request=request, request_options=request_options)
        return _response.data
