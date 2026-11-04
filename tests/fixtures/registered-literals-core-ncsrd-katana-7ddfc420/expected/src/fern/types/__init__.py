



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .resources import Resources
    from .resources_functions_item import ResourcesFunctionsItem
    from .resources_functions_item_pnf_list_item import ResourcesFunctionsItemPnfListItem
    from .resources_functions_item_shared import ResourcesFunctionsItemShared
    from .resources_vi_ms_item import ResourcesViMsItem
    from .resources_vi_ms_item_available_resources import ResourcesViMsItemAvailableResources
    from .resources_vi_ms_item_max_resources import ResourcesViMsItemMaxResources
    from .resources_vi_ms_item_tenants import ResourcesViMsItemTenants
    from .base_slice_des import BaseSliceDes
    from .base_slice_des_deterministic_communication import BaseSliceDesDeterministicCommunication
    from .base_slice_des_mission_critical_support import BaseSliceDesMissionCriticalSupport
    from .base_slice_des_network_dl_throughput import BaseSliceDesNetworkDlThroughput
    from .base_slice_des_network_ul_throughput import BaseSliceDesNetworkUlThroughput
    from .base_slice_des_positional_support import BaseSliceDesPositionalSupport
    from .base_slice_des_qos_item import BaseSliceDesQosItem
    from .base_slice_des_ue_dl_throughput import BaseSliceDesUeDlThroughput
    from .base_slice_des_ue_ul_throughput import BaseSliceDesUeUlThroughput
    from .ems import Ems
    from .gst import Gst
    from .location_descriptor import LocationDescriptor
    from .net_func import NetFunc
    from .net_func_shared import NetFuncShared
    from .nfvo import Nfvo
    from .nfvo_config import NfvoConfig
    from .ns import Ns
    from .nsd import Nsd
    from .nsd_flavor import NsdFlavor
    from .nsi import Nsi
    from .nsi_connections_item import NsiConnectionsItem
    from .nsi_connections_item_core import NsiConnectionsItemCore
    from .nsi_connections_item_core_ns_list_item import NsiConnectionsItemCoreNsListItem
    from .nsi_connections_item_core_pnf_list_item import NsiConnectionsItemCorePnfListItem
    from .nsi_connections_item_core_shared import NsiConnectionsItemCoreShared
    from .nsi_mission_critical_support import NsiMissionCriticalSupport
    from .nsi_network_dl_throughput import NsiNetworkDlThroughput
    from .nsi_network_ul_throughput import NsiNetworkUlThroughput
    from .nsi_ns_list_item import NsiNsListItem
    from .nsi_ns_list_item_nsd_info import NsiNsListItemNsdInfo
    from .nsi_ns_list_item_nsd_info_flavor import NsiNsListItemNsdInfoFlavor
    from .nsi_ns_list_item_placement_loc import NsiNsListItemPlacementLoc
    from .nsi_positional_support import NsiPositionalSupport
    from .nsi_qos_item import NsiQosItem
    from .nsi_ue_dl_throughput import NsiUeDlThroughput
    from .nsi_ue_ul_throughput import NsiUeUlThroughput
    from .nsi_wim_data import NsiWimData
    from .nsi_wim_data_core_connections_item import NsiWimDataCoreConnectionsItem
    from .nsi_wim_data_core_connections_item_core import NsiWimDataCoreConnectionsItemCore
    from .nsi_wim_data_core_connections_item_core_ns_item import NsiWimDataCoreConnectionsItemCoreNsItem
    from .nsi_wim_data_core_connections_item_core_pnf_item import NsiWimDataCoreConnectionsItemCorePnfItem
    from .nsi_wim_data_core_connections_item_radio import NsiWimDataCoreConnectionsItemRadio
    from .nsi_wim_data_core_connections_item_radio_ns_item import NsiWimDataCoreConnectionsItemRadioNsItem
    from .nsi_wim_data_core_connections_item_radio_pnf_item import NsiWimDataCoreConnectionsItemRadioPnfItem
    from .nsi_wim_data_extra_ns_item import NsiWimDataExtraNsItem
    from .nsi_wim_data_slice_sla import NsiWimDataSliceSla
    from .nsi_wim_data_slice_sla_network_dl_throughput import NsiWimDataSliceSlaNetworkDlThroughput
    from .nsi_wim_data_slice_sla_network_ul_throughput import NsiWimDataSliceSlaNetworkUlThroughput
    from .pnf import Pnf
    from .policy import Policy
    from .sbi_ls import SbiLs
    from .service_descriptor import ServiceDescriptor
    from .service_descriptor_ns_list_item import ServiceDescriptorNsListItem
    from .slice_ls import SliceLs
    from .stored_location import StoredLocation
    from .test_descriptor import TestDescriptor
    from .test_descriptor_performance_monitoring import TestDescriptorPerformanceMonitoring
    from .test_descriptor_performance_prediction import TestDescriptorPerformancePrediction
    from .time import Time
    from .time_ns_deployment_time import TimeNsDeploymentTime
    from .vim import Vim
    from .vim_config import VimConfig
    from .wim import Wim
