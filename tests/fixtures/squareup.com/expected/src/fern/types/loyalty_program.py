

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .loyalty_program_accrual_rule import LoyaltyProgramAccrualRule
from .loyalty_program_expiration_policy import LoyaltyProgramExpirationPolicy
from .loyalty_program_reward_tier import LoyaltyProgramRewardTier
from .loyalty_program_terminology import LoyaltyProgramTerminology


class LoyaltyProgram(UniversalBaseModel):
    """
    Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for rewards.
    Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.
    For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).
    """

    accrual_rules: typing.List[LoyaltyProgramAccrualRule] = pydantic.Field()
    """
    Defines how buyers can earn loyalty points.
    """

    created_at: str = pydantic.Field()
    """
    The timestamp when the program was created, in RFC 3339 format.
    """

    expiration_policy: typing.Optional[LoyaltyProgramExpirationPolicy] = None
    id: str = pydantic.Field()
    """
    The Square-assigned ID of the loyalty program. Updates to 
    the loyalty program do not modify the identifier.
    """

    location_ids: typing.List[str] = pydantic.Field()
    """
    The [locations](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) at which the program is active.
    """

    reward_tiers: typing.List[LoyaltyProgramRewardTier] = pydantic.Field()
    """
    The list of rewards for buyers, sorted by ascending points.
    """

    status: str = pydantic.Field()
    """
    Whether the program is currently active.
    """

    terminology: LoyaltyProgramTerminology
    updated_at: str = pydantic.Field()
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
