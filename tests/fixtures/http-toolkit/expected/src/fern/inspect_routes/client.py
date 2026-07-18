

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.request_info import RequestInfo
from .raw_client import AsyncRawInspectRoutesClient, RawInspectRoutesClient


class InspectRoutesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInspectRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInspectRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInspectRoutesClient
        """
        return self._raw_client

    def inspect_inspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_routes.inspect_inspect()
        """
        _response = self._raw_client.inspect_inspect(request_options=request_options)
        return _response.data

    def inspect_inspect_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_routes.inspect_inspect_post()
        """
        _response = self._raw_client.inspect_inspect_post(request_options=request_options)
        return _response.data

    def inspect_inspect_put(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_routes.inspect_inspect_put()
        """
        _response = self._raw_client.inspect_inspect_put(request_options=request_options)
        return _response.data

    def inspect_inspect_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_routes.inspect_inspect_delete()
        """
        _response = self._raw_client.inspect_inspect_delete(request_options=request_options)
        return _response.data

    def inspect_inspect_patch(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
            The request has succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_routes.inspect_inspect_patch()
        """
        _response = self._raw_client.inspect_inspect_patch(request_options=request_options)
        return _response.data


class AsyncInspectRoutesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInspectRoutesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInspectRoutesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInspectRoutesClient
        """
        return self._raw_client

    async def inspect_inspect(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
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
            await client.inspect_routes.inspect_inspect()


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_inspect(request_options=request_options)
        return _response.data

    async def inspect_inspect_post(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
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
            await client.inspect_routes.inspect_inspect_post()


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_inspect_post(request_options=request_options)
        return _response.data

    async def inspect_inspect_put(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
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
            await client.inspect_routes.inspect_inspect_put()


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_inspect_put(request_options=request_options)
        return _response.data

    async def inspect_inspect_delete(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
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
            await client.inspect_routes.inspect_inspect_delete()


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_inspect_delete(request_options=request_options)
        return _response.data

    async def inspect_inspect_patch(self, *, request_options: typing.Optional[RequestOptions] = None) -> RequestInfo:
        """
        Inspect the incoming HTTP request and return the details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RequestInfo
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
            await client.inspect_routes.inspect_inspect_patch()


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_inspect_patch(request_options=request_options)
        return _response.data
