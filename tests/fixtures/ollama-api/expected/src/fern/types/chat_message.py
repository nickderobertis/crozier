

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_message_role import ChatMessageRole
from .tool_call import ToolCall


class ChatMessage(UniversalBaseModel):
    role: ChatMessageRole = pydantic.Field()
    """
    Author of the message.
    """

    content: str = pydantic.Field()
    """
    Message text content
    """

    images: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional list of inline images for multimodal models
    """

    tool_calls: typing.Optional[typing.List[ToolCall]] = pydantic.Field(default=None)
    """
    Tool call requests produced by the model
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
