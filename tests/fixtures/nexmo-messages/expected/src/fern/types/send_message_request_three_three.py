

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_messenger import ChannelOptionsMessenger
from .send_message_request_three_three_video import SendMessageRequestThreeThreeVideo
from .video_message_type import VideoMessageType


class SendMessageRequestThreeThree(ChannelOptionsMessenger, BaseMessageType):
    video: typing.Optional[SendMessageRequestThreeThreeVideo] = None
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
