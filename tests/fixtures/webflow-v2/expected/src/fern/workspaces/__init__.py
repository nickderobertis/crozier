



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from . import audit_logs
    from .audit_logs import (
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
    "CustomRole": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsRequestEventType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsRequestSortOrder": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponse": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemActor": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRole": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemCustomRoleEventSubType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembership": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemSiteMembershipEventSubType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccess": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemUserAccessEventSubType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspace": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitation": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceInvitationEventSubType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembership": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceMembershipEventSubType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSetting": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItemWorkspaceSettingEventSubType": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_CustomRole": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_SiteMembership": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_UserAccess": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceInvitation": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceMembership": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponseItemsItem_WorkspaceSetting": ".audit_logs",
    "GetWorkspaceAuditLogsAuditLogsResponsePagination": ".audit_logs",
    "SettingChange": ".audit_logs",
    "SettingChangeMethod": ".audit_logs",
    "SettingChangeSetting": ".audit_logs",
    "SiteMembership": ".audit_logs",
    "SiteMembershipGranularAccess": ".audit_logs",
    "SiteMembershipGranularAccessType": ".audit_logs",
    "SiteMembershipMethod": ".audit_logs",
    "SiteMembershipSite": ".audit_logs",
    "SiteMembershipTargetUser": ".audit_logs",
    "SiteMembershipUserType": ".audit_logs",
    "UserAccess": ".audit_logs",
    "UserAccessMethod": ".audit_logs",
    "WorkspaceInvitation": ".audit_logs",
    "WorkspaceInvitationMethod": ".audit_logs",
    "WorkspaceInvitationTargetUser": ".audit_logs",
    "WorkspaceInvitationTargetUsersItem": ".audit_logs",
    "WorkspaceInvitationUserType": ".audit_logs",
    "WorkspaceMembership": ".audit_logs",
    "WorkspaceMembershipMethod": ".audit_logs",
    "WorkspaceMembershipTargetUser": ".audit_logs",
    "WorkspaceMembershipUserType": ".audit_logs",
    "audit_logs": ".audit_logs",
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
    "audit_logs",
]
