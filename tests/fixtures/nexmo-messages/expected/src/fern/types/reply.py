

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .reply_message_type import ReplyMessageType
from .reply_reply import ReplyReply


class Reply(BaseMessageType):
    message_type: typing.Optional[ReplyMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `custom` in this field.
    """

    reply: ReplyReply

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
