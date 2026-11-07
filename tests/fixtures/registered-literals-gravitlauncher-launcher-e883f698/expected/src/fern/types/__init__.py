



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .auth_token import AuthToken
    from .build_secrets import BuildSecrets
    from .check_server_response import CheckServerResponse
    from .client_profile import ClientProfile
    from .completed_profile import CompletedProfile
    from .error_response import ErrorResponse
    from .file_upload_response import FileUploadResponse
    from .hashed_dir import HashedDir
    from .launcher_update_info import LauncherUpdateInfo
    from .list_profiles_response import ListProfilesResponse
    from .self_user import SelfUser
    from .texture import Texture
    from .uncompleted_profile import UncompletedProfile
    from .update_info import UpdateInfo
    from .updates_prepare_response import UpdatesPrepareResponse
    from .user import User
    from .user_permissions import UserPermissions
_dynamic_imports: typing.Dict[str, str] = {
    "AuthToken": ".auth_token",
    "BuildSecrets": ".build_secrets",
    "CheckServerResponse": ".check_server_response",
    "ClientProfile": ".client_profile",
    "CompletedProfile": ".completed_profile",
    "ErrorResponse": ".error_response",
    "FileUploadResponse": ".file_upload_response",
    "HashedDir": ".hashed_dir",
    "LauncherUpdateInfo": ".launcher_update_info",
    "ListProfilesResponse": ".list_profiles_response",
    "SelfUser": ".self_user",
    "Texture": ".texture",
    "UncompletedProfile": ".uncompleted_profile",
    "UpdateInfo": ".update_info",
    "UpdatesPrepareResponse": ".updates_prepare_response",
    "User": ".user",
    "UserPermissions": ".user_permissions",
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
    "AuthToken",
    "BuildSecrets",
    "CheckServerResponse",
    "ClientProfile",
    "CompletedProfile",
    "ErrorResponse",
    "FileUploadResponse",
    "HashedDir",
    "LauncherUpdateInfo",
    "ListProfilesResponse",
    "SelfUser",
    "Texture",
    "UncompletedProfile",
    "UpdateInfo",
    "UpdatesPrepareResponse",
    "User",
    "UserPermissions",
]
