

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsVolatilityClient, RawAssetsVolatilityClient
from .types.post_assets_volatility_request import PostAssetsVolatilityRequest
from .types.post_assets_volatility_response import PostAssetsVolatilityResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsVolatilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsVolatilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsVolatilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsVolatilityClient
        """
        return self._raw_client

    def volatility(
        self, *, request: PostAssetsVolatilityRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsVolatilityResponse:
        """
        Compute the volatility (i.e., standard deviation) of one or several asset(s) from either:
        * The asset returns
        * The asset covariance matrix
        * The asset variance(s)

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)

        Parameters
        ----------
        request : PostAssetsVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsVolatilityResponse
            OK

        Examples
        --------
        from fern.assets_volatility import (
            PostAssetsVolatilityRequestAssetsCovarianceMatrix,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_volatility.volatility(
            request=PostAssetsVolatilityRequestAssetsCovarianceMatrix(
                assets=2,
                assets_covariance_matrix=[[0.01, -0.0025], [-0.0025, 0.0025]],
            ),
        )
        """
        _response = self._raw_client.volatility(request=request, request_options=request_options)
        return _response.data


class AsyncAssetsVolatilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsVolatilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsVolatilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsVolatilityClient
        """
        return self._raw_client

    async def volatility(
        self, *, request: PostAssetsVolatilityRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsVolatilityResponse:
        """
        Compute the volatility (i.e., standard deviation) of one or several asset(s) from either:
        * The asset returns
        * The asset covariance matrix
        * The asset variance(s)

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)

        Parameters
        ----------
        request : PostAssetsVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsVolatilityResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_volatility import (
            PostAssetsVolatilityRequestAssetsCovarianceMatrix,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_volatility.volatility(
                request=PostAssetsVolatilityRequestAssetsCovarianceMatrix(
                    assets=2,
                    assets_covariance_matrix=[[0.01, -0.0025], [-0.0025, 0.0025]],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.volatility(request=request, request_options=request_options)
        return _response.data
