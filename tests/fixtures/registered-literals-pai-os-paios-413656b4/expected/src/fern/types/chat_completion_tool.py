

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_tool_type import ChatCompletionToolType
from .function_object import FunctionObject


class ChatCompletionTool(UniversalBaseModel):
    type: ChatCompletionToolType = pydantic.Field()
    """
    The type of the tool. Currently, only `function` is supported.
    """

    function: FunctionObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
