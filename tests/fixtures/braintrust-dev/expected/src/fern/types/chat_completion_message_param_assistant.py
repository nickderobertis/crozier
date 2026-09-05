

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_param_assistant_content import ChatCompletionMessageParamAssistantContent
from .chat_completion_message_param_assistant_function_call import ChatCompletionMessageParamAssistantFunctionCall
from .chat_completion_message_reasoning import ChatCompletionMessageReasoning
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall


class ChatCompletionMessageParamAssistant(UniversalBaseModel):
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
