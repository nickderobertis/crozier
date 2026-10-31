

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_node_pool_provider import LaunchLayerNodePoolProvider
from .nico_node_pool_provider import NicoNodePoolProvider
from .node_name_prefix import NodeNamePrefix
from .node_pool_conditions import NodePoolConditions
from .node_taint import NodeTaint


class NodePool(UniversalBaseModel):
    """
    A group of worker nodes sharing an instance type, release and Kubernetes version.
    """

    id: str = pydantic.Field()
    """
    Node pool ID.
    """

    cluster_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="clusterID"), pydantic.Field(alias="clusterID", description="Parent cluster.")
    ]
    """
    Parent cluster.
    """

    name: str = pydantic.Field()
    """
    Node pool name. Unique within the cluster. Immutable.
    """

    node_name_prefix: typing_extensions.Annotated[
        NodeNamePrefix,
        FieldMetadata(alias="nodeNamePrefix"),
        pydantic.Field(
            alias="nodeNamePrefix",
            description="Node names are `<cluster>-<prefix>-<NNNN>` (four-digit suffix), at most 63 characters in total.",
        ),
    ]
    """
    Node names are `<cluster>-<prefix>-<NNNN>` (four-digit suffix), at most 63 characters in total.
    """

    kubernetes_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="kubernetesVersion"),
        pydantic.Field(
            alias="kubernetesVersion",
            description="Desired Kubernetes version for the pool's nodes. Inherits the cluster's version on create.",
        ),
    ]
    """
    Desired Kubernetes version for the pool's nodes. Inherits the cluster's version on create.
    """

    system_reserved_memory: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="systemReservedMemory"),
        pydantic.Field(
            alias="systemReservedMemory",
            description="Memory reserved for system daemons. Nodes reserve 16Gi when omitted.",
        ),
    ] = None
    """
    Memory reserved for system daemons. Nodes reserve 16Gi when omitted.
    """

    kube_reserved_memory: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="kubeReservedMemory"),
        pydantic.Field(
            alias="kubeReservedMemory",
            description="Memory reserved for Kubernetes components. Empty when the 2Gi default applies.",
        ),
    ] = None
    """
    Memory reserved for Kubernetes components. Empty when the 2Gi default applies.
    """

    machine_annotations: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="machineAnnotations"),
        pydantic.Field(
            alias="machineAnnotations",
            description="Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.",
        ),
    ] = None
    """
    Annotations set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.
    """

    machine_labels: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="machineLabels"),
        pydantic.Field(
            alias="machineLabels",
            description="Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.",
        ),
    ] = None
    """
    Labels set on CAPI Machines only when they are created, including Machines created during scale-out or replacement. Fixed at node-pool creation. Not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.
    """

    node_labels: typing_extensions.Annotated[
        typing.Dict[str, str],
        FieldMetadata(alias="nodeLabels"),
        pydantic.Field(
            alias="nodeLabels",
            description="Labels applied to the pool's nodes, as a map of keys to values. Set at creation.",
        ),
    ]
    """
    Labels applied to the pool's nodes, as a map of keys to values. Set at creation.
    """

    node_taints: typing_extensions.Annotated[
        typing.List[NodeTaint],
        FieldMetadata(alias="nodeTaints"),
        pydantic.Field(alias="nodeTaints", description="Taints applied to the pool's nodes. Set at creation."),
    ]
    """
    Taints applied to the pool's nodes. Set at creation.
    """

    conditions: NodePoolConditions = pydantic.Field()
    """
    Lifecycle conditions: provisioning, provisioned, deleting.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free-text description.
    """

    desired_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="desiredNodeCount"),
        pydantic.Field(alias="desiredNodeCount", description="Number of nodes."),
    ]
    """
    Number of nodes.
    """

    auto_provision_disabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="autoProvisionDisabled"),
        pydantic.Field(alias="autoProvisionDisabled", description="Disables automatic provisioning for the pool."),
    ]
    """
    Disables automatic provisioning for the pool.
    """

    current_node_set_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="currentNodeSetID"),
        pydantic.Field(alias="currentNodeSetID", description="The active NodeSet."),
    ] = None
    """
    The active NodeSet.
    """

    auto_mode_disabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="autoModeDisabled"),
        pydantic.Field(alias="autoModeDisabled", description="Disables auto-mode (automatic node recycling)."),
    ]
    """
    Disables auto-mode (automatic node recycling).
    """

    provisioning_monitor_disabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="provisioningMonitorDisabled"),
        pydantic.Field(
            alias="provisioningMonitorDisabled",
            description="When true, nodes stuck in provisioning past the timeout are not recycled automatically.",
        ),
    ]
    """
    When true, nodes stuck in provisioning past the timeout are not recycled automatically.
    """

    recycle_budget: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="recycleBudget"),
        pydantic.Field(alias="recycleBudget", description="Maximum number of nodes recycled at once."),
    ]
    """
    Maximum number of nodes recycled at once.
    """

    max_surge: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxSurge"),
        pydantic.Field(
            alias="maxSurge",
            description="Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each\nnode is torn down before its replacement is provisioned.",
        ),
    ] = None
    """
    Nodes allowed above desiredNodeCount during a rollout. 0 means sequential: each
    node is torn down before its replacement is provisioned.
    """

    nico: typing.Optional[NicoNodePoolProvider] = pydantic.Field(default=None)
    """
    NICo settings for the pool.
    """

    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerNodePoolProvider],
        FieldMetadata(alias="launchLayer"),
        pydantic.Field(alias="launchLayer", description="LaunchLayer settings for the pool."),
    ] = None
    """
    LaunchLayer settings for the pool.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
