

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyPublicMilestoneChallenge(UniversalBaseModel):
    """
    A Milestone can have many Challenges. Challenges are just extra Objectives that provide a fun way to mix-up play and provide extra rewards.
    """

    activity_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="activityHash")] = (
        pydantic.Field(default=None)
    )
    """
    IF the Objective is related to a specific Activity, this will be that activity's hash. Use it to look up the DestinyActivityDefinition for additional data to show.
    """

    objective_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="objectiveHash")] = (
        pydantic.Field(default=None)
    )
    """
    The objective for the Challenge, which should have human-readable data about what needs to be done to accomplish the objective. Use this hash to look up the DestinyObjectiveDefinition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
