

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_base_item_component_set_ofuint32 import DestinyBaseItemComponentSetOfuint32
from .destiny_item_component_set_ofint64 import DestinyItemComponentSetOfint64
from .dictionary_component_response_ofint64and_destiny_character_activities_component import (
    DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent,
)
from .dictionary_component_response_ofint64and_destiny_character_component import (
    DictionaryComponentResponseOfint64AndDestinyCharacterComponent,
)
from .dictionary_component_response_ofint64and_destiny_character_progression_component import (
    DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent,
)
from .dictionary_component_response_ofint64and_destiny_character_records_component import (
    DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent,
)
from .dictionary_component_response_ofint64and_destiny_character_render_component import (
    DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent,
)
from .dictionary_component_response_ofint64and_destiny_collectibles_component import (
    DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent,
)
from .dictionary_component_response_ofint64and_destiny_craftables_component import (
    DictionaryComponentResponseOfint64AndDestinyCraftablesComponent,
)
from .dictionary_component_response_ofint64and_destiny_currencies_component import (
    DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent,
)
from .dictionary_component_response_ofint64and_destiny_inventory_component import (
    DictionaryComponentResponseOfint64AndDestinyInventoryComponent,
)
from .dictionary_component_response_ofint64and_destiny_kiosks_component import (
    DictionaryComponentResponseOfint64AndDestinyKiosksComponent,
)
from .dictionary_component_response_ofint64and_destiny_loadouts_component import (
    DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent,
)
from .dictionary_component_response_ofint64and_destiny_plug_sets_component import (
    DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent,
)
from .dictionary_component_response_ofint64and_destiny_presentation_nodes_component import (
    DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent,
)
from .dictionary_component_response_ofint64and_destiny_string_variables_component import (
    DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent,
)
from .single_component_response_of_destiny_inventory_component import SingleComponentResponseOfDestinyInventoryComponent
from .single_component_response_of_destiny_kiosks_component import SingleComponentResponseOfDestinyKiosksComponent
from .single_component_response_of_destiny_metrics_component import SingleComponentResponseOfDestinyMetricsComponent
from .single_component_response_of_destiny_platform_silver_component import (
    SingleComponentResponseOfDestinyPlatformSilverComponent,
)
from .single_component_response_of_destiny_plug_sets_component import SingleComponentResponseOfDestinyPlugSetsComponent
from .single_component_response_of_destiny_presentation_nodes_component import (
    SingleComponentResponseOfDestinyPresentationNodesComponent,
)
from .single_component_response_of_destiny_profile_collectibles_component import (
    SingleComponentResponseOfDestinyProfileCollectiblesComponent,
)
from .single_component_response_of_destiny_profile_component import SingleComponentResponseOfDestinyProfileComponent
from .single_component_response_of_destiny_profile_progression_component import (
    SingleComponentResponseOfDestinyProfileProgressionComponent,
)
from .single_component_response_of_destiny_profile_records_component import (
    SingleComponentResponseOfDestinyProfileRecordsComponent,
)
from .single_component_response_of_destiny_profile_transitory_component import (
    SingleComponentResponseOfDestinyProfileTransitoryComponent,
)
from .single_component_response_of_destiny_social_commendations_component import (
    SingleComponentResponseOfDestinySocialCommendationsComponent,
)
from .single_component_response_of_destiny_string_variables_component import (
    SingleComponentResponseOfDestinyStringVariablesComponent,
)
from .single_component_response_of_destiny_vendor_receipts_component import (
    SingleComponentResponseOfDestinyVendorReceiptsComponent,
)


