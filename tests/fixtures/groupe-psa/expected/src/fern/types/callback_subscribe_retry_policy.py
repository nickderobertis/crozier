

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .callback_subscribe_retry_policy_policy import CallbackSubscribeRetryPolicyPolicy


class CallbackSubscribeRetryPolicy(UniversalBaseModel):
    """
    The retry policy to apply when notification failed.
    """

    policy: CallbackSubscribeRetryPolicyPolicy = pydantic.Field()
    """
    Defines the retry rules following a notification failure (ie the return code is not HTTP 2XX for  WebHook mode). ```None``` means with a single try, ```Bounded``` with a limited number of tries and ```Always```  with an infinite number of tries. 
    """

    retry_number: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="retryNumber"),
        pydantic.Field(
            alias="retryNumber",
            description="Maximum number of attempts (to be used with a retryPolicy set to ```Bounded```).",
        ),
    ] = None
    """
    Maximum number of attempts (to be used with a retryPolicy set to ```Bounded```).
    """

    retry_delay: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="retryDelay"),
        pydantic.Field(
            alias="retryDelay",
            description="Time to wait (expressed in seconds) before retrying to push a notification (ignored if retryPolicy is set to ```None```).",
        ),
    ] = None
    """
    Time to wait (expressed in seconds) before retrying to push a notification (ignored if retryPolicy is set to ```None```).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
