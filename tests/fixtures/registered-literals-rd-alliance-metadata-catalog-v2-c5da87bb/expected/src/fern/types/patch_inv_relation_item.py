

import typing

from .patch_inv_relation_item_one import PatchInvRelationItemOne
from .patch_inv_relation_item_zero import PatchInvRelationItemZero

PatchInvRelationItem = typing.Union[PatchInvRelationItemZero, PatchInvRelationItemOne]
