

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsKurtosisClient, RawAssetsKurtosisClient
from .types.post_assets_kurtosis_request_assets_item import PostAssetsKurtosisRequestAssetsItem
from .types.post_assets_kurtosis_response import PostAssetsKurtosisResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsKurtosisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsKurtosisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsKurtosisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsKurtosisClient
        """
        return self._raw_client

    def kurtosis(
        self,
        *,
        assets: typing.Sequence[PostAssetsKurtosisRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsKurtosisResponse:
        """
        Compute the kurtosis of one or several asset(s), from the asset returns.

        References
        * [Wikipedia, Kurtosis](https://en.wikipedia.org/wiki/Kurtosis)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsKurtosisRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsKurtosisResponse
            OK

        Examples
        --------
        from fern.assets_kurtosis import PostAssetsKurtosisRequestAssetsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_kurtosis.kurtosis(
            assets=[
                PostAssetsKurtosisRequestAssetsItem(
                    asset_returns=[0.01, 0.0, 0.02, -0.03],
                )
            ],
        )
        """
        _response = self._raw_client.kurtosis(assets=assets, request_options=request_options)
        return _response.data


class AsyncAssetsKurtosisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsKurtosisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsKurtosisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsKurtosisClient
        """
        return self._raw_client

    async def kurtosis(
        self,
        *,
        assets: typing.Sequence[PostAssetsKurtosisRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsKurtosisResponse:
        """
        Compute the kurtosis of one or several asset(s), from the asset returns.

        References
        * [Wikipedia, Kurtosis](https://en.wikipedia.org/wiki/Kurtosis)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsKurtosisRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsKurtosisResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_kurtosis import PostAssetsKurtosisRequestAssetsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_kurtosis.kurtosis(
                assets=[
                    PostAssetsKurtosisRequestAssetsItem(
                        asset_returns=[0.01, 0.0, 0.02, -0.03],
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.kurtosis(assets=assets, request_options=request_options)
        return _response.data
