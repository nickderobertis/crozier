



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .workspace_api_ocs_add_user_as_workspace_manager_response import (
        WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
    )
    from .workspace_api_ocs_add_user_as_workspace_manager_response_ocs import (
        WorkspaceApiOcsAddUserAsWorkspaceManagerResponseOcs,
    )
    from .workspace_api_ocs_add_users_in_workspace_response import WorkspaceApiOcsAddUsersInWorkspaceResponse
    from .workspace_api_ocs_add_users_in_workspace_response_ocs import WorkspaceApiOcsAddUsersInWorkspaceResponseOcs
    from .workspace_api_ocs_add_users_to_group_response import WorkspaceApiOcsAddUsersToGroupResponse
    from .workspace_api_ocs_add_users_to_group_response_ocs import WorkspaceApiOcsAddUsersToGroupResponseOcs
    from .workspace_api_ocs_find_users_by_id_response import WorkspaceApiOcsFindUsersByIdResponse
    from .workspace_api_ocs_find_users_by_id_response_ocs import WorkspaceApiOcsFindUsersByIdResponseOcs
_dynamic_imports: typing.Dict[str, str] = {
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponse": ".workspace_api_ocs_add_user_as_workspace_manager_response",
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponseOcs": ".workspace_api_ocs_add_user_as_workspace_manager_response_ocs",
    "WorkspaceApiOcsAddUsersInWorkspaceResponse": ".workspace_api_ocs_add_users_in_workspace_response",
    "WorkspaceApiOcsAddUsersInWorkspaceResponseOcs": ".workspace_api_ocs_add_users_in_workspace_response_ocs",
    "WorkspaceApiOcsAddUsersToGroupResponse": ".workspace_api_ocs_add_users_to_group_response",
    "WorkspaceApiOcsAddUsersToGroupResponseOcs": ".workspace_api_ocs_add_users_to_group_response_ocs",
    "WorkspaceApiOcsFindUsersByIdResponse": ".workspace_api_ocs_find_users_by_id_response",
    "WorkspaceApiOcsFindUsersByIdResponseOcs": ".workspace_api_ocs_find_users_by_id_response_ocs",
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
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponse",
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponseOcs",
    "WorkspaceApiOcsAddUsersInWorkspaceResponse",
    "WorkspaceApiOcsAddUsersInWorkspaceResponseOcs",
    "WorkspaceApiOcsAddUsersToGroupResponse",
    "WorkspaceApiOcsAddUsersToGroupResponseOcs",
    "WorkspaceApiOcsFindUsersByIdResponse",
    "WorkspaceApiOcsFindUsersByIdResponseOcs",
]
