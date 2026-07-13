

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsDestinyItemInventoryBlockDefinition(UniversalBaseModel):
    """
    If the item can exist in an inventory - the overwhelming majority of them can and do - then this is the basic properties regarding the item's relationship with the inventory.
    """

    bucket_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="bucketTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier for the DestinyInventoryBucketDefinition to which this item belongs. I should have named this "bucketHash", but too many things refer to it now. Sigh.
    """

    expiration_tooltip: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="expirationTooltip")] = (
        pydantic.Field(default=None)
    )
    """
    The tooltip message to show, if any, when the item expires.
    """

    expired_in_activity_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expiredInActivityMessage")
    ] = pydantic.Field(default=None)
    """
    If the item expires while playing in an activity, we show a different message.
    """

    expired_in_orbit_message: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="expiredInOrbitMessage")
    ] = pydantic.Field(default=None)
    """
    If the item expires in orbit, we show a... more different message. ("Consummate V's, consummate!")
    """

    is_instance_item: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isInstanceItem")] = (
        pydantic.Field(default=None)
    )
    """
    If TRUE, this item is instanced. Otherwise, it is a generic item that merely has a quantity in a stack (like Glimmer).
    """

    max_stack_size: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxStackSize")] = (
        pydantic.Field(default=None)
    )
    """
    The maximum quantity of this item that can exist in a stack.
    """

    recipe_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="recipeItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    A reference to the associated crafting 'recipe' item definition, if this item can be crafted.
    """

    recovery_bucket_type_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="recoveryBucketTypeHash")
    ] = pydantic.Field(default=None)
    """
    If the item is picked up by the lost loot queue, this is the hash identifier for the DestinyInventoryBucketDefinition into which it will be placed. Again, I should have named this recoveryBucketHash instead.
    """

    stack_unique_label: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="stackUniqueLabel")] = (
        pydantic.Field(default=None)
    )
    """
    If this string is populated, you can't have more than one stack with this label in a given inventory. Note that this is different from the equipping block's unique label, which is used for equipping uniqueness.
    """

    suppress_expiration_when_objectives_complete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="suppressExpirationWhenObjectivesComplete")
    ] = None
    tier_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="tierType")] = pydantic.Field(
        default=None
    )
    """
    The enumeration matching the tier type of the item to known values, again for convenience sake.
    """

    tier_type_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="tierTypeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier for the Tier Type of the item, use to look up its DestinyItemTierTypeDefinition if you need to show localized data for the item's tier.
    """

    tier_type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="tierTypeName")] = (
        pydantic.Field(default=None)
    )
    """
    The localized name of the tier type, which is a useful shortcut so you don't have to look up the definition every time. However, it's mostly a holdover from days before we had a DestinyItemTierTypeDefinition to refer to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
