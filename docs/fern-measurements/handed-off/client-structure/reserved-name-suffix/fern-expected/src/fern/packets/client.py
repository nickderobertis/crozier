

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.packet import Packet
from .raw_client import AsyncRawPacketsClient, RawPacketsClient


OMIT = typing.cast(typing.Any, ...)


class PacketsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPacketsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPacketsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPacketsClient
        """
        return self._raw_client

    def get_packet(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> Packet:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Packet
            The packet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packets.get_packet(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_packet(uuid_, request_options=request_options)
        return _response.data

    def relabel_packet(
        self,
        uuid_: str,
        *,
        label: str,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Packet:
        """
        Parameters
        ----------
        uuid_ : str

        label : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Packet
            The relabelled packet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packets.relabel_packet(
            uuid_="uuid",
            label="label",
        )
        """
        _response = self._raw_client.relabel_packet(uuid_, label=label, note=note, request_options=request_options)
        return _response.data


class AsyncPacketsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPacketsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPacketsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPacketsClient
        """
        return self._raw_client

    async def get_packet(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> Packet:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Packet
            The packet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packets.get_packet(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_packet(uuid_, request_options=request_options)
        return _response.data

    async def relabel_packet(
        self,
        uuid_: str,
        *,
        label: str,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Packet:
        """
        Parameters
        ----------
        uuid_ : str

        label : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Packet
            The relabelled packet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packets.relabel_packet(
                uuid_="uuid",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.relabel_packet(
            uuid_, label=label, note=note, request_options=request_options
        )
        return _response.data
