

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyDefinitionsDestinyActivityRewardDefinition(UniversalBaseModel):
    """
    Activities can refer to one or more sets of tooltip-friendly reward data. These are the definitions for those tooltip friendly rewards.
    """

    reward_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]],
        FieldMetadata(alias="rewardItems"),
        pydantic.Field(
            alias="rewardItems",
            description='The "Items provided" in the reward. This is almost always a pointer to a DestinyInventoryItemDefintion for an item that you can\'t actually earn in-game, but that has name/description/icon information for the vague concept of the rewards you will receive. This is because the actual reward generation is non-deterministic and extremely complicated, so the best the game can do is tell you what you\'ll get in vague terms. And so too shall we.\r\nInteresting trivia: you actually *do* earn these items when you complete the activity. They go into a single-slot bucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that match these "dummy" items. You can even see them if you look at the last one you earned in your profile-level inventory through the BNet API! Who said reading documentation is a waste of time?',
        ),
    ] = None
    """
    The "Items provided" in the reward. This is almost always a pointer to a DestinyInventoryItemDefintion for an item that you can't actually earn in-game, but that has name/description/icon information for the vague concept of the rewards you will receive. This is because the actual reward generation is non-deterministic and extremely complicated, so the best the game can do is tell you what you'll get in vague terms. And so too shall we.
    Interesting trivia: you actually *do* earn these items when you complete the activity. They go into a single-slot bucket on your profile, which is how you see the pop-ups of these rewards when you complete an activity that match these "dummy" items. You can even see them if you look at the last one you earned in your profile-level inventory through the BNet API! Who said reading documentation is a waste of time?
    """

    reward_text: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rewardText"),
        pydantic.Field(alias="rewardText", description="The header for the reward set, if any."),
    ] = None
    """
    The header for the reward set, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
