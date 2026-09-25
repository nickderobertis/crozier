

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_whatsapp import ChannelOptionsWhatsapp
from .send_message_request_two_four_video import SendMessageRequestTwoFourVideo
from .video_message_type import VideoMessageType


class SendMessageRequestTwoFour(ChannelOptionsWhatsapp, BaseMessageType):
    video: typing.Optional[SendMessageRequestTwoFourVideo] = None
    message_type: typing.Optional[VideoMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `video` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
