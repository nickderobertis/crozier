

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .cluster_conditions import ClusterConditions
from .cluster_network import ClusterNetwork
from .control_plane_config import ControlPlaneConfig
from .launch_layer_cluster_provider import LaunchLayerClusterProvider
from .nico_cluster_provider import NicoClusterProvider
from .node_agent_upgrade_status import NodeAgentUpgradeStatus


class Cluster(UniversalBaseModel):
    """
    A Kubernetes cluster. Holds the Kubernetes version, network, CNI, etcd
    encryption, control-plane configuration and conditions.
    """

    id: str = pydantic.Field()
    """
    Cluster ID.
    """

    name: str = pydantic.Field()
    """
    Cluster name.
    """

    control_plane_kubernetes_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="controlPlaneKubernetesVersion"),
        pydantic.Field(
            alias="controlPlaneKubernetesVersion",
            description="Desired control-plane Kubernetes version. The running version is in ControlPlaneStatus.",
        ),
    ]
    """
    Desired control-plane Kubernetes version. The running version is in ControlPlaneStatus.
    """

    cni_plugin: typing_extensions.Annotated[
        str, FieldMetadata(alias="cniPlugin"), pydantic.Field(alias="cniPlugin", description="CNI plugin.")
    ]
    """
    CNI plugin.
    """

    cni_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="cniVersion"), pydantic.Field(alias="cniVersion", description="CNI version.")
    ]
    """
    CNI version.
    """

    etcd_encrypted: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="etcdEncrypted"),
        pydantic.Field(alias="etcdEncrypted", description="Whether etcd is encrypted at rest."),
    ]
    """
    Whether etcd is encrypted at rest.
    """

    control_plane_vip: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="controlPlaneVIP"),
        pydantic.Field(alias="controlPlaneVIP", description="API server VIP, if configured."),
    ] = None
    """
    API server VIP, if configured.
    """

    enable_cp_node_recycling: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="enableCPNodeRecycling"),
        pydantic.Field(
            alias="enableCPNodeRecycling",
            description="When true, control-plane upgrades and configuration changes replace nodes\nautomatically. When false, nodes needing replacement are reported as pending and\nwait for an operator.",
        ),
    ] = None
    """
    When true, control-plane upgrades and configuration changes replace nodes
    automatically. When false, nodes needing replacement are reported as pending and
    wait for an operator.
    """

    control_plane_config: typing_extensions.Annotated[
        typing.Optional[ControlPlaneConfig],
        FieldMetadata(alias="controlPlaneConfig"),
        pydantic.Field(alias="controlPlaneConfig", description="Current control-plane configuration."),
    ] = None
    """
    Current control-plane configuration.
    """

    network: ClusterNetwork = pydantic.Field()
    """
    Pod and service network.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt", description="Creation time.")
    ]
    """
    Creation time.
    """

    next_cert_renewal_due: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="nextCertRenewalDue"),
        pydantic.Field(
            alias="nextCertRenewalDue",
            description="The next scheduled certificate-renewal time. A value in the past is\noverdue unless a certificate-renewal operation is currently accepted.\nUnset until the controller first sees the cluster, which schedules\nthe first check one renewal interval later.",
        ),
    ] = None
    """
    The next scheduled certificate-renewal time. A value in the past is
    overdue unless a certificate-renewal operation is currently accepted.
    Unset until the controller first sees the cluster, which schedules
    the first check one renewal interval later.
    """

    conditions: ClusterConditions = pydantic.Field()
    """
    Lifecycle conditions.
    """

    nico: typing.Optional[NicoClusterProvider] = pydantic.Field(default=None)
    """
    NICo identifiers.
    """

    launch_layer: typing_extensions.Annotated[
        typing.Optional[LaunchLayerClusterProvider],
        FieldMetadata(alias="launchLayer"),
        pydantic.Field(alias="launchLayer", description="LaunchLayer identifiers."),
    ] = None
    """
    LaunchLayer identifiers.
    """

    node_agent_upgrade: typing_extensions.Annotated[
        typing.Optional[NodeAgentUpgradeStatus],
        FieldMetadata(alias="nodeAgentUpgrade"),
        pydantic.Field(alias="nodeAgentUpgrade"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
