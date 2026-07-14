



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .admin_get_user_response import AdminGetUserResponse
    from .admin_get_user_response_approved_by import AdminGetUserResponseApprovedBy
    from .admin_get_user_response_groups_item import AdminGetUserResponseGroupsItem
    from .admin_get_user_response_penalty_counts import AdminGetUserResponsePenaltyCounts
    from .admin_get_user_response_tl3requirements import AdminGetUserResponseTl3Requirements
    from .admin_get_user_response_tl3requirements_penalty_counts import AdminGetUserResponseTl3RequirementsPenaltyCounts
    from .admin_list_users_request_asc import AdminListUsersRequestAsc
    from .admin_list_users_request_flag import AdminListUsersRequestFlag
    from .admin_list_users_request_order import AdminListUsersRequestOrder
    from .admin_list_users_response_item import AdminListUsersResponseItem
    from .anonymize_user_response import AnonymizeUserResponse
    from .create_user_response import CreateUserResponse
    from .delete_user_response import DeleteUserResponse
    from .get_user_emails_response import GetUserEmailsResponse
    from .get_user_external_id_response import GetUserExternalIdResponse
    from .get_user_external_id_response_user import GetUserExternalIdResponseUser
    from .get_user_external_id_response_user_custom_fields import GetUserExternalIdResponseUserCustomFields
    from .get_user_external_id_response_user_group_users_item import GetUserExternalIdResponseUserGroupUsersItem
    from .get_user_external_id_response_user_groups_item import GetUserExternalIdResponseUserGroupsItem
    from .get_user_external_id_response_user_user_auth_tokens_item import (
        GetUserExternalIdResponseUserUserAuthTokensItem,
    )
    from .get_user_external_id_response_user_user_fields import GetUserExternalIdResponseUserUserFields
    from .get_user_external_id_response_user_user_notification_schedule import (
        GetUserExternalIdResponseUserUserNotificationSchedule,
    )
    from .get_user_external_id_response_user_user_option import GetUserExternalIdResponseUserUserOption
    from .get_user_identiy_provider_external_id_response import GetUserIdentiyProviderExternalIdResponse
    from .get_user_identiy_provider_external_id_response_user import GetUserIdentiyProviderExternalIdResponseUser
    from .get_user_identiy_provider_external_id_response_user_custom_fields import (
        GetUserIdentiyProviderExternalIdResponseUserCustomFields,
    )
    from .get_user_identiy_provider_external_id_response_user_group_users_item import (
        GetUserIdentiyProviderExternalIdResponseUserGroupUsersItem,
    )
    from .get_user_identiy_provider_external_id_response_user_groups_item import (
        GetUserIdentiyProviderExternalIdResponseUserGroupsItem,
    )
    from .get_user_identiy_provider_external_id_response_user_user_auth_tokens_item import (
        GetUserIdentiyProviderExternalIdResponseUserUserAuthTokensItem,
    )
    from .get_user_identiy_provider_external_id_response_user_user_fields import (
        GetUserIdentiyProviderExternalIdResponseUserUserFields,
    )
    from .get_user_identiy_provider_external_id_response_user_user_notification_schedule import (
        GetUserIdentiyProviderExternalIdResponseUserUserNotificationSchedule,
    )
    from .get_user_identiy_provider_external_id_response_user_user_option import (
        GetUserIdentiyProviderExternalIdResponseUserUserOption,
    )
    from .get_user_response import GetUserResponse
    from .get_user_response_user import GetUserResponseUser
    from .get_user_response_user_custom_fields import GetUserResponseUserCustomFields
    from .get_user_response_user_group_users_item import GetUserResponseUserGroupUsersItem
    from .get_user_response_user_groups_item import GetUserResponseUserGroupsItem
    from .get_user_response_user_user_auth_tokens_item import GetUserResponseUserUserAuthTokensItem
    from .get_user_response_user_user_fields import GetUserResponseUserUserFields
    from .get_user_response_user_user_notification_schedule import GetUserResponseUserUserNotificationSchedule
    from .get_user_response_user_user_option import GetUserResponseUserUserOption
    from .list_user_actions_response import ListUserActionsResponse
    from .list_user_actions_response_user_actions_item import ListUserActionsResponseUserActionsItem
    from .list_users_public_request_asc import ListUsersPublicRequestAsc
    from .list_users_public_request_order import ListUsersPublicRequestOrder
    from .list_users_public_request_period import ListUsersPublicRequestPeriod
    from .list_users_public_response import ListUsersPublicResponse
    from .list_users_public_response_directory_items_item import ListUsersPublicResponseDirectoryItemsItem
    from .list_users_public_response_directory_items_item_user import ListUsersPublicResponseDirectoryItemsItemUser
    from .list_users_public_response_meta import ListUsersPublicResponseMeta
    from .log_out_user_response import LogOutUserResponse
    from .refresh_gravatar_response import RefreshGravatarResponse
    from .send_password_reset_email_response import SendPasswordResetEmailResponse
    from .silence_user_response import SilenceUserResponse
    from .silence_user_response_silence import SilenceUserResponseSilence
    from .silence_user_response_silence_silenced_by import SilenceUserResponseSilenceSilencedBy
    from .suspend_user_response import SuspendUserResponse
    from .suspend_user_response_suspension import SuspendUserResponseSuspension
    from .suspend_user_response_suspension_suspended_by import SuspendUserResponseSuspensionSuspendedBy
    from .update_avatar_request_type import UpdateAvatarRequestType
    from .update_avatar_response import UpdateAvatarResponse
    from .update_user_response import UpdateUserResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AdminGetUserResponse": ".admin_get_user_response",
    "AdminGetUserResponseApprovedBy": ".admin_get_user_response_approved_by",
    "AdminGetUserResponseGroupsItem": ".admin_get_user_response_groups_item",
    "AdminGetUserResponsePenaltyCounts": ".admin_get_user_response_penalty_counts",
    "AdminGetUserResponseTl3Requirements": ".admin_get_user_response_tl3requirements",
    "AdminGetUserResponseTl3RequirementsPenaltyCounts": ".admin_get_user_response_tl3requirements_penalty_counts",
    "AdminListUsersRequestAsc": ".admin_list_users_request_asc",
    "AdminListUsersRequestFlag": ".admin_list_users_request_flag",
    "AdminListUsersRequestOrder": ".admin_list_users_request_order",
    "AdminListUsersResponseItem": ".admin_list_users_response_item",
    "AnonymizeUserResponse": ".anonymize_user_response",
    "CreateUserResponse": ".create_user_response",
    "DeleteUserResponse": ".delete_user_response",
    "GetUserEmailsResponse": ".get_user_emails_response",
    "GetUserExternalIdResponse": ".get_user_external_id_response",
    "GetUserExternalIdResponseUser": ".get_user_external_id_response_user",
    "GetUserExternalIdResponseUserCustomFields": ".get_user_external_id_response_user_custom_fields",
    "GetUserExternalIdResponseUserGroupUsersItem": ".get_user_external_id_response_user_group_users_item",
    "GetUserExternalIdResponseUserGroupsItem": ".get_user_external_id_response_user_groups_item",
    "GetUserExternalIdResponseUserUserAuthTokensItem": ".get_user_external_id_response_user_user_auth_tokens_item",
    "GetUserExternalIdResponseUserUserFields": ".get_user_external_id_response_user_user_fields",
    "GetUserExternalIdResponseUserUserNotificationSchedule": ".get_user_external_id_response_user_user_notification_schedule",
    "GetUserExternalIdResponseUserUserOption": ".get_user_external_id_response_user_user_option",
    "GetUserIdentiyProviderExternalIdResponse": ".get_user_identiy_provider_external_id_response",
    "GetUserIdentiyProviderExternalIdResponseUser": ".get_user_identiy_provider_external_id_response_user",
    "GetUserIdentiyProviderExternalIdResponseUserCustomFields": ".get_user_identiy_provider_external_id_response_user_custom_fields",
    "GetUserIdentiyProviderExternalIdResponseUserGroupUsersItem": ".get_user_identiy_provider_external_id_response_user_group_users_item",
    "GetUserIdentiyProviderExternalIdResponseUserGroupsItem": ".get_user_identiy_provider_external_id_response_user_groups_item",
    "GetUserIdentiyProviderExternalIdResponseUserUserAuthTokensItem": ".get_user_identiy_provider_external_id_response_user_user_auth_tokens_item",
    "GetUserIdentiyProviderExternalIdResponseUserUserFields": ".get_user_identiy_provider_external_id_response_user_user_fields",
    "GetUserIdentiyProviderExternalIdResponseUserUserNotificationSchedule": ".get_user_identiy_provider_external_id_response_user_user_notification_schedule",
    "GetUserIdentiyProviderExternalIdResponseUserUserOption": ".get_user_identiy_provider_external_id_response_user_user_option",
    "GetUserResponse": ".get_user_response",
    "GetUserResponseUser": ".get_user_response_user",
    "GetUserResponseUserCustomFields": ".get_user_response_user_custom_fields",
    "GetUserResponseUserGroupUsersItem": ".get_user_response_user_group_users_item",
    "GetUserResponseUserGroupsItem": ".get_user_response_user_groups_item",
    "GetUserResponseUserUserAuthTokensItem": ".get_user_response_user_user_auth_tokens_item",
    "GetUserResponseUserUserFields": ".get_user_response_user_user_fields",
    "GetUserResponseUserUserNotificationSchedule": ".get_user_response_user_user_notification_schedule",
    "GetUserResponseUserUserOption": ".get_user_response_user_user_option",
    "ListUserActionsResponse": ".list_user_actions_response",
    "ListUserActionsResponseUserActionsItem": ".list_user_actions_response_user_actions_item",
    "ListUsersPublicRequestAsc": ".list_users_public_request_asc",
    "ListUsersPublicRequestOrder": ".list_users_public_request_order",
    "ListUsersPublicRequestPeriod": ".list_users_public_request_period",
    "ListUsersPublicResponse": ".list_users_public_response",
    "ListUsersPublicResponseDirectoryItemsItem": ".list_users_public_response_directory_items_item",
    "ListUsersPublicResponseDirectoryItemsItemUser": ".list_users_public_response_directory_items_item_user",
    "ListUsersPublicResponseMeta": ".list_users_public_response_meta",
    "LogOutUserResponse": ".log_out_user_response",
    "RefreshGravatarResponse": ".refresh_gravatar_response",
    "SendPasswordResetEmailResponse": ".send_password_reset_email_response",
    "SilenceUserResponse": ".silence_user_response",
    "SilenceUserResponseSilence": ".silence_user_response_silence",
    "SilenceUserResponseSilenceSilencedBy": ".silence_user_response_silence_silenced_by",
    "SuspendUserResponse": ".suspend_user_response",
    "SuspendUserResponseSuspension": ".suspend_user_response_suspension",
    "SuspendUserResponseSuspensionSuspendedBy": ".suspend_user_response_suspension_suspended_by",
    "UpdateAvatarRequestType": ".update_avatar_request_type",
    "UpdateAvatarResponse": ".update_avatar_response",
    "UpdateUserResponse": ".update_user_response",
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
    "AdminGetUserResponse",
    "AdminGetUserResponseApprovedBy",
    "AdminGetUserResponseGroupsItem",
    "AdminGetUserResponsePenaltyCounts",
    "AdminGetUserResponseTl3Requirements",
    "AdminGetUserResponseTl3RequirementsPenaltyCounts",
    "AdminListUsersRequestAsc",
    "AdminListUsersRequestFlag",
    "AdminListUsersRequestOrder",
    "AdminListUsersResponseItem",
    "AnonymizeUserResponse",
    "CreateUserResponse",
    "DeleteUserResponse",
    "GetUserEmailsResponse",
    "GetUserExternalIdResponse",
    "GetUserExternalIdResponseUser",
    "GetUserExternalIdResponseUserCustomFields",
    "GetUserExternalIdResponseUserGroupUsersItem",
    "GetUserExternalIdResponseUserGroupsItem",
    "GetUserExternalIdResponseUserUserAuthTokensItem",
    "GetUserExternalIdResponseUserUserFields",
    "GetUserExternalIdResponseUserUserNotificationSchedule",
    "GetUserExternalIdResponseUserUserOption",
    "GetUserIdentiyProviderExternalIdResponse",
    "GetUserIdentiyProviderExternalIdResponseUser",
    "GetUserIdentiyProviderExternalIdResponseUserCustomFields",
    "GetUserIdentiyProviderExternalIdResponseUserGroupUsersItem",
    "GetUserIdentiyProviderExternalIdResponseUserGroupsItem",
    "GetUserIdentiyProviderExternalIdResponseUserUserAuthTokensItem",
    "GetUserIdentiyProviderExternalIdResponseUserUserFields",
    "GetUserIdentiyProviderExternalIdResponseUserUserNotificationSchedule",
    "GetUserIdentiyProviderExternalIdResponseUserUserOption",
    "GetUserResponse",
    "GetUserResponseUser",
    "GetUserResponseUserCustomFields",
    "GetUserResponseUserGroupUsersItem",
    "GetUserResponseUserGroupsItem",
    "GetUserResponseUserUserAuthTokensItem",
    "GetUserResponseUserUserFields",
    "GetUserResponseUserUserNotificationSchedule",
    "GetUserResponseUserUserOption",
    "ListUserActionsResponse",
    "ListUserActionsResponseUserActionsItem",
    "ListUsersPublicRequestAsc",
    "ListUsersPublicRequestOrder",
    "ListUsersPublicRequestPeriod",
    "ListUsersPublicResponse",
    "ListUsersPublicResponseDirectoryItemsItem",
    "ListUsersPublicResponseDirectoryItemsItemUser",
    "ListUsersPublicResponseMeta",
    "LogOutUserResponse",
    "RefreshGravatarResponse",
    "SendPasswordResetEmailResponse",
    "SilenceUserResponse",
    "SilenceUserResponseSilence",
    "SilenceUserResponseSilenceSilencedBy",
    "SuspendUserResponse",
    "SuspendUserResponseSuspension",
    "SuspendUserResponseSuspensionSuspendedBy",
    "UpdateAvatarRequestType",
    "UpdateAvatarResponse",
    "UpdateUserResponse",
]
