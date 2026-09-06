

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .message_attempet_last import MessageAttempetLast


class MessageAttemptExhaustedEventData(UniversalBaseModel):
    """
    Sent when a message delivery has failed (all of the retry attempts have been exhausted) as a "message.attempt.exhausted" type or after it's failed four times as a "message.attempt.failing" event.
    """

    app_id: typing_extensions.Annotated[str, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]
    app_uid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="appUid"), pydantic.Field(alias="appUid")
    ] = None
    endpoint_id: typing_extensions.Annotated[str, FieldMetadata(alias="endpointId"), pydantic.Field(alias="endpointId")]
    last_attempt: typing_extensions.Annotated[
        MessageAttempetLast, FieldMetadata(alias="lastAttempt"), pydantic.Field(alias="lastAttempt")
    ]
    msg_event_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="msgEventId"), pydantic.Field(alias="msgEventId")
    ] = None
    msg_id: typing_extensions.Annotated[str, FieldMetadata(alias="msgId"), pydantic.Field(alias="msgId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
