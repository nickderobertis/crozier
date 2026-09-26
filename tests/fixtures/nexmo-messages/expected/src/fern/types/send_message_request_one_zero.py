

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_mms import ChannelOptionsMms
from .image_message_type import ImageMessageType
from .send_message_request_one_zero_image import SendMessageRequestOneZeroImage


class SendMessageRequestOneZero(ChannelOptionsMms, BaseMessageType):
    image: typing.Optional[SendMessageRequestOneZeroImage] = None
    message_type: typing.Optional[ImageMessageType] = pydantic.Field(default=None)
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
