

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_mms import ChannelOptionsMms
from .send_message_request_one_two_audio import SendMessageRequestOneTwoAudio
from .send_message_request_one_two_message_type import SendMessageRequestOneTwoMessageType


class SendMessageRequestOneTwo(ChannelOptionsMms, BaseMessageType):
    audio: typing.Optional[SendMessageRequestOneTwoAudio] = None
    message_type: typing.Optional[SendMessageRequestOneTwoMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `audio` in this field.
    
    For best device and network support .mp3 is recommended. Not supported for US short codes.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
