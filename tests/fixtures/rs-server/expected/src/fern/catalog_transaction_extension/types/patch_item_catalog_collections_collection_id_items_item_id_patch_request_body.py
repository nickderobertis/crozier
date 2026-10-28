

import typing

from ...types.partial_item import PartialItem
from .patch_item_catalog_collections_collection_id_items_item_id_patch_request_body_one_item import (
    PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyOneItem,
)

PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBody = typing.Union[
    PartialItem, typing.List[PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyOneItem]
]
