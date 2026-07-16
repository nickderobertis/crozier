

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error
from .subscription import Subscription


class ResumeSubscriptionResponse(UniversalBaseModel):
    """
    Defines parameters in a
    [ResumeSubscription](https://developer.squareup.com/reference/square_2021-08-18/subscriptions-api/resume-subscription) endpoint
    response.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    subscription: typing.Optional[Subscription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
