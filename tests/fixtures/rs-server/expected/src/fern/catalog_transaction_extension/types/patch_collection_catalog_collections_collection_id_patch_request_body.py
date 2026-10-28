

import typing

from ...types.partial_collection import PartialCollection
from .patch_collection_catalog_collections_collection_id_patch_request_body_one_item import (
    PatchCollectionCatalogCollectionsCollectionIdPatchRequestBodyOneItem,
)

PatchCollectionCatalogCollectionsCollectionIdPatchRequestBody = typing.Union[
    PartialCollection, typing.List[PatchCollectionCatalogCollectionsCollectionIdPatchRequestBodyOneItem]
]
