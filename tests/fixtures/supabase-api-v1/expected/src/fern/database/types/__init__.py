



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .invite_external_user_jit_access_body_roles_item import InviteExternalUserJitAccessBodyRolesItem
    from .invite_external_user_jit_access_body_roles_item_allowed_networks import (
        InviteExternalUserJitAccessBodyRolesItemAllowedNetworks,
    )
    from .invite_external_user_jit_access_body_roles_item_allowed_networks_allowed_cidrs_item import (
        InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
    )
    from .invite_external_user_jit_access_body_roles_item_allowed_networks_allowed_cidrs_v6item import (
        InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item,
    )
    from .jit_access_request_request_state import JitAccessRequestRequestState
    from .set_up_read_replica_body_read_replica_region import SetUpReadReplicaBodyReadReplicaRegion
    from .ssl_enforcement_request_requested_config import SslEnforcementRequestRequestedConfig
    from .update_jit_access_body_roles_item import UpdateJitAccessBodyRolesItem
    from .update_jit_access_body_roles_item_allowed_networks import UpdateJitAccessBodyRolesItemAllowedNetworks
    from .update_jit_access_body_roles_item_allowed_networks_allowed_cidrs_item import (
        UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
    )
    from .update_jit_access_body_roles_item_allowed_networks_allowed_cidrs_v6item import (
        UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item,
    )
    from .update_postgres_config_body_session_replication_role import UpdatePostgresConfigBodySessionReplicationRole
    from .update_supavisor_config_body_pool_mode import UpdateSupavisorConfigBodyPoolMode
    from .v1get_jit_access_config_response import V1GetJitAccessConfigResponse
    from .v1get_jit_access_config_response_applied_successfully import V1GetJitAccessConfigResponseAppliedSuccessfully
    from .v1get_jit_access_config_response_applied_successfully_state import (
        V1GetJitAccessConfigResponseAppliedSuccessfullyState,
    )
    from .v1get_jit_access_config_response_unavailable_reason import V1GetJitAccessConfigResponseUnavailableReason
    from .v1get_jit_access_config_response_unavailable_reason_state import (
        V1GetJitAccessConfigResponseUnavailableReasonState,
    )
    from .v1get_jit_access_config_response_unavailable_reason_unavailable_reason import (
        V1GetJitAccessConfigResponseUnavailableReasonUnavailableReason,
    )
    from .v1list_all_snippets_request_sort_by import V1ListAllSnippetsRequestSortBy
    from .v1list_all_snippets_request_sort_order import V1ListAllSnippetsRequestSortOrder
    from .v1update_jit_access_config_response import V1UpdateJitAccessConfigResponse
    from .v1update_jit_access_config_response_applied_successfully import (
        V1UpdateJitAccessConfigResponseAppliedSuccessfully,
    )
    from .v1update_jit_access_config_response_applied_successfully_state import (
        V1UpdateJitAccessConfigResponseAppliedSuccessfullyState,
    )
    from .v1update_jit_access_config_response_unavailable_reason import V1UpdateJitAccessConfigResponseUnavailableReason
    from .v1update_jit_access_config_response_unavailable_reason_state import (
        V1UpdateJitAccessConfigResponseUnavailableReasonState,
    )
    from .v1update_jit_access_config_response_unavailable_reason_unavailable_reason import (
        V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "InviteExternalUserJitAccessBodyRolesItem": ".invite_external_user_jit_access_body_roles_item",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworks": ".invite_external_user_jit_access_body_roles_item_allowed_networks",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem": ".invite_external_user_jit_access_body_roles_item_allowed_networks_allowed_cidrs_item",
    "InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item": ".invite_external_user_jit_access_body_roles_item_allowed_networks_allowed_cidrs_v6item",
    "JitAccessRequestRequestState": ".jit_access_request_request_state",
    "SetUpReadReplicaBodyReadReplicaRegion": ".set_up_read_replica_body_read_replica_region",
    "SslEnforcementRequestRequestedConfig": ".ssl_enforcement_request_requested_config",
    "UpdateJitAccessBodyRolesItem": ".update_jit_access_body_roles_item",
    "UpdateJitAccessBodyRolesItemAllowedNetworks": ".update_jit_access_body_roles_item_allowed_networks",
    "UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem": ".update_jit_access_body_roles_item_allowed_networks_allowed_cidrs_item",
    "UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsV6Item": ".update_jit_access_body_roles_item_allowed_networks_allowed_cidrs_v6item",
    "UpdatePostgresConfigBodySessionReplicationRole": ".update_postgres_config_body_session_replication_role",
    "UpdateSupavisorConfigBodyPoolMode": ".update_supavisor_config_body_pool_mode",
    "V1GetJitAccessConfigResponse": ".v1get_jit_access_config_response",
    "V1GetJitAccessConfigResponseAppliedSuccessfully": ".v1get_jit_access_config_response_applied_successfully",
    "V1GetJitAccessConfigResponseAppliedSuccessfullyState": ".v1get_jit_access_config_response_applied_successfully_state",
    "V1GetJitAccessConfigResponseUnavailableReason": ".v1get_jit_access_config_response_unavailable_reason",
    "V1GetJitAccessConfigResponseUnavailableReasonState": ".v1get_jit_access_config_response_unavailable_reason_state",
    "V1GetJitAccessConfigResponseUnavailableReasonUnavailableReason": ".v1get_jit_access_config_response_unavailable_reason_unavailable_reason",
    "V1ListAllSnippetsRequestSortBy": ".v1list_all_snippets_request_sort_by",
    "V1ListAllSnippetsRequestSortOrder": ".v1list_all_snippets_request_sort_order",
    "V1UpdateJitAccessConfigResponse": ".v1update_jit_access_config_response",
    "V1UpdateJitAccessConfigResponseAppliedSuccessfully": ".v1update_jit_access_config_response_applied_successfully",
    "V1UpdateJitAccessConfigResponseAppliedSuccessfullyState": ".v1update_jit_access_config_response_applied_successfully_state",
    "V1UpdateJitAccessConfigResponseUnavailableReason": ".v1update_jit_access_config_response_unavailable_reason",
    "V1UpdateJitAccessConfigResponseUnavailableReasonState": ".v1update_jit_access_config_response_unavailable_reason_state",
    "V1UpdateJitAccessConfigResponseUnavailableReasonUnavailableReason": ".v1update_jit_access_config_response_unavailable_reason_unavailable_reason",
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
