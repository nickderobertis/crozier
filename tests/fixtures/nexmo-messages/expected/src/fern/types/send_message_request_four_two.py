

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_viber_video_channel import ChannelOptionsViberVideoChannel
from .channel_options_viber_video_viber_service import ChannelOptionsViberVideoViberService
from .from_id import FromId
from .send_message_request_four_two_video import SendMessageRequestFourTwoVideo
from .to_number import ToNumber
from .video_message_type import VideoMessageType


class SendMessageRequestFourTwo(BaseMessageType):
    to: ToNumber
    from_: typing_extensions.Annotated[FromId, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsViberVideoChannel = pydantic.Field()
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    video: SendMessageRequestFourTwoVideo
    viber_service: typing.Optional[ChannelOptionsViberVideoViberService] = None
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
