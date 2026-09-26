

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_mms import ChannelOptionsMms
from .send_message_request_one_three_message_type import SendMessageRequestOneThreeMessageType
from .send_message_request_one_three_video import SendMessageRequestOneThreeVideo


class SendMessageRequestOneThree(ChannelOptionsMms, BaseMessageType):
    message_type: typing.Optional[SendMessageRequestOneThreeMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `video` in this field.
    
    For best device and network support .mp4 is recommended. Not supported for US short codes.
    """

    video: typing.Optional[SendMessageRequestOneThreeVideo] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
