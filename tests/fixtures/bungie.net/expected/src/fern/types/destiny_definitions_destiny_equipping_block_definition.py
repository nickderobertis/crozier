

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyEquippingBlockDefinition(UniversalBaseModel):
    """
    Items that can be equipped define this block. It contains information we need to understand how and when the item can be equipped.
    """

    ammo_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ammoType"),
        pydantic.Field(
            alias="ammoType",
            description="Ammo type used by a weapon is no longer determined by the bucket in which it is contained. If the item has an ammo type - i.e. if it is a weapon - this will be the type of ammunition expected.",
        ),
    ] = None
    """
    Ammo type used by a weapon is no longer determined by the bucket in which it is contained. If the item has an ammo type - i.e. if it is a weapon - this will be the type of ammunition expected.
    """

    attributes: typing.Optional[int] = pydantic.Field(default=None)
    """
    These are custom attributes on the equippability of the item.
    For now, this can only be "equip on acquire", which would mean that the item will be automatically equipped as soon as you pick it up.
    """

    display_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="displayStrings"),
        pydantic.Field(
            alias="displayStrings",
            description="These are strings that represent the possible Game/Account/Character state failure conditions that can occur when trying to equip the item. They match up one-to-one with requiredUnlockExpressions.",
        ),
    ] = None
    """
    These are strings that represent the possible Game/Account/Character state failure conditions that can occur when trying to equip the item. They match up one-to-one with requiredUnlockExpressions.
    """

    equipment_slot_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="equipmentSlotTypeHash"),
        pydantic.Field(
            alias="equipmentSlotTypeHash",
            description="An equipped item *must* be equipped in an Equipment Slot. This is the hash identifier of the DestinyEquipmentSlotDefinition into which it must be equipped.",
        ),
    ] = None
    """
    An equipped item *must* be equipped in an Equipment Slot. This is the hash identifier of the DestinyEquipmentSlotDefinition into which it must be equipped.
    """

    gearset_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="gearsetItemHash"),
        pydantic.Field(
            alias="gearsetItemHash",
            description="If the item is part of a gearset, this is a reference to that gearset item.",
        ),
    ] = None
    """
    If the item is part of a gearset, this is a reference to that gearset item.
    """

    unique_label: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uniqueLabel"),
        pydantic.Field(
            alias="uniqueLabel",
            description="If defined, this is the label used to check if the item has other items of matching types already equipped. \r\nFor instance, when you aren't allowed to equip more than one Exotic Weapon, that's because all exotic weapons have identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel vs. all other already equipped items (other than the item in the slot that's about to be occupied).",
        ),
    ] = None
    """
    If defined, this is the label used to check if the item has other items of matching types already equipped. 
    For instance, when you aren't allowed to equip more than one Exotic Weapon, that's because all exotic weapons have identical uniqueLabels and the game checks the to-be-equipped item's uniqueLabel vs. all other already equipped items (other than the item in the slot that's about to be occupied).
    """

    unique_label_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="uniqueLabelHash"),
        pydantic.Field(
            alias="uniqueLabelHash",
            description="The hash of that unique label. Does not point to a specific definition.",
        ),
    ] = None
    """
    The hash of that unique label. Does not point to a specific definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
