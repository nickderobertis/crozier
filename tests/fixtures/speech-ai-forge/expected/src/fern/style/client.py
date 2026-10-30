

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.base_response import BaseResponse
from .raw_client import AsyncRawStyleClient, RawStyleClient


class StyleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStyleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStyleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStyleClient
        """
        return self._raw_client

    def list_styles(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        **DEPRECATED**
        This API is deprecated and will be removed in the future. We will replace it with the speaker system and prompt system.

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
        client.style.list_styles()
        """
        _response = self._raw_client.list_styles(request_options=request_options)
        return _response.data


class AsyncStyleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStyleClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStyleClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStyleClient
        """
        return self._raw_client

    async def list_styles(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseResponse:
        """
        **DEPRECATED**
        This API is deprecated and will be removed in the future. We will replace it with the speaker system and prompt system.

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
            await client.style.list_styles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_styles(request_options=request_options)
        return _response.data
