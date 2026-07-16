

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_milestones_destiny_milestone_reward_entry import DestinyMilestonesDestinyMilestoneRewardEntry


class DestinyMilestonesDestinyMilestoneRewardCategory(UniversalBaseModel):
    """
    Represents a category of "summary" rewards that can be earned for the Milestone regardless of specific quest rewards that can be earned.
    """

    entries: typing.Optional[typing.List[DestinyMilestonesDestinyMilestoneRewardEntry]] = pydantic.Field(default=None)
    """
    The individual reward entries for this category, and their status.
    """

    reward_category_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardCategoryHash"),
        pydantic.Field(
            alias="rewardCategoryHash",
            description="Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up the category info in DestinyMilestoneDefinition.rewards.",
        ),
    ] = None
    """
    Look up the relevant DestinyMilestoneDefinition, and then use rewardCategoryHash to look up the category info in DestinyMilestoneDefinition.rewards.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
