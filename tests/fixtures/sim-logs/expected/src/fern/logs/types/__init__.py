



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_log_stats_request_level import GetLogStatsRequestLevel
    from .list_logs_request_details import ListLogsRequestDetails
    from .list_logs_request_level import ListLogsRequestLevel
    from .list_logs_request_sort_by import ListLogsRequestSortBy
    from .list_logs_request_sort_order import ListLogsRequestSortOrder
_dynamic_imports: typing.Dict[str, str] = {
    "GetLogStatsRequestLevel": ".get_log_stats_request_level",
    "ListLogsRequestDetails": ".list_logs_request_details",
    "ListLogsRequestLevel": ".list_logs_request_level",
    "ListLogsRequestSortBy": ".list_logs_request_sort_by",
    "ListLogsRequestSortOrder": ".list_logs_request_sort_order",
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
    "GetLogStatsRequestLevel",
    "ListLogsRequestDetails",
    "ListLogsRequestLevel",
    "ListLogsRequestSortBy",
    "ListLogsRequestSortOrder",
]
