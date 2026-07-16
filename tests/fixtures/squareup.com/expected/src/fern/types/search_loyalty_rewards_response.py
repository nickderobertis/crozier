

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .loyalty_reward import LoyaltyReward


class SearchLoyaltyRewardsResponse(UniversalBaseModel):
    """
    A response that includes the loyalty rewards satisfying the search criteria.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent 
    request. If empty, this is the final response.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    rewards: typing.Optional[typing.List[LoyaltyReward]] = pydantic.Field(default=None)
    """
    The loyalty rewards that satisfy the search criteria.
    These are returned in descending order by `updated_at`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
