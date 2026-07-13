

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_director_destiny_activity_graph_art_element_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition,
)
from .destiny_definitions_director_destiny_activity_graph_connection_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition,
)
from .destiny_definitions_director_destiny_activity_graph_display_objective_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition,
)
from .destiny_definitions_director_destiny_activity_graph_display_progression_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition,
)
from .destiny_definitions_director_destiny_activity_graph_node_definition import (
    DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition,
)
from .destiny_definitions_director_destiny_linked_graph_definition import (
    DestinyDefinitionsDirectorDestinyLinkedGraphDefinition,
)


class DestinyDefinitionsDirectorDestinyActivityGraphDefinition(UniversalBaseModel):
    """
    Represents a Map View in the director: be them overview views, destination views, or other.
    They have nodes which map to activities, and other various visual elements that we (or others) may or may not be able to use.
    Activity graphs, most importantly, have nodes which can have activities in various states of playability.
    Unfortunately, activity graphs are combined at runtime with Game UI-only assets such as fragments of map images, various in-game special effects, decals etc... that we don't get in these definitions.
    If we end up having time, we may end up trying to manually populate those here: but the last time we tried that, before the lead-up to D1, it proved to be unmaintainable as the game's content changed. So don't bet the farm on us providing that content in this definition.
    """

    art_elements: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphArtElementDefinition]],
        FieldMetadata(alias="artElements"),
    ] = pydantic.Field(default=None)
    """
    Represents one-off/special UI elements that appear on the map.
    """

    connections: typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphConnectionDefinition]] = (
        pydantic.Field(default=None)
    )
    """
    Represents connections between graph nodes. However, it lacks context that we'd need to make good use of it.
    """

    display_objectives: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphDisplayObjectiveDefinition]],
        FieldMetadata(alias="displayObjectives"),
    ] = pydantic.Field(default=None)
    """
    Objectives can display on maps, and this is supposedly metadata for that. I have not had the time to analyze the details of what is useful within however: we could be missing important data to make this work. Expect this property to be expanded on later if possible.
    """

    display_progressions: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphDisplayProgressionDefinition]],
        FieldMetadata(alias="displayProgressions"),
    ] = pydantic.Field(default=None)
    """
    Progressions can also display on maps, but similarly to displayObjectives we appear to lack some required information and context right now. We will have to look into it later and add more data if possible.
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

    linked_graphs: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyLinkedGraphDefinition]],
        FieldMetadata(alias="linkedGraphs"),
    ] = pydantic.Field(default=None)
    """
    Represents links between this Activity Graph and other ones.
    """

    nodes: typing.Optional[typing.List[DestinyDefinitionsDirectorDestinyActivityGraphNodeDefinition]] = pydantic.Field(
        default=None
    )
    """
    These represent the visual "nodes" on the map's view. These are the activities you can click on in the map.
    """

    redacted: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
