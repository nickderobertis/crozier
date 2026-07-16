

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_misc_destiny_color import DestinyMiscDestinyColor


class DestinyDefinitionsSocialDestinySocialCommendationDefinition(UniversalBaseModel):
    activity_giving_limit: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activityGivingLimit"), pydantic.Field(alias="activityGivingLimit")
    ] = None
    card_image_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cardImagePath"), pydantic.Field(alias="cardImagePath")
    ] = None
    color: typing.Optional[DestinyMiscDestinyColor] = None
    display_activities: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition]],
        FieldMetadata(alias="displayActivities"),
        pydantic.Field(
            alias="displayActivities",
            description="The display properties for the the activities that this commendation is available in.",
        ),
    ] = None
    """
    The display properties for the the activities that this commendation is available in.
    """

    display_priority: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="displayPriority"), pydantic.Field(alias="displayPriority")
    ] = None
    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties"),
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

    parent_commendation_node_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="parentCommendationNodeHash"),
        pydantic.Field(alias="parentCommendationNodeHash"),
    ] = None
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
