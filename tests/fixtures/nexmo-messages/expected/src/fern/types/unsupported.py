

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .unsupported_message_type import UnsupportedMessageType


class Unsupported(BaseMessageType):
    message_type: UnsupportedMessageType = pydantic.Field()
    """
    The type of message to send. Will be `unsupported` if the type of message received from user is not supported by the channel.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
