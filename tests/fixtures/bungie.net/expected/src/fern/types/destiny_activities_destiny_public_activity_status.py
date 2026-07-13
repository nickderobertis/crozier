

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyActivitiesDestinyPublicActivityStatus(UniversalBaseModel):
    """
    Represents the public-facing status of an activity: any data about what is currently active in the Activity, regardless of an individual character's progress in it.
    """

    challenge_objective_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="challengeObjectiveHashes")
    ] = pydantic.Field(default=None)
    """
    Active Challenges for the activity, if any - represented as hashes for DestinyObjectiveDefinitions.
    """

    modifier_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="modifierHashes")
    ] = pydantic.Field(default=None)
    """
    The active modifiers on this activity, if any - represented as hashes for DestinyActivityModifierDefinitions.
    """

    reward_tooltip_items: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]], FieldMetadata(alias="rewardTooltipItems")
    ] = pydantic.Field(default=None)
    """
    If the activity itself provides any specific "mock" rewards, this will be the items and their quantity.
    Why "mock", you ask? Because these are the rewards as they are represented in the tooltip of the Activity.
    These are often pointers to fake items that look good in a tooltip, but represent an abstract concept of what you will get for a reward rather than the specific items you may obtain.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
