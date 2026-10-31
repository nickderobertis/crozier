



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AuthenticationResource,
        AuthenticationResourceTokenType,
        AuthenticationResourceUser,
        BadRequestErrorBody,
        NotFoundErrorBody,
        OrganizationResource,
        UnauthorizedErrorBody,
        UserResource,
        UserRole,
        UserStatus,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import auth, organization, organizationlogo, user
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .auth import AuthMeResponse
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .organization import OrganizationIndexResponse
    from .user import (
        UserIndexResponse,
        UserInviteResponse,
        UserRestoreResponse,
        UserShowResponse,
        UserUpdateOwnProfileResponse,
        UserUpdateResponse,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "AuthMeResponse": ".auth",
    "AuthenticationResource": ".types",
    "AuthenticationResourceTokenType": ".types",
    "AuthenticationResourceUser": ".types",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "NotFoundError": ".errors",
    "NotFoundErrorBody": ".types",
    "OrganizationIndexResponse": ".organization",
    "OrganizationResource": ".types",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "UserIndexResponse": ".user",
    "UserInviteResponse": ".user",
    "UserResource": ".types",
    "UserRestoreResponse": ".user",
    "UserRole": ".types",
    "UserShowResponse": ".user",
    "UserStatus": ".types",
    "UserUpdateOwnProfileResponse": ".user",
    "UserUpdateResponse": ".user",
    "__version__": ".version",
    "auth": ".auth",
    "organization": ".organization",
    "organizationlogo": ".organizationlogo",
    "user": ".user",
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
    "AuthMeResponse",
    "AuthenticationResource",
    "AuthenticationResourceTokenType",
    "AuthenticationResourceUser",
    "BadRequestError",
    "BadRequestErrorBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "NotFoundError",
    "NotFoundErrorBody",
    "OrganizationIndexResponse",
    "OrganizationResource",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "UserIndexResponse",
    "UserInviteResponse",
    "UserResource",
    "UserRestoreResponse",
    "UserRole",
    "UserShowResponse",
    "UserStatus",
    "UserUpdateOwnProfileResponse",
    "UserUpdateResponse",
    "__version__",
    "auth",
    "organization",
    "organizationlogo",
    "user",
]
