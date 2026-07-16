

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_animations_destiny_animation_reference import (
    DestinyDefinitionsAnimationsDestinyAnimationReference,
)
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_equipping_block_definition import DestinyDefinitionsDestinyEquippingBlockDefinition
from .destiny_definitions_destiny_item_action_block_definition import DestinyDefinitionsDestinyItemActionBlockDefinition
from .destiny_definitions_destiny_item_crafting_block_definition import (
    DestinyDefinitionsDestinyItemCraftingBlockDefinition,
)
from .destiny_definitions_destiny_item_gearset_block_definition import (
    DestinyDefinitionsDestinyItemGearsetBlockDefinition,
)
from .destiny_definitions_destiny_item_inventory_block_definition import (
    DestinyDefinitionsDestinyItemInventoryBlockDefinition,
)
from .destiny_definitions_destiny_item_investment_stat_definition import (
    DestinyDefinitionsDestinyItemInvestmentStatDefinition,
)
from .destiny_definitions_destiny_item_metric_block_definition import DestinyDefinitionsDestinyItemMetricBlockDefinition
from .destiny_definitions_destiny_item_objective_block_definition import (
    DestinyDefinitionsDestinyItemObjectiveBlockDefinition,
)
from .destiny_definitions_destiny_item_perk_entry_definition import DestinyDefinitionsDestinyItemPerkEntryDefinition
from .destiny_definitions_destiny_item_preview_block_definition import (
    DestinyDefinitionsDestinyItemPreviewBlockDefinition,
)
from .destiny_definitions_destiny_item_quality_block_definition import (
    DestinyDefinitionsDestinyItemQualityBlockDefinition,
)
from .destiny_definitions_destiny_item_sack_block_definition import DestinyDefinitionsDestinyItemSackBlockDefinition
from .destiny_definitions_destiny_item_set_block_definition import DestinyDefinitionsDestinyItemSetBlockDefinition
from .destiny_definitions_destiny_item_socket_block_definition import DestinyDefinitionsDestinyItemSocketBlockDefinition
from .destiny_definitions_destiny_item_source_block_definition import DestinyDefinitionsDestinyItemSourceBlockDefinition
from .destiny_definitions_destiny_item_stat_block_definition import DestinyDefinitionsDestinyItemStatBlockDefinition
from .destiny_definitions_destiny_item_summary_block_definition import (
    DestinyDefinitionsDestinyItemSummaryBlockDefinition,
)
from .destiny_definitions_destiny_item_talent_grid_block_definition import (
    DestinyDefinitionsDestinyItemTalentGridBlockDefinition,
)
from .destiny_definitions_destiny_item_tooltip_notification import DestinyDefinitionsDestinyItemTooltipNotification
from .destiny_definitions_destiny_item_translation_block_definition import (
    DestinyDefinitionsDestinyItemTranslationBlockDefinition,
)
from .destiny_definitions_destiny_item_value_block_definition import DestinyDefinitionsDestinyItemValueBlockDefinition
from .destiny_definitions_items_destiny_item_plug_definition import DestinyDefinitionsItemsDestinyItemPlugDefinition
from .destiny_misc_destiny_color import DestinyMiscDestinyColor
from .links_hyperlink_reference import LinksHyperlinkReference


