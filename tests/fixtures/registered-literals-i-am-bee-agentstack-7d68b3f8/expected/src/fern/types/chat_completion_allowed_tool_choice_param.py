

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_allowed_tool_choice_param_type import ChatCompletionAllowedToolChoiceParamType
from .chat_completion_allowed_tools_param import ChatCompletionAllowedToolsParam


class ChatCompletionAllowedToolChoiceParam(UniversalBaseModel):
    """
    Constrains the tools available to the model to a pre-defined set.
    """

    allowed_tools: ChatCompletionAllowedToolsParam
    type: ChatCompletionAllowedToolChoiceParamType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
