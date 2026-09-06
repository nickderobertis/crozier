

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_param_assistant_content import ChatCompletionMessageParamAssistantContent
from .chat_completion_message_param_assistant_function_call import ChatCompletionMessageParamAssistantFunctionCall
from .chat_completion_message_param_developer_content import ChatCompletionMessageParamDeveloperContent
from .chat_completion_message_param_system_content import ChatCompletionMessageParamSystemContent
from .chat_completion_message_param_tool_content import ChatCompletionMessageParamToolContent
from .chat_completion_message_param_user_content import ChatCompletionMessageParamUserContent
from .chat_completion_message_reasoning import ChatCompletionMessageReasoning
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall


class ChatCompletionMessageParam_System(UniversalBaseModel):
    role: typing.Literal["system"] = "system"
    content: typing.Optional[ChatCompletionMessageParamSystemContent] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionMessageParam_User(UniversalBaseModel):
    role: typing.Literal["user"] = "user"
    content: typing.Optional[ChatCompletionMessageParamUserContent] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionMessageParam_Assistant(UniversalBaseModel):
    role: typing.Literal["assistant"] = "assistant"
    content: typing.Optional[ChatCompletionMessageParamAssistantContent] = None
    function_call: typing.Optional[ChatCompletionMessageParamAssistantFunctionCall] = None
    name: typing.Optional[str] = None
    tool_calls: typing.Optional[typing.List[ChatCompletionMessageToolCall]] = None
    reasoning: typing.Optional[typing.List[ChatCompletionMessageReasoning]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionMessageParam_Tool(UniversalBaseModel):
    role: typing.Literal["tool"] = "tool"
    content: typing.Optional[ChatCompletionMessageParamToolContent] = None
    tool_call_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionMessageParam_Function(UniversalBaseModel):
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


class ChatCompletionMessageParam_Developer(UniversalBaseModel):
    role: typing.Literal["developer"] = "developer"
    content: typing.Optional[ChatCompletionMessageParamDeveloperContent] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ChatCompletionMessageParam_Model(UniversalBaseModel):
    role: typing.Literal["model"] = "model"
    content: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ChatCompletionMessageParam = typing_extensions.Annotated[
    typing.Union[
        ChatCompletionMessageParam_System,
        ChatCompletionMessageParam_User,
        ChatCompletionMessageParam_Assistant,
        ChatCompletionMessageParam_Tool,
        ChatCompletionMessageParam_Function,
        ChatCompletionMessageParam_Developer,
        ChatCompletionMessageParam_Model,
    ],
    pydantic.Field(discriminator="role"),
]