class DestinyDefinitionsDestinyInventoryItemDefinition(UniversalBaseModel):
    """
    So much of what you see in Destiny is actually an Item used in a new and creative way. This is the definition for Items in Destiny, which started off as just entities that could exist in your Inventory but ended up being the backing data for so much more: quests, reward previews, slots, and subclasses.
    In practice, you will want to associate this data with "live" item data from a Bungie.Net Platform call: these definitions describe the item in generic, non-instanced terms: but an actual instance of an item can vary widely from these generic definitions.
    """

    action: typing.Optional[DestinyDefinitionsDestinyItemActionBlockDefinition] = pydantic.Field(default=None)
    """
    If the item can be "used", this block will be non-null, and will have data related to the action performed when using the item. (Guess what? 99% of the time, this action is "dismantle". Shocker)
    """

    allow_actions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="allowActions"),
        pydantic.Field(
            alias="allowActions",
            description="BNet may forbid the execution of actions on this item via the API. If that is occurring, allowActions will be set to false.",
        ),
    ] = None
    """
    BNet may forbid the execution of actions on this item via the API. If that is occurring, allowActions will be set to false.
    """

    animations: typing.Optional[typing.List[DestinyDefinitionsAnimationsDestinyAnimationReference]] = pydantic.Field(
        default=None
    )
    """
    If any animations were extracted from game content for this item, these will be the definitions of those animations.
    """

    background_color: typing_extensions.Annotated[
        typing.Optional[DestinyMiscDestinyColor],
        FieldMetadata(alias="backgroundColor"),
        pydantic.Field(
            alias="backgroundColor",
            description='Sometimes, an item will have a background color. Most notably this occurs with Emblems, who use the Background Color for small character nameplates such as the "friends" view you see in-game. There are almost certainly other items that have background color as well, though I have not bothered to investigate what items have it nor what purposes they serve: use it as you will.',
        ),
    ] = None
    """
    Sometimes, an item will have a background color. Most notably this occurs with Emblems, who use the Background Color for small character nameplates such as the "friends" view you see in-game. There are almost certainly other items that have background color as well, though I have not bothered to investigate what items have it nor what purposes they serve: use it as you will.
    """

    breaker_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="breakerType"),
        pydantic.Field(
            alias="breakerType",
            description='Some weapons and plugs can have a "Breaker Type": a special ability that works sort of like damage type vulnerabilities. This is (almost?) always set on items by plugs.',
        ),
    ] = None
    """
    Some weapons and plugs can have a "Breaker Type": a special ability that works sort of like damage type vulnerabilities. This is (almost?) always set on items by plugs.
    """

    breaker_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="breakerTypeHash"),
        pydantic.Field(
            alias="breakerTypeHash",
            description="Since we also have a breaker type definition, this is the hash for that breaker type for your convenience. Whether you use the enum or hash and look up the definition depends on what's cleanest for your code.",
        ),
    ] = None
    """
    Since we also have a breaker type definition, this is the hash for that breaker type for your convenience. Whether you use the enum or hash and look up the definition depends on what's cleanest for your code.
    """

    class_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="classType"),
        pydantic.Field(
            alias="classType",
            description="We run a similarly weak-sauce algorithm to try and determine whether an item is restricted to a specific class. If we find it to be restricted in such a way, we set this classType property to match the class' enumeration value so that users can easily identify class restricted items.\r\nIf you see a mis-classed item, please inform the developers in the Bungie API forum.",
        ),
    ] = None
    """
    We run a similarly weak-sauce algorithm to try and determine whether an item is restricted to a specific class. If we find it to be restricted in such a way, we set this classType property to match the class' enumeration value so that users can easily identify class restricted items.
    If you see a mis-classed item, please inform the developers in the Bungie API forum.
    """

    collectible_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="collectibleHash"),
        pydantic.Field(
            alias="collectibleHash",
            description="If this item has a collectible related to it, this is the hash identifier of that collectible entry.",
        ),
    ] = None
    """
    If this item has a collectible related to it, this is the hash identifier of that collectible entry.
    """

    crafting: typing.Optional[DestinyDefinitionsDestinyItemCraftingBlockDefinition] = pydantic.Field(default=None)
    """
    Recipe items will have relevant crafting information available here.
    """

    damage_type_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="damageTypeHashes"),
        pydantic.Field(
            alias="damageTypeHashes",
            description="Theoretically, an item can have many possible damage types. In *practice*, this is not true, but just in case weapons start being made that have multiple (for instance, an item where a socket has reusable plugs for every possible damage type that you can choose from freely), this field will return all of the possible damage types that are available to the weapon by default.",
        ),
    ] = None
    """
    Theoretically, an item can have many possible damage types. In *practice*, this is not true, but just in case weapons start being made that have multiple (for instance, an item where a socket has reusable plugs for every possible damage type that you can choose from freely), this field will return all of the possible damage types that are available to the weapon by default.
    """

    damage_types: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="damageTypes"),
        pydantic.Field(
            alias="damageTypes",
            description="This is the list of all damage types that we know ahead of time the item can take on. Unfortunately, this does not preclude the possibility of something funky happening to give the item a damage type that cannot be predicted beforehand: for example, if some designer decides to create arbitrary non-reusable plugs that cause damage type to change.\r\nThis damage type prediction will only use the following to determine potential damage types:\r\n- Intrinsic perks\r\n- Talent Node perks\r\n- Known, reusable plugs for sockets",
        ),
    ] = None
    """
    This is the list of all damage types that we know ahead of time the item can take on. Unfortunately, this does not preclude the possibility of something funky happening to give the item a damage type that cannot be predicted beforehand: for example, if some designer decides to create arbitrary non-reusable plugs that cause damage type to change.
    This damage type prediction will only use the following to determine potential damage types:
    - Intrinsic perks
    - Talent Node perks
    - Known, reusable plugs for sockets
    """

    default_damage_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="defaultDamageType"),
        pydantic.Field(
            alias="defaultDamageType",
            description="If the item has a damage type that could be considered to be default, it will be populated here.\r\nFor various upsetting reasons, it's surprisingly cumbersome to figure this out. I hope you're happy.",
        ),
    ] = None
    """
    If the item has a damage type that could be considered to be default, it will be populated here.
    For various upsetting reasons, it's surprisingly cumbersome to figure this out. I hope you're happy.
    """

    default_damage_type_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="defaultDamageTypeHash"),
        pydantic.Field(
            alias="defaultDamageTypeHash",
            description="Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition.\r\nI will likely regret leaving in the enumeration versions of these properties, but for now they're very convenient.",
        ),
    ] = None
    """
    Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition.
    I will likely regret leaving in the enumeration versions of these properties, but for now they're very convenient.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    display_source: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displaySource"),
        pydantic.Field(
            alias="displaySource",
            description="In theory, it is a localized string telling you about how you can find the item. I really wish this was more consistent. Many times, it has nothing. Sometimes, it's instead a more narrative-forward description of the item. Which is cool, and I wish all properties had that data, but it should really be its own property.",
        ),
    ] = None
    """
    In theory, it is a localized string telling you about how you can find the item. I really wish this was more consistent. Many times, it has nothing. Sometimes, it's instead a more narrative-forward description of the item. Which is cool, and I wish all properties had that data, but it should really be its own property.
    """

    does_postmaster_pull_have_side_effects: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="doesPostmasterPullHaveSideEffects"),
        pydantic.Field(
            alias="doesPostmasterPullHaveSideEffects",
            description='The boolean will indicate to us (and you!) whether something *could* happen when you transfer this item from the Postmaster that might be considered a "destructive" action.\r\nIt is not feasible currently to tell you (or ourelves!) in a consistent way whether this *will* actually cause a destructive action, so we are playing it safe: if it has the potential to do so, we will not allow it to be transferred from the Postmaster by default. You will need to check for this flag before transferring an item from the Postmaster, or else you\'ll end up receiving an error.',
        ),
    ] = None
    """
    The boolean will indicate to us (and you!) whether something *could* happen when you transfer this item from the Postmaster that might be considered a "destructive" action.
    It is not feasible currently to tell you (or ourelves!) in a consistent way whether this *will* actually cause a destructive action, so we are playing it safe: if it has the potential to do so, we will not allow it to be transferred from the Postmaster by default. You will need to check for this flag before transferring an item from the Postmaster, or else you'll end up receiving an error.
    """

    emblem_objective_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="emblemObjectiveHash"),
        pydantic.Field(
            alias="emblemObjectiveHash",
            description="If the item is an emblem that has a special Objective attached to it - for instance, if the emblem tracks PVP Kills, or what-have-you. This is a bit different from, for example, the Vanguard Kill Tracker mod, which pipes data into the \"art channel\". When I get some time, I would like to standardize these so you can get at the values they expose without having to care about what they're being used for and how they are wired up, but for now here's the raw data.",
        ),
    ] = None
    """
    If the item is an emblem that has a special Objective attached to it - for instance, if the emblem tracks PVP Kills, or what-have-you. This is a bit different from, for example, the Vanguard Kill Tracker mod, which pipes data into the "art channel". When I get some time, I would like to standardize these so you can get at the values they expose without having to care about what they're being used for and how they are wired up, but for now here's the raw data.
    """

    equippable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, then you will be allowed to equip the item if you pass its other requirements.
    This being false means that you cannot equip the item under any circumstances.
    """

    equipping_block: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyEquippingBlockDefinition],
        FieldMetadata(alias="equippingBlock"),
        pydantic.Field(
            alias="equippingBlock",
            description="If this item can be equipped, this block will be non-null and will be populated with the conditions under which it can be equipped.",
        ),
    ] = None
    """
    If this item can be equipped, this block will be non-null and will be populated with the conditions under which it can be equipped.
    """

    flavor_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="flavorText"), pydantic.Field(alias="flavorText")
    ] = None
    gearset: typing.Optional[DestinyDefinitionsDestinyItemGearsetBlockDefinition] = pydantic.Field(default=None)
    """
    If this item has related items in a "Gear Set", this will be non-null and the relationships defined herein.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    icon_watermark: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iconWatermark"),
        pydantic.Field(
            alias="iconWatermark",
            description="If available, this is the original 'active' release watermark overlay for the icon. If the item has different versions, this can be overridden by the 'display version watermark icon' from the 'quality' block. Alternatively, if there is no watermark for the version, and the item version has a power cap below the current season power cap, this can be overridden by the iconWatermarkShelved property.",
        ),
    ] = None
    """
    If available, this is the original 'active' release watermark overlay for the icon. If the item has different versions, this can be overridden by the 'display version watermark icon' from the 'quality' block. Alternatively, if there is no watermark for the version, and the item version has a power cap below the current season power cap, this can be overridden by the iconWatermarkShelved property.
    """

    icon_watermark_shelved: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="iconWatermarkShelved"),
        pydantic.Field(
            alias="iconWatermarkShelved",
            description="If available, this is the 'shelved' release watermark overlay for the icon. If the item version has a power cap below the current season power cap, it can be treated as 'shelved', and should be shown with this 'shelved' watermark overlay.",
        ),
    ] = None
    """
    If available, this is the 'shelved' release watermark overlay for the icon. If the item version has a power cap below the current season power cap, it can be treated as 'shelved', and should be shown with this 'shelved' watermark overlay.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    inventory: typing.Optional[DestinyDefinitionsDestinyItemInventoryBlockDefinition] = pydantic.Field(default=None)
    """
    If this item can exist in an inventory, this block will be non-null. In practice, every item that currently exists has one of these blocks. But note that it is not necessarily guaranteed.
    """

    investment_stats: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemInvestmentStatDefinition]],
        FieldMetadata(alias="investmentStats"),
        pydantic.Field(
            alias="investmentStats",
            description='If the item has stats, this block will be defined. It has the "raw" investment stats for the item. These investment stats don\'t take into account the ways that the items can spawn, nor do they take into account any Stat Group transformations. I have retained them for debugging purposes, but I do not know how useful people will find them.',
        ),
    ] = None
    """
    If the item has stats, this block will be defined. It has the "raw" investment stats for the item. These investment stats don't take into account the ways that the items can spawn, nor do they take into account any Stat Group transformations. I have retained them for debugging purposes, but I do not know how useful people will find them.
    """

    is_wrapper: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isWrapper"),
        pydantic.Field(
            alias="isWrapper",
            description='If true, this is a dummy vendor-wrapped item template. Items purchased from Eververse will be "wrapped" by one of these items so that we can safely provide refund capabilities before the item is "unwrapped".',
        ),
    ] = None
    """
    If true, this is a dummy vendor-wrapped item template. Items purchased from Eververse will be "wrapped" by one of these items so that we can safely provide refund capabilities before the item is "unwrapped".
    """

    item_category_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="itemCategoryHashes"),
        pydantic.Field(
            alias="itemCategoryHashes",
            description='BNet attempts to make a more formal definition of item "Categories", as defined by DestinyItemCategoryDefinition. This is a list of all Categories that we were able to algorithmically determine that this item is a member of. (for instance, that it\'s a "Weapon", that it\'s an "Auto Rifle", etc...)\r\nThe algorithm for these is, unfortunately, volatile. If you believe you see a miscategorized item, please let us know on the Bungie API forums.',
        ),
    ] = None
    """
    BNet attempts to make a more formal definition of item "Categories", as defined by DestinyItemCategoryDefinition. This is a list of all Categories that we were able to algorithmically determine that this item is a member of. (for instance, that it's a "Weapon", that it's an "Auto Rifle", etc...)
    The algorithm for these is, unfortunately, volatile. If you believe you see a miscategorized item, please let us know on the Bungie API forums.
    """

    item_sub_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemSubType"),
        pydantic.Field(
            alias="itemSubType",
            description='A value indicating the "sub-type" of the item. For instance, where an item might have an itemType value "Weapon", this will be something more specific like "Auto Rifle".\r\nitemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.',
        ),
    ] = None
    """
    A value indicating the "sub-type" of the item. For instance, where an item might have an itemType value "Weapon", this will be something more specific like "Auto Rifle".
    itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.
    """

    item_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemType"),
        pydantic.Field(
            alias="itemType",
            description='A value indicating the "base" the of the item. This enum is a useful but dramatic oversimplification of what it means for an item to have a "Type". Still, it\'s handy in many situations.\r\nitemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.',
        ),
    ] = None
    """
    A value indicating the "base" the of the item. This enum is a useful but dramatic oversimplification of what it means for an item to have a "Type". Still, it's handy in many situations.
    itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.
    """

    item_type_and_tier_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemTypeAndTierDisplayName"),
        pydantic.Field(
            alias="itemTypeAndTierDisplayName",
            description="It became a common enough pattern in our UI to show Item Type and Tier combined into a single localized string that I'm just going to go ahead and start pre-creating these for items.",
        ),
    ] = None
    """
    It became a common enough pattern in our UI to show Item Type and Tier combined into a single localized string that I'm just going to go ahead and start pre-creating these for items.
    """

    item_type_display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemTypeDisplayName"),
        pydantic.Field(
            alias="itemTypeDisplayName",
            description="The localized title/name of the item's type. This can be whatever the designers want, and has no guarantee of consistency between items.",
        ),
    ] = None
    """
    The localized title/name of the item's type. This can be whatever the designers want, and has no guarantee of consistency between items.
    """

    links: typing.Optional[typing.List[LinksHyperlinkReference]] = pydantic.Field(default=None)
    """
    If we added any help or informational URLs about this item, these will be those links.
    """

    lore_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="loreHash"),
        pydantic.Field(
            alias="loreHash",
            description="If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can use to look up the lore definition.",
        ),
    ] = None
    """
    If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can use to look up the lore definition.
    """

    metrics: typing.Optional[DestinyDefinitionsDestinyItemMetricBlockDefinition] = pydantic.Field(default=None)
    """
    If this item has available metrics to be shown, this block will be non-null have the appropriate hashes defined.
    """

    non_transferrable: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="nonTransferrable"),
        pydantic.Field(
            alias="nonTransferrable",
            description="The intrinsic transferability of an item.\r\nI hate that this boolean is negative - but there's a reason.\r\nJust because an item is intrinsically transferrable doesn't mean that it can be transferred, and we don't want to imply that this is the only source of that transferability.",
        ),
    ] = None
    """
    The intrinsic transferability of an item.
    I hate that this boolean is negative - but there's a reason.
    Just because an item is intrinsically transferrable doesn't mean that it can be transferred, and we don't want to imply that this is the only source of that transferability.
    """

    objectives: typing.Optional[DestinyDefinitionsDestinyItemObjectiveBlockDefinition] = pydantic.Field(default=None)
    """
    If this item has Objectives (extra tasks that can be accomplished related to the item... most frequently when the item is a Quest Step and the Objectives need to be completed to move on to the next Quest Step), this block will be non-null and the objectives defined herein.
    """

    perks: typing.Optional[typing.List[DestinyDefinitionsDestinyItemPerkEntryDefinition]] = pydantic.Field(default=None)
    """
    If the item has any *intrinsic* Perks (Perks that it will provide regardless of Sockets, Talent Grid, and other transitory state), they will be defined here.
    """

    plug: typing.Optional[DestinyDefinitionsItemsDestinyItemPlugDefinition] = pydantic.Field(default=None)
    """
    If this item *is* a Plug, this will be non-null and the info defined herein. See DestinyItemPlugDefinition for more information.
    """

    preview: typing.Optional[DestinyDefinitionsDestinyItemPreviewBlockDefinition] = pydantic.Field(default=None)
    """
    If this item can be Used or Acquired to gain other items (for instance, how Eververse Boxes can be consumed to get items from the box), this block will be non-null and will give summary information for the items that can be acquired.
    """

    quality: typing.Optional[DestinyDefinitionsDestinyItemQualityBlockDefinition] = pydantic.Field(default=None)
    """
    If this item can have a level or stats, this block will be non-null and will be populated with default quality (item level, "quality", and infusion) data. See the block for more details, there's often less upfront information in D2 so you'll want to be aware of how you use quality and item level on the definition level now.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    sack: typing.Optional[DestinyDefinitionsDestinyItemSackBlockDefinition] = pydantic.Field(default=None)
    """
    If this item is a "reward sack" that can be opened to provide other items, this will be non-null and the properties of the sack contained herein.
    """

    screenshot: typing.Optional[str] = pydantic.Field(default=None)
    """
    If we were able to acquire an in-game screenshot for the item, the path to that screenshot will be returned here. Note that not all items have screenshots: particularly not any non-equippable items.
    """

    season_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="seasonHash"),
        pydantic.Field(
            alias="seasonHash",
            description="If this item is related directly to a Season of Destiny, this is the hash identifier for that season.",
        ),
    ] = None
    """
    If this item is related directly to a Season of Destiny, this is the hash identifier for that season.
    """

    secondary_icon: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="secondaryIcon"),
        pydantic.Field(
            alias="secondaryIcon",
            description="A secondary icon associated with the item. Currently this is used in very context specific applications, such as Emblem Nameplates.",
        ),
    ] = None
    """
    A secondary icon associated with the item. Currently this is used in very context specific applications, such as Emblem Nameplates.
    """

    secondary_overlay: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="secondaryOverlay"),
        pydantic.Field(
            alias="secondaryOverlay",
            description='Pulled from the secondary icon, this is the "secondary background" of the secondary icon. Confusing? Sure, that\'s why I call it "overlay" here: because as far as it\'s been used thus far, it has been for an optional overlay image. We\'ll see if that holds up, but at least for now it explains what this image is a bit better.',
        ),
    ] = None
    """
    Pulled from the secondary icon, this is the "secondary background" of the secondary icon. Confusing? Sure, that's why I call it "overlay" here: because as far as it's been used thus far, it has been for an optional overlay image. We'll see if that holds up, but at least for now it explains what this image is a bit better.
    """

    secondary_special: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="secondarySpecial"),
        pydantic.Field(
            alias="secondarySpecial",
            description='Pulled from the Secondary Icon, this is the "special" background for the item. For Emblems, this is the background image used on the Details view: but it need not be limited to that for other types of items.',
        ),
    ] = None
    """
    Pulled from the Secondary Icon, this is the "special" background for the item. For Emblems, this is the background image used on the Details view: but it need not be limited to that for other types of items.
    """

    set_data: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyItemSetBlockDefinition],
        FieldMetadata(alias="setData"),
        pydantic.Field(
            alias="setData",
            description="If this item is a quest, this block will be non-null. In practice, I wish I had called this the Quest block, but at the time it wasn't clear to me whether it would end up being used for purposes other than quests. It will contain data about the steps in the quest, and mechanics we can use for displaying and tracking the quest.",
        ),
    ] = None
    """
    If this item is a quest, this block will be non-null. In practice, I wish I had called this the Quest block, but at the time it wasn't clear to me whether it would end up being used for purposes other than quests. It will contain data about the steps in the quest, and mechanics we can use for displaying and tracking the quest.
    """

    sockets: typing.Optional[DestinyDefinitionsDestinyItemSocketBlockDefinition] = pydantic.Field(default=None)
    """
    If this item has any Sockets, this will be non-null and the individual sockets on the item will be defined herein.
    """

    source_data: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyItemSourceBlockDefinition],
        FieldMetadata(alias="sourceData"),
        pydantic.Field(
            alias="sourceData",
            description="If this item has a known source, this block will be non-null and populated with source information. Unfortunately, at this time we are not generating sources: that is some aggressively manual work which we didn't have time for, and I'm hoping to get back to at some point in the future.",
        ),
    ] = None
    """
    If this item has a known source, this block will be non-null and populated with source information. Unfortunately, at this time we are not generating sources: that is some aggressively manual work which we didn't have time for, and I'm hoping to get back to at some point in the future.
    """

    special_item_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="specialItemType"),
        pydantic.Field(
            alias="specialItemType",
            description="In Destiny 1, we identified some items as having particular categories that we'd like to know about for various internal logic purposes. These are defined in SpecialItemType, and while these days the itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.",
        ),
    ] = None
    """
    In Destiny 1, we identified some items as having particular categories that we'd like to know about for various internal logic purposes. These are defined in SpecialItemType, and while these days the itemCategoryHashes are the preferred way of identifying types, we have retained this enum for its convenience.
    """

    stats: typing.Optional[DestinyDefinitionsDestinyItemStatBlockDefinition] = pydantic.Field(default=None)
    """
    If this item can have stats (such as a weapon, armor, or vehicle), this block will be non-null and populated with the stats found on the item.
    """

    summary: typing.Optional[DestinyDefinitionsDestinyItemSummaryBlockDefinition] = pydantic.Field(default=None)
    """
    Summary data about the item.
    """

    summary_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="summaryItemHash"),
        pydantic.Field(
            alias="summaryItemHash",
            description='There are times when the game will show you a "summary/vague" version of an item - such as a description of its type represented as a DestinyInventoryItemDefinition - rather than display the item itself.\r\nThis happens sometimes when summarizing possible rewards in a tooltip. This is the item displayed instead, if it exists.',
        ),
    ] = None
    """
    There are times when the game will show you a "summary/vague" version of an item - such as a description of its type represented as a DestinyInventoryItemDefinition - rather than display the item itself.
    This happens sometimes when summarizing possible rewards in a tooltip. This is the item displayed instead, if it exists.
    """

    talent_grid: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyItemTalentGridBlockDefinition],
        FieldMetadata(alias="talentGrid"),
        pydantic.Field(
            alias="talentGrid",
            description='If the item has a Talent Grid, this will be non-null and the properties of the grid defined herein. Note that, while many items still have talent grids, the only ones with meaningful Nodes still on them will be Subclass/"Build" items.',
        ),
    ] = None
    """
    If the item has a Talent Grid, this will be non-null and the properties of the grid defined herein. Note that, while many items still have talent grids, the only ones with meaningful Nodes still on them will be Subclass/"Build" items.
    """

    tooltip_notifications: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyItemTooltipNotification]],
        FieldMetadata(alias="tooltipNotifications"),
        pydantic.Field(
            alias="tooltipNotifications",
            description="Tooltips that only come up conditionally for the item. Check the live data DestinyItemComponent.tooltipNotificationIndexes property for which of these should be shown at runtime.",
        ),
    ] = None
    """
    Tooltips that only come up conditionally for the item. Check the live data DestinyItemComponent.tooltipNotificationIndexes property for which of these should be shown at runtime.
    """

    tooltip_style: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tooltipStyle"),
        pydantic.Field(
            alias="tooltipStyle",
            description="An identifier that the game UI uses to determine what type of tooltip to show for the item. These have no corresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differently according to these styles (or ignore it).",
        ),
    ] = None
    """
    An identifier that the game UI uses to determine what type of tooltip to show for the item. These have no corresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differently according to these styles (or ignore it).
    """

    trait_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="traitHashes"),
        pydantic.Field(
            alias="traitHashes",
            description="These are the corresponding trait definition hashes for the entries in traitIds.",
        ),
    ] = None
    """
    These are the corresponding trait definition hashes for the entries in traitIds.
    """

    trait_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="traitIds"),
        pydantic.Field(
            alias="traitIds",
            description="Traits are metadata tags applied to this item. For example: armor slot, weapon type, foundry, faction, etc. These IDs come from the game and don't map to any content, but should still be useful.",
        ),
    ] = None
    """
    Traits are metadata tags applied to this item. For example: armor slot, weapon type, foundry, faction, etc. These IDs come from the game and don't map to any content, but should still be useful.
    """

    translation_block: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyItemTranslationBlockDefinition],
        FieldMetadata(alias="translationBlock"),
        pydantic.Field(
            alias="translationBlock",
            description="If this item can be rendered, this block will be non-null and will be populated with rendering information.",
        ),
    ] = None
    """
    If this item can be rendered, this block will be non-null and will be populated with rendering information.
    """

    ui_item_display_style: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uiItemDisplayStyle"),
        pydantic.Field(
            alias="uiItemDisplayStyle",
            description="A string identifier that the game's UI uses to determine how the item should be rendered in inventory screens and the like. This could really be anything - at the moment, we don't have the time to really breakdown and maintain all the possible strings this could be, partly because new ones could be added ad hoc. But if you want to use it to dictate your own UI, or look for items with a certain display style, go for it!",
        ),
    ] = None
    """
    A string identifier that the game's UI uses to determine how the item should be rendered in inventory screens and the like. This could really be anything - at the moment, we don't have the time to really breakdown and maintain all the possible strings this could be, partly because new ones could be added ad hoc. But if you want to use it to dictate your own UI, or look for items with a certain display style, go for it!
    """

    value: typing.Optional[DestinyDefinitionsDestinyItemValueBlockDefinition] = pydantic.Field(default=None)
    """
    The conceptual "Value" of an item, if any was defined. See the DestinyItemValueBlockDefinition for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
