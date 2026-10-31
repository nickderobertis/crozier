

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .launch_layer_node_set_provider import LaunchLayerNodeSetProvider
from .nico_node_set_provider import NicoNodeSetProvider


class NodeSet(UniversalBaseModel):
    """
    Read-only, immutable snapshot of a node pool's configuration at a point in time.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    NodeSet ID.
    """

    node_pool_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nodePoolID"),
        pydantic.Field(alias="nodePoolID", description="Owning node pool."),
    ] = None
    """
    Owning node pool.
    """

    desired_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="desiredCount"),
        pydantic.Field(alias="desiredCount", description="Number of nodes in the snapshot."),
    ] = None
    """
    Number of nodes in the snapshot.
    """

    kubernetes_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="kubernetesVersion"),
        pydantic.Field(alias="kubernetesVersion", description="Kubernetes version in the snapshot."),
    ] = None
    """
    Kubernetes version in the snapshot.
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

    nico: typing.Optional[NicoNodeSetProvider] = pydantic.Field(default=None)
    """
    NICo settings in the snapshot.
    """

    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerNodeSetProvider],
        FieldMetadata(alias="launchLayer"),
        pydantic.Field(alias="launchLayer", description="LaunchLayer settings in the snapshot."),
    ] = None
    """
    LaunchLayer settings in the snapshot.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
