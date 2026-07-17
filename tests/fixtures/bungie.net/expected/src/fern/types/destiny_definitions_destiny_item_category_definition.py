

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyItemCategoryDefinition(UniversalBaseModel):
    """
    In an attempt to categorize items by type, usage, and other interesting properties, we created DestinyItemCategoryDefinition: information about types that is assembled using a set of heuristics that examine the properties of an item such as what inventory bucket it's in, its item type name, and whether it has or is missing certain blocks of data.
    This heuristic is imperfect, however. If you find an item miscategorized, let us know on the Bungie API forums!
    We then populate all of the categories that we think an item belongs to in its DestinyInventoryItemDefinition.itemCategoryHashes property. You can use that to provide your own custom item filtering, sorting, aggregating... go nuts on it! And let us know if you see more categories that you wish would be added!
    """

    deprecated: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If True, this category has been deprecated: it may have no items left, or there may be only legacy items that remain in it which are no longer relevant to the game.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    grant_destiny_breaker_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="grantDestinyBreakerType"),
        pydantic.Field(
            alias="grantDestinyBreakerType",
            description="If the item in question has this category, it also should have this breaker type.",
        ),
    ] = None
    """
    If the item in question has this category, it also should have this breaker type.
    """

    grant_destiny_class: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="grantDestinyClass"),
        pydantic.Field(
            alias="grantDestinyClass",
            description='If an item belongs to this category, it will also get this class restriction enum value.\r\nSee the other "grant"-prefixed properties on this definition for my color commentary.',
        ),
    ] = None
    """
    If an item belongs to this category, it will also get this class restriction enum value.
    See the other "grant"-prefixed properties on this definition for my color commentary.
    """

    grant_destiny_item_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="grantDestinyItemType"),
        pydantic.Field(
            alias="grantDestinyItemType",
            description="If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol.",
        ),
    ] = None
    """
    If an item belongs to this category, it will also receive this item type. This is now how DestinyItemType is populated for items: it used to be an even jankier process, but that's a story that requires more alcohol.
    """

    grant_destiny_sub_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="grantDestinySubType"),
        pydantic.Field(
            alias="grantDestinySubType",
            description="If an item belongs to this category, it will also receive this subtype enum value.\r\nI know what you're thinking - what if it belongs to multiple categories that provide sub-types?\r\nThe last one processed wins, as is the case with all of these \"grant\" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they?",
        ),
    ] = None
    """
    If an item belongs to this category, it will also receive this subtype enum value.
    I know what you're thinking - what if it belongs to multiple categories that provide sub-types?
    The last one processed wins, as is the case with all of these "grant" enums. Now you can see one reason why we moved away from these enums... but they're so convenient when they work, aren't they?
    """

    group_category_only: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="groupCategoryOnly"),
        pydantic.Field(
            alias="groupCategoryOnly",
            description="If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories.",
        ),
    ] = None
    """
    If true, this category is only used for grouping, and should not be evaluated with its own checks. Rather, the item only has this category if it has one of its child categories.
    """

    grouped_category_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="groupedCategoryHashes"),
        pydantic.Field(
            alias="groupedCategoryHashes",
            description='If this category is a "parent" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition.\r\nIn this way, you can build up a visual hierarchy of item categories. That\'s what we did, and you can do it too. I believe in you. Yes, you, Carl.\r\n(I hope someone named Carl reads this someday)',
        ),
    ] = None
    """
    If this category is a "parent" category of other categories, those children will have their hashes listed in rendering order here, and can be looked up using these hashes against DestinyItemCategoryDefinition.
    In this way, you can build up a visual hierarchy of item categories. That's what we did, and you can do it too. I believe in you. Yes, you, Carl.
    (I hope someone named Carl reads this someday)
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

    item_type_regex: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemTypeRegex"),
        pydantic.Field(
            alias="itemTypeRegex",
            description="The janky regular expression we used against the item type to try and discern whether the item belongs to this category.",
        ),
    ] = None
    """
    The janky regular expression we used against the item type to try and discern whether the item belongs to this category.
    """

    item_type_regex_not: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemTypeRegexNot"),
        pydantic.Field(
            alias="itemTypeRegexNot",
            description="If the item type matches this janky regex, it does *not* belong to this category.",
        ),
    ] = None
    """
    If the item type matches this janky regex, it does *not* belong to this category.
    """

    origin_bucket_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="originBucketIdentifier"),
        pydantic.Field(
            alias="originBucketIdentifier",
            description="If the item belongs to this bucket, it does belong to this category.",
        ),
    ] = None
    """
    If the item belongs to this bucket, it does belong to this category.
    """

    parent_category_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="parentCategoryHashes"),
        pydantic.Field(
            alias="parentCategoryHashes",
            description='All item category hashes of "parent" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It\'s a bit redundant, but having this child-centric list speeds up some calculations.',
        ),
    ] = None
    """
    All item category hashes of "parent" categories: categories that contain this as a child through the hierarchy of groupedCategoryHashes. It's a bit redundant, but having this child-centric list speeds up some calculations.
    """

    plug_category_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="plugCategoryIdentifier"),
        pydantic.Field(
            alias="plugCategoryIdentifier",
            description="If the item is a plug, this is the identifier we expect to find associated with it if it is in this category.",
        ),
    ] = None
    """
    If the item is a plug, this is the identifier we expect to find associated with it if it is in this category.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    short_title: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="shortTitle"),
        pydantic.Field(
            alias="shortTitle",
            description="A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet.",
        ),
    ] = None
    """
    A shortened version of the title. The reason why we have this is because the Armory in German had titles that were too long to display in our UI, so these were localized abbreviated versions of those categories. The property still exists today, even though the Armory doesn't exist for D2... yet.
    """

    trait_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="traitId"),
        pydantic.Field(
            alias="traitId", description="The traitId that can be found on items that belong to this category."
        ),
    ] = None
    """
    The traitId that can be found on items that belong to this category.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If True, this category should be visible in UI. Sometimes we make categories that we don't think are interesting externally. It's up to you if you want to skip on showing them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
