

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawEscapeHatchesClient, RawEscapeHatchesClient


class EscapeHatchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEscapeHatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEscapeHatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEscapeHatchesClient
        """
        return self._raw_client

    def get_escape_hatches_plain_text(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            ok

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.escape_hatches.get_escape_hatches_plain_text()
        """
        _response = self._raw_client.get_escape_hatches_plain_text(request_options=request_options)
        return _response.data


class AsyncEscapeHatchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEscapeHatchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEscapeHatchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEscapeHatchesClient
        """
        return self._raw_client

    async def get_escape_hatches_plain_text(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            ok

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.escape_hatches.get_escape_hatches_plain_text()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_escape_hatches_plain_text(request_options=request_options)
        return _response.data
