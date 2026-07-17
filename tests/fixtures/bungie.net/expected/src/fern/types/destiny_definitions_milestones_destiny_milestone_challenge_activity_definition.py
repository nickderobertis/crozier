

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_milestones_destiny_milestone_challenge_activity_graph_node_entry import (
    DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityGraphNodeEntry,
)
from .destiny_definitions_milestones_destiny_milestone_challenge_activity_phase import (
    DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityPhase,
)
from .destiny_definitions_milestones_destiny_milestone_challenge_definition import (
    DestinyDefinitionsMilestonesDestinyMilestoneChallengeDefinition,
)


class DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityDefinition(UniversalBaseModel):
    activity_graph_nodes: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityGraphNodeEntry]],
        FieldMetadata(alias="activityGraphNodes"),
        pydantic.Field(
            alias="activityGraphNodes",
            description="If the activity and its challenge is visible on any of these nodes, it will be returned.",
        ),
    ] = None
    """
    If the activity and its challenge is visible on any of these nodes, it will be returned.
    """

    activity_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="activityHash"),
        pydantic.Field(alias="activityHash", description="The activity for which this challenge is active."),
    ] = None
    """
    The activity for which this challenge is active.
    """

    challenges: typing.Optional[typing.List[DestinyDefinitionsMilestonesDestinyMilestoneChallengeDefinition]] = None
    phases: typing.Optional[typing.List[DestinyDefinitionsMilestonesDestinyMilestoneChallengeActivityPhase]] = (
        pydantic.Field(default=None)
    )
    """
    Phases related to this activity, if there are any.
    These will be listed in the order in which they will appear in the actual activity.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
