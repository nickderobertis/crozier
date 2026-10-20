

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .message_status_base import MessageStatusBase
from .message_status_sms_channel import MessageStatusSmsChannel


class MessageStatusSms(MessageStatusBase):
    channel: MessageStatusSmsChannel = pydantic.Field()
    """
    The channel sending to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
