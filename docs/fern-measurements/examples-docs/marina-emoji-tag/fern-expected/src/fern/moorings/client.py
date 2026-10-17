

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account import Account
from .raw_client import AsyncRawMooringsClient, RawMooringsClient


class MooringsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMooringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMooringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMooringsClient
        """
        return self._raw_client

    def list_moorings(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Account]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Account]
            Moorings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.moorings.list_moorings()
        """
        _response = self._raw_client.list_moorings(request_options=request_options)
        return _response.data


class AsyncMooringsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMooringsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMooringsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMooringsClient
        """
        return self._raw_client

    async def list_moorings(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Account]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Account]
            Moorings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.moorings.list_moorings()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_moorings(request_options=request_options)
        return _response.data
