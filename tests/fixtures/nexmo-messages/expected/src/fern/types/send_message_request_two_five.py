

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_whatsapp_channel import ChannelOptionsWhatsappChannel
from .file_message_type import FileMessageType
from .from_number import FromNumber
from .send_message_request_two_five_file import SendMessageRequestTwoFiveFile
from .to_number import ToNumber


class SendMessageRequestTwoFive(BaseMessageType):
    to: ToNumber
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsWhatsappChannel = pydantic.Field()
    """
    The channel to send to. You must provide `whatsapp` in this field
    """

    file: SendMessageRequestTwoFiveFile
    message_type: FileMessageType = pydantic.Field()
    """
    The type of message to send. You must provide `file` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
