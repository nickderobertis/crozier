

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsReturnsClient, RawAssetsReturnsClient
from .types.post_assets_returns_average_request_assets_item import PostAssetsReturnsAverageRequestAssetsItem
from .types.post_assets_returns_average_response import PostAssetsReturnsAverageResponse
from .types.post_assets_returns_request_assets_item import PostAssetsReturnsRequestAssetsItem
from .types.post_assets_returns_response import PostAssetsReturnsResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsReturnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsReturnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsReturnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsReturnsClient
        """
        return self._raw_client

    def arithmetic_returns(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsReturnsResponse:
        """
        Compute the arithmetic return(s) of one or several asset(s) for one or several time period(s).

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsReturnsResponse
            OK

        Examples
        --------
        from fern.assets_returns import PostAssetsReturnsRequestAssetsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_returns.arithmetic_returns(
            assets=[
                PostAssetsReturnsRequestAssetsItem(
                    asset_prices=[1.0, 2.0],
                ),
                PostAssetsReturnsRequestAssetsItem(
                    asset_prices=[2.0, 3.0, 6.0],
                ),
            ],
        )
        """
        _response = self._raw_client.arithmetic_returns(assets=assets, request_options=request_options)
        return _response.data

    def arithmetic_average_return(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsReturnsAverageResponse:
        """
        Compute the arithmetic average of the return(s) of one or several asset(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsReturnsAverageResponse
            OK

        Examples
        --------
        from fern.assets_returns import PostAssetsReturnsAverageRequestAssetsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_returns.arithmetic_average_return(
            assets=[
                PostAssetsReturnsAverageRequestAssetsItem(
                    asset_returns=[0.1, -0.05],
                ),
                PostAssetsReturnsAverageRequestAssetsItem(
                    asset_returns=[0.0, -0.01, 0.01],
                ),
            ],
        )
        """
        _response = self._raw_client.arithmetic_average_return(assets=assets, request_options=request_options)
        return _response.data


class AsyncAssetsReturnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsReturnsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsReturnsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsReturnsClient
        """
        return self._raw_client

    async def arithmetic_returns(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsReturnsResponse:
        """
        Compute the arithmetic return(s) of one or several asset(s) for one or several time period(s).

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsReturnsResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_returns import PostAssetsReturnsRequestAssetsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_returns.arithmetic_returns(
                assets=[
                    PostAssetsReturnsRequestAssetsItem(
                        asset_prices=[1.0, 2.0],
                    ),
                    PostAssetsReturnsRequestAssetsItem(
                        asset_prices=[2.0, 3.0, 6.0],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.arithmetic_returns(assets=assets, request_options=request_options)
        return _response.data

    async def arithmetic_average_return(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsReturnsAverageResponse:
        """
        Compute the arithmetic average of the return(s) of one or several asset(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsAverageRequestAssetsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsReturnsAverageResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_returns import PostAssetsReturnsAverageRequestAssetsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_returns.arithmetic_average_return(
                assets=[
                    PostAssetsReturnsAverageRequestAssetsItem(
                        asset_returns=[0.1, -0.05],
                    ),
                    PostAssetsReturnsAverageRequestAssetsItem(
                        asset_returns=[0.0, -0.01, 0.01],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.arithmetic_average_return(assets=assets, request_options=request_options)
        return _response.data
