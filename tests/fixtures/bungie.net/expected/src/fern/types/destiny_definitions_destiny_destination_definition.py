

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_destiny_activity_graph_list_entry_definition import (
    DestinyDefinitionsDestinyActivityGraphListEntryDefinition,
)
from .destiny_definitions_destiny_bubble_definition import DestinyDefinitionsDestinyBubbleDefinition
from .destiny_definitions_destiny_destination_bubble_setting_definition import (
    DestinyDefinitionsDestinyDestinationBubbleSettingDefinition,
)


class DestinyDefinitionsDestinyDestinationDefinition(UniversalBaseModel):
    """
    On to one of the more confusing subjects of the API. What is a Destination, and what is the relationship between it, Activities, Locations, and Places?
    A "Destination" is a specific region/city/area of a larger "Place". For instance, a Place might be Earth where a Destination might be Bellevue, Washington. (Please, pick a more interesting destination if you come to visit Earth).
    """

    activity_graph_entries: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyActivityGraphListEntryDefinition]],
        FieldMetadata(alias="activityGraphEntries"),
    ] = pydantic.Field(default=None)
    """
    If the Destination has default Activity Graphs (i.e. "Map") that should be shown in the director, this is the list of those Graphs. At most, only one should be active at any given time for a Destination: these would represent, for example, different variants on a Map if the Destination is changing on a macro level based on game state.
    """

    bubble_settings: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsDestinyDestinationBubbleSettingDefinition]],
        FieldMetadata(alias="bubbleSettings"),
    ] = pydantic.Field(default=None)
    """
    A Destination may have many "Bubbles" zones with human readable properties.
    We don't get as much info as I'd like about them - I'd love to return info like where on the map they are located - but at least this gives you the name of those bubbles. bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data.
    DEPRECATED - Just use bubbles, it now has this data.
    """

    bubbles: typing.Optional[typing.List[DestinyDefinitionsDestinyBubbleDefinition]] = pydantic.Field(default=None)
    """
    This provides the unique identifiers for every bubble in the destination (only guaranteed unique within the destination), and any intrinsic properties of the bubble.
    bubbleSettings and bubbles both have the identical number of entries, and you should match up their indexes to provide matching bubble and bubbleSettings data.
    """

    default_freeroam_activity_hash: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="defaultFreeroamActivityHash")
    ] = pydantic.Field(default=None)
    """
    If this Destination has a default Free-Roam activity, this is the hash for that Activity. Use it to look up the DestinyActivityDefintion.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    hash: typing.Optional[int] = pydantic.Field(default=None)
    """
    The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.
    When entities refer to each other in Destiny content, it is this hash that they are referring to.
    """

    index: typing.Optional[int] = pydantic.Field(default=None)
    """
    The index of the entity as it was found in the investment tables.
    """

    place_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="placeHash")] = pydantic.Field(
        default=None
    )
    """
    The place that "owns" this Destination. Use this hash to look up the DestinyPlaceDefinition.
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
