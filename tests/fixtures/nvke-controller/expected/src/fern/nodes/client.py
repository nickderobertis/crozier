

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_nodes_response import ListNodesResponse
from ..types.machine_health_issue import MachineHealthIssue
from ..types.node import Node
from .raw_client import AsyncRawNodesClient, RawNodesClient


OMIT = typing.cast(typing.Any, ...)


class NodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNodesClient
        """
        return self._raw_client

    def list_nodes(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        node_pool_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        control_plane: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListNodesResponse:
        """
        Returns all nodes, filtered by the query parameters. All filters are exact match.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        node_pool_id : typing.Optional[str]
            Filter by node pool ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node name (exact match)

        control_plane : typing.Optional[bool]
            `true` returns only control-plane nodes; `false` only workers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNodesResponse
            A list of nodes

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.nodes.list_nodes()
        """
        _response = self._raw_client.list_nodes(
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            cluster_name=cluster_name,
            name=name,
            control_plane=control_plane,
            request_options=request_options,
        )
        return _response.data

    def get_node(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Node:
        """
        Returns one node. Control-plane nodes do not belong to a node pool, so
        their `nodePoolID` and `nodeSetID` are the nil UUID. `nico` is omitted
        when none of its fields are set.

        Parameters
        ----------
        node_id : str
            Node ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Node
            The requested node

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.nodes.get_node(
            node_id="nodeID",
        )
        """
        _response = self._raw_client.get_node(node_id, request_options=request_options)
        return _response.data

    def delete_node(
        self,
        node_id: str,
        *,
        machine_health_issue: typing.Optional[MachineHealthIssue] = OMIT,
        force_unreachable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a single node from a running cluster. Include a
        `machineHealthIssue` to flag the underlying machine for repair.

        For control-plane nodes, a delete sets `deleteRequested`; NVKE then
        starts teardowns one node at a time. `forceUnreachable` is applied
        automatically when the node is unhealthy.

        Also returns 202, with no further effect, if the node, pool or cluster
        is already being deleted or a delete is already requested.

        Returns 400 when deletion would leave no joined control-plane node or
        `machineHealthIssue` is invalid. Delete the cluster to remove its last
        joined control-plane node.
        Deleting a control-plane node requires controlPlaneVIP because the controller
        replaces it, unless allowControlPlaneWithoutVIP is enabled for development.
        Worker node deletion is unaffected.

        Returns 409 for a control-plane node while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_id : str
            Node ID.

        machine_health_issue : typing.Optional[MachineHealthIssue]

        force_unreachable : typing.Optional[bool]
            Treat the node as unreachable: graceful drain and shutdown are attempted, and
            failures are tolerated. Failures removing a control-plane node's etcd member are
            not tolerated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, MachineHealthIssue

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.nodes.delete_node(
            node_id="nodeID",
            machine_health_issue=MachineHealthIssue(
                category="Hardware",
                summary="Node only has 7 GPUs",
                details="The node reboot completed at 12:51Z and it started reporting XID 79 at 14:09Z",
            ),
            force_unreachable=True,
        )
        """
        _response = self._raw_client.delete_node(
            node_id,
            machine_health_issue=machine_health_issue,
            force_unreachable=force_unreachable,
            request_options=request_options,
        )
        return _response.data


class AsyncNodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNodesClient
        """
        return self._raw_client

    async def list_nodes(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        node_pool_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        control_plane: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListNodesResponse:
        """
        Returns all nodes, filtered by the query parameters. All filters are exact match.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        node_pool_id : typing.Optional[str]
            Filter by node pool ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node name (exact match)

        control_plane : typing.Optional[bool]
            `true` returns only control-plane nodes; `false` only workers

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNodesResponse
            A list of nodes

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.nodes.list_nodes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_nodes(
            cluster_id=cluster_id,
            node_pool_id=node_pool_id,
            cluster_name=cluster_name,
            name=name,
            control_plane=control_plane,
            request_options=request_options,
        )
        return _response.data

    async def get_node(self, node_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Node:
        """
        Returns one node. Control-plane nodes do not belong to a node pool, so
        their `nodePoolID` and `nodeSetID` are the nil UUID. `nico` is omitted
        when none of its fields are set.

        Parameters
        ----------
        node_id : str
            Node ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Node
            The requested node

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.nodes.get_node(
                node_id="nodeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_node(node_id, request_options=request_options)
        return _response.data

    async def delete_node(
        self,
        node_id: str,
        *,
        machine_health_issue: typing.Optional[MachineHealthIssue] = OMIT,
        force_unreachable: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a single node from a running cluster. Include a
        `machineHealthIssue` to flag the underlying machine for repair.

        For control-plane nodes, a delete sets `deleteRequested`; NVKE then
        starts teardowns one node at a time. `forceUnreachable` is applied
        automatically when the node is unhealthy.

        Also returns 202, with no further effect, if the node, pool or cluster
        is already being deleted or a delete is already requested.

        Returns 400 when deletion would leave no joined control-plane node or
        `machineHealthIssue` is invalid. Delete the cluster to remove its last
        joined control-plane node.
        Deleting a control-plane node requires controlPlaneVIP because the controller
        replaces it, unless allowControlPlaneWithoutVIP is enabled for development.
        Worker node deletion is unaffected.

        Returns 409 for a control-plane node while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_id : str
            Node ID.

        machine_health_issue : typing.Optional[MachineHealthIssue]

        force_unreachable : typing.Optional[bool]
            Treat the node as unreachable: graceful drain and shutdown are attempted, and
            failures are tolerated. Failures removing a control-plane node's etcd member are
            not tolerated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MachineHealthIssue

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.nodes.delete_node(
                node_id="nodeID",
                machine_health_issue=MachineHealthIssue(
                    category="Hardware",
                    summary="Node only has 7 GPUs",
                    details="The node reboot completed at 12:51Z and it started reporting XID 79 at 14:09Z",
                ),
                force_unreachable=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_node(
            node_id,
            machine_health_issue=machine_health_issue,
            force_unreachable=force_unreachable,
            request_options=request_options,
        )
        return _response.data
