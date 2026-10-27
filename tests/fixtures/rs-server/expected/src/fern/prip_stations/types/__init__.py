



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_prip_collection_items_prip_collections_collection_id_items_get_request_filter_lang import (
        GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang,
    )
    from .get_prip_collection_items_prip_collections_collection_id_items_get_response import (
        GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse,
    )
    from .get_prip_collection_prip_collections_collection_id_get_response import (
        GetPripCollectionPripCollectionsCollectionIdGetResponse,
    )
    from .get_prip_collection_specific_item_prip_collections_collection_id_items_item_id_get_response import (
        GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse,
    )
    from .search_prip_search_get_request_filter_lang import SearchPripSearchGetRequestFilterLang
_dynamic_imports: typing.Dict[str, str] = {
    "GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang": ".get_prip_collection_items_prip_collections_collection_id_items_get_request_filter_lang",
    "GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse": ".get_prip_collection_items_prip_collections_collection_id_items_get_response",
    "GetPripCollectionPripCollectionsCollectionIdGetResponse": ".get_prip_collection_prip_collections_collection_id_get_response",
    "GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse": ".get_prip_collection_specific_item_prip_collections_collection_id_items_item_id_get_response",
    "SearchPripSearchGetRequestFilterLang": ".search_prip_search_get_request_filter_lang",
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
    "GetPripCollectionItemsPripCollectionsCollectionIdItemsGetRequestFilterLang",
    "GetPripCollectionItemsPripCollectionsCollectionIdItemsGetResponse",
    "GetPripCollectionPripCollectionsCollectionIdGetResponse",
    "GetPripCollectionSpecificItemPripCollectionsCollectionIdItemsItemIdGetResponse",
    "SearchPripSearchGetRequestFilterLang",
]
