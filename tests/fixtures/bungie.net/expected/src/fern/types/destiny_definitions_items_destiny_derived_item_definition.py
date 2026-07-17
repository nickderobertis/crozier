

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyDefinitionsItemsDestinyDerivedItemDefinition(UniversalBaseModel):
    """
    This is a reference to, and summary data for, a specific item that you can get as a result of Using or Acquiring some other Item (For example, this could be summary information for an Emote that you can get by opening an an Eververse Box) See DestinyDerivedItemCategoryDefinition for more information.
    """

    icon_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iconPath"),
        pydantic.Field(alias="iconPath", description="An icon for the item."),
    ] = None
    """
    An icon for the item.
    """

    item_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemDescription"),
        pydantic.Field(alias="itemDescription", description="A brief description of the item."),
    ] = None
    """
    A brief description of the item.
    """

    item_detail: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemDetail"),
        pydantic.Field(
            alias="itemDetail", description="Additional details about the derived item, in addition to the description."
        ),
    ] = None
    """
    Additional details about the derived item, in addition to the description.
    """

    item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemHash"),
        pydantic.Field(
            alias="itemHash",
            description="The hash for the DestinyInventoryItemDefinition of this derived item, if there is one. Sometimes we are given this information as a manual override, in which case there won't be an actual DestinyInventoryItemDefinition for what we display, but you can still show the strings from this object itself.",
        ),
    ] = None
    """
    The hash for the DestinyInventoryItemDefinition of this derived item, if there is one. Sometimes we are given this information as a manual override, in which case there won't be an actual DestinyInventoryItemDefinition for what we display, but you can still show the strings from this object itself.
    """

    item_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemName"),
        pydantic.Field(alias="itemName", description="The name of the derived item."),
    ] = None
    """
    The name of the derived item.
    """

    vendor_item_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorItemIndex"),
        pydantic.Field(
            alias="vendorItemIndex",
            description='If the item was derived from a "Preview Vendor", this will be an index into the DestinyVendorDefinition\'s itemList property. Otherwise, -1.',
        ),
    ] = None
    """
    If the item was derived from a "Preview Vendor", this will be an index into the DestinyVendorDefinition's itemList property. Otherwise, -1.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
