



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .custom_role import CustomRole
    from .get_workspace_audit_logs_audit_logs_request_event_type import GetWorkspaceAuditLogsAuditLogsRequestEventType
    from .get_workspace_audit_logs_audit_logs_request_sort_order import GetWorkspaceAuditLogsAuditLogsRequestSortOrder
    from .get_workspace_audit_logs_audit_logs_response import GetWorkspaceAuditLogsAuditLogsResponse
    from .get_workspace_audit_logs_audit_logs_response_items_item import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_actor import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_custom_role import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRole,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_custom_role_event_sub_type import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_site_membership import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_site_membership_event_sub_type import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_user_access import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccess,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_user_access_event_sub_type import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitation,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation_event_sub_type import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembership,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership_event_sub_type import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSetting,
    )
    from .get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting_event_sub_type import (
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType,
    )
    from .get_workspace_audit_logs_audit_logs_response_pagination import (
        GetWorkspaceAuditLogsAuditLogsResponsePagination,
    )
    from .setting_change import SettingChange
    from .setting_change_method import SettingChangeMethod
    from .setting_change_setting import SettingChangeSetting
    from .site_membership import SiteMembership
    from .site_membership_granular_access import SiteMembershipGranularAccess
    from .site_membership_granular_access_type import SiteMembershipGranularAccessType
    from .site_membership_method import SiteMembershipMethod
    from .site_membership_site import SiteMembershipSite
    from .site_membership_target_user import SiteMembershipTargetUser
    from .site_membership_user_type import SiteMembershipUserType
    from .user_access import UserAccess
    from .user_access_method import UserAccessMethod
    from .workspace_invitation import WorkspaceInvitation
    from .workspace_invitation_method import WorkspaceInvitationMethod
    from .workspace_invitation_target_user import WorkspaceInvitationTargetUser
    from .workspace_invitation_target_users_item import WorkspaceInvitationTargetUsersItem
    from .workspace_invitation_user_type import WorkspaceInvitationUserType
    from .workspace_membership import WorkspaceMembership
    from .workspace_membership_method import WorkspaceMembershipMethod
    from .workspace_membership_target_user import WorkspaceMembershipTargetUser
    from .workspace_membership_user_type import WorkspaceMembershipUserType
_dynamic_imports: typing.Dict[str, str] = {
    "CustomRole": ".custom_role",
    "GetWorkspaceAuditLogsAuditLogsRequestEventType": ".get_workspace_audit_logs_audit_logs_request_event_type",
    "GetWorkspaceAuditLogsAuditLogsRequestSortOrder": ".get_workspace_audit_logs_audit_logs_request_sort_order",
    "GetWorkspaceAuditLogsAuditLogsResponse": ".get_workspace_audit_logs_audit_logs_response",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor": ".get_workspace_audit_logs_audit_logs_response_items_item_actor",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRole": ".get_workspace_audit_logs_audit_logs_response_items_item_custom_role",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType": ".get_workspace_audit_logs_audit_logs_response_items_item_custom_role_event_sub_type",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership": ".get_workspace_audit_logs_audit_logs_response_items_item_site_membership",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType": ".get_workspace_audit_logs_audit_logs_response_items_item_site_membership_event_sub_type",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccess": ".get_workspace_audit_logs_audit_logs_response_items_item_user_access",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType": ".get_workspace_audit_logs_audit_logs_response_items_item_user_access_event_sub_type",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitation": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace_invitation_event_sub_type",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembership": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace_membership_event_sub_type",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSetting": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType": ".get_workspace_audit_logs_audit_logs_response_items_item_workspace_setting_event_sub_type",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting": ".get_workspace_audit_logs_audit_logs_response_items_item",
    "GetWorkspaceAuditLogsAuditLogsResponsePagination": ".get_workspace_audit_logs_audit_logs_response_pagination",
    "SettingChange": ".setting_change",
    "SettingChangeMethod": ".setting_change_method",
    "SettingChangeSetting": ".setting_change_setting",
    "SiteMembership": ".site_membership",
    "SiteMembershipGranularAccess": ".site_membership_granular_access",
    "SiteMembershipGranularAccessType": ".site_membership_granular_access_type",
    "SiteMembershipMethod": ".site_membership_method",
    "SiteMembershipSite": ".site_membership_site",
    "SiteMembershipTargetUser": ".site_membership_target_user",
    "SiteMembershipUserType": ".site_membership_user_type",
    "UserAccess": ".user_access",
    "UserAccessMethod": ".user_access_method",
    "WorkspaceInvitation": ".workspace_invitation",
    "WorkspaceInvitationMethod": ".workspace_invitation_method",
    "WorkspaceInvitationTargetUser": ".workspace_invitation_target_user",
    "WorkspaceInvitationTargetUsersItem": ".workspace_invitation_target_users_item",
    "WorkspaceInvitationUserType": ".workspace_invitation_user_type",
    "WorkspaceMembership": ".workspace_membership",
    "WorkspaceMembershipMethod": ".workspace_membership_method",
    "WorkspaceMembershipTargetUser": ".workspace_membership_target_user",
    "WorkspaceMembershipUserType": ".workspace_membership_user_type",
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
    "CustomRole",
    "GetWorkspaceAuditLogsAuditLogsRequestEventType",
    "GetWorkspaceAuditLogsAuditLogsRequestSortOrder",
    "GetWorkspaceAuditLogsAuditLogsResponse",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRole",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccess",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitation",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembership",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSetting",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting",
    "GetWorkspaceAuditLogsAuditLogsResponsePagination",
    "SettingChange",
    "SettingChangeMethod",
    "SettingChangeSetting",
    "SiteMembership",
    "SiteMembershipGranularAccess",
    "SiteMembershipGranularAccessType",
    "SiteMembershipMethod",
    "SiteMembershipSite",
    "SiteMembershipTargetUser",
    "SiteMembershipUserType",
    "UserAccess",
    "UserAccessMethod",
    "WorkspaceInvitation",
    "WorkspaceInvitationMethod",
    "WorkspaceInvitationTargetUser",
    "WorkspaceInvitationTargetUsersItem",
    "WorkspaceInvitationUserType",
    "WorkspaceMembership",
    "WorkspaceMembershipMethod",
    "WorkspaceMembershipTargetUser",
    "WorkspaceMembershipUserType",
]
