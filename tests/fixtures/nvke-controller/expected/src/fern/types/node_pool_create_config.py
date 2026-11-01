

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_node_pool_provider import LaunchLayerNodePoolProvider
from .nico_node_pool_provider import NicoNodePoolProvider
from .node_name_prefix import NodeNamePrefix
from .node_taint import NodeTaint


class NodePoolCreateConfig(UniversalBaseModel):
    """
    A node pool and its provider settings. The provider follows the cluster's
    and is fixed at creation.
    """

    name: str = pydantic.Field()
    """
    Unique within the cluster. Immutable.
    """

    node_name_prefix: typing_extensions.Annotated[
        NodeNamePrefix, FieldMetadata(alias="nodeNamePrefix"), pydantic.Field(alias="nodeNamePrefix")
    ]
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
            alias="kubeReservedMemory", description="Memory reserved for Kubernetes components. Default 2Gi."
        ),
    ] = None
    """
    Memory reserved for Kubernetes components. Default 2Gi.
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
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="nodeLabels"),
        pydantic.Field(
            alias="nodeLabels",
            description="Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.",
        ),
    ] = None
    """
    Labels applied to the pool's nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.
    """

    node_taints: typing_extensions.Annotated[
        typing.Optional[typing.List[NodeTaint]],
        FieldMetadata(alias="nodeTaints"),
        pydantic.Field(
            alias="nodeTaints",
            description="Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.",
        ),
    ] = None
    """
    Taints applied to the pool's nodes at creation. Not allowed on control-plane pools. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved. Each key and effect pair may appear only once.
    """

    desired_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="desiredNodeCount"),
        pydantic.Field(
            alias="desiredNodeCount",
            description="The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.",
        ),
    ]
    """
    The desired number of nodes in the pool. For control-plane pools, aggregate capacity above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Free-text description.
    """

    auto_provision_disabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoProvisionDisabled"),
        pydantic.Field(alias="autoProvisionDisabled", description="Disables automatic provisioning for the pool."),
    ] = None
    """
    Disables automatic provisioning for the pool.
    """

    auto_mode_disabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoModeDisabled"),
        pydantic.Field(alias="autoModeDisabled", description="Disables auto-mode (automatic node recycling)."),
    ] = None
    """
    Disables auto-mode (automatic node recycling).
    """

    provisioning_monitor_disabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="provisioningMonitorDisabled"),
        pydantic.Field(
            alias="provisioningMonitorDisabled",
            description="When true, nodes stuck in provisioning past the timeout are not recycled automatically.",
        ),
    ] = None
    """
    When true, nodes stuck in provisioning past the timeout are not recycled automatically.
    """

    recycle_budget: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="recycleBudget"),
        pydantic.Field(alias="recycleBudget", description="Maximum number of nodes recycled at once."),
    ] = None
    """
    Maximum number of nodes recycled at once.
    """

    nico: typing.Optional[NicoNodePoolProvider] = None
    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerNodePoolProvider],
        FieldMetadata(alias="launchLayer"),
        pydantic.Field(alias="launchLayer"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
