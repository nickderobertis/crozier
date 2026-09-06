

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_attempt_trigger_type import MessageAttemptTriggerType
from .message_status import MessageStatus
from .message_status_text import MessageStatusText


class MessageAttemptOut(UniversalBaseModel):
    endpoint_id: typing_extensions.Annotated[str, FieldMetadata(alias="endpointId"), pydantic.Field(alias="endpointId")]
    id: str
    msg_id: typing_extensions.Annotated[str, FieldMetadata(alias="msgId"), pydantic.Field(alias="msgId")]
    response: str
    response_duration_ms: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="responseDurationMs"),
        pydantic.Field(alias="responseDurationMs", description="Response duration in milliseconds."),
    ]
    """
    Response duration in milliseconds.
    """

    response_status_code: typing_extensions.Annotated[
        int, FieldMetadata(alias="responseStatusCode"), pydantic.Field(alias="responseStatusCode")
    ]
    status: MessageStatus
    status_text: typing_extensions.Annotated[
        MessageStatusText, FieldMetadata(alias="statusText"), pydantic.Field(alias="statusText")
    ]
    timestamp: dt.datetime
    trigger_type: typing_extensions.Annotated[
        MessageAttemptTriggerType, FieldMetadata(alias="triggerType"), pydantic.Field(alias="triggerType")
    ]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
