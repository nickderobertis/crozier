

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_common_destiny_position_definition import DestinyDefinitionsCommonDestinyPositionDefinition
from .destiny_definitions_director_destiny_activity_graph_node_activity_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition,
)
from .destiny_definitions_director_destiny_activity_graph_node_featuring_state_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition,
)
from .destiny_definitions_director_destiny_activity_graph_node_state_entry import (
    DestinyDefinitionsDirectorDestinyActivityGraphNodeStateEntry,
)


class DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition(UniversalBaseModel):
    """
    This is the position and other data related to nodes in the activity graph that you can click to launch activities. An Activity Graph node will only have one active Activity at a time, which will determine the activity to be launched (and, unless overrideDisplay information is provided, will also determine the tooltip and other UI related to the node)
    """

    activities: typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphNodeActivityDefinition]] = (
        pydantic.Field(default=None)
    )
    """
    The node may have various possible activities that could be active for it, however only one may be active at a time. See the DestinyActivityGraphNodeActivityDefinition for details.
    """

    featuring_states: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphNodeFeaturingStateDefinition]],
        FieldMetadata(alias="featuringStates"),
    ] = pydantic.Field(default=None)
    """
    The node may have various visual accents placed on it, or styles applied. These are the list of possible styles that the Node can have. The game iterates through each, looking for the first one that passes a check of the required game/character/account state in order to show that style, and then renders the node in that style.
    """

    node_id: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="nodeId")] = pydantic.Field(
        default=None
    )
    """
    An identifier for the Activity Graph Node, only guaranteed to be unique within its parent Activity Graph.
    """

    override_display: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="overrideDisplay"),
    ] = pydantic.Field(default=None)
    """
    The node *may* have display properties that override the active Activity's display properties.
    """

    position: typing.Optional[DestinyDefinitionsCommonDestinyPositionDefinition] = pydantic.Field(default=None)
    """
    The position on the map for this node.
    """

    states: typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphNodeStateEntry]] = pydantic.Field(
        default=None
    )
    """
    Represents possible states that the graph node can be in. These are combined with some checking that happens in the game client and server to determine which state is actually active at any given time.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
