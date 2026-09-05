

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.static_front_end_dict import StaticFrontEndDict
from .raw_client import AsyncRawStaticsClient, RawStaticsClient


class StaticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStaticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStaticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStaticsClient
        """
        return self._raw_client

    def get_cached_frontend_index(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.statics.get_cached_frontend_index()
        """
        _response = self._raw_client.get_cached_frontend_index(request_options=request_options)
        return _response.data

    def static_frontend_data(self, *, request_options: typing.Optional[RequestOptions] = None) -> StaticFrontEndDict:
        """
        Generic static info on the product's app

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StaticFrontEndDict
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.statics.static_frontend_data()
        """
        _response = self._raw_client.static_frontend_data(request_options=request_options)
        return _response.data


class AsyncStaticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStaticsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStaticsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStaticsClient
        """
        return self._raw_client

    async def get_cached_frontend_index(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.statics.get_cached_frontend_index()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cached_frontend_index(request_options=request_options)
        return _response.data

    async def static_frontend_data(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StaticFrontEndDict:
        """
        Generic static info on the product's app

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StaticFrontEndDict
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.statics.static_frontend_data()


        asyncio.run(main())
        """
        _response = await self._raw_client.static_frontend_data(request_options=request_options)
        return _response.data
