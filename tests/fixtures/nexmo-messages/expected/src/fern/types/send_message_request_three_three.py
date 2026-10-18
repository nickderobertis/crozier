

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_messenger_channel import ChannelOptionsMessengerChannel
from .channel_options_messenger_messenger import ChannelOptionsMessengerMessenger
from .from_id import FromId
from .send_message_request_three_three_video import SendMessageRequestThreeThreeVideo
from .to_id import ToId
from .video_message_type import VideoMessageType


class SendMessageRequestThreeThree(BaseMessageType):
    to: ToId
    from_: typing_extensions.Annotated[FromId, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsMessengerChannel = pydantic.Field()
    """
    The channel to send to. You must provide `messenger` in this field
    """

    video: SendMessageRequestThreeThreeVideo
    messenger: typing.Optional[ChannelOptionsMessengerMessenger] = None
    message_type: VideoMessageType = pydantic.Field()
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
