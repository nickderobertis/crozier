

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAppClient, RawAppClient


class AppClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppClient
        """
        return self._raw_client

    def info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Application details.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app.info()
        """
        _response = self._raw_client.info(request_options=request_options)
        return _response.data

    def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Application version.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.app.version()
        """
        _response = self._raw_client.version(request_options=request_options)
        return _response.data


class AsyncAppClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppClient
        """
        return self._raw_client

    async def info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Application details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app.info()


        asyncio.run(main())
        """
        _response = await self._raw_client.info(request_options=request_options)
        return _response.data

    async def version(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Application version.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.app.version()


        asyncio.run(main())
        """
        _response = await self._raw_client.version(request_options=request_options)
        return _response.data
