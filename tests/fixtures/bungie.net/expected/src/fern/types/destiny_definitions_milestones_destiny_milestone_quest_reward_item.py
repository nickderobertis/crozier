

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem(UniversalBaseModel):
    """
    A subclass of DestinyItemQuantity, that provides not just the item and its quantity but also information that BNet can - at some point - use internally to provide more robust runtime information about the item's qualities.
    If you want it, please ask! We're just out of time to wire it up right now. Or a clever person just may do it with our existing endpoints.
    """

    has_conditional_visibility: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="hasConditionalVisibility")
    ] = pydantic.Field(default=None)
    """
    Indicates that this item quantity may be conditionally shown or hidden, based on various sources of state. For example: server flags, account state, or character progress.
    """

    item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemHash")] = pydantic.Field(
        default=None
    )
    """
    The hash identifier for the item in question. Use it to look up the item's DestinyInventoryItemDefinition.
    """

    item_instance_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="itemInstanceId")] = (
        pydantic.Field(default=None)
    )
    """
    If this quantity is referring to a specific instance of an item, this will have the item's instance ID. Normally, this will be null.
    """

    quantity: typing.Optional[int] = pydantic.Field(default=None)
    """
    The amount of the item needed/available depending on the context of where DestinyItemQuantity is being used.
    """

    vendor_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorHash")] = pydantic.Field(
        default=None
    )
    """
    The quest reward item *may* be associated with a vendor. If so, this is that vendor. Use this hash to look up the DestinyVendorDefinition.
    """

    vendor_item_index: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorItemIndex")] = (
        pydantic.Field(default=None)
    )
    """
    The quest reward item *may* be associated with a vendor. If so, this is the index of the item being sold, which we can use at runtime to find instanced item information for the reward item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
