

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.system_info import SystemInfo
from .raw_client import AsyncRawBaseRoutesClient, RawBaseRoutesClient


class BaseRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBaseRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBaseRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBaseRoutesClient
        """
        return self._raw_client

    def base_ok(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a simple OK response

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.base_routes.base_ok()
        """
        _response = self._raw_client.base_ok(request_options=request_options)
        return _response.data

    def base_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Check the health of the service, always returns 200 OK, /healthz is also available

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.base_routes.base_health()
        """
        _response = self._raw_client.base_health(request_options=request_options)
        return _response.data

    def base_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """
        Get system information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.base_routes.base_info()
        """
        _response = self._raw_client.base_info(request_options=request_options)
        return _response.data


class AsyncBaseRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBaseRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBaseRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBaseRoutesClient
        """
        return self._raw_client

    async def base_ok(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Get a simple OK response

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.base_routes.base_ok()


        asyncio.run(main())
        """
        _response = await self._raw_client.base_ok(request_options=request_options)
        return _response.data

    async def base_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Check the health of the service, always returns 200 OK, /healthz is also available

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.base_routes.base_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.base_health(request_options=request_options)
        return _response.data

    async def base_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemInfo:
        """
        Get system information

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemInfo
            The request has succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.base_routes.base_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.base_info(request_options=request_options)
        return _response.data
