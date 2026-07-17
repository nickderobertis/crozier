

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dates_date_range import DatesDateRange
from .destiny_definitions_destiny_display_category_definition import DestinyDefinitionsDestinyDisplayCategoryDefinition
from .destiny_definitions_destiny_vendor_accepted_item_definition import (
    DestinyDefinitionsDestinyVendorAcceptedItemDefinition,
)
from .destiny_definitions_destiny_vendor_action_definition import DestinyDefinitionsDestinyVendorActionDefinition
from .destiny_definitions_destiny_vendor_category_entry_definition import (
    DestinyDefinitionsDestinyVendorCategoryEntryDefinition,
)
from .destiny_definitions_destiny_vendor_display_properties_definition import (
    DestinyDefinitionsDestinyVendorDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_vendor_group_reference import DestinyDefinitionsDestinyVendorGroupReference
from .destiny_definitions_destiny_vendor_interaction_definition import (
    DestinyDefinitionsDestinyVendorInteractionDefinition,
)
from .destiny_definitions_destiny_vendor_inventory_flyout_definition import (
    DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition,
)
from .destiny_definitions_destiny_vendor_item_definition import DestinyDefinitionsDestinyVendorItemDefinition
from .destiny_definitions_destiny_vendor_service_definition import DestinyDefinitionsDestinyVendorServiceDefinition
from .destiny_definitions_vendors_destiny_vendor_location_definition import (
    DestinyDefinitionsVendorsDestinyVendorLocationDefinition,
)


class DestinyDefinitionsDestinyVendorDefinition(UniversalBaseModel):
    """
    These are the definitions for Vendors.
    In Destiny, a Vendor can be a lot of things - some things that you wouldn't expect, and some things that you don't even see directly in the game. Vendors are the Dolly Levi of the Destiny universe.
    - Traditional Vendors as you see in game: people who you come up to and who give you quests, rewards, or who you can buy things from.
    - Kiosks/Collections, which are really just Vendors that don't charge currency (or charge some pittance of a currency) and whose gating for purchases revolves more around your character's state.
    - Previews for rewards or the contents of sacks. These are implemented as Vendors, where you can't actually purchase from them but the items that they have for sale and the categories of sale items reflect the rewards or contents of the sack. This is so that the game could reuse the existing Vendor display UI for rewards and save a bunch of wheel reinvention.
    - Item Transfer capabilities, like the Vault and Postmaster. Vendors can have "acceptedItem" buckets that determine the source and destination buckets for transfers. When you interact with such a vendor, these buckets are what gets shown in the UI instead of any items that the Vendor would have for sale. Yep, the Vault is a vendor.
    It is pretty much guaranteed that they'll be used for even more features in the future. They have come to be seen more as generic categorized containers for items than "vendors" in a traditional sense, for better or worse.
    Where possible and time allows, we'll attempt to split those out into their own more digestible derived "Definitions": but often time does not allow that, as you can see from the above ways that vendors are used which we never split off from Vendor Definitions externally.
    Since Vendors are so many things to so many parts of the game, the definition is understandably complex. You will want to combine this data with live Vendor information from the API when it is available.
    """

    accepted_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyVendorAcceptedItemDefinition]],
        FieldMetadata(alias="acceptedItems"),
        pydantic.Field(
            alias="acceptedItems",
            description="If the Vendor is actually a vehicle for the transferring of items (like the Vault and Postmaster vendors), this defines the list of source->destination buckets for transferring.",
        ),
    ] = None
    """
    If the Vendor is actually a vehicle for the transferring of items (like the Vault and Postmaster vendors), this defines the list of source->destination buckets for transferring.
    """

    actions: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorActionDefinition]] = pydantic.Field(
        default=None
    )
    """
    Describes "actions" that can be performed on a vendor. Currently, none of these exist. But theoretically a Vendor could let you interact with it by performing actions. We'll see what these end up looking like if they ever get used.
    """

    buy_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="buyString"),
        pydantic.Field(
            alias="buyString",
            description='If the vendor has a custom localized string describing the "buy" action, that is returned here.',
        ),
    ] = None
    """
    If the vendor has a custom localized string describing the "buy" action, that is returned here.
    """

    categories: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorCategoryEntryDefinition]] = pydantic.Field(
        default=None
    )
    """
    These are the headers for sections of items that the vendor is selling. When you see items organized by category in the header, it is these categories that it is showing.
    Well, technically not *exactly* these. On BNet, it doesn't make sense to have categories be "paged" as we do in Destiny, so we run some heuristics to attempt to aggregate pages of categories together. 
    These are the categories post-concatenation, if the vendor had concatenation applied. If you want the pre-aggregated category data, use originalCategories.
    """

    consolidate_categories: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="consolidateCategories"),
        pydantic.Field(
            alias="consolidateCategories",
            description="If TRUE, consolidate categories that only differ by trivial properties (such as having minor differences in name)",
        ),
    ] = None
    """
    If TRUE, consolidate categories that only differ by trivial properties (such as having minor differences in name)
    """

    display_categories: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyDisplayCategoryDefinition]],
        FieldMetadata(alias="displayCategories"),
        pydantic.Field(
            alias="displayCategories",
            description='Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI. \r\nThe "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two.',
        ),
    ] = None
    """
    Display Categories are different from "categories" in that these are specifically for visual grouping and display of categories in Vendor UI. 
    The "categories" structure is for validation of the contained items, and can be categorized entirely separately from "Display Categories", there need be and often will be no meaningful relationship between the two.
    """

    display_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="displayItemHash"),
        pydantic.Field(
            alias="displayItemHash",
            description='If the vendor has an item that should be displayed as the "featured" item, this is the hash identifier for that DestinyVendorItemDefinition.\r\nApparently this is usually a related currency, like a reputation token. But it need not be restricted to that.',
        ),
    ] = None
    """
    If the vendor has an item that should be displayed as the "featured" item, this is the hash identifier for that DestinyVendorItemDefinition.
    Apparently this is usually a related currency, like a reputation token. But it need not be restricted to that.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsDestinyVendorDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
    ] = None
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If a vendor is not enabled, we won't even save the vendor's definition, and we won't return any items or info about them. It's as if they don't exist.
    """

    faction_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="factionHash"),
        pydantic.Field(
            alias="factionHash",
            description='If the Vendor has a faction, this hash will be valid and point to a DestinyFactionDefinition.\r\nThe game UI and BNet often mine the faction definition for additional elements and details to place on the screen, such as the faction\'s Progression status (aka "Reputation").',
        ),
    ] = None
    """
    If the Vendor has a faction, this hash will be valid and point to a DestinyFactionDefinition.
    The game UI and BNet often mine the faction definition for additional elements and details to place on the screen, such as the faction's Progression status (aka "Reputation").
    """

    failure_strings: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="failureStrings"),
        pydantic.Field(
            alias="failureStrings",
            description="If an item can't be purchased from the vendor, there may be many \"custom\"/game state specific reasons why not.\r\nThis is a list of localized strings with messages for those custom failures. The live BNet data will return a failureIndexes property for items that can't be purchased: using those values to index into this array, you can show the user the appropriate failure message for the item that can't be bought.",
        ),
    ] = None
    """
    If an item can't be purchased from the vendor, there may be many "custom"/game state specific reasons why not.
    This is a list of localized strings with messages for those custom failures. The live BNet data will return a failureIndexes property for items that can't be purchased: using those values to index into this array, you can show the user the appropriate failure message for the item that can't be bought.
    """

    groups: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorGroupReference]] = pydantic.Field(default=None)
    """
    A vendor can be a part of 0 or 1 "groups" at a time: a group being a collection of Vendors related by either location or function/purpose. It's used for our our Companion Vendor UI. Only one of these can be active for a Vendor at a time.
    """

    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    ignore_sale_item_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="ignoreSaleItemHashes"),
        pydantic.Field(
            alias="ignoreSaleItemHashes",
            description="Some items don't make sense to return in the API, for example because they represent an action to be performed rather than an item being sold. I'd rather we not do this, but at least in the short term this is a workable workaround.",
        ),
    ] = None
    """
    Some items don't make sense to return in the API, for example because they represent an action to be performed rather than an item being sold. I'd rather we not do this, but at least in the short term this is a workable workaround.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    inhibit_buying: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="inhibitBuying"),
        pydantic.Field(
            alias="inhibitBuying",
            description="If this is true, you aren't allowed to buy whatever the vendor is selling.",
        ),
    ] = None
    """
    If this is true, you aren't allowed to buy whatever the vendor is selling.
    """

    inhibit_selling: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="inhibitSelling"),
        pydantic.Field(
            alias="inhibitSelling",
            description="If this is true, you're not allowed to sell whatever the vendor is buying.",
        ),
    ] = None
    """
    If this is true, you're not allowed to sell whatever the vendor is buying.
    """

    interactions: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorInteractionDefinition]] = pydantic.Field(
        default=None
    )
    """
    In addition to selling items, vendors can have "interactions": UI where you "talk" with the vendor and they offer you a reward, some item, or merely acknowledge via dialog that you did something cool.
    """

    inventory_flyouts: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyVendorInventoryFlyoutDefinition]],
        FieldMetadata(alias="inventoryFlyouts"),
        pydantic.Field(
            alias="inventoryFlyouts",
            description="If the vendor shows you items from your own inventory - such as the Vault vendor does - this data describes the UI around showing those inventory buckets and which ones get shown.",
        ),
    ] = None
    """
    If the vendor shows you items from your own inventory - such as the Vault vendor does - this data describes the UI around showing those inventory buckets and which ones get shown.
    """

    item_list: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyVendorItemDefinition]],
        FieldMetadata(alias="itemList"),
        pydantic.Field(
            alias="itemList",
            description='If the vendor sells items (or merely has a list of items to show like the "Sack" vendors do), this is the list of those items that the vendor can sell. From this list, only a subset will be available from the vendor at any given time, selected randomly and reset on the vendor\'s refresh interval.\r\nNote that a vendor can sell the same item multiple ways: for instance, nothing stops a vendor from selling you some specific weapon but using two different currencies, or the same weapon at multiple "item levels".',
        ),
    ] = None
    """
    If the vendor sells items (or merely has a list of items to show like the "Sack" vendors do), this is the list of those items that the vendor can sell. From this list, only a subset will be available from the vendor at any given time, selected randomly and reset on the vendor's refresh interval.
    Note that a vendor can sell the same item multiple ways: for instance, nothing stops a vendor from selling you some specific weapon but using two different currencies, or the same weapon at multiple "item levels".
    """

    locations: typing.Optional[typing.List[DestinyDefinitionsVendorsDestinyVendorLocationDefinition]] = pydantic.Field(
        default=None
    )
    """
    A vendor can be at different places in the world depending on the game/character/account state. This is the list of possible locations for the vendor, along with conditions we use to determine which one is currently active.
    """

    original_categories: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyVendorCategoryEntryDefinition]],
        FieldMetadata(alias="originalCategories"),
        pydantic.Field(
            alias="originalCategories",
            description="See the categories property for a description of categories and why originalCategories exists.",
        ),
    ] = None
    """
    See the categories property for a description of categories and why originalCategories exists.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    reset_interval_minutes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="resetIntervalMinutes"),
        pydantic.Field(
            alias="resetIntervalMinutes",
            description="A number used for calculating the frequency of a vendor's inventory resetting/refreshing.\r\nDon't worry about calculating this - we do it on the server side and send you the next refresh date with the live data.",
        ),
    ] = None
    """
    A number used for calculating the frequency of a vendor's inventory resetting/refreshing.
    Don't worry about calculating this - we do it on the server side and send you the next refresh date with the live data.
    """

    reset_offset_minutes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="resetOffsetMinutes"),
        pydantic.Field(
            alias="resetOffsetMinutes",
            description="Again, used for reset/refreshing of inventory. Don't worry too much about it. Unless you want to.",
        ),
    ] = None
    """
    Again, used for reset/refreshing of inventory. Don't worry too much about it. Unless you want to.
    """

    return_with_vendor_request: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="returnWithVendorRequest"),
        pydantic.Field(
            alias="returnWithVendorRequest",
            description="As many of you know, Vendor data has historically been pretty brutal on the BNet servers. In an effort to reduce this workload, only Vendors with this flag set will be returned on Vendor requests. This allows us to filter out Vendors that don't dynamic data that's particularly useful: things like \"Preview/Sack\" vendors, for example, that you can usually suss out the details for using just the definitions themselves.",
        ),
    ] = None
    """
    As many of you know, Vendor data has historically been pretty brutal on the BNet servers. In an effort to reduce this workload, only Vendors with this flag set will be returned on Vendor requests. This allows us to filter out Vendors that don't dynamic data that's particularly useful: things like "Preview/Sack" vendors, for example, that you can usually suss out the details for using just the definitions themselves.
    """

    sell_string: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sellString"),
        pydantic.Field(
            alias="sellString",
            description="Ditto for selling. Not that you can sell items to a vendor anymore. Will it come back? Who knows. The string's still there.",
        ),
    ] = None
    """
    Ditto for selling. Not that you can sell items to a vendor anymore. Will it come back? Who knows. The string's still there.
    """

    services: typing.Optional[typing.List[DestinyDefinitionsDestinyVendorServiceDefinition]] = pydantic.Field(
        default=None
    )
    """
    BNet doesn't use this data yet, but it appears to be an optional list of flavor text about services that the Vendor can provide.
    """

    unlock_ranges: typing_extensions.Annotated[
        typing.Optional[typing.List[DatesDateRange]],
        FieldMetadata(alias="unlockRanges"),
        pydantic.Field(
            alias="unlockRanges",
            description="If we were able to predict the dates when this Vendor will be visible/available, this will be the list of those date ranges. Sadly, we're not able to predict this very frequently, so this will often be useless data.",
        ),
    ] = None
    """
    If we were able to predict the dates when this Vendor will be visible/available, this will be the list of those date ranges. Sadly, we're not able to predict this very frequently, so this will often be useless data.
    """

    vendor_banner: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vendorBanner"),
        pydantic.Field(
            alias="vendorBanner", description="If the vendor has a custom banner image, that can be found here."
        ),
    ] = None
    """
    If the vendor has a custom banner image, that can be found here.
    """

    vendor_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vendorIdentifier"),
        pydantic.Field(
            alias="vendorIdentifier",
            description="The internal identifier for the Vendor. A holdover from the old days of Vendors, but we don't have time to refactor it away.",
        ),
    ] = None
    """
    The internal identifier for the Vendor. A holdover from the old days of Vendors, but we don't have time to refactor it away.
    """

    vendor_portrait: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vendorPortrait"),
        pydantic.Field(
            alias="vendorPortrait", description="A portrait of the Vendor's smiling mug. Or frothing tentacles."
        ),
    ] = None
    """
    A portrait of the Vendor's smiling mug. Or frothing tentacles.
    """

    vendor_progression_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorProgressionType"),
        pydantic.Field(
            alias="vendorProgressionType",
            description="The type of reward progression that this vendor has. Default - The original rank progression from token redemption. Ritual - Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Battlegrounds (War Table).",
        ),
    ] = None
    """
    The type of reward progression that this vendor has. Default - The original rank progression from token redemption. Ritual - Progression from ranks in ritual content. For example: Crucible (Shaxx), Gambit (Drifter), and Battlegrounds (War Table).
    """

    vendor_subcategory_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vendorSubcategoryIdentifier"),
        pydantic.Field(
            alias="vendorSubcategoryIdentifier",
            description="The identifier of the VendorCategoryDefinition for this vendor's subcategory.",
        ),
    ] = None
    """
    The identifier of the VendorCategoryDefinition for this vendor's subcategory.
    """

    visible: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If a vendor is not visible, we still have and will give vendor definition info, but we won't use them for things like Advisors or UI.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
