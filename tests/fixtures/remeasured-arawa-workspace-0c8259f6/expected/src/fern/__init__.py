



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestErrorBody,
        BadRequestErrorBodyOcs,
        Capabilities,
        CapabilitiesWorkspace,
        ConfirmationMessage,
        ConflictErrorBody,
        ConflictErrorBodyOcs,
        FindGroups,
        ForbiddenErrorBody,
        ForbiddenErrorBodyOcs,
        GroupInfo,
        NotFoundErrorBody,
        NotFoundErrorBodyOcs,
        OcsMeta,
        Space,
        UnauthorizedErrorBody,
        UnauthorizedErrorBodyOcs,
        UserDefinition,
        UsersList,
    )
    from .errors import BadRequestError, ConflictError, ForbiddenError, NotFoundError, UnauthorizedError
    from . import workspace, workspace_groups, workspace_users
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
    from .workspace import (
        WorkspaceApiOcsCreateResponse,
        WorkspaceApiOcsCreateResponseOcs,
        WorkspaceApiOcsEditResponse,
        WorkspaceApiOcsEditResponseOcs,
        WorkspaceApiOcsFindAllResponse,
        WorkspaceApiOcsFindAllResponseOcs,
        WorkspaceApiOcsFindResponse,
        WorkspaceApiOcsFindResponseOcs,
    )
    from .workspace_groups import (
        WorkspaceApiOcsCreateSubGroupResponse,
        WorkspaceApiOcsCreateSubGroupResponseOcs,
        WorkspaceApiOcsFindGroupsBySpaceIdResponse,
        WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs,
    )
    from .workspace_users import (
        WorkspaceApiOcsAddUserAsWorkspaceManagerResponse,
        WorkspaceApiOcsAddUserAsWorkspaceManagerResponseOcs,
        WorkspaceApiOcsAddUsersInWorkspaceResponse,
        WorkspaceApiOcsAddUsersInWorkspaceResponseOcs,
        WorkspaceApiOcsAddUsersToGroupResponse,
        WorkspaceApiOcsAddUsersToGroupResponseOcs,
        WorkspaceApiOcsFindUsersByIdResponse,
        WorkspaceApiOcsFindUsersByIdResponseOcs,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "BadRequestErrorBodyOcs": ".types",
    "Capabilities": ".types",
    "CapabilitiesWorkspace": ".types",
    "ConfirmationMessage": ".types",
    "ConflictError": ".errors",
    "ConflictErrorBody": ".types",
    "ConflictErrorBodyOcs": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FindGroups": ".types",
    "ForbiddenError": ".errors",
    "ForbiddenErrorBody": ".types",
    "ForbiddenErrorBodyOcs": ".types",
    "GroupInfo": ".types",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "NotFoundErrorBodyOcs": ".types",
    "OcsMeta": ".types",
    "Space": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "UnauthorizedErrorBodyOcs": ".types",
    "UserDefinition": ".types",
    "UsersList": ".types",
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponse": ".workspace_users",
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponseOcs": ".workspace_users",
    "WorkspaceApiOcsAddUsersInWorkspaceResponse": ".workspace_users",
    "WorkspaceApiOcsAddUsersInWorkspaceResponseOcs": ".workspace_users",
    "WorkspaceApiOcsAddUsersToGroupResponse": ".workspace_users",
    "WorkspaceApiOcsAddUsersToGroupResponseOcs": ".workspace_users",
    "WorkspaceApiOcsCreateResponse": ".workspace",
    "WorkspaceApiOcsCreateResponseOcs": ".workspace",
    "WorkspaceApiOcsCreateSubGroupResponse": ".workspace_groups",
    "WorkspaceApiOcsCreateSubGroupResponseOcs": ".workspace_groups",
    "WorkspaceApiOcsEditResponse": ".workspace",
    "WorkspaceApiOcsEditResponseOcs": ".workspace",
    "WorkspaceApiOcsFindAllResponse": ".workspace",
    "WorkspaceApiOcsFindAllResponseOcs": ".workspace",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponse": ".workspace_groups",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs": ".workspace_groups",
    "WorkspaceApiOcsFindResponse": ".workspace",
    "WorkspaceApiOcsFindResponseOcs": ".workspace",
    "WorkspaceApiOcsFindUsersByIdResponse": ".workspace_users",
    "WorkspaceApiOcsFindUsersByIdResponseOcs": ".workspace_users",
    "__version__": ".version",
    "workspace": ".workspace",
    "workspace_groups": ".workspace_groups",
    "workspace_users": ".workspace_users",
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
    "AsyncFernApi",
    "BadRequestError",
    "BadRequestErrorBody",
    "BadRequestErrorBodyOcs",
    "Capabilities",
    "CapabilitiesWorkspace",
    "ConfirmationMessage",
    "ConflictError",
    "ConflictErrorBody",
    "ConflictErrorBodyOcs",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FindGroups",
    "ForbiddenError",
    "ForbiddenErrorBody",
    "ForbiddenErrorBodyOcs",
    "GroupInfo",
    "NotFoundError",
    "NotFoundErrorBody",
    "NotFoundErrorBodyOcs",
    "OcsMeta",
    "Space",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "UnauthorizedErrorBodyOcs",
    "UserDefinition",
    "UsersList",
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponse",
    "WorkspaceApiOcsAddUserAsWorkspaceManagerResponseOcs",
    "WorkspaceApiOcsAddUsersInWorkspaceResponse",
    "WorkspaceApiOcsAddUsersInWorkspaceResponseOcs",
    "WorkspaceApiOcsAddUsersToGroupResponse",
    "WorkspaceApiOcsAddUsersToGroupResponseOcs",
    "WorkspaceApiOcsCreateResponse",
    "WorkspaceApiOcsCreateResponseOcs",
    "WorkspaceApiOcsCreateSubGroupResponse",
    "WorkspaceApiOcsCreateSubGroupResponseOcs",
    "WorkspaceApiOcsEditResponse",
    "WorkspaceApiOcsEditResponseOcs",
    "WorkspaceApiOcsFindAllResponse",
    "WorkspaceApiOcsFindAllResponseOcs",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponse",
    "WorkspaceApiOcsFindGroupsBySpaceIdResponseOcs",
    "WorkspaceApiOcsFindResponse",
    "WorkspaceApiOcsFindResponseOcs",
    "WorkspaceApiOcsFindUsersByIdResponse",
    "WorkspaceApiOcsFindUsersByIdResponseOcs",
    "__version__",
    "workspace",
    "workspace_groups",
    "workspace_users",
]
