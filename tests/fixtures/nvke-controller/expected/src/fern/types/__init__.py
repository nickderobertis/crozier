



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .certificate_renewal_status import CertificateRenewalStatus
    from .certificate_renewal_status_outcome import CertificateRenewalStatusOutcome
    from .certificate_renewal_status_state import CertificateRenewalStatusState
    from .cluster import Cluster
    from .cluster_conditions import ClusterConditions
    from .cluster_control_plane import ClusterControlPlane
    from .cluster_network import ClusterNetwork
    from .cluster_network_create_config import ClusterNetworkCreateConfig
    from .cluster_spire_server_status import ClusterSpireServerStatus
    from .condition import Condition
    from .condition_status import ConditionStatus
    from .control_plane_config import ControlPlaneConfig
    from .control_plane_config_change import ControlPlaneConfigChange
    from .control_plane_config_field import ControlPlaneConfigField
    from .control_plane_config_history import ControlPlaneConfigHistory
    from .control_plane_rollout_change import ControlPlaneRolloutChange
    from .control_plane_rollout_status import ControlPlaneRolloutStatus
    from .control_plane_rollout_summary import ControlPlaneRolloutSummary
    from .control_plane_status import ControlPlaneStatus
    from .create_cluster_control_plane_config import CreateClusterControlPlaneConfig
    from .disk_selection_strategy import DiskSelectionStrategy
    from .disk_selection_strategy_create import DiskSelectionStrategyCreate
    from .etcd_key_rotation_status import EtcdKeyRotationStatus
    from .etcd_key_rotation_status_failure_reason import EtcdKeyRotationStatusFailureReason
    from .etcd_key_rotation_status_phase import EtcdKeyRotationStatusPhase
    from .etcd_key_rotation_status_state import EtcdKeyRotationStatusState
    from .generic_error import GenericError
    from .launch_layer_cluster_owner import LaunchLayerClusterOwner
    from .launch_layer_cluster_provider import LaunchLayerClusterProvider
    from .launch_layer_cluster_provider_vpc_type import LaunchLayerClusterProviderVpcType
    from .launch_layer_control_plane_provider import LaunchLayerControlPlaneProvider
    from .launch_layer_control_plane_provider_fulfillment_strategy import (
        LaunchLayerControlPlaneProviderFulfillmentStrategy,
    )
    from .launch_layer_control_plane_provider_update import LaunchLayerControlPlaneProviderUpdate
    from .launch_layer_node_pool_provider import LaunchLayerNodePoolProvider
    from .launch_layer_node_pool_provider_fulfillment_strategy import LaunchLayerNodePoolProviderFulfillmentStrategy
    from .launch_layer_node_pool_provider_update import LaunchLayerNodePoolProviderUpdate
    from .launch_layer_node_provider import LaunchLayerNodeProvider
    from .launch_layer_node_set_provider import LaunchLayerNodeSetProvider
    from .launch_layer_node_set_provider_fulfillment_strategy import LaunchLayerNodeSetProviderFulfillmentStrategy
    from .launch_layer_security_group import LaunchLayerSecurityGroup
    from .launch_layer_security_group_network_type import LaunchLayerSecurityGroupNetworkType
    from .launch_layer_security_group_refs import LaunchLayerSecurityGroupRefs
    from .launch_layer_security_group_type import LaunchLayerSecurityGroupType
    from .launch_layer_security_groups import LaunchLayerSecurityGroups
    from .list_clusters_response import ListClustersResponse
    from .list_node_pools_response import ListNodePoolsResponse
    from .list_node_sets_response import ListNodeSetsResponse
    from .list_nodes_response import ListNodesResponse
    from .machine_health_issue import MachineHealthIssue
    from .nico_cluster_provider import NicoClusterProvider
    from .nico_control_plane_provider import NicoControlPlaneProvider
    from .nico_control_plane_provider_create import NicoControlPlaneProviderCreate
    from .nico_control_plane_provider_update import NicoControlPlaneProviderUpdate
    from .nico_node_pool_provider import NicoNodePoolProvider
    from .nico_node_pool_provider_update import NicoNodePoolProviderUpdate
    from .nico_node_provider import NicoNodeProvider
    from .nico_node_set_provider import NicoNodeSetProvider
    from .node import Node
    from .node_agent_config import NodeAgentConfig
    from .node_agent_upgrade_status import NodeAgentUpgradeStatus
    from .node_agent_upgrade_status_phase import NodeAgentUpgradeStatusPhase
    from .node_conditions import NodeConditions
    from .node_name_prefix import NodeNamePrefix
    from .node_pool import NodePool
    from .node_pool_conditions import NodePoolConditions
    from .node_pool_create_config import NodePoolCreateConfig
    from .node_set import NodeSet
    from .node_spire_agent_status import NodeSpireAgentStatus
    from .node_taint import NodeTaint
    from .node_taint_effect import NodeTaintEffect
    from .spire_server import SpireServer
    from .update_cluster_control_plane_config import UpdateClusterControlPlaneConfig
    from .update_in_progress import UpdateInProgress
    from .update_in_progress_type import UpdateInProgressType
