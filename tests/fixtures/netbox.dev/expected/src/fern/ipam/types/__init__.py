



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ipam_aggregates_list_response import IpamAggregatesListResponse
    from .ipam_asns_list_response import IpamAsnsListResponse
    from .ipam_fhrp_group_assignments_list_response import IpamFhrpGroupAssignmentsListResponse
    from .ipam_fhrp_groups_list_response import IpamFhrpGroupsListResponse
    from .ipam_ip_addresses_list_response import IpamIpAddressesListResponse
    from .ipam_ip_ranges_list_response import IpamIpRangesListResponse
    from .ipam_l2vpn_terminations_list_response import IpamL2VpnTerminationsListResponse
    from .ipam_l2vpns_list_response import IpamL2VpnsListResponse
    from .ipam_prefixes_list_response import IpamPrefixesListResponse
    from .ipam_rirs_list_response import IpamRirsListResponse
    from .ipam_roles_list_response import IpamRolesListResponse
    from .ipam_route_targets_list_response import IpamRouteTargetsListResponse
    from .ipam_service_templates_list_response import IpamServiceTemplatesListResponse
    from .ipam_services_list_response import IpamServicesListResponse
    from .ipam_vlan_groups_list_response import IpamVlanGroupsListResponse
    from .ipam_vlans_list_response import IpamVlansListResponse
    from .ipam_vrfs_list_response import IpamVrfsListResponse
    from .writable_create_available_vlan_status import WritableCreateAvailableVlanStatus
_dynamic_imports: typing.Dict[str, str] = {
    "IpamAggregatesListResponse": ".ipam_aggregates_list_response",
    "IpamAsnsListResponse": ".ipam_asns_list_response",
    "IpamFhrpGroupAssignmentsListResponse": ".ipam_fhrp_group_assignments_list_response",
    "IpamFhrpGroupsListResponse": ".ipam_fhrp_groups_list_response",
    "IpamIpAddressesListResponse": ".ipam_ip_addresses_list_response",
    "IpamIpRangesListResponse": ".ipam_ip_ranges_list_response",
    "IpamL2VpnTerminationsListResponse": ".ipam_l2vpn_terminations_list_response",
    "IpamL2VpnsListResponse": ".ipam_l2vpns_list_response",
    "IpamPrefixesListResponse": ".ipam_prefixes_list_response",
    "IpamRirsListResponse": ".ipam_rirs_list_response",
    "IpamRolesListResponse": ".ipam_roles_list_response",
    "IpamRouteTargetsListResponse": ".ipam_route_targets_list_response",
    "IpamServiceTemplatesListResponse": ".ipam_service_templates_list_response",
    "IpamServicesListResponse": ".ipam_services_list_response",
    "IpamVlanGroupsListResponse": ".ipam_vlan_groups_list_response",
    "IpamVlansListResponse": ".ipam_vlans_list_response",
    "IpamVrfsListResponse": ".ipam_vrfs_list_response",
    "WritableCreateAvailableVlanStatus": ".writable_create_available_vlan_status",
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
    "IpamAggregatesListResponse",
    "IpamAsnsListResponse",
    "IpamFhrpGroupAssignmentsListResponse",
    "IpamFhrpGroupsListResponse",
    "IpamIpAddressesListResponse",
    "IpamIpRangesListResponse",
    "IpamL2VpnTerminationsListResponse",
    "IpamL2VpnsListResponse",
    "IpamPrefixesListResponse",
    "IpamRirsListResponse",
    "IpamRolesListResponse",
    "IpamRouteTargetsListResponse",
    "IpamServiceTemplatesListResponse",
    "IpamServicesListResponse",
    "IpamVlanGroupsListResponse",
    "IpamVlansListResponse",
    "IpamVrfsListResponse",
    "WritableCreateAvailableVlanStatus",
]
