

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_milestones_destiny_milestone_activity_phase import DestinyMilestonesDestinyMilestoneActivityPhase


class DestinyMilestonesDestinyMilestoneActivityCompletionStatus(UniversalBaseModel):
    """
    Represents this player's personal completion status for the Activity under a Milestone, if the activity has trackable completion and progress information. (most activities won't, or the concept won't apply. For instance, it makes sense to talk about a tier of a raid as being Completed or having progress, but it doesn't make sense to talk about a Crucible Playlist in those terms.
    """

    completed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the activity has been "completed", that information will be returned here.
    """

    phases: typing.Optional[typing.List[DestinyMilestonesDestinyMilestoneActivityPhase]] = pydantic.Field(default=None)
    """
    If the Activity has discrete "phases" that we can track, that info will be here. Otherwise, this value will be NULL. Note that this is a list and not a dictionary: the order implies the ascending order of phases or progression in this activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
