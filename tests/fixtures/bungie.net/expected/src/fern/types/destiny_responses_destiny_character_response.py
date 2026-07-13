

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_base_item_component_set_ofuint32 import DestinyBaseItemComponentSetOfuint32
from .destiny_item_component_set_ofint64 import DestinyItemComponentSetOfint64
from .single_component_response_of_destiny_character_activities_component import (
    SingleComponentResponseOfDestinyCharacterActivitiesComponent,
)
from .single_component_response_of_destiny_character_component import SingleComponentResponseOfDestinyCharacterComponent
from .single_component_response_of_destiny_character_progression_component import (
    SingleComponentResponseOfDestinyCharacterProgressionComponent,
)
from .single_component_response_of_destiny_character_records_component import (
    SingleComponentResponseOfDestinyCharacterRecordsComponent,
)
from .single_component_response_of_destiny_character_render_component import (
    SingleComponentResponseOfDestinyCharacterRenderComponent,
)
from .single_component_response_of_destiny_collectibles_component import (
    SingleComponentResponseOfDestinyCollectiblesComponent,
)
from .single_component_response_of_destiny_currencies_component import (
    SingleComponentResponseOfDestinyCurrenciesComponent,
)
from .single_component_response_of_destiny_inventory_component import SingleComponentResponseOfDestinyInventoryComponent
from .single_component_response_of_destiny_kiosks_component import SingleComponentResponseOfDestinyKiosksComponent
from .single_component_response_of_destiny_loadouts_component import SingleComponentResponseOfDestinyLoadoutsComponent
from .single_component_response_of_destiny_plug_sets_component import SingleComponentResponseOfDestinyPlugSetsComponent
from .single_component_response_of_destiny_presentation_nodes_component import (
    SingleComponentResponseOfDestinyPresentationNodesComponent,
)


class DestinyResponsesDestinyCharacterResponse(UniversalBaseModel):
    """
    The response contract for GetDestinyCharacter, with components that can be returned for character and item-level data.
    """

    activities: typing.Optional[SingleComponentResponseOfDestinyCharacterActivitiesComponent] = pydantic.Field(
        default=None
    )
    """
    Activity data - info about current activities available to the player.
    COMPONENT TYPE: CharacterActivities
    """

    character: typing.Optional[SingleComponentResponseOfDestinyCharacterComponent] = pydantic.Field(default=None)
    """
    Base information about the character in question.
    COMPONENT TYPE: Characters
    """

    collectibles: typing.Optional[SingleComponentResponseOfDestinyCollectiblesComponent] = pydantic.Field(default=None)
    """
    COMPONENT TYPE: Collectibles
    """

    currency_lookups: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyCurrenciesComponent], FieldMetadata(alias="currencyLookups")
    ] = pydantic.Field(default=None)
    """
    A "lookup" convenience component that can be used to quickly check if the character has access to items that can be used for purchasing.
    COMPONENT TYPE: CurrencyLookups
    """

    equipment: typing.Optional[SingleComponentResponseOfDestinyInventoryComponent] = pydantic.Field(default=None)
    """
    Equipped items on the character.
    COMPONENT TYPE: CharacterEquipment
    """

    inventory: typing.Optional[SingleComponentResponseOfDestinyInventoryComponent] = pydantic.Field(default=None)
    """
    The character-level non-equipped inventory items.
    COMPONENT TYPE: CharacterInventories
    """

    item_components: typing_extensions.Annotated[
        typing.Optional[DestinyItemComponentSetOfint64], FieldMetadata(alias="itemComponents")
    ] = pydantic.Field(default=None)
    """
    The set of components belonging to the player's instanced items.
    COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
    """

    kiosks: typing.Optional[SingleComponentResponseOfDestinyKiosksComponent] = pydantic.Field(default=None)
    """
    Items available from Kiosks that are available to this specific character. 
    COMPONENT TYPE: Kiosks
    """

    loadouts: typing.Optional[SingleComponentResponseOfDestinyLoadoutsComponent] = pydantic.Field(default=None)
    """
    The loadouts available to the character.
    COMPONENT TYPE: CharacterLoadouts
    """

    plug_sets: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyPlugSetsComponent], FieldMetadata(alias="plugSets")
    ] = pydantic.Field(default=None)
    """
    When sockets refer to reusable Plug Sets (see DestinyPlugSetDefinition for more info), this is the set of plugs and their states that are scoped to this character.
    This comes back with ItemSockets, as it is needed for a complete picture of the sockets on requested items.
    COMPONENT TYPE: ItemSockets
    """

    presentation_nodes: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyPresentationNodesComponent],
        FieldMetadata(alias="presentationNodes"),
    ] = pydantic.Field(default=None)
    """
    COMPONENT TYPE: PresentationNodes
    """

    progressions: typing.Optional[SingleComponentResponseOfDestinyCharacterProgressionComponent] = pydantic.Field(
        default=None
    )
    """
    Character progression data, including Milestones.
    COMPONENT TYPE: CharacterProgressions
    """

    records: typing.Optional[SingleComponentResponseOfDestinyCharacterRecordsComponent] = pydantic.Field(default=None)
    """
    COMPONENT TYPE: Records
    """

    render_data: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyCharacterRenderComponent], FieldMetadata(alias="renderData")
    ] = pydantic.Field(default=None)
    """
    Character rendering data - a minimal set of information about equipment and dyes used for rendering.
    COMPONENT TYPE: CharacterRenderData
    """

    uninstanced_item_components: typing_extensions.Annotated[
        typing.Optional[DestinyBaseItemComponentSetOfuint32], FieldMetadata(alias="uninstancedItemComponents")
    ] = pydantic.Field(default=None)
    """
    The set of components belonging to the player's UNinstanced items. Because apparently now those too can have information relevant to the character's state.
    COMPONENT TYPE: [See inside the DestinyItemComponentSet contract for component types.]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
