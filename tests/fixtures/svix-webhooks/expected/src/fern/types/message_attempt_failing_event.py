

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_attempt_failing_event_data import MessageAttemptFailingEventData
from .message_attempt_failing_event_type import MessageAttemptFailingEventType


class MessageAttemptFailingEvent(UniversalBaseModel):
    """
    Sent after a message has been failing for a few times.
    It's sent on the fourth failure. It complements `message.attempt.exhausted` which is sent after the last failure.
    """

    data: MessageAttemptFailingEventData
    type: MessageAttemptFailingEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
