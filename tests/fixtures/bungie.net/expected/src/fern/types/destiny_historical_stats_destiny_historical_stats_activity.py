

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyHistoricalStatsDestinyHistoricalStatsActivity(UniversalBaseModel):
    """
    Summary information about the activity that was played.
    """

    director_activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="directorActivityHash"),
        pydantic.Field(
            alias="directorActivityHash",
            description="The unique hash identifier of the DestinyActivityDefinition that was played.",
        ),
    ] = None
    """
    The unique hash identifier of the DestinyActivityDefinition that was played.
    """

    instance_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="instanceId"),
        pydantic.Field(
            alias="instanceId",
            description="The unique identifier for this *specific* match that was played.\r\nThis value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint.",
        ),
    ] = None
    """
    The unique identifier for this *specific* match that was played.
    This value can be used to get additional data about this activity such as who else was playing via the GetPostGameCarnageReport endpoint.
    """

    is_private: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isPrivate"),
        pydantic.Field(alias="isPrivate", description="Whether or not the match was a private match."),
    ] = None
    """
    Whether or not the match was a private match.
    """

    membership_type: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="membershipType"),
        pydantic.Field(
            alias="membershipType",
            description="The Membership Type indicating the platform on which this match was played.",
        ),
    ] = None
    """
    The Membership Type indicating the platform on which this match was played.
    """

    mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    Indicates the most specific game mode of the activity that we could find.
    """

    modes: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The list of all Activity Modes to which this activity applies, including aggregates. This will let you see, for example, whether the activity was both Clash and part of the Trials of the Nine event.
    """

    reference_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="referenceId"),
        pydantic.Field(
            alias="referenceId",
            description="The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now.",
        ),
    ] = None
    """
    The unique hash identifier of the DestinyActivityDefinition that was played. If I had this to do over, it'd be named activityHash. Too late now.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
