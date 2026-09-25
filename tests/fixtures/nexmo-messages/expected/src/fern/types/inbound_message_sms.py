

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .from_number import FromNumber
from .inbound_message_sms_channel import InboundMessageSmsChannel
from .inbound_message_sms_sms import InboundMessageSmsSms
from .message_uuid import MessageUuid
from .timestamp import Timestamp
from .to_number import ToNumber
from .usage import Usage


class InboundMessageSms(UniversalBaseModel):
    channel: InboundMessageSmsChannel = pydantic.Field()
    """
    The channel the message came in on
    """

    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    message_uuid: MessageUuid
    sms: typing.Optional[InboundMessageSmsSms] = pydantic.Field(default=None)
    """
    Channel specific metadata for SMS
    """

    text: str = pydantic.Field()
    """
    The UTF-8 encoded text of the inbound message.
    """

    timestamp: Timestamp
    to: ToNumber
    usage: typing.Optional[Usage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
