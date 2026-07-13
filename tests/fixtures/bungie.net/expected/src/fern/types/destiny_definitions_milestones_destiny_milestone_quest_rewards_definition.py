

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destiny_definitions_milestones_destiny_milestone_quest_reward_item import (
    DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem,
)


class DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition(UniversalBaseModel):
    """
    If rewards are given in a quest - as opposed to overall in the entire Milestone - there's way less to track. We're going to simplify this contract as a result. However, this also gives us the opportunity to potentially put more than just item information into the reward data if we're able to mine it out in the future. Remember this if you come back and ask "why are quest reward items nested inside of their own class?"
    """

    items: typing.Optional[typing.List[DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardItem]] = pydantic.Field(
        default=None
    )
    """
    The items that represent your reward for completing the quest.
    Be warned, these could be "dummy" items: items that are only used to render a good-looking in-game tooltip, but aren't the actual items themselves.
    For instance, when experience is given there's often a dummy item representing "experience", with quantity being the amount of experience you got. We don't have a programmatic association between those and whatever Progression is actually getting that experience... yet.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
