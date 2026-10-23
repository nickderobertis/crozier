



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_user_request_role import CreateUserRequestRole
    from .create_user_response import CreateUserResponse
    from .create_user_response_role import CreateUserResponseRole
    from .get_users_request_filter_date_field import GetUsersRequestFilterDateField
    from .get_users_request_order import GetUsersRequestOrder
    from .get_users_request_sort_by import GetUsersRequestSortBy
    from .get_users_response import GetUsersResponse
    from .get_users_response_data_item import GetUsersResponseDataItem
    from .get_users_response_data_item_role import GetUsersResponseDataItemRole
    from .get_users_response_meta import GetUsersResponseMeta
    from .update_user_request_role import UpdateUserRequestRole
    from .update_user_response import UpdateUserResponse
    from .update_user_response_role import UpdateUserResponseRole
_dynamic_imports: typing.Dict[str, str] = {
    "CreateUserRequestRole": ".create_user_request_role",
    "CreateUserResponse": ".create_user_response",
    "CreateUserResponseRole": ".create_user_response_role",
    "GetUsersRequestFilterDateField": ".get_users_request_filter_date_field",
    "GetUsersRequestOrder": ".get_users_request_order",
    "GetUsersRequestSortBy": ".get_users_request_sort_by",
    "GetUsersResponse": ".get_users_response",
    "GetUsersResponseDataItem": ".get_users_response_data_item",
    "GetUsersResponseDataItemRole": ".get_users_response_data_item_role",
    "GetUsersResponseMeta": ".get_users_response_meta",
    "UpdateUserRequestRole": ".update_user_request_role",
    "UpdateUserResponse": ".update_user_response",
    "UpdateUserResponseRole": ".update_user_response_role",
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
