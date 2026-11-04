

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_allowed_tools_param_mode import ChatCompletionAllowedToolsParamMode


class ChatCompletionAllowedToolsParam(UniversalBaseModel):
    """
    Constrains the tools available to the model to a pre-defined set.
    """

    mode: ChatCompletionAllowedToolsParamMode
    tools: typing.List[typing.Dict[str, typing.Any]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
