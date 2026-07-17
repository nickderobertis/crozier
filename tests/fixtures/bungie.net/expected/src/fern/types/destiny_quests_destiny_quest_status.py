

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_quests_destiny_objective_progress import DestinyQuestsDestinyObjectiveProgress


class DestinyQuestsDestinyQuestStatus(UniversalBaseModel):
    """
    Data regarding the progress of a Quest for a specific character. Quests are composed of multiple steps, each with potentially multiple objectives: this QuestStatus will return Objective data for the *currently active* step in this quest.
    """

    completed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the whole quest has been completed, regardless of whether or not you have redeemed the rewards for the quest.
    """

    item_instance_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="itemInstanceId"),
        pydantic.Field(
            alias="itemInstanceId",
            description="The current Quest Step will be an instanced item in the player's inventory. If you care about that, this is the instance ID of that item.",
        ),
    ] = None
    """
    The current Quest Step will be an instanced item in the player's inventory. If you care about that, this is the instance ID of that item.
    """

    quest_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="questHash"),
        pydantic.Field(
            alias="questHash",
            description="The hash identifier for the Quest Item. (Note: Quests are defined as Items, and thus you would use this to look up the quest's DestinyInventoryItemDefinition). For information on all steps in the quest, you can then examine its DestinyInventoryItemDefinition.setData property for Quest Steps (which are *also* items). You can use the Item Definition to display human readable data about the overall quest.",
        ),
    ] = None
    """
    The hash identifier for the Quest Item. (Note: Quests are defined as Items, and thus you would use this to look up the quest's DestinyInventoryItemDefinition). For information on all steps in the quest, you can then examine its DestinyInventoryItemDefinition.setData property for Quest Steps (which are *also* items). You can use the Item Definition to display human readable data about the overall quest.
    """

    redeemed: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not you have redeemed rewards for this quest.
    """

    started: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not you have started this quest.
    """

    step_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="stepHash"),
        pydantic.Field(
            alias="stepHash",
            description="The hash identifier of the current Quest Step, which is also a DestinyInventoryItemDefinition. You can use this to get human readable data about the current step and what to do in that step.",
        ),
    ] = None
    """
    The hash identifier of the current Quest Step, which is also a DestinyInventoryItemDefinition. You can use this to get human readable data about the current step and what to do in that step.
    """

    step_objectives: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyQuestsDestinyObjectiveProgress]],
        FieldMetadata(alias="stepObjectives"),
        pydantic.Field(
            alias="stepObjectives",
            description="A step can have multiple objectives. This will give you the progress for each objective in the current step, in the order in which they are rendered in-game.",
        ),
    ] = None
    """
    A step can have multiple objectives. This will give you the progress for each objective in the current step, in the order in which they are rendered in-game.
    """

    tracked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the quest is tracked
    """

    vendor_hash: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="vendorHash"),
        pydantic.Field(
            alias="vendorHash",
            description="If the quest has a related Vendor that you should talk to in order to initiate the quest/earn rewards/continue the quest, this will be the hash identifier of that Vendor. Look it up its DestinyVendorDefinition.",
        ),
    ] = None
    """
    If the quest has a related Vendor that you should talk to in order to initiate the quest/earn rewards/continue the quest, this will be the hash identifier of that Vendor. Look it up its DestinyVendorDefinition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
