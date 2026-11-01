

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_control_plane_provider import LaunchLayerControlPlaneProvider
from .nico_control_plane_provider_create import NicoControlPlaneProviderCreate
from .node_agent_config import NodeAgentConfig


class CreateClusterControlPlaneConfig(UniversalBaseModel):
    """
    Writable cluster-level control plane configuration supplied at cluster creation.
    Required when you create a cluster.
    `nico` carries the NICo settings for the control-plane nodes; it is required
    for a NICo cluster. `launchLayer` is required for a LaunchLayer cluster.
    """

    desired_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="desiredCount"),
        pydantic.Field(
            alias="desiredCount",
            description="The desired number of cluster-level control plane nodes. Must be at least 1. Values above 1 require controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.",
        ),
    ]
    """
    The desired number of cluster-level control plane nodes. Must be at least 1. Values above 1 require controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.
    """

    max_surge: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxSurge"),
        pydantic.Field(alias="maxSurge", description="Extra control-plane nodes allowed during a rollout (0 or 1)."),
    ] = None
    """
    Extra control-plane nodes allowed during a rollout (0 or 1).
    """

    auto_scale_down_disabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="autoScaleDownDisabled"),
        pydantic.Field(
            alias="autoScaleDownDisabled",
            description="When true, automatic control-plane scale-down is disabled, so decreasing desiredCount leaves the surplus nodes in place. When scale-down is enabled it never reduces the control plane below the fault-tolerant floor of three nodes.",
        ),
    ] = None
    """
    When true, automatic control-plane scale-down is disabled, so decreasing desiredCount leaves the surplus nodes in place. When scale-down is enabled it never reduces the control plane below the fault-tolerant floor of three nodes.
    """

    provisioning_monitor_disabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="provisioningMonitorDisabled"),
        pydantic.Field(
            alias="provisioningMonitorDisabled",
            description="When true, nodes stuck in provisioning past the timeout are not replaced automatically.",
        ),
    ] = None
    """
    When true, nodes stuck in provisioning past the timeout are not replaced automatically.
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

    machine_annotations: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="machineAnnotations"),
        pydantic.Field(
            alias="machineAnnotations",
            description="Annotations applied to control-plane CAPI Machines at creation, including scale-out and replacement Machines. Fixed at cluster creation and not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.",
        ),
    ] = None
    """
    Annotations applied to control-plane CAPI Machines at creation, including scale-out and replacement Machines. Fixed at cluster creation and not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.
    """

    machine_labels: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="machineLabels"),
        pydantic.Field(
            alias="machineLabels",
            description="Labels applied to control-plane CAPI Machines at creation, including scale-out and replacement Machines. Fixed at cluster creation and not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.",
        ),
    ] = None
    """
    Labels applied to control-plane CAPI Machines at creation, including scale-out and replacement Machines. Fixed at cluster creation and not reconciled after provisioning. Keys under nke.nvidia.com, nke.io, nvke.nvidia.com, kubernetes.io, k8s.io, cluster.x-k8s.io and their subdomains require an explicit deployment allowlist entry for this metadata type.
    """

    node_labels: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="nodeLabels"),
        pydantic.Field(
            alias="nodeLabels",
            description="Labels applied to control-plane nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.",
        ),
    ] = None
    """
    Labels applied to control-plane nodes at creation, as a map of keys to values. Keys under nvke.nvidia.com, nke.nvidia.com (legacy), nke.io (legacy), kubernetes.io, k8s.io and their subdomains are reserved, unless the deployment allows specific Kubernetes keys.
    """

    nico: typing.Optional[NicoControlPlaneProviderCreate] = None
    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerControlPlaneProvider],
        FieldMetadata(alias="launchLayer"),
        pydantic.Field(alias="launchLayer"),
    ] = None
    node_agent_config: typing_extensions.Annotated[
        typing.Optional[NodeAgentConfig],
        FieldMetadata(alias="nodeAgentConfig"),
        pydantic.Field(alias="nodeAgentConfig"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
