

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.lamp import Lamp
from ..types.lamp_colour import LampColour
from .raw_client import AsyncRawClient, RawClient


class Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClient
        """
        return self._raw_client

    def list_lamps(
        self, *, colour: typing.Optional[LampColour] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Lamp]:
        """
        Parameters
        ----------
        colour : typing.Optional[LampColour]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Lamp]
            The lamps

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client..list_lamps()
        """
        _response = self._raw_client.list_lamps(colour=colour, request_options=request_options)
        return _response.data


class AsyncClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClient
        """
        return self._raw_client

    async def list_lamps(
        self, *, colour: typing.Optional[LampColour] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Lamp]:
        """
        Parameters
        ----------
        colour : typing.Optional[LampColour]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Lamp]
            The lamps

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()
        async def main() -> None:
            await client..list_lamps()
        asyncio.run(main())
        """
        _response = await self._raw_client.list_lamps(colour=colour, request_options=request_options)
        return _response.data
