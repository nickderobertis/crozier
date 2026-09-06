



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CustomRole,
        GetWorkspaceAuditLogsAuditLogsRequestEventType,
        GetWorkspaceAuditLogsAuditLogsRequestSortOrder,
        GetWorkspaceAuditLogsAuditLogsResponse,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRole,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccess,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitation,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSetting,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership,
        GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting,
        GetWorkspaceAuditLogsAuditLogsResponsePagination,
        SettingChange,
        SettingChangeMethod,
        SettingChangeSetting,
        SiteMembership,
        SiteMembershipGranularAccess,
        SiteMembershipGranularAccessType,
        SiteMembershipMethod,
        SiteMembershipSite,
        SiteMembershipTargetUser,
        SiteMembershipUserType,
        UserAccess,
        UserAccessMethod,
        WorkspaceInvitation,
        WorkspaceInvitationMethod,
        WorkspaceInvitationTargetUser,
        WorkspaceInvitationTargetUsersItem,
        WorkspaceInvitationUserType,
        WorkspaceMembership,
        WorkspaceMembershipMethod,
        WorkspaceMembershipTargetUser,
        WorkspaceMembershipUserType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CustomRole": ".types",
    "GetWorkspaceAuditLogsAuditLogsRequestEventType": ".types",
    "GetWorkspaceAuditLogsAuditLogsRequestSortOrder": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponse": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRole": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccess": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitation": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembership": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSetting": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting": ".types",
    "GetWorkspaceAuditLogsAuditLogsResponsePagination": ".types",
    "SettingChange": ".types",
    "SettingChangeMethod": ".types",
    "SettingChangeSetting": ".types",
    "SiteMembership": ".types",
    "SiteMembershipGranularAccess": ".types",
    "SiteMembershipGranularAccessType": ".types",
    "SiteMembershipMethod": ".types",
    "SiteMembershipSite": ".types",
    "SiteMembershipTargetUser": ".types",
    "SiteMembershipUserType": ".types",
    "UserAccess": ".types",
    "UserAccessMethod": ".types",
    "WorkspaceInvitation": ".types",
    "WorkspaceInvitationMethod": ".types",
    "WorkspaceInvitationTargetUser": ".types",
    "WorkspaceInvitationTargetUsersItem": ".types",
    "WorkspaceInvitationUserType": ".types",
    "WorkspaceMembership": ".types",
    "WorkspaceMembershipMethod": ".types",
    "WorkspaceMembershipTargetUser": ".types",
    "WorkspaceMembershipUserType": ".types",
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
