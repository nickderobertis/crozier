

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .single_component_response_of_destiny_item_component import SingleComponentResponseOfDestinyItemComponent
from .single_component_response_of_destiny_item_instance_component import (
    SingleComponentResponseOfDestinyItemInstanceComponent,
)
from .single_component_response_of_destiny_item_objectives_component import (
    SingleComponentResponseOfDestinyItemObjectivesComponent,
)
from .single_component_response_of_destiny_item_perks_component import (
    SingleComponentResponseOfDestinyItemPerksComponent,
)
from .single_component_response_of_destiny_item_plug_objectives_component import (
    SingleComponentResponseOfDestinyItemPlugObjectivesComponent,
)
from .single_component_response_of_destiny_item_render_component import (
    SingleComponentResponseOfDestinyItemRenderComponent,
)
from .single_component_response_of_destiny_item_reusable_plugs_component import (
    SingleComponentResponseOfDestinyItemReusablePlugsComponent,
)
from .single_component_response_of_destiny_item_sockets_component import (
    SingleComponentResponseOfDestinyItemSocketsComponent,
)
from .single_component_response_of_destiny_item_stats_component import (
    SingleComponentResponseOfDestinyItemStatsComponent,
)
from .single_component_response_of_destiny_item_talent_grid_component import (
    SingleComponentResponseOfDestinyItemTalentGridComponent,
)


class DestinyResponsesDestinyItemResponse(UniversalBaseModel):
    """
    The response object for retrieving an individual instanced item. None of these components are relevant for an item that doesn't have an "itemInstanceId": for those, get your information from the DestinyInventoryDefinition.
    """

    character_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="characterId")] = (
        pydantic.Field(default=None)
    )
    """
    If the item is on a character, this will return the ID of the character that is holding the item.
    """

    instance: typing.Optional[SingleComponentResponseOfDestinyItemInstanceComponent] = pydantic.Field(default=None)
    """
    Basic instance data for the item.
    COMPONENT TYPE: ItemInstances
    """

    item: typing.Optional[SingleComponentResponseOfDestinyItemComponent] = pydantic.Field(default=None)
    """
    Common data for the item relevant to its non-instanced properties.
    COMPONENT TYPE: ItemCommonData
    """

    objectives: typing.Optional[SingleComponentResponseOfDestinyItemObjectivesComponent] = pydantic.Field(default=None)
    """
    Information specifically about the item's objectives.
    COMPONENT TYPE: ItemObjectives
    """

    perks: typing.Optional[SingleComponentResponseOfDestinyItemPerksComponent] = pydantic.Field(default=None)
    """
    Information specifically about the perks currently active on the item.
    COMPONENT TYPE: ItemPerks
    """

    plug_objectives: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyItemPlugObjectivesComponent],
        FieldMetadata(alias="plugObjectives"),
    ] = pydantic.Field(default=None)
    """
    Information about objectives on Plugs for a given item. See the component's documentation for more info.
    COMPONENT TYPE: ItemPlugObjectives
    """

    render_data: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyItemRenderComponent], FieldMetadata(alias="renderData")
    ] = pydantic.Field(default=None)
    """
    Information about how to render the item in 3D.
    COMPONENT TYPE: ItemRenderData
    """

    reusable_plugs: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyItemReusablePlugsComponent],
        FieldMetadata(alias="reusablePlugs"),
    ] = pydantic.Field(default=None)
    """
    Information about the Reusable Plugs for sockets on an item. These are plugs that you can insert into the given socket regardless of if you actually own an instance of that plug: they are logic-driven plugs rather than inventory-driven.
     These may need to be combined with Plug Set component data to get a full picture of available plugs on a given socket.
     COMPONENT TYPE: ItemReusablePlugs
    """

    sockets: typing.Optional[SingleComponentResponseOfDestinyItemSocketsComponent] = pydantic.Field(default=None)
    """
    Information about the sockets of the item: which are currently active, what potential sockets you could have and the stats/abilities/perks you can gain from them.
    COMPONENT TYPE: ItemSockets
    """

    stats: typing.Optional[SingleComponentResponseOfDestinyItemStatsComponent] = pydantic.Field(default=None)
    """
    Information about the computed stats of the item: power, defense, etc...
    COMPONENT TYPE: ItemStats
    """

    talent_grid: typing_extensions.Annotated[
        typing.Optional[SingleComponentResponseOfDestinyItemTalentGridComponent], FieldMetadata(alias="talentGrid")
    ] = pydantic.Field(default=None)
    """
    Information about the talent grid attached to the item. Talent nodes can provide a variety of benefits and abilities, and in Destiny 2 are used almost exclusively for the character's "Builds".
    COMPONENT TYPE: ItemTalentGrids
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
