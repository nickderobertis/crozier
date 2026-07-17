

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_items_destiny_derived_item_definition import (
    DestinyDefinitionsItemsDestinyDerivedItemDefinition,
)


class DestinyDefinitionsItemsDestinyDerivedItemCategoryDefinition(UniversalBaseModel):
    """
    A shortcut for the fact that some items have a "Preview Vendor" - See DestinyInventoryItemDefinition.preview.previewVendorHash - that is intended to be used to show what items you can get as a result of acquiring or using this item.
    A common example of this in Destiny 1 was Eververse "Boxes," which could have many possible items. This "Preview Vendor" is not a vendor you can actually see in the game, but it defines categories and sale items for all of the possible items you could get from the Box so that the game can show them to you. We summarize that info here so that you don't have to do that Vendor lookup and aggregation manually.
    """

    category_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="categoryDescription"),
        pydantic.Field(
            alias="categoryDescription",
            description="The localized string for the category title. This will be something describing the items you can get as a group, or your likelihood/the quantity you'll get.",
        ),
    ] = None
    """
    The localized string for the category title. This will be something describing the items you can get as a group, or your likelihood/the quantity you'll get.
    """

    items: typing.Optional[typing.List[DestinyDefinitionsItemsDestinyDerivedItemDefinition]] = pydantic.Field(
        default=None
    )
    """
    This is the list of all of the items for this category and the basic properties we'll know about them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
