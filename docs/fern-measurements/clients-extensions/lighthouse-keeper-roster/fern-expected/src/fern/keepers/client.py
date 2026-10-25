

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.keeper import Keeper
from .raw_client import AsyncRawKeepersClient, RawKeepersClient


class KeepersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawKeepersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawKeepersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawKeepersClient
        """
        return self._raw_client

    def list_keepers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Keeper]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Keeper]
            The keepers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.keepers.list_keepers()
        """
        _response = self._raw_client.list_keepers(request_options=request_options)
        return _response.data


class AsyncKeepersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawKeepersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawKeepersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawKeepersClient
        """
        return self._raw_client

    async def list_keepers(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Keeper]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Keeper]
            The keepers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.keepers.list_keepers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_keepers(request_options=request_options)
        return _response.data
