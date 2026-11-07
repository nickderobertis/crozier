



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .library_link_start_url_response import LibraryLinkStartUrlResponse
    from .library_list_response_item import LibraryListResponseItem
    from .library_list_response_item_aggregated_performance import LibraryListResponseItemAggregatedPerformance
    from .library_status_response import LibraryStatusResponse
    from .library_sync_response import LibrarySyncResponse
    from .library_unlink_response import LibraryUnlinkResponse
_dynamic_imports: typing.Dict[str, str] = {
    "LibraryLinkStartUrlResponse": ".library_link_start_url_response",
    "LibraryListResponseItem": ".library_list_response_item",
    "LibraryListResponseItemAggregatedPerformance": ".library_list_response_item_aggregated_performance",
    "LibraryStatusResponse": ".library_status_response",
    "LibrarySyncResponse": ".library_sync_response",
    "LibraryUnlinkResponse": ".library_unlink_response",
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
    "LibraryLinkStartUrlResponse",
    "LibraryListResponseItem",
    "LibraryListResponseItemAggregatedPerformance",
    "LibraryStatusResponse",
    "LibrarySyncResponse",
    "LibraryUnlinkResponse",
]
