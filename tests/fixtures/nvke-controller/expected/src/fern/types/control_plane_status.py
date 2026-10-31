

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .condition import Condition
from .control_plane_rollout_summary import ControlPlaneRolloutSummary


class ControlPlaneStatus(UniversalBaseModel):
    """
    Aggregate runtime status of a cluster's control plane.
    """

    node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="nodeCount"),
        pydantic.Field(alias="nodeCount", description="Total control-plane nodes, including surge nodes."),
    ]
    """
    Total control-plane nodes, including surge nodes.
    """

    ready_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="readyNodeCount"),
        pydantic.Field(alias="readyNodeCount", description="Control-plane nodes reporting Kubernetes Ready."),
    ]
    """
    Control-plane nodes reporting Kubernetes Ready.
    """

    kubernetes_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="kubernetesVersion"),
        pydantic.Field(alias="kubernetesVersion", description="Current running control-plane Kubernetes version."),
    ]
    """
    Current running control-plane Kubernetes version.
    """

    control_plane_upgrading: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="controlPlaneUpgrading"),
        pydantic.Field(alias="controlPlaneUpgrading", description="The control plane is being upgraded."),
    ]
    """
    The control plane is being upgraded.
    """

    cp_nodes_recycling: typing_extensions.Annotated[
        Condition,
        FieldMetadata(alias="cpNodesRecycling"),
        pydantic.Field(alias="cpNodesRecycling", description="Control-plane nodes are being replaced."),
    ]
    """
    Control-plane nodes are being replaced.
    """

    rollout: typing.Optional[ControlPlaneRolloutSummary] = pydantic.Field(default=None)
    """
    Rollout progress.
    """

    deleting_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="deletingNodeCount"),
        pydantic.Field(
            alias="deletingNodeCount",
            description="Control-plane nodes being torn down. Deletes are serialized, so this is at most 1.",
        ),
    ]
    """
    Control-plane nodes being torn down. Deletes are serialized, so this is at most 1.
    """

    delete_requested_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="deleteRequestedNodeCount"),
        pydantic.Field(
            alias="deleteRequestedNodeCount",
            description="Control-plane nodes with an accepted delete that has not started.",
        ),
    ]
    """
    Control-plane nodes with an accepted delete that has not started.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
