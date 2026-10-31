

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_call import ToolCall


class ChatStreamEventMessage(UniversalBaseModel):
    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    Role of the message for this chunk
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    Partial assistant message text
    """

    thinking: typing.Optional[str] = pydantic.Field(default=None)
    """
    Partial thinking text when `think` is enabled
    """

    tool_calls: typing.Optional[typing.List[ToolCall]] = pydantic.Field(default=None)
    """
    Partial tool calls, if any
    """

    images: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Partial base64-encoded images, when present
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
