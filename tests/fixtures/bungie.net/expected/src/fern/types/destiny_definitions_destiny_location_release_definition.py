

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyLocationReleaseDefinition(UniversalBaseModel):
    """
    A specific "spot" referred to by a location. Only one of these can be active at a time for a given Location.
    """

    activity_bubble_name: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityBubbleName"),
        pydantic.Field(
            alias="activityBubbleName",
            description="The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition's bubbles and bubbleSettings properties.",
        ),
    ] = None
    """
    The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition's bubbles and bubbleSettings properties.
    """

    activity_graph_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityGraphHash"),
        pydantic.Field(alias="activityGraphHash", description="The Activity Graph being pointed to by this location."),
    ] = None
    """
    The Activity Graph being pointed to by this location.
    """

    activity_graph_node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityGraphNodeHash"),
        pydantic.Field(
            alias="activityGraphNodeHash",
            description="The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of)",
        ),
    ] = None
    """
    The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of)
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(alias="activityHash", description="The Activity being pointed to by this location."),
    ] = None
    """
    The Activity being pointed to by this location.
    """

    activity_path_bundle: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityPathBundle"),
        pydantic.Field(
            alias="activityPathBundle",
            description="If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information.",
        ),
    ] = None
    """
    If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information.
    """

    activity_path_destination: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityPathDestination"),
        pydantic.Field(
            alias="activityPathDestination",
            description="If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man.",
        ),
    ] = None
    """
    If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man.
    """

    destination_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="destinationHash"),
        pydantic.Field(alias="destinationHash", description="The Destination being pointed to by this location."),
    ] = None
    """
    The Destination being pointed to by this location.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(
            alias="displayProperties", description="Sadly, these don't appear to be populated anymore (ever?)"
        ),
    ] = None
    """
    Sadly, these don't appear to be populated anymore (ever?)
    """

    large_transparent_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="largeTransparentIcon"), pydantic.Field(alias="largeTransparentIcon")
    ] = None
    map_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mapIcon"), pydantic.Field(alias="mapIcon")
    ] = None
    nav_point_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="navPointType"),
        pydantic.Field(
            alias="navPointType",
            description="The type of Nav Point that this represents. See the enumeration for more info.",
        ),
    ] = None
    """
    The type of Nav Point that this represents. See the enumeration for more info.
    """

    small_transparent_icon: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="smallTransparentIcon"), pydantic.Field(alias="smallTransparentIcon")
    ] = None
    spawn_point: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="spawnPoint"),
        pydantic.Field(
            alias="spawnPoint",
            description="If we had map information, this spawnPoint would be interesting. But sadly, we don't have that info.",
        ),
    ] = None
    """
    If we had map information, this spawnPoint would be interesting. But sadly, we don't have that info.
    """

    world_position: typing_extensions.Annotated[
        typing.Optional[typing.List[int]],
        FieldMetadata(alias="worldPosition"),
        pydantic.Field(
            alias="worldPosition",
            description="Looks like it should be the position on the map, but sadly it does not look populated... yet?",
        ),
    ] = None
    """
    Looks like it should be the position on the map, but sadly it does not look populated... yet?
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
