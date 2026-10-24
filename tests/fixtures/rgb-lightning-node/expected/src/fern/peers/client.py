

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empty_response import EmptyResponse
from ..types.list_peers_response import ListPeersResponse
from .raw_client import AsyncRawPeersClient, RawPeersClient


OMIT = typing.cast(typing.Any, ...)


class PeersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPeersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPeersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPeersClient
        """
        return self._raw_client

    def connect_to_a_peer(
        self, *, peer_pubkey_and_addr: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Connect to the provided LN peer

        Parameters
        ----------
        peer_pubkey_and_addr : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.peers.connect_to_a_peer(
            peer_pubkey_and_addr="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d@localhost:9736",
        )
        """
        _response = self._raw_client.connect_to_a_peer(
            peer_pubkey_and_addr=peer_pubkey_and_addr, request_options=request_options
        )
        return _response.data

    def disconnect_from_a_peer(
        self, *, peer_pubkey: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Disconnect from the provided LN peer

        Parameters
        ----------
        peer_pubkey : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.peers.disconnect_from_a_peer(
            peer_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
        )
        """
        _response = self._raw_client.disconnect_from_a_peer(peer_pubkey=peer_pubkey, request_options=request_options)
        return _response.data

    def list_peers(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPeersResponse:
        """
        List the node's LN peers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPeersResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.peers.list_peers()
        """
        _response = self._raw_client.list_peers(request_options=request_options)
        return _response.data


class AsyncPeersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPeersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPeersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPeersClient
        """
        return self._raw_client

    async def connect_to_a_peer(
        self, *, peer_pubkey_and_addr: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Connect to the provided LN peer

        Parameters
        ----------
        peer_pubkey_and_addr : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.peers.connect_to_a_peer(
                peer_pubkey_and_addr="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d@localhost:9736",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_to_a_peer(
            peer_pubkey_and_addr=peer_pubkey_and_addr, request_options=request_options
        )
        return _response.data

    async def disconnect_from_a_peer(
        self, *, peer_pubkey: str, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Disconnect from the provided LN peer

        Parameters
        ----------
        peer_pubkey : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.peers.disconnect_from_a_peer(
                peer_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disconnect_from_a_peer(
            peer_pubkey=peer_pubkey, request_options=request_options
        )
        return _response.data

    async def list_peers(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPeersResponse:
        """
        List the node's LN peers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPeersResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.peers.list_peers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_peers(request_options=request_options)
        return _response.data