_dynamic_imports: typing.Dict[str, str] = {
    "CertificateRenewalStatus": ".certificate_renewal_status",
    "CertificateRenewalStatusOutcome": ".certificate_renewal_status_outcome",
    "CertificateRenewalStatusState": ".certificate_renewal_status_state",
    "Cluster": ".cluster",
    "ClusterConditions": ".cluster_conditions",
    "ClusterControlPlane": ".cluster_control_plane",
    "ClusterNetwork": ".cluster_network",
    "ClusterNetworkCreateConfig": ".cluster_network_create_config",
    "ClusterSpireServerStatus": ".cluster_spire_server_status",
    "Condition": ".condition",
    "ConditionStatus": ".condition_status",
    "ControlPlaneConfig": ".control_plane_config",
    "ControlPlaneConfigChange": ".control_plane_config_change",
    "ControlPlaneConfigField": ".control_plane_config_field",
    "ControlPlaneConfigHistory": ".control_plane_config_history",
    "ControlPlaneRolloutChange": ".control_plane_rollout_change",
    "ControlPlaneRolloutStatus": ".control_plane_rollout_status",
    "ControlPlaneRolloutSummary": ".control_plane_rollout_summary",
    "ControlPlaneStatus": ".control_plane_status",
    "CreateClusterControlPlaneConfig": ".create_cluster_control_plane_config",
    "DiskSelectionStrategy": ".disk_selection_strategy",
    "DiskSelectionStrategyCreate": ".disk_selection_strategy_create",
    "EtcdKeyRotationStatus": ".etcd_key_rotation_status",
    "EtcdKeyRotationStatusFailureReason": ".etcd_key_rotation_status_failure_reason",
    "EtcdKeyRotationStatusPhase": ".etcd_key_rotation_status_phase",
    "EtcdKeyRotationStatusState": ".etcd_key_rotation_status_state",
    "GenericError": ".generic_error",
    "LaunchLayerClusterOwner": ".launch_layer_cluster_owner",
    "LaunchLayerClusterProvider": ".launch_layer_cluster_provider",
    "LaunchLayerClusterProviderVpcType": ".launch_layer_cluster_provider_vpc_type",
    "LaunchLayerControlPlaneProvider": ".launch_layer_control_plane_provider",
    "LaunchLayerControlPlaneProviderFulfillmentStrategy": ".launch_layer_control_plane_provider_fulfillment_strategy",
    "LaunchLayerControlPlaneProviderUpdate": ".launch_layer_control_plane_provider_update",
    "LaunchLayerNodePoolProvider": ".launch_layer_node_pool_provider",
    "LaunchLayerNodePoolProviderFulfillmentStrategy": ".launch_layer_node_pool_provider_fulfillment_strategy",
    "LaunchLayerNodePoolProviderUpdate": ".launch_layer_node_pool_provider_update",
    "LaunchLayerNodeProvider": ".launch_layer_node_provider",
    "LaunchLayerNodeSetProvider": ".launch_layer_node_set_provider",
    "LaunchLayerNodeSetProviderFulfillmentStrategy": ".launch_layer_node_set_provider_fulfillment_strategy",
    "LaunchLayerSecurityGroup": ".launch_layer_security_group",
    "LaunchLayerSecurityGroupNetworkType": ".launch_layer_security_group_network_type",
    "LaunchLayerSecurityGroupRefs": ".launch_layer_security_group_refs",
    "LaunchLayerSecurityGroupType": ".launch_layer_security_group_type",
    "LaunchLayerSecurityGroups": ".launch_layer_security_groups",
    "ListClustersResponse": ".list_clusters_response",
    "ListNodePoolsResponse": ".list_node_pools_response",
    "ListNodeSetsResponse": ".list_node_sets_response",
    "ListNodesResponse": ".list_nodes_response",
    "MachineHealthIssue": ".machine_health_issue",
    "NicoClusterProvider": ".nico_cluster_provider",
    "NicoControlPlaneProvider": ".nico_control_plane_provider",
    "NicoControlPlaneProviderCreate": ".nico_control_plane_provider_create",
    "NicoControlPlaneProviderUpdate": ".nico_control_plane_provider_update",
    "NicoNodePoolProvider": ".nico_node_pool_provider",
    "NicoNodePoolProviderUpdate": ".nico_node_pool_provider_update",
    "NicoNodeProvider": ".nico_node_provider",
    "NicoNodeSetProvider": ".nico_node_set_provider",
    "Node": ".node",
    "NodeAgentConfig": ".node_agent_config",
    "NodeAgentUpgradeStatus": ".node_agent_upgrade_status",
    "NodeAgentUpgradeStatusPhase": ".node_agent_upgrade_status_phase",
    "NodeConditions": ".node_conditions",
    "NodeNamePrefix": ".node_name_prefix",
    "NodePool": ".node_pool",
    "NodePoolConditions": ".node_pool_conditions",
    "NodePoolCreateConfig": ".node_pool_create_config",
    "NodeSet": ".node_set",
    "NodeSpireAgentStatus": ".node_spire_agent_status",
    "NodeTaint": ".node_taint",
    "NodeTaintEffect": ".node_taint_effect",
    "SpireServer": ".spire_server",
    "UpdateClusterControlPlaneConfig": ".update_cluster_control_plane_config",
    "UpdateInProgress": ".update_in_progress",
    "UpdateInProgressType": ".update_in_progress_type",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "CertificateRenewalStatus",
    "CertificateRenewalStatusOutcome",
    "CertificateRenewalStatusState",
    "Cluster",
    "ClusterConditions",
    "ClusterControlPlane",
    "ClusterNetwork",
    "ClusterNetworkCreateConfig",
    "ClusterSpireServerStatus",
    "Condition",
    "ConditionStatus",
    "ControlPlaneConfig",
    "ControlPlaneConfigChange",
    "ControlPlaneConfigField",
    "ControlPlaneConfigHistory",
    "ControlPlaneRolloutChange",
    "ControlPlaneRolloutStatus",
    "ControlPlaneRolloutSummary",
    "ControlPlaneStatus",
    "CreateClusterControlPlaneConfig",
    "DiskSelectionStrategy",
    "DiskSelectionStrategyCreate",
    "EtcdKeyRotationStatus",
    "EtcdKeyRotationStatusFailureReason",
    "EtcdKeyRotationStatusPhase",
    "EtcdKeyRotationStatusState",
    "GenericError",
    "LaunchLayerClusterOwner",
    "LaunchLayerClusterProvider",
    "LaunchLayerClusterProviderVpcType",
    "LaunchLayerControlPlaneProvider",
    "LaunchLayerControlPlaneProviderFulfillmentStrategy",
    "LaunchLayerControlPlaneProviderUpdate",
    "LaunchLayerNodePoolProvider",
    "LaunchLayerNodePoolProviderFulfillmentStrategy",
    "LaunchLayerNodePoolProviderUpdate",
    "LaunchLayerNodeProvider",
    "LaunchLayerNodeSetProvider",
    "LaunchLayerNodeSetProviderFulfillmentStrategy",
    "LaunchLayerSecurityGroup",
    "LaunchLayerSecurityGroupNetworkType",
    "LaunchLayerSecurityGroupRefs",
    "LaunchLayerSecurityGroupType",
    "LaunchLayerSecurityGroups",
    "ListClustersResponse",
    "ListNodePoolsResponse",
    "ListNodeSetsResponse",
    "ListNodesResponse",
    "MachineHealthIssue",
    "NicoClusterProvider",
    "NicoControlPlaneProvider",
    "NicoControlPlaneProviderCreate",
    "NicoControlPlaneProviderUpdate",
    "NicoNodePoolProvider",
    "NicoNodePoolProviderUpdate",
    "NicoNodeProvider",
    "NicoNodeSetProvider",
    "Node",
    "NodeAgentConfig",
    "NodeAgentUpgradeStatus",
    "NodeAgentUpgradeStatusPhase",
    "NodeConditions",
    "NodeNamePrefix",
    "NodePool",
    "NodePoolConditions",
    "NodePoolCreateConfig",
    "NodeSet",
    "NodeSpireAgentStatus",
    "NodeTaint",
    "NodeTaintEffect",
    "SpireServer",
    "UpdateClusterControlPlaneConfig",
    "UpdateInProgress",
    "UpdateInProgressType",
]
