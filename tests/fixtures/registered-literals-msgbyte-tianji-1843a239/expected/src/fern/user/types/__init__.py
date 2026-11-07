



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .user_login_response import UserLoginResponse
    from .user_login_response_info import UserLoginResponseInfo
    from .user_login_response_info_workspaces_item import UserLoginResponseInfoWorkspacesItem
    from .user_login_response_info_workspaces_item_workspace import UserLoginResponseInfoWorkspacesItemWorkspace
    from .user_login_with_token_response import UserLoginWithTokenResponse
    from .user_login_with_token_response_info import UserLoginWithTokenResponseInfo
    from .user_login_with_token_response_info_workspaces_item import UserLoginWithTokenResponseInfoWorkspacesItem
    from .user_login_with_token_response_info_workspaces_item_workspace import (
        UserLoginWithTokenResponseInfoWorkspacesItemWorkspace,
    )
    from .user_register_response import UserRegisterResponse
    from .user_register_response_info import UserRegisterResponseInfo
    from .user_register_response_info_workspaces_item import UserRegisterResponseInfoWorkspacesItem
    from .user_register_response_info_workspaces_item_workspace import UserRegisterResponseInfoWorkspacesItemWorkspace
_dynamic_imports: typing.Dict[str, str] = {
    "UserLoginResponse": ".user_login_response",
    "UserLoginResponseInfo": ".user_login_response_info",
    "UserLoginResponseInfoWorkspacesItem": ".user_login_response_info_workspaces_item",
    "UserLoginResponseInfoWorkspacesItemWorkspace": ".user_login_response_info_workspaces_item_workspace",
    "UserLoginWithTokenResponse": ".user_login_with_token_response",
    "UserLoginWithTokenResponseInfo": ".user_login_with_token_response_info",
    "UserLoginWithTokenResponseInfoWorkspacesItem": ".user_login_with_token_response_info_workspaces_item",
    "UserLoginWithTokenResponseInfoWorkspacesItemWorkspace": ".user_login_with_token_response_info_workspaces_item_workspace",
    "UserRegisterResponse": ".user_register_response",
    "UserRegisterResponseInfo": ".user_register_response_info",
    "UserRegisterResponseInfoWorkspacesItem": ".user_register_response_info_workspaces_item",
    "UserRegisterResponseInfoWorkspacesItemWorkspace": ".user_register_response_info_workspaces_item_workspace",
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
    "UserLoginResponse",
    "UserLoginResponseInfo",
    "UserLoginResponseInfoWorkspacesItem",
    "UserLoginResponseInfoWorkspacesItemWorkspace",
    "UserLoginWithTokenResponse",
    "UserLoginWithTokenResponseInfo",
    "UserLoginWithTokenResponseInfoWorkspacesItem",
    "UserLoginWithTokenResponseInfoWorkspacesItemWorkspace",
    "UserRegisterResponse",
    "UserRegisterResponseInfo",
    "UserRegisterResponseInfoWorkspacesItem",
    "UserRegisterResponseInfoWorkspacesItemWorkspace",
]
