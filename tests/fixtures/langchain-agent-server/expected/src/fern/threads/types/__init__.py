



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .thread_count_request_status import ThreadCountRequestStatus
    from .thread_create_if_exists import ThreadCreateIfExists
    from .thread_create_supersteps_item import ThreadCreateSuperstepsItem
    from .thread_create_ttl import ThreadCreateTtl
    from .thread_create_ttl_strategy import ThreadCreateTtlStrategy
    from .thread_patch_ttl import ThreadPatchTtl
    from .thread_patch_ttl_strategy import ThreadPatchTtlStrategy
    from .thread_prune_request_strategy import ThreadPruneRequestStrategy
    from .thread_search_request_select_item import ThreadSearchRequestSelectItem
    from .thread_search_request_sort_by import ThreadSearchRequestSortBy
    from .thread_search_request_sort_order import ThreadSearchRequestSortOrder
    from .thread_search_request_status import ThreadSearchRequestStatus
    from .thread_state_update_values import ThreadStateUpdateValues
_dynamic_imports: typing.Dict[str, str] = {
    "ThreadCountRequestStatus": ".thread_count_request_status",
    "ThreadCreateIfExists": ".thread_create_if_exists",
    "ThreadCreateSuperstepsItem": ".thread_create_supersteps_item",
    "ThreadCreateTtl": ".thread_create_ttl",
    "ThreadCreateTtlStrategy": ".thread_create_ttl_strategy",
    "ThreadPatchTtl": ".thread_patch_ttl",
    "ThreadPatchTtlStrategy": ".thread_patch_ttl_strategy",
    "ThreadPruneRequestStrategy": ".thread_prune_request_strategy",
    "ThreadSearchRequestSelectItem": ".thread_search_request_select_item",
    "ThreadSearchRequestSortBy": ".thread_search_request_sort_by",
    "ThreadSearchRequestSortOrder": ".thread_search_request_sort_order",
    "ThreadSearchRequestStatus": ".thread_search_request_status",
    "ThreadStateUpdateValues": ".thread_state_update_values",
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
    "ThreadCountRequestStatus",
    "ThreadCreateIfExists",
    "ThreadCreateSuperstepsItem",
    "ThreadCreateTtl",
    "ThreadCreateTtlStrategy",
    "ThreadPatchTtl",
    "ThreadPatchTtlStrategy",
    "ThreadPruneRequestStrategy",
    "ThreadSearchRequestSelectItem",
    "ThreadSearchRequestSortBy",
    "ThreadSearchRequestSortOrder",
    "ThreadSearchRequestStatus",
    "ThreadStateUpdateValues",
]
