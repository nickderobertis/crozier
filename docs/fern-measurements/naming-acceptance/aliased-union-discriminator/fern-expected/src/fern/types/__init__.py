



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .graph_result import GraphResult
    from .query_response import QueryResponse, QueryResponse_Graph, QueryResponse_Table
    from .table_result import TableResult
_dynamic_imports: typing.Dict[str, str] = {
    "GraphResult": ".graph_result",
    "QueryResponse": ".query_response",
    "QueryResponse_Graph": ".query_response",
    "QueryResponse_Table": ".query_response",
    "TableResult": ".table_result",
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


__all__ = ["GraphResult", "QueryResponse", "QueryResponse_Graph", "QueryResponse_Table", "TableResult"]
