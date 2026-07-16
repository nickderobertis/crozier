

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyReward(UniversalBaseModel):
    """
    Represents a contract to redeem loyalty points for a [reward tier](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgramRewardTier) discount. Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state. For more information, see [Redeem loyalty rewards](https://developer.squareup.com/docs/loyalty-api/overview#redeem-loyalty-rewards).
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the reward was created, in RFC 3339 format.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the loyalty reward.
    """

    loyalty_account_id: str = pydantic.Field()
    """
    The Square-assigned ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) to which the reward belongs.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the [order](https://developer.squareup.com/reference/square_2021-08-18/objects/Order) to which the reward is attached.
    """

    points: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of loyalty points used for the reward.
    """

    redeemed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the reward was redeemed, in RFC 3339 format.
    """

    reward_tier_id: str = pydantic.Field()
    """
    The Square-assigned ID of the [reward tier](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyProgramRewardTier) used to create the reward.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of a loyalty reward.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the reward was last updated, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
