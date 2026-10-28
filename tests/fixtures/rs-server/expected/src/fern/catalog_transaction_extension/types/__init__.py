



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_item_catalog_collections_collection_id_items_post_request_body import (
        CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody,
        CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature,
        CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_FeatureCollection,
    )
    from .patch_collection_catalog_collections_collection_id_patch_request_body import (
        PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody,
    )
    from .patch_collection_catalog_collections_collection_id_patch_request_body_one_item import (
        PatchCollectionCatalogCollectionsCollectionIdPatchRequestBodyOneItem,
    )
    from .patch_item_catalog_collections_collection_id_items_item_id_patch_request_body import (
        PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody,
    )
    from .patch_item_catalog_collections_collection_id_items_item_id_patch_request_body_one_item import (
        PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyOneItem,
    )
    from .patch_item_catalog_collections_collection_id_items_item_id_patch_request_body_type import (
        PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyType,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody": ".create_item_catalog_collections_collection_id_items_post_request_body",
    "CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature": ".create_item_catalog_collections_collection_id_items_post_request_body",
    "CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_FeatureCollection": ".create_item_catalog_collections_collection_id_items_post_request_body",
    "PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody": ".patch_collection_catalog_collections_collection_id_patch_request_body",
    "PatchCollectionCatalogCollectionsCollectionIdPatchRequestBodyOneItem": ".patch_collection_catalog_collections_collection_id_patch_request_body_one_item",
    "PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody": ".patch_item_catalog_collections_collection_id_items_item_id_patch_request_body",
    "PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyOneItem": ".patch_item_catalog_collections_collection_id_items_item_id_patch_request_body_one_item",
    "PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyType": ".patch_item_catalog_collections_collection_id_items_item_id_patch_request_body_type",
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
    "CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody",
    "CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_Feature",
    "CreateItemCatalogCollectionsCollectionIdItemsPostRequestBody_FeatureCollection",
    "PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody",
    "PatchCollectionCatalogCollectionsCollectionIdPatchRequestBodyOneItem",
    "PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody",
    "PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyOneItem",
    "PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyType",
]
