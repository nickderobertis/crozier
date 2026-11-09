



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_events_by_cursor_request_sort_order import GetEventsByCursorRequestSortOrder
    from .get_events_by_cursor_response import GetEventsByCursorResponse
    from .get_events_request_date_type import GetEventsRequestDateType
    from .get_events_request_format import GetEventsRequestFormat
    from .get_events_request_sort_by import GetEventsRequestSortBy
    from .get_events_request_sort_order import GetEventsRequestSortOrder
    from .get_fleet_events_by_cursor_request_sort_order import GetFleetEventsByCursorRequestSortOrder
    from .get_fleet_events_by_cursor_response import GetFleetEventsByCursorResponse
    from .get_fleet_events_request_date_type import GetFleetEventsRequestDateType
    from .get_fleet_events_request_format import GetFleetEventsRequestFormat
    from .get_fleet_events_request_sort_by import GetFleetEventsRequestSortBy
    from .get_fleet_events_request_sort_order import GetFleetEventsRequestSortOrder
_dynamic_imports: typing.Dict[str, str] = {
    "GetEventsByCursorRequestSortOrder": ".get_events_by_cursor_request_sort_order",
    "GetEventsByCursorResponse": ".get_events_by_cursor_response",
    "GetEventsRequestDateType": ".get_events_request_date_type",
    "GetEventsRequestFormat": ".get_events_request_format",
    "GetEventsRequestSortBy": ".get_events_request_sort_by",
    "GetEventsRequestSortOrder": ".get_events_request_sort_order",
    "GetFleetEventsByCursorRequestSortOrder": ".get_fleet_events_by_cursor_request_sort_order",
    "GetFleetEventsByCursorResponse": ".get_fleet_events_by_cursor_response",
    "GetFleetEventsRequestDateType": ".get_fleet_events_request_date_type",
    "GetFleetEventsRequestFormat": ".get_fleet_events_request_format",
    "GetFleetEventsRequestSortBy": ".get_fleet_events_request_sort_by",
    "GetFleetEventsRequestSortOrder": ".get_fleet_events_request_sort_order",
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
    "GetEventsByCursorRequestSortOrder",
    "GetEventsByCursorResponse",
    "GetEventsRequestDateType",
    "GetEventsRequestFormat",
    "GetEventsRequestSortBy",
    "GetEventsRequestSortOrder",
    "GetFleetEventsByCursorRequestSortOrder",
    "GetFleetEventsByCursorResponse",
    "GetFleetEventsRequestDateType",
    "GetFleetEventsRequestFormat",
    "GetFleetEventsRequestSortBy",
    "GetFleetEventsRequestSortOrder",
]
