

import typing

from ...types.patch_add_replace_test import PatchAddReplaceTest
from ...types.patch_move_copy import PatchMoveCopy
from ...types.patch_remove import PatchRemove

PatchItemCatalogCollectionsCollectionIdItemsItemIdPatchRequestBodyOneItem = typing.Union[
    PatchAddReplaceTest, PatchMoveCopy, PatchRemove
]
