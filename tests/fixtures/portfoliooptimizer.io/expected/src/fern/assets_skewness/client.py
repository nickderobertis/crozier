

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsSkewnessClient, RawAssetsSkewnessClient
from .types.post_assets_skewness_request_assets_item import PostAssetsSkewnessRequestAssetsItem
from .types.post_assets_skewness_response import PostAssetsSkewnessResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsSkewnessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsSkewnessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsSkewnessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsSkewnessClient
        """
        return self._raw_client

    def skewness(
        self,
        *,
        assets: typing.Sequence[PostAssetsSkewnessRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsSkewnessResponse:
        """
        Compute the skewness of one or several asset(s), from the asset returns.

        References
        * [Wikipedia, Skewness](https://en.wikipedia.org/wiki/Skewness)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsSkewnessRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsSkewnessResponse
            OK

        Examples
        --------
        from fern.assets_skewness import PostAssetsSkewnessRequestAssetsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_skewness.skewness(
            assets=[
                PostAssetsSkewnessRequestAssetsItem(
                    asset_returns=[0.01, 0.0, 0.02, -0.03],
                )
            ],
        )
        """
        _response = self._raw_client.skewness(assets=assets, request_options=request_options)
        return _response.data


class AsyncAssetsSkewnessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsSkewnessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsSkewnessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsSkewnessClient
        """
        return self._raw_client

    async def skewness(
        self,
        *,
        assets: typing.Sequence[PostAssetsSkewnessRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsSkewnessResponse:
        """
        Compute the skewness of one or several asset(s), from the asset returns.

        References
        * [Wikipedia, Skewness](https://en.wikipedia.org/wiki/Skewness)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsSkewnessRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsSkewnessResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_skewness import PostAssetsSkewnessRequestAssetsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_skewness.skewness(
                assets=[
                    PostAssetsSkewnessRequestAssetsItem(
                        asset_returns=[0.01, 0.0, 0.02, -0.03],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.skewness(assets=assets, request_options=request_options)
        return _response.data