class DestinyResponsesDestinyProfileResponse(UniversalBaseModel):
    """
    The response for GetDestinyProfile, with components for character and item-level data.
    """

    character_activities: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCharacterActivitiesComponent],
        FieldMetadata(alias="characterActivities"),
        pydantic.Field(
            alias="characterActivities",
            description="Character activity data - the activities available to this character and its status, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterActivities",
        ),
    ] = None
    """
    Character activity data - the activities available to this character and its status, keyed by the Character's Id.
    COMPONENT TYPE: CharacterActivities
    """

    character_collectibles: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCollectiblesComponent],
        FieldMetadata(alias="characterCollectibles"),
        pydantic.Field(alias="characterCollectibles", description="COMPONENT TYPE: Collectibles"),
    ] = None
    """
    COMPONENT TYPE: Collectibles
    """

    character_craftables: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCraftablesComponent],
        FieldMetadata(alias="characterCraftables"),
        pydantic.Field(alias="characterCraftables", description="COMPONENT TYPE: Craftables"),
    ] = None
    """
    COMPONENT TYPE: Craftables
    """

    character_currency_lookups: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCurrenciesComponent],
        FieldMetadata(alias="characterCurrencyLookups"),
        pydantic.Field(
            alias="characterCurrencyLookups",
            description='A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.\r\nCOMPONENT TYPE: CurrencyLookups',
        ),
    ] = None
    """
    A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
    COMPONENT TYPE: CurrencyLookups
    """

    character_equipment: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyInventoryComponent],
        FieldMetadata(alias="characterEquipment"),
        pydantic.Field(
            alias="characterEquipment",
            description="The character's equipped items, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterEquipment",
        ),
    ] = None
    """
    The character's equipped items, keyed by the Character's Id.
    COMPONENT TYPE: CharacterEquipment
    """

    character_inventories: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyInventoryComponent],
        FieldMetadata(alias="characterInventories"),
        pydantic.Field(
            alias="characterInventories",
            description="The character-level non-equipped inventory items, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterInventories",
        ),
    ] = None
    """
    The character-level non-equipped inventory items, keyed by the Character's Id.
    COMPONENT TYPE: CharacterInventories
    """

    character_kiosks: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyKiosksComponent],
        FieldMetadata(alias="characterKiosks"),
        pydantic.Field(
            alias="characterKiosks",
            description="Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk.\r\nThis component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.\r\nCOMPONENT TYPE: Kiosks",
        ),
    ] = None
    """
    Items available from Kiosks that are available to a specific character as opposed to the account as a whole. It must be combined with data from the profileKiosks property to get a full picture of the character's available items to check out of a kiosk.
    This component returns information about what Kiosk items are available to you on a *Character* level. Usually, kiosk items will be earned for the entire Profile (all characters) at once. To find those, look in the profileKiosks property.
    COMPONENT TYPE: Kiosks
    """

    character_loadouts: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyLoadoutsComponent],
        FieldMetadata(alias="characterLoadouts"),
        pydantic.Field(
            alias="characterLoadouts",
            description="The character loadouts, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterLoadouts",
        ),
    ] = None
    """
    The character loadouts, keyed by the Character's Id.
    COMPONENT TYPE: CharacterLoadouts
    """

    character_plug_sets: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyPlugSetsComponent],
        FieldMetadata(alias="characterPlugSets"),
        pydantic.Field(
            alias="characterPlugSets",
            description="When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped.\r\nThis comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.\r\nCOMPONENT TYPE: ItemSockets",
        ),
    ] = None
    """
    When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states, per character, that are character-scoped.
    This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.
    COMPONENT TYPE: ItemSockets
    """

    character_presentation_nodes: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyPresentationNodesComponent],
        FieldMetadata(alias="characterPresentationNodes"),
        pydantic.Field(alias="characterPresentationNodes", description="COMPONENT TYPE: PresentationNodes"),
    ] = None
    """
    COMPONENT TYPE: PresentationNodes
    """

    character_progressions: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCharacterProgressionComponent],
        FieldMetadata(alias="characterProgressions"),
        pydantic.Field(
            alias="characterProgressions",
            description="Character-level progression data, keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterProgressions",
        ),
    ] = None
    """
    Character-level progression data, keyed by the Character's Id.
    COMPONENT TYPE: CharacterProgressions
    """

    character_records: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCharacterRecordsComponent],
        FieldMetadata(alias="characterRecords"),
        pydantic.Field(alias="characterRecords", description="COMPONENT TYPE: Records"),
    ] = None
    """
    COMPONENT TYPE: Records
    """

    character_render_data: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyCharacterRenderComponent],
        FieldMetadata(alias="characterRenderData"),
        pydantic.Field(
            alias="characterRenderData",
            description="Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id.\r\nCOMPONENT TYPE: CharacterRenderData",
        ),
    ] = None
    """
    Character rendering data - a minimal set of info needed to render a character in 3D - keyed by the Character's Id.
    COMPONENT TYPE: CharacterRenderData
    """

    character_string_variables: typing_extensions.Annotated[
        typing.Optional[DictionaryComponentResponseOfint64AndDestinyStringVariablesComponent],
        FieldMetadata(alias="characterStringVariables"),
        pydantic.Field(alias="characterStringVariables", description="COMPONENT TYPE: StringVariables"),
    ] = None
    """
    COMPONENT TYPE: StringVariables
    """

    character_uninstanced_item_components: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyBaseItemComponentSetOfuint32]],
        FieldMetadata(alias="characterUninstancedItemComponents"),
        pydantic.Field(
            alias="characterUninstancedItemComponents",
            description="Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface?\r\nLet's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise.\r\nAt some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character.\r\nUp to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus \"itemComponents\" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside.\r\nUnfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character.\r\nTo give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory.\r\nI'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay",
        ),
    ] = None
    """
    Do you ever get the feeling that a system was designed *too* flexibly? That it can be used in so many different ways that you end up being unable to provide an easy to use abstraction for the mess that's happening under the surface?
    Let's talk about character-specific data that might be related to items without instances. These two statements are totally unrelated, I promise.
    At some point during D2, it was decided that items - such as Bounties - could be given to characters and *not* have instance data, but that *could* display and even use relevant state information on your account and character.
    Up to now, any item that had meaningful dependencies on character or account state had to be instanced, and thus "itemComponents" was all that you needed: it was keyed by item's instance IDs and provided the stateful information you needed inside.
    Unfortunately, we don't live in such a magical world anymore. This is information held on a per-character basis about non-instanced items that the characters have in their inventory - or that reference character-specific state information even if it's in Account-level inventory - and the values related to that item's state in relation to the given character.
    To give a concrete example, look at a Moments of Triumph bounty. They exist in a character's inventory, and show/care about a character's progression toward completing the bounty. But the bounty itself is a non-instanced item, like a mod or a currency. This returns that data for the characters who have the bounty in their inventory.
    I'm not crying, you're crying Okay we're both crying but it's going to be okay I promise Actually I shouldn't promise that, I don't know if it's going to be okay
    """

    characters: typing.Optional[DictionaryComponentResponseOfint64AndDestinyCharacterComponent] = pydantic.Field(
        default=None
    )
    """
    Basic information about each character, keyed by the CharacterId.
    COMPONENT TYPE: Characters
    """

    item_components: typing_extensions.Annotated[
        typing.Optional[DestinyItemComponentSetOfint64],
        FieldMetadata(alias="itemComponents"),
        pydantic.Field(
            alias="itemComponents",
            description="Information about instanced items across all returned characters, keyed by the item's instance ID.\r\nCOMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]",
        ),
    ] = None
    """
    Information about instanced items across all returned characters, keyed by the item's instance ID.
    COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
    """

    metrics: typing.Optional[SingleComponentResponseOfDestinyMetricsComponent] = pydantic.Field(default=None)
    """
    COMPONENT TYPE: Metrics
    """

    platform_silver: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyPlatformSilverComponent],
        FieldMetadata(alias="platformSilver"),
        pydantic.Field(
            alias="platformSilver",
            description="Silver quantities for any platform on which this Profile plays destiny.\r\n COMPONENT TYPE: PlatformSilver",
        ),
    ] = None
    """
    Silver quantities for any platform on which this Profile plays destiny.
     COMPONENT TYPE: PlatformSilver
    """

    profile: typing.Optional[SingleComponentResponseOfDestinyProfileComponent] = pydantic.Field(default=None)
    """
    The basic information about the Destiny Profile (formerly "Account").
    COMPONENT TYPE: Profiles
    """

    profile_collectibles: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyProfileCollectiblesComponent],
        FieldMetadata(alias="profileCollectibles"),
        pydantic.Field(alias="profileCollectibles", description="COMPONENT TYPE: Collectibles"),
    ] = None
    """
    COMPONENT TYPE: Collectibles
    """

    profile_commendations: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinySocialCommendationsComponent],
        FieldMetadata(alias="profileCommendations"),
        pydantic.Field(alias="profileCommendations", description="COMPONENT TYPE: SocialCommendations"),
    ] = None
    """
    COMPONENT TYPE: SocialCommendations
    """

    profile_currencies: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyInventoryComponent],
        FieldMetadata(alias="profileCurrencies"),
        pydantic.Field(
            alias="profileCurrencies",
            description="The profile-level currencies owned by the Destiny Profile.\r\nCOMPONENT TYPE: ProfileCurrencies",
        ),
    ] = None
    """
    The profile-level currencies owned by the Destiny Profile.
    COMPONENT TYPE: ProfileCurrencies
    """

    profile_inventory: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyInventoryComponent],
        FieldMetadata(alias="profileInventory"),
        pydantic.Field(
            alias="profileInventory",
            description="The profile-level inventory of the Destiny Profile.\r\nCOMPONENT TYPE: ProfileInventories",
        ),
    ] = None
    """
    The profile-level inventory of the Destiny Profile.
    COMPONENT TYPE: ProfileInventories
    """

    profile_kiosks: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyKiosksComponent],
        FieldMetadata(alias="profileKiosks"),
        pydantic.Field(
            alias="profileKiosks",
            description="Items available from Kiosks that are available Profile-wide (i.e. across all characters)\r\nThis component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.\r\nCOMPONENT TYPE: Kiosks",
        ),
    ] = None
    """
    Items available from Kiosks that are available Profile-wide (i.e. across all characters)
    This component returns information about what Kiosk items are available to you on a *Profile* level. It is theoretically possible for Kiosks to have items gated by specific Character as well. If you ever have those, you will find them on the characterKiosks property.
    COMPONENT TYPE: Kiosks
    """

    profile_plug_sets: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyPlugSetsComponent],
        FieldMetadata(alias="profilePlugSets"),
        pydantic.Field(
            alias="profilePlugSets",
            description="When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped.\r\nThis comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.\r\nCOMPONENT TYPE: ItemSockets",
        ),
    ] = None
    """
    When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are profile-scoped.
    This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.
    COMPONENT TYPE: ItemSockets
    """

    profile_presentation_nodes: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyPresentationNodesComponent],
        FieldMetadata(alias="profilePresentationNodes"),
        pydantic.Field(alias="profilePresentationNodes", description="COMPONENT TYPE: PresentationNodes"),
    ] = None
    """
    COMPONENT TYPE: PresentationNodes
    """

    profile_progression: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyProfileProgressionComponent],
        FieldMetadata(alias="profileProgression"),
        pydantic.Field(
            alias="profileProgression",
            description="When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data.\r\nCOMPONENT TYPE: ProfileProgression",
        ),
    ] = None
    """
    When we have progression information - such as Checklists - that may apply profile-wide, it will be returned here rather than in the per-character progression data.
    COMPONENT TYPE: ProfileProgression
    """

    profile_records: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyProfileRecordsComponent],
        FieldMetadata(alias="profileRecords"),
        pydantic.Field(alias="profileRecords", description="COMPONENT TYPE: Records"),
    ] = None
    """
    COMPONENT TYPE: Records
    """

    profile_string_variables: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyStringVariablesComponent],
        FieldMetadata(alias="profileStringVariables"),
        pydantic.Field(alias="profileStringVariables", description="COMPONENT TYPE: StringVariables"),
    ] = None
    """
    COMPONENT TYPE: StringVariables
    """

    profile_transitory_data: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyProfileTransitoryComponent],
        FieldMetadata(alias="profileTransitoryData"),
        pydantic.Field(alias="profileTransitoryData", description="COMPONENT TYPE: Transitory"),
    ] = None
    """
    COMPONENT TYPE: Transitory
    """

    response_minted_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="responseMintedTimestamp"),
        pydantic.Field(
            alias="responseMintedTimestamp",
            description="Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness.",
        ),
    ] = None
    """
    Records the timestamp of when most components were last generated from the world server source. Unless the component type is specified in the documentation for secondaryComponentsMintedTimestamp, this value is sufficient to do data freshness.
    """

    secondary_components_minted_timestamp: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="secondaryComponentsMintedTimestamp"),
        pydantic.Field(
            alias="secondaryComponentsMintedTimestamp",
            description="Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:\r\n PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory\r\n All other component types may use the primary timestamp property.",
        ),
    ] = None
    """
    Some secondary components are not tracked in the primary response timestamp and have their timestamp tracked here. If your component is any of the following, this field is where you will find your timestamp value:
     PresentationNodes, Records, Collectibles, Metrics, StringVariables, Craftables, Transitory
     All other component types may use the primary timestamp property.
    """

    vendor_receipts: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyVendorReceiptsComponent],
        FieldMetadata(alias="vendorReceipts"),
        pydantic.Field(
            alias="vendorReceipts",
            description="Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say...\r\nCOMPONENT TYPE: VendorReceipts",
        ),
    ] = None
    """
    Recent, refundable purchases you have made from vendors. When will you use it? Couldn't say...
    COMPONENT TYPE: VendorReceipts
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
