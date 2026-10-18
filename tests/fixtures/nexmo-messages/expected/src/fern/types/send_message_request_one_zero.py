

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .base_message_type import BaseMessageType
from .channel_options_mms_channel import ChannelOptionsMmsChannel
from .from_number import FromNumber
from .image_message_type import ImageMessageType
from .send_message_request_one_zero_image import SendMessageRequestOneZeroImage
from .to_number import ToNumber


class SendMessageRequestOneZero(BaseMessageType):
    to: ToNumber
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsMmsChannel = pydantic.Field()
    """
    The channel to send to. You must provide `mms` in this field
    """

    image: SendMessageRequestOneZeroImage
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
