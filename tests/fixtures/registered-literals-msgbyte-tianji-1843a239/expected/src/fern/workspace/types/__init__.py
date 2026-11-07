



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .workspace_create_response import WorkspaceCreateResponse
    from .workspace_create_response_workspaces_item import WorkspaceCreateResponseWorkspacesItem
    from .workspace_create_response_workspaces_item_workspace import WorkspaceCreateResponseWorkspacesItemWorkspace
    from .workspace_get_service_count_response import WorkspaceGetServiceCountResponse
    from .workspace_invite_request_role import WorkspaceInviteRequestRole
    from .workspace_members_response_item import WorkspaceMembersResponseItem
    from .workspace_members_response_item_user import WorkspaceMembersResponseItemUser
    from .workspace_rename_response import WorkspaceRenameResponse
    from .workspace_switch_response import WorkspaceSwitchResponse
    from .workspace_switch_response_workspaces_item import WorkspaceSwitchResponseWorkspacesItem
    from .workspace_switch_response_workspaces_item_workspace import WorkspaceSwitchResponseWorkspacesItemWorkspace
    from .workspace_update_member_role_request_role import WorkspaceUpdateMemberRoleRequestRole
    from .workspace_update_settings_response import WorkspaceUpdateSettingsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "WorkspaceCreateResponse": ".workspace_create_response",
    "WorkspaceCreateResponseWorkspacesItem": ".workspace_create_response_workspaces_item",
    "WorkspaceCreateResponseWorkspacesItemWorkspace": ".workspace_create_response_workspaces_item_workspace",
    "WorkspaceGetServiceCountResponse": ".workspace_get_service_count_response",
    "WorkspaceInviteRequestRole": ".workspace_invite_request_role",
    "WorkspaceMembersResponseItem": ".workspace_members_response_item",
    "WorkspaceMembersResponseItemUser": ".workspace_members_response_item_user",
    "WorkspaceRenameResponse": ".workspace_rename_response",
    "WorkspaceSwitchResponse": ".workspace_switch_response",
    "WorkspaceSwitchResponseWorkspacesItem": ".workspace_switch_response_workspaces_item",
    "WorkspaceSwitchResponseWorkspacesItemWorkspace": ".workspace_switch_response_workspaces_item_workspace",
    "WorkspaceUpdateMemberRoleRequestRole": ".workspace_update_member_role_request_role",
    "WorkspaceUpdateSettingsResponse": ".workspace_update_settings_response",
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
    "WorkspaceCreateResponse",
    "WorkspaceCreateResponseWorkspacesItem",
    "WorkspaceCreateResponseWorkspacesItemWorkspace",
    "WorkspaceGetServiceCountResponse",
    "WorkspaceInviteRequestRole",
    "WorkspaceMembersResponseItem",
    "WorkspaceMembersResponseItemUser",
    "WorkspaceRenameResponse",
    "WorkspaceSwitchResponse",
    "WorkspaceSwitchResponseWorkspacesItem",
    "WorkspaceSwitchResponseWorkspacesItemWorkspace",
    "WorkspaceUpdateMemberRoleRequestRole",
    "WorkspaceUpdateSettingsResponse",
]
