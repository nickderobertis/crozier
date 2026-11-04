

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_tool_message_param_content import ChatCompletionToolMessageParamContent


class ChatCompletionToolMessageParam(UniversalBaseModel):
    content: ChatCompletionToolMessageParamContent
    tool_call_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