_dynamic_imports: typing.Dict[str, str] = {
    "BaseSliceDes": ".base_slice_des",
    "BaseSliceDesDeterministicCommunication": ".base_slice_des_deterministic_communication",
    "BaseSliceDesMissionCriticalSupport": ".base_slice_des_mission_critical_support",
    "BaseSliceDesNetworkDlThroughput": ".base_slice_des_network_dl_throughput",
    "BaseSliceDesNetworkUlThroughput": ".base_slice_des_network_ul_throughput",
    "BaseSliceDesPositionalSupport": ".base_slice_des_positional_support",
    "BaseSliceDesQosItem": ".base_slice_des_qos_item",
    "BaseSliceDesUeDlThroughput": ".base_slice_des_ue_dl_throughput",
    "BaseSliceDesUeUlThroughput": ".base_slice_des_ue_ul_throughput",
    "Ems": ".ems",
    "Gst": ".gst",
    "LocationDescriptor": ".location_descriptor",
    "NetFunc": ".net_func",
    "NetFuncShared": ".net_func_shared",
    "Nfvo": ".nfvo",
    "NfvoConfig": ".nfvo_config",
    "Ns": ".ns",
    "Nsd": ".nsd",
    "NsdFlavor": ".nsd_flavor",
    "Nsi": ".nsi",
    "NsiConnectionsItem": ".nsi_connections_item",
    "NsiConnectionsItemCore": ".nsi_connections_item_core",
    "NsiConnectionsItemCoreNsListItem": ".nsi_connections_item_core_ns_list_item",
    "NsiConnectionsItemCorePnfListItem": ".nsi_connections_item_core_pnf_list_item",
    "NsiConnectionsItemCoreShared": ".nsi_connections_item_core_shared",
    "NsiMissionCriticalSupport": ".nsi_mission_critical_support",
    "NsiNetworkDlThroughput": ".nsi_network_dl_throughput",
    "NsiNetworkUlThroughput": ".nsi_network_ul_throughput",
    "NsiNsListItem": ".nsi_ns_list_item",
    "NsiNsListItemNsdInfo": ".nsi_ns_list_item_nsd_info",
    "NsiNsListItemNsdInfoFlavor": ".nsi_ns_list_item_nsd_info_flavor",
    "NsiNsListItemPlacementLoc": ".nsi_ns_list_item_placement_loc",
    "NsiPositionalSupport": ".nsi_positional_support",
    "NsiQosItem": ".nsi_qos_item",
    "NsiUeDlThroughput": ".nsi_ue_dl_throughput",
    "NsiUeUlThroughput": ".nsi_ue_ul_throughput",
    "NsiWimData": ".nsi_wim_data",
    "NsiWimDataCoreConnectionsItem": ".nsi_wim_data_core_connections_item",
    "NsiWimDataCoreConnectionsItemCore": ".nsi_wim_data_core_connections_item_core",
    "NsiWimDataCoreConnectionsItemCoreNsItem": ".nsi_wim_data_core_connections_item_core_ns_item",
    "NsiWimDataCoreConnectionsItemCorePnfItem": ".nsi_wim_data_core_connections_item_core_pnf_item",
    "NsiWimDataCoreConnectionsItemRadio": ".nsi_wim_data_core_connections_item_radio",
    "NsiWimDataCoreConnectionsItemRadioNsItem": ".nsi_wim_data_core_connections_item_radio_ns_item",
    "NsiWimDataCoreConnectionsItemRadioPnfItem": ".nsi_wim_data_core_connections_item_radio_pnf_item",
    "NsiWimDataExtraNsItem": ".nsi_wim_data_extra_ns_item",
    "NsiWimDataSliceSla": ".nsi_wim_data_slice_sla",
    "NsiWimDataSliceSlaNetworkDlThroughput": ".nsi_wim_data_slice_sla_network_dl_throughput",
    "NsiWimDataSliceSlaNetworkUlThroughput": ".nsi_wim_data_slice_sla_network_ul_throughput",
    "Pnf": ".pnf",
    "Policy": ".policy",
    "Resources": ".resources",
    "ResourcesFunctionsItem": ".resources_functions_item",
    "ResourcesFunctionsItemPnfListItem": ".resources_functions_item_pnf_list_item",
    "ResourcesFunctionsItemShared": ".resources_functions_item_shared",
    "ResourcesViMsItem": ".resources_vi_ms_item",
    "ResourcesViMsItemAvailableResources": ".resources_vi_ms_item_available_resources",
    "ResourcesViMsItemMaxResources": ".resources_vi_ms_item_max_resources",
    "ResourcesViMsItemTenants": ".resources_vi_ms_item_tenants",
    "SbiLs": ".sbi_ls",
    "ServiceDescriptor": ".service_descriptor",
    "ServiceDescriptorNsListItem": ".service_descriptor_ns_list_item",
    "SliceLs": ".slice_ls",
    "StoredLocation": ".stored_location",
    "TestDescriptor": ".test_descriptor",
    "TestDescriptorPerformanceMonitoring": ".test_descriptor_performance_monitoring",
    "TestDescriptorPerformancePrediction": ".test_descriptor_performance_prediction",
    "Time": ".time",
    "TimeNsDeploymentTime": ".time_ns_deployment_time",
    "Vim": ".vim",
    "VimConfig": ".vim_config",
    "Wim": ".wim",
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
    "BaseSliceDes",
    "BaseSliceDesDeterministicCommunication",
    "BaseSliceDesMissionCriticalSupport",
    "BaseSliceDesNetworkDlThroughput",
    "BaseSliceDesNetworkUlThroughput",
    "BaseSliceDesPositionalSupport",
    "BaseSliceDesQosItem",
    "BaseSliceDesUeDlThroughput",
    "BaseSliceDesUeUlThroughput",
    "Ems",
    "Gst",
    "LocationDescriptor",
    "NetFunc",
    "NetFuncShared",
    "Nfvo",
    "NfvoConfig",
    "Ns",
    "Nsd",
    "NsdFlavor",
    "Nsi",
    "NsiConnectionsItem",
    "NsiConnectionsItemCore",
    "NsiConnectionsItemCoreNsListItem",
    "NsiConnectionsItemCorePnfListItem",
    "NsiConnectionsItemCoreShared",
    "NsiMissionCriticalSupport",
    "NsiNetworkDlThroughput",
    "NsiNetworkUlThroughput",
    "NsiNsListItem",
    "NsiNsListItemNsdInfo",
    "NsiNsListItemNsdInfoFlavor",
    "NsiNsListItemPlacementLoc",
    "NsiPositionalSupport",
    "NsiQosItem",
    "NsiUeDlThroughput",
    "NsiUeUlThroughput",
    "NsiWimData",
    "NsiWimDataCoreConnectionsItem",
    "NsiWimDataCoreConnectionsItemCore",
    "NsiWimDataCoreConnectionsItemCoreNsItem",
    "NsiWimDataCoreConnectionsItemCorePnfItem",
    "NsiWimDataCoreConnectionsItemRadio",
    "NsiWimDataCoreConnectionsItemRadioNsItem",
    "NsiWimDataCoreConnectionsItemRadioPnfItem",
    "NsiWimDataExtraNsItem",
    "NsiWimDataSliceSla",
    "NsiWimDataSliceSlaNetworkDlThroughput",
    "NsiWimDataSliceSlaNetworkUlThroughput",
    "Pnf",
    "Policy",
    "Resources",
    "ResourcesFunctionsItem",
    "ResourcesFunctionsItemPnfListItem",
    "ResourcesFunctionsItemShared",
    "ResourcesViMsItem",
    "ResourcesViMsItemAvailableResources",
    "ResourcesViMsItemMaxResources",
    "ResourcesViMsItemTenants",
    "SbiLs",
    "ServiceDescriptor",
    "ServiceDescriptorNsListItem",
    "SliceLs",
    "StoredLocation",
    "TestDescriptor",
    "TestDescriptorPerformanceMonitoring",
    "TestDescriptorPerformancePrediction",
    "Time",
    "TimeNsDeploymentTime",
    "Vim",
    "VimConfig",
    "Wim",
]
