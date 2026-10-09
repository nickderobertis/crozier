

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sea_state import SeaState
from .raw_client import AsyncRawSailingsClient, RawSailingsClient


class SailingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSailingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSailingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSailingsClient
        """
        return self._raw_client

    def list_sailings(
        self, *, sea: typing.Optional[SeaState] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        sea : typing.Optional[SeaState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sailings.list_sailings()
        """
        _response = self._raw_client.list_sailings(sea=sea, request_options=request_options)
        return _response.data


class AsyncSailingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSailingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSailingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSailingsClient
        """
        return self._raw_client

    async def list_sailings(
        self, *, sea: typing.Optional[SeaState] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        sea : typing.Optional[SeaState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sailings.list_sailings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sailings(sea=sea, request_options=request_options)
        return _response.data
