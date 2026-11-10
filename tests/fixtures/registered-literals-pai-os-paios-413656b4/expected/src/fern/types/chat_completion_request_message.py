

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_tool_calls import ChatCompletionMessageToolCalls
from .chat_completion_request_assistant_message_function_call import ChatCompletionRequestAssistantMessageFunctionCall
from .chat_completion_request_user_message_content import ChatCompletionRequestUserMessageContent


class ChatCompletionRequestMessage_System(UniversalBaseModel):
    role: typing.Literal["system"] = "system"
    content: str
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessage_User(UniversalBaseModel):
    role: typing.Literal["user"] = "user"
    content: ChatCompletionRequestUserMessageContent
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessage_Assistant(UniversalBaseModel):
    role: typing.Literal["assistant"] = "assistant"
    content: typing.Optional[str] = None
    name: typing.Optional[str] = None
    tool_calls: typing.Optional[ChatCompletionMessageToolCalls] = None
    function_call: typing.Optional[ChatCompletionRequestAssistantMessageFunctionCall] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessage_Tool(UniversalBaseModel):
    role: typing.Literal["tool"] = "tool"
    content: str
    tool_call_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessage_Function(UniversalBaseModel):
    role: typing.Literal["function"] = "function"
    content: typing.Optional[str] = None
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionRequestMessage = typing_extensions.Annotated[
    typing.Union[
        ChatCompletionRequestMessage_System,
        ChatCompletionRequestMessage_User,
        ChatCompletionRequestMessage_Assistant,
        ChatCompletionRequestMessage_Tool,
        ChatCompletionRequestMessage_Function,
    ],
    pydantic.Field(discriminator="role"),
]
