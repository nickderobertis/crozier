

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_control_plane_provider_update import LaunchLayerControlPlaneProviderUpdate
from .nico_control_plane_provider_update import NicoControlPlaneProviderUpdate
from .node_agent_config import NodeAgentConfig


class UpdateClusterControlPlaneConfig(UniversalBaseModel):
    """
    Changes to `release` or the Kubernetes version start a control-plane
    rollout. All fields are optional. A provider payload that does not match the
    cluster's provider is rejected with 400.
    Rollout-triggering changes require controlPlaneVIP unless the development-only
    allowControlPlaneWithoutVIP setting is enabled. maxSurge alone does not
    trigger a rollout and remains mutable without a VIP.
    """

    desired_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="desiredCount"),
        pydantic.Field(
            alias="desiredCount",
            description="The desired number of cluster-level control plane nodes. Must be at least 1.\nIncreasing the count above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.",
        ),
    ] = None
    """
    The desired number of cluster-level control plane nodes. Must be at least 1.
    Increasing the count above 1 requires controlPlaneVIP on the cluster unless the development-only allowControlPlaneWithoutVIP setting is enabled.
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
        pydantic.Field(alias="systemReservedMemory", description="Memory reserved for system daemons."),
    ] = None
    """
    Memory reserved for system daemons.
    """

    nico: typing.Optional[NicoControlPlaneProviderUpdate] = None
    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerControlPlaneProviderUpdate],
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
