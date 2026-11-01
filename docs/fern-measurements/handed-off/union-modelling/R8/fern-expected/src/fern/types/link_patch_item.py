

import typing

from .link_patch_item_one import LinkPatchItemOne
from .link_patch_item_zero import LinkPatchItemZero

LinkPatchItem = typing.Union[LinkPatchItemZero, LinkPatchItemOne]
