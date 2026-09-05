

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_completion_content_part_text_cache_control import ChatCompletionContentPartTextCacheControl
from .chat_completion_content_part_text_type import ChatCompletionContentPartTextType


class ChatCompletionContentPartText(UniversalBaseModel):
    text: typing.Optional[str] = None
    type: ChatCompletionContentPartTextType
    cache_control: typing.Optional[ChatCompletionContentPartTextCacheControl] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
