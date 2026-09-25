



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_time_entries_request_order import ListTimeEntriesRequestOrder
    from .list_time_entries_request_sort import ListTimeEntriesRequestSort
    from .v1hours_create_event import V1HoursCreateEvent
    from .v1hours_create_event_external_links_item import V1HoursCreateEventExternalLinksItem
    from .v1hours_create_event_timestamps_item import V1HoursCreateEventTimestampsItem
    from .v1hours_update_event import V1HoursUpdateEvent
    from .v1hours_update_event_external_links_item import V1HoursUpdateEventExternalLinksItem
    from .v1hours_update_event_timestamps_item import V1HoursUpdateEventTimestampsItem
_dynamic_imports: typing.Dict[str, str] = {
    "ListTimeEntriesRequestOrder": ".list_time_entries_request_order",
    "ListTimeEntriesRequestSort": ".list_time_entries_request_sort",
    "V1HoursCreateEvent": ".v1hours_create_event",
    "V1HoursCreateEventExternalLinksItem": ".v1hours_create_event_external_links_item",
    "V1HoursCreateEventTimestampsItem": ".v1hours_create_event_timestamps_item",
    "V1HoursUpdateEvent": ".v1hours_update_event",
    "V1HoursUpdateEventExternalLinksItem": ".v1hours_update_event_external_links_item",
    "V1HoursUpdateEventTimestampsItem": ".v1hours_update_event_timestamps_item",
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
    "ListTimeEntriesRequestOrder",
    "ListTimeEntriesRequestSort",
    "V1HoursCreateEvent",
    "V1HoursCreateEventExternalLinksItem",
    "V1HoursCreateEventTimestampsItem",
    "V1HoursUpdateEvent",
    "V1HoursUpdateEventExternalLinksItem",
    "V1HoursUpdateEventTimestampsItem",
]
