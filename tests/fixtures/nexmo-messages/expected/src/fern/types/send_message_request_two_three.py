

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .audio_message_type import AudioMessageType
from .base_message_type import BaseMessageType
from .channel_options_whatsapp import ChannelOptionsWhatsapp
from .send_message_request_two_three_audio import SendMessageRequestTwoThreeAudio


class SendMessageRequestTwoThree(ChannelOptionsWhatsapp, BaseMessageType):
    audio: typing.Optional[SendMessageRequestTwoThreeAudio] = None
    message_type: typing.Optional[AudioMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `audio` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
