

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_milestone_activity_completion_status import (
    DestinyMilestonesDestinyMilestoneActivityCompletionStatus,
)


class DestinyMilestonesDestinyMilestoneActivityVariant(UniversalBaseModel):
    """
    Represents custom data that we know about an individual variant of an activity.
    """

    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash for the specific variant of the activity related to this milestone. You can pull more detailed static info from the DestinyActivityDefinition, such as difficulty level.
    """

    activity_mode_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityModeHash")] = (
        pydantic.Field(default=None)
    )
    """
    The hash identifier of the most specific Activity Mode under which this activity is played. This is useful for situations where the activity in question is - for instance - a PVP map, but it's not clear what mode the PVP map is being played under. If it's a playlist, this will be less specific: but hopefully useful in some way.
    """

    activity_mode_type: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityModeType")] = (
        pydantic.Field(default=None)
    )
    """
    The enumeration equivalent of the most specific Activity Mode under which this activity is played.
    """

    completion_status: typing_extensions.Annotated[
        typing.Optional[DestinyMilestonesDestinyMilestoneActivityCompletionStatus],
        FieldMetadata(alias="completionStatus"),
    ] = pydantic.Field(default=None)
    """
    An OPTIONAL component: if it makes sense to talk about this activity variant in terms of whether or not it has been completed or what progress you have made in it, this will be returned. Otherwise, this will be NULL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
