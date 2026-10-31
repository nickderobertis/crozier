

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.base_response import BaseResponse
from .raw_client import AsyncRawSystemClient, RawSystemClient


class SystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemClient
        """
        return self._raw_client

    def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Health check

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.ping()
        """
        _response = self._raw_client.ping(request_options=request_options)
        return _response.data

    def get_versions(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Get versions

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_versions()
        """
        _response = self._raw_client.get_versions(request_options=request_options)
        return _response.data

    def get_audio_formats(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Get audio encoder formats

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.system.get_audio_formats()
        """
        _response = self._raw_client.get_audio_formats(request_options=request_options)
        return _response.data


class AsyncSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemClient
        """
        return self._raw_client

    async def ping(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Health check

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.ping()


        asyncio.run(main())
        """
        _response = await self._raw_client.ping(request_options=request_options)
        return _response.data

    async def get_versions(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Get versions

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_versions()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_versions(request_options=request_options)
        return _response.data

    async def get_audio_formats(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        Get audio encoder formats

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.system.get_audio_formats()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_audio_formats(request_options=request_options)
        return _response.data
