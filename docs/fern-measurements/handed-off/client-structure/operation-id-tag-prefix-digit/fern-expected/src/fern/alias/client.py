

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAliasClient, RawAliasClient


class AliasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAliasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAliasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAliasClient
        """
        return self._raw_client

    def alias_val2(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The second-generation alias.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alias.alias_val2()
        """
        _response = self._raw_client.alias_val2(request_options=request_options)
        return _response.data

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Every alias.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alias.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def alias_v3(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The third-generation alias.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.alias.alias_v3()
        """
        _response = self._raw_client.alias_v3(request_options=request_options)
        return _response.data


class AsyncAliasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAliasClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAliasClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAliasClient
        """
        return self._raw_client

    async def alias_val2(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The second-generation alias.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alias.alias_val2()


        asyncio.run(main())
        """
        _response = await self._raw_client.alias_val2(request_options=request_options)
        return _response.data

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Every alias.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alias.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def alias_v3(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The third-generation alias.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.alias.alias_v3()


        asyncio.run(main())
        """
        _response = await self._raw_client.alias_v3(request_options=request_options)
        return _response.data
