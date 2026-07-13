

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_art_dye_reference import DestinyDefinitionsDestinyArtDyeReference


class DestinyDefinitionsDestinyEquipmentSlotDefinition(UniversalBaseModel):
    """
    Characters can not only have Inventory buckets (containers of items that are generally matched by their type or functionality), they can also have Equipment Slots.
    The Equipment Slot is an indicator that the related bucket can have instanced items equipped on the character. For instance, the Primary Weapon bucket has an Equipment Slot that determines whether you can equip primary weapons, and holds the association between its slot and the inventory bucket from which it can have items equipped.
    An Equipment Slot must have a related Inventory Bucket, but not all inventory buckets must have Equipment Slots.
    """

    apply_custom_art_dyes: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="applyCustomArtDyes")
    ] = pydantic.Field(default=None)
    """
    If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot.
    """

    art_dye_channels: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyArtDyeReference]], FieldMetadata(alias="artDyeChannels")
    ] = pydantic.Field(default=None)
    """
    The Art Dye Channels that apply to this equipment slot.
    """

    bucket_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="bucketTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The inventory bucket that owns this equipment slot.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    equipment_category_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="equipmentCategoryHash")
    ] = pydantic.Field(default=None)
    """
    These technically point to "Equipment Category Definitions". But don't get excited. There's nothing of significant value in those definitions, so I didn't bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
