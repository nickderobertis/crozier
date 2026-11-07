

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.inclusion_proof import InclusionProof
from ..types.signed_tree_head import SignedTreeHead
from .raw_client import AsyncRawTransparencyClient, RawTransparencyClient
from .types.add_gossip_peer_response import AddGossipPeerResponse
from .types.add_to_log_response import AddToLogResponse
from .types.get_gossip_alerts_response import GetGossipAlertsResponse
from .types.get_gossip_peers_response import GetGossipPeersResponse
from .types.get_log_root_response import GetLogRootResponse
from .types.gossip_exchange_response import GossipExchangeResponse


OMIT = typing.cast(typing.Any, ...)


class TransparencyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTransparencyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTransparencyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTransparencyClient
        """
        return self._raw_client

    def add_to_log(
        self, *, bundle_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AddToLogResponse:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        bundle_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddToLogResponse
            Log entry added

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.add_to_log(
            bundle_hash="bundle_hash",
        )
        """
        _response = self._raw_client.add_to_log(bundle_hash=bundle_hash, request_options=request_options)
        return _response.data

    def get_log_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLogRootResponse:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLogRootResponse
            Current Merkle root of the transparency log

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.get_log_root()
        """
        _response = self._raw_client.get_log_root(request_options=request_options)
        return _response.data

    def get_log_proof(self, index: int, *, request_options: typing.Optional[RequestOptions] = None) -> InclusionProof:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        index : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InclusionProof
            Merkle inclusion proof

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.get_log_proof(
            index=1000000,
        )
        """
        _response = self._raw_client.get_log_proof(index, request_options=request_options)
        return _response.data

    def get_signed_tree_head(self, *, request_options: typing.Optional[RequestOptions] = None) -> SignedTreeHead:
        """
        Returns a Signed Tree Head — the current Merkle root signed by the log operator.
        Used for gossip protocol cross-log verification.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignedTreeHead
            Signed tree head

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.get_signed_tree_head()
        """
        _response = self._raw_client.get_signed_tree_head(request_options=request_options)
        return _response.data

    def get_gossip_peers(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetGossipPeersResponse:
        """
        List all known gossip peers and recent split-view alerts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGossipPeersResponse
            Gossip peers and alerts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.get_gossip_peers()
        """
        _response = self._raw_client.get_gossip_peers(request_options=request_options)
        return _response.data

    def add_gossip_peer(
        self, *, peer_id: str, endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AddGossipPeerResponse:
        """
        Parameters
        ----------
        peer_id : str

        endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddGossipPeerResponse
            Peer added

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.add_gossip_peer(
            peer_id="peer_id",
            endpoint="endpoint",
        )
        """
        _response = self._raw_client.add_gossip_peer(
            peer_id=peer_id, endpoint=endpoint, request_options=request_options
        )
        return _response.data

    def gossip_exchange(
        self, *, sth: typing.Optional[SignedTreeHead] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GossipExchangeResponse:
        """
        Exchange signed tree heads between log instances for cross-verification.
        Detects split-view attacks when roots differ for the same tree size.

        Parameters
        ----------
        sth : typing.Optional[SignedTreeHead]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GossipExchangeResponse
            Local STH and any detected alert

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.gossip_exchange()
        """
        _response = self._raw_client.gossip_exchange(sth=sth, request_options=request_options)
        return _response.data

    def get_gossip_alerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetGossipAlertsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGossipAlertsResponse
            List of detected split-view alerts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.transparency.get_gossip_alerts()
        """
        _response = self._raw_client.get_gossip_alerts(request_options=request_options)
        return _response.data


class AsyncTransparencyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTransparencyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTransparencyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTransparencyClient
        """
        return self._raw_client

    async def add_to_log(
        self, *, bundle_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AddToLogResponse:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        bundle_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddToLogResponse
            Log entry added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.add_to_log(
                bundle_hash="bundle_hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_to_log(bundle_hash=bundle_hash, request_options=request_options)
        return _response.data

    async def get_log_root(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetLogRootResponse:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLogRootResponse
            Current Merkle root of the transparency log

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.get_log_root()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_root(request_options=request_options)
        return _response.data

    async def get_log_proof(
        self, index: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InclusionProof:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        index : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InclusionProof
            Merkle inclusion proof

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.get_log_proof(
                index=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_log_proof(index, request_options=request_options)
        return _response.data

    async def get_signed_tree_head(self, *, request_options: typing.Optional[RequestOptions] = None) -> SignedTreeHead:
        """
        Returns a Signed Tree Head — the current Merkle root signed by the log operator.
        Used for gossip protocol cross-log verification.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SignedTreeHead
            Signed tree head

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.get_signed_tree_head()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_signed_tree_head(request_options=request_options)
        return _response.data

    async def get_gossip_peers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGossipPeersResponse:
        """
        List all known gossip peers and recent split-view alerts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGossipPeersResponse
            Gossip peers and alerts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.get_gossip_peers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gossip_peers(request_options=request_options)
        return _response.data

    async def add_gossip_peer(
        self, *, peer_id: str, endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AddGossipPeerResponse:
        """
        Parameters
        ----------
        peer_id : str

        endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddGossipPeerResponse
            Peer added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.add_gossip_peer(
                peer_id="peer_id",
                endpoint="endpoint",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_gossip_peer(
            peer_id=peer_id, endpoint=endpoint, request_options=request_options
        )
        return _response.data

    async def gossip_exchange(
        self, *, sth: typing.Optional[SignedTreeHead] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GossipExchangeResponse:
        """
        Exchange signed tree heads between log instances for cross-verification.
        Detects split-view attacks when roots differ for the same tree size.

        Parameters
        ----------
        sth : typing.Optional[SignedTreeHead]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GossipExchangeResponse
            Local STH and any detected alert

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.gossip_exchange()


        asyncio.run(main())
        """
        _response = await self._raw_client.gossip_exchange(sth=sth, request_options=request_options)
        return _response.data

    async def get_gossip_alerts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetGossipAlertsResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGossipAlertsResponse
            List of detected split-view alerts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.transparency.get_gossip_alerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gossip_alerts(request_options=request_options)
        return _response.data
