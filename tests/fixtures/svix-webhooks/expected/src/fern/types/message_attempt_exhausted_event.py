

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_attempt_exhausted_event_data import MessageAttemptExhaustedEventData
from .message_attempt_exhausted_event_type import MessageAttemptExhaustedEventType


class MessageAttemptExhaustedEvent(UniversalBaseModel):
    """
    Sent when a message delivery has failed (all of the retry attempts have been exhausted).
    """

    data: MessageAttemptExhaustedEventData
    type: MessageAttemptExhaustedEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
