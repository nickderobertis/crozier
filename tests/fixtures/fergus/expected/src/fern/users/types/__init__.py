



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_users_request_filter_status import GetUsersRequestFilterStatus
    from .get_users_request_filter_user_type import GetUsersRequestFilterUserType
    from .get_users_request_sort_field import GetUsersRequestSortField
    from .get_users_request_sort_order import GetUsersRequestSortOrder
    from .patch_users_user_id_request_contact_items_item import PatchUsersUserIdRequestContactItemsItem
    from .patch_users_user_id_request_contact_items_item_contact_type import (
        PatchUsersUserIdRequestContactItemsItemContactType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetUsersRequestFilterStatus": ".get_users_request_filter_status",
    "GetUsersRequestFilterUserType": ".get_users_request_filter_user_type",
    "GetUsersRequestSortField": ".get_users_request_sort_field",
    "GetUsersRequestSortOrder": ".get_users_request_sort_order",
    "PatchUsersUserIdRequestContactItemsItem": ".patch_users_user_id_request_contact_items_item",
    "PatchUsersUserIdRequestContactItemsItemContactType": ".patch_users_user_id_request_contact_items_item_contact_type",
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
    "GetUsersRequestFilterStatus",
    "GetUsersRequestFilterUserType",
    "GetUsersRequestSortField",
    "GetUsersRequestSortOrder",
    "PatchUsersUserIdRequestContactItemsItem",
    "PatchUsersUserIdRequestContactItemsItemContactType",
]
