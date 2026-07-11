



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .inlined_index_response import InlinedIndexResponse
    from .inlined_search_request_filter import InlinedSearchRequestFilter
    from .inlined_search_response import InlinedSearchResponse
    from .inlined_search_response_neighbor import InlinedSearchResponseNeighbor
_dynamic_imports: typing.Dict[str, str] = {
    "InlinedIndexResponse": ".inlined_index_response",
    "InlinedSearchRequestFilter": ".inlined_search_request_filter",
    "InlinedSearchResponse": ".inlined_search_response",
    "InlinedSearchResponseNeighbor": ".inlined_search_response_neighbor",
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
    "InlinedIndexResponse",
    "InlinedSearchRequestFilter",
    "InlinedSearchResponse",
    "InlinedSearchResponseNeighbor",
]
