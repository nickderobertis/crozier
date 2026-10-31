

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .control_plane_rollout_status import ControlPlaneRolloutStatus
from .launch_layer_node_provider import LaunchLayerNodeProvider
from .nico_node_provider import NicoNodeProvider
from .node_conditions import NodeConditions


class Node(UniversalBaseModel):
    """
    A single machine in a cluster, with lifecycle and health conditions.
    """

    id: str = pydantic.Field()
    """
    Node ID.
    """

    node_pool_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nodePoolID"),
        pydantic.Field(alias="nodePoolID", description="Owning node pool. The nil UUID for control-plane nodes."),
    ]
    """
    Owning node pool. The nil UUID for control-plane nodes.
    """

    node_set_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nodeSetID"),
        pydantic.Field(alias="nodeSetID", description="Owning NodeSet. The nil UUID for control-plane nodes."),
    ]
    """
    Owning NodeSet. The nil UUID for control-plane nodes.
    """

    name: str = pydantic.Field()
    """
    Node name.
    """

    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Node IP address.
    """

    nico: typing.Optional[NicoNodeProvider] = pydantic.Field(default=None)
    """
    NICo instanceID, machineID and instanceTypeID. Omitted when none are set.
    """

    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerNodeProvider],
        FieldMetadata(alias="launchLayer"),
        pydantic.Field(
            alias="launchLayer", description="LaunchLayer instanceID, machineID and rackID. Omitted when none are set."
        ),
    ] = None
    """
    LaunchLayer instanceID, machineID and rackID. Omitted when none are set.
    """

    control_plane: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="controlPlane"),
        pydantic.Field(alias="controlPlane", description="Whether the node is a control-plane node."),
    ]
    """
    Whether the node is a control-plane node.
    """

    conditions: NodeConditions = pydantic.Field()
    """
    Lifecycle and health conditions.
    """

    control_plane_rollout: typing_extensions.Annotated[
        typing.Optional[ControlPlaneRolloutStatus],
        FieldMetadata(alias="controlPlaneRollout"),
        pydantic.Field(alias="controlPlaneRollout", description="Control-plane nodes only."),
    ] = None
    """
    Control-plane nodes only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
