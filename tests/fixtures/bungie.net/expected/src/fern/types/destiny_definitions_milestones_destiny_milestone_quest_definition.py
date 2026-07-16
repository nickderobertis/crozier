

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_milestones_destiny_milestone_activity_definition import (
    DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition,
)
from .destiny_definitions_milestones_destiny_milestone_quest_rewards_definition import (
    DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition,
)


class DestinyDefinitionsMilestonesDestinyMilestoneQuestDefinition(UniversalBaseModel):
    """
    Any data we need to figure out whether this Quest Item is the currently active one for the conceptual Milestone. Even just typing this description, I already regret it.
    """

    activities: typing.Optional[typing.Dict[str, DestinyDefinitionsMilestonesDestinyMilestoneActivityDefinition]] = (
        pydantic.Field(default=None)
    )
    """
    The full set of all possible "conceptual activities" that are related to this Milestone. Tiers or alternative modes of play within these conceptual activities will be defined as sub-entities. Keyed by the Conceptual Activity Hash. Use the key to look up DestinyActivityDefinition.
    """

    destination_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="destinationHash"),
        pydantic.Field(
            alias="destinationHash",
            description="Sometimes, a Milestone's quest is related to an entire Destination rather than a specific activity. In that situation, this will be the hash of that Destination. Hotspots are currently the only Milestones that expose this data, but that does not preclude this data from being returned for other Milestones in the future.",
        ),
    ] = None
    """
    Sometimes, a Milestone's quest is related to an entire Destination rather than a specific activity. In that situation, this will be the hash of that Destination. Hotspots are currently the only Milestones that expose this data, but that does not preclude this data from being returned for other Milestones in the future.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(
            alias="displayProperties",
            description="The individual quests may have different definitions from the overall milestone: if there's a specific active quest, use these displayProperties instead of that of the overall DestinyMilestoneDefinition.",
        ),
    ] = None
    """
    The individual quests may have different definitions from the overall milestone: if there's a specific active quest, use these displayProperties instead of that of the overall DestinyMilestoneDefinition.
    """

    override_image: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="overrideImage"),
        pydantic.Field(
            alias="overrideImage",
            description="If populated, this image can be shown instead of the generic milestone's image when this quest is live, or it can be used to show a background image for the quest itself that differs from that of the Activity or the Milestone.",
        ),
    ] = None
    """
    If populated, this image can be shown instead of the generic milestone's image when this quest is live, or it can be used to show a background image for the quest itself that differs from that of the Activity or the Milestone.
    """

    quest_item_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="questItemHash"),
        pydantic.Field(
            alias="questItemHash",
            description="The item representing this Milestone quest. Use this hash to look up the DestinyInventoryItemDefinition for the quest to find its steps and human readable data.",
        ),
    ] = None
    """
    The item representing this Milestone quest. Use this hash to look up the DestinyInventoryItemDefinition for the quest to find its steps and human readable data.
    """

    quest_rewards: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsMilestonesDestinyMilestoneQuestRewardsDefinition],
        FieldMetadata(alias="questRewards"),
        pydantic.Field(
            alias="questRewards",
            description="The rewards you will get for completing this quest, as best as we could extract them from our data. Sometimes, it'll be a decent amount of data. Sometimes, it's going to be sucky. Sorry.",
        ),
    ] = None
    """
    The rewards you will get for completing this quest, as best as we could extract them from our data. Sometimes, it'll be a decent amount of data. Sometimes, it's going to be sucky. Sorry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
