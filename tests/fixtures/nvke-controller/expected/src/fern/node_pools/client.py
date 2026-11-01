

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.launch_layer_node_pool_provider import LaunchLayerNodePoolProvider
from ..types.launch_layer_node_pool_provider_update import LaunchLayerNodePoolProviderUpdate
from ..types.list_node_pools_response import ListNodePoolsResponse
from ..types.nico_node_pool_provider import NicoNodePoolProvider
from ..types.nico_node_pool_provider_update import NicoNodePoolProviderUpdate
from ..types.node_name_prefix import NodeNamePrefix
from ..types.node_pool import NodePool
from ..types.node_taint import NodeTaint
from .raw_client import AsyncRawNodePoolsClient, RawNodePoolsClient


OMIT = typing.cast(typing.Any, ...)


class NodePoolsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNodePoolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNodePoolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNodePoolsClient
        """
        return self._raw_client

    def list_node_pools(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListNodePoolsResponse:
        """
        Returns all node pools, filtered by the query parameters.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node pool name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNodePoolsResponse
            A list of node pools

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_pools.list_node_pools()
        """
        _response = self._raw_client.list_node_pools(
            cluster_id=cluster_id, cluster_name=cluster_name, name=name, request_options=request_options
        )
        return _response.data

    def create_node_pool(
        self,
        *,
        cluster_id: str,
        name: str,
        node_name_prefix: NodeNamePrefix,
        desired_node_count: int,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        machine_annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        machine_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_taints: typing.Optional[typing.Sequence[NodeTaint]] = OMIT,
        description: typing.Optional[str] = OMIT,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        nico: typing.Optional[NicoNodePoolProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NodePool:
        """
        Creates a worker node pool and starts provisioning. The pool takes the
        cluster's Kubernetes version.

        Returns 400 for, among others: parent cluster not found; a duplicate
        pool name in the cluster; missing `nico.instanceTypeID`
        or `nico.release`; not exactly one of
        `subnetIDs` and `vpcPrefixIDs`; a pod CIDR too small for the requested
        nodes.

        Parameters
        ----------
        cluster_id : str
            Parent cluster.

        name : str
            Unique within the cluster. Immutable.

        node_name_prefix : NodeNamePrefix

        desired_node_count : int
            The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. Default 2Gi.

        machine_annotations : typing.Optional[typing.Dict[str, str]]
            Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        machine_labels : typing.Optional[typing.Dict[str, str]]
            Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        node_labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.

        node_taints : typing.Optional[typing.Sequence[NodeTaint]]
            Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.

        description : typing.Optional[str]
            Free-text description.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        nico : typing.Optional[NicoNodePoolProvider]

        launch_layer : typing.Optional[LaunchLayerNodePoolProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodePool
            Node pool created; provisioning has started

        Examples
        --------
        from fern import (
            DiskSelectionStrategyCreate,
            FernApi,
            NicoNodePoolProvider,
            NodeTaint,
            NodeTaintEffect,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_pools.create_node_pool(
            name="gpu-workers-b300",
            node_name_prefix="wb",
            system_reserved_memory="32Gi",
            kube_reserved_memory="4Gi",
            node_labels={"nvidia.com/gpu.product": "B300"},
            node_taints=[
                NodeTaint(
                    key="nvidia.com/dedicated",
                    value="team-b",
                    effect=NodeTaintEffect.NO_SCHEDULE,
                )
            ],
            desired_node_count=4,
            description="Reserved for team-b training jobs",
            recycle_budget=1,
            nico=NicoNodePoolProvider(
                vpc_prefix_i_ds=["2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"],
                instance_type_id="9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
                ssh_key_group_i_ds=["3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"],
                release="example-ubuntu-24.04-amd64",
                disk_selection_strategy=DiskSelectionStrategyCreate.LARGEST,
            ),
            cluster_id="9b1d4e2a-3c5f-4a7b-8e9d-0f1a2b3c4d5e",
        )
        """
        _response = self._raw_client.create_node_pool(
            cluster_id=cluster_id,
            name=name,
            node_name_prefix=node_name_prefix,
            desired_node_count=desired_node_count,
            system_reserved_memory=system_reserved_memory,
            kube_reserved_memory=kube_reserved_memory,
            machine_annotations=machine_annotations,
            machine_labels=machine_labels,
            node_labels=node_labels,
            node_taints=node_taints,
            description=description,
            auto_provision_disabled=auto_provision_disabled,
            auto_mode_disabled=auto_mode_disabled,
            provisioning_monitor_disabled=provisioning_monitor_disabled,
            recycle_budget=recycle_budget,
            nico=nico,
            launch_layer=launch_layer,
            request_options=request_options,
        )
        return _response.data

    def get_node_pool(self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NodePool:
        """
        Returns one node pool.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodePool
            The requested node pool

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_pools.get_node_pool(
            node_pool_id="nodePoolID",
        )
        """
        _response = self._raw_client.get_node_pool(node_pool_id, request_options=request_options)
        return _response.data

    def delete_node_pool(self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a node pool from a running cluster. Also returns 202, with no
        further effect, if the pool or its cluster is already being deleted.

        Returns 409 for a control-plane node pool while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_pools.delete_node_pool(
            node_pool_id="nodePoolID",
        )
        """
        _response = self._raw_client.delete_node_pool(node_pool_id, request_options=request_options)
        return _response.data

    def update_node_pool(
        self,
        node_pool_id: str,
        *,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        desired_node_count: typing.Optional[int] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        max_surge: typing.Optional[int] = OMIT,
        kubernetes_version: typing.Optional[str] = OMIT,
        nico: typing.Optional[NicoNodePoolProviderUpdate] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProviderUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NodePool:
        """
        All fields are optional. Changes to the Kubernetes version, release
        or other node configuration create a new NodeSet and roll the pool's
        nodes to it.

        Returns 400 for, among others: sending a field that is fixed at
        creation (for example `instanceTypeID`); `nico.release: ""`; any update
        to a control-plane node pool, which is configured through the cluster's
        `controlPlaneConfig` instead. That last refusal does not depend on the
        control-plane mutation lock, so retrying later does not help.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. An empty string restores the 2Gi default.

        description : typing.Optional[str]
            Free-text description.

        desired_node_count : typing.Optional[int]
            The desired number of nodes in the pool. Increasing aggregate control-plane capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        max_surge : typing.Optional[int]
            Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each
            node is torn down before its replacement is provisioned.

        kubernetes_version : typing.Optional[str]
            Desired Kubernetes version for the pool's nodes, as X.Y.Z with no leading "v".
            Must be newer than the current version.

        nico : typing.Optional[NicoNodePoolProviderUpdate]

        launch_layer : typing.Optional[LaunchLayerNodePoolProviderUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodePool
            Update accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.node_pools.update_node_pool(
            node_pool_id="nodePoolID",
            desired_node_count=6,
        )
        """
        _response = self._raw_client.update_node_pool(
            node_pool_id,
            auto_provision_disabled=auto_provision_disabled,
            auto_mode_disabled=auto_mode_disabled,
            provisioning_monitor_disabled=provisioning_monitor_disabled,
            system_reserved_memory=system_reserved_memory,
            kube_reserved_memory=kube_reserved_memory,
            description=description,
            desired_node_count=desired_node_count,
            recycle_budget=recycle_budget,
            max_surge=max_surge,
            kubernetes_version=kubernetes_version,
            nico=nico,
            launch_layer=launch_layer,
            request_options=request_options,
        )
        return _response.data


class AsyncNodePoolsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNodePoolsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNodePoolsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNodePoolsClient
        """
        return self._raw_client

    async def list_node_pools(
        self,
        *,
        cluster_id: typing.Optional[str] = None,
        cluster_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListNodePoolsResponse:
        """
        Returns all node pools, filtered by the query parameters.

        Parameters
        ----------
        cluster_id : typing.Optional[str]
            Filter by cluster ID

        cluster_name : typing.Optional[str]
            Filter by cluster name (exact match)

        name : typing.Optional[str]
            Filter by node pool name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNodePoolsResponse
            A list of node pools

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_pools.list_node_pools()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_node_pools(
            cluster_id=cluster_id, cluster_name=cluster_name, name=name, request_options=request_options
        )
        return _response.data

    async def create_node_pool(
        self,
        *,
        cluster_id: str,
        name: str,
        node_name_prefix: NodeNamePrefix,
        desired_node_count: int,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        machine_annotations: typing.Optional[typing.Dict[str, str]] = OMIT,
        machine_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_labels: typing.Optional[typing.Dict[str, str]] = OMIT,
        node_taints: typing.Optional[typing.Sequence[NodeTaint]] = OMIT,
        description: typing.Optional[str] = OMIT,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        nico: typing.Optional[NicoNodePoolProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NodePool:
        """
        Creates a worker node pool and starts provisioning. The pool takes the
        cluster's Kubernetes version.

        Returns 400 for, among others: parent cluster not found; a duplicate
        pool name in the cluster; missing `nico.instanceTypeID`
        or `nico.release`; not exactly one of
        `subnetIDs` and `vpcPrefixIDs`; a pod CIDR too small for the requested
        nodes.

        Parameters
        ----------
        cluster_id : str
            Parent cluster.

        name : str
            Unique within the cluster. Immutable.

        node_name_prefix : NodeNamePrefix

        desired_node_count : int
            The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. Default 2Gi.

        machine_annotations : typing.Optional[typing.Dict[str, str]]
            Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        machine_labels : typing.Optional[typing.Dict[str, str]]
            Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.

        node_labels : typing.Optional[typing.Dict[str, str]]
            Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.

        node_taints : typing.Optional[typing.Sequence[NodeTaint]]
            Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.

        description : typing.Optional[str]
            Free-text description.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        nico : typing.Optional[NicoNodePoolProvider]

        launch_layer : typing.Optional[LaunchLayerNodePoolProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodePool
            Node pool created; provisioning has started

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DiskSelectionStrategyCreate,
            NicoNodePoolProvider,
            NodeTaint,
            NodeTaintEffect,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_pools.create_node_pool(
                name="gpu-workers-b300",
                node_name_prefix="wb",
                system_reserved_memory="32Gi",
                kube_reserved_memory="4Gi",
                node_labels={"nvidia.com/gpu.product": "B300"},
                node_taints=[
                    NodeTaint(
                        key="nvidia.com/dedicated",
                        value="team-b",
                        effect=NodeTaintEffect.NO_SCHEDULE,
                    )
                ],
                desired_node_count=4,
                description="Reserved for team-b training jobs",
                recycle_budget=1,
                nico=NicoNodePoolProvider(
                    vpc_prefix_i_ds=["2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"],
                    instance_type_id="9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
                    ssh_key_group_i_ds=["3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"],
                    release="example-ubuntu-24.04-amd64",
                    disk_selection_strategy=DiskSelectionStrategyCreate.LARGEST,
                ),
                cluster_id="9b1d4e2a-3c5f-4a7b-8e9d-0f1a2b3c4d5e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_node_pool(
            cluster_id=cluster_id,
            name=name,
            node_name_prefix=node_name_prefix,
            desired_node_count=desired_node_count,
            system_reserved_memory=system_reserved_memory,
            kube_reserved_memory=kube_reserved_memory,
            machine_annotations=machine_annotations,
            machine_labels=machine_labels,
            node_labels=node_labels,
            node_taints=node_taints,
            description=description,
            auto_provision_disabled=auto_provision_disabled,
            auto_mode_disabled=auto_mode_disabled,
            provisioning_monitor_disabled=provisioning_monitor_disabled,
            recycle_budget=recycle_budget,
            nico=nico,
            launch_layer=launch_layer,
            request_options=request_options,
        )
        return _response.data

    async def get_node_pool(
        self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NodePool:
        """
        Returns one node pool.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodePool
            The requested node pool

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_pools.get_node_pool(
                node_pool_id="nodePoolID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_node_pool(node_pool_id, request_options=request_options)
        return _response.data

    async def delete_node_pool(
        self, node_pool_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a node pool from a running cluster. Also returns 202, with no
        further effect, if the pool or its cluster is already being deleted.

        Returns 409 for a control-plane node pool while etcd encryption, etcd key
        rotation or certificate renewal holds the control-plane mutation lock.
        Retry once the operation has finished. A failed certificate renewal can
        retain the lock until an operator clears it; see the retained-lock
        recovery procedure in controller/docs/certificate-renewal.md.
        A rotation that fails after `prepare` keeps the `etcd_key_rotation` lock
        until its workflow is reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_pools.delete_node_pool(
                node_pool_id="nodePoolID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_node_pool(node_pool_id, request_options=request_options)
        return _response.data

    async def update_node_pool(
        self,
        node_pool_id: str,
        *,
        auto_provision_disabled: typing.Optional[bool] = OMIT,
        auto_mode_disabled: typing.Optional[bool] = OMIT,
        provisioning_monitor_disabled: typing.Optional[bool] = OMIT,
        system_reserved_memory: typing.Optional[str] = OMIT,
        kube_reserved_memory: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        desired_node_count: typing.Optional[int] = OMIT,
        recycle_budget: typing.Optional[int] = OMIT,
        max_surge: typing.Optional[int] = OMIT,
        kubernetes_version: typing.Optional[str] = OMIT,
        nico: typing.Optional[NicoNodePoolProviderUpdate] = OMIT,
        launch_layer: typing.Optional[LaunchLayerNodePoolProviderUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> NodePool:
        """
        All fields are optional. Changes to the Kubernetes version, release
        or other node configuration create a new NodeSet and roll the pool's
        nodes to it.

        Returns 400 for, among others: sending a field that is fixed at
        creation (for example `instanceTypeID`); `nico.release: ""`; any update
        to a control-plane node pool, which is configured through the cluster's
        `controlPlaneConfig` instead. That last refusal does not depend on the
        control-plane mutation lock, so retrying later does not help.

        Parameters
        ----------
        node_pool_id : str
            Node pool ID.

        auto_provision_disabled : typing.Optional[bool]
            Disables automatic provisioning for the pool.

        auto_mode_disabled : typing.Optional[bool]
            Disables auto-mode (automatic node recycling).

        provisioning_monitor_disabled : typing.Optional[bool]
            When true, nodes stuck in provisioning past the timeout are not recycled automatically.

        system_reserved_memory : typing.Optional[str]
            Memory reserved for system daemons. Nodes reserve 16Gi when omitted.

        kube_reserved_memory : typing.Optional[str]
            Memory reserved for Kubernetes components. An empty string restores the 2Gi default.

        description : typing.Optional[str]
            Free-text description.

        desired_node_count : typing.Optional[int]
            The desired number of nodes in the pool. Increasing aggregate control-plane capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.

        recycle_budget : typing.Optional[int]
            Maximum number of nodes recycled at once.

        max_surge : typing.Optional[int]
            Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each
            node is torn down before its replacement is provisioned.

        kubernetes_version : typing.Optional[str]
            Desired Kubernetes version for the pool's nodes, as X.Y.Z with no leading "v".
            Must be newer than the current version.

        nico : typing.Optional[NicoNodePoolProviderUpdate]

        launch_layer : typing.Optional[LaunchLayerNodePoolProviderUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NodePool
            Update accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.node_pools.update_node_pool(
                node_pool_id="nodePoolID",
                desired_node_count=6,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_node_pool(
            node_pool_id,
            auto_provision_disabled=auto_provision_disabled,
            auto_mode_disabled=auto_mode_disabled,
            provisioning_monitor_disabled=provisioning_monitor_disabled,
            system_reserved_memory=system_reserved_memory,
            kube_reserved_memory=kube_reserved_memory,
            description=description,
            desired_node_count=desired_node_count,
            recycle_budget=recycle_budget,
            max_surge=max_surge,
            kubernetes_version=kubernetes_version,
            nico=nico,
            launch_layer=launch_layer,
            request_options=request_options,
        )
        return _response.data
