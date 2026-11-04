

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_message_content import ChatMessageContent
from .chat_message_role import ChatMessageRole


class ChatMessage(UniversalBaseModel):
    role: ChatMessageRole
    content: ChatMessageContent

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
