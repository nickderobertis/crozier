

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_attempt_recovered_event_data import MessageAttemptRecoveredEventData
from .message_attempt_recovered_event_type import MessageAttemptRecoveredEventType


class MessageAttemptRecoveredEvent(UniversalBaseModel):
    """
    Sent on a successful dispatch after an earlier failure op webhook has already been sent.
    """

    data: MessageAttemptRecoveredEventData
    type: MessageAttemptRecoveredEventType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
