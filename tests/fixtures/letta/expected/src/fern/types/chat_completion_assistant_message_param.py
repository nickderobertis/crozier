

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio import Audio
from .chat_completion_assistant_message_param_content import ChatCompletionAssistantMessageParamContent
from .chat_completion_assistant_message_param_tool_calls_item import ChatCompletionAssistantMessageParamToolCallsItem
from .function_call_input import FunctionCallInput


class ChatCompletionAssistantMessageParam(UniversalBaseModel):
    """
    Messages sent by the model in response to user messages.
    """

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
