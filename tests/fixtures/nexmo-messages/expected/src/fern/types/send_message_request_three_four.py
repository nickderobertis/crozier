

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_messenger import ChannelOptionsMessenger
from .file_message_type import FileMessageType
from .send_message_request_three_four_file import SendMessageRequestThreeFourFile


class SendMessageRequestThreeFour(ChannelOptionsMessenger, BaseMessageType):
    file: typing.Optional[SendMessageRequestThreeFourFile] = None
    message_type: typing.Optional[FileMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `file` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
