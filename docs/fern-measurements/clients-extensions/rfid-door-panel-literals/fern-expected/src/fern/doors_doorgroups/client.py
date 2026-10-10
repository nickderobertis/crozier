

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDoorsDoorgroupsClient, RawDoorsDoorgroupsClient


class DoorsDoorgroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDoorsDoorgroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDoorsDoorgroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDoorsDoorgroupsClient
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
            Door group names.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.doors_doorgroups.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncDoorsDoorgroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDoorsDoorgroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDoorsDoorgroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDoorsDoorgroupsClient
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
            Door group names.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.doors_doorgroups.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
