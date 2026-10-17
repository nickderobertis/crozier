



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        InviteExternalUserJitAccessBodyRolesItem,
        InviteExternalUserJitAccessBodyRolesItemAllowedNetworks,
        InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
        InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item,
        JitAccessRequestRequestState,
        SetUpReadReplicaBodyReadReplicaRegion,
        SslEnforcementRequestRequestedConfig,
        UpdateJitAccessBodyRolesItem,
        UpdateJitAccessBodyRolesItemAllowedNetworks,
        UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
        UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item,
        UpdatePostgresConfigBodySessionReplicationRole,
        UpdateSupavisorConfigBodyPoolMode,
        V1GetJitAccessConfigResponse,
        V1GetJitAccessConfigResponseAppliedSuccessfully,
        V1GetJitAccessConfigResponseAppliedSuccessfullyState,
        V1GetJitAccessConfigResponseUnavailableReason,
        V1GetJitAccessConfigResponseUnavailableReasonState,
        V1GetJitAccessConfigResponseUnavailableReasonUnavailableReason,
        V1ListAllSnippetsRequestSortBy,
        V1ListAllSnippetsRequestSortOrder,
        V1UpdateJitAccessConfigResponse,
        V1UpdateJitAccessConfigResponseAppliedSuccessfully,
        V1UpdateJitAccessConfigResponseAppliedSuccessfullyState,
        V1UpdateJitAccessConfigResponseUnavailableReason,
        V1UpdateJitAccessConfigResponseUnavailableReasonState,
        V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "InviteExternalUserJitAccessBodyRolesItem": ".types",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworks": ".types",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem": ".types",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item": ".types",
    "JitAccessRequestRequestState": ".types",
    "SetUpReadReplicaBodyReadReplicaRegion": ".types",
    "SslEnforcementRequestRequestedConfig": ".types",
    "UpdateJitAccessBodyRolesItem": ".types",
    "UpdateJitAccessBodyRolesItemAllowedNetworks": ".types",
    "UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem": ".types",
    "UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item": ".types",
    "UpdatePostgresConfigBodySessionReplicationRole": ".types",
    "UpdateSupavisorConfigBodyPoolMode": ".types",
    "V1GetJitAccessConfigResponse": ".types",
    "V1GetJitAccessConfigResponseAppliedSuccessfully": ".types",
    "V1GetJitAccessConfigResponseAppliedSuccessfullyState": ".types",
    "V1GetJitAccessConfigResponseUnavailableReason": ".types",
    "V1GetJitAccessConfigResponseUnavailableReasonState": ".types",
    "V1GetJitAccessConfigResponseUnavailableReasonUnavailableReason": ".types",
    "V1ListAllSnippetsRequestSortBy": ".types",
    "V1ListAllSnippetsRequestSortOrder": ".types",
    "V1UpdateJitAccessConfigResponse": ".types",
    "V1UpdateJitAccessConfigResponseAppliedSuccessfully": ".types",
    "V1UpdateJitAccessConfigResponseAppliedSuccessfullyState": ".types",
    "V1UpdateJitAccessConfigResponseUnavailableReason": ".types",
    "V1UpdateJitAccessConfigResponseUnavailableReasonState": ".types",
    "V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason": ".types",
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
    "InviteExternalUserJitAccessBodyRolesItem",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworks",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item",
    "JitAccessRequestRequestState",
    "SetUpReadReplicaBodyReadReplicaRegion",
    "SslEnforcementRequestRequestedConfig",
    "UpdateJitAccessBodyRolesItem",
    "UpdateJitAccessBodyRolesItemAllowedNetworks",
    "UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem",
    "UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item",
    "UpdatePostgresConfigBodySessionReplicationRole",
    "UpdateSupavisorConfigBodyPoolMode",
    "V1GetJitAccessConfigResponse",
    "V1GetJitAccessConfigResponseAppliedSuccessfully",
    "V1GetJitAccessConfigResponseAppliedSuccessfullyState",
    "V1GetJitAccessConfigResponseUnavailableReason",
    "V1GetJitAccessConfigResponseUnavailableReasonState",
    "V1GetJitAccessConfigResponseUnavailableReasonUnavailableReason",
    "V1ListAllSnippetsRequestSortBy",
    "V1ListAllSnippetsRequestSortOrder",
    "V1UpdateJitAccessConfigResponse",
    "V1UpdateJitAccessConfigResponseAppliedSuccessfully",
    "V1UpdateJitAccessConfigResponseAppliedSuccessfullyState",
    "V1UpdateJitAccessConfigResponseUnavailableReason",
    "V1UpdateJitAccessConfigResponseUnavailableReasonState",
    "V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason",
]
