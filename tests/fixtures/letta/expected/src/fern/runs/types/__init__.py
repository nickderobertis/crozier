



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_messages_for_run_request_order import ListMessagesForRunRequestOrder
    from .list_messages_for_run_request_order_by import ListMessagesForRunRequestOrderBy
    from .list_runs_request_order import ListRunsRequestOrder
    from .list_runs_request_order_by import ListRunsRequestOrderBy
    from .list_steps_for_run_request_order import ListStepsForRunRequestOrder
    from .list_steps_for_run_request_order_by import ListStepsForRunRequestOrderBy
_dynamic_imports: typing.Dict[str, str] = {
    "ListMessagesForRunRequestOrder": ".list_messages_for_run_request_order",
    "ListMessagesForRunRequestOrderBy": ".list_messages_for_run_request_order_by",
    "ListRunsRequestOrder": ".list_runs_request_order",
    "ListRunsRequestOrderBy": ".list_runs_request_order_by",
    "ListStepsForRunRequestOrder": ".list_steps_for_run_request_order",
    "ListStepsForRunRequestOrderBy": ".list_steps_for_run_request_order_by",
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
    "ListMessagesForRunRequestOrder",
    "ListMessagesForRunRequestOrderBy",
    "ListRunsRequestOrder",
    "ListRunsRequestOrderBy",
    "ListStepsForRunRequestOrder",
    "ListStepsForRunRequestOrderBy",
]
