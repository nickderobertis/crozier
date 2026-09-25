

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .remote_callback_subscribe_retry_policy_policy import RemoteCallbackSubscribeRetryPolicyPolicy


class RemoteCallbackSubscribeRetryPolicy(UniversalBaseModel):
    """
    The retry policy to apply when notification failed.
    """

    policy: RemoteCallbackSubscribeRetryPolicyPolicy = pydantic.Field()
    """
    Defines the retry rules following a notification failure (ie the return code is not HTTP 2XX for  WebHook mode). ```None``` means with a single try, ```Bounded``` with a limited number of tries. 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
