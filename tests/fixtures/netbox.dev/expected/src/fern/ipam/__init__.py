



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        IpamAggregatesListResponse,
        IpamAsnsListResponse,
        IpamFhrpGroupAssignmentsListResponse,
        IpamFhrpGroupsListResponse,
        IpamIpAddressesListResponse,
        IpamIpRangesListResponse,
        IpamL2VpnTerminationsListResponse,
        IpamL2VpnsListResponse,
        IpamPrefixesListResponse,
        IpamRirsListResponse,
        IpamRolesListResponse,
        IpamRouteTargetsListResponse,
        IpamServiceTemplatesListResponse,
        IpamServicesListResponse,
        IpamVlanGroupsListResponse,
        IpamVlansListResponse,
        IpamVrfsListResponse,
        WritableCreateAvailableVlanStatus,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "IpamAggregatesListResponse": ".types",
    "IpamAsnsListResponse": ".types",
    "IpamFhrpGroupAssignmentsListResponse": ".types",
    "IpamFhrpGroupsListResponse": ".types",
    "IpamIpAddressesListResponse": ".types",
    "IpamIpRangesListResponse": ".types",
    "IpamL2VpnTerminationsListResponse": ".types",
    "IpamL2VpnsListResponse": ".types",
    "IpamPrefixesListResponse": ".types",
    "IpamRirsListResponse": ".types",
    "IpamRolesListResponse": ".types",
    "IpamRouteTargetsListResponse": ".types",
    "IpamServiceTemplatesListResponse": ".types",
    "IpamServicesListResponse": ".types",
    "IpamVlanGroupsListResponse": ".types",
    "IpamVlansListResponse": ".types",
    "IpamVrfsListResponse": ".types",
    "WritableCreateAvailableVlanStatus": ".types",
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
