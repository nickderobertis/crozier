

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_object_reference import CatalogObjectReference
from .loyalty_program_reward_definition import LoyaltyProgramRewardDefinition


class LoyaltyProgramRewardTier(UniversalBaseModel):
    """
    Represents a reward tier in a loyalty program. A reward tier defines how buyers can redeem points for a reward, such as the number of points required and the value and scope of the discount. A loyalty program can offer multiple reward tiers.
    """

    created_at: str = pydantic.Field()
    """
    The timestamp when the reward tier was created, in RFC 3339 format.
    """

    definition: LoyaltyProgramRewardDefinition
    id: str = pydantic.Field()
    """
    The Square-assigned ID of the reward tier.
    """

    name: str = pydantic.Field()
    """
    The name of the reward tier.
    """

    points: int = pydantic.Field()
    """
    The points exchanged for the reward tier.
    """

    pricing_rule_reference: typing.Optional[CatalogObjectReference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
