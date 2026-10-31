

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_node_sets_response import ListNodeSetsResponse
from ..types.node_set import NodeSet
from .raw_client import AsyncRawNodeSetsClient, RawNodeSetsClient


class NodeSetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNodeSetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNodeSetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNodeSetsClient
        """
        return self._raw_client

    def list_node_sets(
        self, *, node_pool_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListNodeSetsResponse:
        """
        Returns all node sets, or those of one node pool.

        Parameters
        ----------
        node_pool_id : typing.Optional[str]
            Filter by node pool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNodeSetsResponse
            A list of node sets

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_sets.list_node_sets()
        """
        _response = self._raw_client.list_node_sets(node_pool_id=node_pool_id, request_options=request_options)
        return _response.data

    def get_node_set(self, node_set_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NodeSet:
        """
        Returns one node set.

        Parameters
        ----------
        node_set_id : str
            Node set ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodeSet
            The requested node set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_sets.get_node_set(
            node_set_id="nodeSetID",
        )
        """
        _response = self._raw_client.get_node_set(node_set_id, request_options=request_options)
        return _response.data


class AsyncNodeSetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNodeSetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNodeSetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNodeSetsClient
        """
        return self._raw_client

    async def list_node_sets(
        self, *, node_pool_id: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListNodeSetsResponse:
        """
        Returns all node sets, or those of one node pool.

        Parameters
        ----------
        node_pool_id : typing.Optional[str]
            Filter by node pool ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNodeSetsResponse
            A list of node sets

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_sets.list_node_sets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_node_sets(node_pool_id=node_pool_id, request_options=request_options)
        return _response.data

    async def get_node_set(
        self, node_set_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodeSet:
        """
        Returns one node set.

        Parameters
        ----------
        node_set_id : str
            Node set ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodeSet
            The requested node set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_sets.get_node_set(
                node_set_id="nodeSetID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_node_set(node_set_id, request_options=request_options)
        return _response.data
