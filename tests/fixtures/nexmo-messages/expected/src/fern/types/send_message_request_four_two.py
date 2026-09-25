

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_viber_video import ChannelOptionsViberVideo
from .send_message_request_four_two_video import SendMessageRequestFourTwoVideo
from .video_message_type import VideoMessageType


class SendMessageRequestFourTwo(ChannelOptionsViberVideo, BaseMessageType):
    video: typing.Optional[SendMessageRequestFourTwoVideo] = None
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
