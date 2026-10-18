



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .assistant_create_if_exists import AssistantCreateIfExists
    from .assistant_search_request_select_item import AssistantSearchRequestSelectItem
    from .assistant_search_request_sort_by import AssistantSearchRequestSortBy
    from .assistant_search_request_sort_order import AssistantSearchRequestSortOrder
_dynamic_imports: typing.Dict[str, str] = {
    "AssistantCreateIfExists": ".assistant_create_if_exists",
    "AssistantSearchRequestSelectItem": ".assistant_search_request_select_item",
    "AssistantSearchRequestSortBy": ".assistant_search_request_sort_by",
    "AssistantSearchRequestSortOrder": ".assistant_search_request_sort_order",
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
    "AssistantCreateIfExists",
    "AssistantSearchRequestSelectItem",
    "AssistantSearchRequestSortBy",
    "AssistantSearchRequestSortOrder",
]
