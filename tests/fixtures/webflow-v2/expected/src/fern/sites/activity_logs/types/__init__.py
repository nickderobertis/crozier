



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_activity_logs_response import ListActivityLogsResponse
    from .list_activity_logs_response_items_item import ListActivityLogsResponseItemsItem
    from .list_activity_logs_response_items_item_actor_type import ListActivityLogsResponseItemsItemActorType
    from .list_activity_logs_response_items_item_event import ListActivityLogsResponseItemsItemEvent
    from .list_activity_logs_response_items_item_resource_operation import (
        ListActivityLogsResponseItemsItemResourceOperation,
    )
    from .list_activity_logs_response_items_item_source import ListActivityLogsResponseItemsItemSource
    from .list_activity_logs_response_items_item_user import ListActivityLogsResponseItemsItemUser
    from .list_activity_logs_response_pagination import ListActivityLogsResponsePagination
_dynamic_imports: typing.Dict[str, str] = {
    "ListActivityLogsResponse": ".list_activity_logs_response",
    "ListActivityLogsResponseItemsItem": ".list_activity_logs_response_items_item",
    "ListActivityLogsResponseItemsItemActorType": ".list_activity_logs_response_items_item_actor_type",
    "ListActivityLogsResponseItemsItemEvent": ".list_activity_logs_response_items_item_event",
    "ListActivityLogsResponseItemsItemResourceOperation": ".list_activity_logs_response_items_item_resource_operation",
    "ListActivityLogsResponseItemsItemSource": ".list_activity_logs_response_items_item_source",
    "ListActivityLogsResponseItemsItemUser": ".list_activity_logs_response_items_item_user",
    "ListActivityLogsResponsePagination": ".list_activity_logs_response_pagination",
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
    "ListActivityLogsResponse",
    "ListActivityLogsResponseItemsItem",
    "ListActivityLogsResponseItemsItemActorType",
    "ListActivityLogsResponseItemsItemEvent",
    "ListActivityLogsResponseItemsItemResourceOperation",
    "ListActivityLogsResponseItemsItemSource",
    "ListActivityLogsResponseItemsItemUser",
    "ListActivityLogsResponsePagination",
]
