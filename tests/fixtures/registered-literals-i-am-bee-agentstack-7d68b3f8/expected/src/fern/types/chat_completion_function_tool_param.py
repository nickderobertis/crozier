

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_function_tool_param_type import ChatCompletionFunctionToolParamType
from .function_definition import FunctionDefinition


class ChatCompletionFunctionToolParam(UniversalBaseModel):
    """
    A function tool that can be used to generate a response.
    """

    function: FunctionDefinition
    type: ChatCompletionFunctionToolParamType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
