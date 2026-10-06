

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPacketsClient, RawPacketsClient


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

    def list_packets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Packets.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ledger_region="YOUR_LEDGER_REGION",
        )
        client.packets.list_packets()
        """
        _response = self._raw_client.list_packets(request_options=request_options)
        return _response.data

    def add_packet(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ledger_region="YOUR_LEDGER_REGION",
        )
        client.packets.add_packet()
        """
        _response = self._raw_client.add_packet(request_options=request_options)
        return _response.data

    def get_packet(self, packet_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        packet_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One packet.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ledger_region="YOUR_LEDGER_REGION",
        )
        client.packets.get_packet(
            packet_id="packet_id",
        )
        """
        _response = self._raw_client.get_packet(packet_id, request_options=request_options)
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

    async def list_packets(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Packets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ledger_region="YOUR_LEDGER_REGION",
        )


        async def main() -> None:
            await client.packets.list_packets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_packets(request_options=request_options)
        return _response.data

    async def add_packet(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            ledger_region="YOUR_LEDGER_REGION",
        )


        async def main() -> None:
            await client.packets.add_packet()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_packet(request_options=request_options)
        return _response.data

    async def get_packet(self, packet_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        packet_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One packet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ledger_region="YOUR_LEDGER_REGION",
        )


        async def main() -> None:
            await client.packets.get_packet(
                packet_id="packet_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_packet(packet_id, request_options=request_options)
        return _response.data
