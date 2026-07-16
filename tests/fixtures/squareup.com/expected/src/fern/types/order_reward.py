

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OrderReward(UniversalBaseModel):
    """
    Represents a reward that can be applied to an order if the necessary
    reward tier criteria are met. Rewards are created through the Loyalty API.
    """

    id: str = pydantic.Field()
    """
    The identifier of the reward.
    """

    reward_tier_id: str = pydantic.Field()
    """
    The identifier of the reward tier corresponding to this reward.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
