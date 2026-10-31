

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_response_message_role import ChatResponseMessageRole
from .tool_call import ToolCall


class ChatResponseMessage(UniversalBaseModel):
    role: typing.Optional[ChatResponseMessageRole] = pydantic.Field(default=None)
    """
    Always `assistant` for model responses
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Assistant message text
    """

    thinking: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional deliberate thinking trace when `think` is enabled
    """

    tool_calls: typing.Optional[typing.List[ToolCall]] = pydantic.Field(default=None)
    """
    Tool calls requested by the assistant
    """

    images: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Optional base64-encoded images in the response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
