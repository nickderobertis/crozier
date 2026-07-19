

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_message_function_tool_call_output_type import ChatCompletionMessageFunctionToolCallOutputType
from .function_output import FunctionOutput


class ChatCompletionMessageFunctionToolCallOutput(UniversalBaseModel):
    """
    A call to a function tool created by the model.
    """

    id: str
    function: FunctionOutput
    type: ChatCompletionMessageFunctionToolCallOutputType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
