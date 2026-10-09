

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stove import Stove
from .raw_client import AsyncRawStovesClient, RawStovesClient


class StovesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStovesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStovesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStovesClient
        """
        return self._raw_client

    def fetch_stove(self, stove_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Stove:
        """
        Parameters
        ----------
        stove_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stove
            The stove.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stoves.fetch_stove(
            stove_id="stoveId",
        )
        """
        _response = self._raw_client.fetch_stove(stove_id, request_options=request_options)
        return _response.data


class AsyncStovesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStovesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStovesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStovesClient
        """
        return self._raw_client

    async def fetch_stove(self, stove_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Stove:
        """
        Parameters
        ----------
        stove_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stove
            The stove.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stoves.fetch_stove(
                stove_id="stoveId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_stove(stove_id, request_options=request_options)
        return _response.data
