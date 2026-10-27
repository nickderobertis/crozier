

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_message_from_application import ChatMessageFromApplication
from .chat_message_from_device import ChatMessageFromDevice
from .chat_message_from_user import ChatMessageFromUser


class ChatMessageFrom(UniversalBaseModel):
    application: typing.Optional[ChatMessageFromApplication] = None
    device: typing.Optional[ChatMessageFromDevice] = None
    user: typing.Optional[ChatMessageFromUser] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
