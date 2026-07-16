

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_destiny_vendor_category_overlay_definition import (
    DestinyDefinitionsDestinyVendorCategoryOverlayDefinition,
)


class DestinyDefinitionsDestinyVendorCategoryEntryDefinition(UniversalBaseModel):
    """
    This is the definition for a single Vendor Category, into which Sale Items are grouped.
    """

    buy_string_override: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="buyStringOverride"),
        pydantic.Field(
            alias="buyStringOverride",
            description="The localized string for making purchases from this category, if it is different from the vendor's string for purchasing.",
        ),
    ] = None
    """
    The localized string for making purchases from this category, if it is different from the vendor's string for purchasing.
    """

    category_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="categoryHash"),
        pydantic.Field(alias="categoryHash", description="The hashed identifier for the category."),
    ] = None
    """
    The hashed identifier for the category.
    """

    category_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="categoryIndex"),
        pydantic.Field(
            alias="categoryIndex",
            description="The index of the category in the original category definitions for the vendor.",
        ),
    ] = None
    """
    The index of the category in the original category definitions for the vendor.
    """

    disabled_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="disabledDescription"),
        pydantic.Field(
            alias="disabledDescription",
            description="If the category is disabled, this is the localized description to show.",
        ),
    ] = None
    """
    If the category is disabled, this is the localized description to show.
    """

    display_title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayTitle"),
        pydantic.Field(alias="displayTitle", description="The localized title of the category."),
    ] = None
    """
    The localized title of the category.
    """

    hide_from_regular_purchase: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hideFromRegularPurchase"),
        pydantic.Field(alias="hideFromRegularPurchase", description="True if this category doesn't allow purchases."),
    ] = None
    """
    True if this category doesn't allow purchases.
    """

    hide_if_no_currency: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hideIfNoCurrency"),
        pydantic.Field(
            alias="hideIfNoCurrency",
            description="If you don't have the currency required to buy items from this category, should the items be hidden?",
        ),
    ] = None
    """
    If you don't have the currency required to buy items from this category, should the items be hidden?
    """

    is_display_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isDisplayOnly"),
        pydantic.Field(
            alias="isDisplayOnly",
            description="If true, this category only displays items: you can't purchase anything in them.",
        ),
    ] = None
    """
    If true, this category only displays items: you can't purchase anything in them.
    """

    is_preview: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPreview"),
        pydantic.Field(
            alias="isPreview",
            description="Sometimes a category isn't actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment.",
        ),
    ] = None
    """
    Sometimes a category isn't actually used to sell items, but rather to preview them. This implies different UI (and manual placement of the category in the UI) in the game, and special treatment.
    """

    overlay: typing.Optional[DestinyDefinitionsDestinyVendorCategoryOverlayDefinition] = pydantic.Field(default=None)
    """
    If this category has an overlay prompt that should appear, this contains the details of that prompt.
    """

    quantity_available: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="quantityAvailable"),
        pydantic.Field(
            alias="quantityAvailable",
            description="The amount of items that will be available when this category is shown.",
        ),
    ] = None
    """
    The amount of items that will be available when this category is shown.
    """

    reset_interval_minutes_override: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="resetIntervalMinutesOverride"),
        pydantic.Field(alias="resetIntervalMinutesOverride"),
    ] = None
    reset_offset_minutes_override: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="resetOffsetMinutesOverride"),
        pydantic.Field(alias="resetOffsetMinutesOverride"),
    ] = None
    show_unavailable_items: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="showUnavailableItems"),
        pydantic.Field(
            alias="showUnavailableItems",
            description="If items aren't up for sale in this category, should we still show them (greyed out)?",
        ),
    ] = None
    """
    If items aren't up for sale in this category, should we still show them (greyed out)?
    """

    sort_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="sortValue"),
        pydantic.Field(
            alias="sortValue",
            description="Used in sorting items in vendors... but there's a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself.",
        ),
    ] = None
    """
    Used in sorting items in vendors... but there's a lot more to it. Just go with the order provided in the itemIndexes property on the DestinyVendorCategoryComponent instead, it should be more reliable than trying to recalculate it yourself.
    """

    vendor_item_indexes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="vendorItemIndexes"),
        pydantic.Field(
            alias="vendorItemIndexes",
            description="A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime.",
        ),
    ] = None
    """
    A shortcut for the vendor item indexes sold under this category. Saves us from some expensive reorganization at runtime.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
