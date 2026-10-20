

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_sms_channel import ChannelOptionsSmsChannel
from .from_number import FromNumber
from .text_message_type import TextMessageType
from .to_number import ToNumber


class SendMessageRequestZero(BaseMessageType):
    to: ToNumber
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsSmsChannel = pydantic.Field()
    """
    The channel to send to. You must provide `sms` in this field
    """

    text: typing.Any
    message_type: TextMessageType = pydantic.Field()
    """
    The type of message to send. You must provide `text` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
