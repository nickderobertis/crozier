

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cluster import Cluster
from ..types.cluster_network_create_config import ClusterNetworkCreateConfig
from ..types.cluster_spire_server_status import ClusterSpireServerStatus
from ..types.create_cluster_control_plane_config import CreateClusterControlPlaneConfig
from ..types.launch_layer_cluster_provider import LaunchLayerClusterProvider
from ..types.list_clusters_response import ListClustersResponse
from ..types.nico_cluster_provider import NicoClusterProvider
from ..types.node_pool_create_config import NodePoolCreateConfig
from ..types.update_cluster_control_plane_config import UpdateClusterControlPlaneConfig
from .raw_client import AsyncRawClustersClient, RawClustersClient


OMIT = typing.cast(typing.Any, ...)


class ClustersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClustersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClustersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClustersClient
        """
        return self._raw_client

    def list_clusters(
        self, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListClustersResponse:
        """
        Returns all clusters, or the cluster whose name matches `name`.

        Parameters
        ----------
        name : typing.Optional[str]
            Filter clusters by name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListClustersResponse
            A list of clusters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clusters.list_clusters()
        """
        _response = self._raw_client.list_clusters(name=name, request_options=request_options)
        return _response.data

    def create_cluster(
        self,
        *,
        name: str,
        control_plane_kubernetes_version: str,
        etcd_encrypted: bool,
        control_plane_vip: typing.Optional[str] = OMIT,
        network: typing.Optional[ClusterNetworkCreateConfig] = OMIT,
        node_pools: typing.Optional[typing.Sequence[NodePoolCreateConfig]] = OMIT,
        control_plane_config: typing.Optional[CreateClusterControlPlaneConfig] = OMIT,
        nico: typing.Optional[NicoClusterProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerClusterProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """
        Creates a cluster and starts provisioning. The cluster is returned before
        provisioning completes.

        Returns 400 for, among others: a duplicate cluster name; missing
        `nico.orgID`, `siteID` or `vpcID`; an unsupported `cniPlugin`; a
        missing `controlPlaneConfig.nico.release`; a
        control-plane `maxSurge` greater than 1; a pod CIDR too small for the
        requested nodes plus surge; a `controlPlaneVIP` inside the pod or
        service CIDR.

        Parameters
        ----------
        name : str
            Cluster name. Lowercase DNS label, unique per management plane. Node names are derived from it.

        control_plane_kubernetes_version : str
            Kubernetes version for the cluster, as X.Y.Z with no leading "v".

        etcd_encrypted : bool
            Encrypt etcd at rest. Can be turned on later with `enableEtcdEncryption`; cannot be turned off.

        control_plane_vip : typing.Optional[str]
            Virtual IP for the API server through kube-vip. Omit to skip kube-vip and
            use the first control-plane node's IP as the API server endpoint. Must not
            fall inside the pod or service CIDR. An explicit empty string is rejected.
            By default, a cluster without a VIP must have exactly one desired
            control-plane node. Scale-up above one node, upgrades and node replacement
            require a VIP unless the controller deployment enables the development-only
            allowControlPlaneWithoutVIP setting. That override keeps the initializing
            node's IP as the endpoint; replacing that node can break API access.
            Quorum, health and deletion protections still apply.

        network : typing.Optional[ClusterNetworkCreateConfig]

        node_pools : typing.Optional[typing.Sequence[NodePoolCreateConfig]]
            Initial worker node pools.

        control_plane_config : typing.Optional[CreateClusterControlPlaneConfig]

        nico : typing.Optional[NicoClusterProvider]

        launch_layer : typing.Optional[LaunchLayerClusterProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster
            Cluster created; provisioning has started

        Examples
        --------
        from fern import (
            ClusterNetworkCreateConfig,
            CreateClusterControlPlaneConfig,
            FernApi,
            NicoClusterProvider,
            NicoControlPlaneProviderCreate,
            NicoNodePoolProvider,
            NodePoolCreateConfig,
            NodeTaint,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clusters.create_cluster(
            name="tenant-a-prod",
            control_plane_kubernetes_version="1.33.4",
            etcd_encrypted=True,
            network=ClusterNetworkCreateConfig(
                pod_cidr="192.168.0.0/16",
                service_cidr="10.96.0.0/12",
            ),
            node_pools=[
                NodePoolCreateConfig(
                    name="gpu-workers",
                    node_name_prefix="w",
                    system_reserved_memory="16Gi",
                    node_labels={"nvidia.com/gpu.present": "true"},
                    node_taints=[
                        NodeTaint(
                            key="nvidia.com/dedicated",
                            value="gpu",
                            effect="NoSchedule",
                        )
                    ],
                    desired_node_count=2,
                    recycle_budget=1,
                    nico=NicoNodePoolProvider(
                        vpc_prefix_i_ds=["2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"],
                        instance_type_id="0d2f4a6c-8e0b-4d2f-9a4c-6e8b0d2f4a6c",
                        ssh_key_group_i_ds=["3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"],
                        release="example-ubuntu-24.04-amd64",
                    ),
                )
            ],
            control_plane_config=CreateClusterControlPlaneConfig(
                desired_count=3,
                max_surge=1,
                system_reserved_memory="16Gi",
                nico=NicoControlPlaneProviderCreate(
                    instance_type_preference=["1c3e5a7f-9b1d-4f3e-a5c7-e9b1d3f5a7c9"],
                    vpc_prefix_i_ds=["2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"],
                    release="example-ubuntu-24.04-amd64",
                    ssh_key_group_i_ds=["3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"],
                ),
            ),
            nico=NicoClusterProvider(
                org_id="dipfedrcvjiw",
                site_id="4f6a8c2e-1b3d-4e5f-a7b9-c1d3e5f7a9b1",
                vpc_id="6a8c0e4f-3d5b-4f7a-b9c1-e3f5a7b9c1d3",
            ),
        )
        """
        _response = self._raw_client.create_cluster(
            name=name,
            control_plane_kubernetes_version=control_plane_kubernetes_version,
            etcd_encrypted=etcd_encrypted,
            control_plane_vip=control_plane_vip,
            network=network,
            node_pools=node_pools,
            control_plane_config=control_plane_config,
            nico=nico,
            launch_layer=launch_layer,
            request_options=request_options,
        )
        return _response.data

    def get_cluster(self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Cluster:
        """
        Returns one cluster. Once provisioning finishes, `conditions.provisioning`
        is False and `conditions.provisioned` is True.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster
            The requested cluster

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clusters.get_cluster(
            cluster_id="clusterID",
        )
        """
        _response = self._raw_client.get_cluster(cluster_id, request_options=request_options)
        return _response.data

    def delete_cluster(self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Starts deletion and sets `conditions.deleting` to `True`. A cluster can
        be deleted in any state, including while it is provisioning or
        upgrading. Deletion takes precedence over an in-progress or retained
        etcd encryption, etcd key rotation or certificate renewal.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

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
        client.clusters.delete_cluster(
            cluster_id="clusterID",
        )
        """
        _response = self._raw_client.delete_cluster(cluster_id, request_options=request_options)
        return _response.data

    def update_cluster(
        self,
        cluster_id: str,
        *,
        enable_cp_node_recycling: typing.Optional[bool] = OMIT,
        control_plane_kubernetes_version: typing.Optional[str] = OMIT,
        enable_etcd_encryption: typing.Optional[bool] = OMIT,
        enable_oidc: typing.Optional[bool] = OMIT,
        control_plane_config: typing.Optional[UpdateClusterControlPlaneConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """
        All fields are optional. See the API description for merge rules.

        Returns 400 for, among others: a Kubernetes downgrade, major-version
        change, or a jump of more than one minor version; an upgrade that would
        leave a worker pool more than 3 minor versions behind;
        `enableEtcdEncryption: false` or `enableOidc: false`; combining OIDC or
        etcd enablement with a version upgrade; etcd or OIDC enablement on a
        cluster that is not provisioned or is deleting; any `network` value;
        a control-plane `maxSurge` greater than 1.

        Returns 409 when another mutually exclusive cluster operation is in
        progress (`etcd_encryption`, `etcd_key_rotation`, `k8s_upgrade`,
        `cp_nodes_recycling`, `oidc_enable`, `certificate_renewal`), or the
        control plane is upgrading or recycling nodes. A failed certificate
        renewal can retain the lock until an operator clears it; see the
        retained-lock recovery procedure in
        controller/docs/certificate-renewal.md. A rotation that fails after
        `prepare` keeps the `etcd_key_rotation` lock until its workflow is
        reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        enable_cp_node_recycling : typing.Optional[bool]
            Turn automatic control-plane node replacement on or off.

        control_plane_kubernetes_version : typing.Optional[str]
            Target control-plane version, as X.Y.Z with no leading "v". Must be newer than
            the current version by at most one minor version and keep every worker pool
            within 3 minor versions.
            The cluster must have controlPlaneVIP configured unless the development-only
            allowControlPlaneWithoutVIP setting is enabled.

        enable_etcd_encryption : typing.Optional[bool]
            `true` starts one-way etcd encryption on a provisioned cluster. `false` is
            rejected. `true` on an already-encrypted cluster does nothing. Other updates
            return 409 while it runs.

        enable_oidc : typing.Optional[bool]
            `true` starts one-way OIDC authentication enablement. `false` is rejected.
            Cannot be combined with a control-plane upgrade or etcd enablement. Other
            updates return 409 while it runs.

        control_plane_config : typing.Optional[UpdateClusterControlPlaneConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster
            Update accepted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clusters.update_cluster(
            cluster_id="clusterID",
            enable_cp_node_recycling=True,
            control_plane_kubernetes_version="1.34.2",
        )
        """
        _response = self._raw_client.update_cluster(
            cluster_id,
            enable_cp_node_recycling=enable_cp_node_recycling,
            control_plane_kubernetes_version=control_plane_kubernetes_version,
            enable_etcd_encryption=enable_etcd_encryption,
            enable_oidc=enable_oidc,
            control_plane_config=control_plane_config,
            request_options=request_options,
        )
        return _response.data

    def get_cluster_spire_server(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClusterSpireServerStatus:
        """
        Returns the SPIRE server last requested through
        `PATCH /clusters/{clusterID}/spire-server`, and for each node the
        server its SPIRE agent points at and whether the agent holds a valid
        X.509 SVID from it. Node status is read live from each node agent on
        every call; an unreachable node is reported with `reachable: false`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterSpireServerStatus
            Requested server and live per-node SPIRE agent status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.clusters.get_cluster_spire_server(
            cluster_id="clusterID",
        )
        """
        _response = self._raw_client.get_cluster_spire_server(cluster_id, request_options=request_options)
        return _response.data

    def update_cluster_spire_server(
        self, cluster_id: str, *, address: str, port: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Starts a `spire_server_update` operation that points the SPIRE agent on
        every node of the cluster at the given server and waits for each agent
        to hold an SVID from it. Track it through `conditions.updateInProgress`
        and `conditions.updateFailed` on the cluster, and per node through
        `GET /clusters/{clusterID}/spire-server`. Repeating the request with
        the same server is safe, including while it is in progress.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        address : str
            Host name or IP address of the SPIRE server.

        port : int
            SPIRE server port.

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
        client.clusters.update_cluster_spire_server(
            cluster_id="clusterID",
            address="192.168.150.100",
            port=30440,
        )
        """
        _response = self._raw_client.update_cluster_spire_server(
            cluster_id, address=address, port=port, request_options=request_options
        )
        return _response.data


class AsyncClustersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClustersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClustersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClustersClient
        """
        return self._raw_client

    async def list_clusters(
        self, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListClustersResponse:
        """
        Returns all clusters, or the cluster whose name matches `name`.

        Parameters
        ----------
        name : typing.Optional[str]
            Filter clusters by name (exact match)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListClustersResponse
            A list of clusters

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clusters.list_clusters()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_clusters(name=name, request_options=request_options)
        return _response.data

    async def create_cluster(
        self,
        *,
        name: str,
        control_plane_kubernetes_version: str,
        etcd_encrypted: bool,
        control_plane_vip: typing.Optional[str] = OMIT,
        network: typing.Optional[ClusterNetworkCreateConfig] = OMIT,
        node_pools: typing.Optional[typing.Sequence[NodePoolCreateConfig]] = OMIT,
        control_plane_config: typing.Optional[CreateClusterControlPlaneConfig] = OMIT,
        nico: typing.Optional[NicoClusterProvider] = OMIT,
        launch_layer: typing.Optional[LaunchLayerClusterProvider] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """
        Creates a cluster and starts provisioning. The cluster is returned before
        provisioning completes.

        Returns 400 for, among others: a duplicate cluster name; missing
        `nico.orgID`, `siteID` or `vpcID`; an unsupported `cniPlugin`; a
        missing `controlPlaneConfig.nico.release`; a
        control-plane `maxSurge` greater than 1; a pod CIDR too small for the
        requested nodes plus surge; a `controlPlaneVIP` inside the pod or
        service CIDR.

        Parameters
        ----------
        name : str
            Cluster name. Lowercase DNS label, unique per management plane. Node names are derived from it.

        control_plane_kubernetes_version : str
            Kubernetes version for the cluster, as X.Y.Z with no leading "v".

        etcd_encrypted : bool
            Encrypt etcd at rest. Can be turned on later with `enableEtcdEncryption`; cannot be turned off.

        control_plane_vip : typing.Optional[str]
            Virtual IP for the API server through kube-vip. Omit to skip kube-vip and
            use the first control-plane node's IP as the API server endpoint. Must not
            fall inside the pod or service CIDR. An explicit empty string is rejected.
            By default, a cluster without a VIP must have exactly one desired
            control-plane node. Scale-up above one node, upgrades and node replacement
            require a VIP unless the controller deployment enables the development-only
            allowControlPlaneWithoutVIP setting. That override keeps the initializing
            node's IP as the endpoint; replacing that node can break API access.
            Quorum, health and deletion protections still apply.

        network : typing.Optional[ClusterNetworkCreateConfig]

        node_pools : typing.Optional[typing.Sequence[NodePoolCreateConfig]]
            Initial worker node pools.

        control_plane_config : typing.Optional[CreateClusterControlPlaneConfig]

        nico : typing.Optional[NicoClusterProvider]

        launch_layer : typing.Optional[LaunchLayerClusterProvider]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster
            Cluster created; provisioning has started

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ClusterNetworkCreateConfig,
            CreateClusterControlPlaneConfig,
            NicoClusterProvider,
            NicoControlPlaneProviderCreate,
            NicoNodePoolProvider,
            NodePoolCreateConfig,
            NodeTaint,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clusters.create_cluster(
                name="tenant-a-prod",
                control_plane_kubernetes_version="1.33.4",
                etcd_encrypted=True,
                network=ClusterNetworkCreateConfig(
                    pod_cidr="192.168.0.0/16",
                    service_cidr="10.96.0.0/12",
                ),
                node_pools=[
                    NodePoolCreateConfig(
                        name="gpu-workers",
                        node_name_prefix="w",
                        system_reserved_memory="16Gi",
                        node_labels={"nvidia.com/gpu.present": "true"},
                        node_taints=[
                            NodeTaint(
                                key="nvidia.com/dedicated",
                                value="gpu",
                                effect="NoSchedule",
                            )
                        ],
                        desired_node_count=2,
                        recycle_budget=1,
                        nico=NicoNodePoolProvider(
                            vpc_prefix_i_ds=["2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"],
                            instance_type_id="0d2f4a6c-8e0b-4d2f-9a4c-6e8b0d2f4a6c",
                            ssh_key_group_i_ds=["3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"],
                            release="example-ubuntu-24.04-amd64",
                        ),
                    )
                ],
                control_plane_config=CreateClusterControlPlaneConfig(
                    desired_count=3,
                    max_surge=1,
                    system_reserved_memory="16Gi",
                    nico=NicoControlPlaneProviderCreate(
                        instance_type_preference=[
                            "1c3e5a7f-9b1d-4f3e-a5c7-e9b1d3f5a7c9"
                        ],
                        vpc_prefix_i_ds=["2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"],
                        release="example-ubuntu-24.04-amd64",
                        ssh_key_group_i_ds=["3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"],
                    ),
                ),
                nico=NicoClusterProvider(
                    org_id="dipfedrcvjiw",
                    site_id="4f6a8c2e-1b3d-4e5f-a7b9-c1d3e5f7a9b1",
                    vpc_id="6a8c0e4f-3d5b-4f7a-b9c1-e3f5a7b9c1d3",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_cluster(
            name=name,
            control_plane_kubernetes_version=control_plane_kubernetes_version,
            etcd_encrypted=etcd_encrypted,
            control_plane_vip=control_plane_vip,
            network=network,
            node_pools=node_pools,
            control_plane_config=control_plane_config,
            nico=nico,
            launch_layer=launch_layer,
            request_options=request_options,
        )
        return _response.data

    async def get_cluster(self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Cluster:
        """
        Returns one cluster. Once provisioning finishes, `conditions.provisioning`
        is False and `conditions.provisioned` is True.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster
            The requested cluster

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clusters.get_cluster(
                cluster_id="clusterID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cluster(cluster_id, request_options=request_options)
        return _response.data

    async def delete_cluster(self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Starts deletion and sets `conditions.deleting` to `True`. A cluster can
        be deleted in any state, including while it is provisioning or
        upgrading. Deletion takes precedence over an in-progress or retained
        etcd encryption, etcd key rotation or certificate renewal.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

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
            await client.clusters.delete_cluster(
                cluster_id="clusterID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cluster(cluster_id, request_options=request_options)
        return _response.data

    async def update_cluster(
        self,
        cluster_id: str,
        *,
        enable_cp_node_recycling: typing.Optional[bool] = OMIT,
        control_plane_kubernetes_version: typing.Optional[str] = OMIT,
        enable_etcd_encryption: typing.Optional[bool] = OMIT,
        enable_oidc: typing.Optional[bool] = OMIT,
        control_plane_config: typing.Optional[UpdateClusterControlPlaneConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Cluster:
        """
        All fields are optional. See the API description for merge rules.

        Returns 400 for, among others: a Kubernetes downgrade, major-version
        change, or a jump of more than one minor version; an upgrade that would
        leave a worker pool more than 3 minor versions behind;
        `enableEtcdEncryption: false` or `enableOidc: false`; combining OIDC or
        etcd enablement with a version upgrade; etcd or OIDC enablement on a
        cluster that is not provisioned or is deleting; any `network` value;
        a control-plane `maxSurge` greater than 1.

        Returns 409 when another mutually exclusive cluster operation is in
        progress (`etcd_encryption`, `etcd_key_rotation`, `k8s_upgrade`,
        `cp_nodes_recycling`, `oidc_enable`, `certificate_renewal`), or the
        control plane is upgrading or recycling nodes. A failed certificate
        renewal can retain the lock until an operator clears it; see the
        retained-lock recovery procedure in
        controller/docs/certificate-renewal.md. A rotation that fails after
        `prepare` keeps the `etcd_key_rotation` lock until its workflow is
        reset and completes; see
        controller/docs/etcd-encryption-key-rotation.md#phase-aware-recovery.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        enable_cp_node_recycling : typing.Optional[bool]
            Turn automatic control-plane node replacement on or off.

        control_plane_kubernetes_version : typing.Optional[str]
            Target control-plane version, as X.Y.Z with no leading "v". Must be newer than
            the current version by at most one minor version and keep every worker pool
            within 3 minor versions.
            The cluster must have controlPlaneVIP configured unless the development-only
            allowControlPlaneWithoutVIP setting is enabled.

        enable_etcd_encryption : typing.Optional[bool]
            `true` starts one-way etcd encryption on a provisioned cluster. `false` is
            rejected. `true` on an already-encrypted cluster does nothing. Other updates
            return 409 while it runs.

        enable_oidc : typing.Optional[bool]
            `true` starts one-way OIDC authentication enablement. `false` is rejected.
            Cannot be combined with a control-plane upgrade or etcd enablement. Other
            updates return 409 while it runs.

        control_plane_config : typing.Optional[UpdateClusterControlPlaneConfig]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Cluster
            Update accepted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clusters.update_cluster(
                cluster_id="clusterID",
                enable_cp_node_recycling=True,
                control_plane_kubernetes_version="1.34.2",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cluster(
            cluster_id,
            enable_cp_node_recycling=enable_cp_node_recycling,
            control_plane_kubernetes_version=control_plane_kubernetes_version,
            enable_etcd_encryption=enable_etcd_encryption,
            enable_oidc=enable_oidc,
            control_plane_config=control_plane_config,
            request_options=request_options,
        )
        return _response.data

    async def get_cluster_spire_server(
        self, cluster_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ClusterSpireServerStatus:
        """
        Returns the SPIRE server last requested through
        `PATCH /clusters/{clusterID}/spire-server`, and for each node the
        server its SPIRE agent points at and whether the agent holds a valid
        X.509 SVID from it. Node status is read live from each node agent on
        every call; an unreachable node is reported with `reachable: false`.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ClusterSpireServerStatus
            Requested server and live per-node SPIRE agent status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.clusters.get_cluster_spire_server(
                cluster_id="clusterID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cluster_spire_server(cluster_id, request_options=request_options)
        return _response.data

    async def update_cluster_spire_server(
        self, cluster_id: str, *, address: str, port: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Starts a `spire_server_update` operation that points the SPIRE agent on
        every node of the cluster at the given server and waits for each agent
        to hold an SVID from it. Track it through `conditions.updateInProgress`
        and `conditions.updateFailed` on the cluster, and per node through
        `GET /clusters/{clusterID}/spire-server`. Repeating the request with
        the same server is safe, including while it is in progress.

        Parameters
        ----------
        cluster_id : str
            Cluster ID.

        address : str
            Host name or IP address of the SPIRE server.

        port : int
            SPIRE server port.

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
            await client.clusters.update_cluster_spire_server(
                cluster_id="clusterID",
                address="192.168.150.100",
                port=30440,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cluster_spire_server(
            cluster_id, address=address, port=port, request_options=request_options
        )
        return _response.data
