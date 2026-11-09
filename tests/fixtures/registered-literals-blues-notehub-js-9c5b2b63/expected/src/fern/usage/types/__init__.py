



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_data_usage_request_aggregate import GetDataUsageRequestAggregate
    from .get_data_usage_request_period import GetDataUsageRequestPeriod
    from .get_data_usage_response import GetDataUsageResponse
    from .get_data_usage_response_data_item import GetDataUsageResponseDataItem
    from .get_data_usage_response_data_item_type import GetDataUsageResponseDataItemType
    from .get_events_usage_request_aggregate import GetEventsUsageRequestAggregate
    from .get_events_usage_request_period import GetEventsUsageRequestPeriod
    from .get_route_logs_usage_request_aggregate import GetRouteLogsUsageRequestAggregate
    from .get_route_logs_usage_request_period import GetRouteLogsUsageRequestPeriod
    from .get_route_logs_usage_response import GetRouteLogsUsageResponse
    from .get_sessions_usage_request_aggregate import GetSessionsUsageRequestAggregate
    from .get_sessions_usage_request_period import GetSessionsUsageRequestPeriod
    from .get_sessions_usage_response import GetSessionsUsageResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetDataUsageRequestAggregate": ".get_data_usage_request_aggregate",
    "GetDataUsageRequestPeriod": ".get_data_usage_request_period",
    "GetDataUsageResponse": ".get_data_usage_response",
    "GetDataUsageResponseDataItem": ".get_data_usage_response_data_item",
    "GetDataUsageResponseDataItemType": ".get_data_usage_response_data_item_type",
    "GetEventsUsageRequestAggregate": ".get_events_usage_request_aggregate",
    "GetEventsUsageRequestPeriod": ".get_events_usage_request_period",
    "GetRouteLogsUsageRequestAggregate": ".get_route_logs_usage_request_aggregate",
    "GetRouteLogsUsageRequestPeriod": ".get_route_logs_usage_request_period",
    "GetRouteLogsUsageResponse": ".get_route_logs_usage_response",
    "GetSessionsUsageRequestAggregate": ".get_sessions_usage_request_aggregate",
    "GetSessionsUsageRequestPeriod": ".get_sessions_usage_request_period",
    "GetSessionsUsageResponse": ".get_sessions_usage_response",
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
    "GetDataUsageRequestAggregate",
    "GetDataUsageRequestPeriod",
    "GetDataUsageResponse",
    "GetDataUsageResponseDataItem",
    "GetDataUsageResponseDataItemType",
    "GetEventsUsageRequestAggregate",
    "GetEventsUsageRequestPeriod",
    "GetRouteLogsUsageRequestAggregate",
    "GetRouteLogsUsageRequestPeriod",
    "GetRouteLogsUsageResponse",
    "GetSessionsUsageRequestAggregate",
    "GetSessionsUsageRequestPeriod",
    "GetSessionsUsageResponse",
]
