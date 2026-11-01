

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition import Condition


class NodeConditions(UniversalBaseModel):
    """
    Each is a Condition. A node normally moves through pending, provisioningClaimed,
    provisioning, readyToJoin, joined and provisioned; deletion moves through
    deleteRequested (control-plane nodes) and deleting.
    """

    pending: Condition = pydantic.Field()
    """
    The node is waiting to be provisioned.
    """

    provisioning_claimed: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="provisioningClaimed"),
        pydantic.Field(alias="provisioningClaimed", description="A provisioning operation has claimed the node."),
    ]
    """
    A provisioning operation has claimed the node.
    """

    provisioning: Condition = pydantic.Field()
    """
    The node is provisioning.
    """

    ready_to_join: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="readyToJoin"),
        pydantic.Field(alias="readyToJoin", description="The node is ready to join the cluster."),
    ]
    """
    The node is ready to join the cluster.
    """

    joined: Condition = pydantic.Field()
    """
    The node has joined the cluster.
    """

    provisioned: Condition = pydantic.Field()
    """
    The node is provisioned.
    """

    deleting: Condition = pydantic.Field()
    """
    The node is being deleted.
    """

    kubernetes_ready: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="kubernetesReady"),
        pydantic.Field(alias="kubernetesReady", description="The kubelet reports Ready."),
    ]
    """
    The kubelet reports Ready.
    """

    kubernetes_unschedulable: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="kubernetesUnschedulable"),
        pydantic.Field(
            alias="kubernetesUnschedulable",
            description="Reflects the Kubernetes node's unschedulable (cordoned) state.",
        ),
    ]
    """
    Reflects the Kubernetes node's unschedulable (cordoned) state.
    """

    node_agent_ready: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="nodeAgentReady"),
        pydantic.Field(alias="nodeAgentReady", description="The NVKE node agent is healthy."),
    ]
    """
    The NVKE node agent is healthy.
    """

    rebooting: Condition = pydantic.Field()
    """
    The node is rebooting.
    """

    marked_for_recycling: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="markedForRecycling"),
        pydantic.Field(alias="markedForRecycling", description="The node is marked for replacement."),
    ]
    """
    The node is marked for replacement.
    """

    marked_for_repair: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="markedForRepair"),
        pydantic.Field(alias="markedForRepair", description="The node is marked for repair."),
    ]
    """
    The node is marked for repair.
    """

    control_plane_rollout_required: typing_extensions.Annotated[
        typing.Optional[Condition],
        FieldMetadata(alias="controlPlaneRolloutRequired"),
        pydantic.Field(
            alias="controlPlaneRolloutRequired",
            description="Control-plane nodes only. True when the node differs from the desired configuration.",
        ),
    ] = None
    """
    Control-plane nodes only. True when the node differs from the desired configuration.
    """

    delete_requested: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="deleteRequested"),
        pydantic.Field(
            alias="deleteRequested",
            description="A delete has been accepted but teardown has not started. Control-plane deletes\nare recorded here first and started one at a time; `deleting` then reports the\nteardown. At most one of deleting and deleteRequested is True.",
        ),
    ]
    """
    A delete has been accepted but teardown has not started. Control-plane deletes
    are recorded here first and started one at a time; `deleting` then reports the
    teardown. At most one of deleting and deleteRequested is True.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
