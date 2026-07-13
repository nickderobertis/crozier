

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)


class DestinyDefinitionsDestinyActivityModeDefinition(UniversalBaseModel):
    """
    This definition represents an "Activity Mode" as it exists in the Historical Stats endpoints. An individual Activity Mode represents a collection of activities that are played in a certain way. For example, Nightfall Strikes are part of a "Nightfall" activity mode, and any activities played as the PVP mode "Clash" are part of the "Clash activity mode.
    Activity modes are nested under each other in a hierarchy, so that if you ask for - for example - "AllPvP", you will get any PVP activities that the user has played, regardless of what specific PVP mode was being played.
    """

    activity_mode_category: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="activityModeCategory")
    ] = pydantic.Field(default=None)
    """
    The type of play being performed in broad terms (PVP, PVE)
    """

    activity_mode_mappings: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, int]], FieldMetadata(alias="activityModeMappings")
    ] = pydantic.Field(default=None)
    """
    If this exists, the mode has specific Activities (referred to by the Key) that should instead map to other Activity Modes when they are played. This was useful in D1 for Private Matches, where we wanted to have Private Matches as an activity mode while still referring to the specific mode being played.
    """

    display: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If FALSE, we want to ignore this type when we're showing activity modes in BNet UI. It will still be returned in case 3rd parties want to use it for any purpose.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
    ] = None
    friendly_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="friendlyName")] = (
        pydantic.Field(default=None)
    )
    """
    A Friendly identifier you can use for referring to this Activity Mode. We really only used this in our URLs, so... you know, take that for whatever it's worth.
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

    is_aggregate_mode: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isAggregateMode")] = (
        pydantic.Field(default=None)
    )
    """
    If true, this mode is an aggregation of other, more specific modes rather than being a mode in itself. This includes modes that group Features/Events rather than Gameplay, such as Trials of The Nine: Trials of the Nine being an Event that is interesting to see aggregate data for, but when you play the activities within Trials of the Nine they are more specific activity modes such as Clash.
    """

    is_team_based: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="isTeamBased")] = (
        pydantic.Field(default=None)
    )
    """
    If True, this mode has oppositional teams fighting against each other rather than "Free-For-All" or Co-operative modes of play.
    Note that Aggregate modes are never marked as team based, even if they happen to be team based at the moment. At any time, an aggregate whose subordinates are only team based could be changed so that one or more aren't team based, and then this boolean won't make much sense (the aggregation would become "sometimes team based"). Let's not deal with that right now.
    """

    mode_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="modeType")] = pydantic.Field(
        default=None
    )
    """
    The Enumeration value for this Activity Mode. Pass this identifier into Stats endpoints to get aggregate stats for this mode.
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    The relative ordering of activity modes.
    """

    parent_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="parentHashes")
    ] = pydantic.Field(default=None)
    """
    The hash identifiers of the DestinyActivityModeDefinitions that represent all of the "parent" modes for this mode. For instance, the Nightfall Mode is also a member of AllStrikes and AllPvE.
    """

    pgcr_image: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="pgcrImage")] = pydantic.Field(
        default=None
    )
    """
    If this activity mode has a related PGCR image, this will be the path to said image.
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
