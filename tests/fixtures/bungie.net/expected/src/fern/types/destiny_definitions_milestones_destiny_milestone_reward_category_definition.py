

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_definitions_common_destiny_display_properties_definition import (
    DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition,
)
from .destiny_definitions_milestones_destiny_milestone_reward_entry_definition import (
    DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition,
)


class DestinyDefinitionsMilestonesDestinyMilestoneRewardCategoryDefinition(UniversalBaseModel):
    """
    The definition of a category of rewards, that contains many individual rewards.
    """

    category_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="categoryHash"),
        pydantic.Field(
            alias="categoryHash",
            description="Identifies the reward category. Only guaranteed unique within this specific component!",
        ),
    ] = None
    """
    Identifies the reward category. Only guaranteed unique within this specific component!
    """

    category_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="categoryIdentifier"),
        pydantic.Field(
            alias="categoryIdentifier",
            description="The string identifier for the category, if you want to use it for some end. Guaranteed unique within the specific component.",
        ),
    ] = None
    """
    The string identifier for the category, if you want to use it for some end. Guaranteed unique within the specific component.
    """

    display_properties: typing_extensions.Annotated[
        typing.Optional[DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition],
        FieldMetadata(alias="displayProperties"),
        pydantic.Field(alias="displayProperties", description="Hopefully this is obvious by now."),
    ] = None
    """
    Hopefully this is obvious by now.
    """

    order: typing.Optional[int] = pydantic.Field(default=None)
    """
    If you want to use BNet's recommended order for rendering categories programmatically, use this value and compare it to other categories to determine the order in which they should be rendered. I don't feel great about putting this here, I won't lie.
    """

    reward_entries: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, DestinyDefinitionsMilestonesDestinyMilestoneRewardEntryDefinition]],
        FieldMetadata(alias="rewardEntries"),
        pydantic.Field(
            alias="rewardEntries",
            description="If this milestone can provide rewards, this will define the sets of rewards that can be earned, the conditions under which they can be acquired, internal data that we'll use at runtime to determine whether you've already earned or redeemed this set of rewards, and the category that this reward should be placed under.",
        ),
    ] = None
    """
    If this milestone can provide rewards, this will define the sets of rewards that can be earned, the conditions under which they can be acquired, internal data that we'll use at runtime to determine whether you've already earned or redeemed this set of rewards, and the category that this reward should be placed under.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
