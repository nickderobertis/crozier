



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AuthToken,
        BuildSecrets,
        CheckServerResponse,
        ClientProfile,
        CompletedProfile,
        ErrorResponse,
        FileUploadResponse,
        HashedDir,
        LauncherUpdateInfo,
        ListProfilesResponse,
        SelfUser,
        Texture,
        UncompletedProfile,
        UpdateInfo,
        UpdatesPrepareResponse,
        User,
        UserPermissions,
    )
    from . import auth, profile_management, profiles, updates, users
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .updates import PostUpdatesCheckVariantRequestVariant, PostUpdatesUploadVariantRequestVariant
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "AuthToken": ".types",
    "BuildSecrets": ".types",
    "CheckServerResponse": ".types",
    "ClientProfile": ".types",
    "CompletedProfile": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FileUploadResponse": ".types",
    "HashedDir": ".types",
    "LauncherUpdateInfo": ".types",
    "ListProfilesResponse": ".types",
    "PostUpdatesCheckVariantRequestVariant": ".updates",
    "PostUpdatesUploadVariantRequestVariant": ".updates",
    "SelfUser": ".types",
    "Texture": ".types",
    "UncompletedProfile": ".types",
    "UpdateInfo": ".types",
    "UpdatesPrepareResponse": ".types",
    "User": ".types",
    "UserPermissions": ".types",
    "__version__": ".version",
    "auth": ".auth",
    "profile_management": ".profile_management",
    "profiles": ".profiles",
    "updates": ".updates",
    "users": ".users",
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
    "AuthToken",
    "BuildSecrets",
    "CheckServerResponse",
    "ClientProfile",
    "CompletedProfile",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "FernApiEnvironment",
    "FileUploadResponse",
    "HashedDir",
    "LauncherUpdateInfo",
    "ListProfilesResponse",
    "PostUpdatesCheckVariantRequestVariant",
    "PostUpdatesUploadVariantRequestVariant",
    "SelfUser",
    "Texture",
    "UncompletedProfile",
    "UpdateInfo",
    "UpdatesPrepareResponse",
    "User",
    "UserPermissions",
    "__version__",
    "auth",
    "profile_management",
    "profiles",
    "updates",
    "users",
]
