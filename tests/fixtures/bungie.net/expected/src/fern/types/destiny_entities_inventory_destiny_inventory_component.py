

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_entities_items_destiny_item_component import DestinyEntitiesItemsDestinyItemComponent


class DestinyEntitiesInventoryDestinyInventoryComponent(UniversalBaseModel):
    """
    A list of minimal information for items in an inventory: be it a character's inventory, or a Profile's inventory. (Note that the Vault is a collection of inventory buckets in the Profile's inventory)
    Inventory Items returned here are in a flat list, but importantly they have a bucketHash property that indicates the specific inventory bucket that is holding them. These buckets constitute things like the separate sections of the Vault, the user's inventory slots, etc. See DestinyInventoryBucketDefinition for more info.
    """

    items: typing.Optional[typing.List[DestinyEntitiesItemsDestinyItemComponent]] = pydantic.Field(default=None)
    """
    The items in this inventory. If you care to bucket them, use the item's bucketHash property to group them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
