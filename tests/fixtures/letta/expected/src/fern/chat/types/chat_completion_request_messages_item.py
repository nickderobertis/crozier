

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.audio import Audio
from ...types.chat_completion_assistant_message_param_content import ChatCompletionAssistantMessageParamContent
from ...types.chat_completion_assistant_message_param_tool_calls_item import (
    ChatCompletionAssistantMessageParamToolCallsItem,
)
from ...types.chat_completion_developer_message_param_content import ChatCompletionDeveloperMessageParamContent
from ...types.chat_completion_system_message_param_content import ChatCompletionSystemMessageParamContent
from ...types.chat_completion_tool_message_param_content import ChatCompletionToolMessageParamContent
from ...types.chat_completion_user_message_param_content import ChatCompletionUserMessageParamContent
from ...types.function_call_input import FunctionCallInput


class ChatCompletionRequestMessagesItem_Developer(UniversalBaseModel):
    role: typing.Literal["developer"] = "developer"
    content: ChatCompletionDeveloperMessageParamContent
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessagesItem_System(UniversalBaseModel):
    role: typing.Literal["system"] = "system"
    content: ChatCompletionSystemMessageParamContent
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessagesItem_User(UniversalBaseModel):
    role: typing.Literal["user"] = "user"
    content: ChatCompletionUserMessageParamContent
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessagesItem_Assistant(UniversalBaseModel):
    role: typing.Literal["assistant"] = "assistant"
    audio: typing.Optional[Audio] = None
    content: typing.Optional[ChatCompletionAssistantMessageParamContent] = None
    function_call: typing.Optional[FunctionCallInput] = None
    name: typing.Optional[str] = None
    refusal: typing.Optional[str] = None
    tool_calls: typing.Optional[typing.List[ChatCompletionAssistantMessageParamToolCallsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessagesItem_Tool(UniversalBaseModel):
    role: typing.Literal["tool"] = "tool"
    content: ChatCompletionToolMessageParamContent
    tool_call_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionRequestMessagesItem_Function(UniversalBaseModel):
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


ChatCompletionRequestMessagesItem = typing_extensions.Annotated[
    typing.Union[
        ChatCompletionRequestMessagesItem_Developer,
        ChatCompletionRequestMessagesItem_System,
        ChatCompletionRequestMessagesItem_User,
        ChatCompletionRequestMessagesItem_Assistant,
        ChatCompletionRequestMessagesItem_Tool,
        ChatCompletionRequestMessagesItem_Function,
    ],
    pydantic.Field(discriminator="role"),
]
