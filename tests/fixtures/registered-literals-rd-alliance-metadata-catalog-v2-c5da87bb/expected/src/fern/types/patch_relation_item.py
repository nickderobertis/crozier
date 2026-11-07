

import typing

from .patch_relation_item_one import PatchRelationItemOne
from .patch_relation_item_zero import PatchRelationItemZero

PatchRelationItem = typing.Union[PatchRelationItemZero, PatchRelationItemOne]
