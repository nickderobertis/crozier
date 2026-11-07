

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_content_part_text_param_type import ChatCompletionContentPartTextParamType


class ChatCompletionContentPartTextParam(UniversalBaseModel):
    """
    Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).
    """

    text: str
    type: ChatCompletionContentPartTextParamType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
