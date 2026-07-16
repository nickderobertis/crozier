

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventRedeemReward(UniversalBaseModel):
    """
    Provides metadata when the event `type` is `REDEEM_REWARD`.
    """

    loyalty_program_id: str = pydantic.Field()
    """
    The ID of the [loyalty program](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgram).
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) that redeemed the reward.
    This field is returned only if the Orders API is used to process orders.
    """

    reward_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the redeemed [loyalty reward](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyReward).
    This field is returned only if the event source is `LOYALTY_API`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
