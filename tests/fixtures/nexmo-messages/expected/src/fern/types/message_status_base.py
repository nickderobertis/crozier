

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .from_number import FromNumber
from .message_status_base_error import MessageStatusBaseError
from .message_status_base_status import MessageStatusBaseStatus
from .message_status_base_usage import MessageStatusBaseUsage
from .message_uuid import MessageUuid
from .to_number import ToNumber


class MessageStatusBase(UniversalBaseModel):
    client_ref: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client reference of up to 100 characters. The reference will be present in every message status.
    """

    error: typing.Optional[MessageStatusBaseError] = pydantic.Field(default=None)
    """
    If the message encountered a problem a descriptive error will be supplied in this object.
    """

    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    message_uuid: MessageUuid
    status: MessageStatusBaseStatus = pydantic.Field()
    """
    The status of the message.
    """

    timestamp: str = pydantic.Field()
    """
    The datetime of when the event occurred, in `ISO 8601` format.
    """

    to: ToNumber
    usage: typing.Optional[MessageStatusBaseUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
