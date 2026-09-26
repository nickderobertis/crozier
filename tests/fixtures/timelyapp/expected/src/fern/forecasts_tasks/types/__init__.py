



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_task_summaries_request_completed import ListTaskSummariesRequestCompleted
    from .list_task_summaries_request_resource import ListTaskSummariesRequestResource
    from .list_tasks_request_completed import ListTasksRequestCompleted
    from .list_tasks_request_order import ListTasksRequestOrder
    from .list_tasks_request_sort import ListTasksRequestSort
    from .v1forecasts_create_forecast import V1ForecastsCreateForecast
    from .v1forecasts_update_forecast import V1ForecastsUpdateForecast
_dynamic_imports: typing.Dict[str, str] = {
    "ListTaskSummariesRequestCompleted": ".list_task_summaries_request_completed",
    "ListTaskSummariesRequestResource": ".list_task_summaries_request_resource",
    "ListTasksRequestCompleted": ".list_tasks_request_completed",
    "ListTasksRequestOrder": ".list_tasks_request_order",
    "ListTasksRequestSort": ".list_tasks_request_sort",
    "V1ForecastsCreateForecast": ".v1forecasts_create_forecast",
    "V1ForecastsUpdateForecast": ".v1forecasts_update_forecast",
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
    "ListTaskSummariesRequestCompleted",
    "ListTaskSummariesRequestResource",
    "ListTasksRequestCompleted",
    "ListTasksRequestOrder",
    "ListTasksRequestSort",
    "V1ForecastsCreateForecast",
    "V1ForecastsUpdateForecast",
]
