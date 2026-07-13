

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_public_milestone_activity import DestinyMilestonesDestinyPublicMilestoneActivity
from .destiny_milestones_destiny_public_milestone_challenge import DestinyMilestonesDestinyPublicMilestoneChallenge


class DestinyMilestonesDestinyPublicMilestoneQuest(UniversalBaseModel):
    activity: typing.Optional[DestinyMilestonesDestinyPublicMilestoneActivity] = pydantic.Field(default=None)
    """
    A milestone need not have an active activity, but if there is one it will be returned here, along with any variant and additional information.
    """

    challenges: typing.Optional[typing.List[DestinyMilestonesDestinyPublicMilestoneChallenge]] = pydantic.Field(
        default=None
    )
    """
    For the given quest there could be 0-to-Many challenges: mini quests that you can perform in the course of doing this quest, that may grant you rewards and benefits.
    """

    quest_item_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="questItemHash")] = (
        pydantic.Field(default=None)
    )
    """
    Quests are defined as Items in content. As such, this is the hash identifier of the DestinyInventoryItemDefinition that represents this quest. It will have pointers to all of the steps in the quest, and display information for the quest (title, description, icon etc) Individual steps will be referred to in the Quest item's DestinyInventoryItemDefinition.setData property, and themselves are Items with their own renderable data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
