



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateUserRequestRole,
        CreateUserResponse,
        CreateUserResponseRole,
        GetUsersRequestFilterDateField,
        GetUsersRequestOrder,
        GetUsersRequestSortBy,
        GetUsersResponse,
        GetUsersResponseDataItem,
        GetUsersResponseDataItemRole,
        GetUsersResponseMeta,
        UpdateUserRequestRole,
        UpdateUserResponse,
        UpdateUserResponseRole,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateUserRequestRole": ".types",
    "CreateUserResponse": ".types",
    "CreateUserResponseRole": ".types",
    "GetUsersRequestFilterDateField": ".types",
    "GetUsersRequestOrder": ".types",
    "GetUsersRequestSortBy": ".types",
    "GetUsersResponse": ".types",
    "GetUsersResponseDataItem": ".types",
    "GetUsersResponseDataItemRole": ".types",
    "GetUsersResponseMeta": ".types",
    "UpdateUserRequestRole": ".types",
    "UpdateUserResponse": ".types",
    "UpdateUserResponseRole": ".types",
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
    "CreateUserRequestRole",
    "CreateUserResponse",
    "CreateUserResponseRole",
    "GetUsersRequestFilterDateField",
    "GetUsersRequestOrder",
    "GetUsersRequestSortBy",
    "GetUsersResponse",
    "GetUsersResponseDataItem",
    "GetUsersResponseDataItemRole",
    "GetUsersResponseMeta",
    "UpdateUserRequestRole",
    "UpdateUserResponse",
    "UpdateUserResponseRole",
]
