

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .callback_subscribe_batch_notify import CallbackSubscribeBatchNotify
from .callback_subscribe_callback import CallbackSubscribeCallback
from .callback_subscribe_retry_policy import CallbackSubscribeRetryPolicy


class CallbackSubscribe(UniversalBaseModel):
    """
    Callback subscription parameters.
    """

    retry_policy: typing_extensions.Annotated[
        typing.Optional[CallbackSubscribeRetryPolicy],
        FieldMetadata(alias="retryPolicy"),
        pydantic.Field(alias="retryPolicy", description="The retry policy to apply when notification failed."),
    ] = None
    """
    The retry policy to apply when notification failed.
    """

    batch_notify: typing_extensions.Annotated[
        typing.Optional[CallbackSubscribeBatchNotify],
        FieldMetadata(alias="batchNotify"),
        pydantic.Field(
            alias="batchNotify",
            description="\nNotification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.\n\n  * **At least, the ```size``` parameter should be provided.**\n  * **If the time window is not set then the default value will be applied.**",
        ),
    ] = None
    """
    
    Notification batch of events defined by a time window and batch size. If this field is not set, the callback will post only one event by call.
    
      * **At least, the ```size``` parameter should be provided.**
      * **If the time window is not set then the default value will be applied.**
    """

    callback: CallbackSubscribeCallback

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
