

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyMilestonesDestinyMilestoneRewardEntry(UniversalBaseModel):
    """
    The character-specific data for a milestone's reward entry. See DestinyMilestoneDefinition for more information about Reward Entries.
    """

    earned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If TRUE, the player has earned this reward.
    """

    redeemed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If TRUE, the player has redeemed/picked up/obtained this reward. Feel free to alias this to "gotTheShinyBauble" in your own codebase.
    """

    reward_entry_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="rewardEntryHash"),
        pydantic.Field(
            alias="rewardEntryHash",
            description="The identifier for the reward entry in question. It is important to look up the related DestinyMilestoneRewardEntryDefinition to get the static details about the reward, which you can do by looking up the milestone's DestinyMilestoneDefinition and examining the DestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data.",
        ),
    ] = None
    """
    The identifier for the reward entry in question. It is important to look up the related DestinyMilestoneRewardEntryDefinition to get the static details about the reward, which you can do by looking up the milestone's DestinyMilestoneDefinition and examining the DestinyMilestoneDefinition.rewards[rewardCategoryHash].rewardEntries[rewardEntryHash] data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
