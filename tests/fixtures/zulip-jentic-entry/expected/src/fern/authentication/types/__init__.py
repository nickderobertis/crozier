



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dev_list_users_response import DevListUsersResponse
    from .dev_list_users_response_direct_admins_item import DevListUsersResponseDirectAdminsItem
    from .dev_list_users_response_direct_users_item import DevListUsersResponseDirectUsersItem
    from .jwt_fetch_api_key_response import JwtFetchApiKeyResponse
    from .jwt_fetch_api_key_response_user import JwtFetchApiKeyResponseUser
_dynamic_imports: typing.Dict[str, str] = {
    "DevListUsersResponse": ".dev_list_users_response",
    "DevListUsersResponseDirectAdminsItem": ".dev_list_users_response_direct_admins_item",
    "DevListUsersResponseDirectUsersItem": ".dev_list_users_response_direct_users_item",
    "JwtFetchApiKeyResponse": ".jwt_fetch_api_key_response",
    "JwtFetchApiKeyResponseUser": ".jwt_fetch_api_key_response_user",
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
    "DevListUsersResponse",
    "DevListUsersResponseDirectAdminsItem",
    "DevListUsersResponseDirectUsersItem",
    "JwtFetchApiKeyResponse",
    "JwtFetchApiKeyResponseUser",
]
