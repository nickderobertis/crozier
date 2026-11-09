



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_policies_policy_id_dry_run_artifacts_response_item import GetPoliciesPolicyIdDryRunArtifactsResponseItem
    from .get_policies_policy_id_dry_run_ipfs_response_item import GetPoliciesPolicyIdDryRunIpfsResponseItem
    from .get_policies_policy_id_dry_run_transactions_response_item import (
        GetPoliciesPolicyIdDryRunTransactionsResponseItem,
    )
    from .get_policies_policy_id_dry_run_users_response_item import GetPoliciesPolicyIdDryRunUsersResponseItem
    from .get_policies_policy_id_groups_response_item import GetPoliciesPolicyIdGroupsResponseItem
    from .get_policies_policy_id_response import GetPoliciesPolicyIdResponse
    from .get_policies_policy_id_tag_tag_response import GetPoliciesPolicyIdTagTagResponse
    from .get_policies_response_item import GetPoliciesResponseItem
    from .policy_api_get_policy_documents_request_type import PolicyApiGetPolicyDocumentsRequestType
    from .policy_api_migrate_data_response_item import PolicyApiMigrateDataResponseItem
    from .post_policies_policy_id_dry_run_login_response_item import PostPoliciesPolicyIdDryRunLoginResponseItem
    from .post_policies_policy_id_dry_run_user_response_item import PostPoliciesPolicyIdDryRunUserResponseItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetPoliciesPolicyIdDryRunArtifactsResponseItem": ".get_policies_policy_id_dry_run_artifacts_response_item",
    "GetPoliciesPolicyIdDryRunIpfsResponseItem": ".get_policies_policy_id_dry_run_ipfs_response_item",
    "GetPoliciesPolicyIdDryRunTransactionsResponseItem": ".get_policies_policy_id_dry_run_transactions_response_item",
    "GetPoliciesPolicyIdDryRunUsersResponseItem": ".get_policies_policy_id_dry_run_users_response_item",
    "GetPoliciesPolicyIdGroupsResponseItem": ".get_policies_policy_id_groups_response_item",
    "GetPoliciesPolicyIdResponse": ".get_policies_policy_id_response",
    "GetPoliciesPolicyIdTagTagResponse": ".get_policies_policy_id_tag_tag_response",
    "GetPoliciesResponseItem": ".get_policies_response_item",
    "PolicyApiGetPolicyDocumentsRequestType": ".policy_api_get_policy_documents_request_type",
    "PolicyApiMigrateDataResponseItem": ".policy_api_migrate_data_response_item",
    "PostPoliciesPolicyIdDryRunLoginResponseItem": ".post_policies_policy_id_dry_run_login_response_item",
    "PostPoliciesPolicyIdDryRunUserResponseItem": ".post_policies_policy_id_dry_run_user_response_item",
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
    "GetPoliciesPolicyIdDryRunArtifactsResponseItem",
    "GetPoliciesPolicyIdDryRunIpfsResponseItem",
    "GetPoliciesPolicyIdDryRunTransactionsResponseItem",
    "GetPoliciesPolicyIdDryRunUsersResponseItem",
    "GetPoliciesPolicyIdGroupsResponseItem",
    "GetPoliciesPolicyIdResponse",
    "GetPoliciesPolicyIdTagTagResponse",
    "GetPoliciesResponseItem",
    "PolicyApiGetPolicyDocumentsRequestType",
    "PolicyApiMigrateDataResponseItem",
    "PostPoliciesPolicyIdDryRunLoginResponseItem",
    "PostPoliciesPolicyIdDryRunUserResponseItem",
]
