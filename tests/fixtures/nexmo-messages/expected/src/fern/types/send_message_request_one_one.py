

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_message_type import BaseMessageType
from .channel_options_mms import ChannelOptionsMms
from .send_message_request_one_one_vcard import SendMessageRequestOneOneVcard
from .v_card_message_type import VCardMessageType


class SendMessageRequestOneOne(ChannelOptionsMms, BaseMessageType):
    vcard: typing.Optional[SendMessageRequestOneOneVcard] = None
    message_type: typing.Optional[VCardMessageType] = pydantic.Field(default=None)
    """
    The type of message to send. You must provide `vcard` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
