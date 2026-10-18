

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_viber_with_button_channel import ChannelOptionsViberWithButtonChannel
from .channel_options_viber_with_button_viber_service import ChannelOptionsViberWithButtonViberService
from .from_id import FromId
from .image_message_type import ImageMessageType
from .send_message_request_four_one_image import SendMessageRequestFourOneImage
from .to_number import ToNumber


class SendMessageRequestFourOne(BaseMessageType):
    to: ToNumber
    from_: typing_extensions.Annotated[FromId, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsViberWithButtonChannel = pydantic.Field()
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    image: SendMessageRequestFourOneImage
    viber_service: typing.Optional[ChannelOptionsViberWithButtonViberService] = None
    message_type: ImageMessageType = pydantic.Field()
    """
    The type of message to send. You must provide `image` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
