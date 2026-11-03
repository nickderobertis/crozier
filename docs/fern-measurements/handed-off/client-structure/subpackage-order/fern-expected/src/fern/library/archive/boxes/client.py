

import typing

from ....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ....core.request_options import RequestOptions
from .raw_client import AsyncRawBoxesClient, RawBoxesClient


class BoxesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBoxesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBoxesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBoxesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Archive boxes.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.library.archive.boxes.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncBoxesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBoxesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBoxesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBoxesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Archive boxes.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.library.archive.boxes.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
