



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_adgs_collection_auxip_collections_collection_id_get_response import (
        GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse,
    )
    from .get_adgs_collection_items_auxip_collections_collection_id_items_get_request_filter_lang import (
        GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang,
    )
    from .get_adgs_collection_items_auxip_collections_collection_id_items_get_response import (
        GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse,
    )
    from .get_adgs_collection_specific_item_auxip_collections_collection_id_items_item_id_get_response import (
        GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse,
    )
    from .search_auxip_search_get_request_filter_lang import SearchAuxipSearchGetRequestFilterLang
_dynamic_imports: typing.Dict[str, str] = {
    "GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse": ".get_adgs_collection_auxip_collections_collection_id_get_response",
    "GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang": ".get_adgs_collection_items_auxip_collections_collection_id_items_get_request_filter_lang",
    "GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse": ".get_adgs_collection_items_auxip_collections_collection_id_items_get_response",
    "GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse": ".get_adgs_collection_specific_item_auxip_collections_collection_id_items_item_id_get_response",
    "SearchAuxipSearchGetRequestFilterLang": ".search_auxip_search_get_request_filter_lang",
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
    "GetAdgsCollectionAuxipCollectionsCollectionIdGetResponse",
    "GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetRequestFilterLang",
    "GetAdgsCollectionItemsAuxipCollectionsCollectionIdItemsGetResponse",
    "GetAdgsCollectionSpecificItemAuxipCollectionsCollectionIdItemsItemIdGetResponse",
    "SearchAuxipSearchGetRequestFilterLang",
]
