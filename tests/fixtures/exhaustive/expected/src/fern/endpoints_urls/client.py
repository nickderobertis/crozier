

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEndpointsUrlsClient, RawEndpointsUrlsClient


class EndpointsUrlsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEndpointsUrlsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEndpointsUrlsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEndpointsUrlsClient
        """
        return self._raw_client

    def endpoints_urls_with_mixed_case(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints_urls.endpoints_urls_with_mixed_case()
        """
        _response = self._raw_client.endpoints_urls_with_mixed_case(request_options=request_options)
        return _response.data

    def endpoints_urls_no_ending_slash(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints_urls.endpoints_urls_no_ending_slash()
        """
        _response = self._raw_client.endpoints_urls_no_ending_slash(request_options=request_options)
        return _response.data

    def endpoints_urls_with_ending_slash(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints_urls.endpoints_urls_with_ending_slash()
        """
        _response = self._raw_client.endpoints_urls_with_ending_slash(request_options=request_options)
        return _response.data

    def endpoints_urls_with_underscores(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints_urls.endpoints_urls_with_underscores()
        """
        _response = self._raw_client.endpoints_urls_with_underscores(request_options=request_options)
        return _response.data


class AsyncEndpointsUrlsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEndpointsUrlsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEndpointsUrlsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEndpointsUrlsClient
        """
        return self._raw_client

    async def endpoints_urls_with_mixed_case(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints_urls.endpoints_urls_with_mixed_case()


        asyncio.run(main())
        """
        _response = await self._raw_client.endpoints_urls_with_mixed_case(request_options=request_options)
        return _response.data

    async def endpoints_urls_no_ending_slash(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints_urls.endpoints_urls_no_ending_slash()


        asyncio.run(main())
        """
        _response = await self._raw_client.endpoints_urls_no_ending_slash(request_options=request_options)
        return _response.data

    async def endpoints_urls_with_ending_slash(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints_urls.endpoints_urls_with_ending_slash()


        asyncio.run(main())
        """
        _response = await self._raw_client.endpoints_urls_with_ending_slash(request_options=request_options)
        return _response.data

    async def endpoints_urls_with_underscores(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints_urls.endpoints_urls_with_underscores()


        asyncio.run(main())
        """
        _response = await self._raw_client.endpoints_urls_with_underscores(request_options=request_options)
        return _response.data
