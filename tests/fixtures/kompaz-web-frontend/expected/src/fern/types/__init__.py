



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .authentication_resource import AuthenticationResource
    from .authentication_resource_token_type import AuthenticationResourceTokenType
    from .authentication_resource_user import AuthenticationResourceUser
    from .bad_request_error_body import BadRequestErrorBody
    from .not_found_error_body import NotFoundErrorBody
    from .organization_resource import OrganizationResource
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .user_resource import UserResource
    from .user_role import UserRole
    from .user_status import UserStatus
_dynamic_imports: typing.Dict[str, str] = {
    "AuthenticationResource": ".authentication_resource",
    "AuthenticationResourceTokenType": ".authentication_resource_token_type",
    "AuthenticationResourceUser": ".authentication_resource_user",
    "BadRequestErrorBody": ".bad_request_error_body",
    "NotFoundErrorBody": ".not_found_error_body",
    "OrganizationResource": ".organization_resource",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UserResource": ".user_resource",
    "UserRole": ".user_role",
    "UserStatus": ".user_status",
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
    "AuthenticationResource",
    "AuthenticationResourceTokenType",
    "AuthenticationResourceUser",
    "BadRequestErrorBody",
    "NotFoundErrorBody",
    "OrganizationResource",
    "UnauthorizedErrorBody",
    "UserResource",
    "UserRole",
    "UserStatus",
]
