

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_stat import DestinyDestinyStat
from .destiny_entities_items_destiny_item_instance_energy import DestinyEntitiesItemsDestinyItemInstanceEnergy


class DestinyEntitiesItemsDestinyItemInstanceComponent(UniversalBaseModel):
    """
    If an item is "instanced", this will contain information about the item's instance that doesn't fit easily into other components. One might say this is the "essential" instance data for the item.
    Items are instanced if they require information or state that can vary. For instance, weapons are Instanced: they are given a unique identifier, uniquely generated stats, and can have their properties altered. Non-instanced items have none of these things: for instance, Glimmer has no unique properties aside from how much of it you own.
    You can tell from an item's definition whether it will be instanced or not by looking at the DestinyInventoryItemDefinition's definition.inventory.isInstanceItem property.
    """

    breaker_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="breakerType")] = (
        pydantic.Field(default=None)
    )
    """
    If populated, this item has a breaker type corresponding to the given value. See DestinyBreakerTypeDefinition for more details.
    """

    breaker_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="breakerTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    If populated, this is the hash identifier for the item's breaker type. See DestinyBreakerTypeDefinition for more details.
    """

    can_equip: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="canEquip")] = pydantic.Field(
        default=None
    )
    """
    If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details.
    """

    cannot_equip_reason: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="cannotEquipReason")] = (
        pydantic.Field(default=None)
    )
    """
    If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn't equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel.
    """

    damage_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="damageType")] = pydantic.Field(
        default=None
    )
    """
    If the item has a damage type, this is the item's current damage type.
    """

    damage_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="damageTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The current damage type's hash, so you can look up localized info and icons for it.
    """

    energy: typing.Optional[DestinyEntitiesItemsDestinyItemInstanceEnergy] = pydantic.Field(default=None)
    """
    IF populated, this item supports Energy mechanics (i.e. Armor 2.0), and these are the current details of its energy type and available capacity to spend energy points.
    """

    equip_required_level: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="equipRequiredLevel")
    ] = pydantic.Field(default=None)
    """
    If the item cannot be equipped until you reach a certain level, that level will be reflected here.
    """

    is_equipped: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isEquipped")] = pydantic.Field(
        default=None
    )
    """
    Is the item currently equipped on the given character?
    """

    item_level: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemLevel")] = pydantic.Field(
        default=None
    )
    """
    The Item's "Level" has the most significant bearing on its stats, such as Light and Power.
    """

    primary_stat: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyStat], FieldMetadata(alias="primaryStat")
    ] = pydantic.Field(default=None)
    """
    The item stat that we consider to be "primary" for the item. For instance, this would be "Attack" for Weapons or "Defense" for armor.
    """

    quality: typing.Optional[int] = pydantic.Field(default=None)
    """
    The "Quality" of the item has a lesser - but still impactful - bearing on stats like Light and Power.
    """

    unlock_hashes_required_to_equip: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="unlockHashesRequiredToEquip")
    ] = pydantic.Field(default=None)
    """
    Sometimes, there are limitations to equipping that are represented by character-level flags called "unlocks".
    This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
