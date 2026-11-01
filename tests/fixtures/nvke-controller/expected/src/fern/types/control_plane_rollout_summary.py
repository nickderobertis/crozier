

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ControlPlaneRolloutSummary(UniversalBaseModel):
    """
    Rollout progress of the control plane. The three node counts are mutually
    exclusive and sum to managedNodeCount.
    """

    managed_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="managedNodeCount"),
        pydantic.Field(alias="managedNodeCount", description="Control-plane nodes under management."),
    ]
    """
    Control-plane nodes under management.
    """

    up_to_date_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="upToDateNodeCount"),
        pydantic.Field(alias="upToDateNodeCount", description="Nodes on the desired configuration."),
    ]
    """
    Nodes on the desired configuration.
    """

    pending_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pendingNodeCount"),
        pydantic.Field(alias="pendingNodeCount", description="Nodes waiting to be replaced."),
    ]
    """
    Nodes waiting to be replaced.
    """

    in_progress_node_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="inProgressNodeCount"),
        pydantic.Field(
            alias="inProgressNodeCount", description="Nodes being replaced. The three counts sum to managedNodeCount."
        ),
    ]
    """
    Nodes being replaced. The three counts sum to managedNodeCount.
    """

    in_progress: typing_extensions.Annotated[
        bool, FieldMetadata(alias="inProgress"), pydantic.Field(alias="inProgress", description="A rollout is running.")
    ]
    """
    A rollout is running.
    """

    recycling_enabled: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="recyclingEnabled"),
        pydantic.Field(
            alias="recyclingEnabled", description="When false, pending nodes are detected but wait for an operator."
        ),
    ]
    """
    When false, pending nodes are detected but wait for an operator.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
