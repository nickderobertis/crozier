



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .meta_destinations_get_response import MetaDestinationsGetResponse
    from .meta_destinations_list_response import MetaDestinationsListResponse
    from .meta_destinations_list_response_items_item import MetaDestinationsListResponseItemsItem
    from .meta_sources_get_response import MetaSourcesGetResponse
    from .meta_sources_list_response import MetaSourcesListResponse
    from .meta_sources_list_response_items_item import MetaSourcesListResponseItemsItem
_dynamic_imports: typing.Dict[str, str] = {
    "MetaDestinationsGetResponse": ".meta_destinations_get_response",
    "MetaDestinationsListResponse": ".meta_destinations_list_response",
    "MetaDestinationsListResponseItemsItem": ".meta_destinations_list_response_items_item",
    "MetaSourcesGetResponse": ".meta_sources_get_response",
    "MetaSourcesListResponse": ".meta_sources_list_response",
    "MetaSourcesListResponseItemsItem": ".meta_sources_list_response_items_item",
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
    "MetaDestinationsGetResponse",
    "MetaDestinationsListResponse",
    "MetaDestinationsListResponseItemsItem",
    "MetaSourcesGetResponse",
    "MetaSourcesListResponse",
    "MetaSourcesListResponseItemsItem",
]
