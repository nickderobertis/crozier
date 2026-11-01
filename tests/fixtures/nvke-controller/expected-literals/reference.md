# Reference
## Clusters
<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">list_clusters</a>(...) -> ListClustersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all clusters, or the cluster whose name matches `name`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.clusters.list_clusters()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter clusters by name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">create_cluster</a>(...) -> Cluster</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a cluster and starts provisioning. The cluster is returned before
provisioning completes.

Returns 400 for, among others: a duplicate cluster name; missing
`nico.orgID`, `siteID` or `vpcID`; an unsupported `cniPlugin`; a
missing `controlPlaneConfig.nico.release`; a
control-plane `maxSurge` greater than 1; a pod CIDR too small for the
requested nodes plus surge; a `controlPlaneVIP` inside the pod or
service CIDR.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, ClusterNetworkCreateConfig, NodePoolCreateConfig, NodeTaint, NicoNodePoolProvider, CreateClusterControlPlaneConfig, NicoControlPlaneProviderCreate, NicoClusterProvider
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
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
            node_labels={
                "nvidia.com/gpu.present": "true"
            },
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
                vpc_prefix_i_ds=[
                    "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
                ],
                instance_type_id="0d2f4a6c-8e0b-4d2f-9a4c-6e8b0d2f4a6c",
                ssh_key_group_i_ds=[
                    "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
                ],
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
            vpc_prefix_i_ds=[
                "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
            ],
            release="example-ubuntu-24.04-amd64",
            ssh_key_group_i_ds=[
                "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
            ],
        ),
    ),
    nico=NicoClusterProvider(
        org_id="dipfedrcvjiw",
        site_id="4f6a8c2e-1b3d-4e5f-a7b9-c1d3e5f7a9b1",
        vpc_id="6a8c0e4f-3d5b-4f7a-b9c1-e3f5a7b9c1d3",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Cluster name. Lowercase DNS label, unique per management plane. Node names are derived from it.
    
</dd>
</dl>

<dl>
<dd>

**control_plane_kubernetes_version:** `str` — Kubernetes version for the cluster, as X.Y.Z with no leading "v".
    
</dd>
</dl>

<dl>
<dd>

**etcd_encrypted:** `bool` — Encrypt etcd at rest. Can be turned on later with `enableEtcdEncryption`; cannot be turned off.
    
</dd>
</dl>

<dl>
<dd>

**control_plane_vip:** `typing.Optional[str]` 

Virtual IP for the API server through kube-vip. Omit to skip kube-vip and
use the first control-plane node's IP as the API server endpoint. Must not
fall inside the pod or service CIDR. An explicit empty string is rejected.
By default, a cluster without a VIP must have exactly one desired
control-plane node. Scale-up above one node, upgrades and node replacement
require a VIP unless the controller deployment enables the development-only
allowControlPlaneWithoutVIP setting. That override keeps the initializing
node's IP as the endpoint; replacing that node can break API access.
Quorum, health and deletion protections still apply.
    
</dd>
</dl>

<dl>
<dd>

**network:** `typing.Optional[ClusterNetworkCreateConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**node_pools:** `typing.Optional[typing.List[NodePoolCreateConfig]]` — Initial worker node pools.
    
</dd>
</dl>

<dl>
<dd>

**control_plane_config:** `typing.Optional[CreateClusterControlPlaneConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**nico:** `typing.Optional[NicoClusterProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**launch_layer:** `typing.Optional[LaunchLayerClusterProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">get_cluster</a>(...) -> Cluster</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one cluster. Once provisioning finishes, `conditions.provisioning`
is False and `conditions.provisioned` is True.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.clusters.get_cluster(
    cluster_id="clusterID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">delete_cluster</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts deletion and sets `conditions.deleting` to `True`. A cluster can
be deleted in any state, including while it is provisioning or
upgrading. Deletion takes precedence over an in-progress or retained
etcd encryption, etcd key rotation or certificate renewal.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.clusters.delete_cluster(
    cluster_id="clusterID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">update_cluster</a>(...) -> Cluster</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.clusters.update_cluster(
    cluster_id="clusterID",
    enable_cp_node_recycling=True,
    control_plane_kubernetes_version="1.34.2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**enable_cp_node_recycling:** `typing.Optional[bool]` — Turn automatic control-plane node replacement on or off.
    
</dd>
</dl>

<dl>
<dd>

**control_plane_kubernetes_version:** `typing.Optional[str]` 

Target control-plane version, as X.Y.Z with no leading "v". Must be newer than
the current version by at most one minor version and keep every worker pool
within 3 minor versions.
The cluster must have controlPlaneVIP configured unless the development-only
allowControlPlaneWithoutVIP setting is enabled.
    
</dd>
</dl>

<dl>
<dd>

**enable_etcd_encryption:** `typing.Optional[bool]` 

`true` starts one-way etcd encryption on a provisioned cluster. `false` is
rejected. `true` on an already-encrypted cluster does nothing. Other updates
return 409 while it runs.
    
</dd>
</dl>

<dl>
<dd>

**enable_oidc:** `typing.Optional[bool]` 

`true` starts one-way OIDC authentication enablement. `false` is rejected.
Cannot be combined with a control-plane upgrade or etcd enablement. Other
updates return 409 while it runs.
    
</dd>
</dl>

<dl>
<dd>

**control_plane_config:** `typing.Optional[UpdateClusterControlPlaneConfig]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">get_cluster_spire_server</a>(...) -> ClusterSpireServerStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the SPIRE server last requested through
`PATCH /clusters/{clusterID}/spire-server`, and for each node the
server its SPIRE agent points at and whether the agent holds a valid
X.509 SVID from it. Node status is read live from each node agent on
every call; an unreachable node is reported with `reachable: false`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.clusters.get_cluster_spire_server(
    cluster_id="clusterID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.clusters.<a href="src/fern/clusters/client.py">update_cluster_spire_server</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts a `spire_server_update` operation that points the SPIRE agent on
every node of the cluster at the given server and waits for each agent
to hold an SVID from it. Track it through `conditions.updateInProgress`
and `conditions.updateFailed` on the cluster, and per node through
`GET /clusters/{clusterID}/spire-server`. Repeating the request with
the same server is safe, including while it is in progress.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.clusters.update_cluster_spire_server(
    cluster_id="clusterID",
    address="192.168.150.100",
    port=30440,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**request:** `SpireServer` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Control plane
<details><summary><code>client.control_plane.<a href="src/fern/control_plane/client.py">get_cluster_control_plane</a>(...) -> ClusterControlPlane</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Read-only view of the control plane: the persisted configuration plus
aggregate runtime status (node counts, current Kubernetes version,
rollout progress, and upgrade and recycling conditions). Change the
control plane through `PATCH /clusters/{clusterID}`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.control_plane.get_cluster_control_plane(
    cluster_id="clusterID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.control_plane.<a href="src/fern/control_plane/client.py">get_cluster_control_plane_config_history</a>(...) -> ControlPlaneConfigHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the control-plane configuration change history, oldest first.
Each entry shows which rollout-relevant fields changed relative to the
previous snapshot. Use it to resolve the `pinnedConfigurationID` on each
control-plane node and the cluster's desired `configurationId`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.control_plane.get_cluster_control_plane_config_history(
    cluster_id="clusterID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `str` — Cluster ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Node pools
<details><summary><code>client.node_pools.<a href="src/fern/node_pools/client.py">list_node_pools</a>(...) -> ListNodePoolsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all node pools, filtered by the query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_pools.list_node_pools()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Filter by cluster ID
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `typing.Optional[str]` — Filter by cluster name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by node pool name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.node_pools.<a href="src/fern/node_pools/client.py">create_node_pool</a>(...) -> NodePool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a worker node pool and starts provisioning. The pool takes the
cluster's Kubernetes version.

Returns 400 for, among others: parent cluster not found; a duplicate
pool name in the cluster; missing `nico.instanceTypeID`
or `nico.release`; not exactly one of
`subnetIDs` and `vpcPrefixIDs`; a pod CIDR too small for the requested
nodes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, NodeTaint, NicoNodePoolProvider
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_pools.create_node_pool(
    name="gpu-workers-b300",
    node_name_prefix="wb",
    system_reserved_memory="32Gi",
    kube_reserved_memory="4Gi",
    node_labels={
        "nvidia.com/gpu.product": "B300"
    },
    node_taints=[
        NodeTaint(
            key="nvidia.com/dedicated",
            value="team-b",
            effect="NoSchedule",
        )
    ],
    desired_node_count=4,
    description="Reserved for team-b training jobs",
    recycle_budget=1,
    nico=NicoNodePoolProvider(
        vpc_prefix_i_ds=[
            "2d4f6b8a-0c2e-4a4f-b6d8-f0c2e4a6b8d0"
        ],
        instance_type_id="9e8d7c6b-5a4f-4e3d-8c2b-1a0f9e8d7c6b",
        ssh_key_group_i_ds=[
            "3e5a7c9b-1d3f-4b5a-c7e9-a1d3f5b7c9e1"
        ],
        release="example-ubuntu-24.04-amd64",
        disk_selection_strategy="largest",
    ),
    cluster_id="9b1d4e2a-3c5f-4a7b-8e9d-0f1a2b3c4d5e",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Unique within the cluster. Immutable.
    
</dd>
</dl>

<dl>
<dd>

**node_name_prefix:** `NodeNamePrefix` 
    
</dd>
</dl>

<dl>
<dd>

**desired_node_count:** `int` — The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.
    
</dd>
</dl>

<dl>
<dd>

**cluster_id:** `str` — Parent cluster.
    
</dd>
</dl>

<dl>
<dd>

**system_reserved_memory:** `typing.Optional[str]` — Memory reserved for system daemons. Nodes reserve 16Gi when omitted.
    
</dd>
</dl>

<dl>
<dd>

**kube_reserved_memory:** `typing.Optional[str]` — Memory reserved for Kubernetes components. Default 2Gi.
    
</dd>
</dl>

<dl>
<dd>

**machine_annotations:** `typing.Optional[typing.Dict[str, str]]` — Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.
    
</dd>
</dl>

<dl>
<dd>

**machine_labels:** `typing.Optional[typing.Dict[str, str]]` — Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.
    
</dd>
</dl>

<dl>
<dd>

**node_labels:** `typing.Optional[typing.Dict[str, str]]` — Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.
    
</dd>
</dl>

<dl>
<dd>

**node_taints:** `typing.Optional[typing.List[NodeTaint]]` — Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Free-text description.
    
</dd>
</dl>

<dl>
<dd>

**auto_provision_disabled:** `typing.Optional[bool]` — Disables automatic provisioning for the pool.
    
</dd>
</dl>

<dl>
<dd>

**auto_mode_disabled:** `typing.Optional[bool]` — Disables auto-mode (automatic node recycling).
    
</dd>
</dl>

<dl>
<dd>

**provisioning_monitor_disabled:** `typing.Optional[bool]` — When true, nodes stuck in provisioning past the timeout are not recycled automatically.
    
</dd>
</dl>

<dl>
<dd>

**recycle_budget:** `typing.Optional[int]` — Maximum number of nodes recycled at once.
    
</dd>
</dl>

<dl>
<dd>

**nico:** `typing.Optional[NicoNodePoolProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**launch_layer:** `typing.Optional[LaunchLayerNodePoolProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.node_pools.<a href="src/fern/node_pools/client.py">get_node_pool</a>(...) -> NodePool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one node pool.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_pools.get_node_pool(
    node_pool_id="nodePoolID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_pool_id:** `str` — Node pool ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.node_pools.<a href="src/fern/node_pools/client.py">delete_node_pool</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_pools.delete_node_pool(
    node_pool_id="nodePoolID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_pool_id:** `str` — Node pool ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.node_pools.<a href="src/fern/node_pools/client.py">update_node_pool</a>(...) -> NodePool</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

All fields are optional. Changes to the Kubernetes version, release
or other node configuration create a new NodeSet and roll the pool's
nodes to it.

Returns 400 for, among others: sending a field that is fixed at
creation (for example `instanceTypeID`); `nico.release: ""`; any update
to a control-plane node pool, which is configured through the cluster's
`controlPlaneConfig` instead. That last refusal does not depend on the
control-plane mutation lock, so retrying later does not help.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_pools.update_node_pool(
    node_pool_id="nodePoolID",
    desired_node_count=6,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_pool_id:** `str` — Node pool ID.
    
</dd>
</dl>

<dl>
<dd>

**auto_provision_disabled:** `typing.Optional[bool]` — Disables automatic provisioning for the pool.
    
</dd>
</dl>

<dl>
<dd>

**auto_mode_disabled:** `typing.Optional[bool]` — Disables auto-mode (automatic node recycling).
    
</dd>
</dl>

<dl>
<dd>

**provisioning_monitor_disabled:** `typing.Optional[bool]` — When true, nodes stuck in provisioning past the timeout are not recycled automatically.
    
</dd>
</dl>

<dl>
<dd>

**system_reserved_memory:** `typing.Optional[str]` — Memory reserved for system daemons. Nodes reserve 16Gi when omitted.
    
</dd>
</dl>

<dl>
<dd>

**kube_reserved_memory:** `typing.Optional[str]` — Memory reserved for Kubernetes components. An empty string restores the 2Gi default.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Free-text description.
    
</dd>
</dl>

<dl>
<dd>

**desired_node_count:** `typing.Optional[int]` — The desired number of nodes in the pool. Increasing aggregate control-plane capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.
    
</dd>
</dl>

<dl>
<dd>

**recycle_budget:** `typing.Optional[int]` — Maximum number of nodes recycled at once.
    
</dd>
</dl>

<dl>
<dd>

**max_surge:** `typing.Optional[int]` 

Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each
node is torn down before its replacement is provisioned.
    
</dd>
</dl>

<dl>
<dd>

**kubernetes_version:** `typing.Optional[str]` 

Desired Kubernetes version for the pool's nodes, as X.Y.Z with no leading "v".
Must be newer than the current version.
    
</dd>
</dl>

<dl>
<dd>

**nico:** `typing.Optional[NicoNodePoolProviderUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**launch_layer:** `typing.Optional[LaunchLayerNodePoolProviderUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Node sets
<details><summary><code>client.node_sets.<a href="src/fern/node_sets/client.py">list_node_sets</a>(...) -> ListNodeSetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all node sets, or those of one node pool.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_sets.list_node_sets()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_pool_id:** `typing.Optional[str]` — Filter by node pool ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.node_sets.<a href="src/fern/node_sets/client.py">get_node_set</a>(...) -> NodeSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one node set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.node_sets.get_node_set(
    node_set_id="nodeSetID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_set_id:** `str` — Node set ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Nodes
<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">list_nodes</a>(...) -> ListNodesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all nodes, filtered by the query parameters. All filters are exact match.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.nodes.list_nodes()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cluster_id:** `typing.Optional[str]` — Filter by cluster ID
    
</dd>
</dl>

<dl>
<dd>

**node_pool_id:** `typing.Optional[str]` — Filter by node pool ID
    
</dd>
</dl>

<dl>
<dd>

**cluster_name:** `typing.Optional[str]` — Filter by cluster name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter by node name (exact match)
    
</dd>
</dl>

<dl>
<dd>

**control_plane:** `typing.Optional[bool]` — `true` returns only control-plane nodes; `false` only workers
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">get_node</a>(...) -> Node</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one node. Control-plane nodes do not belong to a node pool, so
their `nodePoolID` and `nodeSetID` are the nil UUID. `nico` is omitted
when none of its fields are set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
)

client.nodes.get_node(
    node_id="nodeID",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — Node ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.nodes.<a href="src/fern/nodes/client.py">delete_node</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, MachineHealthIssue
from fern.environment import FernApiEnvironment

client = FernApi(
    token="<token>",
    environment=FernApiEnvironment.MANAGEMENT_PLANE,
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

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**node_id:** `str` — Node ID.
    
</dd>
</dl>

<dl>
<dd>

**machine_health_issue:** `typing.Optional[MachineHealthIssue]` 
    
</dd>
</dl>

<dl>
<dd>

**force_unreachable:** `typing.Optional[bool]` 

Treat the node as unreachable: graceful drain and shutdown are attempted, and
failures are tolerated. Failures removing a control-plane node's etcd member are
not tolerated.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

