

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RetrieveSubscriptionRequest(UniversalBaseModel):
    """
    Defines parameters in a
    [RetrieveSubscription](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/retrieve-subscription) endpoint request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
