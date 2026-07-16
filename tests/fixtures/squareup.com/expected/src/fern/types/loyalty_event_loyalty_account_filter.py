

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LoyaltyEventLoyaltyAccountFilter(UniversalBaseModel):
    """
    Filter events by loyalty account.
    """

    loyalty_account_id: str = pydantic.Field()
    """
    The ID of the [loyalty account](https://developer.squareup.com/reference/square_2021-08-18/objects/LoyaltyAccount) associated with loyalty events.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
