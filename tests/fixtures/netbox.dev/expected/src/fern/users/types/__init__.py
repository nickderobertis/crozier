



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .users_groups_list_response import UsersGroupsListResponse
    from .users_permissions_list_response import UsersPermissionsListResponse
    from .users_tokens_list_response import UsersTokensListResponse
    from .users_users_list_response import UsersUsersListResponse
_dynamic_imports: typing.Dict[str, str] = {
    "UsersGroupsListResponse": ".users_groups_list_response",
    "UsersPermissionsListResponse": ".users_permissions_list_response",
    "UsersTokensListResponse": ".users_tokens_list_response",
    "UsersUsersListResponse": ".users_users_list_response",
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
    "UsersGroupsListResponse",
    "UsersPermissionsListResponse",
    "UsersTokensListResponse",
    "UsersUsersListResponse",
]
