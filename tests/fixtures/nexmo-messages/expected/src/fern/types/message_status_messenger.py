

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .from_id import FromId
from .message_status_base_error import MessageStatusBaseError
from .message_status_base_usage import MessageStatusBaseUsage
from .message_status_messenger_channel import MessageStatusMessengerChannel
from .message_status_messenger_status import MessageStatusMessengerStatus
from .message_uuid import MessageUuid
from .to_id import ToId


class MessageStatusMessenger(UniversalBaseModel):
    channel: typing.Optional[MessageStatusMessengerChannel] = pydantic.Field(default=None)
    """
    The channel sending to.
    """

    from_: typing_extensions.Annotated[
        typing.Optional[FromId], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    status: typing.Optional[MessageStatusMessengerStatus] = pydantic.Field(default=None)
    """
    The status of the message.
    """

    to: typing.Optional[ToId] = None
    client_ref: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client reference of up to 100 characters. The reference will be present in every message status.
    """

    error: typing.Optional[MessageStatusBaseError] = pydantic.Field(default=None)
    """
    If the message encountered a problem a descriptive error will be supplied in this object.
    """

    message_uuid: MessageUuid
    timestamp: str = pydantic.Field()
    """
    The datetime of when the event occurred, in `ISO 8601` format.
    """

    usage: typing.Optional[MessageStatusBaseUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
