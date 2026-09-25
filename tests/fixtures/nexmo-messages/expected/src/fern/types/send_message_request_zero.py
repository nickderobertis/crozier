

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_sms import ChannelOptionsSms
from .text_message_type import TextMessageType


class SendMessageRequestZero(ChannelOptionsSms, BaseMessageType):
    text: typing.Optional[typing.Any] = pydantic.Field(default=None)
    """
    The text of message to send; limited to 1000 characters. The Messages API automatically detects unicode characters when sending SMS and sends the message as a unicode SMS. For more information on how concatenation and encoding please visit: [developer.nexmo.com/messaging/sms/guides/concatenation-and-encoding](https://developer.nexmo.com/messaging/sms/guides/concatenation-and-encoding).
    """

    message_type: typing.Optional[TextMessageType] = pydantic.Field(default=None)
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
